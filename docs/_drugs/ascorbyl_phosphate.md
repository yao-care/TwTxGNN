---
layout: default
title: Ascorbyl Phosphate
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 1
---

# Ascorbyl Phosphate
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

# Ascorbyl Phosphate：從眼部刺激緩解到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Ascorbyl Phosphate（磷酸抗壞血酸）是維生素 C 的穩定磷酸酯衍生物，目前台灣核准適應症為點眼液劑，用於**暫時緩解輕微眼部刺激引起的不適、眼紅、眼疲勞及眼癢**。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，但目前**無任何臨床試驗或文獻**直接支持此方向，預測依據純屬機轉推論。
次優預測**痤瘡 (Acne)** 具有 **1 篇 RCT** 和 **2 篇體外研究**支持，臨床潛力相對較高。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛疲勞、眼睛癢 |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ascorbyl Phosphate 是維生素 C 的穩定前驅物，可在體內轉化為具活性的抗壞血酸，發揮強效抗氧化及自由基清除作用，並作為膠原蛋白合成（prolyl/lysyl hydroxylase）的必要輔因子。

嚴重非增殖性糖尿病視網膜病變的病理進程與長期高血糖誘發的**氧化應激**密切相關——活性氧（ROS）累積導致視網膜微血管內皮細胞損傷、周細胞凋亡及毛細血管基底膜增厚。Ascorbyl Phosphate 的抗氧化活性理論上可中和 ROS，從而減緩微血管氧化損傷。

更重要的是，此藥現有台灣核准適應症已為**眼部局部給藥**（點眼液劑），提示藥物具備基本的眼組織穿透性，給藥路徑具可行性。然而，點眼給藥能否達到視網膜層的有效藥物濃度仍是關鍵未知數，且目前完全缺乏任何臨床前動物模型或臨床文獻支持此特定適應症，預測仍停留在機轉推論層次。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對嚴重非增殖性糖尿病視網膜病變，目前無相關文獻。

**附：次優預測適應症「痤瘡 (Acne)」之文獻佐證（TxGNN 分數 99.57%，證據等級 L2）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [20367669](https://pubmed.ncbi.nlm.nih.gov/20367669/) | 2010 | RCT | Journal of Cosmetic Dermatology | Sodium L-ascorbyl-2-phosphate 5% 乳液治療尋常性痤瘡的隨機雙盲對照試驗，顯示其有效性並優於安慰劑 |
| [25894228](https://pubmed.ncbi.nlm.nih.gov/25894228/) | 2015 | In vitro | Archives of Dermatological Research | L-Ascorbyl-2-phosphate 可抑制皮脂腺細胞（SZ95）中的 NF-κB 信號通路，具潛在抗炎機轉 |
| [23055762](https://pubmed.ncbi.nlm.nih.gov/23055762/) | 2012 | In vitro | Clinical, Cosmetic and Investigational Dermatology | 鋅抗壞血酸鹽具超氧化物歧化酶樣活性及對金黃色葡萄球菌、大腸桿菌的體外抗菌活性 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥輸字第023600號 | 德佑視立明眼藥水 | 點眼液劑 | 暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛疲勞、眼睛癢。 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
首要預測適應症（嚴重非增殖性糖尿病視網膜病變）目前完全缺乏臨床試驗及文獻支持，僅憑機轉推論與 TxGNN 模型預測（L5），尚不足以推進任何開發行動。次優預測**痤瘡**（L2，有 RCT 支持）臨床潛力更高，建議優先評估。

**若要推進需要：**
- 查詢 DrugBank API，補充 Ascorbyl Phosphate 完整作用機轉（MOA）資料
- 設計臨床前動物模型，驗證點眼局部給藥是否能達到視網膜層有效藥物濃度
- 搜尋廣義維生素 C 衍生物（ascorbic acid、ascorbate）用於糖尿病視網膜病變的相關文獻，評估類別效應（class effect）可能性
- 若轉向**痤瘡**適應症推進（建議），可直接規劃 Phase 2 隨機對照試驗，利用現有 RCT 作為先導依據

---

