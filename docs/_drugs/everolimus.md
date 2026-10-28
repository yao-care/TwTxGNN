---
layout: default
title: Everolimus
parent: 高證據等級 (L1-L2)
nav_order: 104
evidence_level: L2
indication_count: 8
monitor_inn: "Everolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
last_modified_at: 2026-10-29
description: "Everolimus：預測新適應症為脂肪肉瘤 (liposarcoma)（證據等級 L2）."
---

# Everolimus
{: .fs-9 }

證據等級: **L2** | 預測適應症: **8** 個
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

## Everolimus：mTOR 抑制劑 → 脂肪肉瘤 (liposarcoma)
{: .text-alpha }

## 一句話總結

Everolimus 是一種 mTOR 抑制劑，在台灣已有多張許可證，涵蓋器官移植抗排斥與多種癌症治療。
TxGNN 模型預測它可能對**脂肪肉瘤 (liposarcoma)** 有效，
目前有 **1 個臨床試驗**和 **4 篇文獻**與此方向相關，但 everolimus 在其中僅作為合併用藥的一環。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 「結節性硬化症併有腎血管肌脂肪瘤之成年病患」且須符合以下條件：其腎血管肌脂肪瘤最長直徑需≧4cm，且曾有發生臨床上有意義之出血或確認病灶有血管瘤（aneurysm）直徑≧5mm者，無法以外科手術或動脈栓塞治療，或經動脈栓塞治療或外科手術後無效或復發者。
 
 治療患有結節性硬化症(TS: tuberous sclerosis)相關腦室管膜下巨細胞星狀細胞瘤(SEGA: subependymal giant cell astrocytoma)且須介入治療但不適合接受治療性外科切除手術的患者。; 腎臟及心臟移植
 併用減量ciclosporin微乳製劑及類固醇，預防腎臟或心臟移植的成人病患之免疫器 |

| 預測新適應症 | 脂肪肉瘤 (liposarcoma) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L2 |
| 台灣上市 | 上市中（有效許可證 7 張／共 12 張） |
| 許可證數 | 12 張（有效單方 7／有效複方 0／已註銷 5） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Everolimus 抑制 mTORC1，進而壓抑 PI3K/AKT/mTOR 路徑驅動的細胞增殖。目前缺乏 DrugBank 的詳細作用機轉資料，以下推論依據為本次彙整的機轉假說。

去分化脂肪肉瘤 (dedifferentiated liposarcoma) 常見 CDK4/MDM2 擴增。研究者將 CDK4/6 抑制劑 ribociclib 與 everolimus 合併，期望同時阻斷細胞週期與生長訊號兩條平行路徑；臨床前模型顯示兩者有協同抑制腫瘤生長的作用。

需要注意：目前證據來自單臂 Phase 2 試驗，everolimus 是合併療法的一部分，無法單獨歸因其療效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 進行中（不再招募） | 48 | Ribociclib 合併 everolimus 用於晚期去分化脂肪肉瘤與平滑肌肉瘤，評估抗腫瘤活性 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 試驗報告 | Clin Cancer Res | Ribociclib 合併 everolimus 用於晚期去分化脂肪肉瘤與平滑肌肉瘤；兩藥在腫瘤模型中有協同抑制作用 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 肉瘤 PDOX 模型用於尋找 CDK 抑制劑 palbociclib 的有效組合療法 |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | 體外研究 | Oncogene | XPO1 抑制劑 KPT-330 破壞去分化脂肪肉瘤的核心轉錄調控迴路（未涉及 everolimus） |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 體外研究 | Anticancer Res | Eribulin 與不同機轉抗癌藥物合併的廣譜前臨床抗腫瘤活性（未涉及 everolimus） |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Everolimus 的不重複許可證共 **12 張**：有效單方 7 張、有效複方 0 張、已註銷 5 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署罕藥輸字第000020號 | 愛服妥錠 5 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2027/07/10 | 「結節性硬化症併有腎血管肌脂肪瘤之成年病患」且須符合以下條件：其腎血管肌脂肪瘤最長直徑需≧4cm，且曾有發生臨床上有意義之出血或確認病灶有血管瘤（aneurysm）直徑≧5mm者，… |
| 衛署罕藥輸字第000021號 | 愛服妥錠 2.5 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2027/07/10 | 「結節性硬化症併有腎血管肌脂肪瘤之成年病患」且須符合以下條件：其腎血管肌脂肪瘤最長直徑需≧4cm，且曾有發生臨床上有意義之出血或確認病灶有血管瘤（aneurysm）直徑≧5mm者，… |
| 衛署藥輸字第024770號 | 卓定康錠 0.25 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2028/01/24 | 腎臟及心臟移植 併用減量ciclosporin微乳製劑及類固醇，預防腎臟或心臟移植的成人病患之免疫器官排次作用。 肝臟移植 用於預防肝臟移植病患之器官排斥。Certican應於接受… |
| 衛署藥輸字第024772號 | 卓定康錠 0.5 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2028/01/24 | 腎臟及心臟移植 併用減量ciclosporin微乳製劑及類固醇，預防腎臟或心臟移植的成人病患之免疫器官排次作用。 肝臟移植 用於預防肝臟移植病患之器官排斥。Certican應於接受… |
| 衛署藥輸字第025165號 | 癌伏妥錠5毫克 | 錠劑 | 台灣諾華股份有限公司 | 2030/04/01 | AFINITOR® 合併exemestane 適用於治療荷爾蒙接受體陽性、HER2 受體陰性且之前使用過letrozole 或anastrozole 復發或惡化之停經後晚期乳癌患者… |
| 衛部藥製字第058400號 | "中化合成"依維莫司 B20 | 粉劑 | 中化合成生技股份有限公司山佳工廠 | 2029/09/25 | 器官移植抗排斥藥物、治療腎臟癌藥物。 |
| 衛部藥製字第061853號 | “中化合成”依維莫司 B02 | 粉劑 | 中化合成生技股份有限公司山佳工廠 | 2029/06/21 | 器官移植抗排斥藥物、治療腎臟癌藥物。 |

<details><summary><strong>已註銷</strong>（5 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第024771號</td><td>卓定康錠 0.75 毫克</td><td>EVEROLIMUS</td><td>2026/04/16</td></tr><tr><td>衛署藥輸字第024773號</td><td>卓定康可溶錠 0.25 毫克</td><td>EVEROLIMUS</td><td>2021/03/26</td></tr><tr><td>衛署藥輸字第024774號</td><td>卓定康可溶錠 0.1 毫克</td><td>EVEROLIMUS</td><td>2021/03/23</td></tr><tr><td>衛署藥輸字第024775號</td><td>卓定康錠 1.0 毫克</td><td>EVEROLIMUS</td><td>2021/03/26</td></tr><tr><td>衛署藥輸字第025166號</td><td>癌伏妥錠10毫克</td><td>EVEROLIMUS</td><td>2020/11/09</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（mTOR 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 血液學參數（CBC）、肝腎功能、血糖與血脂（依一般 mTOR 抑制劑監測原則） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本次彙整共記錄 383 筆交互作用。較重要的 Major 等級包括 amphotericin B、aprepitant、dexamethasone、clarithromycin；另有多種降血糖藥（如 metformin、acarbose、dapagliflozin、glimepiride 等）為 Moderate 等級。
- **需留意的疾病背景**：資料中顯示 everolimus 與下列情況有禁忌關聯紀錄（非仿單內容）：肝腎功能不全、血小板或嗜中性球減少、貧血、高血糖與糖尿病、高脂血症、間質性肺病、口腔炎、心包積液、充血性心衰竭等。使用前須對照原廠仿單確認。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有一項直接針對去分化脂肪肉瘤的 Phase 2 試驗（ribociclib 合併 everolimus）及其試驗報告，支持此方向；但 everolimus 僅為合併用藥，試驗為單臂設計且尚未完全結案，無法證明單藥療效。

**若要推進需要：**
- 取得 NCT03114527 的完整療效與安全性結果，並釐清 everolimus 的貢獻
- 補充詳細的作用機轉資料（MOA）
- 規劃合併療法的安全性監測（血液學、代謝、肺部毒性、口腔炎）
- 檢視與常用藥物（CYP3A4 抑制劑/誘導劑、降血糖藥）的交互作用管理

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表列入 lenvatinib 製劑「樂衛瑪膠囊」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

