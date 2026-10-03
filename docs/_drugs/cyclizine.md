---
layout: default
title: Cyclizine
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 9
---

# Cyclizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cyclizine 藥師筆記

## 一句話總結

Cyclizine 是第一代抗組織胺藥物，用於暈動症及過敏性疾患，TxGNN 預測其對蕁麻疹及頭痛疾患有療效，這與其核准適應症高度重疊，屬於已知藥理作用的再確認。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Cyclizine (環立淨) 及其衍生物 |
| DrugBank ID | DB01176 |
| 台灣商品名 | 旅暈平錠、赫敏錠、止敏糖衣錠等 |
| 原核准適應症 | 暈動症（預防或緩解暈車、暈船、暈機引起之頭暈、噁心、嘔吐、頭痛等症狀） |
| 預測新適應症 | 過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病、頭痛疾患 |
| 最高預測分數 | 0.9998 (allergic urticaria) |
| 證據等級 | L2-L3 (已有臨床使用經驗) |

<!-- review:begin cyclizine-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原核准適應症／暈動症、過敏性皮膚炎、濕疹、蕁麻疹、支氣管氣喘、偏頭痛」。台灣現行 cyclizine 單方許可證（旅暈平錠）的核准適應症只有動暈症；過敏性皮膚炎、濕疹、氣喘、蕁麻疹屬於 homochlorcyclizine／chlorcyclizine 等不同成分，偏頭痛屬於已於 2010-05-31 註銷的 ergotamine 複方。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cyclizine-original-indication-2026-10-03 -->

<!-- review:begin cyclizine-prediction-rereview-2026-10-03 -->

> **待重審（2026-10-03）**：這批預測的判讀前提（cyclizine 已核准蕁麻疹、過敏性鼻炎、偏頭痛）與許可證資料不符（見上方查核更正與加註），已標記待重審；證據等級、文獻與決策在重審完成前不更動。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cyclizine-prediction-rereview-2026-10-03 -->

---

## 為什麼這個預測合理

Cyclizine 及其相關衍生物（如 homochlorcyclizine）的藥理機轉直接支持預測適應症：

1. **H1 受體拮抗**：阻斷組織胺 H1 受體，抑制過敏反應中的血管擴張、瘙癢及發炎
2. **抗膽鹼作用**：降低前庭敏感性，這是其抗暈動症作用的基礎
3. **中樞作用**：具有鎮靜及止吐作用

### 預測與核准適應症對照

| 預測適應症 | 與核准適應症關係 | 機轉支持 |
|------------|------------------|----------|
| Allergic urticaria | 已核准 (蕁麻疹) | H1 受體拮抗 |
| Cold urticaria | 屬蕁麻疹亞型 | H1 受體拮抗 |
| Nasal cavity disease | 已核准 (過敏性鼻炎) | H1 受體拮抗 |
| Headache disorder | 已核准 (偏頭痛) | 抗膽鹼 + 止吐作用 |

<!-- review:begin cyclizine-why-approved-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：對照表中「已核准（蕁麻疹）」「已核准（過敏性鼻炎）」「已核准（偏頭痛）」的前提與許可證資料不符：台灣現行 cyclizine 單方許可證只核准動暈症；蕁麻疹、過敏性鼻炎屬於 homochlorcyclizine／chlorcyclizine 等不同成分，偏頭痛屬於已註銷的 ergotamine＋caffeine＋cyclizine 複方。英國仿單所載 cyclizine 的核准用途為噁心、嘔吐與動暈症等。推論原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)；[emc：Valoid 50 mg Tablets（cyclizine hydrochloride）SmPC §4.1](https://www.medicines.org.uk/emc/product/4318/smpc)。

<!-- review:end cyclizine-why-approved-premise-2026-10-03 -->

---

## 臨床試驗證據

Cyclizine 作為經典老藥，臨床證據主要來自歷史研究：

| PMID | 研究類型 | 主要發現 |
|------|----------|----------|
| 8573923 | 病例報告 | Cyclizine 用於日光性蕁麻疹的治療 |
| 4148490 | 對照試驗 | Cyclizine 與止痛藥複方治療偏頭痛有效 |
| 3926322 | RCT | 含 cyclizine 的 ergotamine 複方對偏頭痛急性發作有效 |

---

## 文獻證據

### 蕁麻疹相關

- 多項研究確認第一代抗組織胺藥物對蕁麻疹有效
- Cyclizine 作為 H1 受體拮抗劑，其抗蕁麻疹作用有明確的藥理基礎

### 偏頭痛相關

| PMID | 標題 | 年份 | 發現 |
|------|------|------|------|
| 4148490 | Migraine treated with antihistamine-analgesic combination | 1973 | Cyclizine 複方對偏頭痛有效 |
| 3926322 | Naproxen vs ergotamine compound for acute migraine | 1985 | Ergotamine + cyclizine 複方可縮短偏頭痛發作時間 |
| 10842162 | Chronic ergot toxicity | 2000 | 提醒長期使用含 cyclizine 的 ergotamine 複方的風險 |

---

## 台灣上市資訊

### 主要製劑

| 許可證字號 | 商品名 | 適應症 | 狀態 |
|------------|--------|--------|------|
| 衛署藥製字第002658號 | 旅暈平錠 | 暈動症 (暈車、暈船、暈機) | 有效 |
| 衛署藥製字第032336號 | 應元赫敏錠 (Homochlorcyclizine) | 過敏性皮疹、濕疹、氣喘 | 有效 |
| 衛署藥製字第023981號 | 止敏糖衣錠 (Chlorcyclizine) | 過敏性鼻炎、皮膚搔癢 | 有效 |

<!-- review:begin cyclizine-tw-license-other-ingredients-2026-10-03 -->

> **查核加註（2026-10-03）**：表中「應元赫敏錠」主成分是 homochlorcyclizine、「止敏糖衣錠」主成分是 chlorcyclizine，都是與 cyclizine 不同的成分，其過敏適應症不是 cyclizine 的核准適應症；台灣現行 cyclizine 單方許可證只有「旅暈平錠」（動暈症）。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cyclizine-tw-license-other-ingredients-2026-10-03 -->

### 複方製劑

| 許可證字號 | 商品名 | 成分 | 適應症 | 狀態 |
|------------|--------|------|--------|------|
| 衛署藥輸字第011158號 | 邁克寧錠 | Ergotamine + Caffeine + Cyclizine | 偏頭痛 | 已註銷 |

**備註**：台灣市場上有多種 cyclizine 衍生物製劑，但許多已註銷。目前有效的製劑主要用於暈動症及過敏。

---

## 安全性考量

### 主要副作用

1. **中樞神經**：嗜睡、頭暈、視力模糊
2. **抗膽鹼作用**：口乾、便秘、尿滯留、心搏過速
3. **胃腸道**：噁心（矛盾反應）

### 藥物交互作用

| 交互作用藥物類型 | 代表藥物 | 嚴重程度 | 機轉 |
|------------------|----------|----------|------|
| 抗膽鹼藥物 | Atropine, Scopolamine | Moderate | 加重抗膽鹼副作用 |
| 鉀鹽 | Potassium chloride, Potassium citrate | Major | 抗膽鹼作用可能增加腸道鉀鹽滯留風險 |
| 中樞抑制劑 | Opioids, Benzodiazepines | Moderate | 加重鎮靜作用 |
| 酒精 | Ethanol | Moderate | 增強 CNS 抑制 |

### 特殊族群

- **孕婦**：FDA 分級 B，但仍應謹慎使用
- **老年人**：抗膽鹼副作用較敏感，可能增加跌倒及認知障礙風險
- **攝護腺肥大**：可能加重尿滯留
- **青光眼**：窄角型青光眼禁用

---

## 結論與下一步

### 預測評估

| 評估項目 | 結果 |
|----------|------|
| 機轉合理性 | 高 - H1 受體拮抗對過敏反應有明確效果 |
| 臨床證據 | 中等 - 有歷史臨床使用經驗 |
| 文獻支持 | 中等 |
| 整體證據等級 | **L2-L3 (已有臨床經驗)** |

### 臨床建議

1. **蕁麻疹**：
   - Cyclizine 類藥物可作為急性蕁麻疹的選項
   - 第二代抗組織胺（如 cetirizine、loratadine）因較少嗜睡通常為首選
   - 第一代藥物適用於需要鎮靜效果或夜間使用的情況

2. **偏頭痛**：
   - Cyclizine 的止吐作用可輔助偏頭痛治療
   - 含 ergotamine 的複方製劑目前台灣已無有效許可證

3. **暈動症**：
   - 維持現有適應症使用
   - 提醒病患服藥後避免駕駛

### 方法學意義

此預測結果顯示 TxGNN 能準確識別藥物的已知適應症範圍，驗證了知識圖譜方法的基本可靠性。但這也意味著對於此類「經典」藥物，預測結果更多是確認而非發現。

---

*本筆記僅供研究參考，不構成醫療建議。任何用藥決策應諮詢專業醫療人員。*

*最後更新：2026-02-11*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原核准適應症混入其他成分與已註銷複方的適應症 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 主要製劑表列入 homochlorcyclizine、chlorcyclizine 製劑 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 對照表「已核准 (蕁麻疹)」「已核准 (偏頭痛)」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)；[emc：Valoid 50 mg Tablets（cyclizine hydrochloride）SmPC §4.1](https://www.medicines.org.uk/emc/product/4318/smpc) |
| 2026-10-03 | 蕁麻疹、鼻腔疾病、頭痛預測標記待重審 | 標記待重審 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

