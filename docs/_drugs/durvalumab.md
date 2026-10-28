---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 6
monitor_inn: "Durvalumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-29
description: "Durvalumab：預測新適應症為子宮韌帶腺癌 (uterine ligament adenocarcinoma)（證據等級 L5）。原適應症：非小細胞肺癌（可切除之前導性／輔助治療，及局部晚期無法切除且放化療後未惡化者）、小細胞肺癌、膽道癌、肝細胞癌、子宮內膜癌、膀胱癌"
---

# Durvalumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Durvalumab：從非小細胞肺癌等多種癌症到子宮韌帶腺癌
{: .text-alpha }

## 一句話總結

Durvalumab 是 PD-L1 免疫檢查點抑制劑，在台灣已核准用於非小細胞肺癌、小細胞肺癌、膽道癌、肝細胞癌、子宮內膜癌與膀胱癌。
TxGNN 模型預測它可能對**子宮韌帶腺癌 (uterine ligament adenocarcinoma)** 有效，但此疾病目前**沒有任何臨床試驗或文獻**直接支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌（可切除之前導性／輔助治療，及局部晚期無法切除且放化療後未惡化者）、小細胞肺癌、膽道癌、肝細胞癌、子宮內膜癌、膀胱癌 |
| 預測新適應症 | 子宮韌帶腺癌 (uterine ligament adenocarcinoma) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。根據已知資訊，Durvalumab 是抗 PD-L1 單株抗體，可解除腫瘤微環境對 T 細胞的抑制，恢復抗腫瘤免疫活性。

Durvalumab 已在台灣核准用於晚期或復發性子宮內膜癌的第一線治療（與含鉑化療併用後的維持治療）。子宮韌帶腺癌同屬婦科腺癌，理論上 PD-L1 阻斷可能適用。

但這個推論僅來自模型預測與機轉上的類推，沒有針對此疾病的臨床或文獻證據。因此依證據等級規則，只能判定為 L5。

## 臨床試驗證據

目前無針對子宮韌帶腺癌的臨床試驗登記。

另外，在預測排名第 2 的「子宮頸內膜癌 (endocervical carcinoma)」下，有 1 個相關試驗，列於下方供參考（並非本次主要預測疾病）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | 完成 | 20 | 大分割放射治療併用 durvalumab 與 tremelimumab，用於復發／轉移性子宮頸、陰道或外陰癌的安全性與可行性 |

## 文獻證據

目前無針對子宮韌帶腺癌的相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Durvalumab 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001088號 | 抑癌寧注射劑 | 注射劑 | 臺灣阿斯特捷利康股份有限公司 | 2028/10/11 | １、非小細胞肺癌(NSCLC)： (１)與含鉑化療藥物併用，作為可切除(腫瘤大小>4公分且/或(and/or)淋巴結分期N1及N2)、無已知的表皮生長因子受體(EGFR)突變或間變… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 PD-L1 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整資料共有 81 筆交互作用紀錄，以下為部分重點：
  - **嚴重 (Major)**：Adalimumab
  - **中度 (Moderate)**：多種皮質類固醇（hydrocortisone、dexamethasone、prednisone、prednisolone、methylprednisolone、betamethasone、budesonide、triamcinolone、deflazacort）、roflumilast、alemtuzumab、anakinra、alefacept、破傷風類毒素疫苗、炭疽疫苗
  - **輕微 (Minor)**：多種鋅製劑

  皮質類固醇與免疫抑制類藥物可能削弱免疫檢查點抑制劑的作用，併用時需評估。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 子宮韌帶腺癌目前僅有 TxGNN 模型預測，沒有任何臨床試驗或文獻直接研究，證據等級為 L5。
- 雖然 durvalumab 在子宮內膜癌已有核准，機轉上可類推，但這不足以支持直接推進。

**若要推進需要：**
- 蒐集此疾病或相近婦科腺癌（如子宮頸腺癌）中 PD-L1 表現的資料
- 檢視 durvalumab 在子宮頸癌的臨床試驗結果（例如 NCT03452332 的後續成果），評估是否可作為切入點
- 補充詳細的作用機轉資料
- 確認此罕見疾病的病人族群與試驗可行性，再評估是否升級為研究問題

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證數「13 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

