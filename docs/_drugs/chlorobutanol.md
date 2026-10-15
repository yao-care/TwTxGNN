---
layout: default
title: Chlorobutanol
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Chlorobutanol
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

# Chlorobutanol：從結膜炎與角膜炎到勃起功能障礙

## 一句話總結

Chlorobutanol（氯丁醇）是一種氯醛衍生物，在台灣主要作為眼用、鼻用及外用複方製劑的成分，常見用途為防腐與輔助治療結膜炎、角膜炎。
TxGNN 模型預測它可能對**勃起功能障礙 (Erectile Dysfunction)** 有效，但目前**沒有任何臨床試驗與文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 防腐劑（台灣單方許可證皆為防腐劑用途，且均已註銷）；現行有效許可證皆為複方，用於結膜充血、角膜炎等眼部症狀 |
| 預測新適應症 | 勃起功能障礙 (Erectile Dysfunction) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市（僅複方有效） |
| 許可證數 | 25 張（有效單方 0／有效複方 4／已註銷 21） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Chlorobutanol 是氯醛衍生物，一般認為具有輕度鎮靜與局部麻醉作用，並有抗菌防腐性質，因此常被用作眼用及外用製劑的防腐劑。

勃起功能障礙涉及血管內皮功能、神經傳導與平滑肌舒張等機制，與 chlorobutanol 的已知用途（局部防腐、輕度鎮靜）之間**沒有明確的關聯**。這個高分預測目前只能視為模型的關聯推論，缺乏機轉與臨床依據。

另外值得注意，TxGNN 的前 10 名預測還包括偏頭痛（多個亞型）、妥瑞氏症、拔毛症、注意力不足過動症等，多數為神經精神疾病，其背後的推測理由（可能影響神經興奮性）同樣屬於推測，沒有任何證據支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Chlorobutanol 的不重複許可證共 **25 張**：有效單方 0 張、有效複方 4 張、已註銷 21 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛成製字第000983號 | 皮速平 | SALICYLIC ACID、Compound tincture benzoin、CHLOROBUTANOL (TRIC… | 外用液劑 | 香港腳（水蟲病）、金錢癬、灰指甲、牛皮癬、白癬、黴菌性皮膚病 |
| 內衛藥製字第001635號 | 舒滴兒眼藥水 | PANTOTHENATE CALCIUM、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOH… | 點眼液劑 | 結膜炎、角膜炎、淚囊炎、紫外線引起之眼炎、眼充血 |
| 內衛藥製字第010694號 | "人人"眼用滴劑 | CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、PHENYLEPHRINE HCL | 點眼液劑 | 結膜充血、角膜炎、角膜充血 |
| 衛部藥製字第060942號 | 鼻能爽液 | PHENYLEPHRINE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、DIP… | 外用液劑 | 鼻炎、鼻塞。 |

<details><summary><strong>已註銷</strong>（21 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第004837號</td><td>鼻能爽液</td><td>PHENYLEPHRINE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、DIP…</td><td>2022/05/06</td></tr><tr><td>內衛藥製字第014160號</td><td>鼻適寧噴劑</td><td>NAPHAZOLINE NITRATE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHO…</td><td>1993/07/22</td></tr><tr><td>衛署藥製字第028963號</td><td>噴立明眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>1988/09/10</td></tr><tr><td>衛署藥製字第030904號</td><td>"聯邦" 愛麗眼藥水</td><td>CYANOCOBALAMIN (VIT B12)、CHLORPHENIRAMINE MALEATE、CHLOROBUTA…</td><td>2016/09/30</td></tr><tr><td>衛署藥製字第036308號</td><td>鼻適寧噴劑</td><td>PHENYLEPHRINE HCL、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)…</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第001147號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>1997/12/05</td></tr><tr><td>衛署藥輸字第001339號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第004353號</td><td>邁舒丁眼藥水</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、CHLORAMPHENICOL</td><td>1985/07/02</td></tr><tr><td>衛署藥輸字第006443號</td><td>羅巴諾注射液</td><td>GLYCOPYRROLATE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第007905號</td><td>東亞目藥水</td><td>CHLORPHENIRAMINE MALEATE、CHONDROITIN SULFATE SODIUM (EQ TO S…</td><td>1995/04/14</td></tr><tr><td>衛署藥輸字第008216號</td><td>斯巴眼藥水</td><td>GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSIUM GLYCYRRHIZINA…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第009099號</td><td>愛耳液</td><td>DIPHENHYDRAMINE HCL、UREA、CHLORPHENESIN、CHLOROBUTANOL (TRICHL…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009321號</td><td>視美目藥水</td><td>PYRIDOXINE HCL、BENZALKONIUM CHLORIDE、VITAMIN A、PANTOTHENATE…</td><td>1991/08/12</td></tr><tr><td>衛署藥輸字第009417號</td><td>碧露眼藥水</td><td>CHLORPHENIRAMINE MALEATE、CHONDROITIN SULFATE SODIUM (EQ TO S…</td><td>1989/11/02</td></tr><tr><td>衛署藥輸字第010685號</td><td>愛樂目藥水</td><td>TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、NAPHAZOLINE HCL、…</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第011828號</td><td>舒樂目藥</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、NAPHAZOLINE HCL、T…</td><td>1989/01/05</td></tr><tr><td>衛署藥輸字第012072號</td><td>優汝眼藥水</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、TAURINE (EQ TO 2-…</td><td>1988/08/15</td></tr><tr><td>衛署藥輸字第013022號</td><td>淚膜溶液</td><td>CHLOROBUTANOL ANHYDROUS、SODIUM CHLORIDE、POLYVINYL ALCOHOL</td><td>1991/08/23</td></tr><tr><td>衛署藥輸字第016573號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第017917號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>2014/07/16</td></tr><tr><td>衛署藥輸字第018647號</td><td>視美目藥水</td><td>NAPHAZOLINE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、CHLOR…</td><td>1999/09/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.79%），但沒有任何臨床試驗或文獻，證據等級僅為 L5。
- 作用機轉資料缺乏，與勃起功能障礙之間也沒有可辨識的藥理關聯；現有安全性資料也不足以支持轉換用途。

**若要推進需要：**
- 補齊 chlorobutanol 的作用機轉資料（如查詢 DrugBank）
- 進行系統性文獻檢索與前臨床研究，驗證對勃起功能相關機制的作用
- 評估劑型與給藥途徑的適配性（現有劑型為眼用、鼻用、外用與耳用，並非全身性給藥）
- 補齊完整的安全性與藥物交互作用資料

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」為含 phenylephrine 複方眼藥水的適應症 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表中 4 張成品皆為複方 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

