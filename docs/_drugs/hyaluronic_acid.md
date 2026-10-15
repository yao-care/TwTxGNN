---
layout: default
title: Hyaluronic Acid
parent: 高證據等級 (L1-L2)
nav_order: 135
evidence_level: L2
indication_count: 10
---

# Hyaluronic Acid
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

# Hyaluronic acid：從（原適應症資料缺漏）到乾眼症

## 一句話總結

Hyaluronic acid（玻尿酸）是一種天然的葡萄糖胺聚醣，具保水與潤滑特性。台灣許可證資料中未取得其原適應症。
TxGNN 模型預測它可能對**乾眼症 (Dry Eye Syndrome)** 有效，目前有 **9 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含 1 個已完成的 Phase 3 隨機對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告彙整的資料中未提供 |
| 預測新適應症 | 乾眼症 (Dry Eye Syndrome) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2（有 1 個已完成的 Phase 3 RCT，另有多篇統合分析與 RCT 文獻） |
| 台灣上市 | 未上市 |
| 許可證數 | 11 張（有效單方 0／有效複方 1／已註銷 10） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠 MOA 欄位無資料）。以下根據一般藥理知識說明：玻尿酸是具吸水性與黏彈性的葡萄糖胺聚醣，可在眼表面保留水分、穩定淚膜，並可能透過 CD44 結合促進角膜上皮修復。

這些特性與乾眼症的病理（淚膜不穩、眼表面潤滑不足）直接對應，因此含玻尿酸的人工淚液已廣泛作為乾眼症的治療與對照組。機轉上的合理性，加上有安慰劑對照的 Phase 3 試驗與多篇統合分析，使這個預測的可信度相對高。

其他預測適應症的證據強度不一：Sjögren 症候群（主要是其乾眼症狀，屬症狀緩解而非治療自體免疫疾病）有 L2 等級的間接證據；異位性皮膚炎的臨床證據來自多成分乳霜，無法分離玻尿酸本身的貢獻；乾皮症以外的乾癬、類乾癬、苔蘚樣糠疹、糖尿病視網膜病變、淚腺脫垂等多為動物實驗、載體研究或僅有模型預測，建議暫緩。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00599716](https://clinicaltrials.gov/study/NCT00599716) | Phase 3 | 完成 | 300 | 多中心、隨機、雙盲，比較含玻尿酸鈉的 Vismed 與不含活性成分的載體滴眼液，用於乾眼症 |
| [NCT06478134](https://clinicaltrials.gov/study/NCT06478134) | Phase 2/3 | 完成 | 124 | 多成分人工淚液 TriMix 對比以玻尿酸為基底的對照淚液（雙盲 RCT） |
| [NCT06122428](https://clinicaltrials.gov/study/NCT06122428) | N/A | 完成 | 16 | 回溯性研究，評估核黃素強化玻尿酸滴眼液 (HAr 0.1%) 對乾眼症的效果 |
| [NCT05823961](https://clinicaltrials.gov/study/NCT05823961) | N/A | 完成 | 80 | 交聯玻尿酸滴眼液的上市後臨床追蹤，評估淚液異常與乾眼症狀的表現與安全性 |
| [NCT03074344](https://clinicaltrials.gov/study/NCT03074344) | N/A | 完成 | 40 | 交聯玻尿酸加輔酶 Q10 滴眼液用於輕中度乾眼症（隨機、單盲） |
| [NCT07722650](https://clinicaltrials.gov/study/NCT07722650) | N/A | 完成 | 120 | Systane Complete 每日兩次對比含海藻糖與玻尿酸的 Thealoz Duo 每日四次（非劣性 RCT）；玻尿酸貢獻與其他成分混合 |
| [NCT07089511](https://clinicaltrials.gov/study/NCT07089511) | N/A | 完成 | 101 | 臍帶血乏血小板血漿滴眼液用於乾眼症；玻尿酸可能為對照，角色不明 |
| [NCT04673643](https://clinicaltrials.gov/study/NCT04673643) | Phase 2 | 未知 | 128 | 耳迷走神經刺激治療乾眼症；玻尿酸可能僅為背景治療 |
| [NCT06544447](https://clinicaltrials.gov/study/NCT06544447) | Phase 1/2 | 未知 | 135 | 耳迷走神經刺激治療合併瞼板腺功能障礙的乾眼症；玻尿酸可能僅為背景治療 |

另有 1 個玻尿酸凝膠用於下眼瞼退縮的 Phase 4 試驗（NCT01838252），已撤回、無受試者，與乾眼症無關，未列入上表。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39260878](https://pubmed.ncbi.nlm.nih.gov/39260878/) | 2024 | RCT | BMJ | 以 0.1% 玻尿酸鈉為對照，評估大笑運動對乾眼症眼表不適的非劣性 |
| [38895674](https://pubmed.ncbi.nlm.nih.gov/38895674/) | 2024 | 統合分析 | Int J Ophthalmol | 比較不同濃度玻尿酸滴眼液治療乾眼症的效果 |
| [33804439](https://pubmed.ncbi.nlm.nih.gov/33804439/) | 2021 | 統合分析 | Int J Environ Res Public Health | 比較玻尿酸與非玻尿酸滴眼液（生理食鹽水、一般人工淚液）治療乾眼症的療效 |
| [37162564](https://pubmed.ncbi.nlm.nih.gov/37162564/) | 2023 | 統合分析 | Graefes Arch Clin Exp Ophthalmol | 比較局部 diquafosol 與玻尿酸治療乾眼症的 RCT 統合分析 |
| [37682142](https://pubmed.ncbi.nlm.nih.gov/37682142/) | 2023 | RCT | Medicine | 比較 0.15% 玻尿酸、0.05% 環孢素 A 與 3% diquafosol 對大學生中重度乾眼症的療效 |
| [35514082](https://pubmed.ncbi.nlm.nih.gov/35514082/) | 2022 | Review | Acta Ophthalmol | 評估含玻尿酸人工淚液治療乾眼症的安全性與療效 |
| [37042308](https://pubmed.ncbi.nlm.nih.gov/37042308/) | 2024 | Review | Acta Ophthalmol | 彙整與玻尿酸直接比較過的單一成分滴眼液；玻尿酸長期被視為安全有效的乾眼症治療 |
| [31373862](https://pubmed.ncbi.nlm.nih.gov/31373862/) | 2019 | Review | J Ocul Pharmacol Ther | 交聯玻尿酸作為淚液替代品；黏度與淚膜穩定性優於 PVA、HPMC、CMC 等 |
| [37117131](https://pubmed.ncbi.nlm.nih.gov/37117131/) | 2023 | 臨床研究 | Contact Lens & Anterior Eye | 含海藻糖與玻尿酸的人工淚液，用於不同年齡層女性乾眼症的 3 個月療效 |
| [28557655](https://pubmed.ncbi.nlm.nih.gov/28557655/) | 2017 | Cohort | J Ocul Pharmacol Ther | 玻尿酸與交聯玻尿酸滴眼液對 Sjögren 相關乾眼症淚膜穩定性的比較 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Hyaluronic Acid 的不重複許可證共 **11 張**：有效單方 0 張、有效複方 1 張、已註銷 10 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第027112號 | 視舒坦玻尿酸人工淚液點眼液 | POLYETHYLENE GLYCOL 400、PROPYLENE GLYCOL、HYALURONATE SODIUM… | 無菌眼用液劑 | 暫時緩解因眼睛乾澀所引起的灼熱感及刺激感。 |

<details><summary><strong>已註銷</strong>（10 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第012221號</td><td>喜隆玻璃體替代物</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第013166號</td><td>喜隆玻璃體替代物</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第017184號</td><td>安衛視玻璃體替代物</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第018213號</td><td>喜隆玻璃體替代物</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>2004/12/16</td></tr><tr><td>衛署藥輸字第018759號</td><td>人工玻璃體</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )、CHONDROITIN…</td><td>1996/09/13</td></tr><tr><td>衛署藥輸字第019803號</td><td>泛美視黃色喜隆注射劑</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>2004/12/16</td></tr><tr><td>衛署藥輸字第019910號</td><td>雅爾眼內注入液</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>1997/11/03</td></tr><tr><td>衛署藥輸字第020069號</td><td>泛美視超黏喜隆注射劑</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>1997/11/28</td></tr><tr><td>衛署藥輸字第021167號</td><td>博微視人工玻璃體</td><td>HYALURONATE SODIUM ( EQ TO SODIUM HYALURONATE )</td><td>1997/07/02</td></tr><tr><td>衛署藥輸字第021345號</td><td>人工玻璃體</td><td>CHONDROITIN SULFATE、HYALURONATE SODIUM ( EQ TO SODIUM HYALUR…</td><td>1997/07/11</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**：青光眼（來自 TxGNN 知識圖譜的藥物—疾病禁忌關聯，非仿單文字，使用時需臨床評估）
- **藥物交互作用**：資料庫共查得 2 筆，皆為中度（Moderate）：
  - Cetylpyridinium（外用）
  - Benzalkonium（外用）

  兩者皆為常見的防腐劑或抗菌成分，若同時使用含此類成分的產品，需留意配伍。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 乾眼症有已完成的 Phase 3 雙盲、載體對照 RCT，並有多篇統合分析與 RCT 支持，機轉也合理。主要限制是台灣目前無上市許可證，且仿單層級的安全性資料尚未取得。
- 其他預測適應症（Sjögren 症候群的乾眼症狀屬輔助緩解，其餘多為間接或無證據）不建議作為優先方向。

**若要推進需要：**
- 取得 TFDA 仿單的警語與禁忌症，完成安全性篩選
- 補充藥物作用機轉（MOA）的正式資料
- 確認台灣的法規途徑與劑型（眼用製劑或醫療器材分類）
- 針對 Phase 3 試驗與統合分析做證據品質審視，並釐清不同分子量、濃度與交聯型式的差異
- 若評估 Sjögren 症候群，需明確界定為乾眼症狀緩解，而非疾病修飾治療

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「目前在台灣無任何藥品許可證登記」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

