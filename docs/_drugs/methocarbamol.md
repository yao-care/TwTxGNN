---
layout: default
title: Methocarbamol
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
monitor_inn: "Methocarbamol"
predicted_indications: ["cauda equina syndrome", "irritable bowel syndrome", "panuveitis (disease)", "anaphylaxis", "iris disease", "uveitis", "ventricular tachycardia", "food-dependent exercise-induced anaphylaxis", "conjunctivitis", "obsolete bundle branch block"]
last_modified_at: 2026-10-29
description: "Methocarbamol：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：肌肉攣縮症狀、肩痛斜頸、肌肉痙攣"
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Methocarbamol：從肌肉痙攣與肌痛到馬尾症候群 (Cauda Equina Syndrome)
{: .text-alpha }

## 一句話總結

Methocarbamol 是一種中樞性骨骼肌鬆弛劑，在台灣原本用於緩解肌肉攣縮、肩痛、斜頸及腰背痛等症狀。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，但目前**沒有臨床試驗**，也**沒有直接相關的文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肌肉攣縮症狀、肩痛斜頸、肌肉痙攣 |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 6 張／共 39 張） |
| 許可證數 | 39 張（有效單方 6／有效複方 0／已過期 1／已註銷 32） |
| 建議決策 | Hold |

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

目前缺乏詳細的作用機轉資料。Methocarbamol 屬於中樞性骨骼肌鬆弛劑，其機轉尚未完全釐清，一般認為與中樞神經系統抑制有關。

馬尾症候群是脊椎下段神經根受壓所致，常伴隨腰背痛與下肢症狀。Methocarbamol 或許能緩解伴隨的肌肉痙攣與背痛，這可能是模型將兩者連結的原因。然而，它對造成馬尾症候群的神經根壓迫本身沒有已知作用，而該疾病屬於需要緊急手術處理的急症。因此，這個預測在機轉上的支持相當薄弱，最多只能視為症狀緩解的輔助角色，而非疾病治療。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Methocarbamol 的不重複許可證共 **39 張**：有效單方 6 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 32 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（6 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第007888號 | 達士邦錠 | 錠劑 | 豐田藥品股份有限公司 | 2027/08/20 | 腰痛、肌肉痛、四肢痛、關節痛、變形性脊椎症、肌炎、肌肉之異常緊張、強直疼痛 |
| 衛署藥製字第018570號 | 肌樂弛錠５００公絲（每弛卡摩） | 錠劑 | 榮民製藥股份有限公司 | 2029/09/04 | 解除肌肉攣縮症狀（如骨折、脫臼、肩痛、扭傷、背痛、斜頸等所引起肌肉痙攣） |
| 衛署藥製字第028259號 | "七星" ３－（鄰－甲氧基苯氧基）１，２－丙二醇－１－氨基甲酸鹽粉劑 | （粉） | 七星化學製藥股份有限公司 | 2029/08/29 | 肌肉鬆弛劑 |
| 衛署藥製字第039385號 | 寶樂欣膜衣錠５００毫克（每弛卡摩） | 膜衣錠 | 健喬信元醫藥生技股份有限公司 | 2030/02/07 | 肌肉攣縮症狀、肩痛斜頸、肌肉痙攣。 |
| 衛署藥陸輸字第000306號 | 每弛卡摩 | （粉） | 龍大生技股份有限公司 | 2027/12/31 | 肌肉鬆弛劑。 |
| 衛部藥製字第060618號 | 美卡欣錠500毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2031/01/22 | 肌肉攣縮症狀、肩痛斜頸、肌肉痙攣。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第043325號</td><td>"中化合成" 每弛卡摩</td><td>METHOCARBAMOL</td><td>2024/10/25</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（32 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第008884號</td><td>佳復筋片</td><td>METHOCARBAMOL</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第007693號</td><td>扶百生錠</td><td>METHOCARBAMOL</td><td>2014/10/08</td></tr><tr><td>衛署藥製字第008892號</td><td>美受百通錠</td><td>METHOCARBAMOL</td><td>1988/08/01</td></tr><tr><td>衛署藥製字第017582號</td><td>舒腱錠（每弛卡摩）</td><td>METHOCARBAMOL</td><td>1999/12/30</td></tr><tr><td>衛署藥製字第020908號</td><td>"國信"美弛注射液</td><td>METHOCARBAMOL</td><td>2023/07/12</td></tr><tr><td>衛署藥製字第030987號</td><td>美受百通錠５００公絲（每弛卡摩）</td><td>METHOCARBAMOL</td><td>2024/12/09</td></tr><tr><td>衛署藥製字第037055號</td><td>每弛卡痲</td><td>METHOCARBAMOL</td><td>2023/07/06</td></tr><tr><td>衛署藥製字第038228號</td><td>美佳莫</td><td>METHOCARBAMOL</td><td>2001/11/15</td></tr><tr><td>衛署藥製字第038553號</td><td>達士邦錠５００公絲（每弛卡摩）</td><td>METHOCARBAMOL</td><td>2005/11/30</td></tr><tr><td>衛署藥輸字第000352號</td><td>羥丙基氨基甲醯</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000435號</td><td>莫索卡巴莫</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003069號</td><td>滅痛兒注射液</td><td>METHOCARBAMOL</td><td>1985/10/02</td></tr><tr><td>衛署藥輸字第005702號</td><td>絡脾生錠劑</td><td>METHOCARBAMOL</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005813號</td><td>絡脾生注射劑</td><td>METHOCARBAMOL</td><td>1994/04/15</td></tr><tr><td>衛署藥輸字第005860號</td><td>（Ｏ一甲氧苯氧基）羥丙基氨基甲醯</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005924號</td><td>絡脾舒錠劑</td><td>METHOCARBAMOL、ASPIRIN</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第006933號</td><td>美多卡莫爾</td><td>METHOCARBAMOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第007487號</td><td>複合歐力克新注射液</td><td>SODIUM SALICYLATE、METHOCARBAMOL、SULPYRINE (EQ TO DIPYRONE )</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009232號</td><td>胳必新錠</td><td>METHOCARBAMOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第011428號</td><td>邁肌健錠</td><td>METHOCARBAMOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第011651號</td><td>美舒筋錠</td><td>METHOCARBAMOL</td><td>1986/07/04</td></tr><tr><td>衛署藥輸字第012090號</td><td>寶樂欣錠５００公絲</td><td>METHOCARBAMOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第013024號</td><td>每弛卡麻粉劑</td><td>METHOCARBAMOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第015089號</td><td>美佳舒筋錠</td><td>METHOCARBAMOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第015434號</td><td>每弛卡麻</td><td>METHOCARBAMOL</td><td>1992/11/11</td></tr><tr><td>衛署藥輸字第016049號</td><td>克筋炎錠２５０公絲</td><td>METHOCARBAMOL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第017981號</td><td>滅痠錠７５０公絲</td><td>METHOCARBAMOL</td><td>2007/06/28</td></tr><tr><td>衛署藥輸字第017982號</td><td>滅痠錠５００公絲</td><td>METHOCARBAMOL</td><td>2007/06/28</td></tr><tr><td>衛署藥輸字第018597號</td><td>帕巴可欣注射液</td><td>METHOCARBAMOL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第019202號</td><td>絡脾生錠劑</td><td>METHOCARBAMOL</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019203號</td><td>絡脾舒錠劑</td><td>METHOCARBAMOL、ASPIRIN</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019462號</td><td>絡脾生注射劑</td><td>METHOCARBAMOL</td><td>2007/06/28</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的疾病禁忌（非仿單內容）**：TxGNN 知識圖譜（PrimeKG）列出的藥物與疾病禁忌關聯包括癲癇、腎臟疾病、肝臟疾病、膽囊疾病、血小板低下、貧血、消化性潰瘍、胃炎、痛風、物質濫用/依賴、血友病、血管性血友病 (von Willebrand disease)、維生素 K 缺乏出血症、Reye 症候群、阿茲海默症、Pick 病與小腦退化等。這些來自圖譜資料，並非仿單文字，臨床使用前須對照原廠仿單確認。
- **藥物交互作用**：本報告彙整到 126 筆交互作用紀錄。較重要的有：
  - **嚴重 (Major)**：Morphine、Morphine (liposomal)，合併使用可能加強中樞神經抑制。
  - **中度 (Moderate)**：Dronabinol、Nabilone、Metoclopramide、Opium、Sibutramine。
  - 其餘多筆（如 Metformin、Omeprazole、Prednisone 等）的嚴重度標示為未知。

主要警語與仿單禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（證據等級 L5），沒有臨床試驗與直接相關文獻。
- 馬尾症候群的核心問題是神經根壓迫，屬手術急症，而 Methocarbamol 對此沒有已知作用。

**若要推進需要：**
- 補齊 Methocarbamol 的作用機轉資料（MOA）。
- 釐清是否只作為伴隨肌肉痙攣與背痛的症狀輔助治療，而非針對疾病本身。
- 搜尋並評估相關臨床前或臨床研究，確認是否有任何支持證據。
- 若未來考慮推進，需確認劑型與給藥途徑是否符合預期使用情境。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：Methocarbamol Tablets, USP 仿單（Granules）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c) |
| 2026-10-03 | 把抑制多突觸反射弧寫成確定的主要機轉 | 報告重生後已無此錯誤（2026-10-15：新報告寫機轉尚未完全釐清、與中樞神經抑制有關，未再寫抑制多突觸反射弧；原為加註） | [DailyMed：Methocarbamol Tablets, USP 仿單（Granules），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6f0d3966-962d-fa7c-e053-2a91aa0a8e3c) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

