---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
monitor_inn: "Niraparib"
predicted_indications: ["epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of hypopharynx", "benign neoplasm of tongue", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "tumor of testis and paratestis", "pre-malignant neoplasm", "inner ear neoplasm", "schwannoma of jugular foramen"]
last_modified_at: 2026-10-29
description: "Niraparib：預測新適應症為會厭腫瘤 (epiglottis neoplasm)（證據等級 L5）."
---

# Niraparib
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

## Niraparib：PARP 抑制劑 → 會厭腫瘤 (epiglottis neoplasm)
{: .text-alpha }

## 一句話總結

Niraparib 是一種口服 PARP 抑制劑，目前台灣已有核准的癌症治療用途。
TxGNN 模型預測它可能對**會厭腫瘤 (epiglottis neoplasm)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 與prednisone 或prednisolone 併用，用於治療具BRCA 1/2 (遺傳性及/或體細胞)致病性或疑似致病性突變的轉移性去勢療法抗性前列腺癌(mCRPC)，且尚未需要使用化學治療的成年病人。; １、晚期卵巢癌之第一線維持治療：用於對第一線含鉑化療有完全或部分反應的晚期表皮卵巢癌、輸卵管腫瘤或原發性腹膜癌成年病人之維持治療。
 ２、復發性卵巢癌之維持治療：用於對含鉑化療有完全或部分反應的復發性表皮卵巢癌、輸卵管腫瘤或原發性腹膜癌成年病人之維持治療，病人須對復發前含鉑化療有敏感性。; 1. 晚期卵巢癌之第一線維持治療
 用於對第一線含鉑化療有完全或部分反應的晚期表皮卵巢癌、輸卵管 |

| 預測新適應症 | 會厭腫瘤 (epiglottis neoplasm) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 3 張／共 4 張） |
| 許可證數 | 4 張（有效單方 1／有效複方 2／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Niraparib 屬於 PARP1/2 抑制劑，可透過抑制 PARP 並使其滯留於 DNA 上，在同源重組修復缺陷 (HRD) 的腫瘤細胞中造成合成致死。

不過，針對會厭腫瘤，目前沒有記載任何 HRD 或 DNA 修復缺陷的相關依據，也沒有臨床或文獻資料說明此藥在該腫瘤部位的作用。因此，這個預測目前僅來自 TxGNN 模型本身，機轉上的合理性仍待驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Niraparib 的不重複許可證共 **4 張**：有效單方 1 張、有效複方 2 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028651號 | 截永樂錠100毫克 | 膜衣錠 | 台灣武田藥品工業股份有限公司 | 2029/02/28 | １、晚期卵巢癌之第一線維持治療：用於對第一線含鉑化療有完全或部分反應的晚期表皮卵巢癌、輸卵管腫瘤或原發性腹膜癌成年病人之維持治療。 ２、復發性卵巢癌之維持治療：用於對含鉑化療有完全… |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第028616號 | 澤截膜衣錠100/500毫克 | Abiraterone Acetate、Niraparib tosylate monohydrate | 膜衣錠 | 與prednisone 或prednisolone 併用，用於： １、與雄性素去除療法併用，治療具BRCA1/2 (遺傳性及/或體細胞)致病性或疑似致病性突變的轉移性去勢敏感性前列… |
| 衛部藥輸字第028617號 | 澤截膜衣錠50/500毫克 | Niraparib tosylate monohydrate、Abiraterone Acetate | 膜衣錠 | 與prednisone 或prednisolone 併用，用於： １、與雄性素去除療法併用，治療具BRCA1/2 (遺傳性及/或體細胞)致病性或疑似致病性突變的轉移性去勢敏感性前列… |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027764號</td><td>截永樂膠囊</td><td>Niraparib tosylate monohydrate</td><td></td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

Niraparib 為抗腫瘤藥物（PARP 抑制劑，屬標靶藥物）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 建議監測血液學參數（如 CBC）及肝腎功能，詳細頻率請參考原廠仿單 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共有 351 筆潛在交互作用紀錄，以下為部分範例：
  - 嚴重（Major）：Deferiprone、Samarium (153Sm) lexidronam
  - 中等（Moderate）：Acetylsalicylic acid、Rolapitant、Apixaban、Dipyridamole、Cilostazol、Alteplase、Abciximab 等（多屬抗凝血或抗血小板藥物，以及放射性藥物）

其他安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何臨床試驗或文獻直接研究 Niraparib 用於會厭腫瘤，證據等級為 L5，僅有 TxGNN 模型預測支持。
- 該腫瘤部位也缺乏 HRD 或 DNA 修復缺陷的機轉依據。

**若要推進需要：**
- 取得 Niraparib 詳細的作用機轉資料
- 確認會厭腫瘤是否存在 HRD 或 DNA 修復相關的生物標記
- 進行前臨床或細胞模型研究，初步評估 PARP 抑制在該腫瘤的活性
- 評估此部位腫瘤的臨床試驗可行性及安全性監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」只寫 mCRPC | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列為 niraparib 單方許可證的卵巢癌維持治療；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

