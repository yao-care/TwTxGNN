---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 2
monitor_inn: "Leflunomide"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-10-16
description: "Leflunomide：預測新適應症為短指併指症候群 (Brachydactyly-Syndactyly Syndrome)（證據等級 L5）。原適應症：風濕性關節炎"
---

# Leflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Leflunomide：從類風濕性關節炎到短指併指症候群
{: .text-alpha }

## 一句話總結

Leflunomide 是一種抗風濕藥物（DMARD），原本用於治療成人類風濕性關節炎與活動性乾癬性關節炎。
TxGNN 模型預測它可能對**短指併指症候群 (Brachydactyly-Syndactyly Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 風濕性關節炎 |
| 預測新適應症 | 短指併指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 7 張／共 12 張） |
| 許可證數 | 12 張（有效單方 7／有效複方 0／已註銷 5） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Leflunomide 的活性代謝物 teriflunomide 可抑制二氫乳清酸脫氫酶（DHODH），進而阻斷增殖中淋巴球的嘧啶合成，這是它治療類風濕性關節炎與乾癬性關節炎的基礎。

短指併指症候群是一種肢體發育異常的罕見疾病。就目前所知，DHODH 抑制與肢體形態發生之間並沒有已確立的機轉連結，原適應症（自體免疫性關節炎）與這個先天發育疾病在病理上也相距甚遠。

因此，0.9993 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，不是生物學證據，也不等於有臨床上的支持。此預測應視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Leflunomide 的不重複許可證共 **12 張**：有效單方 7 張、有效複方 0 張、已註銷 5 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第045330號 | "台耀" 耐福諾邁 | （粉） | 台耀化學股份有限公司 | 2028/01/21 | 風濕性關節炎 |
| 衛署藥製字第045971號 | "美時" 雅努麻錠２０毫克 | 錠劑 | 美時化學製藥股份有限公司 | 2028/12/05 | 治療成人類風濕性關節炎，並可能減緩類風濕病程對關節所造成之結構性損害(即屬於DMARD disease modifying antirheumatic drug)。治療具活動性的成… |
| 衛署藥製字第048558號 | "美時" 雅努麻 錠10毫克 | 錠劑 | 美時化學製藥股份有限公司 | 2032/01/26 | 治療成人類風濕性關節炎，並可能減緩類風濕病程對關節所造成之結構性損害(即屬於DMARD disease modifying antirheumatic drug)。 治療具活動性的… |
| 衛部藥輸字第027098號 | 希關炎膜衣錠100毫克 | 膜衣錠 | 西海生技股份有限公司 | 2027/03/28 | 治療成人類風濕性關節炎，並可能減緩類風濕病程對關節所造成之結構性損害（即屬於DMARD DISEASE MODIFYING ANTIRHEUMATIC DRUG）。治療具活動性的成… |
| 衛部藥輸字第027175號 | 希關炎膜衣錠10毫克 | 膜衣錠 | 西海生技股份有限公司 | 2027/06/06 | 治療成人類風濕性關節炎，並可能減緩類風濕病程對關節所造成之結構性損害（即屬於DMARD DISEASE MODIFYING ANTIRHEUMATIC DRUG）。治療具活動性的成… |
| 衛部藥輸字第027176號 | 希關炎膜衣錠20毫克 | 膜衣錠 | 西海生技股份有限公司 | 2027/06/06 | 治療成人類風濕性關節炎，並可能減緩類風濕病程對關節所造成之結構性損害(即屬於DMARD DISEASE MODIFYING ANTIRHEUMATIC DRUG)。治療具活動性的成… |
| 衛部藥輸字第027234號 | 耐福諾邁 | （粉） | 漢旭股份有限公司 | 2027/08/14 | 風濕性關節炎 |

<details><summary><strong>已註銷</strong>（5 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第023615號</td><td>艾炎寧膜衣錠10毫克</td><td>LEFLUNOMIDE</td><td>2026/07/02</td></tr><tr><td>衛署藥輸字第023616號</td><td>艾炎寧膜衣錠20毫克</td><td>LEFLUNOMIDE</td><td>2018/07/03</td></tr><tr><td>衛署藥輸字第023617號</td><td>艾炎寧膜衣錠100毫克</td><td>LEFLUNOMIDE</td><td>2018/07/03</td></tr><tr><td>衛部藥輸字第026363號</td><td>福納膜衣錠10毫克</td><td>LEFLUNOMIDE</td><td>2022/07/07</td></tr><tr><td>衛部藥輸字第026364號</td><td>福納膜衣錠20毫克</td><td>LEFLUNOMIDE</td><td>2022/07/07</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物－疾病禁忌關聯，並非仿單原文）：
  - 肝臟：肝衰竭、肝病、慢性 B 型／C 型肝炎病毒感染、膽囊疾病
  - 血液：血小板低下、嗜中性白血球低下、顆粒球缺乏症、全血球低下、貧血（含巨球性貧血）及多種先天性嗜中性白血球低下症
  - 其他：腎臟病、周邊神經病變、間質性肺病、肺囊蟲症、麴菌症
- **藥物交互作用**：資料庫共收錄 677 筆交互作用，以下為部分列舉：
  - 嚴重（Major）：Acarbose、Pioglitazone、Bupropion、Acetylsalicylic acid、Clarithromycin、Minocycline、Naltrexone，以及 Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide 等類固醇
  - 中度（Moderate）：Metronidazole、Chlorpropamide、Acetohexamide

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測沒有任何臨床試驗或文獻佐證，證據等級僅為 L5，且機轉上找不到與肢體發育異常的合理連結。
- Leflunomide 的安全性疑慮不少（肝臟、血液、肺部等禁忌關聯，以及大量交互作用），對缺乏療效依據的罕見先天疾病而言，風險效益難以成立。

**若要推進需要：**
- 補齊詳細的作用機轉資料，並釐清 DHODH 抑制與該疾病致病路徑（如肢體發育相關訊號）是否有關
- 進行系統性文獻檢索與前臨床（細胞或動物模型）驗證
- 評估該疾病的致病機轉是否為藥物可介入的標的，以及是否有合適的給藥族群與途徑
- 若前述驗證出現正面訊號，再規劃安全性監測方案

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 艾炎寧膜衣錠10毫克許可證狀態 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 美時雅努麻錠10毫克許可證效期 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

