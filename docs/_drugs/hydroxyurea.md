---
layout: default
title: Hydroxyurea
description: "Hydroxyurea 的老藥新用潛力分析。高證據等級 L2，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 高證據等級 (L1-L2)
nav_order: 83
evidence_level: L2
indication_count: 10
---

# Hydroxyurea

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L2</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Hydroxyurea：從血液腫瘤到女性乳腺癌

## 一句話總結

<p class="key-answer" data-question="Hydroxyurea 可以用於治療什麼新適應症？">
Hydroxyurea 原本用於治療慢性骨髓性白血病、骨髓纖維化及真性紅血球增多症。
TxGNN 模型預測它可能對**女性乳腺癌 (female breast carcinoma)** 有效，
目前有 **超過 20 篇文獻**支持這個研究方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性骨髓性白血病、骨髓纖維化、真性紅血球增多症、卵巢癌、頭頸癌 |
| 預測新適應症 | 女性乳腺癌、primary non-gestational choriocarcinoma of ovary、sickle cell-hemoglobin E disease syndrome、sickle cell-hemoglobin c disease syndrome、hereditary persistence of fetal hemoglobin-sickle cell disease syndrome、sickle cell-hemoglobin d disease syndrome、sickle cell-beta-thalassemia disease syndrome、hereditary breast ovarian cancer syndrome、ovarian mucinous adenocarcinoma、ovarian clear cell adenocarcinoma |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 台灣上市 | 有效許可證 |
| 許可證數 | 多張 |
| 建議決策 | Proceed with Guardrails |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. female breast carcinoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.97%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

### 為什麼這個預測合理？

Hydroxyurea 是一種核糖核苷酸還原酶抑制劑，透過阻斷 DNA 合成發揮抗腫瘤作用。
它可以抑制細胞從 G1 期進入 S 期，並增加細胞對放射線的敏感性。

**預測合理性分析：**
- Hydroxyurea 已核准用於多種實體腫瘤（卵巢癌、頭頸癌）
- 在乳癌的高劑量化療方案中已有使用經驗
- 可作為放射增敏劑，與放射治療合併使用
- 研究顯示可與其他藥物（如 valproic acid）產生協同作用

**機轉支持：**
- 抑制 DNA 合成和修復
- 誘導複製壓力，增加 DNA 雙股斷裂
- 與 valproic acid 合併可抑制同源重組修復（PMID: 28837865）
- 脂質藥物複合體可提高細胞攝取率（PMID: 38211596）

### 臨床試驗

文獻中報告的臨床經驗包括：

| 研究類型 | 年份 | 期刊 | 主要發現 |
|---------|------|------|---------|
| Phase I | 1991 | Am J Clin Oncol | FU-LV-HU 組合方案在晚期乳癌中的 Phase I 試驗 |
| Phase I/II | 1994 | Bone Marrow Transplant | 高劑量 CY-Thiotepa-HU 配合自體幹細胞移植用於轉移性乳癌 |
| Phase I | 1992 | Cancer Chemother Pharmacol | 5-FU、LV、HU 與 cisplatin 合併放療的臨床藥理學研究 |

### 相關文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | 電腦模擬 | Drug Res | HU 脂質藥物複合體設計，靶向 PI3K/AKT/mTOR 通路 |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | 體外研究 | DNA Repair | Valproic acid 增敏乳癌細胞對 HU 的反應 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | 體外研究 | DNA Repair | 2-hexyl-4-pentynoic acid 與 HU 聯合抑制乳癌 |
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Phase I/II | Bone Marrow Transplant | 高劑量 CY-Thiotepa-HU 用於轉移性乳癌的鞏固治療 |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | 體外研究 | Br J Cancer | ATR 抑制劑與 HU 在乳癌和卵巢癌細胞中的效果 |

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. sickle cell-hemoglobin E disease syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.67%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. sickle cell-hemoglobin c disease syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.67%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. hereditary persistence of fetal hemoglobin-sickle cell disease syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.67%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. sickle cell-hemoglobin d disease syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.67%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. sickle cell-beta-thalassemia disease syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.67%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. cervical adenosarcoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.40%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.40%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. colon mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.32%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.32%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. rectum mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.31%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.31%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. gallbladder mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.28%</span>
</summary>
<div class="indication-content">

### TxGNN 預測資訊

- **預測分數**：99.28%
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
| - | 捷可衛錠 | 錠劑 | 骨髓纖維化、真性紅血球增多症、GvHD |
| - | Hydroxyurea 膠囊 | 膠囊 | 慢性骨髓性白血病、卵巢癌、頭頸癌 |

## 安全性考量

- **藥物交互作用**：文獻中多與其他化療藥物合併使用
- **注意事項**：
  - 骨髓抑制是最主要的劑量限制毒性
  - 長期使用可能增加繼發性白血病風險
  - 皮膚毒性（色素沉著、潰瘍）
  - 巨球性貧血
- **乳癌適用考量**：
  - 目前多用於高劑量化療方案
  - 需考量與現有標準治療的比較

安全性資訊請參考原廠仿單。


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**Nervous System Diseases** 🔴 Major
- Neurological symptoms such as disorientation or hallucinations have been reported very rarely during hydroxyurea therapy.  Therapy with hydroxyurea should be administered cautiously to patients with or predisposed to neurological disorders.

**肝臟疾病 (Liver Diseases)** 🟡 Moderate
- There are no data supporting specific guidance for hydroxyurea dosage adjustment in patients with hepatic impairment.  Caution and close monitoring is advised in these patients.

**癲癇 (Epilepsy)** 🟡 Moderate
- Seizures have been noted very rarely during hydroxyurea therapy.  Therapy with hydroxyurea should be administered cautiously in patients with seizure disorders.

**Bone Marrow Failure Disorders** 🟢 Minor
- The use of hydroxyurea is contraindicated in patients with marked myelosuppression.  Hydroxyurea induces myelosuppression, primarily leukopenia.  Thrombocytopenia and anemia occur less frequently.  Patients should be instructed to immediately report ...

**腎臟疾病 (Kidney Diseases)** 🟢 Minor
- Hydroxyurea is primarily eliminated by the kidney.  Approximately 80% of urea is excreted in the urine as unchanged drug or urea.  Patients with marked renal impairment (CrCl < 60 mL/min or ESRD) may be at increased risk of toxicity associated with a...

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 豐富的體外研究支持 HU 在乳癌中的活性
- 已有 Phase I/II 臨床經驗，尤其在高劑量化療方案中
- 新穎的藥物傳遞系統（如脂質複合體）可能改善療效
- 與其他藥物的協同作用提供聯合治療機會

**若要推進需要：**
- 評估 HU 在現代乳癌治療中的角色（與 CDK4/6 抑制劑、免疫治療的比較或聯合）
- 開發更有效的藥物傳遞系統以提高腫瘤靶向性
- 確定最適合的乳癌亞型（如三陰性乳癌）
- 設計與 valproic acid 或其他增敏劑的聯合用藥方案


---

## 相關藥物報告

- [Acetazolamide]({{ "/drugs/acetazolamide/" | relative_url }}) - 證據等級 L2
- [Vonoprazan]({{ "/drugs/vonoprazan/" | relative_url }}) - 證據等級 L2
- [Omalizumab]({{ "/drugs/omalizumab/" | relative_url }}) - 證據等級 L2
- [Gemcitabine]({{ "/drugs/gemcitabine/" | relative_url }}) - 證據等級 L2
- [Prednisone]({{ "/drugs/prednisone/" | relative_url }}) - 證據等級 L2

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Hydroxyurea老藥新用驗證報告. https://twtxgnn.yao.care/drugs/hydroxyurea/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_hydroxyurea,
  title = {Hydroxyurea老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/hydroxyurea/}
}
```

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-20 | 審核者：TwTxGNN Research Team</small>
</div>

{% include giscus.html %}
