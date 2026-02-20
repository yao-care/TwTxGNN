---
layout: default
title: Famotidine
description: "Famotidine 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
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
| 預測新適應症 | 十二指腸胃逆流、十二指腸阻塞、活動性消化性潰瘍 |
| 最高預測分數 | 0.9999 (duodenogastric reflux) |
| 證據等級 | L2 (單一 RCT/多個 Phase 2) |

## 為什麼這個預測合理

Famotidine 的預測適應症與其已知藥理機轉高度一致：

1. **胃酸抑制機轉**：H2 受體拮抗劑可減少胃酸分泌，是治療消化性潰瘍的經典機轉
2. **黏膜保護**：減少胃酸可降低胃黏膜損傷，促進潰瘍癒合
3. **適應症重疊**：預測的適應症實際上是原核准適應症的延伸或細分
4. **臨床實務一致**：這些預測反映了 famotidine 的實際臨床使用範圍

## 臨床試驗證據

### ClinicalTrials.gov 搜尋結果

| 試驗編號 | 階段 | 狀態 | 適應症 | 受試者數 |
|---------|------|------|--------|---------|
| NCT00450216 | Phase 3 | 完成 | 十二指腸潰瘍(NSAID相關) | 906 |
| NCT00450658 | Phase 3 | 完成 | 上消化道潰瘍 | 627 |

**證據等級：L2 (有 Phase 3 臨床試驗)**

### 試驗摘要
- **NCT00450216**：評估 HZT-501 (ibuprofen + famotidine) 減少 NSAID 相關潰瘍的效果
- **NCT00450658**：類似設計的確認性試驗

## 文獻證據

PubMed 搜尋發現豐富的文獻支持：

### 十二指腸胃逆流 (Duodenogastric reflux)

| PMID | 年份 | 研究類型 | 關鍵發現 |
|------|------|----------|---------|
| 12532466 | 2003 | 臨床研究 | Famotidine 可減少危重病人的胃食道逆流和十二指腸胃食道逆流 |
| 16259441 | 2004 | 臨床試驗 | Famotidine 20mg BID 對早期胃十二指腸逆流疾病有效 |

### 活動性消化性潰瘍 (Active peptic ulcer disease)

| PMID | 年份 | 研究類型 | 關鍵發現 |
|------|------|----------|---------|
| 2877912 | 1987 | RCT | Famotidine 40mg qhs 4週癒合率 70%，8週達 82% |
| 1863945 | 1991 | RCT | Famotidine 40mg 與 Ranitidine 300mg 比較，8週癒合率 94% vs 80% |
| 34798155 | 2022 | 動物研究 | Famotidine 奈米製劑在消化性潰瘍模型中展現優異療效 |

### 消化道出血

| PMID | 年份 | 研究類型 | 關鍵發現 |
|------|------|----------|---------|
| 2889257 | 1987 | 多中心試驗 | IV famotidine 20mg BID 可降低出血性潰瘍的緊急手術率 |

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
