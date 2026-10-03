---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Bevacizumab：從多種癌症到會厭腫瘤

## 一句話總結
Bevacizumab 原為抗血管新生的癌症標靶藥物，用於轉移性大腸直腸癌、肺癌、卵巢癌等多種惡性腫瘤，TxGNN 預測其可能對會厭腫瘤(epiglottis neoplasm)有治療潛力。

## 快速總覽
| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性大腸直腸癌、乳癌、非小細胞肺癌、卵巢癌、子宮頸癌、神經膠母細胞瘤等 |
| 預測新適應症 | 會厭腫瘤 (epiglottis neoplasm) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 (僅預測) |
| 台灣上市 | 已上市 |
| 許可證數 | 8 張（有效單方 5／有效複方 0／已註銷 3） |
| 建議決策 | Hold（2026-10-03 重審撤回此推論） |

<!-- review:begin bevacizumab-epiglottis-rereview-result-2026-10-03 -->

> **重審結果（2026-10-03）**：**撤回**（證據等級 L5 不變）。原推論的主要理由「已核准用於頭頸部鱗癌」不成立，剩下的只是通用的抗血管新生機轉。查無會厭腫瘤的專屬研究。最接近的證據是頭頸部鱗癌（含喉癌）的第三期試驗：加上 bevacizumab 後整體存活沒有改善，3–5 級出血與治療相關死亡增加（[PMID 31618129](https://pubmed.ncbi.nlm.nih.gov/31618129/)，[NCT00588770](https://clinicaltrials.gov/study/NCT00588770)）。另一項第二期試驗也是毒性增加、療效沒有提升（[PMID 27177865](https://pubmed.ncbi.nlm.nih.gov/27177865/)）。本頁快速總覽「建議決策」已依重審結果更新，原值列在下方查核紀錄。依據：[PubMed：Phase III Randomized Trial of Chemotherapy With or Without Bevacizumab in Patients With Recurrent or Metastatic Head and Neck Cancer（PMID 31618129）](https://pubmed.ncbi.nlm.nih.gov/31618129/)；[ClinicalTrials.gov：Chemotherapy With or Without Bevacizumab in Treating Patients With Recurrent or Metastatic Head and Neck Squamous Cell Carcinoma（NCT00588770）](https://clinicaltrials.gov/study/NCT00588770)；[PubMed：Phase II randomized trial of radiation therapy, cetuximab, and pemetrexed with or without bevacizumab in patients with locally advanced head and neck cancer（PMID 27177865）](https://pubmed.ncbi.nlm.nih.gov/27177865/)；[ClinicalTrials.gov：Testing the Use of Investigational Drugs Atezolizumab and/or Bevacizumab With or Without Standard Chemotherapy in the Second-Line Treatment of Advanced-Stage Head and Neck Cancers（NCT05063552）](https://clinicaltrials.gov/study/NCT05063552)。

<!-- review:end bevacizumab-epiglottis-rereview-result-2026-10-03 -->

## 為什麼這個預測合理？
Bevacizumab 是一種人源化單株抗體，透過結合血管內皮生長因子(VEGF)來抑制腫瘤血管新生。其作用機轉具有廣泛的抗腫瘤活性：

1. **血管新生抑制**：阻斷 VEGF 訊號傳導，減少腫瘤血管形成
2. **頭頸部癌症經驗**：已核准用於頭頸部鱗狀細胞癌(HNSCC)的治療
3. **解剖位置相關**：會厭屬於頭頸部區域，與已核准適應症的頭頸部癌症有相似的血管生成特性

<!-- review:begin bevacizumab-hnscc-not-approved-2026-10-03 -->

> **查核加註（2026-10-03）**：此前提與仿單不符。美國 Avastin 仿單與台灣 5 張有效 bevacizumab 許可證的核准適應症都不含頭頸部鱗狀細胞癌（美國仿單列的是大腸直腸癌、非鱗狀非小細胞肺癌、神經膠母細胞瘤、腎細胞癌、子宮頸癌、卵巢癌與肝細胞癌）。上段原文保留未改。依據：[DailyMed：AVASTIN（bevacizumab）美國仿單 §1 Indications and Usage](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end bevacizumab-hnscc-not-approved-2026-10-03 -->

會厭腫瘤雖為罕見疾病，但其血管供應特性與其他頭頸部腫瘤相似，理論上可能對抗血管新生治療有反應。

## 臨床試驗證據
目前無針對 bevacizumab 治療會厭腫瘤的臨床試驗登記。

然而，相關的頭頸部癌症臨床試驗包括：
- **NCT01552434**：Phase I 試驗，評估 bevacizumab 與 temsirolimus 在晚期惡性腫瘤的應用
- **NCT00023959**：Phase I 試驗，評估 bevacizumab 合併化放療治療預後不良的頭頸部癌症

## 文獻證據
PubMed 檢索發現有關於 bevacizumab 在頭頸部癌症的臨床前研究：

- Bozec A 等人(2008)發表於 *British Journal of Cancer*，證實 bevacizumab 合併 erlotinib 及放療在頭頸部腫瘤正位模式中的抗腫瘤效果
- 多篇研究支持抗 VEGF 療法在頭頸部腫瘤的應用潛力

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Bevacizumab 的不重複許可證共 **8 張**：有效單方 5 張、有效複方 0 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（5 張）

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

Bevacizumab 在台灣有多項藥品許可證：
- **Avastin (癌思停)** - 羅氏
- **MVASI** - 安進
- **ABEVMY (癌畢弭)** - 台灣生資科技
- **Vegzelma (衛癌瑪)** - 台灣賽特瑞恩

<!-- review:begin bevacizumab-vegzelma-name-holder-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「- **Vegzelma (艾法施)** - 信東」。TFDA 登載 Vegzelma 的中文品名是「衛癌瑪注射液」（衛部菌疫輸字第001245號），申請商為台灣賽特瑞恩；「艾法施注射液」是 MVASI（台灣安進）。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end bevacizumab-vegzelma-name-holder-2026-10-03 -->

<!-- review:begin bevacizumab-abevmy-holder-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「- **ABEVMY** - 三星生技」。TFDA 登載 ABEVMY（癌畢弭注射劑，衛部菌疫輸字第001156號）的申請商是台灣生資科技，不是三星生技。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end bevacizumab-abevmy-holder-2026-10-03 -->

核准適應症涵蓋：
- 轉移性大腸直腸癌
- 轉移性乳癌(HER2 陰性)
- 非小細胞肺癌
- 神經膠母細胞瘤
- 卵巢上皮細胞癌
- 子宮頸癌

## 安全性考量
### 常見副作用
- 高血壓
- 蛋白尿
- 出血事件
- 傷口癒合延遲

### 嚴重警語
- 胃腸道穿孔風險
- 動脈血栓栓塞事件
- 需監測血壓及蛋白尿

### 藥物交互作用
與其他抗癌藥物併用時需注意骨髓抑制加成效應。

## 結論與下一步
**證據等級**：L5 (僅 TxGNN 預測，無臨床證據)

**建議**：
1. 會厭腫瘤為罕見疾病，目前無標準治療方案時可考慮探索性使用
2. 建議優先參考頭頸部鱗狀細胞癌的 bevacizumab 使用經驗
3. 若考慮臨床應用，應在腫瘤專科醫師指導下進行

**下一步研究方向**：
- 回顧性分析頭頸部癌症病例中會厭受累的治療反應
- 考慮個案報告或小規模臨床試驗評估可行性

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測原文未改寫；證據等級與決策只依重審結果（降級或撤回）更新，原值列在下表。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「已核准用於頭頸部鱗狀細胞癌(HNSCC)的治療」 | 加註 | [DailyMed：AVASTIN（bevacizumab）美國仿單 §1 Indications and Usage](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 會厭腫瘤預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [DailyMed：AVASTIN（bevacizumab）美國仿單 §1 Indications and Usage](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「Vegzelma (艾法施) - 信東」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「ABEVMY - 三星生技」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 會厭腫瘤預測重審結果 | 重審：撤回，證據等級 L5 不變；快速總覽「建議決策」：原「建議決策／Explore」→「建議決策／Hold（2026-10-03 重審撤回此推論）」 | [PubMed：Phase III Randomized Trial of Chemotherapy With or Without Bevacizumab in Patients With Recurrent or Metastatic Head and Neck Cancer（PMID 31618129）](https://pubmed.ncbi.nlm.nih.gov/31618129/)；[ClinicalTrials.gov：Chemotherapy With or Without Bevacizumab in Treating Patients With Recurrent or Metastatic Head and Neck Squamous Cell Carcinoma（NCT00588770）](https://clinicaltrials.gov/study/NCT00588770)；[PubMed：Phase II randomized trial of radiation therapy, cetuximab, and pemetrexed with or without bevacizumab in patients with locally advanced head and neck cancer（PMID 27177865）](https://pubmed.ncbi.nlm.nih.gov/27177865/)；[ClinicalTrials.gov：Testing the Use of Investigational Drugs Atezolizumab and/or Bevacizumab With or Without Standard Chemotherapy in the Second-Line Treatment of Advanced-Stage Head and Neck Cancers（NCT05063552）](https://clinicaltrials.gov/study/NCT05063552) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

