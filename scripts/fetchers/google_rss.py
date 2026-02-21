#!/usr/bin/env python3
"""
Google News RSS Fetcher

抓取 Google News 健康頻道 RSS，輸出到 data/news/google_rss.json
"""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import feedparser

# 專案根目錄
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News 健康頻道 RSS (台灣繁體中文)
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE"
    "?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
)


def generate_id(title: str, link: str) -> str:
    """產生新聞 ID（基於標題和連結的 hash）"""
    content = f"{title}:{link}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


def parse_source(entry) -> dict:
    """從 RSS entry 中提取來源資訊"""
    # Google News RSS 的 source 標籤
    source_name = "Google News"
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """解析發布時間，轉換為 ISO 8601 格式"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    # 如果解析失敗，使用當前時間
    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """清理摘要文字（移除 HTML 標籤等）"""
    import re
    # 移除 HTML 標籤
    clean = re.sub(r"<[^>]+>", "", summary)
    # 移除多餘空白
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_google_news() -> list[dict]:
    """抓取 Google News 健康頻道"""
    print(f"抓取 Google News RSS...")
    print(f"  URL: {GOOGLE_NEWS_HEALTH_RSS[:80]}...")

    feed = feedparser.parse(GOOGLE_NEWS_HEALTH_RSS)

    if feed.bozo:
        print(f"  警告: RSS 解析有問題 - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"  抓取到 {len(news_items)} 則新聞")
    return news_items


def main():
    # 確保目錄存在
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 抓取新聞
    news_items = fetch_google_news()

    # 輸出
    output = {
        "source": "google_rss",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(news_items),
        "news": news_items
    }

    output_path = DATA_DIR / "google_rss.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n輸出: {output_path}")
    print(f"  - 新聞數: {len(news_items)}")


if __name__ == "__main__":
    main()
