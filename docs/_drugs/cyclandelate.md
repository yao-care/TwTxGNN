---
layout: default
title: Cyclandelate
parent: 高證據等級 (L1-L2)
nav_order: 71
evidence_level: L1
indication_count: 1
---

# Cyclandelate
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Cyclandelate（益寧膠囊）：從末梢血管循環障礙到偏頭痛預防

## 一句話總結

Cyclandelate（益寧膠囊）是台灣已上市的直接作用型血管平滑肌鬆弛劑，原核准用於腦循環及末梢血管循環障礙的改善。
TxGNN 模型共預測了 10 項潛在新適應症，其中**偏頭痛預防 (Migraine Disorder)** 具備最強的臨床證據——目前已有 **6 篇 RCT** 及多篇系統性回顧支持，達到 L1 證據等級，是最具臨床開發潛力的再利用方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 末梢血管循環障礙 |
| 建議主要再利用方向 | 偏頭痛預防 (Migraine Disorder) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

### 全部預測適應症概覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|--------|-----------|---------|------|
| 1 | Prinzmetal Angina（變異型心絞痛） | 99.80% | L5 | Hold |
| 2 | Raynaud Disease（雷諾氏病） | 99.73% | L4 | Research Question |
| **3** | **Migraine Disorder（偏頭痛）** | **99.69%** | **L1** | **Proceed with Guardrails** |
| 4 | Migraine with Brainstem Aura（基底型偏頭痛） | 99.62% | L3 | Research Question |
| 5 | Pulmonary Hypertension（肺動脈高壓） | 99.50% | L5 | Hold |
| 6 | Gout（痛風） | 99.43% | L5 | Hold |
| 7 | Kyphoscoliotic Heart Disease（脊柱性心臟病） | 99.36% | L5 | Hold |
| 8 | Benign Prostatic Hyperplasia（良性前列腺肥大） | 99.08% | L5 | Hold |
| 9 | Exostosis（骨外生骨疣） | 99.06% | L5 | Hold |
| 10 | Peripheral Vascular Disease（周邊血管疾病） | 99.04% | L3 | Hold |

---

## 為什麼偏頭痛預測合理？

目前缺乏詳細的作用機轉資料。根據現有文獻，Cyclandelate 是 3,3,5-三甲基環己醇的杏仁酸酯，具備多重藥理特性：**抑制鈣離子誘導的血管平滑肌收縮**（類鈣離子拮抗機轉）、**抑制多種途徑誘發的血小板聚集**（凝血酶、血小板活化因子、腺苷），以及**抑制血小板釋放血清素（5-HT）**。

偏頭痛的神經血管理論認為，發作與腦血管張力失調、血小板過度活化及血清素波動密切相關——Cyclandelate 對上述三個環節皆具潛在調節作用，在機轉上提供了合理的生物學基礎。

從原適應症角度看，Cyclandelate 已核准用於腦循環障礙改善，而偏頭痛本質上也涉及腦血流調節異常，兩者在血管病理機轉上高度重疊。多項頭對頭 RCT 直接驗證了其預防偏頭痛的效果與 propranolol、flunarizine、pizotifen 等臨床標準藥物相當，進一步支持此預測的臨床可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov 查詢結果為 0 筆）。現有 RCT 均發表於 1987–2001 年，早於強制臨床試驗登記時代，相關證據請見以下文獻區。

---

## 文獻證據（偏頭痛預防）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3304950](https://pubmed.ncbi.nlm.nih.gov/3304950/) | 1987 | RCT | Drugs | 雙盲平行試驗（n=40），Cyclandelate 800 mg BID vs flunarizine 5 mg，兩組均顯著改善頭痛指數、用藥量及偏頭痛天數，效果相當 |
| [1573338](https://pubmed.ncbi.nlm.nih.gov/1573338/) | 1992 | RCT | Journal of Medicine | 雙盲 16 週研究（n=84，篩除安慰劑反應者後 n=61），Cyclandelate vs pizotifen，評估偏頭痛預防效果及耐受性 |
| [7649498](https://pubmed.ncbi.nlm.nih.gov/7649498/) | 1995 | RCT | Functional Neurology | 雙盲安慰劑對照，Cyclandelate vs propranolol；時序分析及反應者/非反應者評估顯示兩藥預防效果相當 |
| [8902255](https://pubmed.ncbi.nlm.nih.gov/8902255/) | 1996 | RCT | Cephalalgia | 多中心雙盲 RCT（n=214），Cyclandelate vs 安慰劑 vs propranolol；同時探討鈣離子誘導收縮、血小板聚集及 5-HT 釋放抑制機轉 |
| [9584874](https://pubmed.ncbi.nlm.nih.gov/9584874/) | 1998 | RCT | Functional Neurology | 雙盲安慰劑對照平行設計；以 CNV（聯合負向電位）客觀量化評估中樞神經機轉，探討鈣離子拮抗劑的中樞作用路徑 |
| [11298666](https://pubmed.ncbi.nlm.nih.gov/11298666/) | 2001 | RCT | Cephalalgia | 多中心 RCT（n=251），1600 mg/day vs 安慰劑，16 週治療期；主要終點（偏頭痛日數減少）**未達統計顯著** ⚠️ |
| [10463349](https://pubmed.ncbi.nlm.nih.gov/10463349/) | 1999 | Review | Journal of Neurology | 偏頭痛藥物治療系統性回顧，含 Cyclandelate 於急性及預防治療中的定位分析 |
| [9829155](https://pubmed.ncbi.nlm.nih.gov/9829155/) | 1998 | Review | Drugs | 偏頭痛管理與預防實務指引，涵蓋預防性用藥選擇策略 |
| [9139407](https://pubmed.ncbi.nlm.nih.gov/9139407/) | 1997 | Review | Therapeutische Umschau | 偏頭痛診斷與治療回顧；頻繁嚴重發作者預防藥物選項含 Cyclandelate |
| [2684591](https://pubmed.ncbi.nlm.nih.gov/2684591/) | 1989 | Review | Drugs | Flunarizine 藥理完整回顧，收錄與 cyclandelate、cinnarizine、propranolol 等藥物的頭對頭比較資料 |

> ⚠️ **關鍵注意**：規模最大的 RCT（PMID 11298666，n=251）主要終點未達統計顯著，此為本適應症最重要的不確定因素，應在決策中充分評估有效劑量與目標族群。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第002324號 | 益寧膠囊 | 膠囊劑 | 末梢血管循環障礙 |
| 內衛藥輸字第000909號 | 安保平膠囊 | 膠囊劑 | 腦、末梢血行障礙 |
| 內衛藥輸字第006652號 | 杏仁酸三甲環已酯 | （粉） | 末稍血管擴張劑 |
| 內衛藥製字第001567號 | 適通膠囊 | 膠囊劑 | 末梢血管循環障礙 |
| 衛署藥製字第001045號 | 脈速朗膠囊 | 膠囊劑 | 末梢血管循環障礙 |

（共 20 張許可證，以上列出代表性 5 張）

---

## 安全性考量

**藥物交互作用**（共 17 筆，均為中度風險，資料來源：DDInter）

| 藥物類別 | 代表藥物 | 等級 |
|---------|---------|------|
| SGLT2 抑制劑 | Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin | 中度 |
| 前列環素類（肺高壓用藥） | Selexipag、Treprostinil、Epoprostenol、Iloprost | 中度 |
| 其他血管活性藥物 | Pentoxifylline、Minoxidil（外用） | 中度 |
| Alpha2 受體促效劑 | Brimonidine（眼用）、Brimonidine（外用） | 中度 |
| 神經／精神用藥 | Promethazine、Ozanimod | 中度 |
| 其他 | Amifostine、Nitrous acid、Procarbazine | 中度 |

主要臨床意義：Cyclandelate 的血管擴張效果可能與 SGLT2 抑制劑、前列環素類等血管活性藥物產生加成性降血壓效應，合用時建議監測血壓。

詳細警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Cyclandelate 用於偏頭痛預防已有 6 篇 RCT（含多中心、安慰劑對照及頭對頭比較研究），達 L1 證據等級；台灣有 20 張藥品許可證與完整供應鏈，法規與市場基礎成熟。主要疑慮在於最大規模 RCT（n=251，2001 年）主要終點未達統計顯著，需釐清有效劑量窗與適用族群，方能推進下一步。

**若要推進需要：**
- 補充完整作用機轉資料（查詢 DrugBank API 取得 MOA）
- 針對現有 6 篇 RCT 進行系統性回顧與 Meta 分析，釐清有效劑量（初步指向 1600 mg/day）及反應者特徵
- 諮詢神經科專家評估台灣偏頭痛預防的未滿足醫療需求與現行治療缺口
- 確認與常見偏頭痛預防藥物（topiramate、propranolol、CGRP 拮抗劑）及急性治療藥物（triptans、NSAIDs）的交互作用
- 在 SGLT2 抑制劑使用者（糖尿病合併偏頭痛族群）中特別注意血壓加成風險

---

