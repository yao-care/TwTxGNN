---
layout: default
title: Insulin Lispro
description: "Insulin Lispro 的老藥新用潛力分析。模型預測等級 L5，包含 9 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 9
---

# Insulin Lispro

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>9</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Insulin Lispro：從糖尿病到 Autoimmune Oophoritis

## 一句話總結

<p class="key-answer" data-question="Insulin Lispro 可以用於治療什麼新適應症？">
Insulin Lispro 原本用於糖尿病的血糖控制。
TxGNN 模型預測它可能對 **Autoimmune Oophoritis** (自體免疫性卵巢炎) 有效，
但目前缺乏臨床試驗和文獻支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病(成人、青少年及1歲以上兒童) |
| 預測新適應症 | Autoimmune Oophoritis |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 多張(含已註銷) |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Insulin Lispro 是一種速效人工胰島素類似物，透過結合胰島素受體來促進葡萄糖進入細胞，降低血糖。

與自體免疫性卵巢炎的關聯分析：
1. **自體免疫多內分泌症候群 (APS)**：第一型糖尿病常與其他自體免疫疾病共存，包括自體免疫性卵巢炎
2. **胰島素的免疫調節作用**：胰島素可能對免疫系統有某些調節作用，但此機轉尚未在卵巢自體免疫中被證實
3. **間接關聯**：此預測可能反映知識圖譜中自體免疫疾病間的關聯性，而非直接治療效果

目前缺乏機轉支持 Insulin Lispro 可直接治療自體免疫性卵巢炎。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無直接相關文獻

**注意**：有文獻探討胰島素治療第二型糖尿病，但與自體免疫性卵巢炎無關。

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 | 狀態 |
|---------|------|------|-----------|------|
| 衛署菌疫輸字第000898號 | 優泌樂筆-混合型 25 100單位/毫升 | 注射劑 | 糖尿病 | 有效 |
| 衛署菌疫輸字第000900號 | 優泌樂筆注射劑 100單位/毫升 | 注射劑 | 糖尿病 | 有效 |
| 衛部菌疫輸字第001148號 | 速泌樂注射劑100單位/毫升 | 注射液劑 | 糖尿病(成人、青少年、1歲以上兒童) | 已註銷 |

## 安全性考量

- **主要風險**：低血糖

- **藥物交互作用**：
  - 影響血糖的藥物（如：口服降血糖藥、thiazide類利尿劑、corticosteroids）
  - Beta-blockers 可能掩蓋低血糖症狀

- **特殊族群**：
  - 腎功能不全需調整劑量
  - 妊娠期間胰島素需求可能變化

## 結論與下一步

**決策：Hold**

**理由：**
Insulin Lispro 用於自體免疫性卵巢炎的預測缺乏明確的機轉支持和臨床證據。雖然糖尿病與自體免疫性卵巢炎可能共存於自體免疫多內分泌症候群中，但胰島素並非針對卵巢自體免疫的治療。

**若要推進需要：**
- 探討胰島素在自體免疫調節中的潛在角色
- 分析 APS 患者中胰島素治療與卵巢功能的關聯
- 進行基礎研究以驗證機轉假說
- 目前應聚焦於已建立的免疫調節治療策略


---

## 相關藥物報告

- [Theophylline]({{ "/drugs/theophylline/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5
- [Sodium Citrate]({{ "/drugs/sodium_citrate/" | relative_url }}) - 證據等級 L5
- [Inclisiran]({{ "/drugs/inclisiran/" | relative_url }}) - 證據等級 L5
- [Metoprolol]({{ "/drugs/metoprolol/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Insulin Lispro老藥新用驗證報告. https://twtxgnn.yao.care/drugs/insulin_lispro/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_insulin_lispro,
  title = {Insulin Lispro老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/insulin_lispro/}
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
