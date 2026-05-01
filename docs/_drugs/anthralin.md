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

Anthralin（二羥蒽酮）是一種外用皮膚科藥物，在台灣長期用於牛皮癬及相關皮膚病治療，擁有 9 張有效許可證。
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
| 許可證數 | 9 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 DrugBank 尚未提供 Anthralin 的正式作用機轉資料。根據現有研究文獻，Anthralin 透過**誘導活性氧（ROS）並抑制粒線體氧化磷酸化**，下調 IL-1、IL-6、TNF-α 等促炎細胞因子，進而抑制局部免疫炎症反應。在牛皮癬治療中，這種機轉能有效緩解角質細胞異常增殖與 T 細胞驅動的皮膚炎症。

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

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥輸字第005432號 | 蒽酚（粉） | 粉劑 | 牛皮癬 |
| 衛署藥製字第011402號 | 嗎爾宜唐 | 軟膏劑 | 緩解皮膚刺激及尿布疹、去角質 |
| 衛署藥製字第022694號 | 嗎爾宜唐軟膏 0.1% | 軟膏劑 | 緩解皮膚刺激及尿布疹、去角質 |
| 衛署藥輸字第017338號 | 蒽酚（粉） | 粉劑 | 牛皮癬 |
| 衛署藥製字第014923號 | 速利癬軟膏 | 軟膏劑 | 頑癬、牛皮癬、及其他癬菌所致之皮膚病症 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Anthralin 用於圓禿的機轉合理性有充分理論依據（T 細胞免疫調節），自 1985 年起已有直接臨床應用文獻，並擁有多篇回顧性研究與系統性回顧，以及動物模型直接實驗證據，英國皮膚科醫學會 2024 年最新指引亦將其列為治療選項；加上台灣已有 9 張有效許可證、藥品可近性高，整體屬 L3 等級的觀察性研究支持，具備推進條件。

**若要推進需要：**
- 補充 DrugBank 正式作用機轉（MOA）資料，強化機轉關聯性論述
- 針對 Anthralin 治療圓禿設計前瞻性隨機對照試驗（目前僅有回顧性研究與病例系列）
- 釐清有效劑量與濃度範圍（現有文獻顯示需足夠刺激強度才有療效）
- 建立台灣族群的安全性監測計畫，特別是皮膚刺激性與長期使用安全性
- 評估是否需向衛福部申請圓禿適應症擴充
---

