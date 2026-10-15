---
layout: default
title: Bempedoic Acid
parent: 中證據等級 (L3-L4)
nav_order: 40
evidence_level: L3
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic acid：從高膽固醇血症到同合子家族性高膽固醇血症

## 一句話總結

Bempedoic acid 原本用於治療原發性高膽固醇血症與混合型血脂異常，以降低 LDL-C。
TxGNN 模型的預測排名第一為甲狀腺機能亢進，但該預測缺乏任何臨床試驗或文獻支持。本報告因此以證據最多的預測 **同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 為重點，目前有 **19 篇文獻**（無臨床試驗登記），其中包含 1 篇真實世界世代研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 異合子家族性或非家族性之原發性高膽固醇血症、混合型血脂異常的成人病人，作為飲食輔助治療以降低 LDL-C |
| 預測新適應症 | 同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia)；排名第一的預測為甲狀腺機能亢進 (hyperthyroidism)，證據等級 L5，建議 Hold |
| TxGNN 預測分數 | HoFH：99.48%（甲狀腺機能亢進：99.61%） |
| 證據等級 | L3（HoFH）；其餘預測為 L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 1／有效複方 1／已註銷 0） |
| 建議決策 | Hold（排名第一的預測）；HoFH 為值得進一步研究的方向 |

<!-- review:begin bempedoic-acid-hofh-rereview-result-2026-10-03 -->

> **重審結果（2026-10-03）**：**維持**（證據等級 L3 不變）。本筆重審的對象是 2026-10-03 版報告；當時的理由「非 LDL 受體依賴機制」與仿單不符（仿單：抑制 ACL 後經上調 LDL 受體降低 LDL-C），但 L3 的依據是一篇 HoFH 回溯研究：5 名已用 statin 的患者加上本藥後，LDL-C 平均下降約 33%（[PMID 41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/)），樣本極小、無對照；動物研究中 LDL 受體完全缺失時降幅（29%）明顯小於部分缺失（61%）（[PMID 29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/)）。2026-10-15 重生的報告已改寫為「作用部分依賴 LDL 受體上調、療效取決於殘存受體活性」，與仿單一致，HoFH 證據等級 L3、決策 Hold。依據：[PubMed：Real-world evaluation of bempedoic acid use in patients with homozygous familial hypercholesterolemia（PMID 41274797）](https://pubmed.ncbi.nlm.nih.gov/41274797/)；[PubMed：Bempedoic Acid Lowers Low-Density Lipoprotein Cholesterol and Attenuates Atherosclerosis in Low-Density Lipoprotein Receptor-Deficient (LDLR(+/-) and LDLR(-/-)) Yucatan Miniature Pigs（PMID 29449335）](https://pubmed.ncbi.nlm.nih.gov/29449335/)。
>
> 決策建議另議：重審當時頁面決策為 Go（methodology：強力證據支持），與 L3 不相稱，建議改為 Explore 或 Consider；2026-10-15 重生的報告決策為 Hold（HoFH 列為值得研究的方向），已無此問題。

<!-- review:end bempedoic-acid-hofh-rereview-result-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏經 DrugBank 確認的詳細作用機轉資料。根據已知資訊，bempedoic acid 是一種在肝臟活化的前驅藥，抑制 ATP-citrate lyase（位於 HMG-CoA 還原酶上游），降低肝臟膽固醇合成，並提升 LDL 受體表現，進而降低 LDL-C。

**排名第一的甲狀腺機能亢進：**機轉上沒有已知的直接關聯，預測僅來自知識圖譜推論，沒有臨床試驗或文獻支持。排名前十的其他預測也多屬同樣情況：甲狀腺激素抗性、甲狀腺素過高血症、骨質疏鬆、內分泌腫瘤等缺乏機轉證據，惡性卡他熱與牛傳染性鼻氣管炎是獸醫病毒疾病，很可能是圖譜的假象。巨細胞病毒感染僅有「病毒複製依賴宿主脂質代謝」的推測性連結。

**HoFH：**與原適應症同屬 LDL-C 升高的疾病，方向上最為合理。不過 HoFH 的 LDL 受體功能嚴重受損，而 bempedoic acid 的作用部分依賴 LDL 受體上調，療效可能受限，取決於殘存的受體活性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為 HoFH 預測的代表文獻（共 19 篇，列出最相關者）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | 世代研究 | Journal of Clinical Lipidology | 真實世界評估 bempedoic acid 用於 HoFH 病人的療效與耐受性 |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | 新興降 LDL-C 療法回顧，包含 bempedoic acid 與 inclisiran |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Review | Journal of Clinical Lipidology | 美國國家脂質學會家族性高膽固醇血症專家共識更新 |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atheroscler Thromb | HoFH 治療進展，強調積極降低 LDL-C |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Experimental and Molecular Pathology | HoFH 創新療法與早期診斷、降脂治療的重要性 |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiology in Review | Evinacumab 用於 HoFH，並討論 bempedoic acid 等其他選項 |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | 傳統與新型非 statin 降脂藥物，適用於 statin 不耐受或未達標者 |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Current Cardiology Reports | 難治型與家族性高膽固醇血症超越 statin 與 PCSK9 抑制劑的處置 |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Prev Cardiol | 長期降低 LDL-C 對預防動脈粥狀硬化心血管疾病的重要性 |
| [42761917](https://pubmed.ncbi.nlm.nih.gov/42761917/) | 2026 | Review | Methodist DeBakey Cardiovasc J | 家族性高膽固醇血症的流行病學、遺傳與治療概述 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Bempedoic Acid 的不重複許可證共 **2 張**：有效單方 1 張、有效複方 1 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028817號 | 寧脂德膜衣錠180毫克 | 膜衣錠 | 台灣第一三共股份有限公司 | 2029/11/05 | １、適用於患有異合子家族性或非家族性之原發性高膽固醇血症、或混合型血脂異常的成人病人，作為飲食的輔助治療以降低低密度脂蛋白膽固醇(LDL-C)： ．與statin類藥品併用、或併用… |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第029062號 | 耐脂德膜衣錠 | Bempedoic Acid、EZETIMIBE | 膜衣錠 | 用於患有異合子家族性和非家族性之原發性高膽固醇血症、或混合型血脂異常的成人病人，作為飲食的輔助治療以降低低密度脂蛋白膽固醇(LDL-C)：  與statin類藥品併用於已接受最大… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：已查得 23 筆交互作用紀錄（以下為資料中列出者）。
  - 嚴重（Major）：多種皮質類固醇（hydrocortisone、prednisolone、prednisone、methylprednisolone、dexamethasone、betamethasone、triamcinolone、budesonide、deflazacort、fludrocortisone）、levofloxacin、simvastatin
  - 中度（Moderate）：rosuvastatin、empagliflozin、glyburide、repaglinide、rifaximin、selexipag、fexofenadine、revefenacin

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（甲狀腺機能亢進）無任何臨床試驗或文獻，機轉上也無直接關聯，僅屬 L5 的模型推論。
- 證據最多的 HoFH 預測（L3）方向合理，但證據以回顧文章為主，僅有 1 篇真實世界世代研究，且 HoFH 病人的 LDL 受體功能受損，療效可能受限，需要更多資料驗證。

**若要推進需要：**
- 取得 DrugBank 的完整作用機轉資料
- 詳讀 HoFH 真實世界世代研究（PMID 41274797）的療效與耐受性數據
- 針對 HoFH 設計或搜尋前瞻性臨床試驗，並評估殘存 LDL 受體活性對療效的影響
- 評估與 simvastatin 等 statin 類及皮質類固醇併用的交互作用管理策略
- 確認 HoFH 是否符合台灣現行核准適應症範圍及相關法規途徑

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「非 LDL 受體依賴機制」 | 報告重生後已無此錯誤（2026-10-15：新報告寫明 bempedoic acid 經提升 LDL 受體表現降低 LDL-C，且 HoFH 療效受殘存受體活性限制，與仿單一致；原為加註） | [DailyMed：NEXLETOL（bempedoic acid）美國仿單 §12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |
| 2026-10-03 | 同合子家族性高膽固醇血症預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [DailyMed：NEXLETOL（bempedoic acid）美國仿單 §12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |
| 2026-10-03 | 同合子家族性高膽固醇血症預測重審結果 | 重審：維持，證據等級 L3 不變（2026-10-16 修訂，前版保留於紀錄） | [PubMed：Real-world evaluation of bempedoic acid use in patients with homozygous familial hypercholesterolemia（PMID 41274797）](https://pubmed.ncbi.nlm.nih.gov/41274797/)；[PubMed：Bempedoic Acid Lowers Low-Density Lipoprotein Cholesterol and Attenuates Atherosclerosis in Low-Density Lipoprotein Receptor-Deficient (LDLR(+/-) and LDLR(-/-)) Yucatan Miniature Pigs（PMID 29449335）](https://pubmed.ncbi.nlm.nih.gov/29449335/) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L3） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

