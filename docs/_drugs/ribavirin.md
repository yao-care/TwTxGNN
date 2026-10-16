---
layout: default
title: Ribavirin
parent: 高證據等級 (L1-L2)
nav_order: 243
evidence_level: L2
indication_count: 10
---

# Ribavirin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Ribavirin：從慢性 C 型肝炎到慢性 B 型肝炎

## 一句話總結

Ribavirin 是一種核苷類抗病毒藥物，原本與干擾素或直接作用抗病毒藥物（DAA）併用，治療慢性 C 型肝炎。
TxGNN 模型預測它可能對**慢性 B 型肝炎 (Chronic Hepatitis B Virus Infection)** 有效，
目前有 **15 個臨床試驗**和 **20 篇文獻**與此方向相關，但多數為 C 型肝炎研究或綜述，直接針對 B 型肝炎的證據有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 與其他藥物併用治療慢性 C 型肝炎病毒（HCV）感染（成人；基因型 1–4，依併用藥物而異），亦用於 12 歲以上兒童之基因型 2 或 3 感染 |
| 預測新適應症 | 慢性 B 型肝炎 (Chronic Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 13 張（有效單方 2／有效複方 0／已註銷 11） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠機轉欄位為空）。根據本報告彙整的機轉分析，Ribavirin 是鳥苷類似物，可抑制 IMPDH 酶而耗竭細胞內 GTP 庫，並干擾病毒聚合酶活性，同時具有促進 Th1 反應的免疫調節作用。

在 C 型肝炎中，Ribavirin 長期是干擾素療法的搭配藥物。B 型與 C 型肝炎同為慢性病毒性肝炎，臨床上也常有共同感染的情形，因此模型會把兩者拉近。其免疫調節作用可能增強干擾素在 B 型肝炎的反應。

但需要注意：Ribavirin 單獨使用時，幾乎沒有直接的抗 HBV 活性。現有 B 型肝炎試驗（如 PARC 研究）也未看到加入 Ribavirin 後有明確的額外好處。因此這個預測屬於「值得研究的問題」，尚不足以視為有效的治療選項。

---

## 臨床試驗證據

以下依與 B 型肝炎的相關程度挑選。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | 完成 | 138 | PEG-IFN alfa-2a 併用 Ribavirin 對比 PEG-IFN 單用，治療 HBeAg 陰性慢性 B 型肝炎；未見 Ribavirin 明確的額外效益 |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | 完成 | 120 | 干擾素 alfa-2b 併用 Ribavirin 治療慢性 B 型肝炎的前導試驗 |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | 未知 | 24 | 在 HBV 核苷類似物治療上加入 Ribavirin，探索免疫調節作用的前導試驗 |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | 未知 | 320 | PEG-IFN alfa-2a 併用 Ribavirin，用於 HCV/HBV 共同感染與慢性 C 型肝炎的比較 |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | 未知 | 20 | PEG-IFN alfa-2b 併用 Ribavirin，用於 B 型與 D 型肝炎雙重感染的前導試驗 |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | 完成 | 129 | PEG-IFN alfa-2a 加 Ribavirin 治療 HCV 基因型 1，探討 IL-28B 表現與持續病毒學反應（與 HBV 僅部分相關） |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | 完成 | 36 | Ombitasvir/paritaprevir/ritonavir 加 dasabuvir 與 Ribavirin，治療失代償性肝硬化的 HCV（HCV 研究） |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Phase 3 | 完成 | 72 | 埃及基因型 4 HCV 患者，複方 sofosbuvir/daclatasvir/Ribavirin 與分開給藥比較（HCV 研究） |
| [NCT01309932](https://clinicaltrials.gov/study/NCT01309932) | Phase 2 | 完成 | 165 | PEG-IFN lambda 併用 Ribavirin 與 DAA，對比 Pegasys 加 Ribavirin，治療 HCV 基因型 1（HCV 研究） |
| [NCT01795911](https://clinicaltrials.gov/study/NCT01795911) | Phase 2 | 完成 | 165 | 與上一項為同一系列研究的另一登記（HCV 研究） |

**說明：**
- 直接與 B 型肝炎相關的試驗是前四項與 NCT00117533；其中完成且規模較大的 Phase 3 是 NCT00114361，且未顯示 Ribavirin 有明確額外效益。
- 其餘多為 C 型肝炎試驗，只能作為藥物安全性與併用經驗的間接參考。
- 本表另有數項 HCV 試驗未列出。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV 共同感染的處置；過去建議 PEG-IFN 加 Ribavirin 用於 HCV RNA 陽性者 |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | HCV/HBV 雙重感染的治療與預後更新；雙重感染者肝病進展風險較高 |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | 綜述（未分類） | World J Gastroenterol | 干擾素加或不加 Ribavirin 為早期療法；DAA 出現後 HCV 可治癒，HBV 仍需長期治療 |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | 綜述（未分類） | Annu Rev Med | B 型與 C 型肝炎的當時治療策略 |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | 慢性 B 型與 C 型肝炎抗病毒治療的免疫學觀點 |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | IL28B 基因型與 B、C 型肝炎治療反應的關係 |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B 多型性與 B 型肝炎感染結果的關聯 |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | 兒童慢性 B 型與 C 型肝炎的治療選項 |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | 慢性病毒性肝炎的肝細胞癌預防 |
| [11929032](https://pubmed.ncbi.nlm.nih.gov/11929032/) | 2002 | Review | Indian J Pediatr | B 型與 C 型肝炎感染的處置 |

**說明：**
- 所列文獻全為綜述，沒有 B 型肝炎的 RCT 文獻。
- 這些文獻多只在談及 C 型肝炎或雙重感染時提到 Ribavirin，並未提供它對 HBV 有效的直接證據。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Ribavirin 的不重複許可證共 **13 張**：有效單方 2 張、有效複方 0 張、已註銷 11 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第048027號 | 摩舒肝清膠囊 | 膠囊劑 | 東生華製藥股份有限公司 | 2031/06/20 | 與PEGINTERFERON α 或 α -INTERFERON併用治療：1.曾經使用 α -INTERFERON單一療法治療後又復發的慢性C型肝炎。2.首次接受治療的慢性C型肝炎… |
| 衛署藥製字第048152號 | 源展膠囊200毫克 | 膠囊劑 | 健喬信元醫藥生技股份有限公司 | 2031/08/02 | 與peginterferon α 或α-interferon 併用治療：1.曾經使用α-interferon 單一療法後又復發的慢性C型肝炎。2.首次接受治療的慢性C型肝炎。 |

<details><summary><strong>已註銷</strong>（11 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第027769號</td><td>速百敏膠囊</td><td>BIOTIN、CHLORPHENIRAMINE MALEATE、GLYCYRRHIZIN (AMMONIATED)、RI…</td><td>1991/09/24</td></tr><tr><td>衛署藥製字第044650號</td><td>羅拔除膠囊200毫克</td><td>RIBAVIRIN</td><td>2021/10/21</td></tr><tr><td>衛署藥輸字第017379號</td><td>丕拉弱凍晶吸入劑</td><td>RIBAVIRIN</td><td>1995/09/18</td></tr><tr><td>衛署藥輸字第021029號</td><td>丕拉弱凍晶吸入劑</td><td>RIBAVIRIN</td><td>1998/08/05</td></tr><tr><td>衛署藥輸字第022173號</td><td>丕拉弱凍晶吸入劑</td><td>RIBAVIRIN</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第023204號</td><td>利必妥合併療法（因治隆注射液六百萬單位﹨毫升合併瑞比達膠囊２</td><td>RIBAVIRIN、INTERFERON ALPHA- 2B</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第023205號</td><td>利必妥合併療法（因治隆注射液一千五百萬單位/毫升合併瑞比達膠</td><td>INTERFERON ALPHA- 2B、RIBAVIRIN</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第023208號</td><td>瑞比達膠囊</td><td>RIBAVIRIN</td><td>2019/02/12</td></tr><tr><td>衛署藥輸字第025232號</td><td>適維肝膠囊 200 毫克</td><td>RIBAVIRIN</td><td>2022/06/23</td></tr><tr><td>衛署藥輸字第025605號</td><td>可珮格膜衣錠200毫克</td><td>RIBAVIRIN</td><td>2021/10/20</td></tr><tr><td>衛署藥輸字第025995號</td><td>立貝維爾</td><td>Ribavirin</td><td>2024/05/02</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **模型關聯之潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物與疾病禁忌關聯，並非仿單文字）：
  - 血液相關：貧血（含溶血性貧血、巨球性貧血）、鐮型血球貧血、血紅素病變、全血球減少、遺傳性再生不良性貧血
  - 心血管：心肌梗塞、冠狀動脈疾病、動脈粥狀硬化、心肌缺血
  - 肺部：慢性阻塞性肺病、氣喘、間質性肺病、類肉瘤病
  - 肝腎與其他：肝硬化、腎功能不全、自體免疫性肝炎、胰臟炎、牙周炎
- **藥物交互作用**：資料庫共記錄 105 筆，列出的前幾項包含 Calcitriol、Pantoprazole、Glimepiride、Mesalazine、Doxycycline、Metformin、Omeprazole、Prednisone、Amphotericin B 等，但交互作用嚴重度均為未知，臨床使用時仍須個別評估。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Ribavirin 單獨使用幾乎沒有直接的抗 HBV 活性，現有最直接的 B 型肝炎 Phase 3 試驗（PARC）也未顯示明確的額外效益。
- 目前 B 型肝炎證據偏少，多數支持證據來自 C 型肝炎；且 B 型肝炎已有成熟的核苷類似物等標準治療，再利用的臨床需求與優勢不明。
- 圖譜中的潛在禁忌（貧血、心血管疾病、肝硬化等）與 B 型肝炎族群重疊，安全性顧慮需要認真看待。

**若要推進需要：**
- 完整的作用機轉資料，釐清 Ribavirin 在 HBV 的免疫調節作用。
- 取得 NCT03759782 的結果，以及 NCT00114361 的完整分析，並納入系統性回顧。
- 設計對照試驗，驗證在核苷類似物或干擾素基礎上加入 Ribavirin 的實際效益。
- 提出針對貧血、心血管風險與血液學監測的安全性計畫。
- 評估在現行 B 型肝炎治療指引下的臨床定位與必要性。

---

### 其他預測適應症的簡要說明

其餘排名預測（肝肺症候群、早發性家族性非肝硬化門脈高壓、特發性銅相關肝硬化、肝門脈硬化症、原發性門靜脈血栓、IgG4 相關疾病等）幾乎只有模型預測，缺乏臨床試驗與機轉依據，建議均為 Hold。
肝性卟啉症的文獻顯示，卟啉症（porphyria cutanea tarda）與 C 型肝炎有關，且曾在 PEG-IFN 加 Ribavirin 治療期間出現，較像是疾病關聯或藥物不良反應，並非治療效益的證據。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「速威干軟膠囊100毫克等」列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

