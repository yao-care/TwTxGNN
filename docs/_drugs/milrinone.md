---
layout: default
title: Milrinone
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Milrinone
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

# Milrinone：從充血性心衰竭到禿髮 (Alopecia)

## 一句話總結

Milrinone 是一種靜脈注射用的 PDE3 抑制劑，原本用於充血性心衰竭的短期治療。
TxGNN 模型預測它可能對**禿髮 (Alopecia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，證據僅來自模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 充血性心衰竭的短期療法 |
| 預測新適應症 | 禿髮 (Alopecia) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 3 張（有效單方 2／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

<!-- review:begin milrinone-alopecia-rereview-result-2026-10-03 -->

> **重審結果（2026-10-03）**：**撤回**（證據等級 L5 不變）。本筆重審的對象是 2026-10-03 版報告；當時唯一的理由「minoxidil 是 PDE 抑制劑」不成立（仿單與 MeSH 都把 minoxidil 列為直接作用的血管擴張劑），拿掉後沒有其他支撐；PubMed 查 milrinone 與毛髮或禿髮的研究為零筆，ClinicalTrials.gov 也查無登錄試驗，因此撤回禿髮症等三筆推論。另一個 PDE3 抑制劑 cilostazol 有促進毛髮生長的前臨床研究（[PMID 29678305](https://pubmed.ncbi.nlm.nih.gov/29678305/)），但藥物不同，不能當作 milrinone 的證據。2026-10-15 重生的報告改以 cAMP 訊號與血管擴張改善毛囊灌流作推測，同樣沒有 milrinone 本身的證據，且以 L5、Hold 呈現，與重審結論一致。依據：[PubMed：The effect of cilostazol, a phosphodiesterase 3 (PDE3) inhibitor, on human hair growth with the dual promoting mechanisms（PMID 29678305）](https://pubmed.ncbi.nlm.nih.gov/29678305/)。

<!-- review:end milrinone-alopecia-rereview-result-2026-10-03 -->

## 為什麼這個預測合理？

Milrinone 透過抑制 PDE3（磷酸二酯酶 3）提高細胞內 cAMP，在心肌產生正性肌力作用，在血管平滑肌產生血管擴張作用。這種「強心加擴血管」的特性，是它用於心衰竭的基礎。藥理資料也顯示它可作用於 PDE2A、PDE3A、PDE3B 與 PDE5A 等標的。

心衰竭與禿髮在疾病性質上差異很大。目前能想到的關聯只有兩點：
- cAMP 訊號與毛囊生物學可能有關。
- 血管擴張可能改善毛囊周圍的血流灌注。

這兩點都只是推測，沒有直接證據。這項預測目前只來自 TxGNN 的模型分數，並未得到機轉或臨床資料的佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Milrinone 的不重複許可證共 **3 張**：有效單方 2 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第021128號 | 哌明克注射劑 | 注射劑 | 賽諾菲股份有限公司 | 2030/06/08 | 充血性心衰竭的短期療法 |
| 衛部藥製字第058150號 | 米力心注射劑0.2毫克/毫升 | 注射劑 | 歐舒邁克有限公司 | 2028/12/12 | EasyMilrinone injection 適用於充血性心衰竭的短期療法。病人接受milrinone治療，應給予適當心電圖設備嚴密監控。對於可能發生的心臟事件，如危及生命的室性… |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第020939號</td><td>/明克注射劑</td><td>MILRINONE</td><td>1996/03/15</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜顯示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物—疾病關聯，並非仿單內容）：腎臟病、心肌梗塞、冠狀動脈血栓、低血壓、心臟傳導疾病、肥厚性心肌病變（含家族性）、肺動脈瓣狹窄、猝死性心臟驟停、血紅素病變、輸尿管積膿。
- **藥物交互作用**（共 9 筆，其中中度交互作用 5 筆）：Amifostine、Diatrizoate、Anagrelide、Ozanimod、Procarbazine。
- **使用情境**：現行許可證劑型僅有注射劑，且仿單要求使用時須有心電圖監測，並備有處理危及生命之室性心律失常的設備。這些限制與禿髮這類非急重症的治療情境明顯不符。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測只有模型分數支持（99.91%），沒有臨床試驗、文獻或明確的機轉證據，證據等級為 L5。
- 現有劑型是需要監測的靜脈注射劑，風險高，與禿髮的治療需求不匹配。

**若要推進需要：**
- 補充 PDE3 抑制或 cAMP 訊號與毛囊生長或禿髮之間的機轉與前臨床研究。
- 評估是否有適合的外用或局部劑型，並確認其全身暴露與安全性。
- 釐清心血管風險（心律失常、低血壓）在此族群的效益風險比。
- 在取得前臨床證據之前，不建議進入臨床試驗規劃。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「PDE 抑制劑（如 minoxidil）已知可促進毛髮生長」 | 報告重生後已無此錯誤（2026-10-15：新報告未再把 minoxidil 稱為 PDE 抑制劑；原為加註） | [DailyMed：Minoxidil Tablets USP 仿單（American Health Packaging），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0b4fc036-9497-442b-b629-c4b386932789)；[NLM MeSH：Minoxidil（D008914）](https://meshb.nlm.nih.gov/record/ui?ui=D008914)；[emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc) |
| 2026-10-03 | 禿髮症／毛髮稀疏症預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [DailyMed：Minoxidil Tablets USP 仿單（American Health Packaging），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0b4fc036-9497-442b-b629-c4b386932789) |
| 2026-10-03 | 禿髮症／毛髮稀疏症預測重審結果 | 重審：撤回，證據等級 L5 不變（2026-10-16 修訂，前版保留於紀錄） | [PubMed：The effect of cilostazol, a phosphodiesterase 3 (PDE3) inhibitor, on human hair growth with the dual promoting mechanisms（PMID 29678305）](https://pubmed.ncbi.nlm.nih.gov/29678305/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

