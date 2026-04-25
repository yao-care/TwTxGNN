---
layout: default
title: Alpha-Tocopherol Succinate
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
---

# Alpha-Tocopherol Succinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Alpha-Tocopherol Succinate：從維他命Ｅ缺乏症到藥物誘發性骨質疏鬆症

## 一句話總結

Alpha-Tocopherol Succinate（維他命Ｅ琥珀酸鹽）是維他命 E 的生物活性酯化形式，台灣核准用於維他命 E 缺乏症、習慣性流產及末梢血行障礙。
TxGNN 模型預測它對**藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)** 可能有效，
惟目前**尚無臨床試驗及文獻**直接支持，屬純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維他命Ｅ缺乏症 |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 alpha-Tocopherol Succinate 詳細的作用機轉資料。根據已知資訊，alpha-tocopherol 是維他命 E 家族中最具生物活性的脂溶性抗氧化劑，其琥珀酸酯形式（succinate）在體內水解後釋出活性 alpha-tocopherol 發揮療效，在維他命 E 缺乏症及末梢血行障礙治療中的效益已獲臨床使用支持。

藥物誘發性骨質疏鬆症（如類固醇、化療藥物所致）的發病機轉中，氧化壓力是重要環節之一：過量活性氧（ROS）可促進破骨細胞活化、抑制成骨細胞功能，進而導致骨密度下降。Alpha-tocopherol 作為強效脂溶性自由基清除劑，理論上可中斷此氧化損傷路徑，緩解骨質流失速率。

然而，目前僅有 TxGNN 模型預測支持此方向，缺乏任何臨床試驗或前臨床研究的直接佐證，機轉合理性有待進一步實驗驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥輸字第012326號 | 維他命Ｅ琥珀酸粉劑 | 粉劑 | 維他命Ｅ缺乏症 |
| 衛署藥輸字第009164號 | 維他命Ｅ琥珀酸鹽 | 粉劑 | 習慣性流產、末梢血行障礙、維他命Ｅ缺乏症 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 所有預測適應症總覽

本次評估屬多適應症候選（TW-DB14001-multi），共涵蓋 10 個 TxGNN 預測方向：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 文獻數 | 建議決策 |
|------|----------|-----------|---------|--------|--------|
| 1 | 藥物誘發性骨質疏鬆症 | 99.997% | L5 | 0 | Hold |
| 2 | 糖尿病性白內障 | 99.992% | L4 | 11 | Hold |
| **3** | **膀胱腫瘤** | **99.991%** | **L3** | **20** | **Research Question** |
| 4 | 強直性白內障 | 99.991% | L5 | 0 | Hold |
| 5 | 不成熟白內障 | 99.991% | L4 | 1 | Hold |
| 6 | 成熟白內障 | 99.991% | L5 | 0 | Hold |
| 7 | 第 2 型糖尿病相關白內障 | 99.991% | L5 | 0 | Hold |
| 8 | 顱縫早閉相關白內障 | 99.991% | L5 | 0 | Hold |
| **9** | **皮質性白內障** | **99.990%** | **L3** | **9** | **Research Question** |
| 10 | 核性老年性白內障 | 99.990% | L4 | 1 | Hold |

**最具研究潛力的兩個方向**：

**膀胱腫瘤（化學預防）**：L3 證據，含 1 篇大型 RCT（ATBC 研究次要終點分析）及 1 篇 Meta-analysis，並有多項前瞻性世代研究，是本次評估中文獻最豐富、證據層次最高的方向。

**皮質性白內障**：L3 證據，含 2 篇 RCT（ATBC 研究、Linxian 介入試驗）及動物劑量反應研究，有直接的人體介入試驗支持，機轉亦最為明確。

---

## 膀胱腫瘤方向補充文獻（最高優先）

由於膀胱腫瘤（Rank 3）具備最高等級的現有文獻，以下列出主要參考文獻供決策參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [11142528](https://pubmed.ncbi.nlm.nih.gov/11142528/) | 2000 | RCT | Cancer Causes & Control | ATBC 大型 RCT 次要終點：alpha-tocopherol 補充對尿路癌症發生率與死亡率的影響分析 |
| [25905583](https://pubmed.ncbi.nlm.nih.gov/25905583/) | 2015 | Meta-analysis | Scientific Reports | 劑量反應 Meta-analysis：維他命 C、D、E 與膀胱癌風險；每增加 10 mg/天 Vit E，相對風險 0.96（90%CI 0.90-1.02） |
| [2790827](https://pubmed.ncbi.nlm.nih.gov/2790827/) | 1989 | Cohort | Cancer Research | 血清 alpha-tocopherol 與後續膀胱癌發展的前瞻性研究，25,802 人追蹤 12 年 |
| [18478342](https://pubmed.ncbi.nlm.nih.gov/18478342/) | 2008 | Case-control | Cancer Causes & Control | 血漿維他命 E（alpha-tocopherol 與 gamma-tocopherol）與膀胱癌風險的病例對照分析 |
| [12434284](https://pubmed.ncbi.nlm.nih.gov/12434284/) | 2002 | Cohort | British Journal of Cancer | ATBC 世代研究：蔬果攝取、類胡蘿蔔素及維他命與膀胱癌風險，追蹤 27,111 名男性吸菸者 |
| [1877596](https://pubmed.ncbi.nlm.nih.gov/1877596/) | 1991 | Nested Case-control | Am J Epidemiology | 芬蘭大型巢式病例對照研究：血清 alpha-tocopherol 與多種低發生率癌症風險 |
| [3567886](https://pubmed.ncbi.nlm.nih.gov/3567886/) | 1987 | Animal | Cancer Letters | 大鼠膀胱致癌模型：alpha-tocopherol 對 BBN 誘發之膀胱癌的修飾效應 |

---

## 皮質性白內障方向補充文獻（次高優先）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [9527321](https://pubmed.ncbi.nlm.nih.gov/9527321/) | 1997 | RCT | Acta Ophthalmologica | ATBC 長期補充試驗：alpha-tocopherol 或 beta-carotene 補充與白內障盛行率及嚴重度 |
| [8363468](https://pubmed.ncbi.nlm.nih.gov/8363468/) | 1993 | RCT | Arch Ophthalmology | Linxian 介入試驗：維他命/礦物質補充對老年性白內障風險的影響（兩項干預試驗） |
| [8512984](https://pubmed.ncbi.nlm.nih.gov/8512984/) | 1993 | Cohort | Epidemiology | Baltimore 老化縱貫研究：血漿抗氧化劑（包含 alpha-tocopherol）與皮質性及核性白內障風險 |
| [7843899](https://pubmed.ncbi.nlm.nih.gov/7843899/) | 1995 | Cohort | Invest Ophthalmol Vis Sci | 血清類胡蘿蔔素與 tocopherol 濃度與核性及皮質性混濁嚴重度的相關性 |
| [21620831](https://pubmed.ncbi.nlm.nih.gov/21620831/) | 2011 | Animal | Exp Eye Research | 大鼠 UV 誘發白內障模型：alpha-tocopherol 保護效果的劑量反應關係 |

---

## 結論與下一步

**決策（主要預測，Rank 1）：Hold**

**理由：**
TxGNN 對藥物誘發性骨質疏鬆症的預測分數雖達 99.997%，但完全缺乏臨床試驗及文獻支持，證據等級僅 L5。在本次評估的 10 個預測適應症中，**膀胱腫瘤（化學預防）**及**皮質性白內障**具備 L3 證據，更值得優先投入研究資源。

**若要推進藥物誘發性骨質疏鬆症方向，需要：**
- 取得完整作用機轉資料（查詢 DrugBank API，DrugBank ID: DB14001）
- 進行系統性文獻回顧，確認 alpha-tocopherol 與骨代謝的間接機轉證據
- 執行前臨床動物實驗（如類固醇誘發骨鬆模型）驗證保護效果

**建議優先評估的替代方向：**
- **膀胱腫瘤（化學預防）**：Rank 3，L3 證據，含 RCT + Meta-analysis，可直接規劃「Alpha-Tocopherol 膀胱癌化學預防」系統性回顧
- **皮質性白內障**：Rank 9，L3 證據，含 2 篇 RCT 及動物劑量反應研究，機轉明確，可評估口服 Vit E 補充延緩白內障進程的臨床研究可行性

---

