---
layout: default
title: Axitinib
parent: 中證據等級 (L3-L4)
nav_order: 37
evidence_level: L4
indication_count: 4
monitor_inn: "Axitinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax"]
last_modified_at: 2026-10-23
description: "Axitinib：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L4）。原適應症：治療已接受過 sunitinib 或 cytokine 治療失敗的晚期腎細胞癌病患"
---

# Axitinib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

## Axitinib：從晚期腎細胞癌到脂肪肉瘤
{: .text-alpha }

## 一句話總結

Axitinib 是一種口服標靶藥物，在台灣核准用於已接受過 sunitinib 或 cytokine 治療失敗的晚期腎細胞癌。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效。
目前沒有相關臨床試驗，僅有 **1 篇**體外（細胞實驗）文獻支持，證據仍屬初步階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療已接受過 sunitinib 或 cytokine 治療失敗的晚期腎細胞癌病患 |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L4 |
| 台灣上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 收錄的詳細作用機轉資料。就一般藥理知識，Axitinib 是多標靶酪胺酸激酶抑制劑，主要作用於 VEGFR1-3，也影響 PDGFR 與 c-KIT，可阻斷由 VEGF 驅動的血管新生。

腎細胞癌是血管豐富的腫瘤，抗血管新生治療是其核心策略。黏液性脂肪肉瘤同樣依賴血管新生，因此從機轉上推測，抑制 VEGFR 有可能抑制腫瘤生長。

支持此預測的是一篇 2016 年的細胞株研究：針對黏液性脂肪肉瘤細胞株篩選多種藥物，發現抗血管新生藥物具抗腫瘤活性，Axitinib 即為其中之一。該研究的證據層級屬體外實驗，尚無臨床資料。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | 2016 | 體外研究 | Sarcoma | 在黏液性脂肪肉瘤細胞株中，Axitinib 顯示抗血管新生與抗腫瘤活性 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Axitinib 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025853號 | 抑癌特膜衣錠 1 毫克 | 膜衣錠 | 輝瑞大藥廠股份有限公司 | 2027/11/13 | 治療已接受過sunitinib或cytokine治療失敗的晚期腎細胞癌病患。 |
| 衛署藥輸字第025854號 | 抑癌特膜衣錠 5 毫克 | 膜衣錠 | 輝瑞大藥廠股份有限公司 | 2027/11/13 | 治療已接受過sunitinib或cytokine治療失敗的晚期腎細胞癌病患。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共 178 筆交互作用紀錄，以下為其中較重要者：
  - **嚴重 (Major)**：Clarithromycin、Dexamethasone
  - **中度 (Moderate)**：Aprepitant、Clotrimazole、Miconazole、Naltrexone
  - 其餘列出的多為輕微 (Minor) 等級，例如制酸劑（氫氧化鋁、碳酸鈣、氫氧化鎂等）、H2 受體阻斷劑（Famotidine、Ranitidine、Cimetidine、Nizatidine）及氫離子幫浦抑制劑（Rabeprazole、Esomeprazole、Lansoprazole、Dexlansoprazole）。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有一篇黏液性脂肪肉瘤細胞株的體外研究，無任何臨床試驗或人體資料，屬於研究假說階段。
- TxGNN 分數雖高，但單憑模型預測與前臨床資料，不足以支持進入臨床推進。

**若要推進需要：**
- 動物模型（如異種移植）驗證療效。
- 回顧性病例或小型 Phase 2 研究，評估 Axitinib 對脂肪肉瘤（尤其黏液性亞型）的療效。
- 補充 Axitinib 的作用機轉資料與安全性警語、禁忌症。
- 評估與目前標準治療的比較及合理的病人族群。

**其他預測適應症備註：** 卵巢黏液性脂肪肉瘤、血管脂肪瘤、家族性自發性氣胸三者均僅有模型預測，無臨床或文獻證據（證據等級 L5），建議皆為 Hold。其中家族性自發性氣胸在機轉上缺乏明確關聯。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | Axitinib 台灣中文品名寫成「英利達」 | 報告重生後已無此錯誤（2026-10-15：新報告正文未再出現中文品名「英利達」；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表只列出 pembrolizumab（吉舒達）的許可證 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

