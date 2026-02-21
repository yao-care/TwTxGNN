#!/usr/bin/env python3
"""
GitHub API utilities for TwTxGNN evidence checking scripts.
Provides deduplication and issue management functions.
"""

import os
import requests
from typing import Optional

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
