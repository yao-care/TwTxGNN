---
layout: default
title: Methocarbamol
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Methocarbamol
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

# Methocarbamol 藥師筆記

## 一句話總結

Methocarbamol 是一種中樞性骨骼肌鬆弛劑，TxGNN 預測其可能對馬尾症候群、腸躁症等神經肌肉相關疾病有治療潛力，但目前缺乏臨床證據支持這些新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Methocarbamol（每弛卡摩） |
| DrugBank ID | DB00423 |
| 台灣商品名 | 佳復筋片、達士邦錠、寶樂欣膜衣錠、肌樂弛錠、美卡欣錠 |
| 原核准適應症 | 肌肉攣縮症狀、腰痛、背痛、頸肩腕疼痛、肌肉痙攣 |
| 預測新適應症 | 馬尾症候群、腸躁症、全葡萄膜炎、過敏性休克、心室頻脈 |
| 最高預測分數 | 0.9998（馬尾症候群） |
| 證據等級 | L5（僅預測） |

---

<!-- review:begin methocarbamol-moa-2026-10-03 -->

## Methocarbamol 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- 美國仿單寫明：methocarbamol 在人體的作用機轉**尚未確立**，可能與整體的中樞神經系統抑制有關。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c)）
- 它不直接作用在橫紋肌的收縮機制、運動終板或神經纖維上，所以不是直接讓肌肉本身放鬆。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c)）

**來源**：[DailyMed：Methocarbamol Tablets, USP 仿單（Granules Pharmaceuticals），Clinical Pharmacology 段](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c)，版本日期 2026-07-07；查閱日期 2026-10-03。

---

<!-- review:end methocarbamol-moa-2026-10-03 -->

## 為什麼這個預測合理？

### 藥理機轉分析

Methocarbamol 作為中樞性肌肉鬆弛劑，主要作用於中樞神經系統抑制多突觸反射弧。其機轉與預測適應症的關聯：

<!-- review:begin methocarbamol-moa-polysynaptic-2026-10-03 -->

> **查核加註（2026-10-03）**：仿單寫 methocarbamol 在人體的作用機轉尚未確立，可能與一般性中樞神經抑制有關；「抑制多突觸反射弧」不是仿單確認的機轉。原文保留。依據：[DailyMed：Methocarbamol Tablets, USP 仿單（Granules），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c)。

<!-- review:end methocarbamol-moa-polysynaptic-2026-10-03 -->

1. **馬尾症候群**（TxGNN Score: 0.9998）
   - 馬尾症候群常伴隨嚴重的肌肉痙攣
   - Methocarbamol 的肌肉鬆弛作用可能有助於緩解相關症狀
   - 但無法治療根本的神經壓迫病因

2. **腸躁症**（TxGNN Score: 0.9998）
   - 腸道平滑肌功能異常是腸躁症的特徵之一
   - 骨骼肌鬆弛劑對平滑肌的作用有限
   - 預測合理性較低

3. **過敏性休克**（TxGNN Score: 0.9996）
   - 有文獻報導 Methocarbamol 用於蜘蛛咬傷引起的全身反應輔助治療
   - 但非第一線治療藥物

---

## 臨床試驗證據

| 疾病 | 臨床試驗數量 | 最高期別 | 證據等級 |
|------|-------------|---------|---------|
| 馬尾症候群 | 0 | - | L5 |
| 腸躁症 | 0 | - | L5 |
| 全葡萄膜炎 | 0 | - | L5 |
| 過敏性休克 | 0 | - | L5 |

**結論：目前無任何預測適應症進入臨床試驗階段。**

---

## 文獻證據

### 過敏性休克相關文獻

| PMID | 標題 | 年份 | 類型 |
|------|------|------|------|
| 20086833 | Managing arthropod bites and stings | 1998 | 期刊文章 |

**文獻摘要**：此文章提到 Methocarbamol 可用於黑寡婦蜘蛛咬傷的全身反應處理，作為輔助治療。然而，過敏性休克的第一線治療仍為 epinephrine 和抗組織胺藥物。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Methocarbamol 的不重複許可證共 **39 張**：有效單方 7 張、有效複方 0 張、已註銷 32 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第007888號 | 達士邦錠 | 錠劑 | 豐田藥品股份有限公司 | 2027/08/20 | 腰痛、肌肉痛、四肢痛、關節痛、變形性脊椎症、肌炎、肌肉之異常緊張、強直疼痛 |
| 衛署藥製字第018570號 | 肌樂弛錠５００公絲（每弛卡摩） | 錠劑 | 榮民製藥股份有限公司 | 2029/09/04 | 解除肌肉攣縮症狀（如骨折、脫臼、肩痛、扭傷、背痛、斜頸等所引起肌肉痙攣） |
| 衛署藥製字第028259號 | "七星" ３－（鄰－甲氧基苯氧基）１，２－丙二醇－１－氨基甲酸鹽粉劑 | （粉） | 七星化學製藥股份有限公司 | 2029/08/29 | 肌肉鬆弛劑 |
| 衛署藥製字第039385號 | 寶樂欣膜衣錠５００毫克（每弛卡摩） | 膜衣錠 | 健喬信元醫藥生技股份有限公司 | 2030/02/07 | 肌肉攣縮症狀、肩痛斜頸、肌肉痙攣。 |
| 衛署藥製字第043325號 | "中化合成" 每弛卡摩 | （粉） | 中化合成生技股份有限公司山佳工廠 | 2024/10/25 | 肌肉鬆弛劑。 |
| 衛署藥陸輸字第000306號 | 每弛卡摩 | （粉） | 龍大生技股份有限公司 | 2027/12/31 | 肌肉鬆弛劑。 |
| 衛部藥製字第060618號 | 美卡欣錠500毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2031/01/22 | 肌肉攣縮症狀、肩痛斜頸、肌肉痙攣。 |

<details><summary><strong>已註銷</strong>（32 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第008884號</td><td>佳復筋片</td><td>METHOCARBAMOL</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第007693號</td><td>扶百生錠</td><td>METHOCARBAMOL</td><td>2014/10/08</td></tr><tr><td>衛署藥製字第008892號</td><td>美受百通錠</td><td>METHOCARBAMOL</td><td>1988/08/01</td></tr><tr><td>衛署藥製字第017582號</td><td>舒腱錠（每弛卡摩）</td><td>METHOCARBAMOL</td><td>1999/12/30</td></tr><tr><td>衛署藥製字第020908號</td><td>"國信"美弛注射液</td><td>METHOCARBAMOL</td><td>2023/07/12</td></tr><tr><td>衛署藥製字第030987號</td><td>美受百通錠５００公絲（每弛卡摩）</td><td>METHOCARBAMOL</td><td>2024/12/09</td></tr><tr><td>衛署藥製字第037055號</td><td>每弛卡痲</td><td>METHOCARBAMOL</td><td>2023/07/06</td></tr><tr><td>衛署藥製字第038228號</td><td>美佳莫</td><td>METHOCARBAMOL</td><td>2001/11/15</td></tr><tr><td>衛署藥製字第038553號</td><td>達士邦錠５００公絲（每弛卡摩）</td><td>METHOCARBAMOL</td><td>2005/11/30</td></tr><tr><td>衛署藥輸字第000352號</td><td>羥丙基氨基甲醯</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000435號</td><td>莫索卡巴莫</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003069號</td><td>滅痛兒注射液</td><td>METHOCARBAMOL</td><td>1985/10/02</td></tr><tr><td>衛署藥輸字第005702號</td><td>絡脾生錠劑</td><td>METHOCARBAMOL</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005813號</td><td>絡脾生注射劑</td><td>METHOCARBAMOL</td><td>1994/04/15</td></tr><tr><td>衛署藥輸字第005860號</td><td>（Ｏ一甲氧苯氧基）羥丙基氨基甲醯</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005924號</td><td>絡脾舒錠劑</td><td>METHOCARBAMOL、ASPIRIN</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第006933號</td><td>美多卡莫爾</td><td>METHOCARBAMOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第007487號</td><td>複合歐力克新注射液</td><td>SODIUM SALICYLATE、METHOCARBAMOL、SULPYRINE (EQ TO DIPYRONE )</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009232號</td><td>胳必新錠</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第011428號</td><td>邁肌健錠</td><td>METHOCARBAMOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第011651號</td><td>美舒筋錠</td><td>METHOCARBAMOL</td><td>1986/07/04</td></tr><tr><td>衛署藥輸字第012090號</td><td>寶樂欣錠５００公絲</td><td>METHOCARBAMOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第013024號</td><td>每弛卡麻粉劑</td><td>METHOCARBAMOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第015089號</td><td>美佳舒筋錠</td><td>METHOCARBAMOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第015434號</td><td>每弛卡麻</td><td>METHOCARBAMOL</td><td>1992/11/11</td></tr><tr><td>衛署藥輸字第016049號</td><td>克筋炎錠２５０公絲</td><td>METHOCARBAMOL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第017981號</td><td>滅痠錠７５０公絲</td><td>METHOCARBAMOL</td><td>2007/06/28</td></tr><tr><td>衛署藥輸字第017982號</td><td>滅痠錠５００公絲</td><td>METHOCARBAMOL</td><td>2007/06/28</td></tr><tr><td>衛署藥輸字第018597號</td><td>帕巴可欣注射液</td><td>METHOCARBAMOL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第019202號</td><td>絡脾生錠劑</td><td>METHOCARBAMOL</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019203號</td><td>絡脾舒錠劑</td><td>METHOCARBAMOL、ASPIRIN</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019462號</td><td>絡脾生注射劑</td><td>METHOCARBAMOL</td><td>2007/06/28</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

### 藥物交互作用

| 交互作用藥物 | 嚴重程度 | 來源 |
|-------------|---------|------|
| Morphine | 重度（Major） | DDInter |
| Morphine (liposomal) | 重度（Major） | DDInter |
| Dronabinol | 中度（Moderate） | DDInter |
| Nabilone | 中度（Moderate） | DDInter |
| Metoclopramide | 中度（Moderate） | DDInter |
| Opium | 中度（Moderate） | DDInter |

### 主要警告

- 與鴉片類藥物併用可能增強中樞神經抑制作用
- 與大麻素類藥物併用需謹慎
- 可能影響駕駛和操作機械的能力

---

## 結論與下一步

### 評估結論

| 評估項目 | 結果 |
|---------|------|
| 預測可信度 | 中等（高 TxGNN 分數但缺乏臨床證據） |
| 臨床轉譯可行性 | 低 |
| 建議優先順序 | 不建議優先開發 |

### 建議

1. **馬尾症候群**：Methocarbamol 可能作為症狀緩解的輔助用藥，但不能作為主要治療
2. **腸躁症**：藥理機轉不支持，不建議進一步研究
3. **過敏性休克**：僅作為蜘蛛咬傷的輔助治療，非老藥新用的適當目標

### 後續行動

- [ ] 監測是否有新的臨床試驗啟動
- [ ] 關注馬尾症候群輔助治療的文獻報告
- [ ] 暫不建議投入資源進行臨床開發

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：Methocarbamol Tablets, USP 仿單（Granules）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c) |
| 2026-10-03 | 把抑制多突觸反射弧寫成確定的主要機轉 | 加註 | [DailyMed：Methocarbamol Tablets, USP 仿單（Granules），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

