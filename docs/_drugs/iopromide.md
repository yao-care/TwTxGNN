---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-10-16
description: "Iopromide：預測新適應症為退化性關節炎易感性 (Osteoarthritis Susceptibility)（證據等級 L5）。原適應症：電腦斷層攝影、數位化減影血管造影術、靜脈內尿路造影、動脈造影（特別是心血管造影）及身體空腔部份（如關節攝影、廔管造影）攝影，但脊椎造影…"
---

# Iopromide
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

## Iopromide：從影像診斷（電腦斷層攝影、血管造影等）到退化性關節炎（Osteoarthritis）
{: .text-alpha }

## 一句話總結

Iopromide 是含碘的非離子型 X 光對比劑，原本用於電腦斷層攝影、血管造影、尿路造影、關節攝影及成人對比增強乳房攝影等影像診斷。
TxGNN 模型預測它可能對**退化性關節炎易感性 (Osteoarthritis Susceptibility)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測，應視為知識圖譜的推論結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 電腦斷層攝影、數位化減影血管造影術、靜脈內尿路造影、動脈造影（特別是心血管造影）及身體空腔部份（如關節攝影、廔管造影）攝影，但脊椎造影、腦室攝影及腦池攝影除外；亦適用於成人對比增強乳房攝影 |
| 預測新適應症 | 退化性關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 3 張（有效單方 3／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Iopromide 是含碘的非離子型放射線對比劑，靠碘對 X 光的衰減來顯影，並非透過藥理作用治療疾病。目前沒有已知的抗發炎、免疫調節或軟骨保護機轉，可與遺傳性退化性關節炎易感性連結。

這個預測較可能源自知識圖譜的關聯假象：Iopromide 在臨床上用於關節攝影，因此在圖譜中與關節疾病相連，但這反映的是「用於關節影像檢查」，而不是「對關節疾病有治療效果」。

排名其後的預測也有同樣特徵，包括退化性關節炎、類風濕性關節炎、短軀幹症 (brachyolmia)、肢中發育不良（Hunter-Thompson 型）、禿髮、肌硬化症、血紅素病變及假性軟骨發育不全。這些預測目前都沒有臨床試驗或文獻佐證，機轉上也找不到合理連結，因此本報告以排名第一者為主要評估對象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Iopromide 的不重複許可證共 **3 張**：有效單方 3 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第016018號 | 優照維斯碘含量３７０毫克/毫升 | 注射劑 | 台灣拜耳股份有限公司 | 2029/09/07 | 1. 電腦斷層攝影、數位化減影血管造影術、靜脈內尿路造影、動脈造影、特別是心血管造影及身體空腔部份(如關節攝影、廔管造影)，但脊椎造影、腦室攝影及腦池攝影除外。 2. 適用於成人對… |
| 衛署藥輸字第016019號 | 優照維斯碘含量３００毫克/毫升 | 注射劑 | 台灣拜耳股份有限公司 | 2029/09/07 | 1. 電腦斷層攝影、數位化減影血管造影術、靜脈內尿路造影、末梢靜脈X-光造影、靜脈造影、動脈造影及身體空腔部份(如關節攝影、子宮輸卵管攝影，廔管造影)，但脊椎造影、腦室攝影及腦池攝… |
| 衛署藥輸字第016804號 | 優照維斯碘含量２４０毫克/毫升注射液 | 注射劑 | 台灣拜耳股份有限公司 | 2028/08/17 | 電腦斷層攝影、數位化減影血管造影術、靜脈造影、尿路造影、末梢靜脈Ｘ－光造影及身體空腔部份（如關節攝影、子宮輸卵管Ｘ光攝影、瘻管造影）、但脊椎造影、腦室攝影及腦池攝影除外 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共收錄 202 筆交互作用。列為 Major 的包括：
  - Metformin
  - Amphotericin B 及其脂質劑型
  - Mesalazine、Balsalazide、Olsalazine、Sulfasalazine
  - Vancomycin
  - 胺基糖苷類（Kanamycin、Neomycin、Streptomycin）
  - Polymyxin B
- Mannitol 為 Moderate。
- Clotrimazole、Acetylsalicylic acid、Bupropion、Dexamethasone、Pantoprazole 的等級為 Unknown。

其他警語與禁忌症請參考原廠仿單。此外，碘化對比劑用於部分血紅素病變（如鐮刀型貧血）時有安全性考量，不支持將其作為這類疾病的治療。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自 TxGNN 模型分數，沒有任何臨床試驗或文獻支持（證據等級 L5）。
- Iopromide 是診斷用對比劑，沒有已知的疾病修飾機轉，預測很可能是因「關節攝影」用途而產生的圖譜假象。

**若要推進需要：**
- 取得作用機轉相關資料，確認是否有任何與關節軟骨或發炎相關的生物學作用。
- 進行系統性文獻與臨床試驗檢索，確認是否有任何實際研究支持。
- 在沒有上述證據前，不建議投入進一步的臨床開發資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

