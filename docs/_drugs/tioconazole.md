---
layout: default
title: Tioconazole
parent: 高證據等級 (L1-L2)
nav_order: 280
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-16
description: "Tioconazole：預測新適應症為外陰陰道炎 (Vulvovaginitis)（證據等級 L2）。原適應症：感受性黴菌引起之局部感染"
monitor_inn: "Tioconazole"
predicted_indications: ["vulvitis", "postmenopausal atrophic vaginitis"]
---

# Tioconazole
{: .fs-9 }

證據等級: **L2** | 預測適應症: **3** 個
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

# Tioconazole：從黴菌局部感染到外陰陰道炎

## 一句話總結

Tioconazole（治可那唑）是咪唑類（imidazole）抗黴菌藥，原本用於感受性黴菌引起之局部感染。
TxGNN 模型預測它可能對**外陰陰道炎 (Vulvovaginitis)** 有效，
目前有 **0 個臨床試驗登記**，但有 **約 20 篇文獻**支持這個方向，其中包含 2 篇 RCT。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 感受性黴菌引起之局部感染 |
| 預測新適應症 | 外陰陰道炎 (Vulvovaginitis) |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張（有效單方 2／有效複方 0／已註銷 4） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依據同類藥物的已知知識，Tioconazole 屬咪唑類抗黴菌藥，
可抑制黴菌的羊毛固醇 14-α 去甲基酶（CYP51 / ERG11），使細胞膜必需成分麥角固醇無法生成，病原體因而無法存活。
另有藥理資料顯示，它也會抑制人類的 CYP8B1（參與膽汁酸合成的分支途徑）。

外陰陰道炎最常見的病因之一是念珠菌感染（外陰陰道念珠菌症）。
原適應症是黴菌（含酵母菌）的局部感染，與念珠菌性外陰陰道炎的病原重疊，因此機轉上高度相關。
文獻中也有以 Tioconazole 陰道給藥治療陰道念珠菌症的臨床研究。

需要注意：現有證據針對的是**念珠菌性**的外陰陰道炎，並非所有類型的外陰陰道炎（如細菌性或萎縮性）。
此外，台灣核准的劑型為乳膏與粉劑，文獻中使用的陰道專用製劑（如 2% 陰道乳霜、6.5% 軟膏）在台灣並非現有劑型，給藥途徑的相容性尚待確認。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | 80 位患者，單劑 6.5% Tioconazole 與 3 日 Clotrimazole 陰道錠比較；治療後 4 週無症狀比例 84% vs 85%，療效相當 |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT | Gynakol Rundsch | 雙盲比較 Tioconazole 與安慰劑用於陰道念珠菌症，並評估全身吸收 |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | 回顧 Tioconazole 的抗菌活性與淺表黴菌症治療；臨床試驗顯示局部製劑對皮膚黴菌/酵母菌感染及陰道念珠菌症有效且安全 |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | 探討外陰陰道念珠菌症的非侵入性唑類抗黴菌新選項 |
| [34550113](https://pubmed.ncbi.nlm.nih.gov/34550113/) | 2021 | Review | Med Lett Drugs Ther | Ibrexafungerp 用於外陰陰道念珠菌症（背景資料，非 Tioconazole 本身） |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | 臨床研究 | Acta Obstet Gynecol Scand | 29 位有症狀婦女使用 2% 陰道乳霜，黴菌學治癒率 88.5% |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | 隨機（開放） | J Int Med Res | 40 位患者，單劑局部 Tioconazole 6% 與 5 日口服 Ketoconazole 比較；5 週後兩組皆有效，局部組症狀緩解較快 |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | 開放性單組 | J Int Med Res | 20 位陰道滴蟲或混合感染患者，2% 陰道乳霜 3 日，首次追蹤治癒率 95% |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Cohort | Gynakol Rundsch | 開放比較 Tioconazole 與 Econazole 3 日療程治療陰道念珠菌症 |
| [10990271](https://pubmed.ncbi.nlm.nih.gov/10990271/) | 2000 | 實驗室研究 | Microb Drug Resist | 念珠菌臨床分離株對非處方唑類藥物存在交叉抗藥性，提示抗藥性風險 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tioconazole 的不重複許可證共 **6 張**：有效單方 2 張、有效複方 0 張、已註銷 4 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第043149號 | "意欣"可寧乳膏１％ | 乳膏劑 | 意欣國際有限公司 | 2029/08/06 | 感受性黴菌引起之局部感染。 |
| 衛署藥製字第047752號 | "黃氏" 蒂可那乳膏 | 乳膏劑 | 黃氏製藥股份有限公司 | 2031/01/13 | 感受性黴菌引起之局部感染。 |

<details><summary><strong>已註銷</strong>（4 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第027631號</td><td>妥舒乳膏１％（治可那唑）</td><td>TIOCONAZOLE</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第046418號</td><td>"十全" 汰黴乳膏</td><td>TIOCONAZOLE</td><td>2011/02/22</td></tr><tr><td>衛署藥輸字第012674號</td><td>妥喜得粉劑</td><td>TIOCONAZOLE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第024484號</td><td>治可那唑</td><td>TIOCONAZOLE</td><td>2022/06/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫收錄 2 筆。其中 Omeprazole 的交互作用等級為未知；另有藥理資料顯示 Tioconazole 可抑制人類 CYP8B1（參與膽汁酸合成）。外用給藥的臨床意義尚待確認。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 篇 RCT（含與 Clotrimazole 的比較，療效相當）及多篇開放性研究支持 Tioconazole 用於念珠菌性外陰陰道炎，機轉也合理；但無登記的臨床試驗，且文獻多為 1980 年代的研究，證據屬間接且較老舊。
- 此預測僅適用於念珠菌性病因；排名第 2 的「外陰炎」證據更間接（等級 L3），排名第 3 的「停經後萎縮性陰道炎」主要由雌激素缺乏所致，與抗黴菌機轉無關，僅有模型預測，建議 Hold。

**若要推進需要：**
- 確認台灣現有乳膏劑型是否適合陰道或外陰黏膜使用，必要時評估陰道專用劑型與劑量
- 補充詳細的作用機轉資料（MOA）與完整的仿單安全性資訊（警語、禁忌）
- 以現行標準治療（如 Clotrimazole、Fluconazole）為對照，設計較新的臨床試驗
- 評估念珠菌的唑類抗藥性與非白色念珠菌的覆蓋範圍
- 限定適應症為念珠菌性外陰陰道炎，並建立療效與黏膜刺激的監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市情形表把已註銷的妥舒乳膏列為有效許可證 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「有效許可證（妥舒乳膏等）」 | 報告重生後已無此錯誤（2026-10-15：新報告未再把已註銷的「妥舒乳膏」列為有效許可證；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

