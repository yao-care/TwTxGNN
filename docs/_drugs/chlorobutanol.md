---
layout: default
title: Chlorobutanol
parent: 僅模型預測 (L5)
nav_order: 61
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

# Chlorobutanol：從結膜炎到勃起功能障礙

## 一句話總結

Chlorobutanol（氯丁醇）是廣泛添加於眼藥水、耳鼻滴劑及注射劑的防腐劑成分，原本核准用於結膜炎、角膜炎等眼科疾病。
TxGNN 模型預測它可能對**勃起功能障礙 (Erectile Dysfunction)** 有效，預測分數高達 **99.79%**，
然而目前**無任何針對此適應症的臨床試驗或文獻支持**，且已知藥理特性與治療方向可能相悖。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 結膜充血、角膜炎、角膜充血 |
| 預測新適應症 | 勃起功能障礙 (Erectile Dysfunction) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 25 張（有效單方 0／有效複方 4／已註銷 21） |
| 建議決策 | Hold |

<!-- review:begin chlorobutanol-original-indication-combo-2026-10-03 -->

> **查核加註（2026-10-03）**：此為複方眼藥水的適應症：內衛藥製字第010694號「"人人"眼用滴劑」含 phenylephrine HCl（血管收縮劑）與 chlorobutanol，結膜充血等適應症屬於整個複方；chlorobutanol 單方許可證（衛署藥輸字第001339號，已註銷）核准的適應症是「防腐劑」。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end chlorobutanol-original-indication-combo-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Chlorobutanol 是一種氯化醇類化合物，具有輕度 CNS 抑制及防腐特性，廣泛添加於眼科、耳鼻科及注射用製劑中，在台灣已取得 25 張許可證（有效 4 張）、多種劑型。

從機轉角度審視，此預測存在根本性矛盾：CNS 抑制劑通常對性功能產生抑制而非促進效果，與勃起功能障礙的標準治療方向（促進 NO/cGMP 路徑、增加陰莖海綿體血流）完全相反。Chlorobutanol 目前無任何已知與陰莖勃起生理相關的藥理作用被報告。

TxGNN 模型的高分預測可能源於知識圖譜中的間接節點關聯，而非直接藥理依據。在缺乏前臨床研究支持的情況下，此預測應視為需要機轉驗證的早期計算信號，而非具有藥理合理性的再利用候選。

---

## 臨床試驗證據

搜尋返回 2 筆結果，但兩者均與 Chlorobutanol 完全無關（相關性等級 C），均為雙極雄激素療法（BAT）治療去勢抗性前列腺癌的試驗——Chlorobutanol 並非研究藥物，勃起功能障礙僅作為雄激素剝奪的背景安全性監測項目出現。以下列出供參考，但不構成任何支持證據：

| 試驗編號 | 階段 | 狀態 | 人數 | 說明 |
|---------|------|------|------|------|
| [NCT02090114](https://clinicaltrials.gov/study/NCT02090114) | Phase 2 | 已完成 | 112 | BAT 序列接 Enzalutamide／Abiraterone 用於轉移性 CRPC；研究藥物與 Chlorobutanol 無關，ED 為副作用背景測量 |
| [NCT02286921](https://clinicaltrials.gov/study/NCT02286921) | Phase 2 | 已完成 | 222 | 比較 BAT 與 Enzalutamide 用於無症狀前列腺癌；研究藥物與 Chlorobutanol 無關，ED 為雄激素剝奪已知副作用的背景記錄 |

**結論：目前無任何以 Chlorobutanol 介入治療勃起功能障礙的臨床試驗登記。**

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Chlorobutanol 的不重複許可證共 **25 張**：有效單方 0 張、有效複方 4 張、已註銷 21 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛成製字第000983號 | 皮速平 | SALICYLIC ACID、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、BE… | 外用液劑 | 香港腳（水蟲病）、金錢癬、灰指甲、牛皮癬、白癬、黴菌性皮膚病 |
| 內衛藥製字第001635號 | 舒滴兒眼藥水 | CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、CHLORPHENIRAMINE… | 點眼液劑 | 結膜炎、角膜炎、淚囊炎、紫外線引起之眼炎、眼充血 |
| 內衛藥製字第010694號 | "人人"眼用滴劑 | PHENYLEPHRINE HCL、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL) | 點眼液劑 | 結膜充血、角膜炎、角膜充血 |
| 衛部藥製字第060942號 | 鼻能爽液 | DIPHENHYDRAMINE、PHENYLEPHRINE、CHLOROBUTANOL (TRICHLORISOBUTY… | 外用液劑 | 鼻炎、鼻塞。 |

<details><summary><strong>已註銷</strong>（21 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第004837號</td><td>鼻能爽液</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、DIPHENHYDRAMINE、P…</td><td>2022/05/06</td></tr><tr><td>內衛藥製字第014160號</td><td>鼻適寧噴劑</td><td>PHENYLEPHRINE HCL、NAPHAZOLINE NITRATE、CHLOROBUTANOL (TRICHLO…</td><td>1993/07/22</td></tr><tr><td>衛署藥製字第028963號</td><td>噴立明眼藥水</td><td>CHLORPHENIRAMINE MALEATE、CHLOROBUTANOL (TRICHLORISOBUTYLIC A…</td><td>1988/09/10</td></tr><tr><td>衛署藥製字第030904號</td><td>"聯邦" 愛麗眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2016/09/30</td></tr><tr><td>衛署藥製字第036308號</td><td>鼻適寧噴劑</td><td>NAPHAZOLINE NITRATE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHO…</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第001147號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>1997/12/05</td></tr><tr><td>衛署藥輸字第001339號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第004353號</td><td>邁舒丁眼藥水</td><td>CHLORAMPHENICOL、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>1985/07/02</td></tr><tr><td>衛署藥輸字第006443號</td><td>羅巴諾注射液</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、GLYCOPYRROLATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第007905號</td><td>東亞目藥水</td><td>PANTOTHENATE CALCIUM、CHONDROITIN SULFATE SODIUM (EQ TO SODIU…</td><td>1995/04/14</td></tr><tr><td>衛署藥輸字第008216號</td><td>斯巴眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第009099號</td><td>愛耳液</td><td>DIPHENHYDRAMINE HCL、CHLORPHENESIN、CHLOROBUTANOL (TRICHLORISO…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009321號</td><td>視美目藥水</td><td>CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL、CHLOROBUTANOL (TRICH…</td><td>1991/08/12</td></tr><tr><td>衛署藥輸字第009417號</td><td>碧露眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>1989/11/02</td></tr><tr><td>衛署藥輸字第010685號</td><td>愛樂目藥水</td><td>NAPHAZOLINE HCL、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、Z…</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第011828號</td><td>舒樂目藥</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>1989/01/05</td></tr><tr><td>衛署藥輸字第012072號</td><td>優汝眼藥水</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、TAURINE (EQ TO 2-…</td><td>1988/08/15</td></tr><tr><td>衛署藥輸字第013022號</td><td>淚膜溶液</td><td>POLYVINYL ALCOHOL、CHLOROBUTANOL ANHYDROUS、SODIUM CHLORIDE</td><td>1991/08/23</td></tr><tr><td>衛署藥輸字第016573號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第017917號</td><td>氯丁醇</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)</td><td>2014/07/16</td></tr><tr><td>衛署藥輸字第018647號</td><td>視美目藥水</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、NAPHAZOLINE、BENZA…</td><td>1999/09/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 前 10 名預測適應症均無直接支持證據（全數 L5），首要預測（勃起功能障礙）的 CNS 抑制機轉與治療目標方向根本相悖，目前不具推進依據。

**若要推進需要：**
- 查詢 DrugBank API 取得 Chlorobutanol 完整的作用機轉與分子靶點資料
- 進行前臨床藥理研究，確認是否存在任何促進勃起功能的生物活性
- 重新評估其他預測適應症（如偏頭痛 #2/#3 的 CNS 抑制連結）是否具備更合理的機轉基礎
- 補充藥物警語、禁忌症及藥物交互作用資料，以完整評估安全性風險

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

