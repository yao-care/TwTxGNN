---
layout: default
title: Leflunomide
description: "Leflunomide 的老藥新用潛力分析。模型預測等級 L5，包含 2 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 2
---

# Leflunomide

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>2</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Leflunomide (來氟米特) - 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Leflunomide 可以用於治療什麼新適應症？">
Leflunomide 為免疫調節劑，目前核准用於類風濕性關節炎與乾癬性關節炎，TxGNN 預測其可能對罕見骨骼發育異常症候群有治療潛力，但缺乏臨床證據，屬於純預測階段 (L5)。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Leflunomide (來氟米特) |
| DrugBank ID | DB01097 |
| 台灣商品名 | 艾炎寧、雅努麻、希關炎等 |
| 原核准適應症 | 類風濕性關節炎、乾癬性關節炎 |
| 預測新適應症 | rheumatoid arthritis、brachydactyly-syndactyly syndrome |
| TxGNN 預測分數 | 0.999 |
| 證據等級 | **L5** (僅預測) |
| 臨床試驗 | 無 |
| PubMed 文獻 | 無 |

---


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. brachydactyly-syndactyly syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.93%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

### 為什麼這個預測合理？

### 機轉推論

1. **DHODH 抑制作用**：Leflunomide 透過抑制二氫乳清酸脫氫酶 (DHODH) 減少嘧啶合成，進而抑制淋巴細胞增殖。這種抑制細胞增殖的機轉在某些發育異常疾病中可能有理論上的應用。

2. **抗發炎與免疫調節**：作為 DMARD (疾病修飾抗風濕藥)，其免疫調節特性可能對某些具有發炎成分的遺傳性疾病有輔助作用。

3. **知識圖譜連結**：TxGNN 可能識別到 Leflunomide 的作用標靶與骨骼發育相關基因網絡的關聯，但這需要進一步驗證。

### 預測限制

- 預測的適應症 (短指併指症候群、眼缺損-根莖骨發育不全症候群) 為極罕見的先天性發育異常
- 這些疾病的病理機轉與 Leflunomide 的作用機轉缺乏直接關聯
- 先天性骨骼發育異常通常難以藥物治療逆轉

### 臨床試驗

**無相關臨床試驗**

在 ClinicalTrials.gov 及 ICTRP 資料庫中，未發現 Leflunomide 用於預測適應症的臨床試驗。

### 相關文獻

**無相關 PubMed 文獻**

在 PubMed 資料庫中，未找到 Leflunomide 與短指併指症候群或眼缺損-根莖骨發育不全症候群相關的文獻。

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. colobomatous microphthalmia-rhizomelic dysplasia syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.93%</span>
</summary>
<div class="indication-content">

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

### 許可證狀態

| 許可證字號 | 商品名 | 劑型 | 持證商 | 狀態 | 效期 |
|-----------|--------|------|--------|------|------|
| 衛署藥輸字第023615號 | 艾炎寧膜衣錠10毫克 | 膜衣錠 | 賽諾菲 | 有效 | 2027/12/30 |
| 衛部藥輸字第027175號 | 希關炎膜衣錠10毫克 | 膜衣錠 | 西海生技 | 有效 | 2027/06/06 |
| 衛部藥輸字第027176號 | 希關炎膜衣錠20毫克 | 膜衣錠 | 西海生技 | 有效 | 2027/06/06 |
| 衛部藥輸字第027098號 | 希關炎膜衣錠100毫克 | 膜衣錠 | 西海生技 | 有效 | 2027/03/28 |
| 衛署藥製字第045971號 | 美時 雅努麻錠20毫克 | 錠劑 | 美時化學製藥 | 有效 | 2028/12/05 |
| 衛署藥製字第048558號 | 美時 雅努麻錠10毫克 | 錠劑 | 美時化學製藥 | 有效 | 2027/01/26 |
| 衛部藥輸字第027234號 | 耐福諾邁 | 粉劑 | 漢旭 | 有效 | 2027/08/14 |

### 核准適應症

- 治療成人類風濕性關節炎，減緩類風濕病程對關節所造成之結構性損害 (DMARD)
- 治療具活動性的成人乾癬性關節炎

---

## 安全性考量

### 藥物交互作用 (DDI)

#### 嚴重 (Major) 交互作用

| 併用藥物 | 影響說明 |
|---------|---------|
| 類固醇類 (Hydrocortisone, Prednisone, Dexamethasone, Betamethasone, Triamcinolone 等) | 增加肝毒性風險 |
| Statins (Rosuvastatin, Simvastatin) | 增加肝毒性與肌病變風險 |
| Acetylsalicylic acid | 增加出血風險 |
| Clarithromycin | 藥物交互作用增強 |
| Minocycline | 增加肝毒性風險 |
| Levofloxacin | 增加肝毒性風險 |
| Sulfasalazine | 增加肝毒性風險 |
| Ethanol | 顯著增加肝毒性風險 |
| Pioglitazone, Rosiglitazone, Troglitazone | 增加肝毒性風險 |
| Eltrombopag | 增加肝毒性風險 |
| Fostamatinib | 增加肝毒性風險 |

#### 中度 (Moderate) 交互作用

| 併用藥物 | 影響說明 |
|---------|---------|
| Warfarin, Dicoumarol | 增強抗凝血效果 |
| Metronidazole, Tinidazole | 藥物代謝影響 |
| 磺脲類降血糖藥 (Glimepiride, Glipizide, Glyburide 等) | 血糖控制影響 |
| 活性碳 | 降低 Leflunomide 吸收 |

### 重要警語

1. **肝毒性**：Leflunomide 具有肝毒性風險，需定期監測肝功能
2. **免疫抑制**：可能增加感染風險
3. **致畸胎性**：**絕對禁用於孕婦**，育齡婦女需有效避孕
4. **洗脫程序**：停藥後藥物代謝物在體內停留時間長，必要時需進行 cholestyramine 洗脫程序
5. **骨髓抑制**：可能導致白血球減少、血小板減少

### 特殊族群

- **孕婦**：**禁用** - Category X
- **哺乳婦女**：**禁用**
- **肝功能不全**：禁用
- **腎功能不全**：無需調整劑量，但需謹慎監測
- **老年人**：需謹慎使用，監測肝腎功能

---

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**酒精 (alcohol)** 🟡 Moderate
- 影響：The consumption of alcohol during therapy with leflunomide may potentiate the risk of liver injury.
- 建議：Patients should be advised to avoid excessive alcohol use during leflunomide treatment.

### 藥物-草藥交互作用 (DHI)

**紫錐花** 🟡 Moderate
- 影響：紫錐花可能影響免疫調節藥物療效
- 建議：避免併用


## 結論與下一步

### 藥師評估

| 評估項目 | 結論 |
|---------|------|
| 預測可信度 | 低 - 缺乏支持證據 |
| 機轉合理性 | 低 - 理論連結薄弱 |
| 臨床可行性 | 極低 - 先天性疾病難以藥物治療 |
| 建議優先度 | 不建議優先追蹤 |

### 建議

1. **不建議臨床探索**：
   - 預測的適應症為先天性發育異常，病理機轉與藥物作用不符
   - Leflunomide 具有顯著肝毒性與致畸胎性，對罕見疾病的風險效益比不佳

2. **現有適應症提醒**：
   - Leflunomide 是類風濕性關節炎的有效 DMARD
   - 使用時需嚴格監測肝功能與血球計數
   - 育齡婦女使用前必須確認未懷孕並使用有效避孕

3. **持續監測**：
   - 關注 Leflunomide 在其他免疫相關疾病的研究進展

### 證據等級說明

**L5 (僅預測)**：此預測僅基於 TxGNN 知識圖譜分析，缺乏任何臨床試驗或文獻支持。考量藥物的安全性特性與預測適應症的性質，不建議進一步探索。

---

*本筆記由 TxGNN 老藥新用預測系統生成，僅供研究參考，不構成醫療建議。*

*生成日期：2026-02-11*


---

## 相關藥物報告

- [Sodium Carbonate]({{ "/drugs/sodium_carbonate/" | relative_url }}) - 證據等級 L5
- [Amorolfine]({{ "/drugs/amorolfine/" | relative_url }}) - 證據等級 L5
- [Cobicistat]({{ "/drugs/cobicistat/" | relative_url }}) - 證據等級 L5
- [Vigabatrin]({{ "/drugs/vigabatrin/" | relative_url }}) - 證據等級 L5
- [Aluminum Chloride]({{ "/drugs/aluminum_chloride/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Leflunomide老藥新用驗證報告. https://twtxgnn.yao.care/drugs/leflunomide/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_leflunomide,
  title = {Leflunomide老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/leflunomide/}
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
