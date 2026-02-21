---
layout: default
title: Pitavastatin
description: "Pitavastatin 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L1
indication_count: 10
---

# Pitavastatin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pitavastatin 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Pitavastatin 可以用於治療什麼新適應症？">
Pitavastatin 為 HMG-CoA 還原酶抑制劑，TxGNN 預測對家族性高膽固醇血症等脂質代謝疾病有療效，已有豐富臨床試驗及文獻支持，部分預測與現有適應症重疊。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品學名 | Pitavastatin (匹伐他汀/環丙烯脂汀) |
| DrugBank ID | DB08860 |
| 原核准適應症 | 原發性高膽固醇血症、混合型血脂異常、兒童家族性高膽固醇血症 |
| TxGNN 預測新適應症 | obsolete familial combined hyperlipidemia、homozygous familial hypercholesterolemia、hyperlipoproteinemia、hyperlipidemia, familial combined, LPL related、familial hypercholesterolemia、cholesterol-ester transfer protein deficiency、hypercholesterolemia, autosomal dominant、hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency、HIV infectious disease、neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter |
| 台灣許可證數 | 46 張 |
| 最高證據等級 | L1-L2 (RCT) |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. homozygous familial hypercholesterolemia</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">100.00%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

Pitavastatin 作為 statin 類藥物，其預測的新適應症在機轉上完全合理：

1. **同型合子家族性高膽固醇血症 (Homozygous FH)**：Pitavastatin 抑制 HMG-CoA 還原酶，減少肝臟膽固醇合成，是 FH 的一線治療選擇
2. **高脂蛋白血症 (Hyperlipoproteinemia)**：Statin 類藥物可有效降低 LDL-C，對各類高脂蛋白血症均有療效
3. **家族性高膽固醇血症**：已是台灣核准適應症的一部分，預測與現有適應症重疊

### 臨床試驗

| 預測適應症 | 臨床試驗數 | 代表性試驗 |
|------------|-----------|-----------|
| 高脂蛋白血症 | 12 | NCT01256476: Phase 4 比較 Pitavastatin 4mg vs Pravastatin 40mg (完成) |
| 家族性高膽固醇血症 | 2 | NCT02107898: Alirocumab 添加於 Pitavastatin 治療 HeFH (完成) |
| 同型合子 FH | 0 | 直接相關試驗少，但異型合子 FH 有多項試驗 |

### 主要臨床試驗

| 試驗 ID | 標題 | Phase | 狀態 | 主要發現 |
|---------|------|-------|------|----------|
| NCT01256476 | Pitavastatin 4mg vs Pravastatin 40mg | Phase 4 | 完成 | 328 例患者，比較兩藥降 LDL-C 效果 |
| NCT01386853 | Pitavastatin vs Atorvastatin 非劣性試驗 | Phase 3 | 完成 | 台灣執行，200 例高風險患者 |
| NCT02056847 | Pitavastatin 在空腹血糖異常患者 | Phase 4 | 完成 | 313 例，評估 HbA1c 影響 |

### 相關文獻

### 同型合子家族性高膽固醇血症
**證據等級：L3 (病例報告)**

| PMID | 標題 | 年份 | 重點發現 |
|------|------|------|----------|
| 39532566 | Rapid lipid-lowering response in ARH | 2025 | Pitavastatin 合併 Ezetimibe 在自體隱性高膽固醇血症有快速降脂效果 |

### 家族性高膽固醇血症 (異型合子)
**證據等級：L2 (多個 RCT)**

| PMID | 標題 | 年份 | 重點發現 |
|------|------|------|----------|
| 29187694 | Pitavastatin in children with FH (Japan/Europe) | 2018 | RCT 證實 Pitavastatin 在兒童 FH 患者安全有效 |
| 25891210 | Pitavastatin in Japanese male children with FH | 2016 | 多中心 RCT，證實 Pitavastatin 在日本兒童 FH 的療效與安全性 |
| 12048134 | Long-term treatment with pitavastatin in FH | 2002 | 104 週長期治療顯示 LDL-C 降低 49% |
| 10955373 | NK-104 in heterozygous FH | 2000 | 劑量依賴性降低 LDL-C，4mg/天可降 48% |

### 高脂蛋白血症
**證據等級：L2 (多個 RCT)**

| PMID | 標題 | 年份 | 重點發現 |
|------|------|------|----------|
| 23672789 | Pitavastatin vs Atorvastatin (COMPACT-CAD) | 2013 | RCT 顯示 Pitavastatin 增加 HDL-C 及 Adiponectin 效果優於 Atorvastatin |
| 17957184 | Pitavastatin vs Atorvastatin on CoQ10 | 2008 | Pitavastatin 較少影響 CoQ10 濃度 |

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. hyperlipoproteinemia</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">100.00%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：100.00%
- **證據等級**：L1（多個大型 RCT 支持）

### 臨床證據

**臨床試驗**：共 12 項

- 試驗階段分布：NA: 1項, PHASE1: 4項, PHASE3: 3項, PHASE4: 4項

**相關文獻**：共 15 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. familial hypercholesterolemia</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.99%
- **證據等級**：L2（單一 RCT 或多個 Phase 2）

### 臨床證據

**臨床試驗**：共 2 項

- 試驗階段分布：PHASE2: 1項, PHASE3: 1項

**相關文獻**：共 19 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. cholesterol-ester transfer protein deficiency</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.98%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. hypercholesterolemia, autosomal dominant</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.97%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.97%
- **證據等級**：L2（單一 RCT 或多個 Phase 2）

### 臨床證據

**臨床試驗**：共 2 項

- 試驗階段分布：PHASE2: 1項, PHASE3: 1項

**相關文獻**：共 12 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.97%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.97%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. HIV infectious disease</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.97%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.97%
- **證據等級**：L1（多個大型 RCT 支持）

### 臨床證據

**臨床試驗**：共 2 項

- 試驗階段分布：PHASE3: 2項

**相關文獻**：共 20 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.95%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.95%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. hyperlipidemia due to hepatic triglyceride lipase deficiency</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.94%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.94%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. simian immunodeficiency virus infection</span>
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


## 台灣上市資訊

### 上市狀態
台灣已核准上市，共有 46 張許可證，目前有效許可證超過 20 張。

### 代表性產品

| 許可證字號 | 商品名 | 劑型 | 許可證持有者 | 效期 |
|------------|--------|------|--------------|------|
| 衛部藥輸字第027002號 | 力清之口溶錠2毫克 (LIVALO) | 口溶錠 | 台田藥品股份有限公司 | 2027/01/19 |
| 衛部藥製字第059192號 | 庇脂清膜衣錠4毫克 | 膜衣錠 | 瑩碩生技醫藥股份有限公司 | 2026/05/23 |
| 衛部藥製字第060290號 | 好脂定膜衣錠4毫克 | 膜衣錠 | 永信藥品工業股份有限公司 | 2029/05/09 |
| 衛署藥製字第057372號 | 必抑脂膜衣錠2毫克 | 膜衣錠 | 友霖生技醫藥股份有限公司 | 2027/09/26 |
| 衛部藥製字第061165號 | 同抑脂膠囊2/10毫克 | 膠囊劑 | 友霖生技醫藥股份有限公司 | 2027/10/28 |

### 核准適應症
- 原發性高膽固醇血症
- 混合型血脂異常
- 10 歲以上兒童家族性高膽固醇血症

## 安全性考量

### 藥物交互作用

DDInter 資料庫顯示 Pitavastatin 與多種藥物有交互作用：

**中度交互作用 (Moderate)**：
- Eluxadoline
- Naltrexone
- Metronidazole

### 注意事項
1. **肌肉毒性**：監測肌肉疼痛、無力，定期檢測 CK 值
2. **肝功能**：開始治療前及治療期間定期監測肝功能
3. **藥物交互作用**：Pitavastatin 主要經 CYP2C9 代謝，與 CYP3A4 無明顯交互作用，較其他 statin 藥物交互作用風險低
4. **HIV 患者**：可用於接受抗病毒治療的 HIV 患者（INTREPID 試驗支持）


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**糖尿病** 🟡 Moderate
- 應謹慎使用本藥物。需定期監測。

**腎臟疾病** 🟡 Moderate
- 應謹慎使用本藥物。需定期監測。可能需要降低劑量。可能有嚴重不良反應。

**肝臟疾病** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。

**Rhabdomyolysis** 🟢 Minor
- 需定期監測。可能有嚴重不良反應。

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**酒精** 🟡 Moderate
- 影響：產生協同作用。
- 建議：建議避免併用。


## 結論與下一步

### 預測價值評估

| 預測適應症 | 證據等級 | 文獻支持 | 臨床試驗 | 總評 |
|------------|----------|----------|----------|------|
| 同型合子 FH | L3 | 2 篇 | 間接 | 中度支持 |
| 高脂蛋白血症 | L2 | 15+ 篇 | 12 | 強力支持 |
| 家族性高膽固醇血症 | L1-L2 | 18+ 篇 | 2 | 已為核准適應症 |

### 建議
1. **高脂蛋白血症**及**家族性高膽固醇血症**預測與現有適應症高度重疊，證實模型預測準確
2. **同型合子 FH**：雖文獻支持較少，但基於作用機轉，Pitavastatin 可作為綜合治療方案的一部分
3. Pitavastatin 較其他 statin 藥物交互作用風險低，適合多重用藥患者

---
*本筆記由 TwTxGNN 系統自動產生，僅供研究參考，不構成醫療建議。*
*產生日期：2026-02-11*

---

## 相關藥物報告

- [Emedastine]({{ "/drugs/emedastine/" | relative_url }}) - 證據等級 L5
- [Theophylline]({{ "/drugs/theophylline/" | relative_url }}) - 證據等級 L5
- [Isoleucine]({{ "/drugs/isoleucine/" | relative_url }}) - 證據等級 L5
- [Nitrofurantoin]({{ "/drugs/nitrofurantoin/" | relative_url }}) - 證據等級 L5
- [Inclisiran]({{ "/drugs/inclisiran/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Pitavastatin老藥新用驗證報告. https://twtxgnn.yao.care/drugs/pitavastatin/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_pitavastatin,
  title = {Pitavastatin老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/pitavastatin/}
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
