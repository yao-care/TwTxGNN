---
layout: default
title: Thyrotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 1
---

# Thyrotropin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Thyrotropin alfa：從甲狀腺分化癌到偏頭痛

## 一句話總結

Thyrotropin alfa（適諾進）是重組人類促甲狀腺激素（rhTSH），原本作為甲狀腺分化癌術後放射碘去除治療的輔助診斷製劑。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
但目前**無任何臨床試驗或支持文獻**，屬純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲狀腺分化癌（術後放射碘輔助治療） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Thyrotropin alfa 是以基因重組技術製造的人類促甲狀腺激素（rhTSH）。其作用機轉為與甲狀腺濾泡細胞表面的 TSH 受體（TSHR）結合，刺激甲狀腺激素（T3/T4）合成及碘攝取。臨床上，它讓甲狀腺癌術後病人無需停用甲狀腺素補充療法，即可在放射碘掃描或消融治療前短暫提升 TSH 濃度，增強殘餘甲狀腺組織的碘攝取效率。

偏頭痛的核心病理機轉涉及三叉神經血管活化（CGRP pathway）與皮質擴散性抑制（CSD），與 TSH 受體激動的甲狀腺內分泌作用屬於不同系統，缺乏直接的機轉交集。TxGNN 的預測可能源於知識圖譜中甲狀腺系統與神經系統之間的遠端路徑關聯——例如甲狀腺激素對神經元代謝的調節作用，或甲狀腺疾病患者偏頭痛盛行率略高的流行病學觀察——但這些關聯僅屬間接推論。

總體而言，本預測的機轉合理性非常薄弱。TxGNN 高分反映的是知識圖譜節點的圖拓樸相似性，而非藥物對偏頭痛的實際療效潛力。建議謹慎看待此預測，需前臨床研究驗證後才能進一步評估可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署罕菌疫輸字第000003號 | 適諾進凍晶注射劑 1.1毫克 | 凍晶注射劑 | 甲狀腺分化癌治療之輔助診斷製劑。適用於因甲狀腺分化癌而接受幾乎全部或全部甲狀腺切除、且沒有轉移性甲狀腺癌的跡象... |

---

## 安全性考量

**藥物交互作用：** 共有 45 筆中度（Moderate）交互作用紀錄，主要集中於**降血糖藥物**類別：

| 交互作用藥物 | 等級 | 類別 |
|-------------|------|------|
| Metformin | Moderate | Biguanide |
| Insulin human | Moderate | 胰島素 |
| Glimepiride | Moderate | Sulfonylurea |
| Glipizide | Moderate | Sulfonylurea |
| Glyburide | Moderate | Sulfonylurea |
| Semaglutide | Moderate | GLP-1 受體促效劑 |
| Dulaglutide | Moderate | GLP-1 受體促效劑 |
| Canagliflozin | Moderate | SGLT-2 抑制劑 |
| Dapagliflozin | Moderate | SGLT-2 抑制劑 |
| Empagliflozin | Moderate | SGLT-2 抑制劑 |

其餘 35 筆亦屬中度交互作用，涵蓋 DPP-4 抑制劑（Alogliptin、Saxagliptin）、SGLT-2 抑制劑（Ertugliflozin）、胰島素類似物等。使用時需特別留意與糖尿病用藥的交互作用。

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖達 99.98%，但 Thyrotropin alfa 的 TSH 受體激動機轉與偏頭痛的三叉神經血管病理缺乏任何已知直接連結；目前完全無臨床試驗或文獻佐證，屬純模型推論，不具備推進再利用研究的依據。

**若要推進需要：**
- 補充正式的 DrugBank MOA 資料（完整藥理機轉描述）
- 評估甲狀腺激素水平與偏頭痛發作頻率之流行病學相關性文獻
- 進行 in vitro 或動物模型前臨床研究，探索 TSH 對三叉神經或 CGRP 路徑的直接或間接作用
- 確認注射劑型對偏頭痛慢性預防治療的臨床可行性及病人接受度

---

