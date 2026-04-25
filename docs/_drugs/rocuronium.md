---
layout: default
title: Rocuronium
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Rocuronium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

使用 `txgnn-pipeline` 確認任務背景後，依據 Evidence Pack v5 Prompt 格式，現在產生 Rocuronium 的藥物再利用評估報告。

---

# Rocuronium：從神經肌肉阻斷到偏頭痛

## 一句話總結

Rocuronium 是全身麻醉常用的非去極化神經肌肉阻斷劑，主要用於手術氣管插管與骨骼肌鬆弛誘導。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **1 個臨床試驗**（但與偏頭痛治療無直接關聯）且**無相關文獻**支持此再利用方向，整體證據力極為有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 拮抗 rocuronium 或 vecuronium 誘導的神經肌肉阻斷 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Rocuronium 詳細作用機轉資料（列為高優先度資料缺口，建議透過 DrugBank API 查詢 DB00728 補充）。根據已知資訊，Rocuronium 是非去極化神經肌肉阻斷劑，透過**競爭性拮抗神經肌肉接頭的菸鹼型乙醯膽鹼受體（nAChR）**，阻斷運動神經衝動傳導至骨骼肌，廣泛應用於全身麻醉誘導及加護病房機械通氣輔助。

偏頭痛的病理核心涉及 **CGRP 釋放、皮質擴散性抑制（CSD）及三叉神經血管系統活化**，與 nAChR 拮抗機轉無直接藥理交集。Rocuronium 幾乎不穿透血腦屏障，對中樞神經電生理或三叉神經系統無已知直接效應，現有 repurposing_rationale 亦明確指出此藥理斷層。

TxGNN 的高預測分數（99.90%）最可能源於知識圖譜中**神經系統相關節點的間接拓樸鄰近**，而非真實藥理關聯。此類預測屬於典型「圖譜信號強、機轉連結弱」案例，需謹慎評估，不宜直接轉譯為臨床研究依據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | 完成 | 3,520 | 兒科多藥藥動學觀察研究，rocuronium 依標準照護給藥；研究目的為 PK 描述，與偏頭痛治療無直接關聯（相關性評級：C） |

> ⚠️ 此試驗並非偏頭痛治療研究，rocuronium 僅作為標準照護藥物納入觀察，無法支持再利用假說。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028665號 | γ-環糊精硫丙酸鈉鹽 | 粉劑 | 拮抗rocuronium或vecuronium誘導的神經肌肉阻斷 |
| 衛部藥輸字第028879號 | 蘇加麻注射劑 100毫克/毫升 | 注射劑 | 用於成人因rocuronium或vecuronium誘導神經肌肉阻斷的逆轉藥物；用於2歲以上兒童及青少年的常規逆轉藥物 |
| 衛部藥陸輸字第001099號 | γ-環糊精硫丙酸鈉鹽 | 粉劑 | 拮抗rocuronium或vecuronium誘導的神經肌肉阻斷 |
| 衛部藥製字第061978號 | 速可逆注射液100毫克/毫升 | 注射劑 | 用於成人因rocuronium或vecuronium誘導神經肌肉阻斷的逆轉藥物；用於2歲以上兒童及青少年的常規逆轉藥物 |
| 衛部藥輸字第028416號 | γ-環糊精硫丙酸鈉鹽 | 粉劑 | 拮抗rocuronium或vecuronium誘導的神經肌肉阻斷 |

> 📌 **資料說明**：台灣許可證查詢結果顯示的品項均為 **Sugammadex**（γ-環糊精硫丙酸鈉鹽，Rocuronium 的特異性逆轉藥物），總計 20 張。這是因為 FDA 資料庫中 Sugammadex 的核准適應症文字包含「rocuronium」關鍵字，導致資料連結。Rocuronium 本身（神經肌肉阻斷劑）亦已在台灣上市，建議另行查詢台灣 FDA 資料庫確認其自身許可證數量。

---

## 安全性考量

**藥物交互作用**（資料庫共收錄 73 筆，以下列出所有 Major 及代表性 Moderate 交互作用）：

| 藥物 | 等級 | 臨床意義 |
|------|------|---------|
| Paromomycin | **Major** | 胺基糖苷類抗生素，可顯著增強及延長神經肌肉阻斷效果 |
| Kanamycin | **Major** | 胺基糖苷類抗生素，可能延長肌肉鬆弛時間，需監測呼吸恢復 |
| Neomycin | **Major** | 胺基糖苷類抗生素，神經肌肉阻斷風險顯著升高 |
| Doxycycline | Moderate | 四環素類抗生素，可能影響神經肌肉傳導 |
| Hydrocortisone | Moderate | 皮質類固醇，可能影響神經肌肉阻斷恢復 |
| Amphotericin B | Moderate | 抗黴菌藥，代謝交互作用 |
| Dexamethasone | Moderate | 皮質類固醇，可能改變神經肌肉阻斷時程 |
| Magnesium sulfate | Moderate | 電解質，鎂離子可協同增強神經肌肉阻斷 |
| Vancomycin | Moderate | 醣肽類抗生素，可能加重神經肌肉阻斷 |
| Metoclopramide | Moderate | 止吐/促腸蠕動藥，代謝交互作用 |

安全性警語及禁忌症詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Rocuronium 的作用機轉（外周骨骼肌 nAChR 競爭性拮抗）與偏頭痛的核心病理機轉（CGRP 釋放、皮質擴散性抑制、三叉神經血管活化）無已知藥理交集，且 Rocuronium 幾乎不穿透血腦屏障；目前無偏頭痛治療相關臨床試驗或文獻，TxGNN 高分極可能源於圖譜拓樸鄰近效應，不具備推進再利用研究的充分依據。

**若要推進需要：**
- **補充 MOA 資料**：查詢 DrugBank API（DB00728）取得 Rocuronium 完整作用機轉，確認是否存在中樞神經系統的次要藥理效應
- **知識圖譜路徑分析**：釐清 TxGNN 連結路徑（Rocuronium → Migraine Disorder 的中介節點），判斷是否為圖譜偽陽性
- **前臨床機轉研究**：確認 Rocuronium 或其代謝物是否對三叉神經血管系統、CGRP 路徑或皮質興奮性有直接效應
- **替代適應症評估**：Rank 10 的 **頭痛疾患 (Headache Disorder)** 有更直接的文獻支持（RCT：PMID [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/)，rocuronium-sugammadex 組合可減少 ECT 後頭痛），機轉連結較偏頭痛更為合理，建議優先評估此方向
---

