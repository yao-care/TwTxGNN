---
layout: default
title: Guaiacol
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 1
monitor_inn: "guaiacol"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-29
description: "Guaiacol：預測新適應症為鼻腔疾病 (Nasal Cavity Disease)（證據等級 L5）。原適應症：袪痰（guaiacol 本身的許可證均已註銷）"
---

# Guaiacol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Guaiacol：從祛痰止咳到鼻腔疾病
{: .text-alpha }

## 一句話總結

Guaiacol（癒創木酚）原本用於祛痰；台灣主成分為 guaiacol 本身的許可證都已註銷。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個預測，僅屬模型推論。

<!-- review:begin guaiacol-guaifenesin-summary-2026-11-25 -->

> **查核更正（2026-11-25）**：原寫「Guaiacol（癒創木酚，台灣常見品名如清痰片）原本用於祛痰，也是多種感冒、咳嗽複方的成分之一。」。清痰片（內衛藥製字第001007號「清痰片」等，主成分 GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)，即 guaifenesin（甘油愈創木酯））與常見的感冒、咳嗽複方所含的都是 guaifenesin，是另一個藥；主成分為 guaiacol 本身的許可證（原料藥、注射劑、口含錠）在 TFDA 資料集中都已註銷。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end guaiacol-guaifenesin-summary-2026-11-25 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 袪痰（guaiacol 本身的許可證核准適應症；這些許可證均已註銷） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 0.9951 |
| 證據等級 | L5 |
| 台灣上市 | 未上市（已註銷許可證 11 張／共 11 張） |
| 許可證數 | 11 張（有效單方 0／有效複方 0／已註銷 11） |
| 建議決策 | Hold |

<!-- review:begin guaiacol-original-indication-2026-11-25 -->

> **查核更正（2026-11-25）**：原寫「原適應症／袪痰（支氣管炎、感冒、急、慢性喉頭炎、氣管炎等引起之喀痰）」。原文括號內的適應症取自內衛藥製字第001007號「清痰片」等，主成分 GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)，即 guaifenesin（甘油愈創木酯），是另一個藥；guaiacol 本身的許可證核准「袪痰劑」「袪痰、潤喉」，都已註銷。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end guaiacol-original-indication-2026-11-25 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Guaiacol 是祛痰劑，單方製劑核准用於祛痰；它也常見於感冒咳嗽複方。

複方許可證的核准適應症中，包含鼻塞、流鼻水、打噴嚏等鼻部症狀。不過這些症狀的緩解，可能來自複方中的其他成分，不能直接視為 Guaiacol 單一成分對鼻腔疾病有效。因此這只是間接的背景關聯，並非療效證據。

<!-- review:begin guaiacol-why-combo-nasal-2026-11-25 -->

> **查核加註（2026-11-25）**：上兩段所說的感冒咳嗽複方、以及核准適應症含鼻塞、流鼻水、打噴嚏的複方，所含的是 guaifenesin（甘油愈創木酯，另一個藥），不是 guaiacol；主成分為 guaiacol 本身的複方都已註銷，適應症是咳嗽、喉痛、口臭與喀痰。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end guaiacol-why-combo-nasal-2026-11-25 -->

TxGNN 模型（深度學習）給出的高分（0.9951）可能反映模型從相關疾病之間學到的相似性，並非生物學證據，沒有任何臨床試驗或文獻佐證，應視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-11-24），主成分含 Guaiacol 的不重複許可證共 **11 張**：有效單方 0 張、有效複方 0 張、已註銷 11 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（11 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛成製字第000783號</td><td>癒創木補爾維他命液</td><td>NIACINAMIDE (NICOTINAMIDE)、THIAMINE HCL (BIOTAMINE)、NYLON (P…</td><td>2017/02/09</td></tr><tr><td>內衛藥輸字第001400號</td><td>果舒</td><td>GUAIACOL</td><td>1986/10/18</td></tr><tr><td>衛署成製字第004078號</td><td>金達錠</td><td>GUAIACOL、TERPINEOL OIL、L-MENTHOL、EUCALYPTUS OIL (OLEUM EUCAL…</td><td>1990/10/06</td></tr><tr><td>衛署成製字第008302號</td><td>金達錠</td><td>GUAIACOL、TERPINEOL OIL、L-MENTHOL、EUCALYPTUS OIL (OLEUM EUCAL…</td><td>2013/10/14</td></tr><tr><td>衛署藥製字第000668號</td><td>複方帕勒托液</td><td>MALT EXT、CREOSOTE、MANGANESE SULFATE MONOHYDRATE、HEMATIC HYPO…</td><td>1998/07/06</td></tr><tr><td>衛署藥製字第021082號</td><td>"明大" 美好口含錠</td><td>EUCALYPTOL (CINEOLE)、MENTHOL、TERPINEOL、GUAIACOL</td><td>2023/07/12</td></tr><tr><td>衛署藥輸字第000317號</td><td>癒創木酚</td><td>GUAIACOL</td><td>1997/12/05</td></tr><tr><td>衛署藥輸字第005017號</td><td>癒創木酚</td><td>GUAIACOL</td><td>1993/12/15</td></tr><tr><td>衛署藥輸字第017828號</td><td>華達錠</td><td>GUAIACOL、THYMOL、TERPINEOL、MENTHOL、EUCALYPTOL (CINEOLE)</td><td>1991/04/13</td></tr><tr><td>衛署藥輸字第018387號</td><td>樺達錠</td><td>GUAIACOL、EUCALYPTOL (CINEOLE)、MENTHOL、TERPINEOL、THYMOL</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第020163號</td><td>癒創木酚</td><td>GUAIACOL</td><td>2010/09/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌關聯**（來自知識圖譜的藥物－疾病關係，並非仿單文字）：高血壓、癲癇、腎臟病、胰臟炎、肝病、膽囊疾病、腎上腺皮質功能不全、甲狀腺功能低下、消化性潰瘍、發炎性腸道疾病、糖尿病、糖尿病酮酸中毒、良性攝護腺增生、無尿、橫紋肌溶解、高鈣血症、冠狀動脈疾病、心肌梗塞、血紅素病變等。這些需以原廠仿單為準，不能直接當作正式禁忌。
- **藥物交互作用**：本次資料查無相關紀錄。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
預測新適應症沒有任何直接研究支持，證據等級為 L5，僅有模型分數。台灣核准的鼻部症狀適應症都來自複方，無法代表 Guaiacol 單一成分的效果。

<!-- review:begin guaiacol-decision-premise-2026-11-25 -->

> **查核加註（2026-11-25）**：這裡所說核准鼻部症狀的複方，所含的是 guaifenesin（另一個藥），不是 guaiacol；台灣主成分為 guaiacol 本身的許可證都已註銷。決策與證據等級未改。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end guaiacol-decision-premise-2026-11-25 -->

**若要推進需要：**
- 補充 Guaiacol 的作用機轉資料，評估與鼻腔疾病的機轉關聯
- 界定具體的鼻腔疾病目標（如鼻炎、鼻竇炎、鼻充血）
- 文獻回顧與臨床前或小型探索性研究，確認單一成分是否有貢獻
- 確認劑型與給藥途徑是否適合鼻腔疾病（目前路徑相容性尚待評估）
- 整理完整的安全性與禁忌資料，並對照原廠仿單

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-11-25 | 「台灣常見品名如清痰片」「多種感冒、咳嗽複方的成分」其實是 guaifenesin | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-11-25 | 「原適應症」括號內文字取自 guaifenesin 許可證 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-11-25 | description 的原適應症取自 guaifenesin 許可證 | 頁面描述（description）更正：原「原適應症：袪痰（支氣管炎、感冒、急、慢性喉頭炎、氣管炎等引起之喀痰）」→「原適應症：袪痰（guaiacol 本身的許可證均已註銷）」 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-11-25 | 推論所引的感冒複方（鼻塞、流鼻水）主成分是 guaifenesin | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-11-25 | 決策理由所說的鼻部症狀複方是 guaifenesin 複方 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

