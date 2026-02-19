#!/usr/bin/env python3
"""
批次為藥物報告加入引用格式和強化免責聲明
"""
import os
import re
from pathlib import Path

DRUGS_DIR = Path(__file__).parent.parent / "docs" / "_drugs"

CITATION_TEMPLATE = '''
---

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). {title}老藥新用驗證報告. https://twtxgnn.yao.care/drugs/{slug}/
```

**BibTeX 格式：**
```bibtex
@misc{{twtxgnn_{slug_safe},
  title = {{{title}老藥新用驗證報告}},
  author = {{TwTxGNN Team}},
  year = {{2026}},
  url = {{https://twtxgnn.yao.care/drugs/{slug}/}}
}}
```

---

<div style="background: #fff3cd; padding: 1rem; margin-top: 1rem; border-left: 4px solid #ffc107; border-radius: 4px;">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
</div>
'''

def extract_front_matter(content: str) -> tuple[dict, str]:
    """提取 front matter 和內容"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content

    fm_text = match.group(1)
    body = match.group(2)

    # 簡單解析 YAML
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            fm[key.strip()] = value.strip().strip('"').strip("'")

    return fm, body

def update_drug_file(filepath: Path) -> bool:
    """更新單一藥物檔案，加入引用格式和免責聲明"""
    content = filepath.read_text(encoding='utf-8')

    # 檢查是否已有引用區塊
    if '## 引用本報告' in content:
        return False

    fm, body = extract_front_matter(content)
    if not fm:
        print(f"  跳過 {filepath.name}: 無法解析 front matter")
        return False

    title = fm.get('title', filepath.stem)
    slug = filepath.stem

    # 移除舊的免責聲明（如果有）
    body = re.sub(r'\n*\{: \.warning \}\n>.*?不構成醫療建議.*?\n*', '\n', body, flags=re.DOTALL)
    body = re.sub(r'\n*---\n*$', '', body)  # 移除結尾的 ---

    # 產生引用和免責聲明區塊
    citation_block = CITATION_TEMPLATE.format(
        title=title,
        slug=slug,
        slug_safe=slug.replace('-', '_').replace('.', '_')
    )

    # 重建內容
    new_content = f"---\n{content.split('---')[1].strip()}\n---\n{body.rstrip()}\n{citation_block}"

    filepath.write_text(new_content, encoding='utf-8')
    return True

def main():
    """主函數"""
    if not DRUGS_DIR.exists():
        print(f"錯誤：找不到目錄 {DRUGS_DIR}")
        return

    drug_files = list(DRUGS_DIR.glob("*.md"))
    print(f"找到 {len(drug_files)} 個藥物報告")

    updated = 0
    for filepath in sorted(drug_files):
        if update_drug_file(filepath):
            updated += 1
            print(f"  已更新: {filepath.name}")

    print(f"\n完成！共更新 {updated} 個檔案")

if __name__ == "__main__":
    main()
