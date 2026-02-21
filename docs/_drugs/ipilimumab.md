---
layout: default
title: Ipilimumab
description: "Ipilimumab 的老藥新用潛力分析。模型預測等級 L5，包含 2 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L1
indication_count: 2
---

# Ipilimumab

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>2</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ipilimumab (易乳莫單抗) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Ipilimumab 可以用於治療什麼新適應症？">
易乳莫單抗是一種抗 CTLA-4 免疫檢查點抑制劑，TxGNN 預測其對非皮膚黑色素瘤有療效，這項預測獲得大量臨床試驗支持，展現了極高的轉譯價值。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物學名 | Ipilimumab |
| 台灣商品名 | 益伏注射劑 5 毫克/毫升 (YERVOY) |
| DrugBank ID | DB06186 |
| 原核准適應症 | 無法切除或轉移性黑色素瘤、腎細胞癌、NSCLC、肝細胞癌、大腸直腸癌、食道癌等（多與 nivolumab 併用） |
| 預測新適應症 | metastatic melanoma、choroideremia |
| 最高證據等級 | L1/L2 (多項 RCT 研究) |
| 台灣上市狀態 | 有效許可證 |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. choroideremia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.06%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

Ipilimumab 透過阻斷 CTLA-4 來增強 T 細胞活化，解除免疫系統對腫瘤的抑制：

1. **非皮膚黑色素瘤** (TxGNN Score: 0.990, Rank: 16733)：
   - 包括黏膜黑色素瘤、眼部黑色素瘤（葡萄膜黑色素瘤）等
   - 這些亞型較皮膚黑色素瘤少見，但具有相似的免疫原性
   - Ipilimumab（特別是與 nivolumab 併用）已在這些亞型中顯示療效

2. **脈絡膜無虹膜症 (Choroideremia)** (TxGNN Score: 0.991, Rank: 16090)：
   - 這是一種遺傳性視網膜退化疾病，非腫瘤性
   - 此預測的機轉關聯不明，可能為偽陽性

### 臨床試驗

針對「非皮膚黑色素瘤」，檢索到超過 **40 項相關臨床試驗**：

### 相關文獻

### 非皮膚黑色素瘤相關（5+ 篇文獻）

1. **Alexander M et al. (2014)** - Medical Journal of Australia
   - 評估 ipilimumab 用於皮膚、葡萄膜和黏膜黑色素瘤的療效
   - 包含不同黑色素瘤亞型的反應率分析

2. **Trinh VA et al. (2018)** - Discovery Medicine
   - 抗 PD-1 單抗治療晚期黑色素瘤的臨床更新
   - 討論非皮膚亞型和腦轉移的治療策略

3. **Woo TE et al. (2023)** - Current Oncology
   - 比較年輕 vs 年長患者使用 ICI 單藥或併用的療效
   - 涵蓋多種黑色素瘤亞型

4. **D'Aniello C et al. (2018)** - Current Cancer Drug Targets
   - 黑色素瘤輔助治療綜述
   - 討論 ipilimumab 在不同亞型中的應用

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. non-cutaneous melanoma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.02%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.02%
- **證據等級**：L1（多個大型 RCT 支持）

### 臨床證據

**臨床試驗**：共 50 項

- 試驗階段分布：EARLY_PHASE1: 1項, N/A: 4項, NA: 4項, PHASE1: 9項, PHASE1, PHASE2: 5項, PHASE2: 23項, PHASE2, PHASE3: 1項, PHASE3: 2項, PHASE4: 1項

**相關文獻**：共 5 篇


</div>
</details>


## 台灣上市資訊

**有效許可證：**

| 許可證字號 | 商品名 | 許可證持有者 | 效期 |
|------------|--------|--------------|------|
| 衛部菌疫輸字第000958號 | 益伏注射劑 5 毫克/毫升 | 台灣必治妥施貴寶 | 2029/08/18 |

**核准適應症（與 nivolumab 併用）：**
1. 無法切除或轉移性黑色素瘤（12 歲以上）
2. 晚期腎細胞癌（中度/重度風險）
3. MSI-H/dMMR 轉移性大腸直腸癌
4. 肝細胞癌（第一線和 sorafenib 失敗後）
5. 轉移性或復發性非小細胞肺癌
6. 惡性肋膜間皮瘤
7. 食道鱗狀細胞癌

## 安全性考量

### 免疫相關不良事件 (irAEs)

Ipilimumab + Nivolumab 併用療法的 Grade 3-4 irAEs 發生率約 50-60%：

| 不良反應類型 | 常見表現 | 管理重點 |
|--------------|----------|----------|
| 腸炎 | 腹瀉、血便 | 可能需 corticosteroids |
| 肝炎 | 轉氨酶升高 | 監測肝功能 |
| 皮膚炎 | 皮疹、搔癢 | 外用/全身性 steroids |
| 內分泌病變 | 甲狀腺/腎上腺功能異常 | 荷爾蒙補充 |
| 肺炎 | 呼吸困難、咳嗽 | 停藥並給予 steroids |
| 腸穿孔 | 罕見但致命 | 緊急外科介入 |

### 主要藥物交互作用

| 交互作用藥物 | 嚴重程度 | 說明 |
|--------------|----------|------|
| Corticosteroids | Moderate | 可能降低免疫治療效果 |
| Hydrocortisone | Moderate | 用於 irAEs 管理時需權衡 |
| Dexamethasone | Moderate | 同上 |
| 其他免疫抑制劑 | Moderate | 可能影響療效 |

### 特殊族群
- **肝功能不全**：輕度肝功能不全不需調整劑量
- **腎功能不全**：不需調整劑量
- **孕婦**：禁用，可能致畸
- **老年患者**：毒性可能增加，需密切監測


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Hepatic Insufficiency** 🟡 Moderate
- 可能有嚴重不良反應。

**Pneumonia** 🟡 Moderate
- 必要時應停止治療。

**Colitis** 🟢 Minor
- 風險包括：感染。可能有致命風險。必要時應停止治療。

**Dermatitis** 🟢 Minor
- 出現症狀時應考慮停藥。

**Endocrine System Diseases** 🟢 Minor
- 需定期監測。可能危及生命。出現症狀時應考慮停藥。

**Hepatitis** 🟢 Minor
- 需定期監測。可能有致命風險。出現症狀時應考慮停藥。

**Graft vs Host Disease** 🟢 Minor
- 需密切監測。可能有致命風險。

**Immune System Diseases** 🟢 Minor
- 需定期監測。可能有致命風險。出現症狀時應考慮停藥。

**Eye Diseases** 🟢 Minor
- 需定期監測。可能有致命風險。出現症狀時應考慮停藥。

## 結論與下一步

### 預測評估結論

Ipilimumab 對非皮膚黑色素瘤的預測是**高度有價值的發現**：

1. **葡萄膜黑色素瘤**：已有 Phase 2 試驗數據，顯示與 nivolumab 併用的療效
2. **黏膜黑色素瘤**：多項進行中的臨床試驗正在評估
3. **脈絡膜無虹膜症**：此預測缺乏機轉支持，可能為偽陽性

### 證據等級總結

| 預測適應症 | TxGNN Score | 證據等級 | 評估 |
|------------|-------------|----------|------|
| 非皮膚黑色素瘤 | 0.990 | **L1/L2** | 多項 RCT 支持，極高價值 |
| 脈絡膜無虹膜症 | 0.991 | L5 | 機轉不明，可能偽陽性 |

### 建議

1. **非皮膚黑色素瘤**：
   - **強烈建議持續追蹤臨床試驗進展**
   - 現有 Phase 2 試驗（NCT02626962）結果已發表
   - 可作為臨床決策參考
   - 部分亞型可能已可在仿單外使用條件下應用

2. **適應症擴增建議**：
   - 葡萄膜黑色素瘤和黏膜黑色素瘤的證據已相對成熟
   - 可考慮向 TFDA 提交適應症擴增申請

3. **臨床應用注意事項**：
   - 非皮膚黑色素瘤預後通常較皮膚型差
   - 需謹慎評估病患狀況和 irAEs 風險
   - 建議在有免疫治療經驗的中心使用

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 知識圖譜預測、ClinicalTrials.gov、PubMed、台灣 FDA*

---

## 相關藥物報告

- [Buprenorphine]({{ "/drugs/buprenorphine/" | relative_url }}) - 證據等級 L5
- [Famotidine]({{ "/drugs/famotidine/" | relative_url }}) - 證據等級 L5
- [Loteprednol Etabonate]({{ "/drugs/loteprednol_etabonate/" | relative_url }}) - 證據等級 L5
- [Ouabain]({{ "/drugs/ouabain/" | relative_url }}) - 證據等級 L5
- [Aspirin]({{ "/drugs/aspirin/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Ipilimumab老藥新用驗證報告. https://twtxgnn.yao.care/drugs/ipilimumab/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_ipilimumab,
  title = {Ipilimumab老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/ipilimumab/}
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
