---
layout: default
title: Famotidine
description: "Famotidine 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L1
indication_count: 10
---

# Famotidine

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Famotidine 藥師評估筆記

## 一句話總結

<p class="key-answer" data-question="Famotidine 可以用於治療什麼新適應症？">
Famotidine 是 H2 受體拮抗劑，TxGNN 預測其可用於十二指腸胃食道逆流和消化性潰瘍，這些預測與原核准適應症高度重疊，具有充分的臨床證據支持。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Famotidine (法莫替丁) |
| DrugBank ID | DB00927 |
| 台灣商品名 | 諾得舒胃福治潰膜衣錠 |
| 原核准適應症 | 胃潰瘍、十二指腸潰瘍、逆流性食道炎、Zollinger-Ellison 症候群 |
| 預測新適應症 | peptic esophagitis、gastrin secretion abnormality、duodenogastric reflux、duodenal obstruction、duodenal ulcer (disease)、active peptic ulcer disease、peptic ulcer perforation、gastrojejunal ulcer、esophagitis (disease)、Zollinger-Ellison syndrome |
| 最高預測分數 | 0.9999 (duodenogastric reflux) |
| 證據等級 | L2 (單一 RCT/多個 Phase 2) |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. duodenogastric reflux</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.99%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Famotidine 的預測適應症與其已知藥理機轉高度一致：</p>

<ol>
<li><strong>胃酸抑制機轉</strong>：H2 受體拮抗劑可減少胃酸分泌，是治療消化性潰瘍的經典機轉</li>
<li><strong>黏膜保護</strong>：減少胃酸可降低胃黏膜損傷，促進潰瘍癒合</li>
<li><strong>適應症重疊</strong>：預測的適應症實際上是原核准適應症的延伸或細分</li>
<li><strong>臨床實務一致</strong>：這些預測反映了 famotidine 的實際臨床使用範圍</li>
</ol>

<h3>臨床試驗</h3>

<p>### ClinicalTrials.gov 搜尋結果</p>

<table>
<thead>
<tr>
<th>試驗編號</th>
<th>階段</th>
<th>狀態</th>
<th>適應症</th>
<th>受試者數</th>
</tr>
</thead>
<tbody>
<tr>
<td>NCT00450216</td>
<td>Phase 3</td>
<td>完成</td>
<td>十二指腸潰瘍(NSAID相關)</td>
<td>906</td>
</tr>
<tr>
<td>NCT00450658</td>
<td>Phase 3</td>
<td>完成</td>
<td>上消化道潰瘍</td>
<td>627</td>
</tr>
</tbody>
</table>

<p><strong>證據等級：L2 (有 Phase 3 臨床試驗)</strong></p>

<h3>相關文獻</h3>

<p>PubMed 搜尋發現豐富的文獻支持：</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. duodenal obstruction</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（2 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00450216" target="_blank">NCT00450216</a></td><td>PHASE3</td><td>COMPLETED</td><td>906</td><td>A Randomized, Double-Blind, Phase 3 Study of the Efficacy and Safety of HZT-501 ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00450658" target="_blank">NCT00450658</a></td><td>PHASE3</td><td>COMPLETED</td><td>627</td><td>A Randomized, Double-Blind, Phase 3 Study of the Efficacy and Safety of HZT-501 ...</td></tr>
</tbody>
</table>

<h3>相關文獻（3 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8165479/" target="_blank">8165479</a></td><td>1994</td><td>Article</td><td>Surgical endoscopy</td><td>Giant marginal ulcer.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9306611/" target="_blank">9306611</a></td><td>1997</td><td>Article</td><td>Surgery today</td><td>Surgical treatment for duodenal involvement in Crohn&#x27;s disea...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2816881/" target="_blank">2816881</a></td><td>1989</td><td>Article</td><td>The American journal</td><td>Failure of single night-time dose of H2-receptor antagonists...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. active peptic ulcer disease</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（19 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9506245/" target="_blank">9506245</a></td><td>1998</td><td>Article</td><td>Drugs</td><td>Rabeprazole.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2905237/" target="_blank">2905237</a></td><td>1988</td><td>Article</td><td>Drugs</td><td>Prostaglandins, H2-receptor antagonists and peptic ulcer dis...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3310199/" target="_blank">3310199</a></td><td>1987</td><td>Article</td><td>Scandinavian journal</td><td>Ulcer pain mechanisms. The clinical features of active pepti...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34798155/" target="_blank">34798155</a></td><td>2022</td><td>Article</td><td>International journa</td><td>Famotidine-loaded solid self-nanoemulsifying drug delivery s...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39345794/" target="_blank">39345794</a></td><td>2024</td><td>Article</td><td>Toxicology research</td><td>Diospyros kaki fruit aqueous extract individual/combined wit...</td></tr>
</tbody>
</table>
<p><em>...及其他 14 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. peptic ulcer perforation</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（2 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00683111" target="_blank">NCT00683111</a></td><td>PHASE4</td><td>COMPLETED</td><td>500</td><td>Famotidine Compared With Esomeprazole in the Prevention of Ulcer Complications i...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00450658" target="_blank">NCT00450658</a></td><td>PHASE3</td><td>COMPLETED</td><td>627</td><td>A Randomized, Double-Blind, Phase 3 Study of the Efficacy and Safety of HZT-501 ...</td></tr>
</tbody>
</table>

<h3>相關文獻（9 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8165479/" target="_blank">8165479</a></td><td>1994</td><td>Article</td><td>Surgical endoscopy</td><td>Giant marginal ulcer.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19837071/" target="_blank">19837071</a></td><td>2010</td><td>Article</td><td>Gastroenterology</td><td>Famotidine is inferior to pantoprazole in preventing recurre...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21954519/" target="_blank">21954519</a></td><td>2011</td><td>Article</td><td>Prescrire internatio</td><td>Nonsteroidal anti-inflammatory drugs: add an anti-ulcer drug...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10379475/" target="_blank">10379475</a></td><td>1999</td><td>Article</td><td>Italian journal of g</td><td>A clinical approach to management of patients with non-stero...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21387691/" target="_blank">21387691</a></td><td>2011</td><td>Article</td><td>Nihon rinsho. Japane</td><td>[Strategy to manage low dose aspirin-induced gastrointestina...</td></tr>
</tbody>
</table>
<p><em>...及其他 4 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. gastrojejunal ulcer</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00557349" target="_blank">NCT00557349</a></td><td>PHASE4</td><td>COMPLETED</td><td>40</td><td>A Randomized, Double-blind Clinical Trial Comparing Zegerid Capsule to Famotidin...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35348552/" target="_blank">35348552</a></td><td>2022</td><td>Article</td><td>The Medical letter o</td><td>Drugs for GERD and peptic ulcer disease.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2028638/" target="_blank">2028638</a></td><td>1991</td><td>Article</td><td>DICP : the annals of</td><td>Famotidine and cardiac arrhythmia.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8853932/" target="_blank">8853932</a></td><td>1996</td><td>Article</td><td>Clinical pharmacokin</td><td>Pharmacokinetics and pharmacodynamics of famotidine in paedi...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2892567/" target="_blank">2892567</a></td><td>1988</td><td>Article</td><td>British medical jour</td><td>Peptic ulceration.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2875864/" target="_blank">2875864</a></td><td>1986</td><td>Article</td><td>Drugs</td><td>Famotidine. Pharmacodynamic and pharmacokinetic properties a...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. abnormality of glucagon secretion</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.91%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. gastroduodenitis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.80%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25521726/" target="_blank">25521726</a></td><td>2014</td><td>Article</td><td>Journal of gastroent</td><td>Comparison of teprenone and famotidine against gastroduodena...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9178671/" target="_blank">9178671</a></td><td>1997</td><td>Article</td><td>Gastroenterology</td><td>Famotidine for healing and maintenance in nonsteroidal anti-...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/7846741/" target="_blank">7846741</a></td><td>1994</td><td>Article</td><td>Therapeutic drug mon</td><td>Pharmacokinetics and pharmacodynamics of famotidine in child...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22066725/" target="_blank">22066725</a></td><td>2012</td><td>Article</td><td>Neurogastroenterolog</td><td>Influence of gastric acid on gastric emptying and gastric di...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/14653238/" target="_blank">14653238</a></td><td>2003</td><td>Article</td><td>Eksperimental&#x27;naia i</td><td>[Laser therapy and famotidine in complex restorative treatme...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. peptic ulcer disease</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.72%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（14 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00683111" target="_blank">NCT00683111</a></td><td>PHASE4</td><td>COMPLETED</td><td>500</td><td>Famotidine Compared With Esomeprazole in the Prevention of Ulcer Complications i...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03667703" target="_blank">NCT03667703</a></td><td>PHASE4</td><td>COMPLETED</td><td>70</td><td>Stress Ulcer Prophylaxis Versus Placebo - a Blinded Randomized Control Trial to ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00839488" target="_blank">NCT00839488</a></td><td>PHASE4</td><td>TERMINATED</td><td>6</td><td>Comparison of Intravenous Pantoprazole and Famotidine for Stress Ulcer Prophylax...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01180179" target="_blank">NCT01180179</a></td><td>PHASE4</td><td>COMPLETED</td><td>228</td><td>Prevention of Recurrent Idiopathic Gastroduodenal Ulcer Bleeding: a Double-blind...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00229424" target="_blank">NCT00229424</a></td><td>PHASE3</td><td>COMPLETED</td><td>325</td><td>Verification Study on Lafutidine in Mild Reflux Oesophagitis - Double Blind Cont...</td></tr>
</tbody>
</table>
<p><em>...及其他 9 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35348552/" target="_blank">35348552</a></td><td>2022</td><td>Article</td><td>The Medical letter o</td><td>Drugs for GERD and peptic ulcer disease.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2573505/" target="_blank">2573505</a></td><td>1989</td><td>Article</td><td>Drugs</td><td>Famotidine. An updated review of its pharmacodynamic and pha...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2875864/" target="_blank">2875864</a></td><td>1986</td><td>Article</td><td>Drugs</td><td>Famotidine. Pharmacodynamic and pharmacokinetic properties a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2905237/" target="_blank">2905237</a></td><td>1988</td><td>Article</td><td>Drugs</td><td>Prostaglandins, H2-receptor antagonists and peptic ulcer dis...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34798155/" target="_blank">34798155</a></td><td>2022</td><td>Article</td><td>International journa</td><td>Famotidine-loaded solid self-nanoemulsifying drug delivery s...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. multiple endocrine neoplasia</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.69%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（3 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05417594" target="_blank">NCT05417594</a></td><td>PHASE1, PHASE2</td><td>RECRUITING</td><td>695</td><td>A Modular Phase I/IIa, Open-label, Multi-centre Study to Assess the Safety, Tole...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01248962" target="_blank">NCT01248962</a></td><td>PHASE2</td><td>COMPLETED</td><td>146</td><td>Standard Infusion Carboplatin Versus Prophylactic Extended Infusion Carboplatin ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00451880" target="_blank">NCT00451880</a></td><td>PHASE1</td><td>COMPLETED</td><td>180</td><td>A Phase 1 Dose-Escalation Study of the Safety and Pharmacokinetics of XL281 Admi...</td></tr>
</tbody>
</table>

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2874977/" target="_blank">2874977</a></td><td>1986</td><td>Article</td><td>Drugs</td><td>Current management of Zollinger-Ellison syndrome.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. acne (disease)</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

Famotidine 在台灣有多種劑型和品牌上市：

| 許可證字號 | 中文品名 | 劑型 | 許可證持有者 | 狀態 |
|-----------|---------|------|-------------|------|
| 衛署藥製字第037684號 | 諾得舒胃福治潰膜衣錠40毫克 | 膜衣錠 | 約克製藥股份有限公司 | 有效 |
| 衛署藥製字第034815號 | 胃康舒膜衣錠20毫克 | 膜衣錠 | 永信藥品工業股份有限公司 | 有效 |
| 衛署藥製字第036152號 | 法瑪乳頓膠囊20毫克 | 膠囊 | 中國化學製藥股份有限公司 | 有效 |

**劑型多樣**：錠劑、膠囊、注射劑、口溶錠等

## 安全性考量

### 已知風險
- **整體安全性良好**：H2 拮抗劑是最安全的抑酸藥物之一
- **頭痛**：最常見的副作用(約 4%)
- **腸胃不適**：便秘、腹瀉
- **血液學異常**：罕見的血小板減少症

### 藥物交互作用
根據 DDInter 資料庫：

| 交互作用藥物 | 嚴重度 | 說明 |
|-------------|--------|------|
| Ketoconazole | Moderate | 減少 ketoconazole 吸收 |
| Atazanavir | Major | 減少 atazanavir 吸收，避免併用 |
| Delavirdine | Major | 減少 delavirdine 吸收 |
| Dasatinib | Moderate | 可能減少吸收 |

### 特殊族群
- **孕婦**：B 級，相對安全
- **哺乳**：分泌至乳汁，建議謹慎使用
- **腎功能不全**：CrCl < 50 mL/min 需減量
- **老年人**：一般無需調整劑量

### 藥物-食物交互作用 (DFI)

**咖啡因（咖啡、茶、可樂）** 🟢 Minor
- 影響：H2 阻斷劑可能增加咖啡因吸收
- 建議：無需特別限制


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**腎臟疾病** 🟡 Moderate
- 可能需要調整劑量。風險包括：癲癇發作。可能有嚴重不良反應。

**Peptic Ulcer Hemorrhage** 🟢 Minor
- 不應使用本藥物。可能有嚴重不良反應。

## 結論與下一步

### 整體評估
此預測**已有充分臨床證據支持**，原因如下：
1. 預測適應症與原核准適應症高度重疊
2. 有多個 RCT 和系統性回顧支持
3. 藥理機轉明確
4. 長期安全性資料完整

### 建議行動
- [x] 這些適應症在臨床實務中已被廣泛使用
- [ ] 可考慮向 TFDA 申請適應症擴展（如明確的「十二指腸胃逆流」適應症）
- [ ] 持續監測長期使用的安全性

### 臨床建議
Famotidine 可安全用於：
- 輕至中度消化性潰瘍
- NSAID 相關潰瘍的預防
- 胃食道逆流疾病
- 應激性潰瘍預防

對於較嚴重的病例，可考慮使用 PPI 類藥物。

### 風險等級
**低風險** - 可在適當適應症下安全使用

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、TFDA*

---

## 相關藥物報告

- [Urea]({{ "/drugs/urea/" | relative_url }}) - 證據等級 L5
- [Alprostadil]({{ "/drugs/alprostadil/" | relative_url }}) - 證據等級 L5
- [Threonine]({{ "/drugs/threonine/" | relative_url }}) - 證據等級 L5
- [Levamisole]({{ "/drugs/levamisole/" | relative_url }}) - 證據等級 L5
- [Tioconazole]({{ "/drugs/tioconazole/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Famotidine老藥新用驗證報告. https://twtxgnn.yao.care/drugs/famotidine/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_famotidine,
  title = {Famotidine老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/famotidine/}
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
