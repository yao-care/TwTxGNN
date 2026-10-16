---
layout: default
title: Everolimus
parent: 高證據等級 (L1-L2)
nav_order: 104
evidence_level: L2
indication_count: 10
monitor_inn: "Everolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma", "renal cell carcinoma associated with neuroblastoma", "unclassified renal cell carcinoma"]
last_modified_at: 2026-10-16
description: "Everolimus：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L2）。原適應症：器官移植抗排斥藥物、治療腎臟癌藥物"
---

# Everolimus
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

# Everolimus：從器官移植抗排斥與腎臟癌到脂肪肉瘤

## 一句話總結

Everolimus（依維莫司）是 mTOR 抑制劑，原本用於預防器官移植排斥，以及治療腎細胞癌、乳癌、神經內分泌腫瘤等。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **1 個臨床試驗**和 **4 篇文獻**與此方向相關，但其中只有 1 個 Phase 2 試驗直接針對去分化脂肪肉瘤，且 everolimus 是與 ribociclib 併用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 器官移植抗排斥藥物、治療腎臟癌藥物 |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 12 張（有效單方 7／有效複方 0／已註銷 5） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，everolimus 是 mTORC1 抑制劑，可抑制 PI3K/AKT/mTOR 路徑所驅動的細胞增殖，這也是它在腎細胞癌、乳癌等腫瘤中發揮作用的基礎。

去分化脂肪肉瘤 (DDLPS) 常見 CDK4/MDM2 擴增。研究者的設想是同時阻斷細胞週期（CDK4/6，ribociclib）與細胞生長（mTOR，everolimus）兩條平行路徑，在多種腫瘤模型中已觀察到協同抑制生長的效果。

需要注意：目前證據中，everolimus 只是組合療法的一員，尚無單藥用於脂肪肉瘤的資料。另外，在其他預測疾病中，以非透明細胞型腎細胞癌（unclassified RCC）的證據最完整，包含 2 個隨機 Phase 2 試驗（ASPEN、ESPN），但該排序第 1 名的預測仍是脂肪肉瘤，故本報告以脂肪肉瘤為主軸。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 進行中（不再招募） | 48 | Ribociclib 併用 everolimus 用於曾接受過至少一線全身治療的晚期去分化脂肪肉瘤 (DDL) 與平滑肌肉瘤 (LMS)，評估抗腫瘤活性；預計 2026 年 12 月完成 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 試驗報告 | Clin Cancer Res | Ribociclib 加 everolimus 用於晚期 DDL 與 LMS；兩藥分別靶向 CDK4/6 與 mTOR，在腫瘤模型中有協同作用 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 以 PDOX 小鼠模型尋找肉瘤的 CDK 抑制劑（palbociclib）組合療法，屬間接佐證 |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 體外研究 | Anticancer Res | Eribulin 與不同機轉抗癌藥物併用的前臨床活性，與 everolimus 的關聯有限 |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | 體外研究 | Oncogene | XPO1 抑制劑 KPT-330 干擾 DDLPS 核心轉錄調控，並未直接測試 everolimus |

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
| 骨髓抑制風險 | 中度；知識圖譜資料列出血小板減少、嗜中性白血球減少、白血球減少、貧血等相關風險 |
| 監測項目 | CBC（含分類）、肝腎功能、血糖、血脂 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜標示的相關風險（非仿單文字）**：肝功能衰竭/肝病、腎病、血小板減少、嗜中性白血球減少、白血球減少、貧血、高血糖/糖尿病、高三酸甘油脂血症/高脂血症、間質性肺病、口腔炎、充血性心衰竭、心包積液等。這些為資料庫關聯，實際禁忌請以仿單為準。
- **藥物交互作用**：共 383 筆。主要（Major）包括 Amphotericin B、Aprepitant、Dexamethasone、Clarithromycin；中度（Moderate）包括多種降血糖藥（如 Metformin、Acarbose、Canagliflozin、Dapagliflozin、Empagliflozin、Glimepiride）及 Cimetidine 等。

警語與禁忌症的仿單資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 脂肪肉瘤僅有 1 個進行中的 Phase 2 組合療法試驗，尚無完整結果，且 everolimus 並非單獨作用，無法確認其貢獻。
- 該預測屬於研究假說階段，尚不足以支持臨床或適應症擴增決策。

**若要推進需要：**
- 等待 NCT03114527 的完整療效與安全性結果，並判斷 everolimus 的獨立貢獻。
- 補充 DrugBank 的作用機轉資料，並建立 mTOR 在 DDLPS 的生物標記佐證。
- 評估安全性（血液學毒性、代謝異常、間質性肺病）與 CYP3A4/P-gp 相關藥物交互作用的監測計畫。
- 若需優先推進，可另行評估非透明細胞型腎細胞癌，其 Phase 2 與隨機試驗證據較充分（該預測的建議為 Proceed with Guardrails）。

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

