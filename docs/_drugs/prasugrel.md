---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 9
monitor_inn: "Prasugrel"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
last_modified_at: 2026-10-16
description: "Prasugrel：預測新適應症為肺高壓 (Pulmonary Hypertension)（證據等級 L5）。原適應症：需要冠狀動脈介入性治療(PCI)的急性冠狀動脈症候群(ACS"
---

# Prasugrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Prasugrel：從急性冠狀動脈症候群到肺高壓
{: .text-alpha }

## 一句話總結

Prasugrel 是一種抗血小板藥物，原本用於需要冠狀動脈介入性治療（PCI）的急性冠狀動脈症候群（ACS）。
TxGNN 模型預測它可能對**肺高壓 (Pulmonary Hypertension)** 有效，但目前**沒有相關臨床試驗**，所收錄的 2 篇文獻也未直接探討 prasugrel 用於肺高壓，證據僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 需要冠狀動脈介入性治療(PCI)的急性冠狀動脈症候群(ACS；不穩定型心絞痛、非ST段上升之心肌梗塞或ST段上升之心肌梗塞) |
| 預測新適應症 | 肺高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效單方 5／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 prasugrel 是不可逆的 P2Y12 血小板受體拮抗劑，可抑制血小板活化與聚集，臨床上用於預防 ACS 患者接受 PCI 後的血栓事件。

肺高壓與 ACS 看似不同，但血小板活化被認為可能參與肺血管重塑與血栓形成，因此抑制 P2Y12 在機轉上有理論上的可能性。

然而，目前收錄的文獻並未研究 prasugrel 用於肺高壓：一篇是 clopidogrel 在 ACS/PCI 病人的使用與服藥遵從性世代研究，另一篇是 COVID-19 患者背景用藥與死亡風險的登錄研究。因此這個預測的支持完全來自 TxGNN 分數，屬於假說階段。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | 探討 ACS 患者接受 PCI 後 clopidogrel 的使用、服藥遵從性及相關因素；並非肺高壓研究 |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | 以 ACTIVE 登錄資料分析 COVID-19 感染前的背景用藥對嚴重度與死亡結局的影響；與肺高壓無直接關聯 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Prasugrel 的不重複許可證共 **5 張**：有效單方 5 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027361號 | 抑凝安® 膜衣錠3.75毫克 | 膜衣錠 | 台灣第一三共股份有限公司 | 2028/03/23 | Efient適用於需要冠狀動脈介入性治療(PCI)的急性冠狀動脈症候群(ACS；不穩定型心絞痛[UA]、非ST段上升之心肌梗塞[NSTEMI]或ST段上升之心肌梗塞[STEMI])… |
| 衛部藥輸字第027362號 | 抑凝安® 膜衣錠5毫克 | 膜衣錠 | 台灣第一三共股份有限公司 | 2028/03/23 | Efient適用於需要冠狀動脈介入性治療(PCI)的急性冠狀動脈症候群(ACS；不穩定型心絞痛[UA]、非ST段上升之心肌梗塞[NSTEMI]或ST段上升之心肌梗塞[STEMI])… |
| 衛部藥輸字第028397號 | 抑凝安口溶錠20毫克 | 口溶錠 | 台灣第一三共股份有限公司 | 2027/12/28 | 適用於需要冠狀動脈介入性治療(PCI)的急性冠狀動脈症候群(ACS；不穩定型心絞痛[UA]、非ST段上升之心肌梗塞[NSTEMI]或ST段上升之心肌梗塞[STEMI]。 |
| 衛部藥輸字第028782號 | 普拉格雷鹽酸鹽 | （粉） | 台灣荃新股份有限公司 | 2029/08/21 | 抗凝血劑 |
| 衛部藥輸字第028966號 | 普拉格雷鹽酸鹽 | （粉） | 龍大生技股份有限公司 | 2030/06/02 | 抗凝血劑。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **知識圖譜標示之潛在禁忌疾病**（來自 TxGNN 知識圖譜，非仿單內容）：肝衰竭、低血壓疾患、凝血疾病、中風、腦血管疾患、腦梗塞、顱內出血、短暫性腦缺血發作、血栓性血小板減少性紫斑症、椎基底動脈循環不全、外傷等。
- **藥物交互作用**：共查得 191 筆，其中列為重大（Major）者包括 Deferasirox、Ibritumomab tiuxetan；中度（Moderate）包括 Acetylsalicylic acid（阿斯匹靈）、Morphine、Opium、Fenfluramine、Dexfenfluramine、Sibutramine。其餘多為輕微（Minor），如多種氫離子幫浦抑制劑與 H2 受體拮抗劑。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 肺高壓這個預測目前僅有模型分數，沒有任何臨床試驗，所列文獻也未直接研究 prasugrel 用於肺高壓，證據等級為 L5。
- Prasugrel 具有出血風險，且知識圖譜顯示多項出血與腦血管相關的潛在禁忌，在缺乏療效證據下不宜推進。

**若要推進需要：**
- 補充作用機轉資料，並建立血小板 P2Y12 與肺血管重塑的機轉證據
- 前臨床研究（如肺高壓動物模型）驗證療效
- 針對肺高壓族群評估出血風險與效益
- 若前臨床結果正向，再設計小規模探索性臨床試驗

**補充說明：** 同一份資料中，**偏頭痛 (migraine disorder)**（TxGNN 分數 0.9988）的證據相對較多，包括 1 項招募中的 Phase 3 試驗（NCT07629635，為 PFO 導向治療）及 2 篇 thienopyridine/ticagrelor 於合併 PFO 偏頭痛的小型研究，證據等級 L3，建議列為後續研究問題，優先於肺高壓評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

