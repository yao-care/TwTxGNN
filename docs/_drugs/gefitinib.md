---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Gefitinib：預測新適應症為牙齦纖維瘤病 (Fibromatosis, Gingival)（證據等級 L5）。原適應症：具 EGFR-TK 突變之局部侵犯性或轉移性非小細胞肺癌（NSCLC）第一線治療"
monitor_inn: "Gefitinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "pulmonary sulcus neoplasm", "lung germ cell tumor", "junctional epidermolysis bullosa"]
---

# Gefitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Gefitinib：從非小細胞肺癌到牙齦纖維瘤病
{: .text-alpha }

## 一句話總結

Gefitinib 是口服的 EGFR 酪胺酸激酶抑制劑，原本用於具 EGFR-TK 突變之局部侵犯性或轉移性非小細胞肺癌（NSCLC）的第一線治療，以及化學治療後惡化之肺腺癌第二線治療。
TxGNN 模型預測它可能對**牙齦纖維瘤病 (Fibromatosis, Gingival)** 有效。
目前針對此疾病**沒有任何臨床試驗與文獻**支持，僅有模型預測分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 具 EGFR-TK 突變之局部侵犯性或轉移性非小細胞肺癌（NSCLC）第一線治療；先前接受化學治療後仍惡化或轉移之肺腺癌第二線治療 |
| 預測新適應症 | 牙齦纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 5 張／共 6 張） |
| 許可證數 | 6 張（有效單方 5／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Gefitinib 仿單（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「表皮生長因子受體（EGFR）表現於正常細胞與癌細胞的細胞表面，並在細胞生長與增生的過程中扮演一定角色。NSCLC 細胞內的某些 EGFR 活化突變（外顯子 19 缺失或外顯子 21 點突變 L858R）已被確認有助於促進腫瘤細胞生長、阻斷細胞凋亡、增加血管新生因子的產生，以及促進轉移過程。[…] Gefitinib 可逆性地抑制野生型及某些活化突變型 EGFR 的激酶活性，防止與該受體相關之酪胺酸殘基的自體磷酸化，從而抑制進一步的下游訊息傳遞，並阻斷 EGFR 依賴性的增生。」英文原文："The epidermal growth factor receptor (EGFR) is expressed on the cell surface of both normal and cancer cells and plays a role in the processes of cell growth and proliferation. Some EGFR activating mutations (exon 19 deletion or exon 21 point mutation L858R) within NSCLC cells have been identified as contributing to the promotion of tumor cell growth, blocking of apoptosis, increasing the production of angiogenic factors and facilitating the processes of metastasis. […] Gefitinib reversibly inhibits the kinase activity of wild-type and certain activating mutations of EGFR, preventing autophosphorylation of tyrosine residues associated with the receptor, thereby inhibiting further downstream signaling and blocking EGFR-dependent proliferation."（[DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41)，版本日期 2023-02-28；查閱日期 2026-11-19）。根據已知資訊，Gefitinib 是 EGFR 酪胺酸激酶抑制劑，在 EGFR 突變的非小細胞肺癌中療效已被證實。

從機轉推論，EGFR 訊號可能參與纖維母細胞增生，因此理論上 EGFR 抑制可能影響纖維增生性疾病。不過這個連結目前僅屬推測，沒有臨床或文獻證據支持，高 TxGNN 分數是唯一的依據。

原適應症（肺癌）與牙齦纖維瘤病在疾病性質、組織來源與治療目標上差異很大，相似性尚待進一步評估。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-11-20），主成分含 Gefitinib 的不重複許可證共 **6 張**：有效單方 5 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-11-20）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第023808號 | 艾瑞莎 膜衣錠２５０公絲 | 膜衣錠 | 臺灣阿斯特捷利康股份有限公司 | 2028/08/27 | IRESSA適用於先前已接受過化學治療後，但仍局部惡化或轉移之肺腺癌病患之第二線用藥。IRESSA適用於具有EGFR-TK突變之局部侵犯性或轉移性之非小細胞肺癌(NSCLC)病患之… |
| 衛部藥製字第059239號 | 癌必莎爾膜衣錠250毫克 | 膜衣錠 | 中國化學製藥股份有限公司新豐工廠 | 2031/07/19 | Gefitinib適用於具有EGFR-TK突變之局部侵犯性或轉移性之非小細胞肺癌(NSCLC)病患之第一線治療。Gefitinib適用於先前已接受過化學治療後，但仍局部惡化或轉移之… |
| 衛部藥製字第060182號 | 費艾舒膜衣錠250毫克 | 膜衣錠 | 美時化學製藥股份有限公司 | 2028/10/09 | 適用於具有EGFR-TK突變之局部侵犯性或轉移性之非小細胞肺癌(NSCLC)病患之第一線治療。適用於先前已接受過化學治療後，但仍局部惡化或轉移之肺腺癌病患之第二線用藥。 |
| 衛部藥製字第060414號 | 吉法莎膜衣錠250毫克 | 膜衣錠 | 杏輝藥品工業股份有限公司 | 2029/12/16 | Gefitinib適用於具有EGFR-TK突變之局部侵犯性或轉移性之非小細胞肺癌(NSCLC)病患之第一線治療。Gefitinib適用於先前已接受過化學治療後，但仍局部惡化或轉移之… |
| 衛部藥輸字第028441號 | 給復能膜衣錠250毫克 | 膜衣錠 | 健喬信元醫藥生技股份有限公司 | 2028/03/01 | 適用於具有EGFR-TK突變之局部侵犯性或轉移性之非小細胞肺癌（NSCLC）病患之第一線治療。適用於先前已接受過化學治療後，但仍局部惡化或轉移之肺腺癌病患之第二線用藥。 |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第028043號</td><td>基扶能膜衣錠250毫克</td><td>GEFITINIB</td><td>2026/01/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（EGFR 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；另依本報告資料，可留意肝功能與肺部症狀 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關係，非仿單文字）：肝病、膽囊疾病、間質性肺病、肺纖維化、發炎後肺纖維化。
- **藥物交互作用**：資料庫共收錄 349 筆交互作用，以下為主要中度等級項目：
  - 胃酸抑制劑：Famotidine、Ranitidine、Cimetidine、Nizatidine、Omeprazole、Esomeprazole、Lansoprazole、Dexlansoprazole、Pantoprazole、Rabeprazole
  - 抗黴菌藥：Miconazole、Clotrimazole
  - 其他：Clarithromycin、Aprepitant、Dexamethasone、Naltrexone、Troglitazone
  - 另有 Calcitriol、Glimepiride 的交互作用，等級為未知

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測分數，沒有任何臨床試驗或文獻支持，證據等級為 L5。EGFR 與牙齦纖維增生之間的機轉連結僅屬推測。
- 知識圖譜顯示 Gefitinib 與間質性肺病、肝病等有禁忌關聯，在缺乏療效證據時，不宜貿然推進。

**若要推進需要：**
- 補齊詳細的作用機轉資料（MOA），並驗證 EGFR 訊號在牙齦纖維瘤病中的角色
- 進行前臨床研究（如病患來源纖維母細胞的細胞實驗），建立初步療效證據
- 評估長期用藥的安全性，特別是肝毒性與間質性肺病風險，是否適用於這類良性、慢性疾病
- 釐清此疾病的給藥途徑與劑量需求

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯與英文原文）。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 艾瑞莎許可證字號錯誤、學名藥字號為佔位符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國仿單節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

