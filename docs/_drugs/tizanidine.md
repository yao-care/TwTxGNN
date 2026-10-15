---
layout: default
title: Tizanidine
parent: 高證據等級 (L1-L2)
nav_order: 282
evidence_level: L2
indication_count: 6
---

# Tizanidine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **6** 個
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

# Tizanidine：從神經疾患所致痙攣到偏頭痛

## 一句話總結

Tizanidine 是中樞型 α2 腎上腺素受體促效劑，原本用於神經疾患所引起的痙攣症狀與疼痛性肌肉痙攣。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **1 個直接相關的 Phase 3 臨床試驗（結果尚未公布）**和 **17 篇文獻**支持這個方向，其中包含 1 篇針對慢性每日頭痛預防的安慰劑對照 RCT。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 神經疾患所引起之痙攣症狀、疼痛性肌肉痙攣 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L2（依資料彙整的評分；惟 Phase 3 試驗狀態未知、無結果，實質證據偏向間接） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 10 張（有效單方 8／有效複方 0／已註銷 2） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中的 MOA 欄位為空）。根據已知藥理資訊，Tizanidine 是中樞型 α2 腎上腺素促效劑，可能抑制三叉神經痛覺傳導，並減輕顱周肌肉緊繃。

原適應症為痙攣與疼痛性肌肉痙攣，與偏頭痛、慢性每日頭痛預防在「肌肉張力與疼痛傳導調節」上有共通之處。文獻回顧（如 Freitag 2003、Mathew 2006）也將 Tizanidine 列為慢性偏頭痛或慢性每日頭痛的預防選項之一。

需注意：現有證據多集中在慢性每日頭痛（含慢性偏頭痛、緊縮型頭痛），對偏頭痛本身的直接證據仍待 Phase 3 試驗結果確認。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | 狀態未知 | 189 | 多中心、隨機、雙盲、安慰劑對照，評估口服 Tizanidine 預防成人發作性偏頭痛的療效、安全性與耐受性；預計 2025-12 完成，尚無結果 |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | 完成 | 300 | 外用 NSAID 止痛療效的觀察性研究，與 Tizanidine 及偏頭痛關聯有限，僅屬間接參考 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | 雙盲、安慰劑對照多中心研究，評估 Tizanidine 作為慢性每日頭痛輔助預防治療的療效 |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | 三叉神經痛藥物治療更新，涵蓋偏頭痛相關新藥，與 Tizanidine 關聯間接 |
| [20442572](https://pubmed.ncbi.nlm.nih.gov/20442572/) | 2010 | Review | Curr Opin Neurol | 慢性偏頭痛治療新進展 |
| [31365643](https://pubmed.ncbi.nlm.nih.gov/31365643/) | 2019 | Review | Arq Neuropsiquiatr | 巴西頭痛學會慢性偏頭痛治療共識 |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Curr Pain Headache Rep | 偏頭痛預防新選項，含 Tizanidine |
| [19188563](https://pubmed.ncbi.nlm.nih.gov/19188563/) | 2009 | Review | Neurology | 慢性偏頭痛治療的動態優化 |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Review | Headache | 慢性每日頭痛預防治療，提及 Tizanidine |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | 作用於肌肉痙攣與張力的藥物（含 Tizanidine）用於偏頭痛與緊縮型頭痛預防 |
| [12221150](https://pubmed.ncbi.nlm.nih.gov/12221150/) | 2002 | Review | Neurology | 慢性頭痛治療策略新進展 |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | 動物研究 | J Control Release | Tizanidine 與 Meloxicam 超分子共晶，在偏頭痛模型中展現協同抗偏頭痛效果 |

另有開放標記劑量滴定研究（PMID 11318882）、止痛藥反彈性頭痛戒斷處方（PMID 11903539）等文獻，為較低層級的支持證據。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tizanidine 的不重複許可證共 **10 張**：有效單方 8 張、有效複方 0 張、已註銷 2 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（8 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第045439號 | 肌得樂錠4毫克 | 錠劑 | 寶齡富錦生技股份有限公司 | 2028/03/24 | 神經疾患所引起的痙攣症狀、疼痛性肌肉痙攣。 |
| 衛署藥製字第045541號 | 舒體錠２毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2028/05/12 | 神經疾患所引起之痙性張力異常(spasticity)；疼痛性肌肉攣縮(spasm)。 |
| 衛署藥製字第045755號 | 肌得樂錠2毫克 | 錠劑 | 寶齡富錦生技股份有限公司 | 2028/09/18 | 神經疾患所之痙攣症狀、疼痛性肌肉痙攣。 |
| 衛署藥製字第046447號 | "政德" 筋舒寧錠2毫克 | 錠劑 | 政德製藥股份有限公司 | 2029/08/10 | 神經疾患所引起之痙攣症狀，疼痛性肌肉痙攣。 |
| 衛署藥製字第046489號 | "十全" 痙汰錠2 毫克 | 錠劑 | 十全實業股份有限公司 | 2029/09/13 | 神經疾患所引起之痙攣症狀、疼痛性肌肉痙攣。 |
| 衛署藥製字第048176號 | 立舒肌錠2毫克 | 錠劑 | 永信藥品工業股份有限公司 | 2031/08/17 | 疼痛性肌肉痙攣：神經疾患所引起之痙攣症狀。 |
| 衛署藥輸字第019626號 | 鬆得樂錠2毫克 | 錠劑 | 台灣山德士藥業股份有限公司 | 2027/11/27 | 神經疾患所引起之痙性張力異常(spasticity)；疼痛性肌肉攣縮(spasm)。 |
| 衛署藥輸字第025425號 | 鹽酸提沙尼汀 | （粉） | 恒亞貿易股份有限公司 | 2031/05/23 | 骨骼肌鬆弛劑 |

<details><summary><strong>已註銷</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第018786號</td><td>鬆得樂錠4毫克</td><td>TIZANIDINE (AS HYDROCHLORIDE)</td><td>2022/06/16</td></tr><tr><td>衛署藥輸字第024113號</td><td>鹽酸提沙尼汀</td><td>TIZANIDINE HYDROCHLORIDE</td><td>2014/01/24</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**：肝衰竭、腎臟疾病、膿輸尿管、精神病性疾患、類精神分裂症疾患、精神疾患、情感性分裂症、低血壓疾患
- **藥物交互作用**：共記錄 249 筆。主要（Major）等級包括 Famotidine、Cimetidine、Morphine、Dolasetron、Obeticholic acid；中度（Moderate）包括 Clarithromycin、Levofloxacin、Metoclopramide、Atropine 等。另有資料指出需留意 CYP1A2 抑制劑（如 fluvoxamine、ciprofloxacin）造成的暴露量上升，以及低血壓與鎮靜風險。

其他警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有針對偏頭痛預防的 Phase 3 試驗登記，並有慢性每日頭痛的安慰劑對照 RCT 及多篇文獻回顧支持，TxGNN 分數也很高。但 Phase 3 試驗狀態未知、無公布結果，因此仍需謹慎推進。
- 藥物交互作用多、有低血壓與鎮靜風險，需設置安全防護。

**若要推進需要：**
- 確認 NCT05484349 的最新狀態與結果
- 補齊作用機轉資料（MOA）
- 建立 CYP1A2 抑制劑併用、低血壓、肝腎功能監測的用藥指引
- 釐清偏頭痛（相對於慢性每日頭痛）的直接療效證據
- 評估台灣現有劑型與劑量用於頭痛預防的可行性及仿單適應症變更需求

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 立舒肌錠效期 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

