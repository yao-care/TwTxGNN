---
layout: default
title: Desogestrel
parent: 中證據等級 (L3-L4)
nav_order: 79
evidence_level: L3
indication_count: 10
---

# Desogestrel
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

# Desogestrel：從避孕到閉經 (Amenorrhea)

## 一句話總結

Desogestrel 是第三代合成孕激素，原本作為口服避孕藥使用，在台灣已有 9 張許可證上市。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，
目前有 **2 個臨床試驗**和 **16 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 避孕 |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Desogestrel 是第三代合成孕激素，其活性代謝物為 etonogestrel，屬於高選擇性孕激素受體（PR）激動劑，雄激素效應相較第二代孕激素顯著偏低。

避孕與閉經在病理生理上密切相關：兩者都涉及下視丘-腦垂體-卵巢（HPO）軸的荷爾蒙調控。功能性閉經（如運動誘發性閉經或低體重相關閉經）的核心問題在於黃體素缺乏與 HPO 軸功能抑制。Desogestrel 作為外源性黃體素，理論上可補充此類患者的黃體素不足；與炔雌醇合用時可恢復規律性月經週期，並改善相關荷爾蒙失衡。

此外，Desogestrel 與炔雌醇的複方製劑在多囊卵巢症候群（PCOS，常伴隨月經稀發或閉經）患者中，已展現出降低雄激素、改善排卵的臨床效益，進一步支持 TxGNN 預測的機轉合理性。值得注意的是，desogestrel 75μg 純黃體素錠（POP）本身也被記錄到可誘發閉經——這同時是其作用機轉的體現，也是評估治療性應用時需謹慎區分方向的關鍵。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | 完成 | 121 | 研究年輕女性運動員的脂肪介導生殖內分泌功能，探討下視丘性閉經（HOA）族群中經皮或口服雌激素對骨密度與骨微結構的影響 |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | 未知 | 42 | 比較含 desogestrel 口服避孕藥與陰道避孕環在 PCOS 婦女中對雄激素、胰島素代謝及發炎指標的長期（59 週）影響 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | RCT | Br J Obstet Gynaecol | 比較含 150μg desogestrel 搭配 20μg 或 30μg EE 的避孕藥週期控制與副作用，確認不同雌激素劑量對出血型態的影響 |
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Meta-analysis | Cochrane Database Syst Rev | 20μg vs >20μg EE 複方 OC 的避孕效果與出血型態系統性回顧，閉經為重要次要終點 |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Meta-analysis | Cochrane Database Syst Rev | 2011 年更新版系統性回顧，確認低劑量 EE 複方 OC 的有效性與週期控制品質 |
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Cohort | Gynecol Endocrinol | 比較 drospirenone 4mg 與 desogestrel 75μg POP 在心血管風險婦女中的出血型態，記錄 desogestrel 相關閉經發生率 |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Cohort | Acta Obstet Gynecol Scand Suppl | 評估 desogestrel 單藥及與 EE 合用的藥效學，對照 PCO 伴隨閉經族群的雄激素參數變化 |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Cohort | Am J Obstet Gynecol | Desogestrel/EE 複方的耐受性全面評估，涵蓋月經週期改善、痛經及子宮內膜異位症等非避孕效益 |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Cohort | J Reprod Med | 評估下視丘性少經/閉經年輕女性使用不同劑量 EE 口服避孕藥後的骨礦物質密度變化 |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Cohort | Georgian Med News | 159 名中樞性少經/閉經不孕婦女的病因分析，比較針對性荷爾蒙治療與常規療法的療效 |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Review | Br Med Bull | 複方口服避孕藥的安全性與有效使用：基於世代研究與病例對照研究的臨床管理綜述 |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Review | Obstet Gynecol Surv | 新一代孕激素（desogestrel、norgestimate、gestodene）的藥理特性、避孕效果與代謝安全性比較綜述 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第027194號 | 美偌琳膜衣錠 | 膜衣錠 | 避孕。 |
| 衛部藥製字第058638號 | 蜜止妊錠 | 錠劑 | 避孕。 |
| 衛部藥輸字第028613號 | 母扶樂膜衣錠 | 膜衣錠 | 口服避孕劑。 |
| 衛署藥輸字第016025號 | 母扶樂錠 | 錠劑 | 口服避孕劑 |
| 衛署藥輸字第025503號 | 愛逸定膜衣錠 | 膜衣錠 | 避妊。 |

---

## 安全性考量

**藥物交互作用**：共有 43 筆交互作用紀錄（來源：DDInter），主要集中於 Moderate 等級，以抗糖尿病藥物類別為主：

| 交互藥物類別 | 代表藥物 | 等級 |
|-------------|---------|------|
| GLP-1 受體激動劑 | Albiglutide、Liraglutide、Lixisenatide | Moderate |
| DPP-4 抑制劑 | Alogliptin、Linagliptin | Moderate |
| SGLT2 抑制劑 | Dapagliflozin、Ertugliflozin | Moderate |
| 胰島素製劑 | Insulin aspart、Insulin detemir、Insulin degludec、Insulin glulisine 等 | Moderate |
| 雙胍類 | Metformin | Moderate |
| 其他降糖藥 | Nateglinide、Rosiglitazone | Moderate |
| 止吐藥（CYP 誘導相關） | Aprepitant | Moderate |

> 上述交互作用均為 Moderate 等級，臨床使用時建議監測血糖控制情況。其餘警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Desogestrel 的孕激素機轉與閉經的病理生理具有合理的荷爾蒙軸關聯，尤其在功能性閉經（下視丘性、運動誘發性）的應用場景下，有觀察性研究與系統性回顧的間接支持（L3 等級）；台灣現有 9 張口服劑型許可證，取得與製劑成熟度佳。

**若要推進需要：**
- 查詢 DrugBank（DB00304）補充詳細 MOA 資料，釐清 etonogestrel 的 HPO 軸調控機制
- 區分治療方向：功能性閉經（補充黃體素）vs. 排卵抑制誘發閉經（副作用），需明確界定目標族群
- 設計針對功能性閉經或下視丘性閉經的前瞻性 RCT，建立直接臨床療效證據
- 評估 desogestrel 單藥 POP（75μg）vs 複方 EE/DSG 在不同閉經亞型的適用性差異
- 建立特定高風險族群（青少年、運動員、低體重婦女）的安全性監測計畫
---

