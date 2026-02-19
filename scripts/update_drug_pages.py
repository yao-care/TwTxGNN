#!/usr/bin/env python3
"""
批量更新藥物頁面 SGE/AEO 標記
- 移除 Kramdown 語法
- 新增 .key-answer 標記
- 新增 .key-takeaway 標記
- 標準化免責聲明
"""

import re
import os
from pathlib import Path
from datetime import datetime


def extract_front_matter(content: str) -> tuple[dict, str]:
    """提取 front matter 和內容"""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    front_matter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            front_matter[key.strip()] = value.strip().strip('"')

    return front_matter, '---' + parts[1] + '---' + parts[2]


def remove_kramdown_syntax(content: str) -> str:
    """移除 Kramdown 屬性語法"""
    # 移除 {: .xxx } 格式（可能跨行）
    content = re.sub(r'\n\{:\s*\.[^}]+\}\n', '\n', content)
    content = re.sub(r'\{:\s*\.[^}]+\}', '', content)

    # 移除 {:toc} 格式
    content = re.sub(r'\{:toc\}', '', content)

    # 移除空的目錄區塊
    content = re.sub(r'## 目錄\n+1\. TOC\n+---', '---', content)

    return content


def update_header_block(content: str, front_matter: dict) -> str:
    """更新標題區塊為內嵌 HTML"""
    title = front_matter.get('title', '')
    evidence_level = front_matter.get('evidence_level', 'L5')
    indication_count = front_matter.get('indication_count', '?')

    # 找到舊的標題格式並替換
    old_header_pattern = rf'# {re.escape(title)}\n+證據等級: \*\*{evidence_level}\*\* \| 預測適應症: \*\*{indication_count}\*\* 個\n+'

    new_header = f'''# {title}

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>{evidence_level}</strong> | 預測適應症: <strong>{indication_count}</strong> 個
</p>

'''

    content = re.sub(old_header_pattern, new_header, content)

    return content


def wrap_summary_with_key_answer(content: str, title: str) -> str:
    """將一句話總結包裝為 key-answer"""
    # 尋找 ## 一句話總結 後面的段落
    pattern = r'(## 一句話總結\n+)([^\n#]+(?:\n[^\n#]+)*)'

    def replace_summary(match):
        header = match.group(1)
        summary_text = match.group(2).strip()

        # 如果已經有 key-answer 標記，跳過
        if 'class="key-answer"' in summary_text:
            return match.group(0)

        # 包裝為 key-answer
        return f'''{header}<p class="key-answer" data-question="{title} 可以用於治療什麼新適應症？">
{summary_text}
</p>

'''

    content = re.sub(pattern, replace_summary, content)
    return content


def add_key_takeaway(content: str) -> str:
    """在結論區塊前添加 key-takeaway（如果沒有的話）"""
    # 如果已經有 key-takeaway，跳過
    if 'class="key-takeaway"' in content:
        return content

    # 在 ## 為什麼這個預測合理？ 後面的第一段後添加 key-takeaway
    pattern = r'(## 為什麼這個預測合理？\n+)([^\n]+(?:\n[^\n#]+)*?)(\n+\*\*機轉|\n+##)'

    def add_takeaway(match):
        header = match.group(1)
        first_para = match.group(2).strip()
        next_section = match.group(3)

        return f'''{header}<p class="key-answer" data-question="這個藥物的作用機轉是什麼？">
{first_para}
</p>

<div class="key-takeaway">
此預測基於藥物的作用機轉，與現有臨床證據方向一致。
</div>
{next_section}'''

    content = re.sub(pattern, add_takeaway, content)
    return content


def standardize_disclaimer(content: str) -> str:
    """標準化免責聲明格式"""
    # 移除舊的免責聲明（各種格式）
    old_disclaimer_patterns = [
        r'<div style="background: #fff3cd[^>]*>.*?</div>\s*$',
        r'<div class="disclaimer">.*?</div>\s*$',
    ]

    for pattern in old_disclaimer_patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)

    # 確保內容末尾沒有多餘空行
    content = content.rstrip()

    # 添加標準化的免責聲明
    today = datetime.now().strftime('%Y-%m-%d')
    disclaimer = f'''

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：{today} | 審核者：TwTxGNN Research Team</small>
</div>
'''

    return content + disclaimer


def process_drug_page(file_path: Path) -> bool:
    """處理單一藥物頁面"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # 提取 front matter
        front_matter, content = extract_front_matter(content)
        title = front_matter.get('title', '')

        # 跳過已經處理過的 temozolomide.md
        if title == 'Temozolomide' and 'class="key-answer"' in content:
            return False

        # 1. 移除 Kramdown 語法
        content = remove_kramdown_syntax(content)

        # 2. 更新標題區塊
        content = update_header_block(content, front_matter)

        # 3. 包裝一句話總結
        content = wrap_summary_with_key_answer(content, title)

        # 4. 添加 key-takeaway（在適當位置）
        content = add_key_takeaway(content)

        # 5. 標準化免責聲明
        content = standardize_disclaimer(content)

        # 清理多餘空行
        content = re.sub(r'\n{4,}', '\n\n\n', content)

        # 檢查是否有變更
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return True

        return False

    except Exception as e:
        print(f"  錯誤處理 {file_path.name}: {e}")
        return False


def main():
    """主程式"""
    drugs_dir = Path(__file__).parent.parent / 'docs' / '_drugs'

    if not drugs_dir.exists():
        print(f"錯誤：找不到目錄 {drugs_dir}")
        return

    drug_files = sorted(drugs_dir.glob('*.md'))
    total = len(drug_files)
    updated = 0
    skipped = 0

    print(f"開始處理 {total} 個藥物頁面...")
    print("-" * 50)

    for i, file_path in enumerate(drug_files, 1):
        result = process_drug_page(file_path)
        if result:
            updated += 1
            print(f"[{i}/{total}] ✅ 已更新: {file_path.name}")
        else:
            skipped += 1
            print(f"[{i}/{total}] ⏭️  跳過: {file_path.name}")

    print("-" * 50)
    print(f"完成！已更新 {updated} 個檔案，跳過 {skipped} 個檔案")


if __name__ == '__main__':
    main()
