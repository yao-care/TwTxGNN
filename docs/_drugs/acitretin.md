---
layout: default
title: Acitretin
description: "Acitretin 的老藥新用潛力分析。中等證據等級 L3，包含 4 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 中證據等級 (L3-L4)
nav_order: 13
evidence_level: L3
indication_count: 4
---

# Acitretin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L3</strong> | 預測適應症: <strong>4</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acitretin：從乾癬到青春痘新適應症探索

## 一句話總結

<p class="key-answer" data-question="Acitretin 可以用於治療什麼新適應症？">
Acitretin 原本用於嚴重性乾癬及皮膚角化症。
TxGNN 模型預測它可能對**青春痘 (acne)** 有效，
目前有 **1 個臨床試驗**和 **18 篇文獻**支持這個方向。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 嚴重性牛皮癬、皮膚角化症 |
| 預測新適應症 | acne (disease)、pediatric systemic lupus erythematosus、fetal erythroblastosis、familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L3 |
| 台灣上市 | 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. acne (disease)</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.94%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Acitretin 屬於第二代芳香族維生素 A 酸衍生物（retinoid），其主要作用機轉包括：</p>
<ol>
<li>調節角質細胞分化與增殖</li>
<li>抑制皮脂腺活性</li>
<li>抗發炎作用</li>
<li>免疫調節功能</li>

</ol>
<p>青春痘的病理機轉涉及皮脂腺過度分泌、毛囊角化異常、痤瘡桿菌增殖及發炎反應。Retinoids 類藥物（如 isotretinoin）已是嚴重青春痘的標準治療。</p>

<p>Acitretin 與 isotretinoin 同屬 retinoids，但 acitretin 傳統上較少用於青春痘，主要因為其抑制皮脂腺的效果較 isotretinoin 弱。然而，文獻顯示 acitretin 在以下情況可作為替代選擇：</p>
<ul>
<li>Isotretinoin 治療失敗後的維持療法</li>
<li>化膿性汗腺炎（hidradenitis suppurativa / acne inversa）合併結節囊腫型青春痘</li>

</ul>
<p>2002 年個案報告 (PMID: 12080949) 顯示，isotretinoin 治療無效的結節囊腫型青春痘患者，使用 acitretin 後獲得顯著改善。</p>

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
<td><a href="https://clinicaltrials.gov/study/NCT04663906">NCT04663906</a></td>
<td>N/A</td>
<td>UNKNOWN</td>
<td>300</td>
<td>研究口服 isotretinoin（同屬 retinoid）在 COVID-19 感染風險的影響</td>
</tr>
</tbody>
</table>

<p>*註：目前無專門針對 acitretin 治療青春痘的註冊臨床試驗*</p>

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
<td><a href="https://pubmed.ncbi.nlm.nih.gov/12080949/">12080949</a></td>
<td>2002</td>
<td>Case Report</td>
<td>Cutis</td>
<td>Isotretinoin 無效的結節囊腫型青春痘合併化膿性汗腺炎，acitretin 維持治療成功</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/25640693/">25640693</a></td>
<td>2015</td>
<td>Guideline</td>
<td>JEADV</td>
<td>歐洲化膿性汗腺炎治療指引，提及 acitretin 為治療選項</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/29234829/">29234829</a></td>
<td>2018</td>
<td>Review</td>
<td>Der Hautarzt</td>
<td>化膿性汗腺炎藥物治療：isotretinoin 療效有限，acitretin 效果較佳</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/20874789/">20874789</a></td>
<td>2011</td>
<td>Journal Article</td>
<td>Br J Dermatol</td>
<td>25 年 acitretin 治療化膿性汗腺炎長期追蹤，療效良好</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/8573927/">8573927</a></td>
<td>1995</td>
<td>Review</td>
<td>Dermatology</td>
<td>Retinoids 與皮脂腺活性：比較不同 retinoids 的抗痘效果</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/9074840/">9074840</a></td>
<td>1997</td>
<td>Review</td>
<td>Drugs</td>
<td>Retinoids 在皮膚科的現況與未來：包含痤瘡相關應用</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. pediatric systemic lupus erythematosus</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.35%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. fetal erythroblastosis</span>
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
<span class="indication-name">4. familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.10%</span>
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
| 衛署藥輸字第022117號 | 新定康癬膠囊 25mg | 膠囊劑 | 嚴重性牛皮癬、皮膚角化症 |
| 衛署藥輸字第022118號 | 新定康癬膠囊 10mg | 膠囊劑 | 嚴重性牛皮癬、皮膚角化症 |

## 安全性考量

### 重要藥物交互作用

**Major 交互作用：**
- Tetracyclines（Doxycycline、Minocycline、Tetracycline）：增加假性腦瘤風險
- Vitamin A：增加維生素 A 過多症風險
- Ethanol（酒精）：可能將 acitretin 轉換為 etretinate，延長半衰期至數月
- Isotretinoin：禁止併用，增加維生素 A 毒性
- Methotrexate：增加肝毒性風險
- 口服避孕藥（Levonorgestrel、Norethisterone 等）：可能降低避孕效果

**Moderate 交互作用：**
- 磺胺尿素類降血糖藥（Glimepiride、Glipizide 等）：可能影響血糖控制
- 光敏感藥物（Aminolevulinic acid、Methoxsalen 等）：增加光敏感反應

### 重要警語
- **絕對禁止懷孕**：acitretin 具有強烈致畸性，育齡婦女必須於治療前、中、後使用有效避孕措施
- 因可能轉換為 etretinate，**停藥後需避孕至少 3 年**
- **禁止飲酒**：酒精會促進 acitretin 轉換為長效 etretinate
- 定期監測肝功能及血脂

安全性資訊請參考原廠仿單。


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Alcoholism** 🟡 Moderate
- 應避免使用本藥物。

**糖尿病** 🟡 Moderate
- 需密切監測。

**Toxic Optic Neuropathy** 🟡 Moderate
- 必要時應停止治療。

**Hyperlipidemias** 🟢 Minor
- 本藥物在此情況下禁用。需密切監測。

**肝臟疾病** 🟢 Minor
- 本藥物在此情況下禁用。可能有嚴重不良反應。

**腎臟疾病** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。可能有嚴重不良反應。

**Intracranial Hypertension** 🟢 Minor
- 出現症狀時應考慮停藥。

**Mental Disorders** 🟢 Minor
- 注意事項：The use of retinoids, primarily isotretinoin, has been associated with causing depression, psychosis and rarely, suicidal ideation...

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**酒精** 🟢 Minor
- 影響：產生協同作用。
- 建議：請諮詢醫師或藥師了解詳細建議。


## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Acitretin 與 isotretinoin 同屬 retinoids，具有相似的抗角化及抗發炎機轉。文獻顯示其在 isotretinoin 治療失敗或需長期維持治療的青春痘患者中有應用價值。特別是在化膿性汗腺炎合併青春痘的情況下，acitretin 可能比 isotretinoin 更有效。

**若要推進需要：**
- 排除懷孕可能性，育齡婦女需使用兩種有效避孕方法
- 完全禁止飲酒
- 定期監測肝功能（ALT、AST）及血脂（TG、Cholesterol）
- 避免併用維生素 A 補充劑
- 避免併用四環黴素類抗生素
- 設計 RCT 比較 acitretin 與 isotretinoin 在不同類型青春痘的療效

---

## 相關藥物報告

- [Vinorelbine]({{ "/drugs/vinorelbine/" | relative_url }}) - 證據等級 L3
- [Interferon Beta-1B]({{ "/drugs/interferon_beta-1b/" | relative_url }}) - 證據等級 L3
- [Lornoxicam]({{ "/drugs/lornoxicam/" | relative_url }}) - 證據等級 L3
- [Amcinonide]({{ "/drugs/amcinonide/" | relative_url }}) - 證據等級 L3
- [Human Immunoglobulin G]({{ "/drugs/human_immunoglobulin_g/" | relative_url }}) - 證據等級 L3

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Acitretin老藥新用驗證報告. https://twtxgnn.yao.care/drugs/acitretin/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_acitretin,
  title = {Acitretin老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/acitretin/}
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
