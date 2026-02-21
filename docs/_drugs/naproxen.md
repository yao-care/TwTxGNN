---
layout: default
title: Naproxen
description: "Naproxen 的老藥新用潛力分析。模型預測等級 L5，包含 4 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 4
---

# Naproxen

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>4</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Naproxen：從 消炎鎮痛 到 罕見骨骼發育症候群

## 一句話總結

<p class="key-answer" data-question="Naproxen 可以用於治療什麼新適應症？">
Naproxen（那普洛辛）是一種非類固醇抗發炎藥物（NSAID），廣泛用於治療關節炎、疼痛和發炎。TxGNN 模型預測它對數種罕見骨骼發育異常疾病有潛在關聯，包括 **brachydactyly-syndactyly syndrome**，但無任何臨床或文獻證據支持。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨關節炎、類風濕性關節炎、急性痛風、原發性經痛、輕中度疼痛 |
| 預測新適應症 | osteoarthritis susceptibility、rheumatoid arthritis、brachydactyly-syndactyly syndrome、osteoarthritis |
| TxGNN 預測分數 | 99.35% (brachydactyly-syndactyly syndrome) |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 167 張 |
| 建議決策 | Hold |

## 為什麼這個預測不合理？

Naproxen 通過抑制環氧化酶（COX-1 和 COX-2）減少前列腺素合成，發揮抗發炎、鎮痛和解熱作用。

**預測適應症問題：**
- Brachydactyly-syndactyly syndrome 等是先天性骨骼發育異常
- 這些疾病為遺傳性疾病，非發炎介導
- NSAID 類藥物無法改變骨骼發育的遺傳基礎
- 缺乏任何藥理學機轉支持

此預測極可能是 TxGNN 模型的偽陽性結果，可能源於知識圖譜中骨骼相關術語的共現。

## 臨床試驗證據

無相關臨床試驗登記。

## 文獻證據

無相關文獻。

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028724號 | 那普洛辛 | 原料藥 | 消炎鎮痛劑 |
| 衛署藥製字第019620號 | 那普洛先錠 | 錠劑 | 風濕關節炎、脊椎炎、腱鞘炎之消炎鎮痛 |
| 衛署藥製字第034014號 | 衛達拿炎錠375毫克 | 錠劑 | 骨關節炎、類風濕性關節炎、急性痛風、原發性經痛 |

## 安全性考量

**藥物交互作用（中度）：**
- Famotidine, Ranitidine：H2 阻斷劑可能與 NSAID 交互作用
- Metformin：可能增加乳酸酸中毒風險
- Aspirin：增加胃腸道出血風險
- Corticosteroids（Hydrocortisone, Dexamethasone, Betamethasone 等）：增加胃腸道潰瘍和出血風險
- Esomeprazole, Lansoprazole：胃酸抑制劑

**主要警告：**
- 心血管事件風險（心肌梗塞、中風）
- 胃腸道出血和潰瘍
- 腎功能損害
- 過敏反應

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**酒精 (alcohol)** 🟡 Moderate
- 影響：The concurrent use of aspirin or nonsteroidal anti-inflammatory drugs (NSAIDs) and ethanol may lead to gastrointestinal (GI) blood loss.  The mechanism may be due to a combined local effect as well as...
- 建議：Patients should be counseled on this potential interaction and advised to refrain from alcohol consumption while taking aspirin or NSAIDs.



### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**心臟衰竭 (Heart Failure)** 🟡 Moderate
- Anaprox and Anaprox DS (brands of naproxen sodium) contain 25 mg and 50 mg of sodium per tablet (approximately 1 mEq/250 mg naproxen), respectively, and Naprosyn suspension contains 39 mg per teaspoonful (approximately 1.5 mEq/125 mg naproxen).  The ...

**Anemia** 🟡 Moderate
- Anemia has been reported in patients treated with nonsteroidal anti-inflammatory drugs (NSAIDs).  This may be due to fluid retention, occult/gross blood loss, or an incompletely described effect on erythropoiesis.  Hemoglobin or hematocrit should be ...

**心臟衰竭 (Heart Failure)** 🟡 Moderate
- Fluid retention and edema have been observed in patients treated with nonsteroidal anti-inflammatory drugs (NSAIDs), including some topical formulations.  These drugs should be avoided in patients with severe heart failure unless the benefits are exp...

**肝臟疾病 (Liver Diseases)** 🟡 Moderate
- Borderline elevations of 1 or more liver tests may occur in up to 15% of patients treated with nonsteroidal anti-inflammatory drugs (NSAIDs).  These laboratory abnormalities may progress, remain unchanged, or regress with continuing therapy.  Elevati...

**Hyperkalemia** 🟡 Moderate
- Increases in serum potassium concentration (including hyperkalemia) have been reported with use of nonsteroidal anti-inflammatory drugs (NSAIDs), even in some patients without renal impairment.  In patients with normal renal function, these effects h...

*另有 8 項疾病注意事項，詳見 [DDInter 2.0](https://ddinter2.scbdd.com/)*

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測的適應症（短指併指症候群等）是罕見的先天性遺傳疾病，與 NSAID 的抗發炎機轉完全無關。這些骨骼發育異常是在胚胎發育期形成的結構缺陷，非發炎過程所致，因此 naproxen 不可能對其有治療效果。此預測應視為模型的偽陽性結果。

**若要推進需要：**
- 不建議進一步探索
- 此預測缺乏任何科學依據


---

## 相關藥物報告

- [Sulfamerazine]({{ "/drugs/sulfamerazine/" | relative_url }}) - 證據等級 L5
- [Pemetrexed]({{ "/drugs/pemetrexed/" | relative_url }}) - 證據等級 L5
- [Dehydrocholic Acid]({{ "/drugs/dehydrocholic_acid/" | relative_url }}) - 證據等級 L5
- [Pentoxifylline]({{ "/drugs/pentoxifylline/" | relative_url }}) - 證據等級 L5
- [Bevacizumab]({{ "/drugs/bevacizumab/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Naproxen老藥新用驗證報告. https://twtxgnn.yao.care/drugs/naproxen/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_naproxen,
  title = {Naproxen老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/naproxen/}
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
