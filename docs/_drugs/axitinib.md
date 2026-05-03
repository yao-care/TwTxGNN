---
layout: default
title: Axitinib
parent: 中證據等級 (L3-L4)
nav_order: 36
evidence_level: L3
indication_count: 10
---

# Axitinib
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Axitinib：從晚期腎細胞癌到未分類腎細胞癌

## 一句話總結

Axitinib（英利達）是高度選擇性的 VEGFR 酪胺酸激酶抑制劑，台灣核准用於接受過 sunitinib 或 cytokine 治療失敗的晚期腎細胞癌病患。
TxGNN 模型預測它可能對**未分類腎細胞癌 (Unclassified Renal Cell Carcinoma)** 有效，
目前有 **2 個真實世界觀察性研究**提供間接支持，尚無針對此特定亞型的直接文獻。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 晚期腎細胞癌（接受 sunitinib 或 cytokine 治療失敗後之二線治療） |
| 預測新適應症 | 未分類腎細胞癌 (Unclassified Renal Cell Carcinoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 Evidence Pack 中缺乏 Axitinib 的完整作用機轉原始資料（MOA 列為待補充）。根據既有文獻，Axitinib 是第二代口服 VEGFR 酪胺酸激酶抑制劑，核心機制為高度選擇性抑制 VEGFR-1、VEGFR-2 及 VEGFR-3，阻斷 VEGF 訊號通路，進而切斷腫瘤新生血管的養分供應。其對 VEGFR 家族的 IC50 較同類 TKI 低約 10 倍，靶點選擇性突出。

「未分類腎細胞癌」涵蓋所有病理上無法歸入已知亞型的腎上皮惡性腫瘤，異質性高，但現有研究提示多數亞型的腫瘤微環境中仍存在 VEGF 訊號通路活化，與 Axitinib 的抗血管新生機轉高度重疊。真實世界觀察性資料顯示，Axitinib 在廣義轉移性 RCC（包含清細胞及非清細胞亞型）中皆展現臨床療效，為此預測提供間接佐證。

值得注意的是，KEYNOTE-426（pembrolizumab + axitinib）及 JAVELIN Renal 101（avelumab + axitinib）兩項大型 Phase 3 RCT 已確立 axitinib 聯合免疫治療作為晚期 RCC 第一線標準治療的地位。此療效基礎延伸至未分類亞型在機轉上具合理性，但目前缺乏專門的前瞻性臨床試驗驗證，建議審慎推進。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04033991](https://clinicaltrials.gov/study/NCT04033991) | 真實世界研究 | 完成 | 684 | 英國單中心回顧性資料庫研究，評估轉移性/晚期 RCC 患者接受 sunitinib 一線及 axitinib 二線治療的真實世界 PFS，並依 MSKCC/IMDC 風險分類分層分析；可能涵蓋未分類亞型患者 |
| [NCT02156895](https://clinicaltrials.gov/study/NCT02156895) | 上市後監測 | 完成 | 111 | Axitinib（Inlyta）於 RCC 患者的上市後安全性與療效監測研究，提供真實使用情境下的直接觀察性資料 |

---

## 文獻證據

目前無相關文獻（針對「未分類腎細胞癌」與 axitinib 的直接文獻尚未收錄）。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部菌疫輸字第001025號 | 吉舒達注射劑 | 注射劑 | 1.黑色素細胞瘤：治療無法切除或轉移性黑色素瘤病人。作為輔助性療法治療患有第IIB或IIC期黑色素... |

> **資料說明**：本 Evidence Pack 台灣許可證資料顯示為 **吉舒達（Pembrolizumab/Keytruda）** 之登記，其核准適應症第 14 項明載「與 axitinib 併用，做為晚期腎細胞癌病人的第一線治療藥物」。Axitinib 本身（英利達/Inlyta，口服膜衣錠）之獨立許可證資料建議另行向台灣食藥署查核補充，以確認 Axitinib 單藥適應症及完整許可證清單。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（VEGFR 酪胺酸激酶抑制劑，第二代 TKI；非傳統細胞毒性藥物） |
| 骨髓抑制風險 | 低（TKI 類骨髓抑制少見，但仍需定期監測） |
| 致吐性分級 | 低度 |
| 監測項目 | 血壓（高血壓為最常見不良反應）、甲狀腺功能、肝腎功能（ALT/AST/Cr）、CBC、尿蛋白 |
| 處置防護 | 口服劑型，一般抗癌藥物安全操作規範即可；重點在高血壓預防性管理及療程中持續血壓監測 |

---

## 安全性考量

**藥物交互作用**（資料庫共收錄 178 筆 DDI，以下列出主要警示交互作用）：

| 交互藥物 | 嚴重程度 | 臨床意義 |
|---------|---------|---------|
| Clarithromycin | **主要（Major）** | CYP3A4 強效抑制劑，可顯著升高 axitinib 血中濃度，毒性風險倍增，應避免併用或密切監測 |
| Dexamethasone | **主要（Major）** | CYP3A4 強效誘導劑，可大幅降低 axitinib 暴露量，恐影響療效，需評估替代方案 |
| Aprepitant | 中度（Moderate） | CYP3A4 中等抑制劑，可中度升高 axitinib 濃度，需監測不良反應 |
| Clotrimazole | 中度（Moderate） | 外用/口腔抗黴菌劑，具 CYP3A4 抑制效應，系統性吸收後可能影響 axitinib 代謝 |
| Miconazole | 中度（Moderate） | 同上，CYP3A4 抑制效應 |
| Naltrexone | 中度（Moderate） | 交互作用機轉尚未完全釐清，建議臨床監測 |
| 制酸劑類（Famotidine、Ranitidine、制酸鋁鎂鹽等） | 輕微（Minor） | 可能輕微影響 axitinib 口服吸收，臨床意義有限 |
| PPI 類（Rabeprazole、Esomeprazole、Lansoprazole 等） | 輕微（Minor） | 同上 |

完整 178 筆交互作用詳情請查閱 DDInter 2.0 資料庫。其餘安全性警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Axitinib 的 VEGFR 抑制機轉在廣義 RCC 中已有充分的療效基礎（L1 級 Phase 3 RCT 支持一般 RCC），延伸至「未分類」亞型在機轉上具合理性；然而目前僅有 2 個間接真實世界觀察性研究，缺乏針對未分類亞型的直接前瞻性證據（L3），且 RCC 亞型異質性高，療效存在不確定性。

**若要推進需要：**
- 補充 Axitinib（DB06626）的完整 MOA 及 DrugBank 分類資料
- 釐清並補充 Axitinib（英利達/Inlyta 口服膜衣錠）在台灣的獨立許可證資料，與吉舒達資料脫鉤
- 設計針對未分類 RCC 亞型的前瞻性探索性 Phase 2 研究（建議納入 axitinib 單藥或聯合 ICI）
- 建立病患分子分型，識別 VEGF 訊號路徑依賴程度較高的亞群以提升療效預測
- 設計特定安全性監測計畫，涵蓋高血壓管理、甲狀腺功能及 CYP3A4 相關 DDI 審查
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

