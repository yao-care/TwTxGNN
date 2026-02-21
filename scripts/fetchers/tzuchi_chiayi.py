#!/usr/bin/env python3
"""
嘉義慈濟醫院健康衛教新聞 Fetcher

抓取嘉義慈濟醫院健康衛教頁面，輸出到 data/news/tzuchi_chiayi.json
來源：https://chiayi.tzuchi-healthcare.org.tw/index.php/zui-xin-xiao-xi/jian-kang-wei-jiao-4
"""

import json
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# 專案根目錄
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# 嘉義慈濟醫院健康衛教頁面
BASE_URL = "https://chiayi.tzuchi-healthcare.org.tw"
NEWS_URL = f"{BASE_URL}/index.php/zui-xin-xiao-xi/jian-kang-wei-jiao-4"

# 抓取的頁數（避免抓太多舊資料）
MAX_PAGES = 2


def generate_id(title: str, link: str) -> str:
    """產生新聞 ID（基於標題和連結的 hash）"""
    content = f"{title}:{link}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


def parse_date(date_str: str) -> str:
    """解析日期字串，轉換為 ISO 8601 格式"""
    # 嘗試解析各種日期格式
    patterns = [
        r"(\d{4})-(\d{2})-(\d{2})",  # 2026-01-15
        r"(\d{4})/(\d{2})/(\d{2})",  # 2026/01/15
        r"(\d{4})年(\d{1,2})月(\d{1,2})日",  # 2026年1月15日
    ]

    for pattern in patterns:
        match = re.search(pattern, date_str)
        if match:
            year, month, day = match.groups()
            try:
                dt = datetime(int(year), int(month), int(day), tzinfo=timezone.utc)
                return dt.isoformat()
            except ValueError:
                pass

    # 解析失敗，使用當前時間
    return datetime.now(timezone.utc).isoformat()


def fetch_page(url: str) -> BeautifulSoup | None:
    """抓取頁面並解析"""
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (compatible; TwTxGNN News Monitor; "
                "+https://twtxgnn.yao.care/)"
            )
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.content, "lxml")
    except Exception as e:
        print(f"  警告: 無法抓取 {url} - {e}")
        return None


def extract_articles(soup: BeautifulSoup) -> list[dict]:
    """從頁面中提取文章列表"""
    articles = []

    # 找出文章容器（根據網站結構調整）
    # 嘗試多種可能的選擇器
    article_elements = soup.select(".article, .item, article, .blog-item")

    if not article_elements:
        # 嘗試找 h2 連結作為文章標題
        article_elements = soup.select("h2 a, .article-title a, .title a")

    for element in article_elements:
        try:
            # 提取標題和連結
            if element.name == "a":
                title = element.get_text(strip=True)
                link = element.get("href", "")
            else:
                title_elem = element.select_one("h2 a, .title a, a")
                if not title_elem:
                    continue
                title = title_elem.get_text(strip=True)
                link = title_elem.get("href", "")

            if not title or not link:
                continue

            # 確保連結是完整 URL
            if link.startswith("/"):
                link = f"{BASE_URL}{link}"

            # 提取日期（嘗試多種方式）
            date_str = ""
            date_elem = element.select_one(
                ".date, .article-date, .created, time, .article-info span"
            )
            if date_elem:
                date_str = date_elem.get_text(strip=True)
            else:
                # 從父元素或相鄰元素找日期
                parent = element.find_parent(class_=["article", "item"])
                if parent:
                    date_elem = parent.select_one(".date, time, span")
                    if date_elem:
                        date_str = date_elem.get_text(strip=True)

            published = parse_date(date_str) if date_str else datetime.now(
                timezone.utc
            ).isoformat()

            articles.append({
                "id": generate_id(title, link),
                "title": title,
                "published": published,
                "summary": "",  # 慈濟網站列表頁通常沒有摘要
                "sources": [{"name": "嘉義慈濟醫院", "link": link}]
            })

        except Exception as e:
            print(f"  警告: 解析文章失敗 - {e}")
            continue

    return articles


def fetch_tzuchi_news() -> list[dict]:
    """抓取嘉義慈濟醫院健康衛教新聞"""
    print(f"抓取嘉義慈濟醫院健康衛教...")
    print(f"  URL: {NEWS_URL}")

    all_articles = []
    seen_ids = set()

    for page in range(1, MAX_PAGES + 1):
        # 第一頁不需要參數，後續頁面需要
        if page == 1:
            url = NEWS_URL
        else:
            url = f"{NEWS_URL}?start={(page - 1) * 10}"  # 假設每頁 10 篇

        print(f"  抓取第 {page} 頁...")
        soup = fetch_page(url)

        if not soup:
            continue

        articles = extract_articles(soup)

        # 去重
        for article in articles:
            if article["id"] not in seen_ids:
                seen_ids.add(article["id"])
                all_articles.append(article)

        # 如果沒有文章，停止翻頁
        if not articles:
            break

    print(f"  抓取到 {len(all_articles)} 則新聞")
    return all_articles


def main():
    # 確保目錄存在
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 抓取新聞
    news_items = fetch_tzuchi_news()

    # 輸出
    output = {
        "source": "tzuchi_chiayi",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(news_items),
        "news": news_items
    }

    output_path = DATA_DIR / "tzuchi_chiayi.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n輸出: {output_path}")
    print(f"  - 新聞數: {len(news_items)}")


if __name__ == "__main__":
    main()
