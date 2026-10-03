---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Niraparib：從卵巢癌到會厭腫瘤

## 一句話總結

Niraparib 是一種 PARP1/2 抑制劑，台灣核准用於晚期卵巢癌/復發性卵巢癌的維持治療，以及具 BRCA1/2 突變的轉移性去勢療法抗性前列腺癌（mCRPC）。
TxGNN 模型預測它可能對**會厭腫瘤（Epiglottis Neoplasm）**有效，預測分數高達 **99.99%**，
但目前**無任何臨床試驗或文獻**支持此方向，屬純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性去勢療法抗性前列腺癌（mCRPC，需具 BRCA 1/2 突變，與 prednisone/prednisolone 併用） |
| 預測新適應症 | 會厭腫瘤（Epiglottis Neoplasm） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 1／有效複方 2／已註銷 1） |
| 建議決策 | Hold |

<!-- review:begin niraparib-original-indication-combo-2026-10-03 -->

> **查核加註（2026-10-03）**：此為 niraparib＋abiraterone 複方「澤截膜衣錠」（衛部藥輸字第028617號）的適應症；niraparib 單方「截永樂錠100毫克」（衛部藥輸字第028651號）核准的是晚期卵巢癌（含輸卵管、原發性腹膜癌）第一線維持治療與復發性卵巢癌維持治療。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end niraparib-original-indication-combo-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的官方作用機轉資料（MOA）。根據已知資訊，Niraparib 是 PARP1/2（poly ADP-ribose polymerase）抑制劑，透過阻斷 DNA 單鏈損傷修復途徑，使具有同源重組缺陷（Homologous Recombination Deficiency，HRD）或 BRCA1/2 突變的腫瘤細胞無法有效修復 DNA 損傷，最終誘發合成致死（synthetic lethality）效應。此機轉已在高級別漿液性卵巢癌及前列腺癌中獲臨床驗證。

然而，會厭腫瘤（位於喉部入口的軟骨結構）與卵巢癌或前列腺癌在腫瘤生物學上差異顯著。PARP 抑制劑的療效高度依賴腫瘤細胞的 BRCA/HRD 缺陷，而會厭腫瘤（無論良性或惡性）中此類分子特徵的發生率極低，目前缺乏相關流行病學或基礎研究支持。

儘管 TxGNN 模型預測分數高，此預測在機轉合理性上仍屬薄弱，完全缺乏臨床前或臨床研究數據的佐證，目前僅具模型層面的探索性價值。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Niraparib 的不重複許可證共 **4 張**：有效單方 1 張、有效複方 2 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028651號 | 截永樂錠100毫克 | 膜衣錠 | 台灣武田藥品工業股份有限公司 | 2029/02/28 | １、晚期卵巢癌之第一線維持治療：用於對第一線含鉑化療有完全或部分反應的晚期表皮卵巢癌、輸卵管腫瘤或原發性腹膜癌成年病人之維持治療。 ２、復發性卵巢癌之維持治療：用於對含鉑化療有完全… |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第028616號 | 澤截膜衣錠100/500毫克 | Abiraterone Acetate、Niraparib tosylate monohydrate | 膜衣錠 | 與prednisone 或prednisolone 併用，用於： １、與雄性素去除療法併用，治療具BRCA1/2 (遺傳性及/或體細胞)致病性或疑似致病性突變的轉移性去勢敏感性前列… |
| 衛部藥輸字第028617號 | 澤截膜衣錠50/500毫克 | Niraparib tosylate monohydrate、Abiraterone Acetate | 膜衣錠 | 與prednisone 或prednisolone 併用，用於： １、與雄性素去除療法併用，治療具BRCA1/2 (遺傳性及/或體細胞)致病性或疑似致病性突變的轉移性去勢敏感性前列… |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027764號</td><td>截永樂膠囊</td><td>Niraparib tosylate monohydrate</td><td></td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP 抑制劑，非傳統細胞毒性化療） |
| 骨髓抑制風險 | 高（血小板減少症為最常見且最嚴重之血液學副作用；另見嗜中性白血球減少、貧血） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含血小板分類）、肝腎功能、血壓（Niraparib 常見高血壓副作用） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

**藥物交互作用**（DDInter 資料庫共 351 筆，以下列出主要交互作用）：

| 藥物 | 交互作用等級 |
|------|------------|
| Deferiprone | **Major**（重大） |
| Samarium (153Sm) lexidronam | **Major**（重大） |
| Acetylsalicylic acid（阿斯匹靈） | Moderate（中度） |
| Apixaban | Moderate（中度） |
| Rolapitant | Moderate（中度） |
| Bivalirudin | Moderate（中度） |
| Abciximab | Moderate（中度） |

> 主要警語及禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 模型預測分數雖高（99.99%），但 Niraparib 的 PARP 抑制合成致死機轉在會厭腫瘤中缺乏生物學依據（BRCA/HRD 突變發生率極低），且完全無臨床試驗或文獻數據佐證，不符合推進此適應症的最低門檻。

**若要推進需要：**
- 會厭腫瘤樣本的 BRCA/HRD 突變率流行病學調查
- 細胞株或類器官模型的臨床前療效驗證數據
- 明確的 Niraparib 完整作用機轉資料（MOA，建議查詢 DrugBank API）

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」只寫 mCRPC | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

