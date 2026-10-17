---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-16
description: "Dorzolamide：預測新適應症為原發性遺傳性青光眼 (Primary Hereditary Glaucoma)（證據等級 L5）。原適應症：碳酸酐脢抑制劑，用於高眼壓和開角型青光眼患者，以降低眼內壓"
monitor_inn: "Dorzolamide"
predicted_indications: ["primary hereditary glaucoma", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "congestive heart failure", "acute pulmonary heart disease", "respiratory failure"]
---

# Dorzolamide
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

# Dorzolamide：從高眼壓症與廣角性青光眼到原發性遺傳性青光眼

## 一句話總結

Dorzolamide（多佐胺）是局部使用的碳酸酐酶抑制劑，原本用於高眼壓症與開角型（廣角性）青光眼，以降低眼內壓。
TxGNN 模型預測的第一名新適應症為**原發性遺傳性青光眼 (Primary Hereditary Glaucoma)**，但針對此疾病目前**沒有臨床試驗與文獻**支持，僅有模型預測。
另外，預測清單中的「開角型青光眼」雖有大量證據（多個 Phase 3/4 試驗與系統性回顧），但它就是藥物已核准的適應症，不屬於真正的新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 碳酸酐脢抑制劑，用於高眼壓和開角型青光眼患者，以降低眼內壓 |
| 預測新適應症 | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 12 張（有效單方 6／有效複方 4／已註銷 2） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。不過依藥理資料，dorzolamide 作用於碳酸酐酶（CA1、CA12、CA14、CA7 等標的），一般認為它抑制睫狀體中的碳酸酐酶 II，減少房水生成，進而降低眼內壓。

原發性遺傳性青光眼同屬青光眼，治療核心同樣是控制眼內壓，因此在機轉上具有生物學上的合理性。不過這項推論僅建立在 TxGNN 預測與一般機轉推理上，尚無任何針對此疾病的臨床試驗或文獻可驗證。

此外，預測清單中排名較前的毛髮疾患（如頭皮單純性毛髮稀少、先天性毛髮稀少伴粟丘疹、禿髮、圓禿）與心肺疾病（充血性心衰竭、急性肺心病、呼吸衰竭），機轉上缺乏合理連結，多半可能是知識圖譜的假象，不建議作為再利用方向。

## 臨床試驗證據

目前無相關臨床試驗登記（針對原發性遺傳性青光眼）。

供參考：預測清單中的「開角型青光眼」有多項已完成的 Phase 3/4 試驗，但這是藥物既有的核准適應症，只能視為對藥物降眼壓療效的驗證，不能視為新適應症的證據。代表性試驗如下：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00878917](https://clinicaltrials.gov/study/NCT00878917) | Phase 3 | 完成 | 32 | 雙盲交叉等效性試驗，比較 dorzolamide 2% 與參考製劑在開角型青光眼或高眼壓症的降眼壓效果 |
| [NCT00108017](https://clinicaltrials.gov/study/NCT00108017) | Phase 3 | 完成 | 330 | 評估 dorzolamide/timolol 複方 24 小時降眼壓效果 |
| [NCT00675207](https://clinicaltrials.gov/study/NCT00675207) | Phase 4 | 完成 | 120 | 比較 brimonidine、dorzolamide、brinzolamide 作為前列腺素類似物的輔助治療 |
| [NCT02325518](https://clinicaltrials.gov/study/NCT02325518) | Phase 4 | 完成 | 218 | brinzolamide/timolol 複方對比 dorzolamide/timolol 複方的降眼壓療效 |
| [NCT00822081](https://clinicaltrials.gov/study/NCT00822081) | Phase 4 | 完成 | 140 | 比較 brimonidine/timolol 與 dorzolamide/timolol 複方 |
| [NCT00991822](https://clinicaltrials.gov/study/NCT00991822) | Phase 2/3 | 完成 | 160 | 比較 dorzolamide 與 timolol 對視神經盤血流的影響 |
| [NCT00273455](https://clinicaltrials.gov/study/NCT00273455) | Phase 4 | 完成 | 34 | 比較 Lumigan 與 Cosopt（dorzolamide/timolol）的眼壓效果與安全性 |
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | 完成 | 37 | 評估 latanoprost 與 dorzolamide 在兒童青光眼的降眼壓效果 |

## 文獻證據

針對原發性遺傳性青光眼目前無相關文獻。以下為青光眼（開角型）領域的代表性文獻，僅作為藥物既有適應症的背景參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | 統合分析 | Ophthalmology | 比較原發性開角型青光眼一線藥物的相對療效並排序 |
| [17943780](https://pubmed.ncbi.nlm.nih.gov/17943780/) | 2007 | 統合分析 | Cochrane Database Syst Rev | 原發性開角型青光眼與高眼壓症的藥物治療回顧 |
| [39677168](https://pubmed.ncbi.nlm.nih.gov/39677168/) | 2024 | RCT | Cureus | 印度族群中 brinzolamide/timolol 與 dorzolamide/timolol 複方的 Phase 3 比較 |
| [19365194](https://pubmed.ncbi.nlm.nih.gov/19365194/) | 2009 | RCT | J Glaucoma | brinzolamide/timolol 與 dorzolamide/timolol 複方的降眼壓療效與安全性比較 |
| [9143858](https://pubmed.ncbi.nlm.nih.gov/9143858/) | 1997 | Review | Drugs & Aging | dorzolamide 2% 每日三次可使尖峰眼壓下降約 4–6 mmHg |
| [11200308](https://pubmed.ncbi.nlm.nih.gov/11200308/) | 2000 | Review | Drugs & Aging | dorzolamide 與 timolol 機轉不同、效果可相加 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dorzolamide 的不重複許可證共 **12 張**：有效單方 6 張、有效複方 4 張、已註銷 2 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（6 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第048554號 | 多舒明點眼液2% | 點眼液劑 | 麥迪森醫藥股份有限公司 | 2027/01/25 | 高眼壓症，廣角性青光眼。 |
| 衛署藥輸字第022107號 | 舒露瞳點眼液劑２％ | 點眼液劑 | 台灣參天製藥股份有限公司 | 2028/03/25 | 高眼壓症、廣角性青光眼。 |
| 衛部藥製字第058555號 | 得舒適點眼液劑2% | 點眼液劑 | 健亞生物科技股份有限公司 | 2029/12/11 | 高眼壓症，廣角性青光眼。 |
| 衛部藥輸字第026845號 | 鹽酸多佐胺 | 原料藥結晶性粉末 | 裕元興業股份有限公司 | 2031/05/31 | 降眼壓用藥。 |
| 衛部藥輸字第027237號 | 鹽酸多佐胺 | （粉） | 新雙隆生技股份有限公司 | 2027/08/15 | 碳酸酐脢抑制劑，用於高眼壓和開角型青光眼患者，以降低眼內壓 |
| 衛部藥輸字第027552號 | 鹽酸多佐胺 | （粉） | 新雙隆生技股份有限公司 | 2028/12/06 | 碳酸酐脢抑制劑，用於高眼壓和開角型青光眼患者，以降低眼內壓 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第048925號 | 可多舒明點眼液 | DORZOLAMIDE HYDROCHLORIDE、TIMOLOL MALEATE | 點眼液劑 | 高眼壓症、開放性青光眼、假性剝離性青光眼所造成之眼內壓升高。 |
| 衛署藥輸字第023337號 | 康舒目點眼液劑 | TIMOLOL MALEATE、DORZOLAMIDE HYDROCHLORIDE | 點眼液劑 | 高眼壓症、開放性青光眼、假性剝離性青光眼所造成之眼內壓升高。 |
| 衛署藥輸字第025410號 | 康舒目(單支裝) 點眼液劑 | TIMOLOL MALEATE、DORZOLAMIDE HYDROCHLORIDE | 點眼液劑 | 高眼壓症、開放性青光眼、假性剝離性青光眼所造成之眼內壓升高。 |
| 衛部藥製字第060271號 | 安視眼藥水 | TIMOLOL MALEATE、DORZOLAMIDE HYDROCHLORIDE | 點眼液劑 | 高眼壓症、開放性青光眼、假性剝離性青光眼所造成之眼內壓升高。 |

<details><summary><strong>已註銷</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第026002號</td><td>瞳適得點眼液劑2%</td><td>DORZOLAMIDE HYDROCHLORIDE</td><td>2024/07/01</td></tr><tr><td>衛部藥製字第060252號</td><td>"景德"景舒瞳點眼液劑2%</td><td>DORZOLAMIDE HYDROCHLORIDE</td><td>2026/01/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用／藥理標的**：資料顯示 dorzolamide 作用於碳酸酐酶 1、7、12、14 等標的。
- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜，非仿單內容）：糖尿病、糖尿病酮酸中毒、重症肌無力、神經肌肉接合部疾病、甲狀腺功能亢進、葛瑞夫茲氏病、低血糖、房室傳導阻滯、肺氣腫、支氣管疾病、過敏性休克。這些僅供參考，實際禁忌請以原廠仿單為準。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 針對首要預測「原發性遺傳性青光眼」，目前沒有任何臨床試驗或文獻，僅有 TxGNN 模型分數（證據等級 L5）。
- 預測清單中證據充足的「開角型青光眼」為既有核准適應症，不構成新的再利用機會；其餘預測（毛髮疾患、心肺疾病）機轉上缺乏合理連結。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA）。
- 針對原發性遺傳性青光眼（含兒童／先天性青光眼）進行文獻與試驗檢索，可參考既有的兒童青光眼 Phase 2 試驗（NCT01527682）作為切入點。
- 確認此類病人的眼壓控制需求與給藥途徑（局部點眼）的相容性。
- 評估知識圖譜所列潛在禁忌疾病對目標族群的影響。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

