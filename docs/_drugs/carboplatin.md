---
layout: default
title: Carboplatin
description: "Carboplatin 的老藥新用潛力分析。高證據等級 L2，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 高證據等級 (L1-L2)
nav_order: 40
evidence_level: L1
indication_count: 10
---

# Carboplatin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L2</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Carboplatin：從化療基石到女性乳腺癌的新探索

## 一句話總結

<p class="key-answer" data-question="Carboplatin 可以用於治療什麼新適應症？">
Carboplatin 是鉑類抗癌藥物，已廣泛用於多種癌症治療。
TxGNN 模型預測它可能對**女性乳腺癌 (female breast carcinoma)** 有效，
目前有超過 **50 個臨床試驗**支持這個方向。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性早期乳癌、轉移性乳癌、黑色素瘤、非小細胞肺癌、何杰金氏淋巴瘤、頭頸部鱗狀細胞癌、泌尿道上皮癌等 |
| 預測新適應症 | 女性乳腺癌、primary non-gestational choriocarcinoma of ovary、hereditary breast ovarian cancer syndrome、ovarian clear cell adenocarcinoma、ovarian mucinous adenocarcinoma、yolk sac tumor、maligant granulosa cell tumor of ovary、ovarian endometrioid adenocarcinoma、rectum mucinous adenocarcinoma、colon mucinous adenocarcinoma |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2 |
| 台灣上市 | 已上市（為多種複方治療的一部分） |
| 許可證數 | 多張（作為 Trastuzumab、Pembrolizumab 等藥物適應症的併用藥物） |
| 建議決策 | Proceed with Guardrails |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. female breast carcinoma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.86%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Carboplatin 是一種鉑類抗癌藥物，透過與 DNA 形成交叉連結來抑制腫瘤細胞增殖。其作用機轉包括：</p>

<ol>
<li><strong>DNA 損傷機制</strong>：Carboplatin 與 DNA 形成鉑-DNA 加合物，干擾 DNA 複製與轉錄</li>
<li><strong>細胞週期阻滯</strong>：誘導細胞週期停滯，促進腫瘤細胞凋亡</li>
<li><strong>對三陰性乳腺癌的特殊療效</strong>：研究顯示 carboplatin 對 BRCA 突變相關的三陰性乳腺癌具有良好療效</li>
</ol>

<h3>臨床試驗</h3>

<table>
<thead>
<tr>
<th>試驗編號</th>
<th>階段</th>
<th>狀態</th>
<th>人數</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT06027268">NCT06027268</a></td>
<td>Phase 2</td>
<td>ACTIVE_NOT_RECRUITING</td>
<td>36</td>
<td>評估 trilaciclib、pembrolizumab、gemcitabine 和 carboplatin 在轉移性三陰性乳腺癌中的療效</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT00047255">NCT00047255</a></td>
<td>Phase 3</td>
<td>COMPLETED</td>
<td>263</td>
<td>比較 docetaxel/trastuzumab 與 docetaxel/carboplatin/trastuzumab 在 HER2 陽性轉移性乳腺癌的療效</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT01881230">NCT01881230</a></td>
<td>Phase 2/3</td>
<td>COMPLETED</td>
<td>191</td>
<td>評估 nab-paclitaxel 與 gemcitabine 或 carboplatin 在三陰性轉移性乳腺癌的療效</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT02413320">NCT02413320</a></td>
<td>Phase 2</td>
<td>COMPLETED</td>
<td>101</td>
<td>評估含 carboplatin 化療方案在三陰性乳腺癌新輔助治療中的病理完全緩解率</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT01445418">NCT01445418</a></td>
<td>Phase 1</td>
<td>COMPLETED</td>
<td>103</td>
<td>研究 PARP 抑制劑 AZD2281 與 carboplatin 併用在 BRCA1/2 突變攜帶者乳腺癌中的安全性</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<p>Carboplatin 在乳腺癌治療中的應用已有多項研究支持，尤其在以下領域：</p>

<ol>
<li><strong>三陰性乳腺癌 (TNBC)</strong>：多項臨床試驗顯示 carboplatin 可提高 TNBC 的病理完全緩解率</li>
<li><strong>BRCA 突變相關乳腺癌</strong>：carboplatin 對 DNA 修復缺陷的腫瘤細胞具有較高敏感性</li>
<li><strong>HER2 陽性乳腺癌</strong>：與 trastuzumab 併用已被證實有效</li>
</ol>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. rectum mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.28%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. colon mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.26%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（7 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21794003/" target="_blank">21794003</a></td><td>2011</td><td>Article</td><td>The journal of obste</td><td>Metastatic urachal carcinoma of the ovary.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33298341/" target="_blank">33298341</a></td><td>2021</td><td>Article</td><td>European journal of </td><td>Laparoscopic cytoreductive surgery and hyperthermic intraper...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15852675/" target="_blank">15852675</a></td><td>2005</td><td>Article</td><td>Hinyokika kiyo. Acta</td><td>[Carcinoma of the urachus: a case report].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29927186/" target="_blank">29927186</a></td><td>2016</td><td>Article</td><td>Journal of the Medic</td><td>Co-Existing Ovarian Mucinous Cystadenocarcinoma with Mature ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11420638/" target="_blank">11420638</a></td><td>2001</td><td>Article</td><td>Gene therapy</td><td>Intravenous infusion of a replication-selective adenovirus (...</td></tr>
</tbody>
</table>
<p><em>...及其他 2 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. adult germ cell tumor</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.24%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01445119" target="_blank">NCT01445119</a></td><td>PHASE1</td><td>COMPLETED</td><td>58</td><td>A Phase I Trial of Enzastaurin (LY317615) in Combination With Carboplatin in Adu...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00293358" target="_blank">NCT00293358</a></td><td>PHASE3</td><td>COMPLETED</td><td>500</td><td>SIOP Intracranial Germ Cell Tumours Protocol</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00010036" target="_blank">NCT00010036</a></td><td>PHASE2</td><td>COMPLETED</td><td>N/A</td><td>A Phase I/II Trial of CPT-11 With Carboplatin in Patients With Glioblastoma Mult...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00536601" target="_blank">NCT00536601</a></td><td>NA</td><td>COMPLETED</td><td>174</td><td>Autologous Blood and Marrow Transplantation for Hematologic Malignancies and Sel...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01857453" target="_blank">NCT01857453</a></td><td>PHASE2</td><td>UNKNOWN</td><td>97</td><td>National, Multicentric, Prospective Phase II Study Estimating the Interest of a ...</td></tr>
</tbody>
</table>
<p><em>...及其他 45 項試驗</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. cervical mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.24%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（2 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01652794" target="_blank">NCT01652794</a></td><td>PHASE1</td><td>COMPLETED</td><td>12</td><td>A Phase 1 Study of Carboplatin and Gemcitabine Chemotherapy and Stereotactic Bod...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06870565" target="_blank">NCT06870565</a></td><td>PHASE3</td><td>NOT_YET_RECRUITING</td><td>238</td><td>A Multicenter Randomized Study Comparing Paclitaxel and Platinum-based Concurren...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. gallbladder mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.23%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. endometrial mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.20%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（3 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01652794" target="_blank">NCT01652794</a></td><td>PHASE1</td><td>COMPLETED</td><td>12</td><td>A Phase 1 Study of Carboplatin and Gemcitabine Chemotherapy and Stereotactic Bod...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01081262" target="_blank">NCT01081262</a></td><td>PHASE3</td><td>ACTIVE_NOT_RECRUITING</td><td>50</td><td>A GCIG Intergroup Multicenter Phase III Trial of Open Label Carboplatin and Pacl...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01440998" target="_blank">NCT01440998</a></td><td>PHASE1</td><td>COMPLETED</td><td>18</td><td>Pilot and Translational Study of Dasatinib (NSC#732517) Paclitaxel and Carboplat...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34092768/" target="_blank">34092768</a></td><td>2021</td><td>Article</td><td>Journal of UOEH</td><td>Synchronous Occurrence of Ovarian Seromucinous Carcinoma and...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19473054/" target="_blank">19473054</a></td><td>2009</td><td>Article</td><td>Neoplasma</td><td>Gemcitabine and carboplatin treatment in patients with relap...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30718314/" target="_blank">30718314</a></td><td>2019</td><td>Article</td><td>International journa</td><td>Adenosine triphosphate-based chemotherapy response assay pre...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16884360/" target="_blank">16884360</a></td><td>2006</td><td>Article</td><td>International journa</td><td>Interferon-gamma in combination with carboplatin and paclita...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26763061/" target="_blank">26763061</a></td><td>2015</td><td>Article</td><td>Annals of the Academ</td><td>Singapore Cancer Network (SCAN) Guidelines for the Systemic ...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. endometrial mixed adenocarcinoma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.20%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（4 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05252416" target="_blank">NCT05252416</a></td><td>PHASE1</td><td>TERMINATED</td><td>50</td><td>A Phase 1/2 Study to Evaluate the Safety, Pharmacokinetics, and Efficacy of BLU-...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03914612" target="_blank">NCT03914612</a></td><td>PHASE3</td><td>ACTIVE_NOT_RECRUITING</td><td>813</td><td>A Phase III Randomized, Placebo-Controlled Study of Pembrolizumab (MK-3475, NSC ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05542407" target="_blank">NCT05542407</a></td><td>PHASE1</td><td>RECRUITING</td><td>58</td><td>Phase 1 Clinical Trial of ONC201 and Atezolizumab in Obesity-Driven Endometrial ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05256225" target="_blank">NCT05256225</a></td><td>PHASE3</td><td>RECRUITING</td><td>360</td><td>A Phase II/III Study of Paclitaxel/Carboplatin Alone or Combined With Either Tra...</td></tr>
</tbody>
</table>

<h3>相關文獻（10 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25611899/" target="_blank">25611899</a></td><td>2015</td><td>Article</td><td>International journa</td><td>Carboplatin and nonpegylated liposomal doxorubicin in primar...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19890461/" target="_blank">19890461</a></td><td>2006</td><td>Article</td><td>American journal of </td><td>Sensitivities of Uterine Adenocarcinoma, Mixed Mullerian Tum...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10811505/" target="_blank">10811505</a></td><td>2000</td><td>Article</td><td>Annals of oncology :</td><td>Endometrial mesodermal mixed tumor occurring after tamoxifen...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31993743/" target="_blank">31993743</a></td><td>2020</td><td>Article</td><td>Journal of cancer re</td><td>Should MMMT still be treated with adjuvant taxane-based comb...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/14599858/" target="_blank">14599858</a></td><td>2003</td><td>Article</td><td>Gynecologic oncology</td><td>A phase II trial of three sequential doublets for the treatm...</td></tr>
</tbody>
</table>
<p><em>...及其他 5 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. villoglandular endometrial endometrioid adenocarcinoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.20%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. extrahepatic bile duct mucinous adenocarcinoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.18%</span>
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
| 衛部藥輸字第027591號 | 曲斯若凍晶注射劑150毫克 | 凍晶注射劑 | 與 docetaxel 及 carboplatin 併用之 HER2 陽性早期乳癌輔助療法 |
| 衛署藥輸字第027591號 | 賀癌平皮下注射劑 | 皮下注射劑 | 與 docetaxel 及 carboplatin 併用之 HER2 陽性早期乳癌輔助療法 |
| 衛部藥輸字第028264號 | 吉舒達膜衣錠 | 膜衣錠 | 與 pemetrexed 及 carboplatin 併用之轉移性非鱗狀非小細胞肺癌第一線治療 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物 |
| 骨髓抑制風險 | 高度（血小板減少為劑量限制毒性） |
| 致吐性分級 | 中度至高度 |
| 監測項目 | CBC（含分類）、腎功能（肌酸酐清除率）、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

**重要警語**：
- Carboplatin 主要經腎臟排泄，腎功能不全患者需調整劑量
- 骨髓抑制為主要毒性，需定期監測血球計數
- 可能引起過敏反應，尤其是多次使用後

**藥物交互作用**：
- 與其他骨髓抑制藥物併用可能增加血液毒性
- 與腎毒性藥物（如 aminoglycoside 抗生素）併用需謹慎
- 避免與活性疫苗同時使用

### 藥物-食物交互作用 (DFI)

**葡萄柚** 🟢 Minor
- 影響：葡萄柚對鉑類化療藥影響較小
- 建議：無需特別限制


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Peripheral Nervous System Diseases** 🔴 Major
- 注意事項：Mild peripheral neuropathy has been noted during carboplatin therapy and is characterized most frequently by paresthesias...

**Infections** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。風險包括：骨髓抑制、感染。

**Hemorrhagic Disorders** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。風險包括：骨髓抑制、出血、血栓。可能有嚴重不良反應。

**Bone Marrow Failure Disorders** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。風險包括：骨髓抑制、出血、感染、血栓、貧血。可能有嚴重不良反應。

**腎臟疾病** 🟢 Minor
- 需定期監測。風險包括：骨髓抑制。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Carboplatin 在乳腺癌治療中已有大量臨床試驗證據支持，尤其在三陰性乳腺癌和 BRCA 突變相關乳腺癌中顯示良好療效。多項 Phase 2/3 試驗已完成或正在進行中。

**若要推進需要：**
- 密切監測骨髓抑制和腎功能
- 針對特定分子亞型（如 BRCA 突變、三陰性）的個體化用藥策略
- 與腫瘤科團隊密切合作，制定適當的併用方案

---

## 相關藥物報告

- [Oteracil]({{ "/drugs/oteracil/" | relative_url }}) - 證據等級 L2
- [Gemcitabine]({{ "/drugs/gemcitabine/" | relative_url }}) - 證據等級 L2
- [Dronedarone]({{ "/drugs/dronedarone/" | relative_url }}) - 證據等級 L2
- [Hydroxyprogesterone Caproate]({{ "/drugs/hydroxyprogesterone_caproate/" | relative_url }}) - 證據等級 L2
- [Vonoprazan]({{ "/drugs/vonoprazan/" | relative_url }}) - 證據等級 L2

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Carboplatin老藥新用驗證報告. https://twtxgnn.yao.care/drugs/carboplatin/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_carboplatin,
  title = {Carboplatin老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/carboplatin/}
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
