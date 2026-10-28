---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 3
monitor_inn: "Probenecid"
predicted_indications: ["hypouricemia, renal", "Lesch-Nyhan syndrome", "hypoxanthine guanine phosphoribosyltransferase partial deficiency"]
last_modified_at: 2026-10-29
description: "Probenecid：預測新適應症為腎性低尿酸血症 (hypouricemia, renal)（證據等級 L5）。原適應症：痛風、痛風性關節炎、青黴素及 PAS 之血中濃度增強維持"
---

# Probenecid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Probenecid：從痛風到腎性低尿酸血症（預測不合理，建議暫緩）
{: .text-alpha }

## 一句話總結

Probenecid 是一種促尿酸排泄藥物，原本用於痛風與痛風性關節炎，也用來提高青黴素類抗生素的血中濃度。
TxGNN 模型預測它可能對**腎性低尿酸血症 (hypouricemia, renal)** 有效，但目前**沒有臨床試驗**，雖有 **20 篇文獻**，皆為疾病描述或病例報告，沒有任何一篇顯示藥物能治療此病。
從機轉判斷，這個預測很可能是假關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痛風、痛風性關節炎、青黴素及 PAS 之血中濃度增強維持 |
| 預測新適應症 | 腎性低尿酸血症 (hypouricemia, renal) |
| TxGNN 預測分數 | 0.9973 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 18 張） |
| 許可證數 | 18 張（有效單方 1／有效複方 0／已過期 1／已註銷 16） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Probenecid 是促尿酸排泄藥物，會抑制腎小管對尿酸的再吸收（主要作用於 URAT1，即 SLC22A12），因此增加尿酸從腎臟排出，血中尿酸下降。

腎性低尿酸血症，則是因為 URAT1 功能喪失，導致尿酸排出過多、血中尿酸過低。兩者在「腎臟尿酸轉運」上高度相關，這大概就是模型給出高分的原因。

不過方向正好相反：Probenecid 會促進尿酸排出，對這類病人不但無益，還可能加重低尿酸狀態。文獻中也有病例用 Probenecid 作為診斷試驗，觀察尿酸清除率的反應，並非治療用途。因此這個高分預測**很可能是假關聯**，不應視為真正的再利用機會。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻多為疾病本身的描述，並非藥物治療證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | 遺傳性腎性低尿酸血症多因 SLC22A12（URAT1）功能喪失突變所致 |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | 為風濕科醫師整理低尿酸血症的病因與臨床處置 |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Review | Am J Kidney Dis | 腎性低尿酸血症可能併發運動誘發急性腎衰竭，並討論預防方式 |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | 尿酸代謝異常的概念與分類 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Case series | J Am Soc Nephrol | 分析 32 位日本患者，探討 URAT1 基因對尿酸排泄的影響 |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case series | Nephron | 家族性低尿酸血症患者對 Probenecid 與 pyrazinamide 的尿酸清除反應減弱 |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case series | Arch Intern Med | 糖尿病患者的腎性低尿酸血症與尿酸清除率增加有關 |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Case series | Nephron | 第一型糖尿病患者出現腎性低尿酸血症 |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Case series | Am J Kidney Dis | 膽管癌合併嚴重腎性低尿酸血症的腎臟機轉研究 |
| [9583212](https://pubmed.ncbi.nlm.nih.gov/9583212/) | 1998 | Case series | Acta Paediatr Jpn | 一名女童因腎性低尿酸血症，在短跑後發生急性腎衰竭 |

另有 10 篇多為病例報告或基礎研究，內容同樣是描述疾病或以 Probenecid 作診斷試驗，未見治療效果的證據。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Probenecid 的不重複許可證共 **18 張**：有效單方 1 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 16 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第007256號 | 彼洛喜錠 | 錠劑 | 強生化學製藥廠股份有限公司 | 2029/05/25 | 痛風、痛風性關節炎、青黴素及ＰＡＳ之血中濃度增強維持 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第039128號</td><td>" 華盛頓 " 伏痛錠500毫克（三丙酸苯甲胺）</td><td>PROBENECID</td><td>2025/08/02</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（16 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第004804號</td><td>普樂倍尼西特錠</td><td>PROBENECID</td><td>1990/12/06</td></tr><tr><td>衛署藥製字第007392號</td><td>普魯便使特</td><td>PROBENECID</td><td>1994/11/16</td></tr><tr><td>衛署藥製字第010138號</td><td>方你邁錠</td><td>PROBENECID</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第013617號</td><td>普泌錠</td><td>PROBENECID</td><td>2013/10/01</td></tr><tr><td>衛署藥製字第025224號</td><td>歐力彼樂錠</td><td>COLCHICINE、PROBENECID</td><td>2025/07/29</td></tr><tr><td>衛署藥製字第027837號</td><td>優耐膜衣錠５００公絲（普魯必喜）</td><td>PROBENECID</td><td>1997/04/07</td></tr><tr><td>衛署藥製字第040720號</td><td>普耐膜衣錠５００公絲（二丙磺胺苯甲酸）</td><td>PROBENECID</td><td>2016/09/08</td></tr><tr><td>衛署藥輸字第000626號</td><td>普魯使他</td><td>PROBENECID</td><td>1994/06/08</td></tr><tr><td>衛署藥輸字第000855號</td><td>倍耐黴錠０．５公克</td><td>PROBENECID</td><td>1992/10/17</td></tr><tr><td>衛署藥輸字第002108號</td><td>普魯使他</td><td>PROBENECID</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第004043號</td><td>普魯使他</td><td>PROBENECID</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006131號</td><td>對－（雙丙基胺磺醯）安息香酸</td><td>PROBENECID</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006183號</td><td>普羅便泄</td><td>PROBENECID</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第019315號</td><td>倍耐黴錠０．５公克</td><td>PROBENECID</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第021235號</td><td>倍耐黴錠５００公絲</td><td>PROBENECID</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第021254號</td><td>二丙磺胺苯甲酸</td><td>PROBENECID</td><td>2009/12/31</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單文字）：肝衰竭、腎臟疾病、腎功能不全、血液疾病、血小板低下、白血球低下、顆粒球缺乏症、嗜中性白血球低下、消化性潰瘍、肌病變、橫紋肌溶解症、腹瀉性疾病、困難梭狀芽孢桿菌結腸炎等。
- **藥物交互作用**：共查得 71 筆，以下為部分重點：
  - 重大 (Major)：Phenylbutyric acid、Glycerol phenylbutyrate
  - 中度 (Moderate)：Acetylsalicylic acid（阿斯匹靈）、磺醯脲類降血糖藥（Chlorpropamide、Glimepiride、Glipizide、Glyburide、Tolbutamide、Tolazamide、Acetohexamide）、Repaglinide、Nateglinide
  - 輕度 (Minor)：Famotidine、Amoxicillin、Levofloxacin 等

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測僅有模型分數，沒有臨床試驗，文獻也只描述疾病，缺乏藥物療效證據（L5）。
- Probenecid 促進尿酸排泄，與 URAT1 功能喪失造成的疾病機轉方向相反，可能加重病情，高分應視為假關聯。

**若要推進需要：**
- 先釐清機轉：確認是否有任何理論或實驗證據顯示 Probenecid 對此疾病有益。目前判斷為無，建議不要投入資源。
- 補齊 Probenecid 的作用機轉資料。
- 若仍要探索尿酸代謝相關的其他預測（Lesch-Nyhan 症候群、HPRT 部分缺乏症），目前同樣僅有模型預測（L5）；這些疾病的尿酸產生過多，促尿酸排泄雖在理論上可降低血中尿酸，卻會增加尿路結石風險。標準治療是抑制黃嘌呤氧化酶，並無直接臨床證據支持 Probenecid，同樣建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

