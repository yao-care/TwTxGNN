---
layout: default
title: Ouabain
description: "Ouabain 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Ouabain

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ouabain 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Ouabain 可以用於治療什麼新適應症？">
Ouabain 為強心配醣體類藥物，TxGNN 預測其可能對鐮刀型紅血球貧血和心肌梗塞有治療潛力，但目前僅有前臨床研究支持，需謹慎評估其治療窗口極窄的安全性問題。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品名稱 | Ouabain (歐巴因) |
| DrugBank ID | DB01092 |
| 台灣商品名 | 安保心注射液 |
| 原適應症 | 心臟衰竭、心房撲動、心房纖維顫動、陣發性上室性心搏過速 |
| 預測新適應症 | 鐮刀型紅血球貧血 (Sickle cell anemia)、心肌梗塞 (Myocardial infarction) |
| 證據等級 | L4 (前臨床研究) |
| TxGNN 預測分數 | 0.995 (鐮刀型紅血球貧血)、0.994 (心肌梗塞) |

---

## 為什麼這個預測合理

### 機轉連結

1. **鐮刀型紅血球貧血**：Ouabain 作為 Na+/K+-ATPase 抑制劑，可調節紅血球陽離子運輸。研究顯示鐮刀型紅血球的陽離子通透性異常，ouabain 敏感性的 ATPase 活性在這些細胞中呈現特殊表現，可能有助於調節細胞膜穩定性。

2. **心肌梗塞**：腦內類 ouabain 化合物 (ouabain-like compounds) 與腎素-血管張力素系統在心肌梗塞後的交感神經過度活化中扮演關鍵角色。低劑量 ouabain 可能透過 Na/K-ATPase 訊號傳導途徑產生心臟保護作用。

---

## 臨床試驗證據

目前無針對上述預測適應症的已完成臨床試驗。

---

## 文獻證據

### 鐮刀型紅血球貧血相關研究

| PMID | 發表年份 | 主要發現 |
|------|----------|----------|
| 149799 | 1978 | 發現不可逆鐮刀型細胞的主動陽離子運輸下降，但膜 Na,K-ATPase 活性正常 |
| 2213597 | 1990 | 脫氧使鐮刀型貧血紅血球對鎂離子通透化，可能影響離子梯度 |
| 7204577 | 1981 | 地中海型貧血和骨髓應激狀態下紅血球陽離子通透性增加 |

### 心肌梗塞相關研究

| PMID | 發表年份 | 主要發現 |
|------|----------|----------|
| 10564131 | 1999 | 腦內 "ouabain" 和血管張力素 II 參與心肌梗塞後心臟功能障礙 |
| 19486591 | 2009 | 腦 RAAS 系統是心肌梗塞後交感神經過度活化和左心室重塑的主要機制 |
| 30096873 | 2018 | 低濃度 CTS 透過 Na/K-ATPase 訊號傳導可能對急性心肌梗塞產生保護作用 |

---

## 台灣上市資訊

| 許可證字號 | 商品名 | 劑型 | 適應症 | 狀態 |
|-----------|--------|------|--------|------|
| 內衛藥製字第001934號 | 安保心注射液 | 注射劑 | 心臟衰竭、心房撲動、心房纖維顫動、陣發性上室性心博過速 | 有效 |
| 內衛藥製字第007192號 | 哇巴因注射液 | 注射劑 | 心臟衰竭、心房撲動 | 已註銷 |
| 衛署藥製字第033771號 | 吾安保因注射液 | 注射劑 | 心臟衰竭、心房撲動 | 已註銷 |

---

## 安全性考量

### 重要警語

- **治療窗口極窄**：Ouabain 屬於強心配醣體，治療劑量與中毒劑量接近
- **心律不整風險**：可能誘發嚴重心律不整，包括心室顫動
- **電解質監測**：低血鉀會增加毒性風險，需密切監測電解質

### 藥物交互作用

目前資料庫中無記載重大藥物交互作用，但臨床上應注意：
- 利尿劑（可能導致低血鉀，增加毒性）
- 其他抗心律不整藥物
- 鈣離子補充劑

### 特殊族群

- 腎功能不全患者需調整劑量
- 老年人對強心配醣體更敏感
- 孕婦及哺乳婦女使用安全性未確立

---

## 結論與下一步

### 整體評估

Ouabain 對鐮刀型紅血球貧血和心肌梗塞的老藥新用預測在機轉上具有合理性，但：

1. **證據等級偏低 (L4)**：目前僅有基礎研究和動物實驗支持
2. **安全性疑慮重大**：治療窗口極窄，臨床應用風險高
3. **臨床可行性有限**：需要開發更安全的給藥方式或找到更安全的類似物

### 建議行動

- **不建議直接進行臨床試驗**：需先進行更多前臨床安全性和有效性研究
- **探索替代策略**：考慮研究其他 Na/K-ATPase 調節劑或開發 ouabain 衍生物
- **持續關注文獻**：追蹤相關基礎研究進展

---

*本報告由 TxGNN 預測系統生成，僅供研究參考，不構成醫療建議。*


---

## 相關藥物報告

- [Clomipramine]({{ "/drugs/clomipramine/" | relative_url }}) - 證據等級 L5
- [Gefitinib]({{ "/drugs/gefitinib/" | relative_url }}) - 證據等級 L5
- [Terbutaline]({{ "/drugs/terbutaline/" | relative_url }}) - 證據等級 L5
- [Remdesivir]({{ "/drugs/remdesivir/" | relative_url }}) - 證據等級 L5
- [Tyrosine]({{ "/drugs/tyrosine/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Ouabain老藥新用驗證報告. https://twtxgnn.yao.care/drugs/ouabain/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_ouabain,
  title = {Ouabain老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/ouabain/}
}
```

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-20 | 審核者：TwTxGNN Research Team</small>
</div>

{% include giscus.html %}
