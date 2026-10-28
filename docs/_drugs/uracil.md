---
layout: default
title: Uracil
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
monitor_inn: "Uracil"
predicted_indications: ["colonic neoplasm", "gastric carcinoma", "rectosigmoid junction neoplasm", "lipoma of colon", "colonic lymphangioma", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "cavernous hemangioma of colon", "cecal disease", "colon leiomyoma"]
last_modified_at: 2026-10-23
description: "Uracil：預測新適應症為大腸腫瘤 (Colonic Neoplasm)（證據等級 L5）。原適應症：抗惡性腫瘤劑"
---

# Uracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Uracil：從抗惡性腫瘤劑到大腸腫瘤
{: .text-alpha }

## 一句話總結

Uracil（尿嘧啶）在台灣的單一成分許可證核准用途為「抗惡性腫瘤劑」，也是 UFT（tegafur-uracil）等複方的成分。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效。
目前彙整到 **1 個臨床試驗**（未直接測試 uracil）和 **20 篇文獻**，多數為 UFT 複方的研究或綜述，並非 uracil 單獨使用的證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗惡性腫瘤劑 |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 0.9950 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 5 張／共 7 張） |
| 許可證數 | 7 張（有效單方 2／有效複方 3／已過期 1／已註銷 1） |
| 建議決策 | Hold |

證據等級說明：所列的臨床試驗（NCT04164069）是 dasatinib 預防奧沙利鉑神經病變的研究，文獻也沒有直接研究 uracil 單方用於大腸腫瘤的臨床試驗，因此依規則定為 L5。資料中的 L3 評級僅反映間接文獻。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。不過，文獻顯示 uracil 是 UFT（tegafur-uracil）的調節成分。它競爭性抑制二氫嘧啶去氫酶（DPD），減少 5-FU 的分解，使 tegafur 轉化而來的 5-FU 在腫瘤中維持較高濃度。

大腸腫瘤是 fluoropyrimidine 類藥物的主要治療對象，因此 TxGNN 的預測在機轉上有線索。但現有證據（例如台灣健保資料庫的 UFT 與 5-FU 輔助化療世代研究、ACTS-CC 02 的 phase III 試驗，其對照組為 UFT/LV）都是以 UFT 複方為研究對象，無法推論 uracil 單獨使用有效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04164069](https://clinicaltrials.gov/study/NCT04164069) | Phase 1 | 完成 | 9 | 以 dasatinib 預防胃腸道癌患者接受 FOLFOX 後的奧沙利鉑神經病變；未評估 uracil，僅為疾病背景的弱相關資料 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT（phase III） | Clin Colorectal Cancer | 高風險 Stage III 結腸癌輔助治療中，S-1 加奧沙利鉑與 UFT/LV 比較（UFT/LV 為對照組） |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT 長期追蹤 | ESMO Open | ACTS-CC 02 試驗的 5 年存活更新；SOX 的無病存活期未優於 UFT/LV |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | 以 OK-432 免疫化學療法與口服嘧啶類（含 UFT）作為大腸直腸癌輔助治療的比較 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 世代研究與統合分析 | Medicine | 台灣全國資料庫比較 Stage II/III 結腸癌輔助治療 UFT 與 5-FU 的存活結果 |
| [37903983](https://pubmed.ncbi.nlm.nih.gov/37903983/) | 2023 | 世代研究 | Int J Colorectal Dis | JFMC46-1201 試驗的事後分析，探討高風險 Stage II 結腸癌的預後因子 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT 作為肺、胃、結直腸及乳癌術後輔助化療的臨床證據與機轉 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | 亞洲轉移性大腸直腸癌治療指引共識 |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | 病例報告 | Cancer Chemother Pharmacol | 轉移性結腸癌患者使用 UFT 後出現溶血性貧血 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Uracil 的不重複許可證共 **7 張**：有效單方 2 張、有效複方 3 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥製字第062093號 | ＂霖揚＂尿嘧啶 | （粉） | 霖揚生技製藥股份有限公司 | 2030/12/29 | 抗惡性腫瘤劑 |
| 衛部藥製字第062102號 | ＂杏國＂尿嘧啶 | （粉） | 杏國新藥股份有限公司 | 2031/01/05 | 抗惡性腫瘤劑 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（3 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第043698號 | 友復　膠囊 | TEGAFUR (FTORAFUR)、URACIL | 膠囊劑 | 胃癌、大腸(結腸直腸)癌、乳癌、與Cisplatin併用治療轉移及末期肺癌、頭頸部癌、用於病理分期T2之第一期B肺腺癌病人手術後輔助治療。 |
| 衛署藥製字第049563號 | 〝美時〞復癒 膠囊 | URACIL、TEGAFUR (FTORAFUR) | 膠囊劑 | 胃癌、大腸（結腸直腸）癌、乳癌、頭頸部鱗狀上皮癌、與cisplatin 併用治療轉移及末期肺癌、用於病理分期T2 之第一期B 肺腺癌病人手術後輔助治療。 |
| 衛署藥輸字第023484號 | 優富多膠囊 | URACIL、TEGAFUR (FTORAFUR) | 膠囊劑 | 胃癌、結腸癌、大腸癌、乳癌、與CISPLATIN併用治療轉移及末期肺癌、頭頸部癌、用於病理分期T2之第一期B肺腺癌病人手術後輔助治療。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛部藥製字第060268號</td><td>"博謙"尿嘧啶</td><td>Uracil</td><td>2024/04/08</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥陸輸字第000668號</td><td>尿嘧啶</td><td>Uracil</td><td>2026/06/11</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗惡性腫瘤劑；在 UFT 中作為 fluoropyrimidine（5-FU 前驅藥 tegafur）的調節成分 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；一般 fluoropyrimidine 治療常見監測 CBC、肝腎功能 |
| 處置防護 | 請參考原廠仿單，並依院內細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

補充：文獻中有 UFT 治療轉移性結腸癌患者出現溶血性貧血的病例報告，屬單一病例，僅供警覺。

## 結論與下一步

**決策：Hold**

**理由：**
- 台灣單方 uracil 的許可證僅載明「抗惡性腫瘤劑」，TxGNN 對大腸腫瘤的預測目前只有 UFT 複方的間接證據，沒有直接以 uracil 為對象、針對大腸腫瘤的研究，因此證據等級為 L5。
- uracil 在 UFT 中的角色是 DPD 抑制劑，其療效來自與 tegafur 的搭配，單獨使用的臨床意義不明。

**若要推進需要：**
- 補充 uracil 的作用機轉資料（MOA）
- 釐清 uracil 單獨使用與作為 UFT 組成的差異，並確認有無直接以 uracil 為對象、針對大腸腫瘤的研究
- 安全性資料（警語、禁忌、藥物交互作用）以原廠仿單為準，並建立監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」寫甲狀腺機能亢進症 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表把 trastuzumab（曲斯若）列為含 uracil 製劑（衛部菌疫輸字第001135號） | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表把 trastuzumab（曲斯若）列為含 uracil 製劑（衛部菌疫輸字第001136號） | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 一句話總結把 methylthiouracil 的適應症當成 uracil | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 標題以甲狀腺機能亢進症為原用途 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 預測理由稱 uracil 單方許可證適應症為甲狀腺機能亢進 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 結論稱 uracil 單方許可證適應症為甲狀腺機能亢進 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 下一步稱 UFT 許可證需另行確認 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

