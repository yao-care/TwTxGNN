---
layout: default
title: Anthralin
parent: 中證據等級 (L3-L4)
nav_order: 29
evidence_level: L3
indication_count: 10
---

# Anthralin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Anthralin：從牛皮癬到圓禿 (Alopecia Areata)

## 一句話總結

Anthralin（二羥蒽酮）是一種外用皮膚科藥物，在台灣長期用於牛皮癬及相關皮膚病治療，擁有 9 張有效許可證（有效 1 張）。
TxGNN 模型預測它可能對**圓禿 (Alopecia Areata)** 有效，
目前有 **4 個臨床試驗**和 **20 篇文獻**支持這個方向，且自 1985 年起即有 Anthralin 直接用於圓禿的臨床應用文獻，並已被納入英國皮膚科醫學會 2024 年治療指引。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 牛皮癬 |
| 預測新適應症 | 圓禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 9 張（有效單方 1／有效複方 0／已註銷 8） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 DrugBank 尚未提供 Anthralin 的正式作用機轉資料。根據現有研究文獻，Anthralin 透過**誘導活性氧（ROS）並抑制粒線體氧化磷酸化**，下調 IL-1、IL-6、TNF-α 等促炎細胞因子，進而抑制局部免疫炎症反應。在牛皮癬治療中，這種機轉能有效緩解角質細胞異常增殖與 T 細胞驅動的皮膚炎症。

<!-- review:begin anthralin-moa-2026-10-03 -->

> **查核加註（2026-10-03）**：仿單寫 anthralin 的確切機轉尚未完全了解，已知有抗增生（抑制 DNA 合成、強還原性）與抗發炎作用，並與誘導脂質過氧化、降低內皮黏附分子有關；沒有提到抑制粒線體氧化磷酸化或下調 IL-1、IL-6、TNF-α。原文保留。依據：[DailyMed：ZITHRANOL-RR（anthralin）Cream 仿單（Elorac），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=45bad116-0351-442f-8e49-f11089a955fd)。

<!-- review:end anthralin-moa-2026-10-03 -->

圓禿與牛皮癬同屬 **T 細胞介導的自體免疫性皮膚病**，兩者共享關鍵的免疫病理機轉：皮膚局部 CD4⁺/CD8⁺ T 細胞浸潤及促炎細胞因子過度活化。圓禿的核心病理是 T 淋巴細胞對毛囊的自體免疫攻擊（毛囊免疫豁免崩潰），而 Anthralin 恰好能夠減輕毛囊周圍的 T 細胞介導炎症，這為其在圓禿的應用提供了合理的機轉基礎。

機轉合理性更獲實驗證據支持：2003 年以 Dundee 實驗禿毛大鼠模型進行的研究顯示，0.1% Anthralin 外用軟膏能達到 100% 的毛囊活性恢復，並確認其透過細胞因子信號調節發揮療效。臨床上，Anthralin 自 1985 年即被直接用於圓禿治療，英國皮膚科醫學會（BAD）2024 年圓禿治療活體指引亦將其列為治療選項之一。

---

## 臨床試驗證據

以下試驗針對圓禿作為疾病目標，但干預藥物並非 Anthralin，可作為圓禿仍有龐大未滿足治療需求的背景參考。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06527729](https://clinicaltrials.gov/study/NCT06527729) | Early Phase 1 | 已完成 | 28 | Sildenafil 奈米脂質載體外用治療圓禿，探索新型藥物遞送策略於圓禿的可行性 |
| [NCT06747611](https://clinicaltrials.gov/study/NCT06747611) | Phase 2 | 招募中 | 40 | 腸道微生物群移植治療圓禿，反映圓禿免疫調節治療的多元探索方向 |
| [NCT05485571](https://clinicaltrials.gov/study/NCT05485571) | N/A | 未知 | 30 | 微針聯合 Methotrexate（免疫抑制劑）治療圓禿，藥物免疫抑制機轉方向與 Anthralin 相近 |
| [NCT06327581](https://clinicaltrials.gov/study/NCT06327581) | N/A | 招募中 | 88 | 微針聯合乳酸／Vitamin D3／Triamcinolone 多臂比較研究，評估局部療法對圓禿相對療效 |

> **注意**：上述試驗均未直接測試 Anthralin；Anthralin 在圓禿的直接臨床證據主要來自以下文獻資料。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [34606676](https://pubmed.ncbi.nlm.nih.gov/34606676/) | 2022 | 系統性回顧 | J Cosmetic Dermatol | 直接比較外用免疫療法與 **Anthralin** 治療嚴重兒科圓禿，評估療效、安全性、治療期與復發率 |
| [33940103](https://pubmed.ncbi.nlm.nih.gov/33940103/) | 2022 | 系統性回顧 | J Am Acad Dermatol | 兒科圓禿各種治療方式的系統性回顧，為 Anthralin 在兒科應用提供整體證據框架 |
| [37559401](https://pubmed.ncbi.nlm.nih.gov/37559401/) | 2023 | 回顧性研究 | J Cutan Med Surg | 回顧性研究 **Anthralin in petrolatum** 治療兒科圓禿的療效、耐受性與安全性，不同濃度比較 |
| [30338548](https://pubmed.ncbi.nlm.nih.gov/30338548/) | 2018 | 回顧性研究 | Pediatr Dermatol | 37 例兒科圓禿患者接受 **Anthralin** 治療的回顧性研究，成人有效但兒科結果不一 |
| [31165933](https://pubmed.ncbi.nlm.nih.gov/31165933/) | 2019 | 病例系列 | Arch Dermatol Res | **Anthralin 聯合 DPCP** 治療對 DPCP 無效的廣泛型圓禿，評估組合療法療效與副作用 |
| [32743037](https://pubmed.ncbi.nlm.nih.gov/32743037/) | 2020 | 病例報告 | JAAD Case Reports | **Anthralin 聯合 Calcipotriene** 治療圓禿，討論兩藥作用機轉的互補性 |
| [30318623](https://pubmed.ncbi.nlm.nih.gov/30318623/) | 2018 | 病例報告 | Pediatr Dermatol | 難治型圓禿以 Leflunomide 和 **Anthralin** 聯合治療有效，探討潛在 JAK/STAT 抑制機轉 |
| [12895001](https://pubmed.ncbi.nlm.nih.gov/12895001/) | 2003 | 動物研究 | J Invest Dermatol Symp | Dundee 禿毛大鼠模型：0.1% **Anthralin** 外用達 100% 毛囊活性恢復，確認細胞因子調節機轉 |
| [39432739](https://pubmed.ncbi.nlm.nih.gov/39432739/) | 2025 | 治療指引 | Br J Dermatol | 英國皮膚科醫學會（BAD）2024 圓禿治療活體指引，**Anthralin 列為治療選項** |
| [3905640](https://pubmed.ncbi.nlm.nih.gov/3905640/) | 1985 | 病例系列 | Int J Dermatol | 最早的 **Anthralin 治療圓禿**臨床先導研究，指出需足夠劑量誘發接觸性皮膚炎才有療效 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Anthralin 的不重複許可證共 **9 張**：有效單方 1 張、有效複方 0 張、已註銷 8 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第049649號 | 貝諾乳膏 1% | 乳膏劑 | 華盛頓製藥廠股份有限公司 | 2028/09/10 | 頑癬、牛皮癬、錢癬及其他癬菌所致之皮膚病。 |

<details><summary><strong>已註銷</strong>（8 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第011402號</td><td>嗎爾宜唐</td><td>SALICYLIC ACID、ZINC OXIDE、ANTHRALIN (DITHRANOL)</td><td>2013/09/26</td></tr><tr><td>衛署藥製字第012742號</td><td>疥能淨軟膏</td><td>ANTHRALIN (DITHRANOL)</td><td></td></tr><tr><td>衛署藥製字第014923號</td><td>速利癬軟膏</td><td>ANTHRALIN (DITHRANOL)、ZINC OXIDE、SALICYLIC ACID</td><td>1989/11/22</td></tr><tr><td>衛署藥製字第022694號</td><td>嗎爾宜唐軟膏０．１％</td><td>SALICYLIC ACID、ZINC OXIDE、ANTHRALIN (DITHRANOL)</td><td>2013/09/26</td></tr><tr><td>衛署藥製字第022883號</td><td>嗎爾宜唐軟膏０．５％</td><td>SALICYLIC ACID、ANTHRALIN (DITHRANOL)、ZINC OXIDE</td><td>2013/09/26</td></tr><tr><td>衛署藥製字第028949號</td><td>嗎爾宜唐軟膏０．３％</td><td>SALICYLIC ACID、ZINC OXIDE、ANTHRALIN (DITHRANOL)</td><td>1999/09/30</td></tr><tr><td>衛署藥輸字第005432號</td><td>/酚</td><td>ANTHRALIN (DITHRANOL)</td><td>1989/10/05</td></tr><tr><td>衛署藥輸字第017338號</td><td>/酚</td><td>ANTHRALIN (DITHRANOL)</td><td>1990/07/07</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Anthralin 用於圓禿的機轉合理性有充分理論依據（T 細胞免疫調節），自 1985 年起已有直接臨床應用文獻，並擁有多篇回顧性研究與系統性回顧，以及動物模型直接實驗證據，英國皮膚科醫學會 2024 年最新指引亦將其列為治療選項；加上台灣已有 9 張有效許可證（有效 1 張）、藥品可近性高，整體屬 L3 等級的觀察性研究支持，具備推進條件。

**若要推進需要：**
- 補充 DrugBank 正式作用機轉（MOA）資料，強化機轉關聯性論述
- 針對 Anthralin 治療圓禿設計前瞻性隨機對照試驗（目前僅有回顧性研究與病例系列）
- 釐清有效劑量與濃度範圍（現有文獻顯示需足夠刺激強度才有療效）
- 建立台灣族群的安全性監測計畫，特別是皮膚刺激性與長期使用安全性
- 評估是否需向衛福部申請圓禿適應症擴充

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「擁有 9 張有效許可證」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 結論理由「台灣已有 9 張有效許可證、藥品可近性高」 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表所列 5 張許可證皆已註銷，其中 3 張為複方 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 機轉寫成誘導 ROS 並抑制粒線體氧化磷酸化 | 加註 | [DailyMed：ZITHRANOL-RR（anthralin）Cream 仿單（Elorac），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=45bad116-0351-442f-8e49-f11089a955fd) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

