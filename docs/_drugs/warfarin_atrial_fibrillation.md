---
layout: default
title: Warfarin Atrial Fibrillation
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 0
---

# Warfarin Atrial Fibrillation
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Warfarin - Atrial Fibrillation（心房顫動）適應症評估

## 一句話總結

Warfarin 用於心房顫動（Atrial Fibrillation）的血栓預防**已是核准適應症**，
此為長期確立的標準治療，非新適應症預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品名稱 | Warfarin |
| DrugBank ID | DB00682 |
| 適應症 | 心房纖維顫動（Atrial Fibrillation）血栓預防 |
| 適應症狀態 | **已核准** |
| 證據等級 | L1（多個 RCT 支持） |
| 台灣上市 | 已上市 |
| 建議決策 | 標準治療（非老藥新用候選） |

## 背景說明

本筆記針對 Warfarin 在心房顫動的應用進行說明。

**重要聲明：**
此適應症並非 TxGNN 預測的「老藥新用」候選，而是已確立數十年的標準治療。Warfarin 自 1950 年代以來即被用於抗凝血治療，並在心房顫動的中風預防中扮演核心角色。

## 台灣核准適應症（TFDA）

根據多張現行許可證（欣服寧錠 1mg/5mg、可化凝錠等）：

```
1. 預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞
2. 預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症
```

## 臨床證據

### 關鍵臨床試驗

Warfarin 在心房顫動的療效已被多個大型 RCT 證實：

1. **SPAF 系列研究（1990s）**
   - Stroke Prevention in Atrial Fibrillation
   - 確立 Warfarin 可降低 AF 患者中風風險約 60-70%

2. **AFASAK 研究**
   - Copenhagen Atrial Fibrillation, Aspirin, Anticoagulation Study
   - 比較 Warfarin vs Aspirin vs 安慰劑

3. **後續與 DOAC 比較研究**
   - RE-LY（Dabigatran vs Warfarin）
   - ROCKET AF（Rivaroxaban vs Warfarin）
   - ARISTOTLE（Apixaban vs Warfarin）
   - ENGAGE AF-TIMI 48（Edoxaban vs Warfarin）

### 證據等級：L1

具有多個大型隨機對照試驗支持，證據等級最高。

## 臨床實務重點

### 適應症選擇

**優先考慮 Warfarin 的情況：**
- 機械性心臟瓣膜置換後
- 中度至重度風濕性二尖瓣狹窄
- 嚴重腎功能不全（CrCl < 15-30 mL/min）
- 抗磷脂質症候群
- DOAC 禁忌或不耐受

**可考慮 DOAC 優先的情況：**
- 非瓣膜性心房顫動
- 無法定期監測 INR
- 藥物交互作用顧慮較高

### INR 監測目標

| 適應症 | 目標 INR |
|--------|---------|
| 非瓣膜性心房顫動 | 2.0-3.0 |
| 機械性二尖瓣 | 2.5-3.5 |
| 機械性主動脈瓣（無其他風險因子） | 2.0-3.0 |

### 起始與維持劑量

- **起始劑量**：通常 2-5 mg/天，依患者特性調整
- **維持劑量**：個體差異大，需根據 INR 調整
- **藥物基因檢測**：CYP2C9、VKORC1 基因多型性可協助預測劑量需求

## 安全性考量

### 主要風險

1. **出血**：最重要的不良反應
   - 輕微出血（牙齦、瘀青）
   - 重大出血（腸胃道、顱內）

2. **藥物交互作用**
   - 增強效果：Aspirin、NSAID、部分抗生素、Amiodarone 等
   - 減弱效果：Rifampin、Carbamazepine、高維生素K食物

3. **皮膚壞死**（罕見但嚴重）
   - 通常發生在治療初期
   - 與 Protein C/S 缺乏有關

### 出血風險評估

使用 HAS-BLED 評分評估出血風險：
- Hypertension
- Abnormal renal/liver function
- Stroke history
- Bleeding history
- Labile INR
- Elderly (>65)
- Drugs/alcohol

## 台灣上市製劑

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Warfarin Atrial Fibrillation 的不重複許可證共 **37 張**：有效單方 14 張、有效複方 2 張、已註銷 21 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（14 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第043862號 | 〝政德〞可化凝錠１毫克 | 錠劑 | 政德製藥股份有限公司 | 2030/07/19 | 靜脈栓塞症。 |
| 衛署藥製字第050068號 | 欣服寧 錠 1 毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2029/03/26 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥製字第050230號 | 欣服寧 錠 3 毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2029/07/14 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥製字第050423號 | 脈化寧 錠 2.5 毫克 | 錠劑 | 恆振企業有限公司 | 2029/08/17 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥製字第052458號 | 欣服寧 錠5毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2030/01/15 | 1.預防及/或治療靜脈栓塞症及相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥製字第055237號 | 欣服寧錠 2.5 毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2030/07/29 | 1.預防及/或治療靜脈栓塞症及相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥製字第055271號 | “政德”可化凝錠 5 毫克 | 錠劑 | 政德製藥股份有限公司 | 2030/08/30 | 1.預防及/或治療靜脈栓塞症及相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥輸字第023572號 | 歐服寧錠５公絲 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2027/10/23 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。 2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥輸字第023573號 | 歐服寧錠3公絲 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2027/10/23 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。 2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛部藥製字第060168號 | 瓦寧錠5毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2028/09/05 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛部藥製字第060318號 | 瓦寧錠2.5毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2029/07/10 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛部藥製字第060391號 | 瓦寧錠1毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2029/11/21 | 1.預防及/或治療靜脈栓塞症及相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛部藥製字第060563號 | 瓦寧錠3毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2030/10/08 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛部藥輸字第026478號 | 苯甲香豆醇鈉籠晶 | （粉） | 新雙隆生技股份有限公司 | 2029/12/29 | 抗凝血劑 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第050095號 | 脈化寧 錠 5 毫克 | WARFARIN SODIUM CLATHRATE、WARFARIN SODIUM CLATHRATE | 錠劑 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。 2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |
| 衛署藥製字第052559號 | 脈化寧 錠 1 毫克 | WARFARIN SODIUM CLATHRATE、WARFARIN SODIUM CLATHRATE | 錠劑 | 1.預防及/或治療靜脈栓塞症及其相關疾病，以及肺栓塞。2.預防或治療因心房纖維顫動及/或更換心臟瓣膜引起之血栓性栓塞症。 |

<details><summary><strong>已註銷</strong>（21 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第002493號</td><td>活福寧鈉片</td><td>WARFARIN SODIUM</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第002494號</td><td>活福寧鈉片</td><td>WARFARIN SODIUM</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第002938號</td><td>安汝命－Ｋ</td><td>WARFARIN POTASSIUM</td><td>1985/07/01</td></tr><tr><td>內衛藥輸字第003471號</td><td>可邁丁錠１０公絲</td><td>WARFARIN (SODIUM)</td><td>1986/10/15</td></tr><tr><td>內衛藥輸字第003472號</td><td>可邁丁錠５公絲</td><td>WARFARIN (SODIUM)</td><td>1986/10/15</td></tr><tr><td>衛署藥製字第045335號</td><td>"生達" 歐發靈鈉鹽</td><td>WARFARIN SODIUM</td><td>2023/06/30</td></tr><tr><td>衛署藥輸字第006396號</td><td>抗凝血原錠</td><td>WARFARIN POTASSIUM</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第014066號</td><td>活福寧鈉錠５公絲</td><td>WARFARIN SODIUM</td><td>1990/03/02</td></tr><tr><td>衛署藥輸字第014067號</td><td>活福寧鈉錠３公絲</td><td>WARFARIN SODIUM</td><td>1990/02/22</td></tr><tr><td>衛署藥輸字第015348號</td><td>可邁丁錠５公絲</td><td>WARFARIN SODIUM</td><td>1990/06/30</td></tr><tr><td>衛署藥輸字第015349號</td><td>可邁丁錠１０公絲</td><td>WARFARIN (SODIUM)</td><td>1990/06/30</td></tr><tr><td>衛署藥輸字第017512號</td><td>活福寧鈉錠５公絲</td><td>WARFARIN SODIUM</td><td>2009/06/28</td></tr><tr><td>衛署藥輸字第017514號</td><td>活福寧鈉錠３公絲</td><td>WARFARIN SODIUM</td><td>2009/06/28</td></tr><tr><td>衛署藥輸字第017523號</td><td>苯甲香豆醇鈉</td><td>WARFARIN (SODIUM)</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第017879號</td><td>可邁丁錠１０公絲</td><td>WARFARIN (SODIUM)</td><td>1994/09/07</td></tr><tr><td>衛署藥輸字第017880號</td><td>可邁丁錠５公絲</td><td>WARFARIN SODIUM</td><td>1994/09/07</td></tr><tr><td>衛署藥輸字第020346號</td><td>可邁丁錠２．５公絲</td><td>WARFARIN SODIUM</td><td>2020/04/16</td></tr><tr><td>衛署藥輸字第020354號</td><td>可邁丁錠1毫克</td><td>WARFARIN SODIUM CRYSTALLINE</td><td>2020/04/16</td></tr><tr><td>衛署藥輸字第020515號</td><td>可邁丁錠１０公絲</td><td>WARFARIN SODIUM</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第020516號</td><td>可邁丁錠５毫克</td><td>WARFARIN SODIUM</td><td>2019/04/25</td></tr><tr><td>衛署藥輸字第023426號</td><td>瓦化寧錠5公絲</td><td>WARFARIN SODIUM</td><td>2016/05/31</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 與 TxGNN 預測的關聯

本專案（TwTxGNN）使用 TxGNN 模型預測 Warfarin 的潛在新適應症。

**預測結果顯示：**
- Heparin Cofactor 2 Deficiency（99.87%）
- Factor 5 Excess with Spontaneous Thrombosis（99.84%）
- Antithrombin Deficiency Type 2（99.84%）

上述為真正的「老藥新用」候選適應症，詳見 [Warfarin 主要藥師筆記](../warfarin/drug_pharmacist_notes.md)。

心房顫動作為已核准適應症，不在預測範圍內。

## 結論

**此筆記為參考性質說明**

Warfarin 用於心房顫動是已確立的標準治療，具有 L1 等級證據支持。
醫療人員應依據現行治療指引及個別患者特性選擇抗凝血治療。

**相關資源：**
- [Warfarin 完整藥師筆記（含新適應症預測）](../warfarin/drug_pharmacist_notes.md)
- [Warfarin - AF 簡要說明](../warfarin_af/drug_pharmacist_notes.md)
- 台灣心臟學會心房顫動治療指引

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

