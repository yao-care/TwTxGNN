---
layout: default
title: Hydroxyurea
description: "Hydroxyurea 的老藥新用潛力分析。高證據等級 L2，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 高證據等級 (L1-L2)
nav_order: 83
evidence_level: L1
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
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.97%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Hydroxyurea 是一種核糖核苷酸還原酶抑制劑，透過阻斷 DNA 合成發揮抗腫瘤作用。</p>
<p>它可以抑制細胞從 G1 期進入 S 期，並增加細胞對放射線的敏感性。</p>

<p><strong>預測合理性分析：</strong></p>
<ul>
<li>Hydroxyurea 已核准用於多種實體腫瘤（卵巢癌、頭頸癌）</li>
<li>在乳癌的高劑量化療方案中已有使用經驗</li>
<li>可作為放射增敏劑，與放射治療合併使用</li>
<li>研究顯示可與其他藥物（如 valproic acid）產生協同作用</li>

</ul>
<p><strong>機轉支持：</strong></p>
<ul>
<li>抑制 DNA 合成和修復</li>
<li>誘導複製壓力，增加 DNA 雙股斷裂</li>
<li>與 valproic acid 合併可抑制同源重組修復（PMID: 28837865）</li>
<li>脂質藥物複合體可提高細胞攝取率（PMID: 38211596）</li>
</ul>

<h3>臨床試驗</h3>

<p>文獻中報告的臨床經驗包括：</p>

<table>
<thead>
<tr>
<th>研究類型</th>
<th>年份</th>
<th>期刊</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>Phase I</td>
<td>1991</td>
<td>Am J Clin Oncol</td>
<td>FU-LV-HU 組合方案在晚期乳癌中的 Phase I 試驗</td>
</tr>
<tr>
<td>Phase I/II</td>
<td>1994</td>
<td>Bone Marrow Transplant</td>
<td>高劑量 CY-Thiotepa-HU 配合自體幹細胞移植用於轉移性乳癌</td>
</tr>
<tr>
<td>Phase I</td>
<td>1992</td>
<td>Cancer Chemother Pharmacol</td>
<td>5-FU、LV、HU 與 cisplatin 合併放療的臨床藥理學研究</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<table>
<thead>
<tr>
<th>PMID</th>
<th>年份</th>
<th>類型</th>
<th>期刊</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/38211596/">38211596</a></td>
<td>2024</td>
<td>電腦模擬</td>
<td>Drug Res</td>
<td>HU 脂質藥物複合體設計，靶向 PI3K/AKT/mTOR 通路</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/28837865/">28837865</a></td>
<td>2017</td>
<td>體外研究</td>
<td>DNA Repair</td>
<td>Valproic acid 增敏乳癌細胞對 HU 的反應</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/32795962/">32795962</a></td>
<td>2020</td>
<td>體外研究</td>
<td>DNA Repair</td>
<td>2-hexyl-4-pentynoic acid 與 HU 聯合抑制乳癌</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/7914447/">7914447</a></td>
<td>1994</td>
<td>Phase I/II</td>
<td>Bone Marrow Transplant</td>
<td>高劑量 CY-Thiotepa-HU 用於轉移性乳癌的鞏固治療</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/21730979/">21730979</a></td>
<td>2011</td>
<td>體外研究</td>
<td>Br J Cancer</td>
<td>ATR 抑制劑與 HU 在乳癌和卵巢癌細胞中的效果</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. sickle cell-hemoglobin E disease syndrome</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（4 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03763656" target="_blank">NCT03763656</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>33</td><td>A Prospective Open Label, Pharmacokinetic Study of an Oral Hydroxyurea Solution ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03264989" target="_blank">NCT03264989</a></td><td>PHASE2</td><td>COMPLETED</td><td>57</td><td>A Phase 2, Multicenter, Open-Label Study to Assess PK/PD of SEG101 (Crizanlizuma...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02709681" target="_blank">NCT02709681</a></td><td>N/A</td><td>COMPLETED</td><td>628</td><td>Hydroxyurea in Sickle Cell Disease: a Large Nation-wide Cohort Study From Italy</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04927247" target="_blank">NCT04927247</a></td><td>PHASE3</td><td>TERMINATED</td><td>72</td><td>A Randomized, Double-blind, Placebo-controlled, Multicenter Study of a Single Do...</td></tr>
</tbody>
</table>

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36799926/" target="_blank">36799926</a></td><td>2023</td><td>Article</td><td>Blood advances</td><td>Most adults with severe HbSC disease are not treated with hy...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. sickle cell-hemoglobin c disease syndrome</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（11 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03975894" target="_blank">NCT03975894</a></td><td>PHASE2</td><td>UNKNOWN</td><td>50</td><td>A Feasibility Trial of Serial Prophylactic Exchange Blood Transfusion in Pregnan...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01987908" target="_blank">NCT01987908</a></td><td>PHASE2</td><td>TERMINATED</td><td>35</td><td>A Phase 2, Exploratory, Placebo-Controlled, Multicenter, Double-Blind Evaluation...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02640573" target="_blank">NCT02640573</a></td><td>PHASE2</td><td>TERMINATED</td><td>1</td><td>Treatment of Adult Patients With Hemoglobin SC Disease</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03474965" target="_blank">NCT03474965</a></td><td>PHASE2</td><td>COMPLETED</td><td>117</td><td>A Phase 2,Multicenter,Open-Label Study to Assess Appropriate Dosing and to Evalu...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05850156" target="_blank">NCT05850156</a></td><td>N/A</td><td>NOT_YET_RECRUITING</td><td>130</td><td>Study of a Deformability Parameter of Red Blood Cell. FITRED</td></tr>
</tbody>
</table>
<p><em>...及其他 6 項試驗</em></p>

<h3>相關文獻（19 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36047926/" target="_blank">36047926</a></td><td>2022</td><td>Article</td><td>The Cochrane databas</td><td>Hydroxyurea (hydroxycarbamide) for sickle cell disease.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39647172/" target="_blank">39647172</a></td><td>2025</td><td>Article</td><td>NEJM evidence</td><td>Hydroxyurea for Children and Adults with Hemoglobin SC Disea...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28426137/" target="_blank">28426137</a></td><td>2017</td><td>Article</td><td>The Cochrane databas</td><td>Hydroxyurea (hydroxycarbamide) for sickle cell disease.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33679049/" target="_blank">33679049</a></td><td>2021</td><td>Article</td><td>Journal of clinical </td><td>Sickle Hepatopathy.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11406036/" target="_blank">11406036</a></td><td>2001</td><td>Article</td><td>The Cochrane databas</td><td>Hydroxyurea for sickle cell disease.</td></tr>
</tbody>
</table>
<p><em>...及其他 14 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. hereditary persistence of fetal hemoglobin-sickle cell disease syndrome</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/23342821/" target="_blank">23342821</a></td><td>2012</td><td>Article</td><td>Journal of the Natio</td><td>Kikuchi-Fugimoto&#x27;s disease in sickle cell disease: report of...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. sickle cell-hemoglobin d disease syndrome</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（4 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04046705" target="_blank">NCT04046705</a></td><td>PHASE3</td><td>UNKNOWN</td><td>78</td><td>A Prospective Multicenter Trial Comparing Allogeneic Matched Related Haematopoie...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06464458" target="_blank">NCT06464458</a></td><td>NA</td><td>RECRUITING</td><td>30</td><td>Optimizing the Management of Sickle Cell Patients on Hydroxyurea: The Value of T...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03763656" target="_blank">NCT03763656</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>33</td><td>A Prospective Open Label, Pharmacokinetic Study of an Oral Hydroxyurea Solution ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06979492" target="_blank">NCT06979492</a></td><td>PHASE4</td><td>NOT_YET_RECRUITING</td><td>50</td><td>Prophylactic Transfusion In Pregnant in Women With Sickle Cell Disease</td></tr>
</tbody>
</table>

<h3>相關文獻（2 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36799926/" target="_blank">36799926</a></td><td>2023</td><td>Article</td><td>Blood advances</td><td>Most adults with severe HbSC disease are not treated with hy...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20502357/" target="_blank">20502357</a></td><td>2010</td><td>Article</td><td>Journal of pediatric</td><td>First report of successful stem cell transplantation in a pa...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. sickle cell-beta-thalassemia disease syndrome</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.67%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（4 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01962415" target="_blank">NCT01962415</a></td><td>PHASE2</td><td>RECRUITING</td><td>100</td><td>A Phase II Study of Reduced Intensity Conditioning in Pediatric Patients and You...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04528355" target="_blank">NCT04528355</a></td><td>N/A</td><td>RECRUITING</td><td>50</td><td>A Prospective Outcomes Study of Pediatric and Adult Patients With Non-Malignant ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03653338" target="_blank">NCT03653338</a></td><td>PHASE1, PHASE2</td><td>RECRUITING</td><td>5</td><td>T-Cell Depleted, Alternative Donor Transplant in Pediatric and Adult Patients Wi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03763656" target="_blank">NCT03763656</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>33</td><td>A Prospective Open Label, Pharmacokinetic Study of an Oral Hydroxyurea Solution ...</td></tr>
</tbody>
</table>

<h3>相關文獻（2 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27053181/" target="_blank">27053181</a></td><td>2016</td><td>Article</td><td>Indian journal of pe</td><td>Sickle Cell Disease in Central India: A Potentially Severe S...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10326220/" target="_blank">10326220</a></td><td>1999</td><td>Article</td><td>Pediatric hematology</td><td>Effect of hydroxyurea in sickle cell anemia: a clinical tria...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. cervical adenosarcoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.40%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
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

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
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

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
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

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
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

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Nervous System Diseases** 🔴 Major
- 注意事項：Neurological symptoms such as disorientation or hallucinations have been reported very rarely during hydroxyurea therapy...

**肝臟疾病** 🟡 Moderate
- 應謹慎使用本藥物。需定期監測。可能需要調整劑量。

**癲癇** 🟡 Moderate
- 風險包括：癲癇發作。

**Bone Marrow Failure Disorders** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。風險包括：骨髓抑制、出血、感染、血栓、貧血。可能有嚴重不良反應。

**腎臟疾病** 🟢 Minor
- 注意事項：Hydroxyurea is primarily eliminated by the kidney...

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
