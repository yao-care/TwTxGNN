---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase alfa：從小兒發作型低磷酸酯酶症到粒線體氧化磷酸化障礙（核 DNA 異常所致）

## 一句話總結

Asfotase alfa 是一種酵素替代療法，原本用於治療小兒發作型低磷酸酯酶症 (HPP)。
TxGNN 模型預測它可能對**核 DNA 異常所致的粒線體氧化磷酸化障礙 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 小兒發作型低磷酸酯酶症 (Pediatric-onset hypophosphatasia; HPP) 病人之長期酵素替代療法 |
| 預測新適應症 | 核 DNA 異常所致的粒線體氧化磷酸化障礙 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Asfotase alfa 是重組的組織非特異性鹼性磷酸酶 (TNSALP)，
可水解細胞外的受質，例如無機焦磷酸 (inorganic pyrophosphate) 與吡哆醛-5'-磷酸 (pyridoxal-5'-phosphate)，
在低磷酸酯酶症中用來促進骨礦化。

然而，這個機轉與核基因編碼的氧化磷酸化 (OXPHOS) 缺陷之間，並沒有已建立的關聯。
高分數僅來自知識圖譜的關聯推論，不代表有生物學上的支持。
因此這項預測應視為一個**待驗證的假說**，而非有依據的治療方向。

另外，在排名前 10 的其他預測中（如 Steel syndrome、Scheie syndrome、Hurler syndrome、胰臟外分泌不足等），
同樣沒有臨床試驗或文獻佐證，機轉連結也都相當薄弱，多半只是「酵素替代」或「骨骼表現」的概念類比。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Asfotase Alfa 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部罕菌疫輸字第000052號 | 賜壯骼皮下注射劑40毫克/毫升 | 注射液劑 | 臺灣阿斯特捷利康股份有限公司 | 2034/10/08 | 適用於小兒發作型低磷酸酯酶症(Pediatric-onset hypophosphatasia ; HPP) 病人之長期酵素替代療法。 |
| 衛部罕菌疫輸字第000053號 | 賜壯骼皮下注射劑100毫克/毫升 | 注射液劑 | 臺灣阿斯特捷利康股份有限公司 | 2034/10/08 | 適用於小兒發作型低磷酸酯酶症(Pediatric-onset hypophosphatasia ; HPP) 病人之長期酵素替代療法。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5：沒有臨床試驗、沒有文獻，只有模型分數。
- 機轉上找不到 Asfotase alfa 與核 DNA 相關 OXPHOS 缺陷之間的合理連結，高分很可能是圖譜推論的假象。

**若要推進需要：**
- 補齊詳細的作用機轉資料 (MOA)，並評估其與粒線體疾病病理的可能關聯
- 進行系統性文獻回顧，確認是否有任何前臨床或病例層級的證據
- 若有機轉假說，先以細胞或動物模型做前臨床驗證
- 補齊安全性資料（警語、禁忌、藥物交互作用），再評估特定族群的風險
- 在上述證據出現前，建議不投入臨床開發資源，並持續監測新發表的研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

