---
layout: default
title: Milrinone
parent: 中證據等級 (L3-L4)
nav_order: 168
evidence_level: L3
indication_count: 10
---

# Milrinone
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Milrinone 藥師筆記

## 一句話總結

Milrinone 是一種磷酸二酯酶抑制劑，TxGNN 預測其對禿髮症及頭痛障礙有潛力，其中頭痛障礙（特別是可逆性腦血管收縮症候群相關頭痛）已有病例報告支持動脈內 Milrinone 的療效。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Milrinone（米力心） |
| DrugBank ID | DB00235 |
| 台灣商品名 | 米力心注射劑0.2毫克/毫升 |
| 原核准適應症 | 充血性心衰竭的短期療法 |
| 預測新適應症 | 禿髮症、頭皮單純性毛髮稀疏症、先天性毛髮稀疏症合併粟粒疹、頭痛障礙、充血性心衰竭 |
| 最高預測分數 | 0.9991（禿髮症） |
| 證據等級 | L3（觀察性研究/病例報告 - 頭痛障礙） |

<!-- review:begin milrinone-alopecia-rereview-2026-10-03 -->

> **待重審（2026-10-03）**：禿髮症、頭皮單純性毛髮稀疏症、先天性毛髮稀疏症合併粟粒疹這幾筆預測的機轉理由有一項前提與仿單不符（見下方「為什麼這個預測合理」的查核加註），已標記待重審；頭痛障礙與充血性心衰竭不在此列。證據等級、文獻與決策在重審完成前不更動。依據：[DailyMed：Minoxidil Tablets USP 仿單（American Health Packaging），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0b4fc036-9497-442b-b629-c4b386932789)。

<!-- review:end milrinone-alopecia-rereview-2026-10-03 -->

---

## 為什麼這個預測合理？

### 藥理機轉分析

Milrinone 是選擇性磷酸二酯酶-3（PDE3）抑制劑，透過增加細胞內 cAMP 濃度發揮作用。其機轉與預測適應症的關聯：

1. **禿髮症/毛髮稀疏症**（TxGNN Score: 0.9991）
   - PDE 抑制劑（如 minoxidil）已知可促進毛髮生長
   - Milrinone 作為 PDE3 抑制劑理論上可能有類似作用
   - 但缺乏直接證據

<!-- review:begin milrinone-minoxidil-not-pde-inhibitor-2026-10-03 -->

> **查核加註（2026-10-03）**：此前提與仿單不符。Minoxidil 仿單把它歸類為直接作用的周邊血管擴張劑，NLM MeSH 列的藥理作用是抗高血壓藥與血管擴張劑，都沒有把它列為磷酸二酯酶（PDE）抑制劑；外用製劑仿單也寫明生髮機轉尚未完全了解。上段原文保留未改。依據：[DailyMed：Minoxidil Tablets USP 仿單（American Health Packaging），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0b4fc036-9497-442b-b629-c4b386932789)；[NLM MeSH：Minoxidil（D008914）](https://meshb.nlm.nih.gov/record/ui?ui=D008914)；[emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc)。

<!-- review:end milrinone-minoxidil-not-pde-inhibitor-2026-10-03 -->

2. **頭痛障礙**（TxGNN Score: 0.9946）
   - Milrinone 具有血管擴張作用
   - 已有病例報告顯示動脈內 Milrinone 可用於治療可逆性腦血管收縮症候群（RCVS）
   - 透過解除腦血管痙攣來緩解頭痛

3. **充血性心衰竭**（TxGNN Score: 0.9945）
   - 此為原核准適應症，有豐富臨床試驗證據

---

## 臨床試驗證據

| 疾病 | 臨床試驗數量 | 最高期別 | 證據等級 |
|------|-------------|---------|---------|
| 頭痛障礙 | 1 | N/A（觀察性） | L3 |
| 充血性心衰竭 | 30+ | Phase 4 | L1 |
| 禿髮症 | 0 | - | L5 |

### 重點臨床試驗（心衰竭相關）

| NCT ID | 標題 | 期別 | 狀態 | 國家 |
|--------|------|------|------|------|
| NCT02098629 | Milrinone 與 Esmolol 併用於急性心肌梗塞 | Phase 2 | 已完成 | 新加坡 |
| NCT07186062 | Levosimendan vs Dobutamine vs Milrinone 比較 | N/A | 已完成 | 埃及 |
| NCT04718350 | 靜脈 Levosimendan vs 吸入 Milrinone 比較 | N/A | 已完成 | 希臘 |

---

## 文獻證據

### 頭痛障礙（可逆性腦血管收縮症候群）

| PMID | 標題 | 年份 | 類型 | 證據等級 |
|------|------|------|------|---------|
| 34784343 | Reversible Cerebral Vasoconstriction Syndrome in Eclampsia Responding to Milrinone | 2021 | 病例報告 | L3 |
| 25440342 | Novel approach to diagnose reversible cerebral vasoconstriction syndrome | 2015 | 病例系列 | L3 |
| 18647181 | Intra-arterial milrinone for reversible cerebral vasoconstriction syndrome | 2009 | 病例報告 | L3 |

**關鍵發現**：
- 多篇病例報告顯示動脈內 Milrinone 可快速改善 RCVS 相關的腦血管痙攣和神經症狀
- 特別適用於鈣離子通道阻斷劑治療無效的病例
- 作為 PDE 抑制劑，可有效鬆弛血管平滑肌

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Milrinone 的不重複許可證共 **3 張**：有效單方 2 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第021128號 | 哌明克注射劑 | 注射劑 | 賽諾菲股份有限公司 | 2030/06/08 | 充血性心衰竭的短期療法 |
| 衛部藥製字第058150號 | 米力心注射劑0.2毫克/毫升 | 注射劑 | 歐舒邁克有限公司 | 2028/12/12 | EasyMilrinone injection 適用於充血性心衰竭的短期療法。病人接受milrinone治療，應給予適當心電圖設備嚴密監控。對於可能發生的心臟事件，如危及生命的室性… |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第020939號</td><td>/明克注射劑</td><td>MILRINONE</td><td>1996/03/15</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**適應症**：充血性心衰竭的短期療法。需在有適當心電圖監測設備的環境下使用。

---

## 安全性考量

### 使用注意事項

1. **心律不整風險**
   - 可能引起危及生命的室性心律不整
   - 需持續心電圖監測

2. **使用限制**
   - 目前無使用超過 48 小時的對照試驗經驗
   - 建議僅作為短期療法

3. **藥物交互作用**
   - 常與 digoxin 和利尿劑併用
   - 與其他強心藥物併用時需謹慎

### 給藥途徑考量

- **靜脈注射**：心衰竭標準給藥方式
- **動脈內注射**：RCVS 治療的研究給藥方式，需專業介入設備
- **吸入給藥**：肺高壓治療的研究給藥方式

---

## 結論與下一步

### 評估結論

| 預測適應症 | 證據等級 | 臨床轉譯可行性 | 建議優先順序 |
|-----------|---------|---------------|-------------|
| 頭痛障礙（RCVS） | L3 | 中等 | 建議進一步研究 |
| 禿髮症 | L5 | 低 | 不建議優先開發 |
| 心衰竭 | L1 | 高（已核准） | 不適用 |

### 建議

1. **可逆性腦血管收縮症候群（RCVS）**
   - 目前已有多篇病例報告支持動脈內 Milrinone 的療效
   - 建議設計前瞻性研究評估安全性和有效性
   - 可考慮作為鈣離子通道阻斷劑無效時的救援治療

2. **禿髮症**
   - 雖然 PDE 抑制劑理論上可能有效
   - 但 Milrinone 為注射劑型，不適合局部外用治療禿髮
   - 不建議進一步開發

### 後續行動

- [x] 確認頭痛障礙文獻證據（已有 3 篇病例報告）
- [ ] 監測 RCVS 治療的新臨床試驗
- [ ] 評估是否有可能開發局部外用劑型用於禿髮（可行性低）

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「PDE 抑制劑（如 minoxidil）已知可促進毛髮生長」 | 加註 | [DailyMed：Minoxidil Tablets USP 仿單（American Health Packaging），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0b4fc036-9497-442b-b629-c4b386932789)；[NLM MeSH：Minoxidil（D008914）](https://meshb.nlm.nih.gov/record/ui?ui=D008914)；[emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc) |
| 2026-10-03 | 禿髮症／毛髮稀疏症預測標記待重審 | 標記待重審 | [DailyMed：Minoxidil Tablets USP 仿單（American Health Packaging），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0b4fc036-9497-442b-b629-c4b386932789) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

