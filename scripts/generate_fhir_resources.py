#!/usr/bin/env python3
"""
Generate FHIR R4 resources from TwTxGNN drug prediction data.

This script reads the search-index.json and generates:
- MedicationKnowledge resources for each drug
- ClinicalUseDefinition resources for each predicted indication
- A Bundle containing all resources
- A CapabilityStatement (metadata)
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from twtxgnn.regulatory import withdrawn as W  # noqa: E402  重審撤回的預測（2026-11-03）


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


DRUGS_DIR = Path(__file__).resolve().parent.parent / "docs" / "_drugs"


def _page(slug: str, drugs_dir: Path = DRUGS_DIR) -> Path | None:
    for cand in dict.fromkeys([slug, slug.replace("-", "_"), slug.replace("_", "-")]):
        f = drugs_dir / f"{cand}.md"
        if f.exists():
            return f
    return None


def page_level(slug: str, drugs_dir: Path = DRUGS_DIR) -> str | None:
    """藥物頁頁首的 evidence_level（L1–L5 或 N/A；2026-11-03 起 MedicationKnowledge 的等級以頁首為準）。"""
    f = _page(slug, drugs_dir)
    if not f:
        return None
    m = re.search(r"^evidence_level:[ \t]*(L[1-5]|N/A)[ \t]*$", f.read_text(encoding="utf-8")[:3000], re.M)
    return m.group(1) if m else None


def page_hidden(slug: str, drugs_dir: Path = DRUGS_DIR) -> bool:
    """藥物頁是 noindex／search_exclude／轉址頁：不進 FHIR（跟 search-index 一致，2026-11-03 用戶決定）。"""
    f = _page(slug, drugs_dir)
    if not f:
        return False
    text = f.read_text(encoding="utf-8", errors="replace")
    return bool(re.search(r"^(noindex|search_exclude):[ \t]*true", text[:3000], re.M | re.I)) or 'http-equiv="refresh"' in text


def create_medication_knowledge(drug: dict, base_url: str) -> dict:
    """Create a FHIR MedicationKnowledge resource for a drug."""
    resource = {
        "resourceType": "MedicationKnowledge",
        "id": drug["slug"],
        "meta": {
            "profile": ["http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"]
        },
        "status": "active",
        "code": {
            "coding": [
                {
                    "system": f"{base_url}/drugs",
                    "code": drug["slug"],
                    "display": drug["name"]
                }
            ],
            "text": drug["name"]
        },
        "intendedJurisdiction": [
            {
                "coding": [
                    {
                        "system": "urn:iso:std:iso:3166",
                        "code": "TW",
                        "display": "Taiwan"
                    }
                ]
            }
        ],
        "extension": [
            {
                "url": f"{base_url}/fhir/StructureDefinition/evidence-level",
                "valueCode": page_level(drug["slug"]) or drug.get("level", "L5")
            }
        ]
    }

    # Add original indication if available
    if drug.get("original"):
        resource["indicationGuideline"] = [
            {
                "indication": [
                    {
                        "reference": {
                            "display": drug["original"][:200]  # Truncate if too long
                        }
                    }
                ]
            }
        ]

    # Add brand names if available
    if drug.get("brands"):
        resource["synonym"] = drug["brands"]

    return resource


def create_clinical_use_definition(
    drug: dict,
    indication: dict,
    base_url: str
) -> dict:
    """Create a FHIR ClinicalUseDefinition resource for a predicted indication."""
    ind_slug = slugify(indication["name"])
    resource_id = f"{drug['slug']}-{ind_slug}"[:64]  # Limit ID length

    resource = {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "meta": {
            "profile": ["http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition"]
        },
        "type": "indication",
        "status": {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/publication-status",
                    "code": "draft",
                    "display": "Draft"
                }
            ]
        },
        "subject": [
            {
                "reference": f"MedicationKnowledge/{drug['slug']}"
            }
        ],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {
                    "text": indication["name"]
                }
            }
        },
        "extension": [
            {
                "url": f"{base_url}/fhir/StructureDefinition/prediction-status",
                "valueCode": "predicted"
            },
            {
                "url": f"{base_url}/fhir/StructureDefinition/evidence-level",
                "valueCode": indication.get("level", "L5")
            },
            {
                "url": f"{base_url}/fhir/StructureDefinition/txgnn-score",
                "valueDecimal": indication.get("score", 0) / 100  # Convert to 0-1 scale
            }
        ]
    }

    return resource


def create_capability_statement(base_url: str, drug_count: int, indication_count: int) -> dict:
    """Create a FHIR CapabilityStatement (metadata)."""
    return {
        "resourceType": "CapabilityStatement",
        "id": "twtxgnn-fhir-server",
        "url": f"{base_url}/fhir/metadata",
        "version": "1.0.0",
        "name": "TwTxGNNFHIRServer",
        "title": "TwTxGNN FHIR Server",
        "status": "active",
        "experimental": True,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "TwTxGNN",
        "contact": [
            {
                "telecom": [
                    {
                        "system": "url",
                        "value": base_url
                    }
                ]
            }
        ],
        "description": f"TwTxGNN drug repurposing prediction data exposed as FHIR resources. Contains {drug_count} drugs and {indication_count} predicted indications.",
        "kind": "instance",
        "software": {
            "name": "TwTxGNN Static FHIR API",
            "version": "1.0.0"
        },
        "implementation": {
            "description": "Static FHIR resources served from GitHub Pages",
            "url": f"{base_url}/fhir"
        },
        "fhirVersion": "4.0.1",
        "format": ["application/fhir+json"],
        "rest": [
            {
                "mode": "server",
                "documentation": "Static FHIR API - read-only access to drug repurposing predictions",
                "resource": [
                    {
                        "type": "MedicationKnowledge",
                        "profile": "http://hl7.org/fhir/StructureDefinition/MedicationKnowledge",
                        "interaction": [
                            {"code": "read"}
                        ],
                        "searchParam": [
                            {
                                "name": "_id",
                                "type": "token",
                                "documentation": "Drug identifier (slug)"
                            }
                        ]
                    },
                    {
                        "type": "ClinicalUseDefinition",
                        "profile": "http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition",
                        "interaction": [
                            {"code": "read"}
                        ],
                        "searchParam": [
                            {
                                "name": "subject",
                                "type": "reference",
                                "documentation": "Reference to MedicationKnowledge"
                            }
                        ]
                    }
                ]
            }
        ]
    }


def create_bundle(entries: list, base_url: str) -> dict:
    """Create a FHIR Bundle containing all resources."""
    return {
        "resourceType": "Bundle",
        "id": "all-predictions",
        "type": "collection",
        "timestamp": datetime.now().isoformat(),
        "total": len(entries),
        "link": [
            {
                "relation": "self",
                "url": f"{base_url}/fhir/Bundle/all-predictions.json"
            }
        ],
        "entry": [
            {
                "fullUrl": f"{base_url}/fhir/{entry['resourceType']}/{entry['id']}",
                "resource": entry
            }
            for entry in entries
        ]
    }


def _cud_key(res: dict):
    """ClinicalUseDefinition → (藥 slug, 適應症名稱)。"""
    subj = (res.get("subject") or [{}])[0].get("reference", "")
    slug = subj.split("/", 1)[1] if subj.startswith("MedicationKnowledge/") else ""
    concept = ((res.get("indication") or {}).get("diseaseSymptomProcedure") or {}).get("concept") or {}
    name = concept.get("text") or next((c.get("display", "") for c in concept.get("coding") or []), "")
    return slug, name


def prune_withdrawn(output_dir: Path) -> int:
    """重審撤回的預測（docs/_data/drug_reviews.json verdict=withdraw）從 FHIR 拿掉（2026-11-03 用戶決定）：
    刪掉對應的 ClinicalUseDefinition 檔與 Bundle 內的 entry（total 同步扣掉），其他資源與欄位不動。
    MedicationKnowledge 不引用 ClinicalUseDefinition，不需改。回傳刪掉的 CUD 數。"""
    table = W.load()
    gone = set()
    for f in sorted((output_dir / "ClinicalUseDefinition").glob("*.json")):
        res = json.loads(f.read_text(encoding="utf-8"))
        if res.get("resourceType") == "ClinicalUseDefinition" and W.is_withdrawn(table, *_cud_key(res)):
            gone.add(res.get("id"))
            f.unlink()
    bpath = output_dir / "Bundle" / "all-predictions.json"
    if bpath.exists():
        bundle = json.loads(bpath.read_text(encoding="utf-8"))
        before = len(bundle.get("entry") or [])
        bundle["entry"] = [e for e in bundle.get("entry") or []
                           if not (e.get("resource", {}).get("resourceType") == "ClinicalUseDefinition"
                                   and (e["resource"].get("id") in gone or W.is_withdrawn(table, *_cud_key(e["resource"]))))]
        removed = before - len(bundle["entry"])
        if removed:
            if isinstance(bundle.get("total"), int):
                bundle["total"] -= removed
            bpath.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Pruned {len(gone)} withdrawn ClinicalUseDefinition resources")
    return len(gone)


def _dump(path: Path, obj) -> bool:
    """跟現有檔案同格式（ensure_ascii=False、indent=2、無結尾換行）寫檔；內容沒變就不寫。"""
    text = json.dumps(obj, ensure_ascii=False, indent=2)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def sync_from_files(output_dir: Path, drugs_dir: Path = DRUGS_DIR) -> dict:
    """FHIR 與頁面、實際檔案對齊（2026-11-03 用戶決定）：
    0. noindex／search_exclude／轉址頁的藥（page_hidden）：刪掉它的 MedicationKnowledge 與 ClinicalUseDefinition。
    1. MedicationKnowledge 的 evidence-level ＝ 藥物頁頁首（含 N/A）；找不到頁的不動。
    2. Bundle 依實際的 MedicationKnowledge／ClinicalUseDefinition 檔重建：既有 entry 保留順序、內容換成檔案內容，
       沒有檔案的 entry 刪除，缺的資源補在同藥最後一筆之後（整個藥都缺就接在最後）；total＝entry 數。
    3. metadata（CapabilityStatement）描述裡的藥物數、適應症數＝MedicationKnowledge／ClinicalUseDefinition 檔數。
    內容有變才改 Bundle timestamp 與 metadata date。"""
    base_url = "https://twtxgnn.yao.care"
    stats = {"mk_level_changed": [], "bundle_changed": False, "metadata_changed": False, "hidden_removed": []}
    # 0. noindex／search_exclude／轉址頁的藥：刪掉它的 MedicationKnowledge 與 ClinicalUseDefinition 檔
    for f in sorted((output_dir / "ClinicalUseDefinition").glob("*.json")):
        if page_hidden(_cud_key(json.loads(f.read_text(encoding="utf-8")))[0], drugs_dir):
            stats["hidden_removed"].append(f"ClinicalUseDefinition/{f.stem}")
            f.unlink()
    for f in sorted((output_dir / "MedicationKnowledge").glob("*.json")):
        if page_hidden(f.stem, drugs_dir):
            stats["hidden_removed"].append(f"MedicationKnowledge/{f.stem}")
            f.unlink()
    mk = {}
    for f in sorted((output_dir / "MedicationKnowledge").glob("*.json")):
        res = json.loads(f.read_text(encoding="utf-8"))
        lv = page_level(res["id"], drugs_dir)
        for ext in res.get("extension") or []:
            if ext.get("url", "").endswith("/evidence-level") and lv and ext.get("valueCode") != lv:
                stats["mk_level_changed"].append((res["id"], ext.get("valueCode"), lv))
                ext["valueCode"] = lv
        _dump(f, res)
        mk[res["id"]] = res
    cud = {}
    for f in sorted((output_dir / "ClinicalUseDefinition").glob("*.json")):
        res = json.loads(f.read_text(encoding="utf-8"))
        cud[res["id"]] = res
    files = {("MedicationKnowledge", k): v for k, v in mk.items()}
    files.update({("ClinicalUseDefinition", k): v for k, v in cud.items()})

    def drug_of(rt, res):
        return res["id"] if rt == "MedicationKnowledge" else _cud_key(res)[0]

    bpath = output_dir / "Bundle" / "all-predictions.json"
    bundle = json.loads(bpath.read_text(encoding="utf-8")) if bpath.exists() else create_bundle([], base_url)
    old_entries = bundle.get("entry") or []
    keys = [(e["resource"]["resourceType"], e["resource"]["id"]) for e in old_entries
            if (e["resource"]["resourceType"], e["resource"]["id"]) in files]
    keys = list(dict.fromkeys(keys))
    missing = sorted(set(files) - set(keys), key=lambda k: (k[0] != "MedicationKnowledge", k[1]))
    by_drug = {}
    for k in missing:
        by_drug.setdefault(drug_of(k[0], files[k]), []).append(k)
    out = []
    for i, k in enumerate(keys):
        out.append(k)
        d = drug_of(k[0], files[k])
        later = any(drug_of(x[0], files[x]) == d for x in keys[i + 1:i + 2])
        if not later and d in by_drug:
            out.extend(by_drug.pop(d))
    for d in sorted(by_drug):
        out.extend(by_drug[d])
    entries = [{"fullUrl": f"{base_url}/fhir/{rt}/{rid}", "resource": files[(rt, rid)]} for rt, rid in out]
    if entries != old_entries or bundle.get("total") != len(entries):
        bundle["entry"] = entries
        bundle["total"] = len(entries)
        bundle["timestamp"] = datetime.now().isoformat()
        stats["bundle_changed"] = _dump(bpath, bundle)
    mpath = output_dir / "metadata"
    if mpath.exists():
        meta = json.loads(mpath.read_text(encoding="utf-8"))
        desc = re.sub(r"Contains \d+ drugs and \d+ predicted indications",
                      f"Contains {len(mk)} drugs and {len(cud)} predicted indications", meta.get("description", ""))
        if desc != meta.get("description"):
            meta["description"] = desc
            meta["date"] = datetime.now().strftime("%Y-%m-%d")
            stats["metadata_changed"] = _dump(mpath, meta)
    stats.update(mk=len(mk), cud=len(cud), entries=len(entries))
    return stats


def fhir_problems(output_dir: Path, drugs_dir: Path = DRUGS_DIR) -> list[str]:
    """gate 用：MedicationKnowledge 等級＝頁首、不含 noindex／轉址頁的藥、Bundle 與檔案一致（total＝entry 數）、
    metadata 數字＝檔案數。"""
    errs = []
    mk = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in (output_dir / "MedicationKnowledge").glob("*.json")}
    cud = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in (output_dir / "ClinicalUseDefinition").glob("*.json")}
    bad = []
    for rid, res in mk.items():
        lv = page_level(rid, drugs_dir)
        got = next((e.get("valueCode") for e in res.get("extension") or [] if e.get("url", "").endswith("/evidence-level")), None)
        if lv and got != lv:
            bad.append(f"{rid}（{got}≠頁首 {lv}）")
    if bad:
        errs.append(f"MedicationKnowledge 等級與頁首不一致 {len(bad)} 個：{bad[:5]}")
    hidden = sorted({k for k in mk if page_hidden(k, drugs_dir)} | {_cud_key(v)[0] for v in cud.values() if page_hidden(_cud_key(v)[0], drugs_dir)})
    if hidden:
        errs.append(f"FHIR 含 noindex／轉址頁的藥 {len(hidden)} 個：{hidden[:5]}")
    bpath = output_dir / "Bundle" / "all-predictions.json"
    if bpath.exists():
        b = json.loads(bpath.read_text(encoding="utf-8"))
        ent = b.get("entry") or []
        files = {("MedicationKnowledge", k): v for k, v in mk.items()}
        files.update({("ClinicalUseDefinition", k): v for k, v in cud.items()})
        got = {(e["resource"]["resourceType"], e["resource"]["id"]): e["resource"] for e in ent}
        if b.get("total") != len(ent):
            errs.append(f"Bundle total={b.get('total')}，entry {len(ent)} 筆")
        if set(got) != set(files) or len(got) != len(ent):
            errs.append(f"Bundle 與資源檔不一致：缺 {len(set(files) - set(got))}、多 {len(set(got) - set(files))}、重複 {len(ent) - len(got)}")
        elif any(got[k] != files[k] for k in files):
            errs.append("Bundle 內有 entry 與資源檔內容不同")
    mpath = output_dir / "metadata"
    if mpath.exists():
        m = re.search(r"Contains (\d+) drugs and (\d+) predicted indications",
                      json.loads(mpath.read_text(encoding="utf-8")).get("description", ""))
        if not m or (int(m.group(1)), int(m.group(2))) != (len(mk), len(cud)):
            errs.append(f"metadata 寫 {m.groups() if m else '（無數字）'}，實際 MedicationKnowledge {len(mk)}、ClinicalUseDefinition {len(cud)}")
    return errs


def main():
    """Main function to generate FHIR resources."""
    # Configuration
    base_url = "https://twtxgnn.yao.care"
    project_root = Path(__file__).parent.parent
    input_file = project_root / "docs" / "data" / "search-index.json"
    output_dir = project_root / "docs" / "fhir"

    print(f"Reading search index from {input_file}")

    # Load search index
    with open(input_file, "r", encoding="utf-8") as f:
        search_index = json.load(f)

    drugs = search_index.get("drugs", [])
    print(f"Found {len(drugs)} drugs")
    withdrawn = W.load()

    # Create output directories
    (output_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (output_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)
    (output_dir / "Bundle").mkdir(parents=True, exist_ok=True)

    # Generate resources
    all_resources = []
    total_indications = 0

    for drug in drugs:
        if page_hidden(drug["slug"]):
            continue  # noindex／轉址頁的藥不進 FHIR（2026-11-03）
        # Create MedicationKnowledge
        med_knowledge = create_medication_knowledge(drug, base_url)
        all_resources.append(med_knowledge)

        # Save MedicationKnowledge
        output_file = output_dir / "MedicationKnowledge" / f"{drug['slug']}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(med_knowledge, f, ensure_ascii=False, indent=2)

        # Create ClinicalUseDefinition for each indication
        for indication in drug.get("indications", []):
            if W.is_withdrawn(withdrawn, drug["slug"], indication.get("name", "")):
                continue  # 重審撤回的預測不發布（頁面原文不動，2026-11-03）
            clinical_use = create_clinical_use_definition(drug, indication, base_url)
            all_resources.append(clinical_use)
            total_indications += 1

            # Save ClinicalUseDefinition
            output_file = output_dir / "ClinicalUseDefinition" / f"{clinical_use['id']}.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(clinical_use, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(drugs)} MedicationKnowledge resources")
    print(f"Generated {total_indications} ClinicalUseDefinition resources")

    # Create CapabilityStatement (metadata)
    capability = create_capability_statement(base_url, len(drugs), total_indications)
    with open(output_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(capability, f, ensure_ascii=False, indent=2)
    print("Generated CapabilityStatement (metadata)")

    # Create Bundle with all resources
    bundle = create_bundle(all_resources, base_url)
    with open(output_dir / "Bundle" / "all-predictions.json", "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
    print(f"Generated Bundle with {len(all_resources)} resources")

    prune_withdrawn(output_dir)  # 舊檔裡殘留的撤回預測一併清掉
    print(sync_from_files(output_dir))  # 等級對頁首、Bundle／metadata 數字對實際檔案
    print(f"\nFHIR resources generated successfully in {output_dir}")


if __name__ == "__main__":
    if "--prune-withdrawn" in sys.argv or "--sync-from-files" in sys.argv:
        # 不重產資源本身（現行 FHIR 由 kept 產生，格式與本腳本的全量重產不完全相同）：
        # --prune-withdrawn 清撤回的預測；兩者都會把 MK 等級對頁首、Bundle／metadata 對實際檔案
        _out = Path(__file__).parent.parent / "docs" / "fhir"
        if "--prune-withdrawn" in sys.argv:
            prune_withdrawn(_out)
        print(sync_from_files(_out))
    else:
        main()
