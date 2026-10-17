---
layout: default
title: Silicon Dioxide
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-16
description: "Silicon Dioxide：預測新適應症為活動性消化性潰瘍 (Active Peptic Ulcer Disease)（證據等級 L5）。原適應症：賦形劑、氣體吸著劑"
---

# Silicon Dioxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# 二氧化矽 (Silicon dioxide)：從賦形劑與氣體吸著劑到活動性消化性潰瘍

<!-- review:begin silicon_dioxide-antacid-combo-title-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「# 二氧化矽 (Silicon dioxide)：從祛痰與制酸輔助用途到活動性消化性潰瘍」。TFDA 許可證資料中，二氧化矽單方許可證只有衛署藥輸字第006893號「矽酸」（賦形劑）與第012366號「矽凝膠」（氣體吸著劑），皆已註銷。含二氧化矽的複方中，寫祛痰的如息速坦腸溶糖衣錠（衛署藥製字第030558號、第033025號，與 mecysteine 的複方，皆已註銷），寫營養補給的如維生素礦物質複方（衛署藥輸字第022252號，已註銷），寫制酸劑的如與氧化鋁、矽酸鎂鋁的複方「二矽酸鋁鎂」（衛署藥輸字第024482號，有效期至 2026-07-07，已過期）。二氧化矽本身不是制酸或祛痰成分。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-title-2026-10-16 -->

## 一句話總結

二氧化矽在台灣多以賦形劑、氣體吸著劑及制酸劑複方成分的形式使用，單方許可證（皆已註銷）核准的是賦形劑與氣體吸著劑；祛痰、胃酸過多屬於含二氧化矽的複方（皆已註銷或過期）的適應症。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
但目前**沒有臨床試驗與文獻**支持，僅有模型預測。

<!-- review:begin silicon_dioxide-antacid-combo-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「原本涉及祛痰、胃酸過多與鼓腸等用途。」。TFDA 許可證資料中，二氧化矽單方許可證只有衛署藥輸字第006893號「矽酸」（賦形劑）與第012366號「矽凝膠」（氣體吸著劑），皆已註銷。含二氧化矽的複方中，寫祛痰的如息速坦腸溶糖衣錠（衛署藥製字第030558號、第033025號，與 mecysteine 的複方，皆已註銷），寫營養補給的如維生素礦物質複方（衛署藥輸字第022252號，已註銷），寫制酸劑的如與氧化鋁、矽酸鎂鋁的複方「二矽酸鋁鎂」（衛署藥輸字第024482號，有效期至 2026-07-07，已過期）。二氧化矽本身不是制酸或祛痰成分。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-summary-2026-10-16 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 賦形劑、氣體吸著劑（二氧化矽單方許可證，皆已註銷）；含二氧化矽的制酸劑複方「二矽酸鋁鎂」（衛署藥輸字第024482號）已於 2026-07-07 過期 |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 截至資料集日期無主成分登載為二氧化矽的有效許可證（唯一未註銷的複方「二矽酸鋁鎂」已於 2026-07-07 過期） |
| 許可證數 | 20 張（有效單方 0／有效複方 0／已過期 1／已註銷 19） |
| 建議決策 | Hold |

<!-- review:begin silicon_dioxide-antacid-combo-row-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「原適應症／氣體吸著劑、賦形劑、維生素（單方許可證皆已註銷；現行有效者為制酸劑複方）」。TFDA 許可證資料中，二氧化矽單方許可證只有衛署藥輸字第006893號「矽酸」（賦形劑）與第012366號「矽凝膠」（氣體吸著劑），皆已註銷。含二氧化矽的複方中，寫祛痰的如息速坦腸溶糖衣錠（衛署藥製字第030558號、第033025號，與 mecysteine 的複方，皆已註銷），寫營養補給的如維生素礦物質複方（衛署藥輸字第022252號，已註銷），寫制酸劑的如與氧化鋁、矽酸鎂鋁的複方「二矽酸鋁鎂」（衛署藥輸字第024482號，有效期至 2026-07-07，已過期）。二氧化矽本身不是制酸或祛痰成分。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-row-2026-10-16 -->

<!-- review:begin silicon_dioxide-antacid-combo-marketed-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「台灣上市／✓ 已上市（僅 1 張有效複方許可證）」。截至資料集日期（2026-09-29），台灣沒有主成分欄登載為二氧化矽的有效許可證：唯一未註銷的含二氧化矽制酸複方「二矽酸鋁鎂」（衛署藥輸字第024482號）已於 2026-07-07 過期，其餘都已註銷（含 simethicone 等矽酮成分的製劑不在此列）。本頁許可證數列也是有效單方 0、有效複方 0。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-marketed-2026-10-16 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，二氧化矽在台灣多作為賦形劑、氣體吸著劑，以及制酸劑複方（例如與鋁、鎂矽酸鹽合用）的成分，其在胃酸過多、胃灼熱等症狀緩解上的角色已有許可證適應症可循。

<!-- review:begin silicon_dioxide-antacid-combo-why-2026-10-16 -->

> **查核加註（2026-10-16）**：TFDA 許可證資料中，二氧化矽單方許可證只有衛署藥輸字第006893號「矽酸」（賦形劑）與第012366號「矽凝膠」（氣體吸著劑），皆已註銷。含二氧化矽的複方中，寫祛痰的如息速坦腸溶糖衣錠（衛署藥製字第030558號、第033025號，與 mecysteine 的複方，皆已註銷），寫營養補給的如維生素礦物質複方（衛署藥輸字第022252號，已註銷），寫制酸劑的如與氧化鋁、矽酸鎂鋁的複方「二矽酸鋁鎂」（衛署藥輸字第024482號，有效期至 2026-07-07，已過期）。二氧化矽本身不是制酸或祛痰成分。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-why-2026-10-16 -->

消化性潰瘍與胃酸過多在病理上相關，因此制酸類產品可能緩解酸相關症狀。不過，沒有證據顯示二氧化矽能促進潰瘤癒合或治療潰瘍的根本病因。這項預測主要來自知識圖譜中與潰瘍相關疾病的網路鄰近性，以及制酸相關的標示用途。

<!-- review:begin silicon_dioxide-antacid-combo-label-use-2026-10-16 -->

> **查核加註（2026-10-16）**：截至資料集日期（2026-09-29），台灣沒有主成分欄登載為二氧化矽的有效許可證：唯一未註銷的含二氧化矽制酸複方「二矽酸鋁鎂」（衛署藥輸字第024482號）已於 2026-07-07 過期，其餘都已註銷（含 simethicone 等矽酮成分的製劑不在此列）。二氧化矽單方許可證（皆已註銷）核准的是賦形劑與氣體吸著劑，沒有制酸用途。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-label-use-2026-10-16 -->

其他預測也有類似限制：吻合口潰瘍 (gastrojejunal ulcer) 與胃潰瘍 (gastric ulcer) 同樣僅有症狀緩解的間接關聯。消化性潰瘍穿孔 (peptic ulcer perforation) 是急性外科併發症，制酸劑或吸著性賦形劑在其中沒有合理的治療角色，該預測較可能是模型的假陽性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Silicon Dioxide 的不重複許可證共 **20 張**：有效單方 0 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 19 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥輸字第024482號</td><td>二矽酸鋁鎂</td><td>ALUMINUM OXIDE (ALUMINA)、ALUMINUM MAGNESIUM SILICATE、SILICON…</td><td>2026/07/07</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（19 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第023669號</td><td>美爾胃膠囊（斯比樂）”大同”　　　　　　　　　　　　　　　　 S</td><td>SULPIRIDE、SILICON DIOXIDE (SILICA GEL)</td><td>1989/11/28</td></tr><tr><td>衛署藥製字第029865號</td><td>佳樂心膠囊２００公絲（歐轉惠寧）</td><td>OXTRIPHYLLINE、SILICON DIOXIDE (SILICA GEL)</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第030558號</td><td>息速坦腸溶糖衣錠１００公絲（西士恩）</td><td>SILICON DIOXIDE (SILICA GEL)、MECYSTEINE HCL (CYSTEINE L- MET…</td><td>1990/12/14</td></tr><tr><td>衛署藥製字第033025號</td><td>息速坦腸溶糖衣錠１００公絲（西士恩）</td><td>SILICON DIOXIDE (SILICA GEL)、MECYSTEINE HCL (CYSTEINE L- MET…</td><td>1998/08/17</td></tr><tr><td>衛署藥製字第036028號</td><td>喜滿佳靈－愛（矽酸鎂鋁）</td><td>SILICON DIOXIDE (SILICA GEL)、ALUMINUM OXIDE (ALUMINA)、MAGNES…</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第036030號</td><td>喜滿佳靈（偏矽酸鎂鋁）</td><td>ALUMINUM OXIDE (ALUMINA)、SILICON DIOXIDE (SILICA GEL)、MAGNES…</td><td>2023/06/30</td></tr><tr><td>衛署藥輸字第002867號</td><td>製錠輔助劑Ｔ型</td><td>CARMELLOSE (CARBOXYMETHYLCELLULOSE)、CELLULOSE、SILICON DIOXID…</td><td>1986/01/16</td></tr><tr><td>衛署藥輸字第002868號</td><td>製錠輔助劑克型</td><td>CARMELLOSE (CARBOXYMETHYLCELLULOSE)、STARCH、CELLULOSE、MAGNESI…</td><td>1986/06/03</td></tr><tr><td>衛署藥輸字第006893號</td><td>矽酸</td><td>SILICON DIOXIDE (SILICA GEL)</td><td>1992/07/09</td></tr><tr><td>衛署藥輸字第011812號</td><td>適胃爽錠</td><td>MAGNESIUM TRISILICATE、MAGNESIUM HYDROXIDE、CALCIUM CARBONATE…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第012366號</td><td>矽凝膠</td><td>SILICON DIOXIDE COLLOIDAL(COLLOIDAL SILICA)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第013408號</td><td>利護腸錠</td><td>SILICON DIOXIDE COLLOIDAL(COLLOIDAL SILICA)、SIMETHICONE (ACT…</td><td>1988/03/12</td></tr><tr><td>衛署藥輸字第013587號</td><td>舒汝胃凝膠</td><td>CARMELLOSE SODIUM (CMC SOD.)(CELLULOSE GUM SOD.)、CALCIUM CAR…</td><td>1991/11/26</td></tr><tr><td>衛署藥輸字第014632號</td><td>製錠輔助劑Ｄ型</td><td>SILICON DIOXIDE (SILICA GEL)、CARMELLOSE (CARBOXYMETHYLCELLUL…</td><td>1990/06/23</td></tr><tr><td>衛署藥輸字第016328號</td><td>利護腸錠</td><td>SILICON DIOXIDE COLLOIDAL(COLLOIDAL SILICA)、SIMETHICONE (ACT…</td><td>1990/07/04</td></tr><tr><td>衛署藥輸字第017858號</td><td>利護腸錠</td><td>CALCIUM ARACHINATE、SILICON DIOXIDE COLLOIDAL(COLLOIDAL SILIC…</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第017958號</td><td>製錠輔助劑Ｄ型</td><td>CELLULOSE、SILICON DIOXIDE (SILICA GEL)、MAGNESIUM STEARATE (E…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第018615號</td><td>"富田" 二矽酸鋁鎂</td><td>ALUMINUM MAGNESIUM SILICATE、SILICON DIOXIDE (SILICA GEL)、ALU…</td><td>2017/04/12</td></tr><tr><td>衛署藥輸字第022252號</td><td>高品安利納華陀錠</td><td>DEHYDROACETATE SODIUM、RIBOFLAVIN (VIT B2)、CALCIUM CARBONATE…</td><td>2010/09/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單文字）：腎臟病、輸尿管積膿、鬱血性心衰竭、腹瀉性疾病、慢性腹瀉、便祕、低磷血症、腸道阻塞（糞便嵌塞）、痔瘡。
  這些多與含鋁、鎂的制酸複方有關，實際使用前仍須對照個別產品仿單。

其餘警語、禁忌與藥物交互作用資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或文獻佐證，證據等級僅為 L5，且缺乏作用機轉資料。
- 二氧化矽最多只可能緩解酸相關症狀，無證據顯示能治療潰瘍本身；穿孔等急性併發症更無合理的治療角色。

<!-- review:begin silicon_dioxide-antacid-combo-conclusion-2026-10-16 -->

> **查核加註（2026-10-16）**：TFDA 許可證資料中，二氧化矽單方許可證只有衛署藥輸字第006893號「矽酸」（賦形劑）與第012366號「矽凝膠」（氣體吸著劑），皆已註銷。含二氧化矽的複方中，寫祛痰的如息速坦腸溶糖衣錠（衛署藥製字第030558號、第033025號，與 mecysteine 的複方，皆已註銷），寫營養補給的如維生素礦物質複方（衛署藥輸字第022252號，已註銷），寫制酸劑的如與氧化鋁、矽酸鎂鋁的複方「二矽酸鋁鎂」（衛署藥輸字第024482號，有效期至 2026-07-07，已過期）。二氧化矽本身不是制酸或祛痰成分。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-conclusion-2026-10-16 -->

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料，釐清二氧化矽本身（而非複方中其他制酸成分）的貢獻。
- 進行系統性文獻搜尋，確認是否有制酸或吸著作用與潰瘍症狀緩解的臨床資料。
- 若要發展，應將目標限縮為「症狀緩解」而非「潰瘍治療」，並以含二氧化矽的現有制酸複方為對象設計研究。
- 針對知識圖譜標示的禁忌族群（如腎臟病、心衰竭、便祕或腸阻塞）建立安全性評估。

<!-- review:begin silicon_dioxide-antacid-combo-study-target-2026-10-16 -->

> **查核加註（2026-10-16）**：截至資料集日期（2026-09-29），台灣沒有主成分欄登載為二氧化矽的有效許可證：唯一未註銷的含二氧化矽制酸複方「二矽酸鋁鎂」（衛署藥輸字第024482號）已於 2026-07-07 過期，其餘都已註銷（含 simethicone 等矽酮成分的製劑不在此列）。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end silicon_dioxide-antacid-combo-study-target-2026-10-16 -->

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「息速坦腸溶糖衣錠100公絲」列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「原適應症」的制酸劑、胃酸過多來自複方 | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列已寫明單方許可證皆已註銷；同列「現行有效者為制酸劑複方」（該複方已於 2026-07-07 過期）與「維生素」仍不正確，另有查核紀錄更正；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 原適應症列入「維生素」 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 標題以祛痰與制酸為原用途 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結稱原本涉及祛痰、胃酸過多 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 預測理由稱胃酸過多已有許可證適應症 | 加註（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 結論稱二氧化矽可緩解酸相關症狀 | 加註（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 台灣上市列寫「僅 1 張有效複方」 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 下一步以現有制酸複方為研究對象 | 加註（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 預測理由稱有制酸相關的標示用途 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

