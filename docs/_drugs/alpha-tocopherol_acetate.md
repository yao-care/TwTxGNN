---
layout: default
title: Alpha-Tocopherol Acetate
parent: 高證據等級 (L1-L2)
nav_order: 18
evidence_level: L2
indication_count: 1
---

# Alpha-Tocopherol Acetate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **1** 個
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

# Alpha-Tocopherol Acetate（維生素E醋酸鹽）：從維他命E缺乏症到糖尿病視網膜病變

## 一句話總結

Alpha-tocopherol acetate（維生素E醋酸酯）是廣泛核准用於治療維他命E缺乏症的脂溶性維生素補充劑，在台灣已有 20 張許可證。TxGNN 模型預測它可能對**糖尿病視網膜病變 (Diabetic Retinopathy)** 有效，目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向，是 10 項預測適應症中證據最充分、最具行動潛力的候選。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維他命Ｅ缺乏症 |
| 預測新適應症 | 糖尿病視網膜病變 (Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Alpha-tocopherol acetate 在體內水解為活性的 alpha-tocopherol，其核心藥理是作為**脂溶性自由基清除劑**，可嵌入細胞膜磷脂雙層，阻斷脂質過氧化連鎖反應。此外，alpha-tocopherol 已有實驗證據顯示能抑制**蛋白激酶C（PKC）β 亞型**的過度活化——這一機轉對糖尿病視網膜病變具有關鍵意義。

糖尿病視網膜病變的核心致病路徑正是高血糖誘導的 **PKC β 活化**與**氧化壓力累積**，造成視網膜血管通透性上升、白血球黏附（leukostasis）增加及血流動力學異常，最終導致微血管閉塞與新生血管增生。Alpha-tocopherol 能從兩個節點同時介入：一是直接清除 ROS，二是透過 PKC β 抑制正常化視網膜血流，與病理機轉的契合度高。

從原適應症到新適應症的橋接也相當直觀：維他命E缺乏症本身即已知會引發視網膜功能異常，而多項世代研究也顯示糖尿病患者的血漿 alpha-tocopherol 水平系統性偏低。換言之，補充 alpha-tocopherol 在這類患者族群中既有機轉依據，也有流行病學支持。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04071977](https://clinicaltrials.gov/study/NCT04071977) | Phase 2 | 完成 | 40 | 評估複合抗氧化療法（含 alpha-tocopherol）對增生性糖尿病視網膜病變患者玻璃體切除術前後房水與玻璃體氧化壓力標記的影響，2 個月介入 |
| [NCT03702374](https://clinicaltrials.gov/study/NCT03702374) | Phase 3 | 完成 | 132 | 評估長期複合抗氧化療法對中度、重度及增生性糖尿病視網膜病變患者氧化壓力與粒線體功能障礙標記的影響，12 個月口服介入，設有安慰劑對照組 |

> **注意**：兩項試驗均採用**複合抗氧化療法**（含 alpha-tocopherol），無法單獨分離 alpha-tocopherol 的貢獻。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19900709](https://pubmed.ncbi.nlm.nih.gov/19900709/) | 2010 | Meta-analysis | Ophthalmology | 系統性回顧維生素C、E及鎂與糖尿病視網膜病變的關聯，評估微量營養素介入的臨床潛力 |
| [12882944](https://pubmed.ncbi.nlm.nih.gov/12882944/) | 2003 | Cohort | Am J Epidemiology | NHANES III 大型世代（n=998），分析血清 alpha-tocopherol 對第二型糖尿病患者視網膜病變盛行率的影響 |
| [8407170](https://pubmed.ncbi.nlm.nih.gov/8407170/) | 1993 | Cohort | Int J Vitam Nutr Res | 第一型糖尿病患者血漿 alpha-tocopherol 低下與視網膜病變及腎病等微血管併發症顯著相關 |
| [9609359](https://pubmed.ncbi.nlm.nih.gov/9609359/) | 1998 | Clinical | Diabetic Medicine | Alpha-tocopherol nicotinate 治療 3 個月後，第二型糖尿病視網膜病變患者血液黏度與紅血球膜脂質過氧化壓力顯著改善 |
| [9523029](https://pubmed.ncbi.nlm.nih.gov/9523029/) | 1998 | Animal | BioFactors | d-alpha-tocopherol 可透過抑制視網膜 PKC 活性，正常化鏈脲佐菌素（STZ）誘發糖尿病大鼠的異常視網膜血流動力學 |
| [11473058](https://pubmed.ncbi.nlm.nih.gov/11473058/) | 2001 | Animal | Diabetes | 長期維生素C+E 複合抗氧化療法可顯著抑制糖尿病與半乳糖血症大鼠的視網膜病變進展 |
| [14703729](https://pubmed.ncbi.nlm.nih.gov/14703729/) | 2003 | Animal | Free Radical Research | 含 alpha-tocopherol 的多重抗氧化劑可抑制糖尿病大鼠視網膜 NF-κB 氧化還原敏感轉錄因子的異常活化 |
| [35715832](https://pubmed.ncbi.nlm.nih.gov/35715832/) | 2022 | Animal | Int J Retina Vitreous | Retinol 與 α-tocopherol 聯合使用可預防高血糖誘發的視網膜光感受器與視網膜神經節細胞凋亡 |
| [22695936](https://pubmed.ncbi.nlm.nih.gov/22695936/) | 2012 | Clinical | Graefe's Archive | 抗氧化劑補充可減緩急性強化胰島素治療引起的糖尿病視網膜病變暫時性惡化，涉及 ROS 抑制機轉 |
| [13148290](https://pubmed.ncbi.nlm.nih.gov/13148290/) | 1954 | Case series | Am J Ophthalmology | 最早期病例系列報告 alpha-tocopherol 直接用於治療糖尿病視網膜病變的臨床嘗試 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥輸字第002603號 | 左右旋性－甲類－戊種維生素醋酸鹽 | 原料藥溶液劑 | 維他命Ｅ缺乏症 |
| 衛署藥製字第025667號 | 惠力糖衣錠50公絲 | 糖衣錠 | 維他命Ｅ缺乏症 |
| 衛署藥製字第026490號 | 必達益糖衣錠100公絲 | 糖衣錠 | 習慣性流產、末梢血行障礙、維他命Ｅ缺乏症 |
| 衛署藥製字第022376號 | 益壽膠囊 | 膠囊劑 | 習慣性流產、末梢血行障礙、維他命Ｅ缺乏症 |
| 衛署藥輸字第002895號 | 乙醯維他命Ｅ | 原料藥浸膏劑 | 維他命Ｅ缺乏症 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
兩項已完成的 Phase 2/3 RCT 及一篇 Meta-analysis（Ophthalmology 2010）支持含 alpha-tocopherol 抗氧化療法對糖尿病視網膜病變的保護效果，PKC β 抑制與氧化壓力清除的機轉明確且與病理高度契合，且藥物在台灣已有 20 張許可證廣泛上市，安全性基礎良好。

**若要推進需要：**
- Alpha-tocopherol **單藥**（而非複合療法）用於糖尿病視網膜病變的獨立設計 RCT，以釐清個別藥物貢獻
- 確認最佳劑量（oral 補充劑量 vs. 高劑量介入）與給藥途徑（口服 vs. 眼部局部）
- 補充完整的作用機轉資料（MOA，建議透過 DrugBank API 查詢 DB14003 補充）
- 台灣糖尿病患者族群的安全性監測計畫（含長期 Vit E 補充的出血風險評估）
- 考量與現行第一線糖尿病視網膜病變治療（抗 VEGF、雷射）的聯合或輔助定位

---

