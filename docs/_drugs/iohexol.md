---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Iohexol
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

# Iohexol：從脊椎／血管／泌尿道造影到失眠（預測）

## 一句話總結

Iohexol 是一種非離子型含碘造影劑，原本用於脊椎造影、血管造影、電腦斷層掃描增強造影與泌尿道造影。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，但目前**沒有任何臨床試驗與文獻**支持，屬於純模型預測，機轉上也缺乏合理依據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影 |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 18 張（有效單方 2／有效複方 2／已註銷 14） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Iohexol 是惰性的非離子型碘造影劑，作用在於影像對比，並無已知的鎮靜或調節睡眠的藥理活性。

失眠屬於中樞神經與睡眠調節問題，與造影劑的診斷用途沒有明顯關聯。TxGNN 的高分更可能來自知識圖譜中的間接關聯，而非真實的藥理連結。

其他排名較前的預測（焦慮、類風濕性關節炎、抗凝血酶缺乏、纖維肌痛、結膜炎、肌腱炎等）同樣缺乏機轉或臨床支持。文獻中 Iohexol 僅作為造影工具、腎絲球過濾率測量工具或過敏反應誘因出現，並非治療用途。因此，**本預測不建議視為合理的再利用方向**。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前沒有針對「失眠」的文獻。以下為次要預測（焦慮）下檢索到的文獻，僅供參考，內容皆非治療效益證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | 比較 iodixanol 與 iohexol 用於肢體靜脈攝影的療效、安全性與注射不適感，與焦慮治療無關 |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohort | Neuroradiology | 200 名腰椎脊髓造影患者的副作用分析，頭痛、噁心、頭暈及輕微精神症狀（含焦慮或憂鬱）較常見，屬不良反應而非療效 |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Cohort | Acta Neurochirurgica | 腦血管攝影期間以經顱都卜勒監測雙側腦血流動力學，屬技術與生理觀察 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Iohexol 的不重複許可證共 **18 張**：有效單方 2 張、有效複方 2 張、已註銷 14 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第022865號 | 〝奇異愛爾蘭廠〞安你拍克 注射劑350毫克碘/公撮 | 注射劑 | 奇異亞洲醫療設備股份有限公司 | 2030/04/27 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影。 |
| 衛署藥輸字第022866號 | "奇異愛爾蘭廠" 安你拍克 注射劑300毫克碘/公撮 | 注射劑 | 奇異亞洲醫療設備股份有限公司 | 2030/04/27 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第044709號 | 威能碘注射液300公絲碘/公撮 | IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL) | 注射劑 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影。 |
| 衛署藥製字第044720號 | 威能碘注射液350公絲碘/公撮 | TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL | 注射劑 | 脊椎造影、血管造影、電腦斷層掃瞄增強造影劑、泌尿道造影。 |

<details><summary><strong>已註銷</strong>（14 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第014483號</td><td>安你拍克注射劑３００毫克碘/公撮</td><td>IOHEXOL (ANHYDROUS)</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第014484號</td><td>安你拍克注射劑３５０毫克碘/公撮</td><td>IOHEXOL</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第015944號</td><td>安你拍克注射劑１８０毫克碘/公撮</td><td>TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第015975號</td><td>安你拍克注射劑２４０毫克碘/公撮</td><td>TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第020621號</td><td>安你拍克注射劑１８０毫克碘/公撮</td><td>TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第020622號</td><td>安你拍克注射劑２４０毫克碘/公撮</td><td>IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第020740號</td><td>安你拍克注射劑３５０毫克碘/公撮</td><td>IOHEXOL</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第020741號</td><td>安你拍克注射劑３００毫克碘/公撮</td><td>IOHEXOL (ANHYDROUS)、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO…</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第021651號</td><td>安你拍克注射劑２４０毫克碘／公撮</td><td>IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第021652號</td><td>安你拍克注射劑３００毫克碘／公撮</td><td>IOHEXOL (ANHYDROUS)</td><td>2023/11/15</td></tr><tr><td>衛署藥輸字第021653號</td><td>安你拍克注射劑３５０毫克碘／公撮</td><td>IOHEXOL</td><td>2023/11/16</td></tr><tr><td>衛署藥輸字第021654號</td><td>安你拍克注射劑１８０毫克碘／公撮</td><td>IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第023241號</td><td>"奇異愛爾蘭廠" 安你拍克 注射劑180毫克碘/公撮</td><td>IOHEXOL</td><td>2025/09/15</td></tr><tr><td>衛署藥輸字第023242號</td><td>"奇異愛爾蘭廠" 安你拍克 注射劑240毫克碘/公撮</td><td>IOHEXOL</td><td>2025/09/15</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 325 筆交互作用紀錄，其中多筆為 Major 等級，例如：
  - Metformin
  - Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone 等皮質類固醇
  - Amphotericin B
  - Vancomycin、Kanamycin、Neomycin 等胺基糖苷／糖肽類抗生素
  - Levofloxacin
  - Bupropion
  - Morphine
  - Metoclopramide
  - Mesalazine、Balsalazide

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 失眠預測僅來自 TxGNN 模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- Iohexol 是惰性造影劑，無已知中樞神經或睡眠調節作用，機轉上缺乏合理性。

**若要推進需要：**
- 提出可驗證的作用機轉假說，並補足 MOA 資料
- 完成前臨床或機轉研究，證明對睡眠調節有任何作用
- 評估造影劑給藥途徑與長期使用需求是否符合失眠治療情境
- 若無上述證據，建議不進一步投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

