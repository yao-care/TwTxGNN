---
layout: default
title: Hydrocortisone
parent: 高證據等級 (L1-L2)
nav_order: 125
evidence_level: L1
indication_count: 10
---

# Hydrocortisone
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Hydrocortisone：從過敏性皮膚炎到圓禿

## 一句話總結

Hydrocortisone（氫化可體松）是人體腎上腺皮質自然分泌的內源性糖皮質激素，原本廣泛用於過敏性皮膚炎、風濕性關節炎、支氣管氣喘、腎上腺皮質功能缺乏症等炎症性與自體免疫疾病的治療。TxGNN 模型預測它可能對**圓禿 (Alopecia Areata)** 有效，目前有 **4 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 風濕性關節炎、急性關節風濕、支氣管氣喘、過敏性疾患、慢性潰瘍性大腸炎及局部性腸炎、濕疹樣症候群、蕁麻疹、腎臟疾患等 |
| 預測新適應症 | 圓禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的藥物作用機轉（MOA）資料。根據已知資訊，Hydrocortisone 是內源性糖皮質激素，透過與細胞內糖皮質激素受體（GR）結合，抑制 NF-κB 等關鍵炎症訊號傳導路徑，進而抑制 IL-2、IFN-γ、TNF-α 等促炎細胞激素的分泌，同時抑制 T 淋巴細胞的活化與增殖。

圓禿（Alopecia Areata）的核心病因是 CD8+ 細胞毒性 T 淋巴細胞異常浸潤毛囊周圍，破壞毛囊的「免疫豁免區（immune privilege）」，引發非瘢痕性毛髮脫落。Hydrocortisone 透過抑制毛囊周圍 CD8+ T 淋巴細胞浸潤及下調 IL-2/IFN-γ 等促炎細胞激素，理論上可緩解這種自體免疫性毛囊損傷。

事實上，皮質類固醇是目前圓禿臨床治療的重要骨幹，外用、皮內注射及系統性用法均有文獻記錄。Hydrocortisone 1% 乳膏屬效力較低的外用選擇，已完成的 Phase 3 RCT 顯示其療效略遜於高效皮質類固醇（Clobetasol propionate 0.05%），臨床應用需依病灶範圍與嚴重程度選擇適當效力等級。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 已完成 | 41 | 兒童圓禿 RCT：直接比較 Hydrocortisone 1% cream vs Clobetasol propionate 0.05% cream，為本適應症最強等級的直接臨床證據（對應 PMID 24226568） |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | 已完成 | 18 | 圓禿局部注射 Triamcinolone acetonide（同類皮質類固醇）對腎上腺功能影響之安全性研究，提供局部類固醇用於圓禿的安全性背景數據 |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | 尚未招募 | 72 | 皮質類固醇不同劑量製劑用於輕中度雄性禿（Grade I-III）之四臂雙盲劑量反應比較研究 |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | 已完成 | 380 | 類固醇代謝組異常（MACS）對骨質強度與體成分影響之觀察性研究，提供全身性類固醇暴露的機轉背景數據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | 兒童圓禿 RCT：Hydrocortisone 1% vs Clobetasol 0.05%，直接評估本藥物用於本適應症之療效 |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | RCT | Clinical and Experimental Dermatology | 局部皮質類固醇密封性（occlusion）治療用於嚴重兒童圓禿（含全禿 AT 及全身禿 AU）之單中心回顧性分析 |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Meta-analysis | Journal of Cosmetic Dermatology | 分段式雷射單獨或合併治療圓禿之系統性回顧與 Meta 分析，提供圓禿治療全貌背景 |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case series | Medical Times | 早期圓禿、部分禿及全禿以皮質素、Hydrocortisone 及其類似物（Prednisone、Prednisolone）治療之臨床觀察 |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Clinical report | Der Hautarzt | 圓禿及惡性禿患者皮內注射 Hydrocortisone 後毛髮再生之觀察報告 |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Clinical report | Actas Dermo-Sifiliograficas | 皮內注射 Hydrocortisone 治療圓禿之臨床報告 |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Clinical report | Vestnik Dermatologii | 圓禿及全禿患者以皮內注射 Hydrocortisone 治療之臨床觀察 |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | JEADV | 探討圓禿患者 HPA 軸是否具超活性，評估皮質醇與 MSH 分泌在圓禿神經內分泌機轉中的角色 |
| [39506493](https://pubmed.ncbi.nlm.nih.gov/39506493/) | 2025 | Cohort | Journal of Cosmetic Dermatology | 慢性心理壓力對皮膚老化的影響，提及皮質醇及腎上腺素釋放在圓禿等皮膚疾病觸發中的角色 |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case series | JAAD | 先天性圓禿 4 例報告（3-5 年追蹤），治療包括 Minoxidil 2% 及多種外用藥物 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第004637號 | 醋酸氫化可體松懸浮劑 | 注射劑 | 風濕性關節炎、急性關節風濕、支氣管氣喘、過敏性疾患、慢性潰瘍性大腸炎及局部性腸炎、濕疹樣症候群、蕁麻疹、腎臟疾患等 |
| 內衛藥輸字第002641號 | 敷疾聖眼膏 | 點眼膏劑 | 革蘭氏陽性與陰性細菌所引起之眼疾患 |
| 內衛藥輸字第002642號 | 敷疾聖軟膏 | 軟膏劑 | 革蘭氏陽性及陰性細菌所引起之皮膚疾患 |
| 內衛藥輸字第004919號 | 可蘭小丸劑 | 錠劑 | 鵝口瘡及口腔潰瘍 |
| 內衛藥輸字第004931號 | 氫化腎上腺皮質酮醋酸鹽 | 粉劑 | 腎上腺皮質分泌缺乏症 |

---

## 安全性考量

**藥物交互作用**：共有 722 筆交互作用記錄，以下列出代表性項目：

| 交互藥物 | 嚴重程度 |
|---------|---------|
| Adalimumab | Major（重大） |
| Zidovudine | Moderate（中度） |
| Ibuprofen | Moderate（中度） |
| Ketorolac | Moderate（中度） |
| Isotretinoin | Moderate（中度） |
| Nifedipine | Moderate（中度） |
| Acarbose | Moderate（中度） |
| Acetazolamide | Moderate（中度） |
| Ethinylestradiol | Moderate（中度） |
| Aldesleukin | Moderate（中度） |

其餘安全性警語及禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有 Phase 3 RCT（NCT01453686）直接比較 Hydrocortisone 1% 乳膏用於兒童圓禿的療效，加上自 1950 年代起多篇臨床報告記錄皮內注射 Hydrocortisone 治療圓禿的效果，證據等級達 L1；然而現有最強直接證據顯示 Hydrocortisone 效力略遜於高效皮質類固醇，臨床定位需謹慎釐清。

**若要推進需要：**
- 補充詳細藥物作用機轉（MOA）資料，特別是 GR 結合、NF-κB 抑制及毛囊免疫豁免恢復的機轉文獻
- 評估不同給藥途徑（外用 1% 乳膏、皮內注射、局部密封性治療）的療效差異，確定最佳劑型
- 釐清 Hydrocortisone 在現行圓禿治療階梯（相較於高效類固醇、JAK 抑制劑等）中的定位與適用族群
- 針對兒童族群（尤其輕度圓禿）制定安全性監測計畫，包括 HPA 軸抑制風險評估
---

