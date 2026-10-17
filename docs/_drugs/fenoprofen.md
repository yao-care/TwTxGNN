---
layout: default
title: Fenoprofen
parent: 中證據等級 (L3-L4)
nav_order: 107
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-16
description: "Fenoprofen：預測新適應症為僵直性脊椎炎 (Ankylosing Spondylitis)（證據等級 L3）。原適應症：鎮痛"
monitor_inn: "Fenoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "WHIM syndrome"]
---

# Fenoprofen
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Fenoprofen：從鎮痛到僵直性脊椎炎

<!-- review:begin fenoprofen-why-as-premise-title-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「# Fenoprofen：從疼痛與風濕性關節炎到僵直性脊椎炎」。TFDA 許可證資料中，fenoprofen 現行有效的 2 張許可證（「應元」炎普朗膠囊、伏炎痛膠囊）核准適應症都只有「鎮痛」；風濕性關節炎、骨關節炎、關節強硬性脊椎炎等適應症屬於衛署藥製字第011765號「風諾保膠囊」，該證已於 2002-09-02 註銷。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fenoprofen-why-as-premise-title-2026-10-16 -->

## 一句話總結

Fenoprofen（芬諾普芬）是一種非類固醇消炎止痛藥（NSAID），在台灣現行許可證核准的適應症只有「鎮痛」（風濕性關節炎、骨關節炎等見於已註銷的舊許可證）。
TxGNN 模型預測分數最高的是罕見骨骼發育疾病，但這些預測完全沒有證據支持。本報告改以**證據最完整的預測：僵直性脊椎炎 (Ankylosing Spondylitis)** 為主軸，目前有 **0 個臨床試驗**和 **9 篇文獻**（含 2 篇雙盲交叉試驗）支持這個方向。

<!-- review:begin fenoprofen-why-as-premise-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「在台灣原本用於鎮痛、消炎與解熱，並用於風濕性關節炎、骨關節炎等疾病。」。TFDA 許可證資料中，fenoprofen 現行有效的 2 張許可證（「應元」炎普朗膠囊、伏炎痛膠囊）核准適應症都只有「鎮痛」；風濕性關節炎、骨關節炎、關節強硬性脊椎炎等適應症屬於衛署藥製字第011765號「風諾保膠囊」，該證已於 2002-09-02 註銷。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fenoprofen-why-as-premise-summary-2026-10-16 -->

<!-- review:begin fenoprofen-why-as-premise-rct-count-2026-10-16 -->

> **查核加註（2026-10-16）**：本頁文獻證據表列有 3 篇雙盲交叉研究：PMID 7010512（對 phenylbutazone）、6996071（對 indomethacin 與安慰劑）、7026817（六種 NSAID 比較，資料庫標示為 Review）。原文保留。依據：[本頁「文獻證據」表](https://twtxgnn.yao.care/drugs/fenoprofen/)。

<!-- review:end fenoprofen-why-as-premise-rct-count-2026-10-16 -->

> 說明：預測清單第 1 名為 acromesomelic dysplasia, Hunter-Thompson type（預測分數 99.997%），但沒有任何臨床試驗或文獻，證據等級為 L5，建議為 Hold。第 1～9 名預測均屬此類，只有第 10 名的僵直性脊椎炎有文獻證據，因此以它作為評估重點。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鎮痛（有效單方許可證之核准適應症） |
| 預測新適應症 | 僵直性脊椎炎 (Ankylosing Spondylitis) |
| TxGNN 預測分數 | 99.94%（本藥預測清單第 10 名；全模型排名第 2006） |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 10 張（有效單方 2／有效複方 0／已註銷 8） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin fenoprofen-why-as-premise-rank-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「TxGNN 預測分數／99.94%（模型排名第 1839）」。依本站 TxGNN 深度學習預測檔 txgnn_dl_predictions.csv.gz（2026-10-12 產出），fenoprofen 對 ankylosing spondylitis 的分數 0.9994、全模型排名第 2006；在本藥報告採用的預測清單中排第 10。這個檔案沒有進 git，已與其他資料一併封存於 GitHub Release data-20261015 的 TwTxGNN-data 包（yao-care/txgnn 私有 repo，路徑 TwTxGNN/data/processed/txgnn_dl_predictions.csv.gz）。依據：[TwTxGNN TxGNN 深度學習預測檔 txgnn_dl_predictions.csv.gz（2026-10-12 產出；封存於 GitHub Release data-20261015 的 TwTxGNN-data 包，yao-care/txgnn 私有 repo）](https://github.com/yao-care/txgnn/releases/tag/data-20261015)。

<!-- review:end fenoprofen-why-as-premise-rank-2026-10-16 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fenoprofen 是丙酸類 NSAID，一般認為它透過抑制 COX-1 與 COX-2 來減少前列腺素合成，進而發揮消炎、止痛與解熱作用。

僵直性脊椎炎的核心症狀是脊椎與薦髂關節的發炎性疼痛與僵硬，NSAID 本來就是這類疾病的第一線治療。Fenoprofen 的原核准適應症中也包含關節強硬性脊椎炎（僵直性脊椎炎的舊稱），因此這個預測與其既有用途高度重疊，屬於合理性高但「新意」有限的預測。

<!-- review:begin fenoprofen-why-as-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：TFDA 許可證資料中，fenoprofen 現行有效的 2 張許可證（「應元」炎普朗膠囊、伏炎痛膠囊）核准適應症都只有「鎮痛」；風濕性關節炎、骨關節炎、關節強硬性脊椎炎等適應症屬於衛署藥製字第011765號「風諾保膠囊」，該證已於 2002-09-02 註銷。推論原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fenoprofen-why-as-premise-2026-10-03 -->

此外，已有雙盲交叉試驗將 Fenoprofen 與 phenylbutazone、indomethacin 比較，另有一項六種 NSAID 的雙盲研究顯示 fenoprofen calcium 在僵直性脊椎炎中屬於較有效的藥物之一。不過這些研究規模小、年代久遠（1970～1980 年代）。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7010512](https://pubmed.ncbi.nlm.nih.gov/7010512/) | 1980 | RCT | Rheumatology and Rehabilitation | 30 名患者雙盲交叉試驗，fenoprofen 600 mg 每日三次對比 phenylbutazone；phenylbutazone 顯著改善晨僵、疼痛等多項指標，fenoprofen 僅胸廓擴張度有改善 |
| [6996071](https://pubmed.ncbi.nlm.nih.gov/6996071/) | 1980 | RCT | Rheumatology and Rehabilitation | 雙盲交叉試驗，比較 indomethacin、fenoprofen 與安慰劑（無摘要可供摘錄結果） |
| [7026817](https://pubmed.ncbi.nlm.nih.gov/7026817/) | 1981 | 雙盲隨機交叉研究（資料庫標示為 Review） | JAMA | 六種 NSAID 比較；在僵直性脊椎炎中，naproxen、indomethacin 與 fenoprofen calcium 最有效 |
| [324748](https://pubmed.ncbi.nlm.nih.gov/324748/) | 1977 | Review | Drugs | 回顧 fenoprofen 的藥理與在風濕疾病的療效，指出可用於類風濕性關節炎、退化性關節病、僵直性脊椎炎與痛風 |
| [300118](https://pubmed.ncbi.nlm.nih.gov/300118/) | 1977 | Review | JAMA | 新型抗風濕藥回顧；fenoprofen 等可能適用於僵直性脊椎炎，但療效與劑量的資料不足 |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Review | Drugs | Naproxen 的回顧，與 fenoprofen 屬同類藥物，間接參考 |
| [391117](https://pubmed.ncbi.nlm.nih.gov/391117/) | 1979 | Review | Annals of Internal Medicine | Ibuprofen 回顧，提到其與 fenoprofen 化學結構相關，間接參考 |
| [4615887](https://pubmed.ncbi.nlm.nih.gov/4615887/) | 1974 | Case series | Current Medical Research and Opinion | Fenoprofen 作為新型抗風濕藥的臨床使用經驗（無摘要） |
| [36583943](https://pubmed.ncbi.nlm.nih.gov/36583943/) | 2023 | In vitro | ChemMedChem | Fenoprofen 的碳硼烷類似物具有較佳的抗腫瘤活性，屬前臨床研究，與僵直性脊椎炎無直接關係 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Fenoprofen 的不重複許可證共 **10 張**：有效單方 2 張、有效複方 0 張、已註銷 8 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第037862號 | 伏炎痛膠囊 | 膠囊劑 | 西德有機化學藥品股份有限公司 | 2029/08/02 | 鎮痛。 |
| 衛署藥製字第041435號 | "應元"炎普朗膠囊２００毫克（芬諾普芬） | 膠囊劑 | 應元化學製藥股份有限公司 | 2027/06/26 | 鎮痛。 |

<details><summary><strong>已註銷</strong>（8 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第011765號</td><td>風諾保膠囊３００公絲</td><td>FENOPROFEN (CALCIUM)</td><td>2002/09/02</td></tr><tr><td>衛署藥製字第022278號</td><td>痛保膠囊２００公絲（芬諾普芬）</td><td>FENOPROFEN (CALCIUM)</td><td>2002/09/02</td></tr><tr><td>衛署藥輸字第001373號</td><td>菲諾普魯芬鈣</td><td>FENOPROFEN CALCIUM</td><td>1987/09/21</td></tr><tr><td>衛署藥輸字第015760號</td><td>芬諾普芬鈣（膠囊用）</td><td>FENOPROFEN CALCIUM</td><td>2016/05/18</td></tr><tr><td>衛署藥輸字第016969號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第019161號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019882號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第019945號</td><td>芬諾普芬鈣</td><td>FENOPROFEN CALCIUM</td><td>2000/10/18</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **禁忌症（知識圖譜推論，非仿單內容）**：知識圖譜顯示本藥與下列疾病存在禁忌關聯，需對照原廠仿單確認：
  - 心血管：高血壓、鬱血性心衰竭、心肌梗塞、腦中風與腦梗塞、血栓性疾病、冠狀動脈血栓
  - 腎臟：腎臟病、腎乳頭壞死
  - 胃腸與肝臟：活動性消化性潰瘍、藥物性肝損傷
  - 血液：凝血疾病、貧血、血紅素病變
  - 其他：視覺障礙、聽覺障礙、物質濫用／依賴
- **藥物交互作用**：共查得 159 筆，以下為部分範例：
  - 中度：乙醯水楊酸（阿斯匹靈）、hydrocortisone、dexamethasone、betamethasone、triamcinolone、budesonide、metformin、glimepiride、chlorpropamide、mesalazine、balsalazide、檸檬酸鉀與碳酸氫鉀
  - 輕度：famotidine、ranitidine、cimetidine、linaclotide

其餘警語請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 僵直性脊椎炎是預測清單中唯一有文獻支持的項目，且有雙盲交叉試驗，但研究規模小、年代久遠，且其中一項試驗顯示 fenoprofen 的療效不及 phenylbutazone。
- 此適應症與既有核准適應症（關節強硬性脊椎炎）重疊，屬於既有用途的再確認，而非真正的新適應症。
- 其餘 9 個預測（多為罕見骨骼發育疾病）僅有模型分數，無任何證據，建議全部 Hold。

<!-- review:begin fenoprofen-why-as-premise-conclusion-2026-10-16 -->

> **查核加註（2026-10-16）**：TFDA 許可證資料中，fenoprofen 現行有效的 2 張許可證（「應元」炎普朗膠囊、伏炎痛膠囊）核准適應症都只有「鎮痛」；風濕性關節炎、骨關節炎、關節強硬性脊椎炎等適應症屬於衛署藥製字第011765號「風諾保膠囊」，該證已於 2002-09-02 註銷。推論原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fenoprofen-why-as-premise-conclusion-2026-10-16 -->

**若要推進需要：**
- 取得 Fenoprofen 完整的作用機轉資料
- 與現行第一線 NSAID（如 naproxen、celecoxib）及生物製劑做療效與安全性比較
- 針對心血管、腎臟與胃腸道風險設計安全性監測，特別是高風險族群
- 確認現行有效許可證（鎮痛）的核准適應症是否需要擴增，並對照原廠仿單

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原核准適應症取自已註銷許可證 | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列為有效許可證的「鎮痛」；標題、一句話總結、預測理由與結論仍把已註銷許可證的關節炎適應症當原用途，另有查核紀錄處理；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「原核准適應症中也包含關節強硬性脊椎炎」 | 加註（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L3，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L2）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |
| 2026-10-16 | 標題以風濕性關節炎為原用途 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結把已註銷許可證的適應症寫成原用途 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 結論稱與既有核准適應症（關節強硬性脊椎炎）重疊 | 加註（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 模型排名寫第 1839 | 更正（2026-10-16 修訂，前版保留於紀錄） | [TwTxGNN TxGNN 深度學習預測檔 txgnn_dl_predictions.csv.gz（2026-10-12 產出；封存於 GitHub Release data-20261015 的 TwTxGNN-data 包，yao-care/txgnn 私有 repo）](https://github.com/yao-care/txgnn/releases/tag/data-20261015) |
| 2026-10-16 | 一句話總結稱含 2 篇雙盲交叉試驗 | 加註 | [本頁「文獻證據」表](https://twtxgnn.yao.care/drugs/fenoprofen/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

