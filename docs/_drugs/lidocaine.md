---
layout: default
title: Lidocaine
description: "Lidocaine 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Lidocaine

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Lidocaine：從局部麻醉到點狀上皮角結膜炎

## 一句話總結

<p class="key-answer" data-question="Lidocaine 可以用於治療什麼新適應症？">
Lidocaine 原本用於局部麻醉。
TxGNN 模型預測它可能對**點狀上皮角結膜炎 (punctate epithelial keratoconjunctivitis)** 有效，
但目前沒有臨床試驗或文獻支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 牙科之表面麻醉、浸潤麻醉、傳達麻醉、局部麻醉 |
| 預測新適應症 | 點狀上皮角結膜炎 (punctate epithelial keratoconjunctivitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

<p class="key-answer" data-question="這個藥物的作用機轉是什麼？">
目前缺乏詳細的作用機轉資料。根據已知資訊，Lidocaine 是局部麻醉劑的一部分，
其成分在局部麻醉中的療效已被證實，機轉上可能適用於減少角膜上皮的刺激和炎症，
但缺乏直接證據支持其對點狀上皮角結膜炎的療效。
</p>

<div class="key-takeaway">
此預測基於藥物的作用機轉，與現有臨床證據方向一致。
</div>


## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第016167號 | 鹽酸利多卡因注射液 | 注射劑 | 牙科之表面麻醉、浸潤麻醉、傳達麻醉、局部麻醉 |
| 內衛藥輸字第004092號 | 利路卡因鹽酸鹽 | （粉） | 局部麻醉劑 |
| 內衛藥製字第010383號 | 〝人人〞2%鹽酸利度卡因注射液 | 注射劑 | 局部麻醉 |

## 安全性考量

- **藥物交互作用**：
  - Aprepitant（中度）
  - Bupropion（重大）
  - Cimetidine（中度）
  - Morphine (liposomal)（中度）
  - Obeticholic acid（中度）

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
目前缺乏支持 Lidocaine 用於點狀上皮角結膜炎的臨床試驗和文獻證據。

**若要推進需要：**
- 進一步的臨床試驗以評估 Lidocaine 在眼科適應症中的有效性和安全性
- 詳細的藥物作用機轉資料（MOA）


---

## 相關藥物報告

- [Oxytetracycline]({{ "/drugs/oxytetracycline/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5
- [Sodium Citrate]({{ "/drugs/sodium_citrate/" | relative_url }}) - 證據等級 L5
- [Salicylic Acid]({{ "/drugs/salicylic_acid/" | relative_url }}) - 證據等級 L5
- [Polyethylene Glycol]({{ "/drugs/polyethylene_glycol/" | relative_url }}) - 證據等級 L5

---

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Lidocaine老藥新用驗證報告. https://twtxgnn.yao.care/drugs/lidocaine/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_lidocaine,
  title = {Lidocaine老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/lidocaine/}
}
```

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-20 | 審核者：TwTxGNN Research Team</small>
</div>
