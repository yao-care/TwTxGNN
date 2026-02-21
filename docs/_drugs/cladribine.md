---
layout: default
title: Cladribine
description: "Cladribine 的老藥新用潛力分析。模型預測等級 L5，包含 7 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 7
---

# Cladribine

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>7</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cladribine 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Cladribine 可以用於治療什麼新適應症？">
Cladribine 是一種核苷類似物抗腫瘤藥，目前核准用於多發性硬化症及毛髮狀細胞白血病，TxGNN 預測其可能對橫紋肌肉瘤及肝臟肉瘤等罕見腫瘤有療效，但目前缺乏臨床證據支持。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Cladribine (克拉屈濱) |
| DrugBank ID | DB00242 |
| 台灣商品名 | 瑪威克錠 10 毫克 (Mavenclad)、祿斯得停注射劑 (Leustatin) |
| 原核准適應症 | 復發型多發性硬化症、毛髮狀細胞白血病 |
| 預測新適應症 | parameningeal embryonal rhabdomyosarcoma、botryoid-type embryonal rhabdomyosarcoma of the vagina、embryonal extrahepatic bile duct rhabdomyosarcoma、prostate embryonal rhabdomyosarcoma、extrahepatic bile duct rhabdomyosarcoma、rhabdomyosarcoma (disease)、liver sarcoma |
| 最高預測分數 | 0.998 (parameningeal embryonal rhabdomyosarcoma) |
| 證據等級 | L5 (僅預測) |

---

## 為什麼這個預測合理

Cladribine 是一種嘌呤核苷類似物，具有強效的抗增殖及免疫調節作用。其作用機轉包括：

1. **DNA 合成抑制**：Cladribine 進入細胞後被磷酸化為活性代謝物，干擾 DNA 合成與修復
2. **淋巴細胞毒性**：選擇性地對淋巴細胞產生細胞毒性，這也是其用於治療毛髮狀細胞白血病的基礎
3. **廣譜抗腫瘤活性**：作為核苷類似物，理論上對快速分裂的腫瘤細胞有抑制作用

橫紋肌肉瘤屬於軟組織肉瘤，傳統上使用 VAC (vincristine, actinomycin D, cyclophosphamide) 方案治療。知識圖譜預測 cladribine 可能對此類腫瘤有效，可能基於其與其他核苷類抗腫瘤藥物的結構相似性。

---

## 臨床試驗證據

目前 **無** 針對 cladribine 用於橫紋肌肉瘤或肝臟肉瘤的臨床試驗登記。

---

## 文獻證據

| PMID | 標題 | 相關性 |
|------|------|--------|
| 15241520 | Smoldering systemic mastocytosis - Successful therapy with cladribine | 間接證據：Cladribine 對肥大細胞增生症有效，顯示其對某些造血系統腫瘤的活性 |

文獻中關於 cladribine 用於肝臟肉瘤的報告實際上是關於全身性肥大細胞增生症的個案，與預測適應症的直接相關性有限。

---

## 台灣上市資訊

| 許可證字號 | 商品名 | 適應症 | 劑型 | 許可證持有者 | 狀態 |
|------------|--------|--------|------|--------------|------|
| 衛部罕藥輸字第000058號 | 瑪威克錠 10 毫克 | 復發型多發性硬化症 | 錠劑 | 台灣默克股份有限公司 | 有效 |
| 衛署藥輸字第021992號 | 祿斯得停注射劑 | 毛髮狀細胞白血病 | 注射劑 | 裕利股份有限公司 | 有效 |
| 衛部藥製字第061006號 | 台灣神隆克拉屈濱 | 復發型多發性硬化症 | 原料藥 | 台灣神隆股份有限公司 | 有效 |

---

## 安全性考量

### 重要藥物交互作用 (Major)

| 交互作用藥物 | 嚴重程度 | 臨床意義 |
|--------------|----------|----------|
| 皮質類固醇 (Hydrocortisone, Prednisolone, Dexamethasone 等) | Major | 增加免疫抑制風險 |
| 免疫抑制劑 (Tacrolimus, Azathioprine) | Major | 加重骨髓抑制 |
| 抗病毒藥 (Zidovudine, Ganciclovir) | Major | 骨髓毒性疊加 |
| 其他化療藥物 (Gemcitabine, Mercaptopurine) | Major | 增加血液學毒性 |
| 放射性藥物 | Major | 加重骨髓抑制 |

### 主要警語

- 嚴重骨髓抑制：可能導致感染、出血風險增加
- 免疫抑制：長期淋巴細胞減少，增加機會性感染風險
- 致畸性：孕婦禁用，育齡婦女需有效避孕

---


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**肝臟疾病 (Liver Diseases)** 🟡 Moderate
- The pharmacokinetic disposition of cladribine has not be fully assessed. The effect of hepatic impairment on the elimination of cladribine is not known.  Therapy with cladribine should be administered cautiously in patient with existing or predisposi...

**腎臟疾病 (Kidney Diseases)** 🟡 Moderate
- The effect of renal impairment on the elimination of cladribine has not been assessed in humans.  Renal toxicity such as acidosis, anuria, elevated serum creatinine has been reported with doses four to nine times the recommended dosage of cladribine ...

**Infections** 🟢 Minor
- Because of their cytotoxic effects on rapidly proliferating tissues, antineoplastic agents frequently can, to varying extent, induce myelosuppression.  The use of these drugs may be contraindicated in patients with known infectious diseases.  All pat...

**Bone Marrow Failure Disorders** 🟢 Minor
- Cladribine induces myelosuppression, primarily affecting lymphocytes and monocytes, however, neutropenia, anemia, and thrombocytopenia have been reported during cladribine therapy.  Myelosuppressive effects are most notable the first month following ...

**Nervous System Diseases** 🟢 Minor
- Severe unspecified neurological toxicity has been reported rarely during cladribine therapy administered at therapeutic doses.  Serious neurological toxicity such as irreversible paraparesis and quadriparesis has been reported in patients receiving f...

## 結論與下一步

### 預測評估

| 評估項目 | 結果 |
|----------|------|
| 機轉合理性 | 中等 - 核苷類似物對快速分裂細胞有廣譜活性 |
| 臨床證據 | 無 |
| 文獻支持 | 極弱 |
| 整體證據等級 | **L5 (僅預測)** |

### 建議

1. **不建議臨床使用**：目前無足夠證據支持 cladribine 用於橫紋肌肉瘤或肝臟肉瘤
2. **前臨床研究需求**：若有興趣探索此預測，建議先進行體外細胞株及動物模型研究
3. **持續監測文獻**：關注是否有新的臨床或基礎研究發表

---

*本筆記僅供研究參考，不構成醫療建議。任何用藥決策應諮詢專業醫療人員。*

*最後更新：2026-02-11*


---

## 相關藥物報告

- [Tenofovir Alafenamide]({{ "/drugs/tenofovir_alafenamide/" | relative_url }}) - 證據等級 L5
- [Felodipine]({{ "/drugs/felodipine/" | relative_url }}) - 證據等級 L5
- [Lidocaine]({{ "/drugs/lidocaine/" | relative_url }}) - 證據等級 L5
- [Iodixanol]({{ "/drugs/iodixanol/" | relative_url }}) - 證據等級 L5
- [Potassium Iodide]({{ "/drugs/potassium_iodide/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Cladribine老藥新用驗證報告. https://twtxgnn.yao.care/drugs/cladribine/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_cladribine,
  title = {Cladribine老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/cladribine/}
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
