#!/usr/bin/env python3
"""
Check TFDA (Taiwan FDA) open data for new or changed drug licenses.
Creates GitHub Issues when changes are detected.
"""

import hashlib
import json
import os
import zipfile
from datetime import datetime
from io import BytesIO
from pathlib import Path

import requests

from github_utils import create_issue, issue_exists, close_older_tfda_issues

# Configuration
# New URL format as of 2026 (old URL returned 404)
TFDA_DATA_URL = "https://data.fda.gov.tw/data/opendata/export/36/json"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "tfda_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/TwTxGNN")


def load_cache() -> dict:
    """Load the cache of previously seen TFDA data."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "data_hash": None, "drug_licenses": {}}


def save_cache(cache: dict):
    """Save the cache."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    cache["last_check"] = datetime.now().isoformat()
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def load_drug_list() -> list:
    """Load the drug list."""
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["drugs"]


def download_tfda_data() -> tuple:
    """Download and extract TFDA data. Returns (data_list, content_hash)."""
    print("Downloading TFDA data...")

    try:
        response = requests.get(TFDA_DATA_URL, timeout=120)
        response.raise_for_status()

        content_hash = hashlib.sha256(response.content).hexdigest()

        # Check if it's a ZIP file
        if response.content[:2] == b'PK':
            print("Extracting ZIP file...")
            with zipfile.ZipFile(BytesIO(response.content)) as zf:
                # Find JSON file in the archive
                for name in zf.namelist():
                    if name.endswith('.json'):
                        with zf.open(name) as f:
                            data = json.load(f)
                            return data, content_hash
        else:
            # Try to parse as JSON directly
            data = response.json()
            return data, content_hash

    except requests.RequestException as e:
        print(f"Error downloading TFDA data: {e}")
        return [], None
    except (json.JSONDecodeError, zipfile.BadZipFile) as e:
        print(f"Error parsing TFDA data: {e}")
        return [], None

    return [], None


def find_drug_licenses(tfda_data: list, drug_name: str) -> list:
    """Find all licenses for a specific drug."""
    licenses = []
    drug_name_lower = drug_name.lower()

    for item in tfda_data:
        # Check multiple fields for drug name match
        eng_name = str(item.get("英文品名", "")).lower()
        cn_name = str(item.get("中文品名", "")).lower()
        ingredients = str(item.get("成分", "")).lower()

        if drug_name_lower in eng_name or drug_name_lower in ingredients:
            licenses.append({
                "license_no": item.get("許可證字號", ""),
                "cn_name": item.get("中文品名", ""),
                "eng_name": item.get("英文品名", ""),
                "form": item.get("劑型", ""),
                "indication": item.get("適應症", ""),
                "manufacturer": item.get("製造商名稱", ""),
                "status": item.get("許可證狀態", "")
            })

    return licenses


def compare_licenses(old_licenses: list, new_licenses: list) -> dict:
    """Compare old and new licenses to find changes."""
    old_by_no = {lic["license_no"]: lic for lic in old_licenses}
    new_by_no = {lic["license_no"]: lic for lic in new_licenses}

    added = [new_by_no[no] for no in new_by_no if no not in old_by_no]
    removed = [old_by_no[no] for no in old_by_no if no not in new_by_no]

    changed = []
    for no in old_by_no:
        if no in new_by_no:
            if old_by_no[no] != new_by_no[no]:
                changed.append({
                    "old": old_by_no[no],
                    "new": new_by_no[no]
                })

    return {
        "added": added,
        "removed": removed,
        "changed": changed
    }


def create_github_issue(drug_name: str, changes: dict):
    """Create a GitHub Issue for TFDA changes."""
    total_changes = len(changes["added"]) + len(changes["removed"]) + len(changes["changed"])
    title = f"🏥 TFDA 許可證變更：{drug_name} ({total_changes} 筆)"

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue for {drug_name}")
        if changes["added"]:
            print(f"  New licenses: {len(changes['added'])}")
        if changes["removed"]:
            print(f"  Removed licenses: {len(changes['removed'])}")
        if changes["changed"]:
            print(f"  Changed licenses: {len(changes['changed'])}")
        return

    # Close older issues for this drug before creating a new one
    closed_count = close_older_tfda_issues(drug_name)
    if closed_count > 0:
        print(f"  → Closed {closed_count} older issue(s) for {drug_name}")

    # Format license details
    sections = []

    if changes["added"]:
        sections.append("### 新增許可證\n")
        for lic in changes["added"]:
            sections.append(
                f"- **{lic['license_no']}** {lic['cn_name']}\n"
                f"  - 劑型: {lic['form']}\n"
                f"  - 適應症: {lic['indication'][:100]}...\n"
            )

    if changes["removed"]:
        sections.append("\n### 移除/註銷許可證\n")
        for lic in changes["removed"]:
            sections.append(f"- **{lic['license_no']}** {lic['cn_name']}\n")

    if changes["changed"]:
        sections.append("\n### 許可證變更\n")
        for change in changes["changed"]:
            sections.append(
                f"- **{change['new']['license_no']}** {change['new']['cn_name']}\n"
                f"  - 狀態: {change['old']['status']} → {change['new']['status']}\n"
            )

    evidence_type = []
    if changes["added"]:
        evidence_type.append("新許可證")
    if changes["removed"] or changes["changed"]:
        evidence_type.append("許可證變更")

    body = f"""## 🔬 自動偵測到 TFDA 許可證變更

此 Issue 由 GitHub Actions 自動建立。

### 藥物名稱
{drug_name}

### 資料來源
TFDA (衛福部食藥署)

### 證據類型
{', '.join(evidence_type)}

### 詳細資訊
{"".join(sections)}

### 建議行動
- [ ] 檢視許可證變更內容
- [ ] 更新藥物報告的台灣上市資訊
- [ ] 確認適應症是否有變更

---
*自動偵測時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Create the issue with deduplication check
    labels = ["auto-detected", "needs-review", "tfda"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("TFDA Evidence Checker")
    print(f"Started at: {datetime.now().isoformat()}")
    print("=" * 60)

    # Load data
    cache = load_cache()
    drugs = load_drug_list()

    print(f"Loaded {len(drugs)} drugs from drug list")
    print(f"Last check: {cache.get('last_check', 'Never')}")
    print(f"Previous data hash: {cache.get('data_hash', 'None')}")

    # Download current TFDA data
    tfda_data, data_hash = download_tfda_data()

    if not tfda_data:
        print("Failed to download TFDA data. Exiting.")
        return

    print(f"Downloaded {len(tfda_data)} license records")
    print(f"Current data hash: {data_hash}")

    # Check if data has changed at all
    if data_hash == cache.get("data_hash"):
        print("TFDA data unchanged since last check. No updates needed.")
        cache["last_check"] = datetime.now().isoformat()
        save_cache(cache)
        return

    # Check each drug for changes
    new_findings = []
    cached_licenses = cache.get("drug_licenses", {})

    for i, drug in enumerate(drugs):
        drug_name = drug["name"]

        if (i + 1) % 20 == 0:
            print(f"[{i+1}/{len(drugs)}] Processing...")

        # Find current licenses
        current_licenses = find_drug_licenses(tfda_data, drug_name)

        if not current_licenses:
            continue

        # Compare with cached licenses
        old_licenses = cached_licenses.get(drug_name, [])
        changes = compare_licenses(old_licenses, current_licenses)

        has_changes = changes["added"] or changes["removed"] or changes["changed"]

        # Skip if this is initial discovery (no previous cache for this drug)
        # Only report actual changes, not initial discovery of existing licenses
        is_initial_discovery = not old_licenses and current_licenses

        # Skip if all licenses were "removed" - likely API/data error
        all_removed = old_licenses and not current_licenses
        if all_removed:
            print(f"  Warning: All licenses removed for {drug_name} - likely data error, skipping")
            continue

        # Only report if there are meaningful changes (not just 1-2 minor updates)
        total_changes = len(changes["added"]) + len(changes["removed"]) + len(changes["changed"])
        is_significant = total_changes >= 1  # Can adjust threshold if needed

        if has_changes and not is_initial_discovery and is_significant:
            print(f"  Changes found for {drug_name}:")
            print(f"    Added: {len(changes['added'])}, Removed: {len(changes['removed'])}, Changed: {len(changes['changed'])}")
            new_findings.append({
                "drug": drug_name,
                "changes": changes
            })
        elif is_initial_discovery:
            print(f"  Initial discovery for {drug_name}: {len(current_licenses)} licenses (no issue created)")

        # Update cached licenses
        cached_licenses[drug_name] = current_licenses

    # Update cache
    cache["data_hash"] = data_hash
    cache["drug_licenses"] = cached_licenses
    save_cache(cache)

    # Create issues for findings
    print("\n" + "=" * 60)
    print("Creating Issues for TFDA Changes")
    print("=" * 60)

    if new_findings:
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["changes"])
    else:
        print("No license changes detected.")

    print(f"\nCompleted at: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
