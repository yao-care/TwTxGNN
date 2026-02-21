---
layout: default
title: Oxybutynin
description: "Oxybutynin 的老藥新用潛力分析。模型預測等級 L5，包含 3 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 3
---

# Oxybutynin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>3</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Oxybutynin 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Oxybutynin 可以用於治療什麼新適應症？">
Oxybutynin 為抗膽鹼藥物，原用於膀胱過動症，TxGNN 預測其可能對某些腸胃道疾病有潛在應用，但目前缺乏直接臨床證據支持。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品名稱 | Oxybutynin (羥布托尼/奧斯必得寧) |
| DrugBank ID | DB01062 |
| 台灣商品名 | 達多幫錠、安薄汗擦劑、歐保尿克貼布等 |
| 原適應症 | 膀胱過動症、原發性手掌多汗症、膀胱神經控制不適伴隨排尿症狀 |
| 預測新適應症 | cauda equina syndrome、overactive bladder (disease)、restless legs syndrome |
| 證據等級 | L5 (僅預測) |
| TxGNN 預測分數 | 高分預測 |

---

## 為什麼這個預測合理

### 機轉連結

1. **抗膽鹼作用**：Oxybutynin 為蕈毒鹼受體拮抗劑 (M1-M3)，可抑制平滑肌收縮。此機轉除了作用於膀胱逼尿肌外，理論上也可能影響腸胃道平滑肌。

2. **副交感神經抑制**：台灣 TFDA 核准適應症包含「副交感神經抑制藥」，顯示其對副交感神經系統的廣泛作用。

---

## 臨床試驗證據

目前無針對預測新適應症的已完成臨床試驗。

---

## 文獻證據

目前資料庫中無直接支持預測新適應症的 PubMed 文獻。

---

## 台灣上市資訊

| 許可證字號 | 商品名 | 劑型 | 適應症 | 狀態 |
|-----------|--------|------|--------|------|
| 衛部藥輸字第028910號 | 安薄汗擦劑 20% | 擦劑 | 原發性手掌多汗症 (12歲以上) | 有效 |
| 衛部藥輸字第028008號 | 歐保尿克快適貼布 | 貼布 | 膀胱過動症 | 有效 |
| 衛署藥製字第027361號 | 達多幫錠 5mg | 錠劑 | 膀胱神經控制不適伴隨排尿症狀 | 有效 |
| 衛署藥製字第035278號 | 優樂控錠 5mg | 錠劑 | 膀胱神經控制不適伴隨排尿症狀 | 有效 |
| 衛署藥製字第057414號 | 泌停緩釋錠 5mg | 緩釋錠 | 膀胱過動症 (急尿、頻尿、急迫性尿失禁) | 有效 |

---

## 安全性考量

### 重要警語

- **抗膽鹼副作用**：口乾、便秘、視力模糊、尿滯留、心跳加速
- **中樞神經系統影響**：可能造成認知功能障礙，特別是老年人
- **熱調節障礙**：減少出汗可能導致中暑風險增加

### 藥物交互作用 (Major)

| 交互作用藥物 | 嚴重程度 | 來源 |
|-------------|----------|------|
| Potassium chloride | Major | DDInter |

### 藥物交互作用 (Moderate)

| 交互作用藥物 | 說明 |
|-------------|------|
| Eluxadoline | 可能增強抗膽鹼作用 |
| Trospium | 抗膽鹼作用疊加 |
| Mepenzolate | 抗膽鹼作用疊加 |
| Methscopolamine | 抗膽鹼作用疊加 |
| Metoclopramide | 藥效可能相互拮抗 |
| Scopolamine | 抗膽鹼作用疊加 |
| Pramlintide | 可能影響胃排空 |

### 特殊族群

- **老年人**：增加認知障礙風險，應謹慎使用
- **閉角型青光眼患者**：禁忌使用
- **重症肌無力患者**：可能加重症狀
- **尿道阻塞患者**：可能加重尿滯留

---

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**酒精 (alcohol)** 🟡 Moderate
- 影響：Use of anticholinergic agents with alcohol may result in sufficient impairment of attention so as to render driving and operating machinery more hazardous.  In addition, the potential for abuse may be...
- 建議：Alcohol should generally be avoided during therapy with anticholinergic agents.  Patients should be counseled to avoid activities requiring mental alertness until they know how these agents affect the...



### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**Parkinson Disease** 🟡 Moderate
- Oxybutynin is associated with anticholinergic central nervous system (CNS) effects.  If a patient experiences anticholinergic CNS effects, dose reduction or drug discontinuation should be considered.  Oxybutynin should be used with caution in patient...

**Diabetic Neuropathies** 🟢 Minor
- Agents with anticholinergic activity can exacerbate many of the manifestations of autonomic neuropathy, including tachycardia, anhidrosis, bladder atony, obstipation, dry mouth and eyes, cycloplegia and blurring of vision, and sexual impotence in mal...

**Dysentery** 🟢 Minor
- The use of drugs with antiperistaltic activity (primarily antidiarrheal and antimuscarinic agents, but also antispasmodic agents such as dicyclomine or oxybutynin at high dosages) is contraindicated in patients with diarrhea due to pseudomembranous e...

**Glaucoma, Angle-Closure** 🟢 Minor
- The use of oxybutynin is contraindicated in patients with uncontrolled angle-closure (narrow angle) or narrow anterior chamber glaucoma.  Oxybutynin exerts anticholinergic activity (1/5 that of atropine) and can result in increased intraocular pressu...

**Intestinal Obstruction** 🟢 Minor
- The use of oxybutynin is contraindicated in patients with GI obstruction, ileus, atony, megacolon, toxic megacolon associated with ulcerative colitis, severe colitis, and obstructive uropathy.  Oxybutynin exerts direct antispasmodic effects on smooth...

*另有 1 項疾病注意事項，詳見 [DDInter 2.0](https://ddinter2.scbdd.com/)*

## 結論與下一步

### 整體評估

Oxybutynin 對預測新適應症的支持證據極為有限：

1. **證據等級最低 (L5)**：僅有 TxGNN 演算法預測，無臨床或前臨床證據
2. **機轉連結薄弱**：抗膽鹼作用可能有理論上的關聯，但缺乏驗證
3. **安全性考量**：已知副作用較多，特別是對老年人群

### 建議行動

- **需要更多基礎研究**：建立機轉假說的證據基礎
- **評估風險效益比**：考慮到已知副作用，需要強力的療效證據才值得進一步研究
- **優先使用現有適應症**：目前適合用於其已核准的膀胱相關適應症

---

*本報告由 TxGNN 預測系統生成，僅供研究參考，不構成醫療建議。*


---

## 相關藥物報告

- [Pemetrexed]({{ "/drugs/pemetrexed/" | relative_url }}) - 證據等級 L5
- [Potassium Iodide]({{ "/drugs/potassium_iodide/" | relative_url }}) - 證據等級 L5
- [Paclitaxel]({{ "/drugs/paclitaxel/" | relative_url }}) - 證據等級 L5
- [Sulfamethazine]({{ "/drugs/sulfamethazine/" | relative_url }}) - 證據等級 L5
- [Homatropine Methylbromide]({{ "/drugs/homatropine_methylbromide/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Oxybutynin老藥新用驗證報告. https://twtxgnn.yao.care/drugs/oxybutynin/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_oxybutynin,
  title = {Oxybutynin老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/oxybutynin/}
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
