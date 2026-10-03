---
layout: default
title: Choline Salicylate
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Choline Salicylate
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

# Choline Salicylate：從解熱鎮痛到 Prinzmetal 心絞痛

## 一句話總結

Choline salicylate（水楊酸膽素）是非乙醯化水楊酸鹽類藥物，原本核准用於解熱、鎮痛及口腔局部抗炎治療。
TxGNN 模型預測它可能對 **Prinzmetal 心絞痛（Prinzmetal Angina）** 有效，
但目前**無任何臨床試驗或文獻**支持這個方向，屬純模型預測結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 解熱鎮痛劑 |
| 預測新適應症 | Prinzmetal 心絞痛 (Prinzmetal Angina) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張（有效單方 1／有效複方 2／已註銷 3） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Choline salicylate 是非乙醯化水楊酸鹽（non-acetylated salicylate）的一員，在解熱、鎮痛及口腔黏膜抗炎方面已有臨床核准應用，其成分在減少前列腺素合成、緩解發炎反應的療效已被證實。

從機轉角度推論，水楊酸鹽透過抑制環氧化酶（COX）減少前列腺素介導的血管收縮，理論上可能輕度緩解冠狀動脈痙攣；Prinzmetal 心絞痛的核心病生理機轉正是冠狀動脈痙攣，此連結提供初步的機轉合理性。此外，水楊酸鹽具有輕度抗血小板效果，或可減少痙攣發作時的血小板活化。

然而，這些機轉連結屬高度推論性質。相較於阿斯匹林，非乙醯化水楊酸鹽的 COX 抑制及抗血小板效果均較弱，且目前完全缺乏針對 Prinzmetal 心絞痛的臨床試驗或文獻佐證，整體機轉支持薄弱。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Choline Salicylate 的不重複許可證共 **6 張**：有效單方 1 張、有效複方 2 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第021417號 | 蒙得莎凝膠 | 外用凝膠劑 | 嘉德藥品企業股份有限公司 | 2026/11/06 | 發炎、疼痛、單純疱瘡 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第039009號 | 治膜炎凝膠 | CHOLINE SALICYLATE、CETALKONIUM CHLORIDE | 外用凝膠劑 | 發炎、疼痛、單純庖瘡 |
| 衛署藥製字第047620號 | 允消炎凝膠 | CHOLINE SALICYLATE、CETALKONIUM CHLORIDE | 外用凝膠劑 | 發炎、疼痛、單純&#30129;瘡。 |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第008406號</td><td>炎可愈凝膠</td><td>CETALKONIUM CHLORIDE、CHOLINE SALICYLATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第009882號</td><td>水楊酸膽素８０％</td><td>CHOLINE SALICYLATE</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第011187號</td><td>柳酸膽/</td><td>CHOLINE SALICYLATE</td><td>1999/09/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

**藥物交互作用**：共有 107 筆 DDI 紀錄，以下列出主要交互作用：

| 交互藥物 | 嚴重程度 | 說明 |
|---------|---------|------|
| Hydrocortisone | Moderate | 皮質類固醇類 |
| Triamcinolone | Moderate | 皮質類固醇類 |
| Dexamethasone | Moderate | 皮質類固醇類 |
| Betamethasone | Moderate | 皮質類固醇類 |
| Budesonide | Moderate | 皮質類固醇類 |
| Glimepiride | Moderate | 磺醯脲類降血糖藥 |
| Glipizide | Moderate | 磺醯脲類降血糖藥 |
| Glyburide | Moderate | 磺醯脲類降血糖藥 |
| Insulin human | Moderate | 胰島素類 |
| Aluminum hydroxide | Moderate | 制酸劑（可能降低吸收） |
| Calcium carbonate | Moderate | 制酸劑（可能降低吸收） |
| Activated charcoal | Moderate | 吸附劑（可能降低吸收） |
| Rabeprazole | Minor | 質子幫浦抑制劑 |
| Dexlansoprazole | Minor | 質子幫浦抑制劑 |

> 與**皮質類固醇**合用時需監測水楊酸鹽血中濃度；與**降血糖藥或胰島素**合用時需注意可能強化降血糖效果；與**制酸劑**同時服用可能降低吸收效率。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.84%），但目前 Prinzmetal 心絞痛方向完全缺乏臨床試驗與文獻支持（證據等級 L5），機轉連結屬純理論推論，且現有台灣核准劑型（外用凝膠、原料藥溶液）與心血管適應症所需的給藥途徑不相符，不建議在無更多證據前推進。

**若要推進需要：**
- 確認 Choline salicylate 的詳細作用機轉（MOA）資料（建議查詢 DrugBank API）
- 蒐集水楊酸鹽類藥物用於冠狀動脈痙攣的基礎研究或動物實驗數據
- 評估全身性給藥劑型的可行性（現有核准劑型為局部/外用）
- 建立心血管疾病族群的安全性監測計畫，特別關注合併使用皮質類固醇或降血糖藥的患者

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表中原料藥已註銷、兩張凝膠為複方 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

