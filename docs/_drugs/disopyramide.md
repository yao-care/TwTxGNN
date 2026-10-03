---
layout: default
title: Disopyramide
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Disopyramide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Disopyramide (待索匹拉邁) - 藥師評估報告

## 一句話總結

Disopyramide 是一種 Class Ia 抗心律不整藥物，TxGNN 預測其可能對妥瑞症、ADHD 和拔毛症等神經精神疾病有療效，但這些預測缺乏機轉支持和臨床證據，可能是知識圖譜中的假陽性關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Disopyramide (待索匹拉邁/二索匹拉麥) |
| DrugBank ID | DB00280 |
| 台灣商品名 | 福元心達寧膠囊 100mg |
| 原適應症 | 心室性不整律、心律不整 |
| 預測新適應症 | 妥瑞症、ADHD、拔毛症、多灶性心房頻脈、新生兒心房撲動 |
| 最高 TxGNN 分數 | 0.9986 (妥瑞症) |
| 臨床試驗支持 | 無 |
| 文獻支持 | 極弱（僅心律不整相關） |

## 為什麼預測合理

### 機轉分析

1. **妥瑞症 (Tourette syndrome)** - TxGNN 分數 0.9986：
   - Disopyramide 具有抗膽鹼作用
   - 妥瑞症涉及多巴胺系統異常
   - 但 disopyramide 主要作用於心臟鈉離子通道，對中樞神經系統的直接影響有限
   - **機轉連結薄弱**

2. **注意力不足過動症 (ADHD)** - TxGNN 分數 0.9982：
   - ADHD 主要與多巴胺和正腎上腺素通路相關
   - Disopyramide 無已知的中樞神經系統活性
   - **機轉連結極為薄弱**

3. **拔毛症 (trichotillomania)** - TxGNN 分數 0.9981：
   - 這是一種強迫相關障礙
   - 與 disopyramide 的藥理作用無關
   - **機轉連結極為薄弱**

4. **新生兒心房撲動 / 多灶性心房頻脈**：
   - 這些預測與原適應症（心律不整）直接相關
   - Disopyramide 作為 Class Ia 抗心律不整藥確實可能用於某些心房心律不整
   - **但已在原適應症範圍內**

### 預測品質評估

- 神經精神疾病預測（妥瑞症、ADHD、拔毛症）可能是知識圖譜中的假陽性關聯
- 這些預測可能源於藥物的抗膽鹼作用與某些神經疾病的間接關聯
- 心律不整相關預測與原適應症重疊

## 臨床試驗

**無相關臨床試驗**

未發現 disopyramide 用於妥瑞症、ADHD 或其他預測新適應症的臨床試驗。

## 文獻證據

### 多灶性心房頻脈相關文獻

1. **Somani P et al. (1980)** - Chest
   - 報告一例難治性心室和心房心律不整患者
   - 患者對多種藥物（包括 disopyramide）無效
   - 最終使用 lorcainide 成功治療
   - 相關性：僅提及 disopyramide 為失敗治療選項之一

### 神經精神疾病相關文獻

**無相關文獻**

未發現任何將 disopyramide 用於妥瑞症、ADHD 或拔毛症治療的文獻。

## 台灣上市狀態

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Disopyramide 的不重複許可證共 **28 張**：有效單方 2 張、有效複方 0 張、已註銷 26 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第025427號 | "福元"心達寧膠囊１００毫克 | 膠囊劑 | 福元化學製藥股份有限公司 | 2028/05/15 | 心室性不整律 |
| 衛署藥製字第055890號 | “應元”定律膠囊 100 毫克 | 膠囊劑 | 應元化學製藥股份有限公司 | 2030/12/23 | 心室性不整律。 |

<details><summary><strong>已註銷</strong>（26 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第005470號</td><td>律使當膠囊</td><td>DISOPYRAMIDE</td><td>1987/04/20</td></tr><tr><td>衛署藥輸字第005663號</td><td>諾培心膠囊</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>1993/12/03</td></tr><tr><td>衛署藥輸字第005950號</td><td>律使當注射液</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>1987/03/20</td></tr><tr><td>衛署藥輸字第007217號</td><td>諾培心注射液２０公絲/公撮</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第007876號</td><td>心律敏注射液１０公絲/公撮</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>1987/07/02</td></tr><tr><td>衛署藥輸字第008620號</td><td>心律敏膠囊１００公絲</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>1994/06/10</td></tr><tr><td>衛署藥輸字第010297號</td><td>磷酸二索匹拉麥</td><td>DISOPYRAMIDE PHOSPHATE</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第012826號</td><td>律使當持續性錠</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>1987/04/01</td></tr><tr><td>衛署藥輸字第013149號</td><td>磷酸二索匹拉麥粉劑</td><td>DISOPYRAMIDE PHOSPHATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第014016號</td><td>二索匹拉麥粉劑</td><td>DISOPYRAMIDE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第015016號</td><td>待索比樂邁</td><td>DISOPYRAMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015159號</td><td>磷酸待索匹拉邁</td><td>DISOPYRAMIDE PHOSPHATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015169號</td><td>待索匹拉邁</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015240號</td><td>磷酸待索匹拉邁</td><td>DISOPYRAMIDE PHOSPHATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015256號</td><td>二索匹拉麥</td><td>DISOPYRAMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015295號</td><td>磷酸二索匹拉麥</td><td>DISOPYRAMIDE PHOSPHATE</td><td>1995/01/31</td></tr><tr><td>衛署藥輸字第015693號</td><td>律使當注射液</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015694號</td><td>律使當持續性錠</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015752號</td><td>律使當膠囊</td><td>DISOPYRAMIDE</td><td>1996/07/24</td></tr><tr><td>衛署藥輸字第015861號</td><td>心律敏注射液１０公絲/公撮</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>1991/11/26</td></tr><tr><td>衛署藥輸字第016307號</td><td>心脈平膠囊１００公絲</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第020011號</td><td>待索匹拉邁</td><td>DISOPYRAMIDE BASE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第020096號</td><td>諾培心膠囊</td><td>DISOPYRAMIDE (PHOSPHATE)</td><td>2004/12/16</td></tr><tr><td>衛署藥輸字第020467號</td><td>司比樂膠囊</td><td>DISOPYRAMIDE</td><td>2000/06/05</td></tr><tr><td>衛署藥輸字第021474號</td><td>達舒脈膠囊１００公絲</td><td>DISOPYRAMIDE</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第022010號</td><td>待索匹拉邁</td><td>DISOPYRAMIDE</td><td>2005/06/15</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**現況**：台灣僅剩一項有效許可證，其他製劑均已註銷。市場供應有限。

## 安全性

### 重要藥物交互作用

| 併用藥物 | 嚴重程度 | 臨床意義 |
|----------|----------|----------|
| Clarithromycin | **Major** | QT 延長風險 |
| Cisapride | **Major** | QT 延長風險 |
| Granisetron | **Major** | QT 延長風險 |
| Dolasetron | **Major** | QT 延長風險 |
| Potassium citrate | **Major** | 低血鉀增加心律不整風險 |
| Eliglustat | **Major** | QT 延長風險 |
| 多種降血糖藥 | Moderate | 可能增強降血糖效果 |
| 抗膽鹼藥物 | Moderate | 抗膽鹼作用加成 |
| 類固醇 | Moderate | 電解質異常風險 |

### 重要警語

- **QT 延長**：可能引起尖端扭轉型室速 (Torsades de pointes)
- **負性肌力作用**：心衰竭患者禁用或謹慎使用
- **抗膽鹼作用**：尿滯留、口乾、便秘、視力模糊
- **低血糖**：可能增強胰島素和口服降血糖藥的作用
- **心臟傳導阻滯**：需監測心電圖

## 結論

### 整體評估：不推薦

Disopyramide 的 TxGNN 預測新適應症主要為神經精神疾病（妥瑞症、ADHD、拔毛症），這些預測極有可能是知識圖譜中的假陽性關聯，完全缺乏機轉支持和臨床證據。考慮到 disopyramide 的心臟毒性風險，將其用於神經精神疾病治療是不合理的。

### 建議

1. **強烈不建議**研究 disopyramide 用於神經精神疾病
2. 心律不整相關預測已在原適應症範圍內
3. 此藥物因安全性顧慮，使用已大幅減少，不適合老藥新用研究
4. TxGNN 對此藥物的預測可能反映了知識圖譜的限制

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 妥瑞症 | 0.9986 | 無 | 無 | 極低 | **不推薦** |
| ADHD | 0.9982 | 無 | 無 | 極低 | **不推薦** |
| 拔毛症 | 0.9981 | 無 | 無 | 極低 | **不推薦** |
| 新生兒心房撲動 | 0.9942 | 無 | 無 | 中等 | 已為適應症範疇 |
| 多灶性心房頻脈 | 0.9920 | 無 | 極弱 | 中等 | 已為適應症範疇 |

### 安全性警示

即使未來有任何研究興趣，disopyramide 的嚴重心臟毒性（QT 延長、負性肌力作用）使其成為高風險藥物，不適合用於非致命性神經精神疾病的治療。

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣僅剩一項有效許可證」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

