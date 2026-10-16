---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

# Fidaxomicin：從困難梭狀桿菌相關腹瀉到葡萄球菌燙傷樣皮膚症候群

## 一句話總結

Fidaxomicin 是一種窄譜的口服巨環內酯類抗生素，原本用於治療困難梭狀桿菌相關腹瀉（CDAD）。
TxGNN 模型預測它可能對**葡萄球菌燙傷樣皮膚症候群 (Staphylococcal Scalded Skin Syndrome)** 有效，
但目前**沒有任何臨床試驗或直接相關文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 困難梭狀桿菌相關腹瀉 (C. difficile-associated diarrhoea, CDAD) |
| 預測新適應症 | 葡萄球菌燙傷樣皮膚症候群 (Staphylococcal Scalded Skin Syndrome) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fidaxomicin 是一種抑制細菌 RNA 聚合酶的窄譜巨環內酯類抗生素，對部分革蘭氏陽性菌（包含金黃色葡萄球菌）在體外具有活性。這是模型預測唯一可能的機轉連結。

然而，這個連結相當薄弱。葡萄球菌燙傷樣皮膚症候群是由金黃色葡萄球菌所產生的毒素介導的全身性疾病，而 Fidaxomicin 幾乎不被全身吸收，難以在皮膚或血液中達到有效濃度。此外，現有的標準治療已相當完善。

整體而言，此預測僅來自 TxGNN 模型，沒有臨床或前臨床證據佐證，應視為假說性質。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無針對此預測適應症的直接相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Fidaxomicin 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025757號 | 鼎腹欣膜衣錠 200 毫克 | 膜衣錠 | 美商默沙東藥廠股份有限公司台灣分公司 | 2027/09/07 | 困難梭狀桿菌相關腹瀉(C. difficile-associated diarrhoea, CDAD) |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共記錄 79 筆交互作用，其中須特別注意者：
  - **重大 (Major)**：霍亂弧菌活疫苗 (Vibrio cholerae CVD 103-HgR strain live antigen)
  - **中度 (Moderate)**：Alpelisib、Apalutamide、Binimetinib、Picosulfuric acid
  - 其餘列出者多為輕微 (Minor) 等級，例如 Nifedipine、Amiodarone、Diltiazem、Verapamil、Clarithromycin、Erythromycin、Cyclosporine 等

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自 TxGNN 模型（證據等級 L5），沒有臨床試驗或直接文獻支持。
- Fidaxomicin 幾乎不被全身吸收，無法對毒素介導的全身性皮膚疾病發揮作用，機轉上缺乏合理性。

**若要推進需要：**
- 詳細的作用機轉資料（MOA）
- 體外與動物模型證據，證明對相關金黃色葡萄球菌菌株及疾病模型有效
- 評估藥物遞送可行性（例如是否需要全新的外用或全身性劑型）
- 與現有標準治療比較的臨床價值評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 作用機轉寫成「σ 因子釋放步驟」 | 報告重生後已無此錯誤（2026-10-15：新報告機轉只寫抑制細菌 RNA 聚合酶，未再寫 σ 因子釋放步驟；新報告另寫對金黃色葡萄球菌在體外有活性，有體外研究支持（Biedenbach 等，Antimicrob Agents Chemother 2010，PMC2863674）；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [DailyMed：DIFICID（fidaxomicin）仿單（Merck），12.4 Microbiology／12.3 Pharmacokinetics](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb)；[EMA：DIFICLIR（fidaxomicin）產品資訊（SmPC）§5.1、§5.2](https://www.ema.europa.eu/en/documents/product-information/dificlir-epar-product-information_en.pdf)；[PubChem：Fidaxomicin（CID 10034073），Pharmacology and Biochemistry › Mechanism of Action（DrugBank 提供）](https://pubchem.ncbi.nlm.nih.gov/compound/10034073) |
| 2026-10-03 | 口服生體可用率寫「< 1%」 | 報告重生後已無此錯誤（2026-10-15：新報告只寫幾乎不被全身吸收，未再寫生體可用率 < 1%；原為加註） | [EMA：DIFICLIR（fidaxomicin）產品資訊（SmPC）§5.1、§5.2](https://www.ema.europa.eu/en/documents/product-information/dificlir-epar-product-information_en.pdf)；[DailyMed：DIFICID（fidaxomicin）仿單（Merck），12.4 Microbiology／12.3 Pharmacokinetics](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

