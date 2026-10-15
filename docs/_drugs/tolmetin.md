---
layout: default
title: Tolmetin
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Tolmetin
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

# Tolmetin：從類風濕性關節炎到肢端中段發育不良（Hunter-Thompson 型）

## 一句話總結

Tolmetin（妥美汀）是一種非類固醇消炎止痛藥（NSAID），原本用於類風濕性關節炎、骨關節炎、僵直性脊椎炎等發炎性關節疾病的症狀緩解。
TxGNN 模型預測它可能對**肢端中段發育不良（Hunter-Thompson 型，acromesomelic dysplasia, Hunter-Thompson type）**有效，
但目前**沒有任何臨床試驗與文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、骨關節炎（關節痛、退化性關節炎）、僵直性脊椎炎、急性肌肉骨骼症狀、急性痛風 |
| 預測新適應症 | 肢端中段發育不良，Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 14 張（有效單方 3／有效複方 0／已註銷 11） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tolmetin 是非選擇性 COX 抑制劑，具有消炎與止痛作用，在類風濕性關節炎等發炎性關節疾病中的症狀緩解效果已有核准適應症。

然而，Hunter-Thompson 型肢端中段發育不良是一種與 CDMP1/GDF5 相關的罕見遺傳性骨骼發育異常。Tolmetin 的 COX 抑制作用與此疾病的致病機轉之間，**沒有已知的機轉連結**。此預測完全來自 TxGNN 圖譜分數，高分並不等於有生物學或臨床上的合理性。

此外，同一份預測清單的前幾名多為罕見遺傳性骨骼或發育疾病（如 brachyolmia、pseudoachondroplasia 等），多數缺乏機轉依據。相對而言，排名較後但與原適應症較相關的項目，例如類風濕性結節病、類風濕因子陽性多關節型幼年特發性關節炎、脊椎關節病變，在機轉上較為合理，但同樣沒有任何試驗或文獻證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tolmetin 的不重複許可證共 **14 張**：有效單方 3 張、有效複方 0 張、已註銷 11 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第022712號 | 妥美定錠（妥美汀） | 錠劑 | 恆信藥品有限公司 | 2029/12/30 | 下列疾患及症狀之鎮痛、消炎、頸肩腕症候群、腰背痛症 |
| 衛署藥製字第025549號 | "利達" 痛必定錠200毫克（妥美汀） | 錠劑 | 利達製藥股份有限公司 | 2028/05/25 | 類風濕性關節炎、骨關節炎（關節痛、退化性關節炎）僵直性脊椎炎、急性肌肉骨骼症狀、急性痛風 |
| 衛署藥製字第055941號 | “應元”遠痛錠 200 毫克 | 錠劑 | 應元化學製藥股份有限公司 | 2031/02/21 | 類風濕性關節炎、骨關節炎(關節痛、退化性關節炎)、僵直性脊椎炎、急性肌肉骨骼症狀、急性痛風。 |

<details><summary><strong>已註銷</strong>（11 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第030056號</td><td>妥力定錠２００公絲（妥美汀）</td><td>TOLMETIN (SODIUM DIHYDRATE)</td><td>2013/09/30</td></tr><tr><td>衛署藥輸字第006365號</td><td>妥力定錠</td><td>TOLMETIN (SODIUM DIHYDRATE)</td><td>1987/12/18</td></tr><tr><td>衛署藥輸字第008441號</td><td>一－甲基５－對位－甲苯基/喀２－醋酸鈉二水合物</td><td>TOLMETIN SODIUM</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第008609號</td><td>妥力定膠囊４００公絲</td><td>TOLMETIN (SODIUM)</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第014881號</td><td>妥力定膠囊４００公絲</td><td>TOLMETIN (SODIUM DIHYDRATE)</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015258號</td><td>施樂妥力定錠</td><td>TOLMETIN (SODIUM DIHYDRATE)</td><td>1989/08/29</td></tr><tr><td>衛署藥輸字第017293號</td><td>妥力定凝膠</td><td>TOLMETIN</td><td>1993/02/12</td></tr><tr><td>衛署藥輸字第017649號</td><td>妥美汀</td><td>TOLMETIN SODIUM DIHYDRATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第019628號</td><td>妥力定凝膠</td><td>TOLMETIN</td><td>2004/07/15</td></tr><tr><td>衛署藥輸字第021930號</td><td>妥力定膠囊２００公絲　〝嬌生瑞士廠〞</td><td>TOLMETIN、TOLMETIN SODIUM DIHYDRATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第021935號</td><td>妥力定膠４００公絲　〝嬌生瑞士廠〞</td><td>TOLMETIN SODIUM DIHYDRATE、TOLMETIN</td><td>2005/06/15</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 153 筆交互作用，以下為部分範例：
  - 中度：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide（皮質類固醇類）；Acetylsalicylic acid（阿斯匹靈）；Metformin；Glimepiride、Chlorpropamide（磺醯脲類降血糖藥）；Mesalazine、Balsalazide；Naltrexone；Potassium citrate、Potassium bicarbonate；Picosulfuric acid；Polyethylene glycol（含電解質）
  - 輕度：Famotidine、Ranitidine、Cimetidine、Linaclotide
- **知識圖譜顯示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物—疾病禁忌關聯，非仿單文字）：高血壓、肝衰竭、肝臟疾病、腎臟疾病、膽囊疾病、活動性消化性潰瘍、血液凝固疾病、心肌梗塞、冠狀動脈血栓、心血管疾病、心臟病、血紅蛋白病變等。

其餘警語與禁忌症，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有任何臨床試驗或文獻佐證（證據等級 L5），且 Tolmetin 的 COX 抑制機轉與 CDMP1/GDF5 相關骨骼發育異常之間沒有已知連結。
- 該藥物的 NSAID 類安全性疑慮（心血管、胃腸道、腎臟、肝臟等）對罕見遺傳性骨骼疾病的長期使用並不划算。

**若要推進需要：**
- 補齊 Tolmetin 的作用機轉資料，並釐清與 GDF5 訊號路徑或軟骨發育的可能關聯。
- 進行系統性文獻與臨床試驗檢索，確認是否有任何前臨床或病例層級的證據。
- 若仍想探索，建議優先評估與原適應症較相關的預測（如類風濕因子陽性多關節型幼年特發性關節炎、脊椎關節病變、類風濕性結節病），這些在機轉上較合理。
- 補充仿單層級的警語與禁忌症資料，並評估長期使用的風險效益。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

