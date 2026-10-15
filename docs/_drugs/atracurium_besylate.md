---
layout: default
title: Atracurium Besylate
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Atracurium Besylate
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

# Atracurium besylate：從手術麻醉輔助（神經肌肉阻斷）到子癇前症

## 一句話總結

Atracurium besylate 是一種非去極化神經肌肉阻斷劑，原本用於全身麻醉與加護病房的骨骼肌鬆弛。
TxGNN 模型預測它可能對**子癇前症 (Preeclampsia)** 有效，但目前**沒有任何臨床試驗與文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高選擇性及競爭性的非去極化神經肌肉阻斷劑，可作為手術全身麻醉劑之輔助劑或加護病房使用，用以鬆弛骨骼肌，幫助氣管插管及與人工呼吸器的協調 |
| 預測新適應症 | 子癇前症 (Preeclampsia) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 5 張（有效單方 1／有效複方 0／已註銷 4） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理分類，Atracurium 是作用於神經肌肉接合處菸鹼型乙醯膽鹼受體的非去極化神經肌肉阻斷劑，主要用於麻醉時的骨骼肌鬆弛。

目前**沒有已知機轉**能把這類藥物與子癇前症的病理（胎盤與血管內皮功能異常）連結起來。肌肉鬆弛劑在子癇前症的相關性，僅限於分娩時的麻醉處置，並不是治療疾病本身。這項預測完全來自知識圖譜的模型分數，缺乏藥理學或臨床支持，應謹慎看待。

其他排名較前的預測（如子癇前症亞型、馬尾症候群、眼瞼痙攣、偏頭痛、腸躁症等）同樣沒有任何臨床試驗或文獻佐證。其中眼瞼痙攣在機轉上較可想像（涉及不自主肌肉收縮），但全身性使用 atracurium 並不實際且不安全。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Atracurium Besylate 的不重複許可證共 **5 張**：有效單方 1 張、有效複方 0 張、已註銷 4 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第042879號 | 〝健亞〞健舒注射液１０公絲/公撮（艾翠克瑞） | 注射劑 | 健亞生物科技股份有限公司 | 2029/04/02 | 本藥乃一高選擇性及競爭性的非去極化神經肌肉阻斷劑。可作為手術全身麻醉或加護病房鎮靜的輔助劑、以鬆弛骨骼肌、幫助氣管插管與人工吸器的協調。 |

<details><summary><strong>已註銷</strong>（4 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第013148號</td><td>妥開利注射劑</td><td>ATRACURIUM BESYLATE</td><td>2025/06/09</td></tr><tr><td>衛署藥輸字第022066號</td><td>爾促開利注射劑１０公絲／公撮〝岱比博〞</td><td>ATRACURIUM BESYLATE</td><td>2010/10/18</td></tr><tr><td>衛署藥輸字第023136號</td><td>亞庫凱林注射劑５０公絲/小瓶</td><td>ATRACURIUM BESYLATE</td><td>2013/01/03</td></tr><tr><td>衛署藥輸字第023147號</td><td>亞庫凱林注射劑１０公絲/公撮（多次劑量）</td><td>ATRACURIUM BESYLATE</td><td>2013/01/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數（證據等級 L5），沒有臨床試驗、文獻或可說明的作用機轉支持。
- 藥物的藥理作用（神經肌肉阻斷）與子癇前症的病理無明確關聯，且全身性神經肌肉阻斷劑需在具備呼吸支持的環境使用，風險高。

**若要推進需要：**
- 補齊作用機轉資料，並釐清是否存在任何可成立的機轉假說
- 進行系統性文獻檢索，確認是否有前臨床或臨床研究
- 在有可信機轉假說之前，不建議啟動臨床開發
- 若要探索其他預測適應症，可優先評估機轉較合理者，但仍須先確認給藥途徑與安全性是否可行

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測原文未改寫；證據等級與決策只依重審結果（降級或撤回）更新，原值列在下表。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「不引起組織胺釋放相關的血壓波動」 | 加註 | [DailyMed：Atracurium Besylate Injection USP 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=de1c2dcd-295b-47ce-b7a1-a8be59939a54) |
| 2026-10-03 | 子癇前症預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [DailyMed：Atracurium Besylate Injection USP 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=de1c2dcd-295b-47ce-b7a1-a8be59939a54) |
| 2026-10-03 | 許可證表中三張是 cisatracurium 製劑 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 子癇前症預測重審結果 | 重審：降級，證據等級 L3→L5；快速總覽「證據等級」：原「證據等級／L3 (觀察性研究/文獻支持)」→「證據等級／L5（2026-10-03 重審降級）」；快速總覽「建議決策」：原「建議決策／Consider」→「建議決策／Hold（2026-10-03 重審調整）」；結論「決策」：原「**決策：Consider**」→「**決策：Hold**（2026-10-03 重審調整）」 | [PubMed：Use of atracurium in pre-eclamptic patients（PMID 3778800）](https://pubmed.ncbi.nlm.nih.gov/3778800/)；[PubMed：Clinical pharmacokinetics of neuromuscular relaxants in pregnancy（PMID 9646009）](https://pubmed.ncbi.nlm.nih.gov/9646009/)；[PubMed：[Remifentanil bolus for cesarean section in high-risk patients: study of 12 cases]（PMID 18383970）](https://pubmed.ncbi.nlm.nih.gov/18383970/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

