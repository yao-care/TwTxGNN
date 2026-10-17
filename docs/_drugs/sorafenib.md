---
layout: default
title: Sorafenib
parent: 高證據等級 (L1-L2)
nav_order: 262
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-16
description: "Sorafenib：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L2）。原適應症：轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌 (HCC)"
monitor_inn: "sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
---

# Sorafenib
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

# Sorafenib：從晚期肝細胞癌 (HCC) 到脂肪肉瘤

## 一句話總結

Sorafenib 是一種多標靶激酶抑制劑，原本用於晚期肝細胞癌、晚期腎細胞癌與放射性碘治療無效的分化型甲狀腺癌。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **1 個臨床試驗**（軟組織肉瘤的 Phase 2 試驗，非脂肪肉瘤專屬）和 **8 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性或無法手術切除且不適合局部治療或局部治療失敗之晚期肝細胞癌 (HCC)；晚期腎細胞癌 (RCC)；放射性碘治療無效之局部晚期或轉移性進行性分化型甲狀腺癌 (DTC) |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2（僅 1 個已完成的 Phase 2 試驗，且為混合軟組織肉瘤族群） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 7 張（有效單方 7／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未收錄）。根據已知資訊，sorafenib 可抑制 RAF/MEK/ERK 訊號路徑，以及 VEGFR、PDGFR 等酪胺酸激酶，可能同時減少腫瘤血管新生與增殖訊號。

原適應症（肝癌、腎癌、甲狀腺癌）與脂肪肉瘤同屬實體腫瘤，其生長都依賴血管新生與激酶訊號。在軟組織肉瘤中，這些路徑被認為有治療意義。體外研究也顯示，sorafenib 能抑制去分化脂肪肉瘤細胞株的生長與 MAPK 訊號。

不過，現有人體證據來自混合型軟組織肉瘤，並非脂肪肉瘤專屬，因此機轉上合理，但臨床療效仍待驗證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | 完成 | 51 | Sorafenib 用於晚期軟組織肉瘤，族群涵蓋脂肪肉瘤，但非脂肪肉瘤專屬 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 試驗 | Cancer | SWOG 主導的 S0505 試驗，評估 sorafenib 用於晚期軟組織肉瘤 |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase I/II 試驗 | Ann Surg Oncol | 術前適形放療併用 sorafenib 用於局部晚期肢體軟組織肉瘤 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 軟組織肉瘤依組織型態選擇治療；trabectedin 對脂肪肉瘤有活性 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | 軟組織肉瘤的藥物治療日益依組織亞型決定 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 肉瘤 PDOX 模型用於找出併用療法（以 palbociclib 為主） |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | 體外研究 | Mol Cancer Ther | Sorafenib 抑制惡性周邊神經鞘瘤及去分化脂肪肉瘤細胞株的生長與 MAPK 訊號 |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | 動物研究 | Am J Pathol | 去分化脂肪肉瘤異種移植模型；顯示 PTEN 下調與對 PI3K 路徑抑制的反應 |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | 病例系列 | Anti-cancer Drugs | Trabectedin 用於滑膜肉瘤肺轉移病人（與 sorafenib 無直接關聯） |

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
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；知識圖譜提示的相關疾病風險包含血小板減少、嗜中性白血球減少、貧血、高血壓、肝衰竭，建議留意血液學參數、血壓與肝功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜提示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物-疾病關聯，非仿單內容）：高血壓、肝衰竭、血小板減少、嗜中性白血球減少、顆粒球缺乏症、凝血疾病、急性冠心症、冠狀動脈疾病、心肌梗塞、心肌缺血、貧血、血紅素病變、低磷血症、胰臟炎、焦慮症、神經症、輕鬱症。
- **藥物交互作用**：資料庫共記載 509 項交互作用。
  - 重大等級：Dolasetron。
  - 中度等級：Famotidine、Loperamide、Dexamethasone、Bisacodyl、Clarithromycin、Levofloxacin、Palonosetron、Naltrexone 等。
  - 輕微等級：Dapagliflozin、Metronidazole、Naloxegol。

主要警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Sorafenib 在台灣已有多張許可證，安全性特性已有臨床使用經驗，機轉上（RAF、VEGFR、PDGFR 抑制）對軟組織肉瘤有合理性。
- 但支持證據僅有 1 個混合軟組織肉瘤的 Phase 2 試驗，缺乏脂肪肉瘤專屬的臨床證據，因此只適合在嚴格設計下作為研究問題推進。

**若要推進需要：**
- 取得 NCT00217620 與 S0505 試驗中脂肪肉瘤亞組的療效數據（反應率、無惡化存活期）。
- 設計以脂肪肉瘤（特別是去分化亞型）為對象的前瞻性試驗，並設明確的停藥與安全監測準則。
- 取得完整的作用機轉資料與原廠仿單的警語、禁忌症，補足安全性資訊。
- 建立血壓、肝功能與血液學參數的監測計畫，並審查併用藥物（如 dolasetron）的交互作用。
- 若有興趣追蹤，其他預測適應症中，乳癌（多個 Phase 1/2 併用試驗）也值得另行評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

