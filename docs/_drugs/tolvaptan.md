---
layout: default
title: Tolvaptan
parent: 高證據等級 (L1-L2)
nav_order: 285
evidence_level: L1
indication_count: 10
---

# Tolvaptan
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Tolvaptan：從自體顯性多囊性腎臟病到 PKD3 型多囊性腎臟病（合併或不合併多囊肝）

## 一句話總結

Tolvaptan 是一種口服血管加壓素 V2 受體拮抗劑，原本用於延緩自體顯性多囊性腎臟病（ADPKD）的惡化，以及治療心臟衰竭與 SIADH 引起的低血鈉症。
TxGNN 模型預測它可能對**多囊性腎臟病第 3 型，合併或不合併多囊肝 (polycystic kidney disease 3 with or without polycystic liver disease)** 有效。
目前本報告彙整的資料中沒有登記的臨床試驗，但有 **19 篇文獻**支持這個方向，其中包含 2 篇 RCT（TEMPO 3:4 與 REPRISE）與 1 篇統合分析。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 自體顯性多囊性腎臟病（ADPKD），適用於 eGFR 大於 25 mL/min/1.73m² 且已出現病情迅速惡化跡象之慢性腎臟病成人患者 |
| 預測新適應症 | 多囊性腎臟病第 3 型，合併或不合併多囊肝 (polycystic kidney disease 3 with or without polycystic liver disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（資料彙整的評等；但上述 RCT 針對 ADPKD 整體，並非專門針對 PKD3，見下方說明） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 7 張（有效單方 7／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Tolvaptan 是選擇性的血管加壓素 V2 受體拮抗劑。V2 受體被阻斷後，腎臟細胞內的 cAMP 會下降，而 cAMP 正是驅動囊泡液體分泌與囊泡細胞增生的關鍵因子。原廠機轉資料欄位目前缺漏，但上述機轉在文獻中有充分描述（如 PMID 28614813、18434616）。

PKD3（GANAB 基因相關）屬於 ADPKD 的遺傳亞型，與 PKD1/PKD2 同樣呈現 cAMP 驅動的囊泡形成，並可合併多囊肝。因此，Tolvaptan 對 PKD1/PKD2 為主的 ADPKD 所展現的療效，可合理外推至 PKD3，這也是模型給出高分的原因。

需要注意的是，目前的 RCT（TEMPO 3:4、REPRISE）主要納入 PKD1/PKD2 族群，**沒有專門針對 PKD3 的直接證據**，此為外推而來。此外，ADPKD 本身已是 Tolvaptan 在台灣的核准適應症，所以這項預測更像是對既有適應症的基因亞型擴充，而非全新疾病領域。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | TEMPO 3:4 試驗：V2 受體拮抗劑可抑制囊泡生長、延緩腎功能下降（早期 ADPKD） |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | 針對較晚期 ADPKD 的試驗，評估療效與安全性；先前試驗顯示肝臟轉胺酶與膽紅素上升較多 |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | 統合分析 | Cochrane Database Syst Rev | 評估各種延緩 ADPKD 進展的介入措施 |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD 綜述，涵蓋疾病特徵與治療 |
| [41771281](https://pubmed.ncbi.nlm.nih.gov/41771281/) | 2026 | Review | Lancet | Tolvaptan 為疾病修飾治療，建議高風險族群早期使用 |
| [40844441](https://pubmed.ncbi.nlm.nih.gov/40844441/) | 2025 | Review | Am J Kidney Dis | 腎體積、腎功能與基因突變可預測進展風險，以篩選適合疾病修飾治療者 |
| [40268755](https://pubmed.ncbi.nlm.nih.gov/40268755/) | 2025 | Review | Renal Failure | ADPKD 遺傳與臨床進展總覽，含腎外表現 |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Tolvaptan 為目前唯一獲 FDA 核准的疾病進展治療，另有新療法在發展中 |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | 多囊肝是 ADPKD 最常見的腎外表現；Tolvaptan 可延緩腎功能惡化與囊泡生長 |
| [32392574](https://pubmed.ncbi.nlm.nih.gov/32392574/) | 2021 | Review | Pediatr Res | 討論青少年與年輕成人快速進展者使用 Tolvaptan |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tolvaptan 的不重複許可證共 **7 張**：有效單方 7 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025295號 | 伸舒康錠30毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2030/11/23 | SAMSCA適用於治療心臟衰竭及抗利尿激素分泌不當症候群（SIADH）引起之低血鈉症。 |
| 衛署藥輸字第025296號 | 伸舒康錠15毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2030/11/23 | SAMSCA適用於治療心臟衰竭及抗利尿激素分泌不當症候群（SIADH）引起之低血鈉症。 |
| 衛部藥輸字第027341號 | 佳腎康錠15毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027342號 | 佳腎康錠30毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027343號 | 佳腎康錠45毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027344號 | 佳腎康錠60毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027345號 | 佳腎康錠90毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **禁忌症（知識圖譜資料，非仿單文字）**：知識圖譜列出的藥物－疾病禁忌關聯包括肝衰竭、肝硬化、物質濫用/依賴、活動性消化性潰瘍、脫髓鞘疾病。
- **肝臟安全性**：文獻指出 Tolvaptan 可使肝臟轉胺酶與膽紅素上升較多，需進行肝功能監測。
- **藥物交互作用**：資料庫共收錄 128 項交互作用。主要例子包括：
  - 重大（Major）：Clarithromycin
  - 中度（Moderate）：Aprepitant、Dexamethasone、Miconazole、Rifaximin、Rolapitant、Empagliflozin，以及多種鉀補充劑（氯化鉀、檸檬酸鉀、碳酸氫鉀、葡萄糖酸鉀）
  - 另需審視 CYP3A4 抑制劑與誘導劑的併用

其餘警語與詳細禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Tolvaptan 在 ADPKD 已有 Phase 3 RCT 與統合分析支持，並已於台灣取得 ADPKD 適應症；PKD3 與 PKD1/PKD2 共享 cAMP 驅動的囊泡形成機轉，外推合理。但目前缺乏 PKD3 專屬的臨床證據，且有肝損傷風險，因此需設置安全防護。

**若要推進需要：**
- 蒐集 PKD3（GANAB）患者使用 Tolvaptan 的臨床或真實世界資料
- 建立肝功能監測計畫（用藥前與用藥期間定期檢測）
- 確認病人符合仿單的 eGFR 門檻與快速惡化標準
- 逐項審視併用藥物，特別是 CYP3A4 抑制劑與誘導劑
- 補充詳細的作用機轉資料與完整仿單警語、禁忌症
- 對於預測排名較後的其他疾病（如腎肝胰發育不良、卡里奧巨核間質性腎炎等），目前僅有模型預測、缺乏實質證據，建議暫不推進（Hold）

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「許可證數：19 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表下「台灣共有 19 張許可證」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「PKD3 由 GANAB 或 DNAJB11 基因突變引起」 | 報告重生後已無此錯誤（2026-10-15：新報告寫 PKD3 為 GANAB 基因相關，未再列 DNAJB11；原為加註） | [NCBI MedGen：Polycystic kidney disease 3 with or without polycystic liver disease（C3887964）](https://www.ncbi.nlm.nih.gov/medgen/854672)；[NCBI MedGen：Polycystic kidney disease 6 with or without polycystic liver disease（C4748044）](https://www.ncbi.nlm.nih.gov/medgen/1648469) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L1） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

