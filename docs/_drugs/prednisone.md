---
layout: default
title: Prednisone
parent: 高證據等級 (L1-L2)
nav_order: 232
evidence_level: L2
indication_count: 10
---

# Prednisone
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

# Prednisone：從糖皮質素抗發炎用途到圓形禿 (Alopecia Areata)

<!-- review:begin prednisone-original-indication-other-drugs-title-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「# Prednisone：從風溼性關節炎到圓形禿 (Alopecia Areata)」。TFDA 許可證資料中，prednisone 目前沒有有效單方許可證（已註銷的單方證曾載濕疹、過敏症、類風濕關節炎）；唯一有效許可證是 prednisone＋crotamiton 複方軟膏（衛署藥製字第042080號，濕疹或皮膚炎）。「風溼性關節炎」字樣見於主成分為 prednisolone 的已註銷許可證（內衛藥輸字第005124號），「急性病症（氣喘、休克）」來自 methylprednisone 針劑（內衛藥輸字第003633號，已註銷）。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end prednisone-original-indication-other-drugs-title-2026-10-16 -->

## 一句話總結

Prednisone 是口服糖皮質素（glucocorticoid）類藥物，台灣目前沒有有效的 prednisone 單方許可證，唯一有效許可證是與 crotamiton 的複方軟膏（濕疹或皮膚炎）。
TxGNN 模型預測它可能對**圓形禿 (Alopecia Areata)** 有效，
目前**無登記的臨床試驗**，但有 **20 篇文獻**支持這個方向，其中包含 1 篇隨機對照試驗（RCT）。

<!-- review:begin prednisone-original-indication-other-drugs-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「台灣核准適應症涵蓋風溼性關節炎、急性過敏性病症等發炎與免疫相關疾病。」。TFDA 許可證資料中，prednisone 目前沒有有效單方許可證（已註銷的單方證曾載濕疹、過敏症、類風濕關節炎）；唯一有效許可證是 prednisone＋crotamiton 複方軟膏（衛署藥製字第042080號，濕疹或皮膚炎）。「風溼性關節炎」字樣見於主成分為 prednisolone 的已註銷許可證（內衛藥輸字第005124號），「急性病症（氣喘、休克）」來自 methylprednisone 針劑（內衛藥輸字第003633號，已註銷）。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end prednisone-original-indication-other-drugs-summary-2026-10-16 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 台灣現無有效單方許可證（已註銷單方證曾載濕疹、過敏症、類風濕關節炎）；唯一有效許可證為 prednisone＋crotamiton 複方軟膏：濕疹或皮膚炎（衛署藥製字第042080號） |
| 預測新適應症 | 圓形禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2（註：文獻中有 1 篇 RCT，但為 methotrexate 單用對比 methotrexate 加低劑量 prednisone，並非 prednisone 單用的已完成 Phase 2/3 RCT，且無臨床試驗登記，實際證據偏弱，保守可視為 L3） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 7 張（有效單方 0／有效複方 1／已註銷 6） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin prednisone-original-indication-other-drugs-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／風溼性關節炎」。TFDA 許可證資料中，prednisone 目前沒有有效單方許可證（已註銷的單方證曾載濕疹、過敏症、類風濕關節炎）；唯一有效許可證是 prednisone＋crotamiton 複方軟膏（衛署藥製字第042080號，濕疹或皮膚炎）。「風溼性關節炎」字樣見於主成分為 prednisolone 的已註銷許可證（內衛藥輸字第005124號），「急性病症（氣喘、休克）」來自 methylprednisone 針劑（內衛藥輸字第003633號，已註銷）。已改為台灣許可證現況。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end prednisone-original-indication-other-drugs-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位為空）。根據一般藥理知識，Prednisone 在體內轉換為 prednisolone，作為糖皮質素受體促效劑，具有抗發炎與免疫抑制作用。

圓形禿是 T 細胞介導的自體免疫疾病，免疫細胞攻擊毛囊。Prednisone 在風溼性關節炎等自體免疫、發炎疾病中的療效已被證實，抑制 T 細胞攻擊的機轉上，可能同樣適用於圓形禿。

不過，歷史文獻顯示療效多為短期：1976 年的追蹤報告指出，停藥後長期效益不顯著，且全身性類固醇有痤瘡、肥胖、水晶體混濁、輕度高血壓等副作用。近年的研究方向是低劑量 prednisone 與其他藥物（如 methotrexate、baricitinib）併用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下表列出最相關的文獻（RCT 優先）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | 針對全禿／普禿型圓形禿，比較 methotrexate 單用與 methotrexate 加低劑量 prednisone 的兩階段雙盲試驗 |
| [1444500](https://pubmed.ncbi.nlm.nih.gov/1444500/) | 1992 | 隨機對照試驗（原資料未標示類型） | Arch Dermatol | 32 名患者接受 6 週 prednisone 漸減，之後合併 2% minoxidil 或安慰劑，另與 48 人開放試驗比較 |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Arch Dermatol | 回顧圓形禿的治療、療效、安全性與機轉；因研究設計差異大，難以比較各藥物 |
| [38650498](https://pubmed.ncbi.nlm.nih.gov/38650498/) | 2024 | Cohort | Ital J Dermatol Venereol | 義大利圓形禿住院患者的共病、治療模式與經濟負擔 |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case series | Clin Exp Dermatol | 8 例極嚴重圓形禿，baricitinib 併用低劑量類固醇有明顯改善 |
| [41958306](https://pubmed.ncbi.nlm.nih.gov/41958306/) | 2026 | Case series | JEADV | Baricitinib 加低劑量 prednisone 治療極嚴重圓形禿的回溯性病例系列 |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Case series | Ann Dermatol Venereol | 每月一次口服 prednisone 脈衝療法的療效與安全性評估 |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Case series | Arch Dermatol | 18 名隔日服用 prednisone 者，停藥後平均 15 個月追蹤，長期效益不顯著且副作用多 |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | 未分類 | J Am Acad Dermatol | 全身性 cyclosporine 加低劑量 prednisone 治療慢性嚴重圓形禿 |
| [24326561](https://pubmed.ncbi.nlm.nih.gov/24326561/) | 2013 | 病例報告 | J Investig Dermatol Symp Proc | 嚴重圓形禿合併多重自體免疫疾病患者，使用 cyclosporine 加 prednisone 後有臨床反應 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Prednisone 的不重複許可證共 **7 張**：有效單方 0 張、有效複方 1 張、已註銷 6 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第042080號 | 育麗素軟膏 | PREDNISONE、CROTAMITON | 軟膏劑 | 濕疹或皮膚炎 |

<details><summary><strong>已註銷</strong>（6 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第006887號</td><td>育麗素軟膏</td><td>CROTAMITON、PREDNISONE</td><td>1998/07/30</td></tr><tr><td>內衛藥製字第013051號</td><td>百力康軟膏</td><td>PREDNISONE</td><td>1996/08/15</td></tr><tr><td>衛署藥輸字第001597號</td><td>"普強" 去氫可體松</td><td>PREDNISONE</td><td>2016/05/31</td></tr><tr><td>衛部藥輸字第026256號</td><td>樂多特1毫克緩釋錠</td><td>PREDNISONE</td><td>2018/09/10</td></tr><tr><td>衛部藥輸字第026257號</td><td>樂多特2毫克緩釋錠</td><td>PREDNISONE</td><td>2018/09/10</td></tr><tr><td>衛部藥輸字第026258號</td><td>樂多特5毫克緩釋錠</td><td>PREDNISONE</td><td>2018/09/10</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共記錄 806 筆交互作用，部分重要項目如下：
  - 重大（Major）：Adalimumab
  - 中度（Moderate）：Zidovudine、Isotretinoin、Acarbose、Ketorolac、Ibuprofen、Nifedipine、Ethinylestradiol、Aldesleukin、Alemtuzumab 等
  - 輕微（Minor）：Formoterol、Salbutamol
- **知識圖譜顯示的疾病禁忌**（來自模型知識圖譜，非仿單內容）：高血壓、癲癇、高血糖、充血性心衰竭、麻疹、單純疱疹病毒角膜炎、尿素循環代謝異常（如瓜胺酸血症、高精胺酸血症）、腦下垂體功能不全與生長激素缺乏相關疾病等。
- 文獻也提到全身性類固醇的實際副作用，包括痤瘡、肥胖、水晶體混濁與輕度高血壓。

詳細警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 糖皮質素的免疫抑制機轉與圓形禿的自體免疫病理吻合，且有 1 篇 2023 年 RCT 與多篇病例系列支持低劑量 prednisone 作為合併治療的一環。
- 但缺乏臨床試驗登記，早期研究顯示單用療效短暫、停藥後易復發，且長期全身性使用副作用明顯，因此需設限條件推進。

**若要推進需要：**
- 補充 prednisone 作用機轉資料（MOA）。
- 設計以 prednisone 為主體的前瞻性對照試驗，並明確定義劑量、療程與合併藥物（如 methotrexate、JAK 抑制劑）。
- 建立長期安全性監測計畫（血壓、血糖、眼睛、骨密度、感染風險），並考量排除有高血壓、高血糖、心衰竭等禁忌共病的族群。
- 與已核准的圓形禿治療（如 JAK 抑制劑）進行定位比較。

**其他預測適應症的簡要說明：**
- 腱鞘炎（tenosynovitis，L3）：有觀察性文獻，屬研究性問題，建議列為後續探索。
- 黏蛋白性禿髮（alopecia mucinosis，L4）：僅有病例報告，列為研究性問題。
- 其餘預測（休止期落髮、禿髮性毛囊炎、遺傳性毛髮疾病等）僅有模型預測，機轉合理性不足，建議暫緩（Hold）。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「保癌寧等」列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症寫風溼性關節炎（台灣無有效單方） | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 標題以風溼性關節炎為台灣原適應症 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結稱台灣核准適應症涵蓋風溼性關節炎、急性過敏性病症 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

