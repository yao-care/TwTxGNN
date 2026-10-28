---
layout: default
title: Doxorubicin
parent: 高證據等級 (L1-L2)
nav_order: 93
evidence_level: L1
indication_count: 8
monitor_inn: "Doxorubicin"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)"]
last_modified_at: 2026-10-29
description: "Doxorubicin：預測新適應症為尤文氏肉瘤 (Ewing sarcoma)（證據等級 L1）。原適應症：急慢性白血球過多症、硬瘤、淋巴瘤、軟纖維性肉瘤、交感神經母細胞瘤、乳癌、肺癌"
---

# Doxorubicin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **8** 個
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

## Doxorubicin：蒽環類 DNA 嵌入劑與拓撲異構酶 II 抑制劑 → 尤文氏肉瘤 (Ewing sarcoma)
{: .text-alpha }

## 一句話總結

Doxorubicin 是蒽環類（anthracycline）細胞毒性化療藥物。
TxGNN 模型預測它可能對**尤文氏肉瘤 (Ewing sarcoma)** 有效。
目前有 **30 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多個已完成的 Phase 3 隨機試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急慢性白血球過多症、硬瘤、淋巴瘤、軟纖維性肉瘤、交感神經母細胞瘤、乳癌、肺癌。; 用於治療CD4數量低下(<200 CD4 LYMPHOCYTES/MM3）和黏膜、皮膚或內臟有病變的AIDS RELATED KAPOSI'S SARCOMA的病人。用於治療曾接受第一線含鉑類藥物(PLATINUM-BASED)化學治療而失敗者或再復發之進行性或轉移性卵巢癌病人。可用於單一治療有心臟疾病風險考量之轉移性乳癌患者。可與bortezomib併用治療於曾接受過至少一種治療方式且已經接受或不適宜接受骨髓移植的進展性多發性骨髓瘤病人。; 抗癌藥; 用於治療CD4數量低下(<200 D4 LYMPHOCYTE |
| 預測新適應症 | 尤文氏肉瘤 (Ewing sarcoma) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L1 |
| 台灣上市 | 上市中（有效許可證 7 張／共 28 張） |
| 許可證數 | 28 張（有效單方 7／有效複方 0／已註銷 21） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏來自 DrugBank 的詳細作用機轉資料。
依本報告所整理的資料，doxorubicin 可嵌入 DNA 並抑制拓撲異構酶 II，造成 DNA 損傷，對快速增生的小圓細胞腫瘤具有細胞毒性。

尤文氏肉瘤是好發於兒童、青少年與年輕成人的骨與軟組織惡性腫瘤。
目前主流的多藥化療組合，如 VDC/IE（vincristine、doxorubicin、cyclophosphamide 與 ifosfamide、etoposide 交替），都以 doxorubicin 為核心成分。
多個隨機 Phase 3 試驗與多篇文獻也以含 doxorubicin 的方案作為標準治療骨幹。

因此從機轉與臨床使用來看，模型預測有相當的合理性。
需要注意，現有證據多半是「含 doxorubicin 的多藥合併方案」的整體結果，很難單獨拆出 doxorubicin 的貢獻。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 完成 | 587 | 比較不同化療強度（間隔縮短）搭配放射治療或手術，用於尤文氏肉瘤及相關腫瘤 |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 完成 | 642 | 在含 vincristine、doxorubicin、cyclophosphamide、ifosfamide、etoposide 的標準五藥方案上，加入 vincristine-topotecan-cyclophosphamide，用於非轉移性尤文氏肉瘤 |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 完成 | 278 | 隨機比較標準與強化治療，用於非轉移性尤文氏肉瘤 |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 未知 | 1200 | EURO-E.W.I.N.G.99：歐洲多國研究，評估含放射治療、手術與幹細胞移植的合併化療 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 進行中（不再招募） | 312 | 在含 doxorubicin 的多藥化療上加入 ganitumab，用於新診斷轉移性尤文氏肉瘤 |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | 未知 | 未提供 | EICESS 92：隨機比較多種合併化療，搭配手術與放射治療 |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | 完成 | 未提供 | VAC 加 dexrazoxane，搭配或不搭配 ImmTher，用於高風險尤文氏肉瘤 |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | 提前終止 | 46 | 評估高劑量強度 VAC 加 dexrazoxane 的 2 年無病存活與毒性 |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | 完成 | 未提供 | 含 doxorubicin 的多藥化療，之後接手術與放射治療，用於週邊原始神經外胚層腫瘤或尤文氏肉瘤 |
| [NCT01313884](https://clinicaltrials.gov/study/NCT01313884) | Phase 2 | 提前終止 | 3 | cyclophosphamide/doxorubicin/vincristine 與 irinotecan/temozolomide 交替，用於轉移性尤文氏肉瘤；僅收 3 人，無法解讀 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 在標準化療上加入 ifosfamide 與 etoposide，檢驗能否改善新診斷尤文氏肉瘤與骨原始神經外胚層腫瘤的存活 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012：開放性 Phase 3，比較歐洲與美國兩種標準化療策略 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | 在間隔縮短的化療上加入 ganitumab，用於新診斷轉移性尤文氏肉瘤的 Phase 3 試驗 |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | 間隔縮短化療（VDC 與 IE 交替）用於局部尤文氏肉瘤的隨機試驗 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT（試驗計畫） | Trials | EURO EWING 2012 國際隨機試驗的設計 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review | Cancer | 國家尤文氏肉瘤腫瘤委員會的治療共識建議 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | 以風險分層的密集新輔助與輔助化療，搭配手術與放射治療的多專科治療現況 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | 化療使局部疾病存活率由約 10% 提升至約 75%，轉移性疾病預後仍差 |
| [25993235](https://pubmed.ncbi.nlm.nih.gov/25993235/) | 2015 | Review | ASCO Educ Book | 骨肉瘤與尤文氏肉瘤的全身性治療，需結合有效化療與局部控制 |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | 文獻分析 | J Natl Cancer Inst | 分析 doxorubicin 劑量強度與骨肉瘤、尤文氏肉瘤反應及預後的關係 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Doxorubicin 的不重複許可證共 **28 張**：有效單方 7 張、有效複方 0 張、已註銷 21 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第036418號 | 利癌凍晶注射劑10毫克(多索如比辛) | 凍晶注射劑 | 南光化學製藥股份有限公司 | 2028/06/02 | 急慢性白血球過多症、硬瘤、淋巴瘤、軟纖維性肉瘤、交感神經母細胞瘤、乳癌、肺癌。 |
| 衛署藥製字第041037號 | 力得微脂體注射劑2毫克/毫升（鹽酸杜薩魯比辛） | 注射劑 | 台灣東洋藥品工業股份有限公司 | 2028/09/18 | 用於治療CD4數量低下(<200 CD4 LYMPHOCYTES/MM3）和黏膜、皮膚或內臟有病變的AIDS RELATED KAPOSI'S SARCOMA的病人。用於治療曾接受… |
| 衛署藥輸字第022712號 | 艾黴素注射液 | 注射劑 | 輝瑞大藥廠股份有限公司 | 2029/12/21 | 急慢性白血球過多症、硬瘤、淋巴瘤、軟纖維性肉瘤、交感神經母細胞瘤、乳癌、肺癌。 |
| 衛署藥輸字第025867號 | 鹽酸杜薩魯比辛 | （粉） | 川聖貿易股份有限公司 | 2027/12/02 | 抗癌藥 |
| 衛部藥製字第061125號 | "意欣"杜索拉凍晶注射劑 | 凍晶注射劑 | 意欣國際有限公司 | 2027/06/13 | 急慢性白血球過多症、硬瘤、淋巴瘤、軟纖維性肉瘤、交感神經母細胞瘤、乳癌、肺癌。 |
| 衛部藥製字第061132號 | "霖揚"鹽酸杜薩魯比辛凍晶注射劑10毫克 | 凍晶注射劑 | 霖揚生技製藥股份有限公司 | 2027/07/08 | 急慢性白血球過多症、硬瘤、淋巴瘤、軟纖維性肉瘤、交感神經母細胞瘤、乳癌、肺癌。 |
| 衛部藥輸字第027886號 | 德露斯微脂體注射劑2毫克/毫升 | 注射劑 | 台灣瑞迪博士有限公司 | 2030/05/19 | 用於治療CD4數量低下(<200 D4 LYMPHOCYTES/ MM3)和黏膜、皮膚或內臟有病變的AIDS RELATED KAPOSI’S SARCOMA的病人。用於治療曾接受… |

<details><summary><strong>已註銷</strong>（21 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第012027號</td><td>艾黴素注射劑</td><td>DOXORUBICIN HCL</td><td>2004/12/16</td></tr><tr><td>衛署藥輸字第014812號</td><td>艾黴素注射劑５０公絲</td><td>DOXORUBICIN HCL</td><td>2004/12/16</td></tr><tr><td>衛署藥輸字第018174號</td><td>德壽魯素注射劑</td><td>DOXORUBICIN HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第018176號</td><td>達必素注射劑</td><td>DOXORUBICIN HCL</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第018580號</td><td>"速溶"艾黴素注射劑10毫克</td><td>DOXORUBICIN HCL</td><td>2024/06/18</td></tr><tr><td>衛署藥輸字第018613號</td><td>"速溶" 艾黴素注射劑５０公絲</td><td>DOXORUBICIN HCL</td><td>2022/06/30</td></tr><tr><td>衛署藥輸字第019117號</td><td>德壽魯素注射液２公絲/１公撮</td><td>DOXORUBICIN HCL</td><td>1997/09/02</td></tr><tr><td>衛署藥輸字第019443號</td><td>待朗必信靜脈凍晶注射劑５０公絲</td><td>DOXORUBICIN HCL</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第019444號</td><td>待明必信靜脈凍晶注射劑１０公絲</td><td>DOXORUBICIN HCL</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第020335號</td><td>得甦幸注射劑</td><td>DOXORUBICIN HCL</td><td>1997/06/30</td></tr><tr><td>衛署藥輸字第021576號</td><td>德壽魯素注射液２公絲／公撮</td><td>DOXORUBICIN HCL</td><td>2019/03/27</td></tr><tr><td>衛署藥輸字第021718號</td><td>得甦幸注射劑</td><td>DOXORUBICIN HCL</td><td>2000/01/27</td></tr><tr><td>衛署藥輸字第022174號</td><td>阿雷素凍晶注射劑５０公絲/小瓶</td><td>DOXORUBICIN HCL</td><td>2014/03/05</td></tr><tr><td>衛署藥輸字第022175號</td><td>阿雷素凍晶注射劑１０公絲/小瓶</td><td>DOXORUBICIN HCL</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第022207號</td><td>康利斯微脂粒注射劑</td><td>DOXORUBICIN HCL</td><td>2013/10/25</td></tr><tr><td>衛署藥輸字第025840號</td><td>癌佐莓注射液</td><td>DOXORUBICIN HCL</td><td>2024/06/18</td></tr><tr><td>衛署藥輸字第026026號</td><td>艾諾幸"艾威群"注射液2毫克/毫升</td><td>DOXORUBICIN HCL</td><td>2024/05/07</td></tr><tr><td>衛部藥輸字第025808號</td><td>多受祿注射劑2毫克/毫升</td><td>DOXORUBICIN HYDROCHLORIDE</td><td>2024/04/26</td></tr><tr><td>衛部藥輸字第026249號</td><td>克思癌微脂體注射劑2毫克/毫升(鹽酸杜薩魯比辛)</td><td>DOXORUBICIN HCL</td><td>2014/10/08</td></tr><tr><td>衛部藥輸字第026572號</td><td>"精金"德舒癌注射液2毫克/毫升</td><td>DOXORUBICIN HCL</td><td>2022/06/16</td></tr><tr><td>衛部藥輸字第028057號</td><td>多受祿凍晶注射劑</td><td>DOXORUBICIN HYDROCHLORIDE、DOXORUBICIN HYDROCHLORIDE</td><td>2025/08/25</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（蒽環類，DNA 嵌入劑與拓撲異構酶 II 抑制劑） |
| 骨髓抑制風險 | 高（常見嗜中性白血球減少、白血球減少、血小板減少與貧血） |
| 致吐性分級 | 中至高（與 cyclophosphamide 併用時偏高） |
| 監測項目 | CBC（含分類）、肝腎功能、心臟功能（如左心室射出分率）、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作（配製、給藥與廢棄物處理） |

蒽環類具累積性心臟毒性，兒童與年輕病人長期存活後仍需追蹤。
詳細警語請參考原廠仿單。

## 安全性考量

- **藥物交互作用**：資料庫共收錄 665 筆交互作用。列為 Major 的包括 dolasetron、cisapride、papaverine。常見 Moderate 的有 ondansetron、granisetron、palonosetron、aprepitant、rolapitant、dexamethasone、clarithromycin、levofloxacin 等，其中不少是化療常用的止吐藥，併用時需留意。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 尤文氏肉瘤已有多個已完成的 Phase 3 隨機試驗與高品質文獻，所用的標準多藥方案都以 doxorubicin 為核心成分之一，證據等級為 L1。
- doxorubicin 的骨髓抑制與累積性心臟毒性明確，且證據多來自合併方案，因此需設定安全防護。

**若要推進需要：**
- 釐清 doxorubicin 在多藥方案中的獨立貢獻，例如以各試驗的方案細節與分層分析確認。
- 核對本地許可證的適應症，確認尤文氏肉瘤是否屬於已核准用途，以及是否需要新增適應症申請。
- 建立心臟功能（累積劑量與 LVEF）與血液學監測計畫。
- 補充詳細作用機轉資料與完整的警語、禁忌症資訊。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 一句話總結以併用藥物許可證的適應症為原用途 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症取自 trastuzumab 類許可證 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表列 polatuzumab vedotin 製劑「保癌寧」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 資料說明「20 張許可證均登記為相同許可證號」 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 標題以 HER2 陽性乳癌與 DLBCL 為原用途 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

