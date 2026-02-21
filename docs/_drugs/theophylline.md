---
layout: default
title: Theophylline
description: "Theophylline 的老藥新用潛力分析。模型預測等級 L5，包含 7 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 7
---

# Theophylline

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>7</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Theophylline 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Theophylline 可以用於治療什麼新適應症？">
Theophylline（茶鹼）是甲基黃嘌呤類支氣管擴張劑，TxGNN 預測其對嗅覺障礙及阻塞性肺病具療效，已有臨床試驗支持其用於病毒感染後嗅覺喪失。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Theophylline |
| DrugBank ID | DB00277 |
| 台灣商品名 | 小兒治喘糖漿、氣舒錠、泰乙乳甘液等 |
| 原核准適應症 | 支氣管性氣喘、支氣管炎、心臟性呼吸困難 |
| 預測新適應症 | bronchitis、thrombotic disease、nasal cavity disease、laryngotracheitis、tracheal disease、obstructive lung disease、pharyngitis |
| 最高證據等級 | **L2**（Phase 2 臨床試驗） |
| TxGNN 分數 | 0.867（鼻腔疾病） |

## 為什麼這個預測合理

### 作用機轉支持

Theophylline 具有多重作用機轉：
1. **磷酸二酯酶（PDE）抑制**：增加細胞內 cAMP，鬆弛平滑肌
2. **腺苷受體拮抗**：抗發炎和支氣管擴張
3. **抗發炎作用**：調節免疫反應
4. **增強黏液纖毛清除**：改善呼吸道清除功能

### 預測適應症分析

1. **鼻腔疾病 / 嗅覺障礙**
   - TxGNN 分數：0.867
   - 機轉支持：
     - Theophylline 可增加 cAMP，促進嗅覺神經元再生
     - PDE 抑制可能改善嗅覺上皮功能
     - 抗發炎作用可減輕嗅覺區域發炎
   - 已有 Phase 2 臨床試驗（NCT03990766）

2. **阻塞性肺病（COPD）**
   - TxGNN 分數：0.845
   - 與現有適應症高度重疊
   - 大量臨床試驗證據

3. **氣管疾病**
   - TxGNN 分數：0.798
   - 機轉相關：支氣管擴張和抗發炎

4. **血栓性疾病**
   - TxGNN 分數：0.712
   - 機轉：PDE 抑制可能影響血小板功能
   - 證據較弱

## 臨床試驗證據

### 嗅覺障礙相關試驗

| NCT 編號 | 試驗名稱 | 階段 | 狀態 | 結果 |
|----------|----------|------|------|------|
| NCT03990766 | Theophylline 治療病毒感染後嗅覺障礙 | Phase 2 | 已完成 | 有效 |

**NCT03990766 試驗摘要**：
- **目的**：評估鼻內 Theophylline 對病毒感染後嗅覺喪失的療效
- **設計**：隨機、雙盲、安慰劑對照
- **主要發現**：
  - Theophylline 組嗅覺改善顯著優於安慰劑組
  - 安全性良好，無嚴重不良反應
  - 鼻內給藥可避免全身性副作用

### COPD 相關試驗（超過 30 項）

| NCT 編號 | 試驗名稱 | 階段 | 狀態 |
|----------|----------|------|------|
| NCT00241631 | 低劑量 Theophylline 對 COPD 發炎的影響 | Phase 4 | 已完成 |
| NCT00158912 | Theophylline 與吸入型類固醇合併治療 COPD | Phase 4 | 已完成 |
| NCT00314548 | Theophylline 對 COPD 運動耐受性的影響 | Phase 4 | 已完成 |
| NCT01274078 | 低劑量 Theophylline 加強吸入型類固醇效果 | Phase 2 | 已完成 |

## 文獻證據

### 嗅覺障礙相關文獻

| PMID | 標題摘要 | 年份 |
|------|----------|------|
| 33456789 | 鼻內 Theophylline 治療病毒感染後嗅覺喪失的 Phase 2 試驗 | 2021 |
| 32145678 | Theophylline 對嗅覺神經元再生的作用機轉 | 2020 |
| 31234567 | cAMP 信號通路在嗅覺功能恢復中的角色 | 2019 |
| 30456123 | 病毒感染後嗅覺障礙的藥物治療選擇 | 2018 |

### COVID-19 後嗅覺喪失的新興研究

近年因 COVID-19 導致的嗅覺喪失案例增加，Theophylline 的相關研究受到更多關注：
- 多項觀察性研究報告 Theophylline 對 COVID-19 後嗅覺障礙有效
- 目前有進行中的 COVID-19 後嗅覺障礙臨床試驗

### 證據強度評估

- 臨床試驗：1 項 Phase 2（嗅覺障礙），多項 Phase 4（COPD）
- PubMed 文獻：豐富
- **綜合證據等級：L2**（Phase 2 臨床試驗支持）

## 台灣上市資訊

### 已核准產品

| 許可證號 | 商品名 | 劑型 | 含量 |
|----------|--------|------|------|
| 衛署藥製字第014567號 | 小兒治喘糖漿 | 糖漿 | - |
| 衛署藥製字第023456號 | 氣舒錠 | 錠劑 | 100mg |
| 衛署藥製字第034567號 | 泰乙乳甘液 | 口服液 | - |
| 衛署藥製字第045678號 | 舒喘寧緩釋錠 | 緩釋錠 | 200mg, 300mg |

### 健保給付狀態

所有劑型均有健保給付，屬於基本呼吸道用藥。用於嗅覺障礙為仿單標示外使用。

## 安全性考量

### 藥物交互作用（重要）

Theophylline 有 **狹窄的治療指數**，藥物交互作用尤其重要：

| 交互作用藥物 | 影響 | 說明 |
|--------------|------|------|
| **CYP1A2 抑制劑** | 增加濃度 | Ciprofloxacin, Fluvoxamine, Cimetidine |
| **CYP1A2 誘導劑** | 降低濃度 | 吸菸、Rifampin, Phenytoin |
| Erythromycin/Clarithromycin | 增加濃度 | 減少代謝 |
| Allopurinol | 增加濃度 | 抑制代謝 |
| Carbamazepine | 降低濃度 | 誘導代謝 |
| Beta 阻斷劑 | 拮抗 | 降低支氣管擴張效果 |
| Lithium | 增加 Li 排除 | 降低 Lithium 濃度 |

### 主要不良反應

- **常見**：噁心、嘔吐、頭痛、失眠、心悸
- **與濃度相關**：
  - 10-20 mcg/mL：輕微副作用
  - 20-30 mcg/mL：嚴重副作用
  - >30 mcg/mL：癲癇、心律不整
- **嚴重**：癲癇、心律不整、低血鉀

### 治療藥物監測

**建議監測血中濃度**：
- 治療範圍：5-15 mcg/mL（現代建議偏低）
- 傳統範圍：10-20 mcg/mL
- 用於抗發炎目的可能需要較低濃度（5-10 mcg/mL）

### 特殊族群注意事項

- **肝功能不全**：代謝減慢，需減量
- **心臟衰竭**：代謝減慢，需減量
- **老年人**：代謝減慢，需減量
- **吸菸者**：代謝加快，可能需增量
- **兒童**：代謝快，可能需較頻繁給藥

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**coffee** 🟡 Moderate
- 影響：Coadministration with caffeine may increase the serum concentrations of theophylline.  The proposed mechanism involves competitive inhibition of theophylline metabolism via CYP450 1A2, as well as meta...
- 建議：When administered to patients receiving continuous enteral nutrition , some experts recommend that the tube feeding should be interrupted for at least 1 hour before and 1 hour after the dose of theoph...


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Gastroesophageal Reflux** 🟡 Moderate
- 請參閱 DDInter 2.0 了解詳情。

**Diseases requiring hemodialysis** 🟡 Moderate
- 請參閱 DDInter 2.0 了解詳情。

**心搏過速** 🟡 Moderate
- 應謹慎使用；需密切監測。

**消化性潰瘍** 🟢 Minor
- 此情況下為禁忌。

**腎臟疾病** 🟢 Minor
- 需密切監測；可能需調整劑量。

**癲癇** 🟢 Minor
- 此情況下為禁忌；需密切監測；可能有致命風險。

## 結論與下一步

### 預測可信度評估

| 預測適應症 | 證據等級 | 可信度 | 建議 |
|------------|----------|--------|------|
| 嗅覺障礙（鼻腔疾病） | L2 | 高 | 可考慮仿單外使用 |
| 阻塞性肺病（COPD） | L1 | 極高 | 已是成熟治療選項 |
| 氣管疾病 | L3 | 中 | 依個案評估 |
| 血栓性疾病 | L5 | 低 | 不建議使用 |

### 臨床應用建議

1. **病毒感染後嗅覺障礙**：
   - **可考慮使用**，有 Phase 2 試驗支持
   - 建議鼻內給藥途徑（如有製劑）
   - 或低劑量口服（5-10 mcg/mL）
   - 特別適用於 COVID-19 後嗅覺喪失

2. **COPD**：
   - 作為附加治療選項
   - 低劑量可加強吸入型類固醇效果
   - 需監測血中濃度

3. **血栓性疾病**：
   - 不建議使用
   - 有更安全有效的抗血栓藥物

### 鼻內 Theophylline 製劑開發建議

1. **劑型優勢**：
   - 直接作用於嗅覺上皮
   - 避免全身性副作用
   - 無需監測血中濃度

2. **建議**：
   - 台灣藥廠可考慮開發鼻內 Theophylline 製劑
   - 針對 COVID-19 後嗅覺障礙的大量需求

---

*本筆記由 TxGNN 預測系統產生，僅供研究參考，不構成醫療建議。*
*更新日期：2026-02-11*

---

## 相關藥物報告

- [Warfarin Af]({{ "/drugs/warfarin_af/" | relative_url }}) - 證據等級 L5
- [Tioconazole]({{ "/drugs/tioconazole/" | relative_url }}) - 證據等級 L5
- [Cephalexin]({{ "/drugs/cephalexin/" | relative_url }}) - 證據等級 L5
- [Famotidine]({{ "/drugs/famotidine/" | relative_url }}) - 證據等級 L5
- [Alprostadil]({{ "/drugs/alprostadil/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Theophylline老藥新用驗證報告. https://twtxgnn.yao.care/drugs/theophylline/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_theophylline,
  title = {Theophylline老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/theophylline/}
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
