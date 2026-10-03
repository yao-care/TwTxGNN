---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid：從高膽固醇到同合子家族性高膽固醇血症

## 一句話總結
Bempedoic acid 是 ATP 檸檬酸裂解酶抑制劑，用於降低 LDL-C，TxGNN 預測其對同合子家族性高膽固醇血症 (HoFH) 有額外價值，此預測已獲文獻強力支持。

## 快速總覽
| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性高膽固醇血症、混合型血脂異常、動脈粥狀硬化心血管疾病風險降低 |
| 預測新適應症 | 同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia) |
| TxGNN 預測分數 | 99.48% |
| 證據等級 | L3 (多篇文獻支持，真實世界數據) |
| 台灣上市 | 已上市 |
| 許可證數 | 1 |
| 建議決策 | Go |

<!-- review:begin bempedoic-acid-hofh-rereview-2026-10-03 -->

> **待重審（2026-10-03）**：HoFH 這筆預測的首要理由（非 LDL 受體依賴）與仿單所載機轉不符（見下方「為什麼這個預測合理」的查核加註），已標記待重審；證據等級、文獻與決策在重審完成前不更動。依據：[DailyMed：NEXLETOL（bempedoic acid）美國仿單 §12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9)。

<!-- review:end bempedoic-acid-hofh-rereview-2026-10-03 -->

## 為什麼這個預測合理？
Bempedoic acid 透過抑制 ATP 檸檬酸裂解酶 (ACL) 降低膽固醇合成，作用位點在 HMG-CoA 還原酶的上游。對 HoFH 患者的關鍵優勢：
1. **非 LDL 受體依賴機制**：HoFH 患者 LDL 受體功能缺損或缺失，傳統 statin 和 PCSK9 抑制劑效果受限
2. **與現有療法協同**：可與 statin、ezetimibe、PCSK9 抑制劑等合併使用
3. **不依賴肌肉代謝**：作為前藥僅在肝臟活化，不會在肌肉細胞中活化，減少肌肉相關副作用

<!-- review:begin bempedoic-acid-ldlr-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：此前提與仿單不符。仿單寫明 bempedoic acid 抑制肝臟 ACL、減少膽固醇合成後，是「經由上調 LDL 受體」降低血中 LDL-C，和 statin 一樣依賴 LDL 受體，不是非 LDL 受體依賴的機制。上段原文保留未改。依據：[DailyMed：NEXLETOL（bempedoic acid）美國仿單 §12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9)。

<!-- review:end bempedoic-acid-ldlr-premise-2026-10-03 -->

## 臨床試驗證據
| 試驗編號 | 階段 | 狀態 | 收案人數 | 主要發現 |
|----------|------|------|----------|----------|
| - | - | - | - | (無專門 HoFH 的註冊臨床試驗) |

## 文獻證據
| PMID | 年份 | 標題 | 相關性 |
|------|------|------|--------|
| 41274797 | 2026 | Real-world evaluation of bempedoic acid use in patients with homozygous familial hypercholesterolemia | 直接相關：HoFH 患者使用 bempedoic acid 的真實世界數據 |
| 41106315 | 2025 | Breaking barriers: Innovative therapies for managing homozygous familial hypercholesterolemia | 綜述 HoFH 新療法，包含 bempedoic acid |
| 35466160 | 2022 | Advancements in the Treatment of Homozygous Familial Hypercholesterolemia | HoFH 治療進展，提及 bempedoic acid |
| 33766264 | 2021 | New and Emerging Therapies for Reduction of LDL-Cholesterol | LDL-C 降低新療法，涵蓋 HoFH 應用 |
| 29449335 | 2018 | Bempedoic Acid Lowers LDL-C in LDLR-Deficient Yucatan Miniature Pigs | 前臨床研究：在 LDL 受體缺陷動物模型中證實療效 |

## 台灣上市資訊
| 許可證號 | 中文品名 | 劑型 | 許可證持有者 | 效期 |
|----------|----------|------|--------------|------|
| 衛部藥輸字第028817號 | 寧脂德膜衣錠180毫克 | 膜衣錠 | 台灣第一三共 | 2029/11/05 |

## 安全性考量
- **Major 交互作用**：
  - 類固醇類：hydrocortisone, prednisone, prednisolone, methylprednisolone, dexamethasone, betamethasone, budesonide, deflazacort, fludrocortisone
  - Simvastatin：增加肌病風險，劑量需限制在 20mg
  - Levofloxacin：增加肌腱病變風險
- **Moderate 交互作用**：
  - Rosuvastatin：建議劑量不超過 40mg
  - 多種其他藥物

## 結論與下一步
**決策：Go**
**理由：** TxGNN 的預測已獲得大量文獻支持，包括 2026 年最新發表的真實世界數據研究。Bempedoic acid 對 HoFH 的療效機轉明確，且已有多篇綜述文章將其列為 HoFH 治療選項之一。藥物已在台灣上市，具備立即臨床應用的條件。
**若要推進需要：**
1. 與心臟科/脂質門診合作，在 HoFH 患者中開始使用
2. 收集台灣 HoFH 患者使用經驗，建立本土數據
3. 考慮申請適應症擴展
4. 注意與 simvastatin 的交互作用，避免超過建議劑量

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「非 LDL 受體依賴機制」 | 加註 | [DailyMed：NEXLETOL（bempedoic acid）美國仿單 §12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |
| 2026-10-03 | 同合子家族性高膽固醇血症預測標記待重審 | 標記待重審 | [DailyMed：NEXLETOL（bempedoic acid）美國仿單 §12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

