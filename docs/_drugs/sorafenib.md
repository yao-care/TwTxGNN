---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 6
monitor_inn: "sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-10-27
description: "Sorafenib：預測新適應症為脂肪肉瘤 (liposarcoma)（證據等級 L5）."
---

# Sorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Sorafenib：多標靶激酶抑制劑 → 脂肪肉瘤 (liposarcoma)
{: .text-alpha }

## 一句話總結

Sorafenib 是一種多標靶激酶抑制劑，抑制 RAF/MEK/ERK 訊號路徑以及 VEGFR、PDGFR 等酪胺酸激酶。
TxGNN 模型預測它可能對**脂肪肉瘤 (liposarcoma)** 有效。
目前有 **1 個相關臨床試驗**（軟組織肉瘤混合族群，非脂肪肉瘤專屬）和 **8 篇文獻**，但沒有直接以脂肪肉瘤為對象的臨床研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌(HCC)。
 晚期腎細胞癌(RCC)且已接受interferon-alpha或interleukin-2治療失敗，或不適合以上兩種藥物治療之病患。
 放射性碘治療無效之局部晚期或轉移性的進行性(progressive)分化型甲狀腺癌(DTC)。; 轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌(HCC)。晚期腎細胞癌(RCC)且已接受interferon-alpha或interleukin-2治療失敗，或不適合以上兩種藥物治療之病患。放射性碘治療無效之局部晚期或轉移性的進行性(progressive)分化型甲狀 |

| 預測新適應症 | 脂肪肉瘤 (liposarcoma) |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效單方 7／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已整理的資料，sorafenib 可抑制 RAF/MEK/ERK 訊號，並抑制 VEGFR、PDGFR 等酪胺酸激酶，可能減少腫瘤血管新生與增殖訊號。

軟組織肉瘤（含脂肪肉瘤）常依賴這些訊號路徑，因此機轉上有合理性。體外研究也顯示，sorafenib 可抑制去分化脂肪肉瘤細胞株的生長與 MAPK 訊號。

不過，現有人體證據來自混合型軟組織肉瘤的研究，並非脂肪肉瘤專屬，因此對脂肪肉瘤的實際療效仍不確定。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | 完成 | 51 | 評估 sorafenib 用於晚期軟組織肉瘤；族群包含脂肪肉瘤，但並非脂肪肉瘤專屬 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | 第二期試驗（Cohort） | Cancer | SWOG S0505 研究，評估 sorafenib 用於晚期軟組織肉瘤 |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | 第一期試驗（Cohort） | Ann Surg Oncol | 術前放療合併 sorafenib 用於肢體局部晚期軟組織肉瘤 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | 軟組織肉瘤依組織型態選擇藥物治療 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 軟組織肉瘤的組織型態導向與非導向療法 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 肉瘤 PDOX 小鼠模型用於尋找 palbociclib 組合療法 |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | 體外研究 | Mol Cancer Ther | Sorafenib 抑制惡性周邊神經鞘瘤與去分化脂肪肉瘤細胞株的生長及 MAPK 訊號 |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | 動物研究 | Am J Pathol | 去分化脂肪肉瘤異種移植模型，顯示 PTEN 下調及對 PI3K 抑制的反應 |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | 病例系列 | Anti-Cancer Drugs | Trabectedin 用於滑膜肉瘤肺轉移（與 sorafenib 無直接關聯） |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sorafenib 的不重複許可證共 **7 張**：有效單方 7 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第024727號 | 蕾莎瓦膜衣錠 200 毫克 | 膜衣錠 | 台灣拜耳股份有限公司 | 2027/10/23 | 轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌(HCC)。 晚期腎細胞癌(RCC)且已接受interferon-alpha或interleukin-2治療失敗，或… |
| 衛部藥製字第061955號 | 鎖癌飛膜衣錠200毫克 | 膜衣錠 | 中國化學製藥股份有限公司新豐工廠 | 2030/03/28 | 轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌(HCC)。晚期腎細胞癌(RCC)且已接受interferon-alpha或interleukin-2治療失敗，或不… |
| 衛部藥輸字第028192號 | 索福耐膜衣錠200毫克 | 膜衣錠 | 健喬信元醫藥生技股份有限公司 | 2031/10/27 | 轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌(HCC)。晚期腎細胞癌(RCC)且已接受interferon-alpha或interleukin-2治療失敗，或不… |
| 衛部藥輸字第028536號 | 易芬妮膜衣錠200毫克 | 膜衣錠 | 美時化學製藥股份有限公司 | 2028/08/09 | 1.轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌(HCC)。 2.晚期腎細胞癌(RCC)且已接受interferon-alpha或interleukin-2治療… |
| 衛部藥輸字第028614號 | 索拿癌膜衣錠200毫克 | 膜衣錠 | 台灣山德士藥業股份有限公司 | 2028/11/16 | 轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌(HCC)。 晚期腎細胞癌(RCC)且已接受interferon-alpha或interleukin-2治療失敗，或… |
| 衛部藥輸字第028680號 | 煞拉速肌瘤靶泊甲苯磺酸鹽 | （粉） | 川聖貿易股份有限公司 | 2029/03/26 | 抗腫瘤藥 |
| 衛部藥陸輸字第001104號 | 煞拉速肌瘤靶泊甲苯磺酸鹽 | 原料藥粉劑 | 西海生技股份有限公司 | 2028/05/23 | 抗腫瘤藥 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 建議監測血液學參數（CBC）、肝腎功能、血壓 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：共查得 509 筆交互作用紀錄。其中較需注意的包括：
  - 重大 (Major)：Dolasetron
  - 中度 (Moderate)：Clarithromycin、Dexamethasone、Levofloxacin、Palonosetron、Famotidine、Loperamide 等
- **需留意的相關疾病（資料庫標示）**：高血壓、肝衰竭、血小板低下、嗜中性白血球低下、凝血疾病、急性冠心症／心肌梗塞、貧血、低磷血症、胰臟炎等。這些為模型資料庫的禁忌關聯，並非仿單文字，使用前仍須對照原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何研究直接以脂肪肉瘤為對象，現有試驗皆為混合型軟組織肉瘤，因此證據等級僅能判定為 L5。
- 機轉上合理，且體外與動物資料有些支持，但尚不足以支持臨床推進。

**若要推進需要：**
- 從 NCT00217620 與 S0505 試驗中取出脂肪肉瘤亞群的療效數據進行分析
- 針對脂肪肉瘤（特別是去分化型）設計專屬的前瞻性試驗或擴展世代研究
- 補充 DrugBank 的作用機轉資料
- 針對心血管、血壓與出血風險擬定監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

