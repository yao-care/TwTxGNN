---
layout: default
title: Pefloxacin
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
monitor_inn: "pefloxacin"
predicted_indications: ["heart conduction disease", "heart neoplasm", "heart valve disease", "congenital anomaly of ventricular septum", "pericardium disease", "heart aneurysm", "cardiac anomalies-heterotaxy syndrome", "cor biloculare", "carcinoid heart disease", "myocardial rupture"]
last_modified_at: 2026-10-15
description: "Pefloxacin：預測新適應症為心臟傳導疾病 (Heart Conduction Disease)（證據等級 L5）。原適應症：成人由革蘭氏陰性菌及葡萄球菌引起的嚴重感染症"
---

# Pefloxacin
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

# Pefloxacin：從革蘭氏陰性菌及葡萄球菌嚴重感染到心臟傳導疾病

## 一句話總結

Pefloxacin 是一種氟喹諾酮類（fluoroquinolone）抗菌藥，原本用於成人由革蘭氏陰性菌及葡萄球菌引起的嚴重感染症。
TxGNN 模型預測它可能對**心臟傳導疾病 (Heart Conduction Disease)** 有效，但目前**沒有任何臨床試驗或文獻**支持此預測，僅屬模型推論，且機轉上存在安全疑慮。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 成人由革蘭氏陰性菌及葡萄球菌引起的嚴重感染症 |
| 預測新適應症 | 心臟傳導疾病 (Heart Conduction Disease) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 台灣上市 | 僅有已註銷許可證（目前無有效上市） |
| 許可證數 | 1 張（有效單方 0／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，pefloxacin 屬於氟喹諾酮類抗菌藥，一般認為其作用是抑制細菌的 DNA 旋轉酶（DNA gyrase）與拓樸異構酶 IV（topoisomerase IV），在原適應症（細菌感染）中的療效基於此機制。

然而，心臟傳導疾病屬於心臟電生理異常，與細菌感染並無明顯關聯。目前沒有已知機轉能說明 pefloxacin 可治療此疾病。相反地，氟喹諾酮類與 QT 間期延長相關，對傳導異常的患者反而是安全疑慮，而非療效依據。因此這個預測的合理性主要來自模型的統計關聯，缺乏生物學上的支持。

其他排名較前的預測（如心臟腫瘤、心臟瓣膜疾病、先天性心室中隔缺損、心包疾病等）同樣缺乏實質證據。其中心臟瓣膜疾病與心包疾病僅有間接的抗菌相關研究（見下方文獻），不足以支持非感染性心臟疾病的用途。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首要預測（心臟傳導疾病）目前無相關文獻。

以下為排名較後的相關預測中檢索到的少數文獻，僅供參考，**不直接支持首要預測**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10671762](https://pubmed.ncbi.nlm.nih.gov/10671762/) | 2000 | 動物試驗 | Chemotherapy | 兔子綠膿桿菌心內膜炎模型中比較多種氟喹諾酮與 amikacin 的療效（對應心臟瓣膜疾病預測，屬間接的前臨床證據） |
| [7784809](https://pubmed.ncbi.nlm.nih.gov/7784809/) | 1995 | 病例系列 | Scand J Infect Dis | 義大利北部 1982–1992 年諾卡氏菌病回溯性調查，僅為間接關聯（對應心包疾病預測） |
| [34285735](https://pubmed.ncbi.nlm.nih.gov/34285735/) | 2021 | 病例報告 | Pan Afr Med J | 血液透析患者自行服用 ciprofloxacin 後發生阿基里斯腱病變與斷裂，屬氟喹諾酮的不良反應訊號，而非療效證據 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Pefloxacin 的不重複許可證共 **1 張**：有效單方 0 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第041639號</td><td>〝壽元〞美賽新靜脈注射液８０毫克﹨毫升</td><td>Pefloxacin (Methanesulfonate)</td><td>2024/04/29</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

另外，依本報告彙整的資料，氟喹諾酮類與 QT 間期延長、主動脈瘤與主動脈剝離風險，以及肌腱病變／斷裂的報告有關；這些對心血管疾病患者尤其值得注意。目前未查得藥物交互作用資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自 TxGNN 模型（證據等級 L5），沒有臨床試驗或直接文獻支持，且缺乏合理的作用機轉。
- 氟喹諾酮類的 QT 延長風險與心臟傳導疾病直接衝突，另在台灣目前僅有已註銷的許可證，無有效上市產品。

**若要推進需要：**
- 補充 pefloxacin 的詳細作用機轉資料，並評估是否存在任何可信的心臟相關機轉。
- 進行系統性文獻回顧，確認是否有任何心臟傳導方面的療效訊號，並同步評估心臟安全性（QT 延長、心律不整）。
- 若仍有意探索，應先進行前臨床或機轉研究，再考慮臨床試驗。
- 實際上，較合理的方向是保留其抗感染用途（如感染性心內膜炎等），而非非感染性心臟疾病。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

