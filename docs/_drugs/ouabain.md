---
layout: default
title: Ouabain
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
monitor_inn: "Ouabain"
predicted_indications: ["Prinzmetal angina", "hemoglobinopathy", "myocardial infarction", "thrombotic disease", "hyperthyroidism", "homozygous familial hypercholesterolemia", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
last_modified_at: 2026-10-16
description: "Ouabain：預測新適應症為Prinzmetal 心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：心臟衰竭、心房撲動、心房纖維顫動、陣發性上室性心博過速"
---

# Ouabain
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

## Ouabain：從心臟衰竭與心律不整到 Prinzmetal 心絞痛
{: .text-alpha }

## 一句話總結

Ouabain（哇巴因，台灣商品名「安保心注射液」）是一種強心配醣體（cardiotonic steroid），原本用於心臟衰竭、心房撲動、心房纖維顫動及陣發性上室性心搏過速。
TxGNN 模型預測它可能對 **Prinzmetal 心絞痛 (Prinzmetal angina)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心臟衰竭、心房撲動、心房纖維顫動、陣發性上室性心博過速 |
| 預測新適應症 | Prinzmetal 心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 1／有效複方 0／已註銷 3） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ouabain 為強心配醣體，一般認為其作用在於抑制 Na⁺/K⁺-ATPase，使細胞內鈉離子上升，進而提高細胞內鈣離子濃度與心肌收縮力。

然而，就 Prinzmetal 心絞痛（冠狀動脈血管痙攣所致）而言，這個機轉反而**不支持**預測的合理性。抑制 Na⁺/K⁺-ATPase 會使細胞內鈣離子上升、血管平滑肌張力增加，理論上可能加重而非緩解冠狀動脈痙攣。因此這個預測目前沒有機轉或臨床證據的支持，應視為模型輸出的假說，而非有依據的再利用方向。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（備註：在模型預測的其他候選適應症中，心肌梗塞、血栓性疾病、血紅素病變等有部分文獻，多為動物或體外研究，或僅把 Ouabain 當作 Na⁺/K⁺-ATPase 的研究探針，與 Prinzmetal 心絞痛無直接關聯，故不列入本節。）

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Ouabain 的不重複許可證共 **4 張**：有效單方 1 張、有效複方 0 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第001934號 | 安保心注射液 | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 心臟衰竭、心房撲動、心房纖維顫動、陣發性上室性心博過速 |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第007192號</td><td>哇巴因注射液</td><td>OUABAIN</td><td>1997/12/22</td></tr><tr><td>衛署藥製字第000399號</td><td>吾安保因注射液</td><td>OUABAIN</td><td>1991/05/06</td></tr><tr><td>衛署藥製字第033771號</td><td>吾安保因注射液０．０７５公絲/公撮（歐巴因）</td><td>OUABAIN</td><td>2017/02/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

另外，資料中也提到強心配醣體在缺血心肌中可能增加觸發性心律不整的風險（例如缺血性浦金氏纖維的相關研究），若考慮用於缺血性心臟疾病，須特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有臨床試驗、文獻，且 Ouabain 的藥理機轉（提高細胞內鈣、增加血管張力）反而可能使冠狀動脈痙攣惡化。
- 缺乏機轉資料與安全性資料，現階段不建議推進。

**若要推進需要：**
- 補充完整的作用機轉（MOA）資料，並釐清其對冠狀動脈血管平滑肌的實際作用
- 前臨床研究（如血管痙攣動物模型）評估是否有益或有害
- 補齊仿單中的警語、禁忌症與藥物交互作用資料
- 若要尋找較有潛力的方向，可優先檢視心肌梗塞等有前臨床機轉文獻的候選適應症，但這些目前也僅屬於研究問題（L4），尚無臨床證據。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄；頁首證據等級依本頁「快速總覽」的證據等級列重算，模型預測、總覽表與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L5，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L4）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

