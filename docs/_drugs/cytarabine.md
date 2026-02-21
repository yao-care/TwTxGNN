---
layout: default
title: Cytarabine
description: "Cytarabine 的老藥新用潛力分析。模型預測等級 L5，包含 9 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 9
---

# Cytarabine

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>9</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cytarabine 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Cytarabine 可以用於治療什麼新適應症？">
Cytarabine (Ara-C) 是治療急性白血病的核心化療藥物，TxGNN 預測其對小細胞肺癌及原發性肺淋巴瘤有療效，這些預測有歷史臨床研究支持，但療效有限且非現代標準治療。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Cytarabine (阿糖胞苷, Ara-C) |
| DrugBank ID | DB00987 |
| 台灣商品名 | 複方製劑中的成分，如 Midostaurin 併用方案 |
| 原核准適應症 | 急性骨髓性白血病 (AML)、慢性淋巴球性白血病 (CLL)、與其他藥物併用 |
| 預測新適應症 | small cell lung carcinoma、primary pulmonary lymphoma、well-differentiated fetal adenocarcinoma of the lung、pulmonary blastoma、myeloid leukemia、upper aerodigestive tract neoplasm、ganglioneuroblastoma (disease)、vertebral anomalies and variable endocrine and T-cell dysfunction、腹膜後腫瘤 |
| 最高預測分數 | 0.998 (small cell lung carcinoma) |
| 證據等級 | L3 (歷史臨床研究，非現代標準) |

---

## 為什麼這個預測合理

Cytarabine 的抗腫瘤機轉支持其對多種惡性腫瘤的潛在活性：

1. **核苷類似物**：Cytarabine 是胞嘧啶核苷的類似物，干擾 DNA 合成
2. **S 期特異性**：主要作用於 DNA 合成期，對快速分裂的腫瘤細胞有選擇性
3. **廣譜活性**：歷史上曾用於多種惡性腫瘤的探索性治療

### 預測適應症分析

| 預測適應症 | 機轉合理性 | 歷史研究 |
|------------|------------|----------|
| 小細胞肺癌 | 高 - SCLC 分裂速度快 | 1970-1990 年代有多項研究 |
| 原發性肺淋巴瘤 | 高 - 淋巴瘤對 Ara-C 敏感 | 用於 CNS 淋巴瘤及復發性淋巴瘤 |

---

## 臨床試驗證據

### 小細胞肺癌相關試驗

| 試驗編號 | 標題 | 階段 | 狀態 | 相關性 |
|----------|------|------|------|--------|
| NCT03507244 | 鞘內 Pemetrexed 治療腦膜轉移 | Phase 1/2 | 已完成 | 提及 cytarabine 作為對照 |
| NCT03101579 | 鞘內 Pemetrexed 治療 NSCLC 腦膜轉移 | Phase 1 | 已完成 | Cytarabine 作為傳統鞘內治療比較 |

### 淋巴瘤相關試驗

| 試驗編號 | 標題 | 階段 | 狀態 | 發現 |
|----------|------|------|------|------|
| NCT00345865 | 淋巴瘤自體移植 | Phase 2 | 已完成 | Cytarabine 為條件療法一部分 |
| NCT00452374 | Oxaliplatin + Fludarabine + Ara-C + Rituximab | Phase 1/2 | 已完成 | 用於 Richter 轉化及 CLL |

---

## 文獻證據

### 小細胞肺癌

| PMID | 標題 | 年份 | 主要發現 |
|------|------|------|----------|
| 232239 | Combination radiotherapy and chemotherapy for SCLC | 1979 | Ara-C 併用方案有效但無優勢 |
| 3030547 | High-dose cytarabine in SCLC | 1987 | 高劑量 Ara-C 單獨使用反應有限 |
| 6095640 | Intensive cytosine arabinoside therapy in SCLC | 1984 | Ara-C 加入 CAV 方案無額外益處 |
| 2841844 | VP-16 and Ara-C for relapsed SCLC | 1988 | 復發 SCLC 治療，毒性高但活性有限 |

**文獻結論**：1980 年代的研究顯示 cytarabine 對 SCLC 有一定活性，但並未優於當時的標準方案，且毒性顯著。

### 原發性 CNS 淋巴瘤

| PMID | 標題 | 年份 | 主要發現 |
|------|------|------|----------|
| 12860951 | Chemotherapy for primary CNS lymphoma in elderly | 2003 | MTX + Ara-C 對老年患者有效 |
| 12241119 | HD-MTX and Ara-C for primary CNS lymphoma | 2002 | 100% 反應率，86% CR |
| 15957966 | Management of leptomeningeal malignancy | 2005 | Ara-C 為腦膜癌症的標準鞘內治療 |

**文獻結論**：Cytarabine（特別是高劑量或鞘內給藥）是 CNS 淋巴瘤治療的重要成分。

---

## 台灣上市資訊

Cytarabine 在台灣主要以下列形式使用：

| 用途 | 藥品 | 說明 |
|------|------|------|
| AML 前導治療 | Midostaurin (彌多妥) 併用 | FLT3 突變陽性 AML |
| AML 鞏固治療 | 高劑量 Ara-C | 標準方案 |
| CLL 治療 | Venetoclax 併用低劑量 Ara-C | 不適合強化化療的患者 |

---

## 安全性考量

### 主要毒性

| 毒性類型 | 表現 | 管理 |
|----------|------|------|
| 骨髓抑制 | 嚴重嗜中性球低下、血小板低下 | 監測 CBC，預防性使用 G-CSF |
| 感染 | 機會性感染風險高 | 預防性抗生素、抗黴菌藥 |
| 神經毒性 | 高劑量時可能出現小腦症狀 | 監測神經功能，調整劑量 |
| 消化道 | 黏膜炎、噁心嘔吐 | 止吐藥、口腔護理 |
| Ara-C 症候群 | 發燒、肌痛、骨痛、皮疹 | 類固醇預防 |

### 藥物交互作用注意

- **其他骨髓抑制藥物**：毒性疊加
- **Digoxin**：可能降低 digoxin 吸收
- **Flucytosine**：競爭性拮抗

---


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**肝臟疾病 (Liver Diseases)** 🟡 Moderate
- Cytarabine is extensively metabolized by the liver.  Patients with impaired hepatic function may be at increased risk for CNS toxicity during high dose cytarabine therapy.  Therapy with cytarabine should be administered cautiously and the dosages mod...

**腎臟疾病 (Kidney Diseases)** 🟡 Moderate
- Cytarabine is primarily eliminated by the kidney.  Patients with impaired renal function may be at increased risk for CNS toxicity during high dose cytarabine therapy.  Therapy with cytarabine should be administered cautiously and the dosages modifie...

**Infections** 🟢 Minor
- Because of their cytotoxic effects on rapidly proliferating tissues, antineoplastic agents frequently can, to varying extent, induce myelosuppression.  The use of these drugs may be contraindicated in patients with known infectious diseases.  All pat...

**Bone Marrow Failure Disorders** 🟢 Minor
- Cytarabine is a potent bone marrow suppressant.  Therapy with cytarabine should be administered cautiously in patients whose bone marrow reserve may be severely depressed by prior chemotherapy or whose marrow function is recovering from previous cyto...

## 結論與下一步

### 預測評估

| 評估項目 | 小細胞肺癌 | 原發性肺淋巴瘤 |
|----------|------------|----------------|
| 機轉合理性 | 高 | 高 |
| 臨床證據 | L3 (歷史研究) | L2 (CNS 淋巴瘤有 RCT) |
| 文獻支持 | 中等但過時 | 較強（用於 CNS 淋巴瘤） |

### 臨床意義評估

#### 小細胞肺癌

- **不建議臨床使用**：現代 SCLC 治療已不包含 cytarabine
- **現代標準**：Cisplatin/Carboplatin + Etoposide，免疫治療 (如 atezolizumab)
- **歷史價值**：反映了知識圖譜能捕捉歷史用藥關聯

#### 原發性肺淋巴瘤/CNS 淋巴瘤

- **有臨床價值**：高劑量 Ara-C 是 CNS 淋巴瘤治療的重要成分
- **現代方案**：通常與 MTX、rituximab 併用
- **注意事項**：「原發性肺淋巴瘤」較罕見，治療通常參考全身性淋巴瘤方案

### 建議

1. **SCLC**：不建議使用 cytarabine，應依循現代治療指引
2. **CNS 淋巴瘤**：高劑量 cytarabine 仍有其角色，需由血液腫瘤專科評估
3. **腦膜轉移**：鞘內 cytarabine 或 liposomal cytarabine 為可選方案

### 整體證據等級

**L3 (觀察性研究/歷史臨床經驗)** - 有文獻支持但非現代標準治療

---

*本筆記僅供研究參考，不構成醫療建議。任何用藥決策應諮詢專業醫療人員。*

*最後更新：2026-02-11*


---

## 相關藥物報告

- [Raloxifene]({{ "/drugs/raloxifene/" | relative_url }}) - 證據等級 L5
- [Brivaracetam]({{ "/drugs/brivaracetam/" | relative_url }}) - 證據等級 L5
- [Flunitrazepam]({{ "/drugs/flunitrazepam/" | relative_url }}) - 證據等級 L5
- [Clomipramine]({{ "/drugs/clomipramine/" | relative_url }}) - 證據等級 L5
- [Tenofovir Alafenamide]({{ "/drugs/tenofovir_alafenamide/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Cytarabine老藥新用驗證報告. https://twtxgnn.yao.care/drugs/cytarabine/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_cytarabine,
  title = {Cytarabine老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/cytarabine/}
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
