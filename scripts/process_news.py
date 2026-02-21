#!/usr/bin/env python3
"""
新聞處理腳本

功能：
1. 讀取所有 data/news/*.json 來源檔案
2. 載入 keywords.json 進行關鍵字匹配
3. 跨站去重（相似標題合併來源）
4. 輸出 matched_news.json
5. 產生 docs/_news/*.md 頁面
"""

import json
import re
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path

# 專案根目錄
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"
DOCS_DIR = PROJECT_ROOT / "docs"
NEWS_COLLECTION_DIR = DOCS_DIR / "_news"

# 設定
SIMILARITY_THRESHOLD = 0.8  # 標題相似度閾值
TIME_WINDOW_HOURS = 24  # 去重時間窗口（小時）
MAX_NEWS_AGE_DAYS = 30  # 最大新聞保留天數


def load_json(path: Path) -> dict | list:
    """載入 JSON 檔案"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict | list, path: Path):
    """儲存 JSON 檔案"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_all_sources() -> list[dict]:
    """載入所有來源的新聞"""
    all_news = []
    excluded = {"keywords.json", "matched_news.json"}

    for json_file in DATA_DIR.glob("*.json"):
        if json_file.name in excluded:
            continue

        try:
            data = load_json(json_file)
            source_name = data.get("source", json_file.stem)
            news_items = data.get("news", [])
            print(f"  - {json_file.name}: {len(news_items)} 則")

            for item in news_items:
                item["_source_file"] = source_name
                all_news.append(item)

        except Exception as e:
            print(f"  警告: 無法載入 {json_file.name} - {e}")

    return all_news


def filter_old_news(news_items: list[dict]) -> list[dict]:
    """過濾超過 30 天的舊新聞"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_NEWS_AGE_DAYS)
    filtered = []

    for item in news_items:
        try:
            published = datetime.fromisoformat(item.get("published", ""))
            if published >= cutoff:
                filtered.append(item)
        except (ValueError, TypeError):
            # 無法解析日期，保留
            filtered.append(item)

    removed = len(news_items) - len(filtered)
    if removed > 0:
        print(f"  過濾舊新聞: {removed} 則")

    return filtered


def title_similarity(title1: str, title2: str) -> float:
    """計算兩個標題的相似度"""
    # 移除來源標記（如「- 聯合報」）
    clean1 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title1).strip()
    clean2 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title2).strip()

    return SequenceMatcher(None, clean1, clean2).ratio()


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """跨站去重，合併相似新聞的來源"""
    # 按發布時間排序（最新的在前）
    sorted_news = sorted(
        news_items,
        key=lambda x: x.get("published", ""),
        reverse=True
    )

    merged = []
    used_indices = set()

    for i, item in enumerate(sorted_news):
        if i in used_indices:
            continue

        # 找出相似的新聞
        similar_items = [item]
        item_time = datetime.fromisoformat(
            item.get("published", datetime.now(timezone.utc).isoformat())
        )

        for j, other in enumerate(sorted_news[i + 1:], start=i + 1):
            if j in used_indices:
                continue

            # 檢查時間窗口
            other_time = datetime.fromisoformat(
                other.get("published", datetime.now(timezone.utc).isoformat())
            )
            time_diff = abs((item_time - other_time).total_seconds() / 3600)

            if time_diff > TIME_WINDOW_HOURS:
                continue

            # 檢查標題相似度
            if title_similarity(item["title"], other["title"]) >= SIMILARITY_THRESHOLD:
                similar_items.append(other)
                used_indices.add(j)

        # 合併來源
        all_sources = []
        seen_links = set()
        for sim_item in similar_items:
            for source in sim_item.get("sources", []):
                if source["link"] not in seen_links:
                    seen_links.add(source["link"])
                    all_sources.append(source)

        # 使用最早的發布時間
        earliest_time = min(
            datetime.fromisoformat(s.get("published", datetime.now(timezone.utc).isoformat()))
            for s in similar_items
        )

        merged_item = {
            "id": item["id"],
            "title": re.sub(r"\s*[-–—]\s*[^\s]+$", "", item["title"]).strip(),
            "published": earliest_time.isoformat(),
            "summary": item.get("summary", ""),
            "sources": all_sources,
            "matched_keywords": []  # 稍後填入
        }
        merged.append(merged_item)
        used_indices.add(i)

    print(f"  去重後: {len(merged)} 則（合併 {len(news_items) - len(merged)} 則）")
    return merged


def match_keywords(news_items: list[dict], keywords: dict) -> list[dict]:
    """對新聞進行關鍵字匹配"""
    drugs = keywords.get("drugs", [])
    indications = keywords.get("indications", [])

    # 建立藥物 slug -> name 的對照表
    drug_name_map = {d["slug"]: d["name"] for d in drugs}

    matched_count = 0

    for item in news_items:
        text_to_search = f"{item['title']} {item.get('summary', '')}".lower()
        matches = []

        # 匹配藥物
        for drug in drugs:
            drug_name = drug["name"]
            drug_slug = drug["slug"]

            # 英文關鍵字
            for kw in drug["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "drug",
                        "slug": drug_slug,
                        "keyword": kw,
                        "name": drug_name,
                        "url": drug["url"]
                    })
                    break  # 同一藥物只記錄一次

            # 中文關鍵字
            for kw in drug["keywords"].get("zh", []):
                if kw in item["title"] or kw in item.get("summary", ""):
                    # 確保沒有重複
                    if not any(m["slug"] == drug_slug for m in matches):
                        matches.append({
                            "type": "drug",
                            "slug": drug_slug,
                            "keyword": kw,
                            "name": drug_name,
                            "url": drug["url"]
                        })
                    break

        # 匹配適應症
        for ind in indications:
            ind_name = ind["name"]

            # 將 related_drugs 從 slug 轉換為 {slug, name} 格式
            related_drugs = [
                {"slug": slug, "name": drug_name_map.get(slug, slug)}
                for slug in ind.get("related_drugs", [])
            ]

            # 英文關鍵字
            for kw in ind["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "indication",
                        "name": ind_name,
                        "keyword": kw,
                        "related_drugs": related_drugs
                    })
                    break

            # 中文關鍵字
            for kw in ind["keywords"].get("zh", []):
                if kw in item["title"] or kw in item.get("summary", ""):
                    # 確保同一關鍵字沒有重複（避免 "感冒" 同時出現在 "common cold" 和 "感冒" 兩個條目）
                    if not any(m.get("keyword") == kw and m["type"] == "indication" for m in matches):
                        matches.append({
                            "type": "indication",
                            "name": ind_name,
                            "keyword": kw,
                            "related_drugs": related_drugs
                        })
                    break

        item["matched_keywords"] = matches
        if matches:
            matched_count += 1

    print(f"  匹配到關鍵字: {matched_count} 則")
    return news_items


def generate_news_pages(matched_news: list[dict], keywords: dict):
    """產生 Jekyll 新聞頁面"""
    # 確保目錄存在
    NEWS_COLLECTION_DIR.mkdir(parents=True, exist_ok=True)

    # 清除舊頁面
    for old_file in NEWS_COLLECTION_DIR.glob("*.md"):
        old_file.unlink()

    # 建立藥物和適應症的新聞索引
    drug_news = {}  # slug -> [news_items]
    indication_news = {}  # name -> [news_items]

    for item in matched_news:
        if not item.get("matched_keywords"):
            continue

        for match in item["matched_keywords"]:
            if match["type"] == "drug":
                slug = match["slug"]
                if slug not in drug_news:
                    drug_news[slug] = []
                drug_news[slug].append(item)
            elif match["type"] == "indication":
                name = match["name"]
                if name not in indication_news:
                    indication_news[name] = []
                indication_news[name].append(item)

    # 產生藥物新聞頁面
    drugs_map = {d["slug"]: d for d in keywords.get("drugs", [])}

    for slug, items in drug_news.items():
        drug_info = drugs_map.get(slug, {})
        generate_drug_news_page(slug, drug_info, items)

    # 產生適應症新聞頁面
    for name, items in indication_news.items():
        generate_indication_news_page(name, items, keywords)

    print(f"  產生頁面: {len(drug_news)} 藥物 + {len(indication_news)} 適應症")


def slugify(text: str) -> str:
    """將文字轉換為 URL-safe 的 slug"""
    # 移除特殊字符，保留英文字母、數字和連字號
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug.strip("-")


def generate_drug_news_page(slug: str, drug_info: dict, news_items: list[dict]):
    """產生藥物新聞頁面"""
    name = drug_info.get("name", slug)

    content = f"""---
layout: default
title: "{name} 相關新聞"
parent: 健康新聞
nav_exclude: true
permalink: /news/{slug}/
---

# {name} 相關新聞

[← 返回新聞總覽]({{{{ '/news/' | relative_url }}}})

---

<div class="drug-info-card">
<strong>藥物資訊</strong>

[查看完整藥物報告 →]({{{{ '/drugs/{slug}/' | relative_url }}}})

</div>

## 相關新聞（{len(news_items)} 則）

"""

    for item in sorted(news_items, key=lambda x: x["published"], reverse=True):
        # 格式化日期
        try:
            dt = datetime.fromisoformat(item["published"])
            date_str = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_str = "未知日期"

        # 來源連結
        sources_html = " · ".join(
            f'[{s["name"]}]({s["link"]})'
            for s in item.get("sources", [])
        )

        content += f"""### {item["title"]}

{date_str}

來源：{sources_html}

---

"""

    content += """
<div class="disclaimer">
<strong>免責聲明</strong>：本頁新聞由系統自動收集，僅供研究參考，不構成醫療建議。
</div>
"""

    # 寫入檔案
    output_path = NEWS_COLLECTION_DIR / f"{slug}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_indication_news_page(name: str, news_items: list[dict], keywords: dict):
    """產生適應症新聞頁面"""
    slug = slugify(name)

    # 找出相關藥物
    related_drugs = set()
    for ind in keywords.get("indications", []):
        if ind["name"] == name:
            related_drugs.update(ind.get("related_drugs", []))
            break

    drugs_map = {d["slug"]: d for d in keywords.get("drugs", [])}

    content = f"""---
layout: default
title: "{name} 相關新聞"
parent: 健康新聞
nav_exclude: true
permalink: /news/{slug}/
---

# {name} 相關新聞

[← 返回新聞總覽]({{{{ '/news/' | relative_url }}}})

---

"""

    if related_drugs:
        content += """<div class="related-drugs-card">
<strong>相關藥物報告</strong>

以下藥物的預測適應症可能與此疾病相關：

"""
        for drug_slug in sorted(related_drugs):
            drug = drugs_map.get(drug_slug, {})
            drug_name = drug.get("name", drug_slug)
            content += f"- [{drug_name}]({{{{ '/drugs/{drug_slug}/' | relative_url }}}})\n"

        content += "\n</div>\n\n"

    content += f"""## 相關新聞（{len(news_items)} 則）

"""

    for item in sorted(news_items, key=lambda x: x["published"], reverse=True):
        try:
            dt = datetime.fromisoformat(item["published"])
            date_str = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_str = "未知日期"

        sources_html = " · ".join(
            f'[{s["name"]}]({s["link"]})'
            for s in item.get("sources", [])
        )

        content += f"""### {item["title"]}

{date_str}

來源：{sources_html}

---

"""

    content += """
<div class="disclaimer">
<strong>免責聲明</strong>：本頁新聞由系統自動收集，僅供研究參考，不構成醫療建議。
</div>
"""

    output_path = NEWS_COLLECTION_DIR / f"{slug}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_news_index(matched_news: list[dict]):
    """產生前端用的新聞索引 JSON"""
    # 只保留有匹配關鍵字的新聞
    indexed_news = [
        {
            "id": item["id"],
            "title": item["title"],
            "published": item["published"],
            "sources": item["sources"],
            "keywords": item["matched_keywords"]
        }
        for item in matched_news
        if item.get("matched_keywords")
    ]

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "count": len(indexed_news),
        "news": indexed_news
    }

    output_path = DOCS_DIR / "data" / "news-index.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(output, output_path)
    print(f"  產生索引: {output_path}")


def main():
    print("處理新聞資料...")

    # 1. 載入所有來源
    print("\n載入來源檔案:")
    all_news = load_all_sources()
    print(f"  總計: {len(all_news)} 則")

    # 2. 過濾舊新聞
    print("\n過濾舊新聞:")
    all_news = filter_old_news(all_news)

    # 3. 去重
    print("\n跨站去重:")
    all_news = deduplicate_news(all_news)

    # 4. 載入關鍵字並匹配
    print("\n關鍵字匹配:")
    keywords = load_json(DATA_DIR / "keywords.json")
    print(f"  關鍵字: {keywords['drug_count']} 藥物 + {keywords['indication_count']} 適應症")
    all_news = match_keywords(all_news, keywords)

    # 5. 輸出 matched_news.json
    output = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_count": len(all_news),
        "matched_count": sum(1 for n in all_news if n.get("matched_keywords")),
        "news": all_news
    }
    save_json(output, DATA_DIR / "matched_news.json")
    print(f"\n輸出: {DATA_DIR / 'matched_news.json'}")

    # 6. 產生頁面
    print("\n產生 Jekyll 頁面:")
    generate_news_pages(all_news, keywords)

    # 7. 產生索引
    generate_news_index(all_news)

    print("\n完成！")


if __name__ == "__main__":
    main()
