---
layout: default
title: Verteporfin
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 1
monitor_inn: "Verteporfin"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies"]
last_modified_at: 2026-10-16
description: "Verteporfin：預測新適應症為核 DNA 異常所致的粒線體氧化磷酸化疾病 (mitochondrial oxidative phosphorylation disord…（證據等級 L5）。原適應症：因年齡相關性黃斑部退化病變引起之主要典型或潛隱性視網膜下中央凹脈絡膜血管新生…"
---

# Verteporfin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Verteporfin：從年齡相關性黃斑部退化病變之脈絡膜血管新生到粒線體氧化磷酸化疾病

## 一句話總結

Verteporfin（維視達）是一種光敏劑，原本用於治療年齡相關性黃斑部退化病變、病理性近視或疑似眼組織漿菌症所引起的視網膜下中央凹脈絡膜血管新生。
TxGNN 模型預測它可能對**核 DNA 異常所致的粒線體氧化磷酸化疾病 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 因年齡相關性黃斑部退化病變引起之主要典型或潛隱性視網膜下中央凹脈絡膜血管新生，病理性近視(PM)或疑似眼組織漿菌症引起之視網膜下中央凹脈絡膜血管新生 |
| 預測新適應症 | 核 DNA 異常所致的粒線體氧化磷酸化疾病 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| TxGNN 預測分數 | 99.49% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Verteporfin 是一種光敏劑，經特定波長光線照射活化後會產生活性氧（ROS），選擇性破壞異常的脈絡膜新生血管。此外，已有報告指出它可能不依賴光照而抑制 YAP-TEAD 訊號傳遞。

然而，就本次整理的資料來看，看不出 Verteporfin 與核 DNA 編碼的氧化磷酸化缺陷之間有直接關聯。光動力作用所產生的 ROS 反而可能加重粒線體功能障礙。因此，0.995 的預測分數目前只能視為計算模型的輸出，機轉上的合理性尚未建立，需要額外的機轉研究才能判斷。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Verteporfin 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第023479號 | 維視達凍晶注射劑１５毫克 | 凍晶注射劑 | 裕利股份有限公司 | 2027/07/01 | 因年齡相關性黃斑部退化病變引起之主要典型或潛隱性視網膜下中央凹脈絡膜血管新生，病理性近視(PM)或疑似眼組織漿菌症引起之視網膜下中央凹脈絡膜血管新生。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單內容）：遺傳性紫質症、紫質代謝疾病、紫質症、肝臟疾病、膽囊疾病。
- **藥物交互作用**：資料庫共查得 117 筆交互作用，以下為部分中度交互作用的藥物：
  - 四環素類抗生素：Doxycycline、Tetracycline、Minocycline（含外用劑型）
  - 磺醯尿素類降血糖藥：Chlorpropamide、Glimepiride、Glipizide、Glyburide、Tolbutamide、Tolazamide、Acetohexamide
  - 其他：Acetylsalicylic acid（阿斯匹靈）、Levofloxacin、Mannitol、Sulfasalazine、Beta carotene、Papaverine
  - 輕度交互作用：Polymyxin B
- 光敏劑類藥物一般需注意光敏感反應，詳細警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型計算，沒有臨床試驗或文獻佐證（證據等級 L5），且機轉上找不到合理連結。
- 光動力 ROS 產生還可能加重粒線體功能障礙，存在潛在的安全疑慮。

**若要推進需要：**
- 補齊 Verteporfin 的作用機轉資料（MOA）。
- 進行文獻回顧與前臨床研究，驗證 Verteporfin 對粒線體氧化磷酸化缺陷的影響，特別是 ROS 產生與 YAP-TEAD 抑制是否有益或有害。
- 釐清給藥途徑與光照需求是否適用於全身性的粒線體疾病（目前途徑相容性尚未評估）。
- 在確認機轉安全且有前臨床證據前，不建議進入臨床開發。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

