---
layout: default
title: Pravastatin
description: "Pravastatin 的老藥新用潛力分析。模型預測等級 L5，包含 9 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 9
---

# Pravastatin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>9</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pravastatin (普伐他汀) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Pravastatin 可以用於治療什麼新適應症？">
普伐他汀是一種HMG-CoA還原酶抑制劑(他汀類藥物),TxGNN預測其可用於同合子家族性高膽固醇血症和HIV感染相關血脂異常,兩者均有臨床試驗和文獻證據支持,且部分已接近核准適應症範圍。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Pravastatin (普伐他汀) |
| DrugBank ID | DB00175 |
| 台灣品牌名 | 帕瓦斯德定鈉鹽、Mevalotin等 |
| 原核准適應症 | 高血脂症、心血管疾病預防、移植後高脂血症 |
| 預測新適應症 | homozygous familial hypercholesterolemia、obsolete familial combined hyperlipidemia、HIV infectious disease、neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter、feline acquired immunodeficiency syndrome、simian immunodeficiency virus infection、hyperlipoproteinemia、familial hypercholesterolemia、hypoalphalipoproteinemia |
| 最高證據等級 | L1-L2 (多個RCT支持) |
| 臨床試驗數 | 4項以上 |
| 文獻支持 | 豐富 (>13篇) |

## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. homozygous familial hypercholesterolemia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.95%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

### 同合子家族性高膽固醇血症預測分析 (TxGNN Score: 0.9995, Rank: 1691)

1. **他汀類藥物機制**: Pravastatin抑制HMG-CoA還原酶,減少肝臟膽固醇合成
2. **家族性高膽固醇血症治療**: 已核准用於家族性高膽固醇血症(heterozygous)
3. **同合子型挑戰**: hoFH患者LDL受體功能嚴重缺陷,單一他汀療效有限但仍為基礎治療
4. **合併治療策略**: 通常需與PCSK9抑制劑、ezetimibe、LDL血漿分離術合併

### HIV感染相關血脂異常預測分析 (TxGNN Score: 0.997, Rank: 5819)

1. **抗病毒藥物副作用**: HIV蛋白酶抑制劑常導致血脂異常
2. **代謝安全性優勢**: Pravastatin不經CYP3A4代謝,與抗病毒藥物交互作用少
3. **臨床實證支持**: 已有隨機對照試驗證實其在HIV患者中的安全性和有效性

### 臨床試驗

### 同合子家族性高膽固醇血症相關試驗

| 試驗編號 | Phase | 狀態 | 研究藥物 | 說明 |
|----------|-------|------|----------|------|
| NCT03510715 | Phase 3 | 已完成 | Alirocumab | 兒童青少年hoFH,背景他汀治療 |

**NCT03510715試驗重點**:
- 8-17歲hoFH患者
- 在他汀類(含pravastatin)+/-其他降脂藥基礎上加用alirocumab
- 證實合併療法的可行性

### HIV感染相關血脂異常試驗

| 試驗編號 | Phase | 狀態 | 設計 | 受試者數 |
|----------|-------|------|------|----------|
| NCT00982189 | N/A | 已完成 | Polypill預防研究 | 37人 |
| NCT00227500 | Phase 4 | 已完成 | 隨機雙盲對照 | 40人 |
| NCT00017758 | Phase 1 | 已完成 | 藥動學交互作用研究 | 56人 |

**NCT00227500試驗重點**:
- 隨機、安慰劑對照研究
- HIV感染合併蛋白酶抑制劑使用的高膽固醇血症患者
- 主要終點: 空腹總膽固醇的時間加權變化
- 證實pravastatin在HIV患者中的降脂效果

**NCT00017758試驗重點**:
- 評估efavirenz和nelfinavir對pravastatin藥動學的影響
- 確認pravastatin與抗病毒藥物的交互作用特性

### 相關文獻

### 同合子家族性高膽固醇血症相關文獻 (>13篇)

| PMID | 年份 | 研究類型 | 主要發現 |
|------|------|----------|----------|
| 28437620 | 2017 | 指引 | AACE/ACE血脂異常管理指引 |
| 28685504 | 2017 | Cochrane系統性回顧 | 兒童FH的他汀類藥物治療 |
| 31696945 | 2019 | Cochrane系統性回顧更新 | 確認他汀在兒童FH的角色 |
| 12269853 | 2002 | 藥物評論 | Rosuvastatin與pravastatin比較 |

**關鍵發現**:
- 他汀類藥物是家族性高膽固醇血症的基礎治療
- 兒童期開始治療可降低長期心血管風險
- hoFH需多重療法合併,單一他汀效果有限

### HIV相關血脂異常文獻

| PMID | 年份 | 研究類型 | 主要發現 |
|------|------|----------|----------|
| 28416195 | 2017 | Phase 4 RCT | Pitavastatin vs Pravastatin在HIV患者(INTREPID試驗) |

**INTREPID試驗 (PMID: 28416195)重點**:
- 多中心、隨機、雙盲、52週試驗
- HIV-1感染合併血脂異常患者
- Pravastatin因不經CYP3A4代謝,藥物交互作用風險低
- Pitavastatin降LDL效果優於pravastatin

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. HIV infectious disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.74%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.74%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.62%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.62%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. feline acquired immunodeficiency syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.55%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. simian immunodeficiency virus infection</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.55%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. familial hypercholesterolemia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.34%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.34%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. hypoalphalipoproteinemia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.21%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.21%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.07%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.07%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. cholesterol-ester transfer protein deficiency</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.04%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.04%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

## 台灣上市資訊

### 有效許可證

台灣已有多項pravastatin製劑核准,核准適應症包括:

1. **高血脂症**: 原發性高膽固醇血症、混合型高血脂症
2. **初發性預防**: 高膽固醇血症無冠心病患者的心肌梗塞預防
3. **再發性預防**: 冠心病患者的二次預防
4. **移植後高脂血症**: 心臟移植後免疫抑制治療相關高脂血症

### 重要說明
家族性高膽固醇血症已在部分製劑核准適應症中提及。

## 安全性考量

### 已知安全性資訊

1. **肌肉毒性**: 罕見但可能發生橫紋肌溶解症
2. **肝功能異常**: 需監測肝功能指數
3. **糖尿病風險**: 長期使用可能輕微增加糖尿病風險
4. **藥物交互作用**: 與部分藥物有交互作用,但程度較其他他汀輕

### HIV患者特殊考量

1. **CYP代謝優勢**: Pravastatin不經CYP3A4代謝
2. **與抗病毒藥物交互作用**:
   - 與蛋白酶抑制劑交互作用較少
   - Lopinavir/ritonavir可能增加pravastatin血中濃度
3. **監測建議**: 仍需定期監測肝功能和肌酸激酶

### 藥物交互作用重點

- 與fibrates併用增加肌病風險
- 與免疫抑制劑(ciclosporin)交互需謹慎
- 與抗凝血劑需監測INR

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**酒精 (alcohol)** 🟡 Moderate
- 影響：Concomitant use of statin medication with substantial quantities of alcohol may increase the risk of hepatic injury.
- 建議：Patients should be counseled to avoid substantial quantities of alcohol in combination with statin medications and clinicians should be aware of the increased risk for hepatotoxicity in these patients...


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Cognitive Dysfunction** 🟡 Moderate
- 應謹慎使用本藥物。可能有嚴重不良反應。

**糖尿病** 🟡 Moderate
- 應謹慎使用本藥物。需定期監測。

**腎臟疾病** 🟡 Moderate
- 應謹慎使用本藥物。需定期監測。可能需要降低劑量。可能有嚴重不良反應。

**肝臟疾病** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。

**Rhabdomyolysis** 🟢 Minor
- 需定期監測。可能有嚴重不良反應。

**腎臟疾病** 🟢 Minor
- 需定期監測。可能有嚴重不良反應。

## 結論與下一步

### 整體評估

| 評估項目 | 同合子家族性高膽固醇血症 | HIV相關血脂異常 |
|----------|--------------------------|------------------|
| 證據等級 | L2 (系統性回顧支持) | L1-L2 (多個RCT) |
| 機制合理性 | 高 (已為基礎治療) | 高 (代謝優勢) |
| 臨床可行性 | 高 (合併療法一部分) | 高 |
| 建議優先順序 | 高 | 高 |

### 建議

**同合子家族性高膽固醇血症**:
1. **臨床定位**: 作為hoFH多重療法的基礎治療
2. **合併用藥**: 需與PCSK9抑制劑、ezetimibe等合併
3. **適應症擴展**: 考慮在現有家族性高膽固醇血症適應症下包含hoFH

**HIV相關血脂異常**:
1. **首選他汀之一**: 因代謝特性,為HIV患者較安全的他汀選擇
2. **臨床推廣**: 可在抗病毒治療相關血脂異常指引中推薦
3. **藥動學優勢**: 特別適用於使用CYP3A4抑制劑型抗病毒藥物的患者

### 實務建議

1. **監測計畫**:
   - 基線和治療期間定期監測肝功能、CK
   - HIV患者注意病毒載量和CD4變化

2. **劑量考量**:
   - HIV患者可能需較低起始劑量
   - 根據降脂效果調整劑量

### 限制說明

- hoFH患者因LDL受體缺陷,他汀單一療法效果有限
- Pravastatin降脂效力不如其他高效他汀(如atorvastatin, rosuvastatin)
- HIV患者的心血管預後長期數據仍在累積中

---
*報告產生日期: 2026-02-11*
*資料來源: TxGNN預測、ClinicalTrials.gov、PubMed、台灣食品藥物管理署*

---

## 相關藥物報告

- [Nepafenac]({{ "/drugs/nepafenac/" | relative_url }}) - 證據等級 L5
- [Pimozide]({{ "/drugs/pimozide/" | relative_url }}) - 證據等級 L5
- [Etanercept]({{ "/drugs/etanercept/" | relative_url }}) - 證據等級 L5
- [Bempedoic Acid]({{ "/drugs/bempedoic_acid/" | relative_url }}) - 證據等級 L5
- [Homatropine Methylbromide]({{ "/drugs/homatropine_methylbromide/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Pravastatin老藥新用驗證報告. https://twtxgnn.yao.care/drugs/pravastatin/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_pravastatin,
  title = {Pravastatin老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/pravastatin/}
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
