---
layout: default
title: Hymecromone
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Hymecromone
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

# Hymecromone：從膽石症到糖尿病腎病

## 一句話總結

Hymecromone（和美克隆）是一種利膽鎮痙藥，原本核准用於膽石症、膽囊炎及膽囊切除後症候群的治療。
TxGNN 模型預測它可能對**糖尿病腎病 (Diabetic Nephropathy)** 有效，
但目前**無臨床試驗**且**無相關文獻**直接支持此適應症，預測依據為純模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 利膽、鎮痙劑（膽石症、膽囊炎、膽道阻礙、膽囊切除後症候群） |
| 預測新適應症 | 糖尿病腎病 (Diabetic Nephropathy) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 14 張（有效單方 2／有效複方 0／已註銷 12） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap）。根據現有研究資訊，Hymecromone 又稱 4-methylumbelliferone（4-MU），為香豆素衍生物。其代謝產物 4-methylumbelliferyl glucuronide（4-MUG）可耗竭 UDP-葡萄糖醛酸（UDP-glucuronic acid），進而抑制透明質酸（hyaluronan, HA）的生合成。

在糖尿病腎病的病理機轉中，透明質酸於腎小管間質大量積聚，促進纖維化與慢性炎症反應，加劇腎臟功能惡化。理論上，Hymecromone 透過抑制透明質酸合成，或可緩解腎臟纖維化與炎症，提供腎臟保護效果。

然而，**此關聯目前僅為機轉推論，無任何臨床或前臨床研究直接支持**。值得注意的是，本次預測排名第 8 的 **1 型糖尿病（Type 1 Diabetes Mellitus）**具有更明確的前臨床機轉基礎——已有 3 篇動物研究顯示抑制透明質酸合成可恢復胰島炎模型的免疫耐受性，證據等級達 L4，可作為後續研究的優先探索方向。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Hymecromone 的不重複許可證共 **14 張**：有效單方 2 張、有效複方 0 張、已註銷 12 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第049261號 | 利鎮膽膠囊 | 膠囊劑 | 瑩碩生技醫藥股份有限公司 | 2028/01/28 | 下列諸症之利膽及鎮痙作用膽石、膽囊炎、膽道阻礙、膽囊切除後症候群。 |
| 衛署藥製字第055889號 | 〝元宙〞安利膽膠囊 | 膠囊劑 | 元宙化學製藥股份有限公司 | 2030/12/23 | 下列諸症之利膽及鎮痙作用：膽石、膽囊炎、膽道阻礙、膽囊切除後症候群。 |

<details><summary><strong>已註銷</strong>（12 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第003962號</td><td>七氫氧四甲基香豆素</td><td>HYMECROMONE (IMECROMONE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006149號</td><td>膽能爽膠囊</td><td>HYMECROMONE (IMECROMONE)</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第006437號</td><td>趕膽炎膠囊</td><td>ALUMINUM MAGNESIUM SILICATE、HYMECROMONE (IMECROMONE)</td><td>1986/06/21</td></tr><tr><td>衛署藥輸字第006507號</td><td>膽力可定膠囊</td><td>HYMECROMONE (IMECROMONE)</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第007023號</td><td>益膽膠囊</td><td>HYMECROMONE (IMECROMONE)</td><td>2014/05/15</td></tr><tr><td>衛署藥輸字第007493號</td><td>可爾膽蒙膠囊</td><td>HYMECROMONE (IMECROMONE)</td><td>2005/06/14</td></tr><tr><td>衛署藥輸字第010217號</td><td>賜康寧軟膠囊</td><td>HYMECROMONE (IMECROMONE)</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第010616號</td><td>和美克隆</td><td>HYMECROMONE (IMECROMONE)</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第011950號</td><td>優克膽膠囊２００公絲</td><td>HYMECROMONE (IMECROMONE)</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第015053號</td><td>趕膽炎膠囊</td><td>HYMECROMONE (IMECROMONE)</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015334號</td><td>利樂道膠囊</td><td>HYMECROMONE (IMECROMONE)</td><td>2013/11/26</td></tr><tr><td>衛署藥陸輸字第000135號</td><td>和美克隆</td><td>HYMECROMONE (IMECROMONE)</td><td>2013/12/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高達 99.85%，但糖尿病腎病適應症目前完全缺乏臨床試驗與文獻支持，機轉關聯亦僅為理論推論，不具備推進的實證基礎。

**若要推進需要：**
- 補充 Hymecromone 完整作用機轉資料（透過 DrugBank API 查詢 DB07118）
- 建立糖尿病腎病動物模型的前臨床研究（測試 4-MU 對腎小管纖維化的影響）
- 優先評估機轉基礎更明確的 **1 型糖尿病（Rank 8，L4 等級）**——已有動物研究支持，可作為更可行的切入點
- 補全安全性資料（警語、禁忌症），為後續人體試驗設計提供依據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

