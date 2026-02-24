#!/usr/bin/env python3
"""
Check PubMed for new publications related to our drug list.
Creates GitHub Issues when new papers are found.
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path

import requests

from github_utils import create_issue, issue_exists, close_older_pubmed_issues

# Configuration
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "pubmed_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/TwTxGNN")
NCBI_API_KEY = os.environ.get("NCBI_API_KEY")  # Optional, for higher rate limits
RATE_LIMIT_DELAY = 0.4 if NCBI_API_KEY else 1.0  # seconds between API calls


def load_cache() -> dict:
    """Load the cache of previously seen PMIDs."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "seen_pmids": {}}


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


def search_pubmed(drug_name: str, indication: str = "", days_back: int = 7) -> list:
    """Search PubMed for recent publications."""
    # Build search query
    query_parts = [f'"{drug_name}"[Title/Abstract]']
    if indication:
        # Clean up indication text
        indication = indication.split("(")[0].strip()  # Remove parenthetical notes
        if indication and len(indication) > 3:
            query_parts.append(f'"{indication}"[Title/Abstract]')

    query = " AND ".join(query_parts)

    params = {
        "db": "pubmed",
        "term": query,
        "datetype": "edat",  # Entry date
        "reldate": days_back,  # Last N days
        "retmode": "json",
        "retmax": 50,
        "sort": "date"
    }

    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    try:
        response = requests.get(ESEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        id_list = data.get("esearchresult", {}).get("idlist", [])
        return id_list
    except requests.RequestException as e:
        print(f"Error searching PubMed for {drug_name}: {e}")
        return []


def get_paper_details(pmids: list) -> list:
    """Get details for a list of PMIDs."""
    if not pmids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json"
    }

    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    try:
        response = requests.get(ESUMMARY_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        result = data.get("result", {})
        papers = []

        for pmid in pmids:
            paper_data = result.get(pmid, {})
            if paper_data and "title" in paper_data:
                papers.append({
                    "pmid": pmid,
                    "title": paper_data.get("title", ""),
                    "source": paper_data.get("source", ""),
                    "pubdate": paper_data.get("pubdate", ""),
                    "authors": [a.get("name", "") for a in paper_data.get("authors", [])[:3]]
                })

        return papers
    except requests.RequestException as e:
        print(f"Error getting paper details: {e}")
        return []


def create_github_issue(drug_name: str, new_papers: list):
    """Create a GitHub Issue for new papers found."""
    title = f"📚 新文獻：{drug_name} ({len(new_papers)} 篇)"

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue for {drug_name} with {len(new_papers)} new papers")
        for paper in new_papers[:3]:
            print(f"  - PMID {paper['pmid']}: {paper['title'][:60]}...")
        return

    # Close older issues for this drug before creating a new one
    closed_count = close_older_pubmed_issues(drug_name)
    if closed_count > 0:
        print(f"  → Closed {closed_count} older issue(s) for {drug_name}")

    # Format paper details
    paper_details = []
    for paper in new_papers:
        authors = ", ".join(paper["authors"]) + (" et al." if len(paper["authors"]) >= 3 else "")
        paper_details.append(
            f"### PMID: {paper['pmid']}\n"
            f"- **標題**: {paper['title']}\n"
            f"- **期刊**: {paper['source']}\n"
            f"- **發表日期**: {paper['pubdate']}\n"
            f"- **作者**: {authors}\n"
            f"- **連結**: https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/\n"
        )

    body = f"""## 🔬 自動偵測到新學術文獻

此 Issue 由 GitHub Actions 自動建立。

### 藥物名稱
{drug_name}

### 資料來源
PubMed

### 證據類型
新學術文獻

### 詳細資訊
發現 **{len(new_papers)}** 篇新文獻：

{"".join(paper_details)}

### 建議行動
- [ ] 閱讀文獻摘要
- [ ] 評估文獻類型（RCT、觀察性研究、案例報告等）
- [ ] 評估是否需要更新藥物報告證據等級
- [ ] 新增文獻資訊到報告

---
*自動偵測時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Create the issue with deduplication check
    labels = ["auto-detected", "needs-review", "pubmed"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("PubMed Evidence Checker")
    print(f"Started at: {datetime.now().isoformat()}")
    print(f"NCBI API Key: {'Configured' if NCBI_API_KEY else 'Not configured (slower rate limit)'}")
    print("=" * 60)

    # Load data
    cache = load_cache()
    drugs = load_drug_list()

    print(f"Loaded {len(drugs)} drugs from drug list")
    print(f"Last check: {cache.get('last_check', 'Never')}")

    # Check each drug
    new_findings = []
    seen_pmids = cache.get("seen_pmids", {})

    for i, drug in enumerate(drugs):
        drug_name = drug["name"]
        indication = drug.get("predicted_indication", "")

        print(f"\n[{i+1}/{len(drugs)}] Checking: {drug_name}")

        pmids = search_pubmed(drug_name, indication, days_back=7)
        time.sleep(RATE_LIMIT_DELAY)

        if not pmids:
            continue

        # Filter to truly new papers
        drug_seen = seen_pmids.get(drug_name, [])
        new_pmids = [p for p in pmids if p not in drug_seen]

        if new_pmids:
            # Get paper details
            papers = get_paper_details(new_pmids)
            time.sleep(RATE_LIMIT_DELAY)

            if papers:
                print(f"  Found {len(papers)} new papers!")
                new_findings.append({
                    "drug": drug_name,
                    "papers": papers
                })

            # Update seen PMIDs
            drug_seen.extend(new_pmids)

        seen_pmids[drug_name] = drug_seen

    # Update cache
    cache["seen_pmids"] = seen_pmids
    save_cache(cache)

    # Create issues for new findings
    print("\n" + "=" * 60)
    print("Creating Issues for New Findings")
    print("=" * 60)

    if new_findings:
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["papers"])
    else:
        print("No new papers found.")

    print(f"\nCompleted at: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
