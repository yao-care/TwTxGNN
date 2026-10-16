---
layout: default
title: Balsalazide
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-16
description: "Balsalazide：預測新適應症為痛風 (Gout)（證據等級 L5）。原適應症：輕度至中度的急性潰瘍性結腸炎"
---

# Balsalazide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Balsalazide：從潰瘍性結腸炎到痛風

## 一句話總結

Balsalazide 是一種會在結腸釋放 5-ASA（5-氨基水楊酸）的前驅藥，原本用於輕度至中度的急性潰瘍性結腸炎。
TxGNN 模型預測它可能對**痛風 (Gout)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 輕度至中度的急性潰瘍性結腸炎 |
| 預測新適應症 | 痛風 (Gout) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 3 張（有效單方 1／有效複方 0／已註銷 2） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Balsalazide 是一種前驅藥，會將 5-ASA 送到結腸，具有抗發炎活性，在潰瘍性結腸炎中的療效已被證實。

不過，目前沒有證據顯示它與尿酸代謝或痛風性發炎有直接關聯。這個預測目前只有 TxGNN 分數支持，機轉上是否適用於痛風仍屬未驗證的推測。

值得一提的是，TxGNN 前幾名的其他預測（如僵直性脊椎炎、類風濕性關節炎）與 5-ASA 的抗發炎作用及腸道與關節發炎的關聯性較為接近，但同樣缺乏臨床試驗與文獻佐證。另外有些預測（如先天性少毛症合併青少年黃斑部失養症、尾骨過度活動）在機轉上看不出合理的關聯，可能是圖譜運算的假象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Balsalazide 的不重複許可證共 **3 張**：有效單方 1 張、有效複方 0 張、已註銷 2 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第046643號 | "美時" 巴塞治膠囊750毫克 | 膠囊劑 | 美時化學製藥股份有限公司 | 2029/11/18 | 輕度至中度的急性潰瘍性結腸炎。 |

<details><summary><strong>已註銷</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第045854號</td><td>"台耀" 巴塞納晒鈉鹽</td><td>Balsalazide Disodium Dihydrate</td><td>2025/08/29</td></tr><tr><td>衛署藥陸輸字第000523號</td><td>巴塞納晒鈉鹽</td><td>Balsalazide Disodium Dihydrate (Balsalazide Disodium)</td><td>2019/03/20</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病關聯，非仿單內容）：腎臟病、輸尿管積膿、幽門狹窄。
- **藥物交互作用**：共查得 196 筆，以下為部分範例：
  - **重度**：人類免疫球蛋白 G（靜脈注射）
  - **中度**：Doxycycline、Ketorolac、Ibuprofen、Celecoxib、Acyclovir、Azathioprine、Amphotericin B、Amikacin、Amoxicillin、Azithromycin 等。其中多數為腎毒性藥物或 NSAIDs，與知識圖譜中的腎臟病風險方向一致，併用時宜留意腎功能。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 痛風預測僅有模型分數支持，沒有臨床試驗、文獻，也缺乏作用機轉資料，證據等級為 L5。
- 5-ASA 的抗發炎作用與尿酸代謝、痛風性發炎之間沒有直接連結。

**若要推進需要：**
- 補齊 Balsalazide 的作用機轉資料（MOA）
- 系統性搜尋 5-ASA 或 Balsalazide 與痛風的前臨床或臨床研究
- 評估是否有更合理的候選適應症（如僵直性脊椎炎、類風濕性關節炎）並優先驗證
- 若未來考慮推進，需評估腎功能風險與常見併用藥（如 NSAIDs）的交互作用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

