---
layout: default
title: Hexachlorophene
parent: 中證據等級 (L3-L4)
nav_order: 120
evidence_level: L3
indication_count: 1
---

# Hexachlorophene
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Hexachlorophene：從皮膚抑菌消毒到廣義皮膚病 (Skin Disease)

## 一句話總結

Hexachlorophene（六氯酚）是歷史悠久的外用廣效抗菌劑，台灣核准用於皮膚消毒殺菌、外科擦拭、以及濕疹與皮膚炎等皮膚症狀。TxGNN 模型在 10 個預測適應症中，以**廣義皮膚病 (Skin Disease)** 的臨床證據最為充分，目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向，建議在嚴格安全條件下推進評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 濕疹、腫痛、皮膚炎、搔癢與蟲咬 |
| 預測新適應症 | 廣義皮膚病 (Skin Disease) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏正式記錄的作用機轉資料（MOA 資料缺口）。根據現有資訊，Hexachlorophene 是一種有機氯類外用抗菌劑，歷史應用中以**干擾革蘭氏陽性菌細胞膜通透性、抑制膜結合酶系統**為主要殺菌途徑，對金黃色葡萄球菌（包括 MRSA）和鏈球菌具有強效活性。此外，Guide to PHARMACOLOGY 資料庫顯示，Hexachlorophene 可能抑制 N-Acylphosphatidylethanolamine-phospholipase D（NAPEPLD），並有初步文獻提示可透過 SHP2 抑制路徑干擾 RAS/MEK/ERK 及 PI3K/AKT 訊號（PMID: 32284327），後者屬藥理學靶點資料，臨床意義尚待釐清。

原核准用途（皮膚消毒、外科擦拭、嬰兒室葡萄球菌去定植）與「廣義皮膚病」的關聯性相當直接——臨床試驗 NCT01049438 直接以 Hexachlorophene 全身洗浴作為 MRSA 皮膚去定植的核心干預，明確支持其對細菌性皮膚感染的管理能力。多項文獻亦顯示，停用 Hexachlorophene 沐浴後新生兒葡萄球菌皮膚感染率顯著上升，反向驗證了其皮膚防護效果。

然而需特別留意：Hexachlorophene 在 FDA 的核准外用用途**已全面停用**，主要原因是早產兒皮膚吸收所致的中樞神經系統空泡化病變。任何新適應症的推進，都必須嚴格界定安全的目標族群，並排除神經毒性高風險族群（早產兒、新生兒）。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01049438](https://clinicaltrials.gov/study/NCT01049438) | N/A | 完成 | 31 | 前瞻性試驗：鼻腔 Mupirocin＋Hexachlorophene 全身洗浴＋全身性抗生素三聯療法，驗證對社區型 MRSA 復發性皮膚感染去定植的效果 |
| [NCT00532324](https://clinicaltrials.gov/study/NCT00532324) | N/A | 完成 | 107 | 前瞻性世代研究：評估孕婦金黃色葡萄球菌（含 CA-MRSA）的臨床與分子流行病學，提供皮膚病原菌背景資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [958762](https://pubmed.ncbi.nlm.nih.gov/958762/) | 1976 | 世代研究 | Pediatrics | 五期序列研究：3% Hexachlorophene 全身沐浴期間金黃色葡萄球菌定植率最低；停用後定植率升至 80%、感染率 9.5% |
| [1143981](https://pubmed.ncbi.nlm.nih.gov/1143981/) | 1975 | 世代研究 | Pediatrics | 停用 Hexachlorophene 後嬰兒室爆發鏈球菌／葡萄球菌皮膚感染；嚴格無菌技術比恢復使用 Hexachlorophene 更具長期控制效果 |
| [958085](https://pubmed.ncbi.nlm.nih.gov/958085/) | 1976 | 世代研究 | Med J Australia | 81,756 例出生分析：早產兒使用 3% Hexachlorophene 乳劑洗浴可發生中樞神經系統空泡化病變；足月兒長期追蹤未見神經後遺症 |
| [4834430](https://pubmed.ncbi.nlm.nih.gov/4834430/) | 1974 | 對照研究 | Can Med Assoc J | 158 對 156 例新生兒比較：Hexachlorophene vs Lactacyd 洗浴對鼻腔及臍帶金黃色葡萄球菌定植率的差異 |
| [25017526](https://pubmed.ncbi.nlm.nih.gov/25017526/) | 2014 | 其他 | J Allergy Clin Immunol Pract | 異位性皮膚炎合併反覆 MRSA 皮膚感染管理回顧，涵蓋 S. aureus 去定植治療策略（含 Hexachlorophene 洗浴） |
| [6643773](https://pubmed.ncbi.nlm.nih.gov/6643773/) | 1983 | 回顧 | J Am Acad Dermatol | 手術抗菌劑回顧：比較 Hexachlorophene、Chlorhexidine、Benzalkonium chloride 及 Povidone-iodine 的皮膚消毒效果 |
| [12418624](https://pubmed.ncbi.nlm.nih.gov/12418624/) | 2002 | 回顧 | MMWR | CDC/HICPAC 醫療場所手部衛生指引；含 Hexachlorophene 手術抗菌應用的歷史評估與現行建議 |
| [15060207](https://pubmed.ncbi.nlm.nih.gov/15060207/) | 2004 | 回顧 | Pediatrics | 兒童皮膚屏障與環境暴露回顧；涵蓋 Hexachlorophene 新生兒皮膚護理的毒性疑慮及監管歷史 |
| [123433](https://pubmed.ncbi.nlm.nih.gov/123433/) | 1975 | 病例系列 | Arch Dermatol | 皂類粉刺原性評估：含 Hexachlorophene 的殺菌皂具輕度粉刺原性，可能加重痤瘡患者皮膚狀況 |
| [2235790](https://pubmed.ncbi.nlm.nih.gov/2235790/) | 1990 | 其他 | Postgrad Med | 陰囊搔癢症鑑別診斷與治療，涵蓋外用抑菌劑在皮膚炎症及感染症狀管理中的應用場景 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第012461號 | 脫濕美軟膏 | 軟膏劑 | 濕疹、腫痛、皮膚炎、搔癢與蟲咬 |
| 內衛藥製字第005898號 | 菲克斯潔膚消毒漿 | 外用液劑 | 外科擦拭用、供皮膚抑菌目的使用之清潔劑 |
| 內衛藥製字第005793號 | 康速龍軟膏 | 乳膏劑 | 急慢性皮膚炎及皮膚過敏症 |
| 衛署藥製字第000974號 | "惠民" 柔和潔乳白軟膏（六氯酚） | 軟膏劑 | 外科擦拭用、供皮膚抑菌使用目的之清潔劑 |
| 衛署成製字第008210號 | 諾德露洗劑 | 洗劑 | 體臭、止汗 |

---

## 安全性考量

**藥物-靶點交互作用：**
根據 Guide to PHARMACOLOGY 資料庫，Hexachlorophene 可抑制人類 N-Acylphosphatidylethanolamine-phospholipase D（NAPEPLD，Ensembl: ENSG00000161048），並有初步文獻（PMID: 32284327）提示可能透過 SHP2 抑制途徑，干擾 RAS/MEK/ERK 及 PI3K/AKT 訊號路徑，在 KRAS 突變癌細胞中產生抗增殖效果。此為藥理學靶點資料，臨床藥物交互作用意義尚待進一步評估。

**重要安全背景：**
FDA 核准的 Hexachlorophene 外用品已全面停用（discontinued）。主要安全疑慮為**新生兒（尤其早產兒）透過皮膚吸收導致中樞神經系統空泡化病變**（見 PMID: 958085），黃疸為早產兒的加重因子。台灣現有 20 張許可證均為外用劑型，應嚴格遵守核准適應症及濃度限制，不得用於新生兒全身性洗浴。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Hexachlorophene 在細菌性皮膚感染（尤其 MRSA 皮膚去定植）方面有歷史應用紀錄及前瞻性臨床試驗直接支持，機轉基礎明確；惟 FDA 已停用其核准用途，已知神經毒性安全疑慮（特別針對早產兒／新生兒族群）構成顯著限制，須在嚴格安全監控框架下方可推進。

**若要推進需要：**
- 補充完整的作用機轉資料（DrugBank MOA 查詢 DB00756）
- 明確界定安全的目標族群（成人為主，排除早產兒、新生兒），建立神經毒性監測計畫
- 聚焦具明確機轉依據的皮膚病亞型（如 MRSA 相關復發性皮膚感染、外科部位皮膚去定植），避免機轉不明的廣義適應症申請
- 進行台灣法規可行性評估：在 FDA 已停用背景下，現有台灣許可證的延伸使用路徑及監管策略
- 確認現有製劑濃度、劑型是否符合擬議新適應症的藥學需求

---

