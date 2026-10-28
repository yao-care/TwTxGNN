---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
last_modified_at: 2026-10-16
description: "Bevacizumab：預測新適應症為會厭腫瘤 (Epiglottis Neoplasm)（證據等級 L5）。原適應症：轉移性大腸直腸癌（mCRC）：與含 5-fluorouracil 的化學療法併用，作為第一線治療"
---

# Bevacizumab
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

## Bevacizumab：從轉移性大腸直腸癌到會厭腫瘤
{: .text-alpha }

## 一句話總結

Bevacizumab 是一種抗血管內皮生長因子（VEGF）的單株抗體，原本用於轉移性大腸直腸癌、乳癌、神經膠母細胞瘤、肺癌、卵巢癌與子宮頸癌等治療。
TxGNN 模型預測它可能對**會厭腫瘤 (Epiglottis Neoplasm)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，證據僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性大腸直腸癌（mCRC）：與含 5-fluorouracil 的化學療法併用，作為第一線治療 |
| 預測新適應症 | 會厭腫瘤 (Epiglottis Neoplasm) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 5 張／共 8 張） |
| 許可證數 | 8 張（有效單方 5／有效複方 0／已註銷 3） |
| 建議決策 | Hold |

<!-- review:begin bevacizumab-epiglottis-rereview-result-2026-10-03 -->

> **重審結果（2026-10-03）**：**撤回**（證據等級 L5 不變）。本筆重審的對象是 2026-10-03 版報告；當時的主要理由「已核准用於頭頸部鱗癌」不成立，剩下的只是通用的抗血管新生機轉；查無會厭腫瘤的專屬研究。最接近的證據是頭頸部鱗癌（含喉癌）的第三期試驗：加上 bevacizumab 後整體存活沒有改善，3–5 級出血與治療相關死亡增加（[PMID 31618129](https://pubmed.ncbi.nlm.nih.gov/31618129/)，[NCT00588770](https://clinicaltrials.gov/study/NCT00588770)）；另一項第二期試驗也是毒性增加、療效沒有提升（[PMID 27177865](https://pubmed.ncbi.nlm.nih.gov/27177865/)），因此撤回此推論。2026-10-15 重生的報告已不再寫頭頸部鱗癌核准，證據等級 L5、決策 Hold，與重審結論一致；上述相近族群的反面證據新報告未提及。依據：[PubMed：Phase III Randomized Trial of Chemotherapy With or Without Bevacizumab in Patients With Recurrent or Metastatic Head and Neck Cancer（PMID 31618129）](https://pubmed.ncbi.nlm.nih.gov/31618129/)；[ClinicalTrials.gov：Chemotherapy With or Without Bevacizumab in Treating Patients With Recurrent or Metastatic Head and Neck Squamous Cell Carcinoma（NCT00588770）](https://clinicaltrials.gov/study/NCT00588770)；[PubMed：Phase II randomized trial of radiation therapy, cetuximab, and pemetrexed with or without bevacizumab in patients with locally advanced head and neck cancer（PMID 27177865）](https://pubmed.ncbi.nlm.nih.gov/27177865/)；[ClinicalTrials.gov：Testing the Use of Investigational Drugs Atezolizumab and/or Bevacizumab With or Without Standard Chemotherapy in the Second-Line Treatment of Advanced-Stage Head and Neck Cancers（NCT05063552）](https://clinicaltrials.gov/study/NCT05063552)。

<!-- review:end bevacizumab-epiglottis-rereview-result-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Bevacizumab 是中和 VEGF-A 的單株抗體，理論上可抑制腫瘤血管新生，進而限制腫瘤生長。

原適應症（大腸直腸癌、肺癌、卵巢癌等）都是依賴血管新生的實體腫瘤，而會厭腫瘤同屬頭頸部腫瘤。從機轉上看，抗血管新生策略有可能適用，但這只是一般性的推論。

需要注意：目前沒有針對會厭腫瘤的臨床或文獻證據，這項預測的合理性僅建立在 TxGNN 模型分數與通用的抗血管新生機轉上。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Bevacizumab 的不重複許可證共 **8 張**：有效單方 5 張、有效複方 0 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署菌疫輸字第000807號 | 癌思停 注射劑 | 注射劑 | 羅氏大藥廠股份有限公司 | 2030/05/24 | 1. 轉移性大腸直腸癌 (mCRC)： Avastin (bevacizumab) 與含有5-fluorouracil為基礎的化學療法合併使用，可以作為轉移性大腸或直腸癌病人的第一… |
| 衛部菌疫輸字第001117號 | 艾法施注射液 | 注射液劑 | 台灣安進藥品有限公司 | 2029/12/17 | 1.轉移性大腸直腸癌(mCRC)：(1)與含有5-fluorouracil為基礎的化學療法合併使用，可以作為轉移性大腸或直腸癌病人的第一線治療。(2)與含有5-fluorourac… |
| 衛部菌疫輸字第001156號 | 癌畢弭 注射劑 | 注射液劑 | 台灣生資科技股份有限公司 | 2031/06/29 | 一、轉移性大腸直腸癌 ( mCRC )： (1)與含有5-fluorouracil為基礎的化學療法合併使用，可以作為轉移性大腸或直腸癌病人的第一線治療。 (2)與含有5-fluor… |
| 衛部菌疫輸字第001185號 | 艾麥思注射劑 | 注射劑 | 美時化學製藥股份有限公司 | 2032/01/14 | 1. 轉移性大腸直腸癌 (mCRC)： (1) 與含有5-fluorouracil為基礎的化學療法合併使用，可以作為轉移性大腸或直腸癌病人的第一線治療。 (2) 與含有5-fluo… |
| 衛部菌疫輸字第001245號 | 衛癌瑪注射液 | 注射液劑 | 台灣賽特瑞恩有限公司 | 2029/01/09 | 轉移性大腸直腸癌(mCRC) 與含有5-fluorouracil為基礎的化學療法合併使用，可以作為轉移性大腸或直腸癌病人的第一線治療。 與含有5-fluorouracil/leuc… |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署菌疫輸字第000874號</td><td>癌思停 注射劑 (瑞士廠)</td><td>BEVACIZUMAB</td><td>2017/08/04</td></tr><tr><td>衛部菌疫輸字第001146號</td><td>力癌停注射劑</td><td>BEVACIZUMAB</td><td>2025/07/23</td></tr><tr><td>衛部菌疫輸字第001193號</td><td>安備咨注射劑25毫克/毫升</td><td>BEVACIZUMAB</td><td>2024/03/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 VEGF 單株抗體），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 22 項交互作用。屬於**嚴重（Major）**等級者包括 Deferiprone、Samarium (153Sm) lexidronam、Panitumumab、Sunitinib、Thalidomide。其餘多為中度（Moderate），例如雙磷酸鹽類（Alendronic acid、Risedronic acid、Pamidronic acid 等）、Filgrastim、Pegfilgrastim、Sargramostim 等。

其他警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 會厭腫瘤的預測分數雖高（0.9990），但沒有任何臨床試驗或文獻支持，證據等級僅為 L5。
- 機轉資料也不完整，目前無法以證據支持進一步推進。

**若要推進需要：**
- 補充詳細的作用機轉（MOA）資料。
- 進行會厭及相關頭頸部腫瘤的文獻與臨床試驗系統性檢索。
- 釐清此預測疾病的實際臨床定義，以及與原適應症的關聯。
- 評估頭頸部癌前臨床與早期臨床資料，再決定是否設計探索性研究。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「已核准用於頭頸部鱗狀細胞癌(HNSCC)的治療」 | 報告重生後已無此錯誤（2026-10-15：新報告未再寫 bevacizumab 已核准用於頭頸部鱗狀細胞癌；原為加註） | [DailyMed：AVASTIN（bevacizumab）美國仿單 §1 Indications and Usage](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 會厭腫瘤預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [DailyMed：AVASTIN（bevacizumab）美國仿單 §1 Indications and Usage](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「Vegzelma (艾法施) - 信東」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「ABEVMY - 三星生技」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 會厭腫瘤預測重審結果 | 重審：撤回，證據等級 L5 不變（2026-10-16 修訂，前版保留於紀錄） | [PubMed：Phase III Randomized Trial of Chemotherapy With or Without Bevacizumab in Patients With Recurrent or Metastatic Head and Neck Cancer（PMID 31618129）](https://pubmed.ncbi.nlm.nih.gov/31618129/)；[ClinicalTrials.gov：Chemotherapy With or Without Bevacizumab in Treating Patients With Recurrent or Metastatic Head and Neck Squamous Cell Carcinoma（NCT00588770）](https://clinicaltrials.gov/study/NCT00588770)；[PubMed：Phase II randomized trial of radiation therapy, cetuximab, and pemetrexed with or without bevacizumab in patients with locally advanced head and neck cancer（PMID 27177865）](https://pubmed.ncbi.nlm.nih.gov/27177865/)；[ClinicalTrials.gov：Testing the Use of Investigational Drugs Atezolizumab and/or Bevacizumab With or Without Standard Chemotherapy in the Second-Line Treatment of Advanced-Stage Head and Neck Cancers（NCT05063552）](https://clinicaltrials.gov/study/NCT05063552) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

