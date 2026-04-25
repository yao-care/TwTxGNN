---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

使用 `txgnn-pipeline` 技能確認上下文後，以下根據 Evidence Pack 產生評估報告：

---

# Fidaxomicin：從困難梭狀桿菌相關腹瀉到葡萄球菌燙傷樣皮膚症候群

## 一句話總結

Fidaxomicin（鼎腹欣）是一種窄譜口服抗生素，原本核准用於治療**困難梭狀桿菌相關腹瀉（CDAD）**。
TxGNN 模型預測它可能對**葡萄球菌燙傷樣皮膚症候群（Staphylococcal Scalded Skin Syndrome）** 有效（預測分數 99.71%）。
目前**無任何臨床試驗或支持性文獻**，屬純模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 困難梭狀桿菌相關腹瀉 (C. difficile-associated diarrhoea, CDAD) |
| 預測新適應症 | 葡萄球菌燙傷樣皮膚症候群 (Staphylococcal Scalded Skin Syndrome) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Data Gap）。根據已知資訊，Fidaxomicin 藉由抑制細菌 **RNA 聚合酶的 σ 因子釋放步驟**來發揮抗菌作用，對革蘭氏陽性菌（包括 *Clostridioides difficile*）具有高度選擇性。

葡萄球菌燙傷樣皮膚症候群（SSSS）由 *Staphylococcus aureus* 噬菌體 II 型產生的剝脫毒素所引起。由於 *S. aureus* 同屬革蘭氏陽性菌，Fidaxomicin 理論上可透過抑制其 RNA 聚合酶、減少毒素基因轉錄來發揮作用。CDAD 與 SSSS 同屬細菌毒素媒介疾病，這是模型做出此預測的生物學基礎。

然而，Fidaxomicin 有一個根本性的藥動學障礙：**口服生體可用率極低（< 1%）**，藥物幾乎全部停留於腸道局部，無法達到全身性治療 SSSS 所需的系統性血中濃度。目前亦無任何外用或靜脈注射劑型上市，因此在製劑條件未解決之前，機轉上的合理性難以轉化為臨床可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥輸字第025757號 | 鼎腹欣膜衣錠 200 毫克 | 膜衣錠 | 困難梭狀桿菌相關腹瀉 (C. difficile-associated diarrhoea, CDAD) |

---

## 安全性考量

**藥物交互作用**（資料庫共 79 筆，以下列出重要項目）：

| 交互藥物 | 嚴重程度 |
|---------|---------|
| Vibrio cholerae CVD 103-HgR 活性疫苗（口服霍亂疫苗） | **Major（重大）** |
| Alpelisib | Moderate（中度） |
| Apalutamide | Moderate（中度） |
| Binimetinib | Moderate（中度） |
| Picosulfuric acid | Moderate（中度） |
| Amiodarone | Minor（輕微） |
| Clarithromycin | Minor（輕微） |
| Cyclosporine | Minor（輕微） |
| Diltiazem | Minor（輕微） |
| Erythromycin | Minor（輕微） |

> **重要提示**：與口服活性霍亂疫苗的交互作用評為 **Major**，抗生素使用期間及停藥後 14 天內不建議接種活性疫苗。其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
所有 10 個 TxGNN 預測新適應症均屬 **L5 純模型預測**，無任何臨床試驗或直接文獻支持。更關鍵的是，Fidaxomicin 口服生體可用率極低（< 1%），其「腸道局部藥物」特性構成根本性的遞送障礙，在替代給藥途徑或製劑突破出現前，推進全身性感染適應症的臨床可行性極低。

**若要推進需要：**
- 補充 Fidaxomicin 對 *S. aureus* 的體外 MIC 數據（目前缺乏公開資料）
- 評估外用製劑（如局部皮膚應用）的技術可行性
- 取得 DrugBank 完整 MOA 資料以強化機轉分析
- 至少達到前臨床動物模型（in vivo）的初步療效證據，才可重新評估升至 Go
---

