---
layout: default
title: Mycophenolate Mofetil
parent: 中證據等級 (L3-L4)
nav_order: 171
evidence_level: L3
indication_count: 10
---

# Mycophenolate Mofetil
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

The txgnn-pipeline skill covers pipeline operations and doesn't add constraints to report generation. The system prompt (v5) contains the complete report format. Proceeding to generate the report now.

---

# Mycophenolate Mofetil：從器官移植排斥到 HIV 感染症

## 一句話總結

Mycophenolate Mofetil（MMF）是廣泛用於器官移植的免疫抑制劑，原適應症為預防腎臟、心臟和肝臟移植後的急性排斥反應及狼瘡性腎炎治療。
TxGNN 模型預測它可能對 **HIV 感染症 (HIV infectious disease)** 有效，
目前有 **10 個臨床試驗**和 **20 篇文獻**支持這個研究方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防腎臟、心臟和肝臟移植之急性器官排斥 |
| 預測新適應症 | HIV 感染症 (HIV infectious disease) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知研究文獻，MMF 的活性代謝物黴酚酸（Mycophenolic Acid, MPA）藉由抑制次黃嘌呤核苷單磷酸去氫酶（IMPDH），選擇性阻斷淋巴細胞的嘌呤從頭合成路徑，進而耗竭細胞內脫氧鳥苷三磷酸（dGTP）的儲量。

這個機轉與 HIV 治療存在直接的生物學關聯：HIV 進行逆轉錄複製時需大量消耗 dGTP，MMF 誘導的 dGTP 耗竭理論上可直接干擾 HIV 在活化 CD4+ T 細胞中的複製。體外研究也顯示 MPA 可增強 Abacavir 等核苷類反轉錄酶抑制劑的抗病毒活性，並可透過抑制淋巴細胞增殖減少病毒活化儲庫、降低免疫系統的慢性過度活化。

然而，這個機轉在臨床的實際效益尚未通過 Phase 3 RCT 驗證。現有臨床研究（含 Phase 4 MAN2 Study）規模偏小，且部分試驗因故撤回或處於「未知」狀態，尚無法得出明確結論。此外，MMF 作為免疫抑制劑，在 HIV 感染者中使用需特別評估進一步免疫抑制的安全性風險。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | 未知 | 90 | MAN2 Study：評估 MMF 是否能抑制未接受抗病毒治療之慢性 HIV-1 感染患者的免疫過活化，並觀察 CD4+ 計數、血漿 HIV-1 RNA 及病程進展 |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | 未知 | 90 | MAN2 子研究：評估 MMF 500mg BID 對 HIV-1 感染患者心血管代謝替代指標的影響（與 MAN2 同族群）|
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | 已撤回 | 0 | 評估 MMF 作為 Abacavir 輔助治療的安全性、耐受性與抗反轉錄病毒活性，針對治療失敗且多線暴露的 HIV 感染者（因故撤回，無有效數據）|
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | 完成 | 27 | HIV 感染者腎臟移植後多中心前瞻研究，MMF 作為免疫抑制方案組成，評估含 Raltegravir 的三聯抗病毒方案下 6 個月內急性排斥率 |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | 完成 | 10 | HIV 感染末期腎病患者腎臟移植安全性與有效性研究，MMF 作為免疫抑制組成，評估免疫功能受損族群接受移植的可行性 |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | 完成 | 5 | 以低強度化療（Fludarabine）加全身放療後異體 HSCT，誘導混合造血嵌合達成 HIV 功能性治療，MMF + Cyclosporin 作為移植後免疫抑制 |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | 完成 | 56 | 隨機雙盲先導研究：比較新型核苷類 DAPD 單用與 DAPD+MMF 聯用在多藥耐受 HIV 感染者中的安全性與抗病毒活性 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 已終止 | 8 | 抗 EPO 誘發純紅血球再生障礙（PRCA）治療研究：Cyclosporin+MMF vs. Cyclophosphamide+Prednisolone（主適應症非 HIV，提前終止）|
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | 招募中 | 56 | 老年高風險 AML 患者 TBF 方案半相合 HSCT，MMF 作為 GVHD 預防藥物（與 HIV 治療無直接關聯）|
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | 完成 | 80 | HLA 不相合非親屬骨髓移植加 PTCy+Sirolimus+MMF 預防 GVHD 於血液惡性腫瘤患者（與 HIV 治療無直接關聯）|

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39515757](https://pubmed.ncbi.nlm.nih.gov/39515757/) | 2025 | Cohort | Am J Transplant | 分析 2004–2022 年 HIV 感染者腎臟移植接受者（n=1,155），比較 r-ATG 與 IL2Ra 誘導方案聯合 Tacrolimus/MMF 的長期存活結果 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | Cohort | Clin Pharmacokinet | 評估低劑量 MMF 在接受 ABC+EFV+NFV 的 HIV 感染患者中的藥動學與藥效學，提示需進行 PK-PD 監測 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retrovir | 縱向研究顯示 MMF 聯合 HAART 對初始及慢性 HIV-1 感染患者的 T 細胞增殖與 HIV 特異性免疫無明顯有害影響 |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | Cohort | Clin Pharmacokinet | 評估 MMF 對多種抗反轉錄病毒藥物藥動學及細胞內核苷三磷酸庫（dGTP、dCTP、3TCTP）的影響 |
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Cohort | J Acquir Immune Defic Syndr | 隨機先導研究（n=17）：評估慢性 HIV-1 感染患者中斷 HAART 期間使用 MMF 對免疫反應及血漿/淋巴組織病毒載量的影響 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Case series | J Acquir Immune Defic Syndr | 5 名治療失敗 AIDS 患者加入 MMF 500mg BID 後觀察到細胞內 dGTP 耗竭及 HIV-1 RNA 下降，支持 MMF 輔助 ABC 的機轉假說 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | 回顧免疫抑制藥物在 HIV 疾病中的應用：討論免疫過活化作為疾病進展指標，及 MMF 透過 IMPDH 抑制干擾 HIV 複製的機轉與臨床潛力 |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Cohort | AIDS | 評估 DAPD（Amdoxovir）單用或聯合 MMF 在廣泛多藥耐受 HIV-1 感染中的安全性、耐受性及抗病毒活性 |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Case series | J Acquir Immune Defic Syndr | 7 名多藥耐受 AIDS 患者接受 MMF+ABC+ddI+APV+RTV 方案的先導研究，藥物耐受性良好，但未觀察到顯著病毒載量下降 |
| [23622672](https://pubmed.ncbi.nlm.nih.gov/23622672/) | 2013 | Cohort | Transplant Proc | 西班牙三級醫院 HIV 感染者腎臟移植經驗回顧，免疫抑制方案含 MMF，移植存活率與 HIV 陰性受者相近 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第026397號 | 免達抑膠囊250毫克 | 膠囊劑 | 與Cyclosporin和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥。 |
| 衛部藥輸字第027227號 | 山喜多注射劑500毫克(法國廠) | 凍晶注射劑 | 與cyclosporin和類固醇合併使用，以預防腎臟、心臟和肝臟移植之器官排斥。 |
| 衛署菌疫輸字第000526號 | 新睦樂凍晶注射劑 | 凍晶注射劑 | 用於新的腎臟移植(DE NOVO RENAL TRANSPLANTATION)、預防急性器官排斥現象之發生，而且是伴隨以CYCLOSPORIN的微乳劑型(MICROEMULSION)和皮質固醇為基礎的免疫抑制劑治療方式併用... |

> 注：本 JSON 提供 3 張許可證資料（含去重），台灣共有 20 張有效許可證，涵蓋膠囊劑、凍晶注射劑、膜衣錠等多種劑型。

---

## 安全性考量

**藥物交互作用**（共 92 筆，以下列出主要項目）：

| 交互藥物 | 嚴重程度 | 備註 |
|---------|---------|------|
| Activated charcoal（活性炭） | **Major（重大）** | 可顯著降低 MMF 吸收，應避免併用 |
| Rabeprazole / Omeprazole / Esomeprazole / Lansoprazole / Dexlansoprazole | Moderate（中度） | 質子幫浦抑制劑可降低 MMF 活性代謝物 MPA 的血中濃度 |
| Doxycycline / Tetracycline / Minocycline | Moderate（中度） | 四環黴素類抗生素可能影響 MMF 的腸肝循環，降低暴露量 |
| Clarithromycin / Amoxicillin / Vancomycin / Kanamycin / Paromomycin | Moderate（中度） | 抗生素改變腸道菌叢，可能干擾 MMF 代謝物的再活化 |
| Aluminum hydroxide / Calcium carbonate / Magnesium oxide | Moderate（中度） | 制酸劑可能降低 MMF 吸收，建議錯開服用時間 |
| Zinc sulfate / Zinc acetate / Iron | Minor（輕微） | 微量元素補充劑可能輕度影響 MMF 吸收 |

> 完整 92 筆交互作用資料請參考 DDInter 資料庫，其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉假說合理（IMPDH 抑制 → dGTP 耗竭 → 干擾 HIV 逆轉錄），且有多項早期臨床研究提供概念驗證；但目前僅達 L3 證據等級，缺乏已完成的 Phase 3 RCT，且已有 Phase 1/2 試驗（NCT00021489）因故撤回。
- 在 HIV 感染者中使用免疫抑制劑存在加重免疫缺乏的潛在風險，需審慎評估風險效益比，需更嚴謹的臨床設計來確認療效與安全性。

**若要推進需要：**
- 確認 MMF 完整的作用機轉資料（DrugBank MOA）
- 設計適當的 Phase 2 RCT，納入現代抗病毒治療背景（如整合酶抑制劑方案），評估 MMF 對 HIV 儲庫及免疫活化指標的影響
- 評估 MMF 在 HIV 感染者中的長期安全性，特別是機會性感染風險
- 確認 MAN2 Study（NCT00120419）的完整結果資料（目前狀態為「未知」）
- 針對 HIV 合併腎臟移植的特定族群，收集 MMF 劑量最佳化數據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

