---
layout: default
title: Fenoprofen
parent: 高證據等級 (L1-L2)
nav_order: 100
evidence_level: L2
indication_count: 10
---

# Fenoprofen
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Fenoprofen 藥師評估筆記

## 一句話總結

Fenoprofen 是一種 NSAID 類止痛藥，TxGNN 預測其可用於多種骨骼肌肉疾病，其中僵直性脊椎炎的預測具有多項臨床試驗支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Fenoprofen (芬諾普芬) |
| DrugBank ID | DB00573 |
| 台灣商品名 | 風諾保膠囊 |
| 原核准適應症 | 鎮痛（現行有效許可證）；風濕性關節炎、骨關節炎、急性痛風、解熱等見於已註銷的原廠許可證 |
| 預測新適應症 | 僵直性脊椎炎、假性軟骨發育不全、WHIM 症候群 |
| 最高預測分數 | 0.9999 (acromesomelic dysplasia) |
| 證據等級 | L2 (僵直性脊椎炎有多個臨床試驗) |

<!-- review:begin fenoprofen-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原核准適應症／風濕性關節炎、骨關節炎、急性痛風、鎮痛、解熱」。台灣現行有效的 fenoprofen 許可證核准適應症只有「鎮痛」；風濕性關節炎、骨關節炎、急性痛風、解熱等屬於已於 2002-09-02 註銷的風諾保膠囊。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fenoprofen-original-indication-2026-10-03 -->

## 為什麼這個預測合理

Fenoprofen 作為丙酸類 NSAID，其對預測適應症的機轉如下：

1. **COX 抑制作用**：同時抑制 COX-1 和 COX-2，減少前列腺素合成
2. **抗發炎效果**：對關節炎和脊椎炎的發炎有效
3. **止痛作用**：中樞和周邊的止痛機轉
4. **同類藥物比較**：屬於與 naproxen、ibuprofen 同類的丙酸類 NSAID

### 僵直性脊椎炎預測特別合理
- NSAIDs 是僵直性脊椎炎的一線治療藥物
- 部分原核准適應症已包含「關節強硬性脊椎炎」（即僵直性脊椎炎）

<!-- review:begin fenoprofen-why-as-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：依 TFDA 許可證資料，含「關節強硬性脊椎炎」的是原廠「風諾保膠囊」（衛署藥製字第011765號），該證已於 2002-09-02 註銷；現行有效的 fenoprofen 許可證適應症只有「鎮痛」。推論原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fenoprofen-why-as-premise-2026-10-03 -->

## 臨床試驗證據

### 僵直性脊椎炎相關試驗

雖然 ClinicalTrials.gov 未找到近期試驗，但 PubMed 文獻記載了多項歷史臨床試驗：

| 研究 | 設計 | 關鍵發現 |
|------|------|---------|
| Wordsworth 1980 | 雙盲交叉試驗 | Fenoprofen 600mg tid vs Phenylbutazone 100mg tid；Phenylbutazone 較優 |
| Wasner 1981 | 雙盲隨機試驗 | 比較 6 種 NSAIDs，fenoprofen 為僵直性脊椎炎的有效選擇之一 |
| Shipley 1980 | 雙盲交叉試驗 | Fenoprofen vs Indomethacin vs 安慰劑比較 |

**證據等級：L2 (多個臨床試驗)**

## 文獻證據

### 僵直性脊椎炎

| PMID | 年份 | 研究類型 | 關鍵發現 |
|------|------|----------|---------|
| 7010512 | 1980 | RCT | 30 位患者；fenoprofen 改善胸廓擴張，但整體效果不如 phenylbutazone |
| 7026817 | 1981 | RCT | 32 位患者；naproxen、indomethacin、fenoprofen 為最有效的三種 NSAIDs |
| 6996071 | 1980 | RCT | Fenoprofen 優於安慰劑，但不如 indomethacin |
| 324748 | 1977 | 綜述 | Fenoprofen 2.4g/day 用於僵直性脊椎炎的療效與安全性回顧 |

### 其他關節疾病

| PMID | 年份 | 研究類型 | 關鍵發現 |
|------|------|----------|---------|
| 387372 | 1979 | 綜述 | 比較 naproxen 和 fenoprofen 在類風濕性關節炎的效果 |
| 300118 | 1977 | 綜述 | Fenoprofen、naproxen、tolmetin 在風濕疾病的應用 |

### 重要歷史研究
Brogden et al. (1977) 的藥物回顧指出：
- Fenoprofen 2.4g/day 療效與 aspirin 3.6-4g/day 相當
- 胃腸道副作用較 aspirin 少且輕微
- 可用於類風濕性關節炎、退化性關節炎、僵直性脊椎炎和痛風

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Fenoprofen 的不重複許可證共 **10 張**：有效單方 2 張、有效複方 0 張、已註銷 8 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第037862號 | 伏炎痛膠囊 | 膠囊劑 | 西德有機化學藥品股份有限公司 | 2029/08/02 | 鎮痛。 |
| 衛署藥製字第041435號 | "應元"炎普朗膠囊２００毫克（芬諾普芬） | 膠囊劑 | 應元化學製藥股份有限公司 | 2027/06/26 | 鎮痛。 |

<details><summary><strong>已註銷</strong>（8 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第011765號</td><td>風諾保膠囊３００公絲</td><td>FENOPROFEN (CALCIUM)</td><td>2002/09/02</td></tr><tr><td>衛署藥製字第022278號</td><td>痛保膠囊２００公絲（芬諾普芬）</td><td>FENOPROFEN (CALCIUM)</td><td>2002/09/02</td></tr><tr><td>衛署藥輸字第001373號</td><td>菲諾普魯芬鈣</td><td>FENOPROFEN CALCIUM</td><td>1987/09/21</td></tr><tr><td>衛署藥輸字第015760號</td><td>芬諾普芬鈣（膠囊用）</td><td>FENOPROFEN CALCIUM</td><td>2016/05/18</td></tr><tr><td>衛署藥輸字第016969號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第019161號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019882號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第019945號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>2000/10/18</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**注意**：多數 fenoprofen 製劑已註銷，目前在台灣取得較困難。

## 安全性考量

### 已知風險
- **胃腸道風險**：潰瘍、出血、穿孔
- **心血管風險**：NSAIDs 類效應，可能增加心血管事件風險
- **腎臟風險**：可能導致急性腎損傷，尤其在脫水狀態
- **過敏反應**：aspirin 過敏者可能交叉過敏

### 藥物交互作用

根據 DDInter 資料庫：

| 交互作用藥物 | 嚴重度 | 說明 |
|-------------|--------|------|
| Acetylsalicylic acid | Moderate | 增加胃腸道出血風險 |
| Hydrocortisone | Moderate | 增加胃腸道副作用 |
| Metformin | Moderate | 可能增加乳酸中毒風險 |
| Triamcinolone | Moderate | 增加胃腸道副作用 |
| Famotidine | Minor | 可降低 NSAIDs 相關潰瘍風險 |
| Ranitidine | Minor | 可降低 NSAIDs 相關潰瘍風險 |

### 禁忌症
- 活動性胃腸道潰瘍或出血
- 嚴重心衰竭
- 冠狀動脈繞道手術前後
- 對 NSAIDs 或 aspirin 過敏

### 特殊族群
- **孕婦**：C 級(第三孕期 D 級)，避免使用
- **哺乳**：分泌至乳汁，不建議使用
- **老年人**：增加胃腸道出血風險，建議最低有效劑量
- **腎功能不全**：避免使用或減量

## 結論與下一步

### 整體評估
僵直性脊椎炎的預測**具有臨床價值**，原因如下：
1. 多個歷史 RCT 支持 fenoprofen 對僵直性脊椎炎的療效
2. NSAIDs 是僵直性脊椎炎的一線治療藥物
3. 部分原核准適應症已涵蓋此用途

其他預測（如罕見骨骼發育異常）缺乏證據，不建議應用。

### 建議行動
- [x] 僵直性脊椎炎可作為 fenoprofen 的合理使用適應症
- [ ] 考量到 fenoprofen 在台灣取得困難，可優先選用其他同類 NSAIDs
- [ ] 其他預測的罕見疾病需要進一步研究

### 臨床建議
對於僵直性脊椎炎患者：
1. NSAIDs 仍是一線藥物選擇
2. Fenoprofen 是有效選項之一，但療效可能不如 indomethacin 或 naproxen
3. 若 fenoprofen 不可得，可選用其他丙酸類 NSAIDs

### 風險等級
**中等風險** - 僵直性脊椎炎使用有證據支持，但需注意 NSAIDs 通用風險

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、TFDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原核准適應症取自已註銷許可證 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「部分原核准適應症已包含關節強硬性脊椎炎」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L2） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

