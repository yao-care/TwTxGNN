---
layout: default
title: Prednisone
parent: 高證據等級 (L1-L2)
nav_order: 214
evidence_level: L2
indication_count: 10
---

# Prednisone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Prednisone：從風濕性疾病到圓禿症

## 一句話總結

Prednisone 是一種廣泛使用的皮質類固醇，原本用於風濕性關節炎、氣喘、休克等多種適應症。TxGNN 模型預測它可能對**圓禿症 (Alopecia Areata)** 有效，目前有 **30+ 個臨床試驗**和 **多篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 台灣現無有效單方許可證（已註銷單方證曾載濕疹、過敏症、類風濕關節炎）；唯一有效許可證為 prednisone＋crotamiton 複方軟膏：濕疹或皮膚炎（衛署藥製字第042080號） |
| 預測新適應症 | 圓禿症 (Alopecia Areata) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 台灣上市 | 已上市 |
| 許可證數 | 7 張（有效單方 0／有效複方 1／已註銷 6） |
| 建議決策 | Go |

<!-- review:begin prednisone-original-indication-other-drugs-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／風濕性關節炎、急性病症（氣喘、休克）、皮膚疾患」。原寫的「急性病症（氣喘、休克）」來自主成分登載為 methylprednisone 的已註銷注射劑（內衛藥輸字第003633號），「風濕性關節炎」字樣來自 prednisolone 的已註銷許可證（內衛藥輸字第005124號），都不是 prednisone 的許可證。Prednisone 單方許可證已全部註銷（曾載濕疹、過敏症、類風濕關節炎）；現行唯一有效許可證是與 crotamiton 的複方軟膏（衛署藥製字第042080號，濕疹或皮膚炎）。已改為許可證原文。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end prednisone-original-indication-other-drugs-2026-10-03 -->

## 為什麼這個預測合理？

Prednisone 是一種合成皮質類固醇，具有強效的抗炎和免疫抑制作用。它透過抑制多種炎症介質和免疫細胞功能來發揮作用。

圓禿症是一種自體免疫疾病，特徵是免疫系統攻擊毛囊導致脫髮。這種疾病的病理機轉涉及 T 細胞介導的自體免疫反應。Prednisone 的免疫抑制作用可以抑制這種異常的免疫反應，從而減少對毛囊的攻擊。

臨床上，皮質類固醇（包括 prednisone）已被廣泛用於治療嚴重的圓禿症，特別是與 methotrexate 併用時效果更佳。最新的隨機對照試驗證實了這種組合療法的有效性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | 已完成 | 90 | Methotrexate 加低劑量 prednisone vs 安慰劑治療嚴重圓禿 |
| [NCT02953821](https://clinicaltrials.gov/study/NCT02953821) | Phase 4 | 已完成 | 172 | Acthar Gel 用於系統性紅斑狼瘡患者 |
| [NCT03616964](https://clinicaltrials.gov/study/NCT03616964) | Phase 3 | 已完成 | 778 | Baricitinib 用於系統性紅斑狼瘡 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | Methotrexate 加低劑量 prednisone 對圓禿全禿/普禿有效 |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Journal Article | Dermatology | Methotrexate 與中低劑量皮質類固醇併用治療嚴重圓禿的安全性和療效 |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case Series | Clin Exp Dermatol | Baricitinib 與低劑量皮質類固醇併用治療非常嚴重的圓禿有顯著改善 |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Arch Dermatol | 圓禿治療的療效、安全性和機轉回顧 |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Journal Article | Arch Dermatol | Prednisone 治療圓禿的免疫學研究 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Prednisone 的不重複許可證共 **7 張**：有效單方 0 張、有效複方 1 張、已註銷 6 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第042080號 | 育麗素軟膏 | PREDNISONE、CROTAMITON | 軟膏劑 | 濕疹或皮膚炎 |

<details><summary><strong>已註銷</strong>（6 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第006887號</td><td>育麗素軟膏</td><td>CROTAMITON、PREDNISONE</td><td>1998/07/30</td></tr><tr><td>內衛藥製字第013051號</td><td>百力康軟膏</td><td>PREDNISONE</td><td>1996/08/15</td></tr><tr><td>衛署藥輸字第001597號</td><td>"普強" 去氫可體松</td><td>PREDNISONE</td><td>2016/05/31</td></tr><tr><td>衛部藥輸字第026256號</td><td>樂多特1毫克緩釋錠</td><td>PREDNISONE</td><td>2018/09/10</td></tr><tr><td>衛部藥輸字第026257號</td><td>樂多特2毫克緩釋錠</td><td>PREDNISONE</td><td>2018/09/10</td></tr><tr><td>衛部藥輸字第026258號</td><td>樂多特5毫克緩釋錠</td><td>PREDNISONE</td><td>2018/09/10</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

安全性資訊請參考原廠仿單。

長期使用皮質類固醇的常見注意事項：
- 骨質疏鬆風險
- 血糖升高
- 免疫抑制導致感染風險增加
- 腎上腺皮質功能抑制

## 結論與下一步

**決策：Go**

**理由：**
有高品質的隨機對照試驗（包括 2023 年發表於 JAMA Dermatology 的研究）證實 prednisone 與 methotrexate 併用對嚴重圓禿有效。這個預測有充分的臨床證據支持。

**若要推進需要：**
- 根據患者個別情況評估風險效益
- 考慮與 methotrexate 或 JAK 抑制劑併用
- 制定長期監測計畫（骨密度、血糖等）

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「保癌寧等」列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「原適應症」混入 methylprednisolone 等其他成分的許可證 | 更正（2026-10-03 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

