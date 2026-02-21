---
layout: default
title: Inclisiran
description: "Inclisiran 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Inclisiran

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Inclisiran：從高膽固醇血症到 Potassium Deficiency Disease

## 一句話總結

<p class="key-answer" data-question="Inclisiran 可以用於治療什麼新適應症？">
Inclisiran 原本用於原發性高血脂症的 LDL-C 降低治療。
TxGNN 模型預測它可能對 **Potassium Deficiency Disease** 有效，
但目前缺乏臨床試驗和文獻支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性高血脂症(含異合子家族性高膽固醇血症)之 LDL-C 降低 |
| 預測新適應症 | potassium deficiency disease、esophageal disease、atypical coarctation of aorta、migraine disorder、non-syndromic esophageal malformation、migraine with brainstem aura、migraine with or without aura, susceptibility to、aortic malformation、esophageal ulcer、Raynaud disease |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 1 張(3筆重複記錄) |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Inclisiran 是一種小干擾 RNA (siRNA) 藥物，透過抑制肝臟中 PCSK9 蛋白的合成來增加 LDL 受體的表現，進而降低血液中的 LDL 膽固醇濃度。

與鉀缺乏症的關聯目前缺乏明確的機轉解釋：
1. Inclisiran 的主要作用靶點為 PCSK9，與鉀代謝無直接關聯
2. 目前沒有臨床或臨床前研究探討 Inclisiran 對鉀代謝的影響
3. 此預測可能源於知識圖譜中的間接關聯，需要進一步驗證

## 臨床試驗證據

目前無相關臨床試驗登記

**注意**：有 2 項進行中的 Inclisiran 兒童家族性高膽固醇血症試驗([NCT06597006](https://clinicaltrials.gov/study/NCT06597006)、[NCT06597019](https://clinicaltrials.gov/study/NCT06597019))，但與鉀缺乏症無關。

## 文獻證據

目前無相關文獻

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028761號 | 樂脂益注射劑 | 注射液劑 | 原發性高血脂症(含異合子家族性高膽固醇血症)作為飲食及降血脂藥品的輔助治療 |

## 安全性考量

- **藥物交互作用**：目前 DDI 資料庫中未發現顯著交互作用

- **已知副作用**：注射部位反應、上呼吸道感染、肌肉骨骼疼痛

## 結論與下一步

**決策：Hold**

**理由：**
Inclisiran 用於鉀缺乏症的預測缺乏明確的機轉支持和臨床證據。目前無任何臨床試驗或文獻探討此關聯性。

**若要推進需要：**
- 進行機轉層面的研究，探討 PCSK9 抑制與鉀代謝的潛在關聯
- 分析 Inclisiran 臨床試驗中的電解質變化數據
- 建立假說並設計探索性臨床研究


---

## 相關藥物報告

- [Cyclizine]({{ "/drugs/cyclizine/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5
- [Oxytetracycline]({{ "/drugs/oxytetracycline/" | relative_url }}) - 證據等級 L5
- [Pipemidic Acid]({{ "/drugs/pipemidic_acid/" | relative_url }}) - 證據等級 L5
- [Insulin Lispro]({{ "/drugs/insulin_lispro/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Inclisiran老藥新用驗證報告. https://twtxgnn.yao.care/drugs/inclisiran/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_inclisiran,
  title = {Inclisiran老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/inclisiran/}
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
