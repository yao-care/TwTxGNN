---
layout: default
title: Vonoprazan
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 8
monitor_inn: "Vonoprazan"
predicted_indications: ["peptic ulcer perforation", "hiatus hernia (disease)", "achlorhydria", "Dieulafoy lesion", "cascade stomach", "pylorospasm", "gastric dilatation", "hemorrhagic duodenitis"]
last_modified_at: 2026-10-27
description: "Vonoprazan：預測新適應症為消化性潰瘍穿孔 (peptic ulcer perforation)（證據等級 L5）."
---

# Vonoprazan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Vonoprazan：鉀離子競爭型酸阻斷劑 → 消化性潰瘍穿孔 (peptic ulcer perforation)
{: .text-alpha }

## 一句話總結

Vonoprazan 是一種抑制胃酸分泌的口服藥物，在台灣已有上市許可證。
TxGNN 模型預測它可能對**消化性潰瘍穿孔 (peptic ulcer perforation)** 有關聯。
目前**沒有直接以此疾病為對象的臨床試驗或研究**，僅有 3 篇相關的潰瘍治療文獻（2 篇指引、1 篇統合分析）提供間接參考。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 1.	糜爛性食道炎(EE)的治療及維持治療。
 2.	治療胃潰瘍。
 3.	治療十二指腸潰瘍。
 4.	輔助根除幽門螺旋桿菌(Helicobacter pylori)。 |

| 預測新適應症 | 消化性潰瘍穿孔 (peptic ulcer perforation) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 3 張／共 4 張） |
| 許可證數 | 4 張（有效單方 3／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料，Vonoprazan 的作用標的為胃壁細胞的質子幫浦（H+/K+-ATPase，基因 ATP4A），屬於鉀離子競爭型酸阻斷劑，可強效抑制胃酸分泌。

消化性潰瘍穿孔的根本成因是胃酸與黏膜損傷造成的潰瘍。因此，抑制胃酸理論上可能有助於穿孔修補後底層潰瘍的癒合，並降低復發風險。

不過，穿孔是需要外科處置的急症，Vonoprazan 最多只能作為輔助用藥。目前支持這個方向的證據都來自未發生併發症的潰瘍研究，屬於間接推論，沒有針對穿孔本身的藥物研究。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39294424](https://pubmed.ncbi.nlm.nih.gov/39294424/) | 2024 | 統合分析 | Digestive Diseases and Sciences | 比較 Vonoprazan 與質子幫浦抑制劑用於胃或十二指腸潰瘍的治療與預防，探討其療效與安全性；對潰瘍的療效先前仍有爭議 |
| [33620586](https://pubmed.ncbi.nlm.nih.gov/33620586/) | 2021 | 指引（回顧） | Journal of Gastroenterology | 日本消化器病學會 2020 年消化性潰瘍實證指引，涵蓋出血性潰瘍、幽門螺旋桿菌根除、藥物性潰瘍與手術治療等 |
| [42635735](https://pubmed.ncbi.nlm.nih.gov/42635735/) | 2026 | 指引（回顧） | Journal of Gastroenterology | 2026 年第四版消化性潰瘍指引，內容包含穿孔與狹窄的保守治療，但摘要未顯示針對 Vonoprazan 的穿孔研究 |

以上文獻均未直接評估 Vonoprazan 對消化性潰瘍穿孔的效果。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Vonoprazan 的不重複許可證共 **4 張**：有效單方 3 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027623號 | 福星定膜衣錠20毫克 | 膜衣錠 | 台灣武田藥品工業股份有限公司 | 2029/08/12 | 1. 糜爛性食道炎(EE)的治療及維持治療。 2. 治療胃潰瘍。 3. 治療十二指腸潰瘍。 4. 輔助根除幽門螺旋桿菌(Helicobacter pylori)。 |
| 衛部藥輸字第029115號 | 芙諾抑瘍延胡索酸鹽 | （粉） | 丞泰企業有限公司 | 2031/03/12 | 胃潰瘍治療藥 |
| 衛部藥陸輸字第001272號 | 芙諾抑瘍反丁烯二酸鹽 | （粉） | 丞泰企業有限公司 | 2031/04/23 | 胃潰瘍治療藥 |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027622號</td><td>福星定膜衣錠10毫克</td><td>Vonoprazan Fumarate</td><td>2026/04/27</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

另外，已有病例報告指出長期使用 Vonoprazan 後，可能出現明顯的胃黏膜變化與停藥後的反彈性胃酸過度分泌。若用於潰瘍相關情境，需留意長期使用的風險。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 Vonoprazan 用於消化性潰瘍穿孔，因此證據等級僅為 L5。
- 穿孔是外科急症，藥物最多只能扮演輔助角色，現有資料不足以支持推進。

**若要推進需要：**
- 針對穿孔修補術後使用 Vonoprazan 的回溯性研究或前瞻性試驗，並以潰瘍癒合與復發為指標
- 與質子幫浦抑制劑的比較資料
- 完整的作用機轉與長期使用安全性資料
- 與外科及消化內科專家討論實際的臨床使用情境

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市資訊表「衛部藥輸字（待確認）福星定膜衣錠10毫克」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「許可證數：1 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

