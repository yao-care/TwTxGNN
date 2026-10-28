---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
monitor_inn: "Alpelisib"
predicted_indications: ["pulmonary hypertension"]
last_modified_at: 2026-10-29
description: "Alpelisib：預測新適應症為肺動脈高壓 (Pulmonary Hypertension)（證據等級 L5）。原適應症：與 fulvestrant 併用，治療 HR 陽性、HER2 陰性及 PIK3CA 突變的局部晚期或轉移性乳癌…"
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Alpelisib：從乳癌到肺動脈高壓
{: .text-alpha }

## 一句話總結

Alpelisib 是一種口服 PI3K-alpha 抑制劑，原本與 fulvestrant 併用，治療 HR 陽性、HER2 陰性且帶有 PIK3CA 突變的晚期或轉移性乳癌。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，但目前**沒有相關臨床試驗**，僅有 **1 篇文獻**，而且該文獻是 alpelisib 引起間質性肺病的病例報告，屬於安全性警訊，並非支持證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 與 fulvestrant 併用，治療 HR 陽性、HER2 陰性及 PIK3CA 突變的局部晚期或轉移性乳癌，且曾接受內分泌治療但疾病惡化的停經後女性及男性病人 |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 0.9903 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效單方 3／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 alpelisib 是 PI3K-alpha 抑制劑，而 PI3K/AKT 訊號與肺血管重塑有關，這是此預測在機轉上的可能依據。

不過，原適應症（PIK3CA 突變的乳癌）與肺動脈高壓在疾病性質上差異很大，兩者之間缺乏直接的臨床關聯。目前唯一檢索到的文獻，描述的是 alpelisib 引起間質性肺病，屬於肺部安全性訊號，並不支持其對肺部血管疾病有益。

因此，這個預測目前主要來自模型分數，機轉推論尚未得到實際研究驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | 病例報告 | Journal of Oncology Pharmacy Practice | 一名晚期乳癌病人使用 alpelisib 後發生間質性肺病，屬於不良反應通報，並非療效證據 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Alpelisib 的不重複許可證共 **3 張**：有效單方 3 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027994號 | 愛克利50毫克膜衣錠 | 膜衣錠 | 台灣諾華股份有限公司 | 2030/12/23 | 與fulvestrant併用可治療患有荷爾蒙受體(HR)陽性、第二型人類表皮生長因子受體(HER2)陰性及PIK3CA突變的局部晚期或轉移性乳癌，且曾接受內分泌治療但疾病惡化的停經… |
| 衛部藥輸字第027995號 | 愛克利150毫克膜衣錠 | 膜衣錠 | 台灣諾華股份有限公司 | 2030/12/23 | 與fulvestrant併用可治療患有荷爾蒙受體(HR)陽性、第二型人類表皮生長因子受體(HER2)陰性及PIK3CA突變的局部晚期或轉移性乳癌，且曾接受內分泌治療但疾病惡化的停經… |
| 衛部藥輸字第027996號 | 愛克利200毫克膜衣錠 | 膜衣錠 | 台灣諾華股份有限公司 | 2030/12/23 | 與fulvestrant併用可治療患有荷爾蒙受體(HR)陽性、第二型人類表皮生長因子受體(HER2)陰性及PIK3CA突變的局部晚期或轉移性乳癌，且曾接受內分泌治療但疾病惡化的停經… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PI3K-alpha 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項；另依臨床試驗資料，使用期間需留意血糖變化 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共有 284 筆交互作用紀錄，列出的前 20 筆皆為中度等級，主要涉及以下類別：
  - 降血糖藥物：acarbose、albiglutide、alogliptin、metformin、pioglitazone、acetohexamide、canagliflozin、chlorpropamide、dapagliflozin、dulaglutide、empagliflozin、ertugliflozin、exenatide、glimepiride、glipizide
  - 其他：alosetron、bupropion、dexamethasone、dronabinol、fidaxomicin
- **肺部安全性訊號**：已有 alpelisib 引起間質性肺病的病例報告，若考慮用於肺部疾病，這一點需要特別重視。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數支持（證據等級 L5），沒有相關臨床試驗，唯一的文獻是肺部不良反應的病例報告，與預期方向相反。

**若要推進需要：**
- 補齊 alpelisib 的作用機轉資料。
- 進行前臨床研究，例如肺動脈高壓動物模型，驗證 PI3K-alpha 抑制是否有益。
- 評估間質性肺病等肺部不良反應風險，確認在肺部疾病族群中的安全性。
- 取得上述前臨床或機轉證據後，再重新評估是否值得設計臨床試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

