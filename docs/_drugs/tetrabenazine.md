---
layout: default
title: Tetrabenazine
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
monitor_inn: "Tetrabenazine"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "thoracic malformation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "acute intermittent porphyria", "adult familial nephronophthisis-spastic quadriparesia syndrome", "atypical glycine encephalopathy", "congenital disorder of glycosylation with defective fucosylation"]
last_modified_at: 2026-10-16
description: "Tetrabenazine：預測新適應症為多囊腎疾病 3 型，可合併多囊肝（證據等級 L5）。原適應症：治療亨汀頓舞蹈症之舞蹈症狀"
---

# Tetrabenazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Tetrabenazine：從亨汀頓舞蹈症到多囊腎疾病 3 型，可合併多囊肝
{: .text-alpha }

## 一句話總結

Tetrabenazine 是一種 VMAT2 抑制劑，原本用於治療亨汀頓舞蹈症之舞蹈症狀。
TxGNN 模型預測它可能對**多囊腎疾病 3 型（可合併多囊肝，polycystic kidney disease 3 with or without polycystic liver disease）**有效，
但目前**沒有任何臨床試驗與文獻**支持此預測，僅有模型運算結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療亨汀頓舞蹈症之舞蹈症狀 |
| 預測新適應症 | 多囊腎疾病 3 型，可合併多囊肝 (polycystic kidney disease 3 with or without polycystic liver disease) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tetrabenazine 是可逆性 VMAT2 抑制劑，會耗竭突觸前的單胺類神經傳遞物質，這也是它用於控制亨汀頓舞蹈症之舞蹈症狀的基礎。

然而，多囊腎疾病屬於與纖毛及腎臟病理相關的遺傳性疾病，單胺耗竭與囊腫形成之間，目前看不出合理的機轉關聯。這個預測完全來自 TxGNN 的模型分數，並無機轉、臨床或文獻上的佐證。

需要說明的是，TxGNN 排名較前的其他預測（例如腎肝胰發育不良、伴腎臟缺陷的 Joubert 症候群、核巨大型間質性腎炎等）同樣缺乏機轉依據，顯示這批預測整體可信度有限，應視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（註：排名第 5 的預測「胸腔畸形」僅檢索到一篇痙攣性斜頸合併椎體血管瘤的病例系列，屬於動作障礙情境，並非該適應症的證據，故不納入。）

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tetrabenazine 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署罕藥輸字第000026號 | 止蹈錠25毫克 | 錠劑 | 吉泰藥品股份有限公司 | 2028/02/05 | 治療亨汀頓舞蹈症之舞蹈症狀。 |
| 衛署罕藥輸字第000027號 | 止蹈錠12.5毫克 | 錠劑 | 吉泰藥品股份有限公司 | 2028/02/04 | 治療亨汀頓舞蹈症之舞蹈症狀。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，非仿單原文）：
  - 心血管與血壓相關：長 QT 症候群（含家族性）、尖端扭轉型心室頻脈、姿勢性直立心搏過速症候群、姿勢性低血壓、低血壓性疾患、多系統萎縮
  - 精神相關：焦慮症、神經症、輕鬱症
  - 動作障礙相關：遲發性運動不全、口顎顏面運動不全、帕金森氏症及類帕金森症、藥物引起的靜坐不能
  - 內分泌相關：高泌乳素血症（含家族性、後天性及泌乳素分泌型腦下垂體腫瘤）
  - 肝膽相關：肝臟疾病、膽囊疾病
- **藥物交互作用**：資料庫共收錄 168 筆，以下為較重要者：
  - 嚴重（Major）：Bupropion、Dolasetron、Metoclopramide
  - 中度（Moderate）：Clarithromycin、Levofloxacin、Morphine、Famotidine、Loperamide、Palonosetron 等
  - 輕微（Minor）：Metronidazole

其餘警語與仿單禁忌資訊請參考原廠仿單。此外，對於預測的新適應症（尤其是急性間歇性紫質症），藥物在該族群的安全性尚未評估。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（0.9990），但沒有任何臨床試驗或文獻佐證，證據等級僅為 L5。
- 作用機轉（VMAT2 抑制）與多囊腎疾病的病理（纖毛／囊腫形成）缺乏合理連結，且藥物本身有 QT 延長、憂鬱與帕金森症狀等安全性顧慮。

**若要推進需要：**
- 補齊 Tetrabenazine 的作用機轉資料，並探討任何可能與腎臟囊腫形成相關的路徑。
- 進行前臨床研究（如多囊腎疾病的細胞或動物模型）以驗證是否有生物學訊號。
- 系統性檢索文獻與試驗登錄，確認是否存在未被收錄的相關研究。
- 若有初步訊號，再評估腎／肝功能受損族群的安全性與劑量。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 止蹈錠 12.5 毫克許可證字號 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 止蹈錠 25 毫克許可證字號 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

