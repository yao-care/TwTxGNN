---
layout: default
title: Fluphenazine
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-16
description: "Fluphenazine：預測新適應症為視網膜失養症 (Retinal dystrophy with or without extraocular anomalies)（證據等級 L5）。原適應症：精神病狀態、噁心、嘔吐"
---

# Fluphenazine
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

# Fluphenazine：從精神病狀態到視網膜失養症

## 一句話總結

Fluphenazine（氟芬那辛）是典型抗精神病藥物，原本用於精神病狀態、噁心與嘔吐。
TxGNN 模型預測它可能對**視網膜失養症（Retinal dystrophy with or without extraocular anomalies）**有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 精神病狀態、噁心、嘔吐 |
| 預測新適應症 | 視網膜失養症 (Retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 18 張（有效單方 1／有效複方 0／已註銷 17） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理背景，Fluphenazine 是多巴胺 D2 受體拮抗劑，同時也具有鈣調蛋白（calmodulin）抑制作用。視網膜中的多巴胺訊號與視網膜生理功能有關，這是此預測唯一可推想的機轉連結。

然而，目前沒有證據顯示此藥與遺傳性視網膜失養症有直接關聯。原適應症（精神病狀態）與預測的新適應症（遺傳性視網膜疾病）在疾病性質上差異很大，此預測僅來自知識圖譜模型，應視為待驗證的假說。

**其他高分預測的整體觀察：**
資料中排名前 9 的預測（視網膜失養症、症候群性近視、X 連鎖近視、無腦回/水腦畸形、糖基化先天異常、夏柯-馬利-杜斯氏症 1G 型、多小腦回畸形、非典型甘胺酸腦病變等）皆無臨床試驗或文獻支持，機轉連結多為推測，部分（如近視）甚至可能因 D2 拮抗而產生反效果。

排名第 10 的**躁期雙相情感疾病（Manic bipolar affective disorder）**是唯一有間接文獻支持的預測（TxGNN 分數 99.98%，證據等級 L4，建議為「研究問題」）。D2 受體阻斷與抗躁效果在機轉上一致，但現有文獻多為長效針劑抗精神病藥的類別回顧，並無 fluphenazine 專屬的試驗。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（視網膜失養症）目前無相關文獻。

作為參考，排名第 10 的預測（躁期雙相情感疾病）有以下較相關的文獻（皆為間接證據）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22494448](https://pubmed.ncbi.nlm.nih.gov/22494448/) | 2012 | Review | CNS Drugs | 回顧第一、二代長效針劑抗精神病藥用於雙相情感疾病維持治療的療效與安全性；第一代藥物尚未被核准用於此病 |
| [26243837](https://pubmed.ncbi.nlm.nih.gov/26243837/) | 2015 | 系統性回顧與專家共識 | Clin Psychopharmacol Neurosci | 長效針劑抗精神病藥（含 fluphenazine decanoate）可改善服藥順從性並減少復發 |
| [36779113](https://pubmed.ncbi.nlm.nih.gov/36779113/) | 2023 | 病例報告 | Cureus | 兩例有物質濫用史的雙相情感疾病患者，探討 fluphenazine 的仿單外使用 |
| [39756485](https://pubmed.ncbi.nlm.nih.gov/39756485/) | 2025 | 回溯性分析 | J Affect Disord | 評估躁期住院期間加用長效針劑對再住院率的影響 |
| [30129771](https://pubmed.ncbi.nlm.nih.gov/30129771/) | 2018 | 回溯性研究 | J Comp Eff Res | 比較雙相 I 型患者開始使用長效針劑後的住院風險 |
| [37345508](https://pubmed.ncbi.nlm.nih.gov/37345508/) | 2023 | Review | Expert Opin Pharmacother | 長效針劑抗精神病藥的轉換策略與實務做法 |
| [34353834](https://pubmed.ncbi.nlm.nih.gov/34353834/) | 2021 | 病例報告 | BMJ Case Rep | 使用 fluphenazine decanoate 的雙相患者發生非典型惡性抗精神病藥症候群 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Fluphenazine 的不重複許可證共 **18 張**：有效單方 1 張、有效複方 0 張、已註銷 17 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第035671號 | "瑞士"復康注射液25毫克/毫升(氟芬那辛) | 注射劑 | 瑞士藥廠股份有限公司 | 2027/09/10 | 精神病狀態、噁心、嘔吐。 |

<details><summary><strong>已註銷</strong>（17 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000571號</td><td>強力復安寧糖衣錠</td><td>FLUPHENAZINE HCL</td><td>2010/03/05</td></tr><tr><td>內衛藥製字第005613號</td><td>復安寧糖衣錠</td><td>FLUPHENAZINE HCL</td><td>2010/03/05</td></tr><tr><td>內衛藥製字第009321號</td><td>舒安靜糖衣錠</td><td>FLUPHENAZINE 2HCL</td><td>1999/07/30</td></tr><tr><td>內衛藥輸字第000894號</td><td>安添壽注射劑２．５ＭＧ/ＣＣ</td><td>FLUPHENAZINE HCL</td><td>1988/11/17</td></tr><tr><td>內衛藥輸字第004476號</td><td>靜得唯安Ｓ</td><td>MEPHOBARBITAL (METHYL PHENOBARBITAL)、FLUPHENAZINE、NIACINAMID…</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第004776號</td><td>靜得唯安Ｎ</td><td>TRIFLUOPERAZINE、PEMOLINE (PHENYLPSEUDOHYDANTOINPHENYLISOHYDA…</td><td>1999/09/22</td></tr><tr><td>衛署藥製字第034719號</td><td>保利神注射液２５公絲/公撮（氟芬那辛）</td><td>FLUPHENAZINE DECANOATE</td><td>2010/03/01</td></tr><tr><td>衛署藥輸字第002703號</td><td>鹽酸氟非那靜</td><td>FLUPHENAZINE HCL</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第003647號</td><td>謀對煩錠</td><td>NORTRIPTYLINE (HCL)、FLUPHENAZINE HCL</td><td>2004/08/19</td></tr><tr><td>衛署藥輸字第006777號</td><td>氟非那辛鹽酸鹽</td><td>FLUPHENAZINE 2HCL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第007282號</td><td>安添壽錠５公絲</td><td>FLUPHENAZINE 2HCL</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第012316號</td><td>保利神注射液</td><td>FLUPHENAZINE DECANOATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第016488號</td><td>寧法定注射液</td><td>FLUPHENAZINE DECANOATE</td><td>1997/12/17</td></tr><tr><td>衛署藥輸字第019401號</td><td>鹽酸氟芬那辛</td><td>FLUPHENAZINE HCL</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第019580號</td><td>保利神注射液</td><td>FLUPHENAZINE DECANOATE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第020896號</td><td>保利神注射液</td><td>FLUPHENAZINE DECANOATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第021881號</td><td>寧法定注射液</td><td>FLUPHENAZINE DECANOATE</td><td>2013/11/25</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 PrimeKG 藥物—疾病禁忌關聯，非仿單內容），主要包括：
  - 心血管：長 QT 症候群、尖端扭轉型心室頻脈、姿勢性低血壓、心肌梗塞、心臟傳導疾病、猝死性心臟驟停
  - 血液：嗜中性白血球低下、顆粒球缺乏症、白血球低下、血小板低下、貧血
  - 神經：癲癇、基底核疾病、眼瞼痙攣、多重系統萎縮
  - 其他：肝病、膽囊疾病、高血糖、良性攝護腺肥大、物質濫用/依賴、乳癌、肥胖

- **藥物交互作用**：資料庫共收錄 313 項交互作用，其中較重要的包括：
  - **嚴重（Major）**：Bupropion、Morphine
  - **中度（Moderate）**：Epinephrine、Metformin、Pioglitazone、Acarbose、Famotidine、Atropine、Hyoscyamine、Loperamide、多種皮質類固醇（Hydrocortisone、Dexamethasone 等）、Amphotericin B 等

詳細警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（視網膜失養症）僅有模型分數，沒有任何臨床試驗或文獻佐證，機轉連結也只是推測。
- 此藥具有 QT 延長、血球低下等重要安全風險，且 313 項交互作用需審慎評估，在缺乏療效訊號的情況下不宜推進。

**若要推進需要：**
- 補充詳細的作用機轉（MOA）資料。
- 進行視網膜多巴胺/鈣調蛋白相關的前臨床研究（細胞或動物模型），以驗證是否有治療訊號。
- 若優先考量有間接證據的方向，可改以**躁期雙相情感疾病**為研究問題，並蒐集 fluphenazine 專屬的對照試驗資料。
- 針對目標族群制定安全性監測計畫（心電圖/QT、血球計數、錐體外症候群）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

