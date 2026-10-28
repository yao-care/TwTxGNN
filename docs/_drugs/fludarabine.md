---
layout: default
title: Fludarabine
parent: 中證據等級 (L3-L4)
nav_order: 112
evidence_level: L3
indication_count: 10
monitor_inn: "Fludarabine"
predicted_indications: ["plasma cell myeloma", "hyperthyroidism", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "indolent plasma cell myeloma", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "brain small vessel disease 1 with or without ocular anomalies", "myelodysplastic syndrome", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "diabetic nephropathy"]
last_modified_at: 2026-10-16
description: "Fludarabine：預測新適應症為漿細胞骨髓瘤 (Plasma Cell Myeloma)（證據等級 L3）。原適應症：B 細胞慢性淋巴性白血病（CLL）、低惡性度非何杰金氏淋巴瘤（LG-NHL"
---

# Fludarabine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

## Fludarabine：從非何杰金氏淋巴瘤與慢性淋巴球性白血病到漿細胞骨髓瘤
{: .text-alpha }

## 一句話總結

Fludarabine 是嘌呤類似物（purine analog）化療藥，台灣許可證資料中的核准適應症以 B 細胞惡性腫瘤（非何杰金氏淋巴瘤、慢性淋巴球性白血病）為主。
TxGNN 模型預測它可能對**漿細胞骨髓瘤 (Plasma Cell Myeloma)** 有效，
目前有 **30 個臨床試驗**和 **20 篇文獻**列入此預測，但多數為含 fludarabine 的移植前處理或 CAR-T 淋巴清除情境，並非以 fludarabine 單獨治療骨髓瘤的證據。

<!-- review:begin fludarabine-original-indication-name-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「Fludarabine（癌即瓦）是嘌呤類似物（purine analog）」。「癌即瓦注射劑」（衛部菌疫輸字第000973號）的主成分是 obinutuzumab，不是 fludarabine；fludarabine 現行有效許可證是衛署藥輸字第022732號「福達樂靜脈凍晶注射劑」。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fludarabine-original-indication-name-2026-10-16 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | B 細胞慢性淋巴性白血病（CLL）、低惡性度非何杰金氏淋巴瘤（LG-NHL；限烷化基藥劑治療無效或惡化者）（衛署藥輸字第022732號） |
| 預測新適應症 | 漿細胞骨髓瘤 (Plasma Cell Myeloma) |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L3 |
| 台灣上市 | 上市中（有效許可證 1 張／共 3 張） |
| 許可證數 | 3 張（有效單方 1／有效複方 0／已註銷 2） |
| 建議決策 | Hold（作為研究問題持續追蹤；不建議以單藥骨髓瘤適應症推進） |

<!-- review:begin fludarabine-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／慢性淋巴球性白血病（CLL）、濾泡性淋巴瘤等 B 細胞惡性腫瘤（註：許可證資料中的單方適應症文字多為 CD20 抗體類產品的內容，與 fludarabine 本身的標示可能不一致，建議對照原廠仿單）」。台灣現行 fludarabine 許可證的適應症是 B 細胞慢性淋巴性白血病（CLL）與低惡性度非何杰金氏淋巴瘤（LG-NHL），未寫濾泡性淋巴瘤；已改為許可證寫法。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fludarabine-original-indication-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未收錄）。根據已知資訊，fludarabine 是嘌呤類似物，其活性代謝物會抑制 DNA 合成並造成明顯的淋巴細胞耗竭。

骨髓瘤與 CLL 同屬 B 細胞系惡性腫瘤，一篇 1992 年的綜述也討論了兩者的相似與差異。
fludarabine 在骨髓瘤中的角色，主要是作為異體幹細胞移植的減量前處理（reduced-intensity conditioning）骨幹，以及 BCMA CAR-T 療法的淋巴清除（lymphodepletion）用藥，而非直接的抗骨髓瘤藥物。

另有一篇體外與動物研究（PMID 17976186）顯示 fludarabine 對骨髓瘤細胞株有抑制作用，但這類研究對骨髓瘤的直接療效仍有爭議，需要更多臨床證據。

## 臨床試驗證據

資料中共有 30 個試驗，以下列出與 fludarabine 關聯度較高的 10 個。多數為移植前處理或 CAR-T 試驗，fludarabine 並非受試的主要介入。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | 提前終止 | 6 | Busulfan／fludarabine／cyclophosphamide 移植前處理用於骨髓瘤或骨髓纖維化；人數極少，證據有限 |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | 完成 | 20 | Fludarabine 併用 methoxyamine 用於復發或難治性血液惡性腫瘤；族群廣泛，非骨髓瘤專屬 |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | 完成 | 16 | 自體加非清髓異體移植用於高風險淋巴瘤、骨髓瘤或 CLL；fludarabine 可能為前處理一部分 |
| [NCT00909948](https://clinicaltrials.gov/study/NCT00909948) | Phase 1 | 提前終止 | 7 | 非清髓移植後刻意排斥供者移植物；樣本小 |
| [NCT00056966](https://clinicaltrials.gov/study/NCT00056966) | Phase 1/2 | 完成 | 24 | CD45 抗體與 alemtuzumab 的減量前處理異體移植 |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | 完成 | 213 | Cyclophosphamide／fludarabine／全身放射線的臍帶血移植前處理，用於血液疾病 |
| [NCT00606437](https://clinicaltrials.gov/study/NCT00606437) | Phase 1 | 完成 | 40 | 全身放射線加 fludarabine 前處理，合併臍帶血移植 |
| [NCT06045806](https://clinicaltrials.gov/study/NCT06045806) | Phase 3 | 進行中（不再收案） | 79 | Ide-cel 加 lenalidomide 維持治療；fludarabine 僅可能作為淋巴清除，屬機轉面的佐證 |
| [NCT07764978](https://clinicaltrials.gov/study/NCT07764978) | Phase 3 | 收案中 | 750 | BCMA/CD19 CAR-T 鞏固治療；fludarabine 僅涉及淋巴清除 |
| [NCT06413498](https://clinicaltrials.gov/study/NCT06413498) | Phase 3 | 進行中（不再收案） | 452 | Anito-cel 對比標準治療用於復發／難治性骨髓瘤；fludarabine 僅涉及淋巴清除 |

## 文獻證據

資料中的文獻多為世代研究與回顧，沒有以 fludarabine 為主要介入的隨機對照試驗。以下列出與 fludarabine 較相關者。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | 體外／動物研究 | Eur J Haematol | Fludarabine 在體外與體內均能抑制骨髓瘤細胞株 RPMI8226 |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | 世代研究（回顧性） | Bone Marrow Transplant | Fludarabine 加 treosulfan 的低毒性前處理用於骨髓瘤異體移植（34 位病人），可行 |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | 第一期研究 | Am J Clin Oncol | Bortezomib／fludarabine／melphalan（可加全骨髓照射）用於高風險或難治性骨髓瘤的異體移植前處理 |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | 第二期研究 | Leuk Res Rep | 分次 busulfan、fludarabine 與移植後 cyclophosphamide；2 位骨髓瘤病人，1 年非復發死亡率 33.3% |
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | 真實世界研究 | Transplant Cell Ther | Ide-cel 前的 fludarabine 淋巴清除暴露量與毒性相關 |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | 世代研究 | J Hematol Oncol | LEGEND-2 五年追蹤：BCMA CAR-T 可帶來長期緩解（fludarabine 非研究主體） |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | 世代研究 | Blood | Cilta-cel 在標準照護情境的結果 |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | 其他 | Eur J Haematol | Fludarabine 與漿細胞白血病（無摘要可供摘錄） |
| [1415309](https://pubmed.ncbi.nlm.nih.gov/1415309/) | 1992 | 回顧 | Am J Med | 骨髓瘤與 CLL 的異同 |
| [31058154](https://pubmed.ncbi.nlm.nih.gov/31058154/) | 2019 | 回顧 | Front Med | [18F]-Fludarabine 用於血液惡性腫瘤的 PET 影像 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Fludarabine 的不重複許可證共 **3 張**：有效單方 1 張、有效複方 0 張、已註銷 2 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第022732號 | 福達樂靜脈凍晶注射劑 | 凍晶注射劑 | 賽諾菲股份有限公司 | 2030/01/05 | 用於B細胞慢性淋巴性白血病(CLL)病患的起始治療及CLL與低惡性度非何杰金氏淋巴瘤(LG-NHL)病患，歷經至少一種標準內容的烷化基藥劑(ALKYLATING AGENT)的治療… |

<details><summary><strong>已註銷</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第023585號</td><td>福達樂錠</td><td>FLUDARABINE PHOSPHATE</td><td>2017/05/08</td></tr><tr><td>衛署藥輸字第025782號</td><td>"百博"伏達諾平25毫克/毫升靜脈凍晶注射劑</td><td>FLUDARABINE PHOSPHATE</td><td>2024/04/11</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤類似物） |
| 骨髓抑制風險 | 高（文獻指出使用可能導致明顯骨髓抑制與其他毒性） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 全血球計數（含分類）、肝腎功能；另據文獻，高劑量與神經毒性相關 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

此外，文獻顯示 fludarabine 合併化療後有發生治療相關 MDS／AML 的報告。

## 安全性考量

- **藥物交互作用**：資料庫共記錄 369 筆交互作用。其中中度者包括 metronidazole、rosuvastatin、simvastatin、tinidazole；輕度者包括 levofloxacin；其餘（如 doxycycline、amphotericin B、metformin、morphine、omeprazole 等）分級未明。

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 骨髓瘤相關證據幾乎都來自含 fludarabine 的移植前處理或 CAR-T 淋巴清除情境，缺乏 fludarabine 單獨或作為主要介入的骨髓瘤對照試驗。
- 其證據可支持「移植前處理與淋巴清除骨幹」的角色，不支持新增直接抗骨髓瘤適應症。藥物本身也有明顯骨髓抑制與免疫抑制風險。

**若要推進需要：**
- 明確定義用途（移植前處理或 CAR-T 淋巴清除，還是直接抗骨髓瘤），並分別彙整對應證據。
- 取得 fludarabine 的作用機轉資料（MOA）及原廠仿單的警語、禁忌症。
- 確認台灣許可證中 fludarabine 本身的核准適應症文字，因目前取得的單方適應症多屬 CD20 抗體類產品內容。
- 若要評估直接療效，需有骨髓瘤專屬、以 fludarabine 為主要介入的前瞻性試驗。

<!-- review:begin fludarabine-original-indication-next-step-2026-10-16 -->

> **查核加註（2026-10-16）**：TFDA 資料集中 fludarabine 現行有效許可證只有衛署藥輸字第022732號「福達樂靜脈凍晶注射劑」，適應症為 B 細胞慢性淋巴性白血病（CLL）與經烷化基藥劑治療無效或惡化之低惡性度非何杰金氏淋巴瘤，已列於快速總覽的查核更正。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fludarabine-original-indication-next-step-2026-10-16 -->

**其他預測適應症的簡要說明：**
- **骨髓發育不良症候群（MDS）**：證據等級 L2，有含 fludarabine 前處理的 Phase 2/3 試驗與隨機對照（如 PMID 31606445），但同樣是前處理骨幹角色，建議「Proceed with Guardrails」。
- **惰性漿細胞骨髓瘤、未分類 MDS**：證據等級 L3，屬研究問題。
- **甲狀腺機能亢進、糖尿病腎病變及其他罕見遺傳疾病**：僅有模型預測，缺乏可信的機轉或臨床證據，建議 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「癌即瓦注射劑」「瑞樂靶注射劑」兩列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症寫濾泡性淋巴瘤並稱單方適應症屬 CD20 抗體 | 更正（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 下一步稱取得的單方適應症多屬 CD20 抗體 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結把「癌即瓦」當成本藥品名 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

