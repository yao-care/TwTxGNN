---
layout: default
title: Cyclizine
parent: 中證據等級 (L3-L4)
nav_order: 73
evidence_level: L4
indication_count: 9
---

# Cyclizine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **9** 個
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
| 原核准適應症 | 預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀（衛署藥製字第002658號） |
| 預測新適應症 | 過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病、頭痛疾患 |
| 最高預測分數 | 0.9998 (allergic urticaria) |
| 證據等級 | 頭痛疾患 L4；過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病 L5（2026-10-03 重審降級） |

<!-- review:begin cyclizine-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原核准適應症／暈動症、過敏性皮膚炎、濕疹、蕁麻疹、支氣管氣喘、偏頭痛」。台灣現行 cyclizine 單方許可證只有旅暈平錠（衛署藥製字第002658號），適應症為「預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀」；過敏性皮膚炎、濕疹、氣喘、蕁麻疹屬於 homochlorcyclizine／chlorcyclizine 等不同成分，偏頭痛屬於已於 2010-05-31 註銷的 ergotamine 複方。已改為許可證原文。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cyclizine-original-indication-2026-10-03 -->

<!-- review:begin cyclizine-prediction-rereview-result-2026-10-03 -->

> **重審結果（2026-10-03）**：**降級**（證據等級 L2–L3→頭痛疾患 L4；過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病 L5）。原判定的依據「已核准、已有臨床經驗」來自其他成分（homochlorcyclizine、chlorcyclizine）或已註銷複方的許可證。PubMed 與 ClinicalTrials.gov 都查無 cyclizine 單方用於蕁麻疹或鼻炎的臨床研究，只剩 H1 拮抗的類別推論。頭痛方面只有含 ergotamine 的複方試驗，無法分離 cyclizine 本身的效果，而且該複方療效不如 naproxen、嘔吐較多（[PMID 3926322](https://pubmed.ncbi.nlm.nih.gov/3926322/)）。本頁快速總覽「證據等級」、結論「整體證據等級」已依重審結果更新，原值列在下方查核紀錄。依據：[PubMed：Acute migraine attack therapy: comparison of naproxen sodium and an ergotamine tartrate compound（PMID 3926322）](https://pubmed.ncbi.nlm.nih.gov/3926322/)；[PubMed：Migraine treated with an antihistamine-analgesic combination（PMID 4148490）](https://pubmed.ncbi.nlm.nih.gov/4148490/)；[PubMed：Detection of action, inhibition and augmentation spectra in solar urticaria（PMID 8573923）](https://pubmed.ncbi.nlm.nih.gov/8573923/)；[PubMed：Standard treatment: the role of antihistamines（PMID 11764306）](https://pubmed.ncbi.nlm.nih.gov/11764306/)；[PubMed：Cyclizine anaphylaxis, when administered with propanidid（PMID 5762012）](https://pubmed.ncbi.nlm.nih.gov/5762012/)。

<!-- review:end cyclizine-prediction-rereview-result-2026-10-03 -->

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

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cyclizine 的不重複許可證共 **9 張**：有效單方 1 張、有效複方 0 張、已註銷 8 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第002658號 | 旅暈平錠 | 錠劑 | 華盛頓製藥廠股份有限公司 | 2029/05/25 | 預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀。 |

<details><summary><strong>已註銷</strong>（8 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第003276號</td><td>邁可抗黴酊</td><td>CYCLIZINE HCL、SALICYLIC ACID</td><td>1986/02/04</td></tr><tr><td>內衛藥輸字第004700號</td><td>鹽酸環立淨</td><td>CYCLIZINE HCL</td><td>1985/07/12</td></tr><tr><td>衛署藥製字第022713號</td><td>肝克寧膠囊</td><td>CYCLIZINE、RIBOFLAVIN(5-PHOSPHATE SODIUM)、THIAMINE HYDROCHLOR…</td><td>1996/04/16</td></tr><tr><td>衛署藥輸字第009561號</td><td>滅暈錠</td><td>CYCLIZINE HCL</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第010504號</td><td>二苯甲基４－甲基呱/鹽酸鹽</td><td>CYCLIZINE HCL</td><td>1998/09/29</td></tr><tr><td>衛署藥輸字第011158號</td><td>邁克寧錠</td><td>CYCLIZINE HCL、CAFFEINE (HYDRATE)、ERGOTAMINE TARTRATE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第013612號</td><td>鹽酸環立淨粉劑</td><td>CYCLIZINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014591號</td><td>邁可抗黴酊</td><td>CYCLIZINE HCL、SALICYLIC ACID</td><td>1999/10/25</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

### 複方製劑

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
| 整體證據等級 | **L4**（頭痛疾患；其餘三筆 L5，2026-10-03 重審降級） |

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

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測原文未改寫；證據等級與決策只依重審結果（降級或撤回）更新，原值列在下表。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原核准適應症混入其他成分與已註銷複方的適應症 | 更正（2026-10-03 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 主要製劑表列入 homochlorcyclizine、chlorcyclizine 製劑 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 對照表「已核准 (蕁麻疹)」「已核准 (偏頭痛)」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)；[emc：Valoid 50 mg Tablets（cyclizine hydrochloride）SmPC §4.1](https://www.medicines.org.uk/emc/product/4318/smpc) |
| 2026-10-03 | 蕁麻疹、鼻腔疾病、頭痛預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 蕁麻疹、鼻腔疾病、頭痛預測重審結果 | 重審：降級，證據等級 L2–L3→頭痛疾患 L4；過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病 L5；快速總覽「證據等級」：原「證據等級／L2-L3 (已有臨床使用經驗)」→「證據等級／頭痛疾患 L4；過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病 L5（2026-10-03 重審降級）」；結論「整體證據等級」：原「整體證據等級／**L2-L3 (已有臨床經驗)**」→「整體證據等級／**L4**（頭痛疾患；其餘三筆 L5，2026-10-03 重審降級）」 | [PubMed：Acute migraine attack therapy: comparison of naproxen sodium and an ergotamine tartrate compound（PMID 3926322）](https://pubmed.ncbi.nlm.nih.gov/3926322/)；[PubMed：Migraine treated with an antihistamine-analgesic combination（PMID 4148490）](https://pubmed.ncbi.nlm.nih.gov/4148490/)；[PubMed：Detection of action, inhibition and augmentation spectra in solar urticaria（PMID 8573923）](https://pubmed.ncbi.nlm.nih.gov/8573923/)；[PubMed：Standard treatment: the role of antihistamines（PMID 11764306）](https://pubmed.ncbi.nlm.nih.gov/11764306/)；[PubMed：Cyclizine anaphylaxis, when administered with propanidid（PMID 5762012）](https://pubmed.ncbi.nlm.nih.gov/5762012/) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L4） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

