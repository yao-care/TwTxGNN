---
layout: default
title: Acetazolamide
description: "Acetazolamide 的老藥新用潛力分析。高證據等級 L2，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 高證據等級 (L1-L2)
nav_order: 12
evidence_level: L2
indication_count: 10
---

# Acetazolamide

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L2</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acetazolamide：從青光眼利尿到心肌病變探索

## 一句話總結

<p class="key-answer" data-question="Acetazolamide 可以用於治療什麼新適應症？">
Acetazolamide 原本用於青光眼及利尿。
TxGNN 模型預測它可能對**心肌病變 (cardiomyopathy)** 及**肥厚性心肌病變 (hypertrophic cardiomyopathy)** 有效，
目前有 **3 個臨床試驗**和 **11 篇文獻**支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 青光眼、癲癇、充血性心衰竭水腫 |
| 預測新適應症 | exercise-induced malignant hyperthermia、hypertrophic cardiomyopathy、congenital myopathy with excess of thin filaments、hypertrophic cardiomyopathy due to intensive athletic training、distal myopathy, Tateyama type、cirrhotic cardiomyopathy、心肌病變、intestinal obstruction、glycogen storage disease due to acid maltase deficiency, late-onset、myopathic intestinal pseudoobstruction |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L2 |
| 台灣上市 | 已上市 |
| 許可證數 | 22 張（部分已註銷） |
| 建議決策 | Proceed with Guardrails |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. exercise-induced malignant hyperthermia</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.95%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

Acetazolamide 是碳酸酐酶抑制劑，傳統上用於青光眼和利尿。近年研究發現其在急性失代償性心衰竭中的應用價值顯著提升。

ADVOR 試驗 (2022) 顯示，acetazolamide 加上 loop diuretics 可顯著改善急性心衰竭患者的去鬱血效果。其機轉包括：
1. 抑制近端腎小管碳酸酐酶，增加鈉離子排泄
2. 克服利尿劑抵抗
3. 調節電解質平衡（特別是氯離子）

對於心肌病變患者，常伴隨心衰竭症狀，acetazolamide 作為輔助利尿劑的角色已獲臨床驗證。此外，2018 年日本個案報告顯示，acetazolamide 可用於治療肥厚性心肌病變合併低氯血症患者。

### 臨床試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | RECRUITING | 400 | 評估 acetazolamide 口服在失代償性心衰竭（包括心肌病變）中的療效 |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | RECRUITING | 939 | 比較 loop diuretics 合併 Metolazone 或 Acetazolamide 在急性心衰竭容量過負荷的效果 |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | RECRUITING | 466 | TAILOR-AHF：尿鈉導向的利尿劑演算法研究 |

### 相關文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41696050](https://pubmed.ncbi.nlm.nih.gov/41696050/) | 2026 | Case Report | Int J Heart Fail | 利尿劑抵抗性晚期心衰竭使用 acetazolamide 成功作為移植前橋接治療 |
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC heart failure | 2024 心衰竭更新：肯定 acetazolamide 加 loop diuretics 的聯合療法 |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Journal Article | Eur Heart J Cardiovasc Pharmacother | 2022 年心血管藥理進展回顧，acetazolamide 聯合 loop diuretics 被納入標準治療 |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | J Cardiol Cases | 肥厚性心肌病變合併低氯血症，使用 acetazolamide 成功矯正電解質 |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Journal Article | Acta Neurol Scand | 低鉀週期性麻痺與心肌病變之關聯研究 |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Report | Acta Neurol Scand | 家族性低鉀週期性麻痺中發現心肌疾病證據 |

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. hypertrophic cardiomyopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.93%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.93%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. congenital myopathy with excess of thin filaments</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.90%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.90%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. hypertrophic cardiomyopathy due to intensive athletic training</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.89%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. distal myopathy, Tateyama type</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.88%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.88%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. cirrhotic cardiomyopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.88%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.88%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. cardiomyopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.83%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.83%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. intestinal obstruction</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.82%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.82%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. glycogen storage disease due to acid maltase deficiency, late-onset</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.80%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.80%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. unclassified intestinal pseudoobstruction</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.79%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.79%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>


## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第007548號 | "人人" 乙醯偶氮胺錠 | 錠劑 | 青光眼及水腫、癲癇輔助治療 |
| 衛部藥輸字第027543號 | 乙醯偶氮胺 | 粉劑 | 碳酸酐酶抑制藥 |
| 衛署藥製字第023932號 | "新喜" 壓作錠 | 錠劑 | 青光眼、充血性心不全之水腫 |
| 衛署藥製字第007819號 | 安賜他明錠 | 錠劑 | 青光眼及水腫、癲癇輔助治療 |

## 安全性考量

### 重要藥物交互作用

**Major 交互作用：**
- Aspirin（高劑量）：增加 acetazolamide 毒性風險，可能引起代謝性酸中毒

**Moderate 交互作用：**
- 降血糖藥物（各類口服降糖藥、胰島素）：可能影響血糖控制
- Amphotericin B：增加低鉀血症風險
- 類固醇（Betamethasone、Budesonide 等）：增加低鉀血症風險
- Bisacodyl：電解質失衡風險
- Digoxin：低鉀可能增加毛地黃毒性
- Lithium：可能增加鋰毒性
- Metformin：可能增加乳酸酸中毒風險
- Carbamazepine、Phenytoin：可能影響抗癲癇藥血中濃度
- Topiramate：增加代謝性酸中毒和腎結石風險

### 禁忌症
- 磺胺類藥物過敏
- 嚴重肝功能不全
- 低鈉血症或低鉀血症
- 代謝性酸中毒
- 艾迪森氏症

安全性資訊請參考原廠仿單。


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**Acidosis, Respiratory** 🟡 Moderate
- Carbonic anhydrase inhibitors may exacerbate pulmonary disease in patients with elevated pCO2 levels.  Respiratory acidosis may be precipitated or increased in these patients.  Therapy with carbonic anhydrase inhibitors should be administered cautiou...

**腎臟疾病 (Kidney Diseases)** 🟡 Moderate
- The major route of elimination of carbonic anhydrase inhibitors is through the kidney.  These drugs should be administered cautiously in patients with reduced renal function and a dose adjustment might be required depending on the level of impairment...

**糖尿病 (Diabetes Mellitus)** 🟡 Moderate
- Elevation of blood glucose, possibly caused by hypokalemia, and glycosuria have been reported rarely in diabetics receiving carbonic anhydrase inhibitors.  Therapy with carbonic anhydrase inhibitors should be administered cautiously in patients with ...

**Gout** 🟡 Moderate
- Uric acid excretion is decreased during therapy with carbonic anhydrase inhibitors, and gout may be exacerbated.  Therapy with carbonic anhydrase inhibitors should be administered cautiously in patients with gout.  Elevated serum uric acid levels ret...

**Acidosis** 🟡 Moderate
- Reduced plasma bicarbonate levels and, in some instances, elevated plasma chloride levels may result in metabolic acidosis during long-term therapy with carbonic anhydrase inhibitors.  Therapy with carbonic anhydrase inhibitors should be administered...

*另有 7 項疾病注意事項，詳見 [DDInter 2.0](https://ddinter2.scbdd.com/)*

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Acetazolamide 在急性失代償性心衰竭的輔助利尿角色已有高品質 RCT 證據支持（ADVOR 試驗），且目前有多個第四期臨床試驗正在進行中。對於心肌病變合併心衰竭的患者，acetazolamide 可作為克服利尿劑抵抗的有效選擇。

**若要推進需要：**
- 密切監測電解質（特別是鉀、鈉、氯、碳酸氫根）
- 避免與高劑量 aspirin 併用
- 監測腎功能及酸鹼平衡
- 評估是否有磺胺類過敏史


---

## 相關藥物報告

- [Hydroxyprogesterone Caproate]({{ "/drugs/hydroxyprogesterone_caproate/" | relative_url }}) - 證據等級 L2
- [Omalizumab]({{ "/drugs/omalizumab/" | relative_url }}) - 證據等級 L2
- [Regorafenib]({{ "/drugs/regorafenib/" | relative_url }}) - 證據等級 L2
- [Gemcitabine]({{ "/drugs/gemcitabine/" | relative_url }}) - 證據等級 L2
- [Isosorbide Dinitrate]({{ "/drugs/isosorbide_dinitrate/" | relative_url }}) - 證據等級 L2

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Acetazolamide老藥新用驗證報告. https://twtxgnn.yao.care/drugs/acetazolamide/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_acetazolamide,
  title = {Acetazolamide老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/acetazolamide/}
}
```

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-21 | 審核者：TwTxGNN Research Team</small>
</div>

{% include giscus.html %}
