#!/usr/bin/env python3
"""
GitHub API utilities for TwTxGNN evidence checking scripts.
Provides deduplication and issue management functions.
"""

import os
import re
import requests
from typing import Optional, List

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/TwTxGNN")

def get_headers() -> dict:
    """Get GitHub API headers."""
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def issue_exists(title: str, state: str = "all") -> bool:
    """
    Check if an issue with the given title already exists.

    Args:
        title: The exact issue title to search for
        state: "open", "closed", or "all" (default: "all")

    Returns:
        True if an issue with this title exists, False otherwise
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would check for existing issue: {title}")
        return False

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"

    # Search for issues with exact title match
    # GitHub API doesn't support exact title search, so we fetch and filter
    params = {
        "state": state,
        "labels": "auto-detected",
        "per_page": 100
    }

    try:
        response = requests.get(url, headers=get_headers(), params=params, timeout=30)
        response.raise_for_status()
        issues = response.json()

        # Check for exact title match
        for issue in issues:
            if issue.get("title") == title:
                print(f"  → Issue already exists: #{issue['number']} - {title}")
                return True

        return False

    except requests.RequestException as e:
        print(f"Warning: Could not check for existing issues: {e}")
        # If we can't check, assume it doesn't exist to avoid blocking
        return False


def find_existing_tfda_issues(drug_name: str, state: str = "open") -> List[dict]:
    """
    Find existing TFDA issues for a specific drug.

    Args:
        drug_name: The drug name to search for
        state: "open", "closed", or "all" (default: "open")

    Returns:
        List of matching issues (sorted by number, newest first)
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would search for TFDA issues: {drug_name}")
        return []

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    params = {
        "state": state,
        "labels": "tfda",
        "per_page": 100
    }

    try:
        response = requests.get(url, headers=get_headers(), params=params, timeout=30)
        response.raise_for_status()
        issues = response.json()

        # Filter issues matching the drug name pattern
        # Title format: 🏥 TFDA 許可證變更：DrugName (N 筆)
        matching = []
        drug_name_lower = drug_name.lower()
        for issue in issues:
            title = issue.get("title", "")
            match = re.search(r'：(.+?)\s*\(', title)
            if match:
                issue_drug = match.group(1).strip().lower()
                if issue_drug == drug_name_lower:
                    matching.append({
                        "number": issue["number"],
                        "title": issue["title"],
                        "url": issue["html_url"]
                    })

        # Sort by issue number (newest first)
        matching.sort(key=lambda x: x["number"], reverse=True)
        return matching

    except requests.RequestException as e:
        print(f"Warning: Could not search for existing issues: {e}")
        return []


def close_issue(issue_number: int, comment: str = None) -> bool:
    """
    Close a GitHub issue with an optional comment.

    Args:
        issue_number: The issue number to close
        comment: Optional comment to add before closing

    Returns:
        True if successful, False otherwise
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would close issue #{issue_number}")
        return True

    try:
        # Add comment if provided
        if comment:
            comment_url = f"https://api.github.com/repos/{GITHUB_REPO}/issues/{issue_number}/comments"
            requests.post(comment_url, headers=get_headers(), json={"body": comment}, timeout=30)

        # Close the issue
        url = f"https://api.github.com/repos/{GITHUB_REPO}/issues/{issue_number}"
        response = requests.patch(url, headers=get_headers(), json={"state": "closed"}, timeout=30)
        response.raise_for_status()
        print(f"  → Closed issue #{issue_number}")
        return True

    except requests.RequestException as e:
        print(f"Error closing issue #{issue_number}: {e}")
        return False


def close_older_tfda_issues(drug_name: str) -> int:
    """
    Close older TFDA issues for a drug, keeping only the latest.

    Args:
        drug_name: The drug name to process

    Returns:
        Number of issues closed
    """
    existing = find_existing_tfda_issues(drug_name, state="open")

    if len(existing) <= 1:
        return 0

    # Keep the first (newest), close the rest
    closed_count = 0
    for issue in existing[1:]:
        comment = f"🤖 自動關閉：已有更新的 issue #{existing[0]['number']} 追蹤此藥物的許可證變更。"
        if close_issue(issue["number"], comment):
            closed_count += 1

    return closed_count


def create_issue(title: str, body: str, labels: list) -> Optional[str]:
    """
    Create a GitHub issue with deduplication check.

    Args:
        title: Issue title
        body: Issue body (markdown)
        labels: List of label names

    Returns:
        Issue URL if created, None if skipped or failed
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue: {title}")
        return None

    # Check if issue already exists
    if issue_exists(title):
        print(f"  → Skipping duplicate issue: {title}")
        return None

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    payload = {
        "title": title,
        "body": body,
        "labels": labels
    }

    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
        response.raise_for_status()
        issue_url = response.json().get("html_url")
        print(f"  → Created issue: {issue_url}")
        return issue_url

    except requests.RequestException as e:
        print(f"Error creating issue: {e}")
        return None
