---
layout: default
title: Vigabatrin
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 0
---

# Vigabatrin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Vigabatrin：抗癲癇輔助療法

## 一句話總結

Vigabatrin 是一種用於抗癲癇輔助療法的藥物。
TxGNN 模型**未預測**出任何新的適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗癲癇之輔助療法 |
| 預測新適應症 | 無 |
| TxGNN 預測分數 | N/A |
| 證據等級 | N/A |
| 台灣上市 | 已上市 |
| 許可證數 | 4 張（有效單方 2／有效複方 0／已註銷 2） |
| 建議決策 | 無老藥新用候選 |

## 為什麼沒有預測新適應症？

Vigabatrin 是一種選擇性 GABA 轉胺酶（GABA-T）不可逆抑制劑，透過抑制 4-aminobutyrate aminotransferase 增加腦內 GABA 濃度。其作用機轉高度專一，主要針對癲癇相關的神經傳導異常，因此在 TxGNN 知識圖譜分析中未發現與其他疾病的顯著關聯。

## 臨床試驗證據

無相關新適應症的臨床試驗。

## 文獻證據

無相關新適應症的文獻證據。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Vigabatrin 的不重複許可證共 **4 張**：有效單方 2 張、有效複方 0 張、已註銷 2 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第021847號 | 赦癲易膜衣錠５００公絲 | 膜衣錠 | 賽諾菲股份有限公司 | 2029/05/31 | 抗癲癇之輔助療法。 |
| 衛部藥輸字第028723號 | 必抗癲口服溶液用粉劑500毫克 | 口服溶液用粉劑 | 凱沛爾藥品有限公司 | 2029/06/24 | 抗癲癇之輔助療法 |

<details><summary><strong>已註銷</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第020477號</td><td>赦癲易錠５００公絲</td><td>CELLULOSE MICROCRYSTALLINE (MICROCRYSTALLINE CELLULOSE)、VIGA…</td><td>1997/07/02</td></tr><tr><td>衛署藥輸字第021691號</td><td>膜衣錠５００公絲</td><td>VIGABATRIN</td><td>1997/11/17</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

### 重大藥物交互作用（Major）

| 交互作用藥物 | 嚴重度 |
|-------------|--------|
| Hydrocortisone | Major |
| Triamcinolone | Major |
| Dexamethasone | Major |
| Betamethasone | Major |
| Budesonide | Major |
| Prednisone | Major |
| Prednisolone | Major |
| Methylprednisolone | Major |
| Deflazacort | Major |
| Deferoxamine | Major |
| Chloroquine | Major |
| Hydroxychloroquine | Major |
| Quinine | Major |
| Tamoxifen | Major |

### 中度藥物交互作用（Moderate）

與多種鎮靜劑、抗組織胺藥物及類鴉片藥物有中度交互作用，可能增加中樞神經抑制作用。常見包括：Morphine、Codeine、Cetirizine、Diphenhydramine、Ethanol 等。

### 作用標靶

- Vesicular inhibitory amino acid transporter (SLC32A1)
- 4-aminobutyrate aminotransferase (ABAT)

## 結論與下一步

**決策：無老藥新用候選**

**理由：**
Vigabatrin 的作用機轉高度專一於 GABA 能神經傳導，TxGNN 模型未發現具有足夠證據支持的新適應症候選。

**注意事項：**
- Vigabatrin 可能導致不可逆的視野缺損，需定期監測視力
- 與皮質類固醇併用需特別注意交互作用

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「許可證數：6 張（2 張有效）」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

