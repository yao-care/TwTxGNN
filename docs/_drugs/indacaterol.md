---
layout: default
title: Indacaterol
parent: 高證據等級 (L1-L2)
nav_order: 133
evidence_level: L1
indication_count: 1
---

# Indacaterol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

此技能適用於 TxGNN 模型訓練與部署管道，與本次撰寫評估報告的任務不直接相關。依照系統提示的報告格式直接輸出。

---

# Indacaterol：從 COPD 到 支氣管疾病

## 一句話總結

Indacaterol 是超長效 β2 腎上腺素受體激動劑（ultra-LABA），台灣核准用於 COPD 及氣喘的吸入維持治療。TxGNN 模型共預測 10 個新適應症，其中**支氣管疾病 (Bronchial Disease)** 具備最完整的臨床證據，目前有 **37 個臨床試驗**和 **20 篇文獻**支持；其餘 9 項預測（頭痛疾病、腎臟抗利尿症候群、腱炎、肌炎等）均僅有模型預測，缺乏直接臨床或前臨床依據，建議暫緩。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘維持治療（ICS 控制不佳，需合併 LABA/ICS 之成年病人） |
| 預測新適應症 | 支氣管疾病 (Bronchial Disease) |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Indacaterol 為選擇性超長效 β2 腎上腺素受體激動劑，與氣道平滑肌上的 β2 受體結合後，啟動 Gs 蛋白→腺苷酸環化酶→cAMP→PKA 訊號路徑，使平滑肌持續鬆弛達 24 小時以上。這個機轉直接對應支氣管疾病（含氣喘與 COPD）的核心病機——氣道可逆性收縮與氣流阻塞，是其核准適應症的直接藥理依據。

支氣管疾病與 Indacaterol 現有核准的 COPD 及氣喘適應症本質上高度重疊：COPD 的慢性支氣管炎即屬支氣管疾病的一環，而 ultra-LABA 在氣道的持久鬆弛作用，同樣可改善各類支氣管收縮引起的氣流受限。TxGNN 對支氣管疾病的預測，可視為已核准適應症在更廣泛支氣管疾病類別上的確認性延伸。

多項國際 Phase 3 關鍵試驗（含 IRIDIUM 研究、QVM149 vs QMF149 試驗）已系統性驗證 Indacaterol 單藥及三合一固定劑量組合製劑（搭配 Glycopyrronium + Mometasone）的療效與長期安全性。在本 Evidence Pack 全部 10 項 TxGNN 預測適應症中，支氣管疾病是唯一達到 L1 最高證據等級的適應症。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02571777](https://clinicaltrials.gov/study/NCT02571777) | Phase 3 | 完成 | 3,092 | QVM149 兩種劑量（IND/GLY/MF 150/50/80μg 及 150/50/160μg）vs QMF149（IND/MF）52 週療效與安全性比較，評估三合一組合用於控制不佳氣喘患者的肺功能及氣喘控制 |
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | 完成 | 2,216 | QMF149（Indacaterol/Mometasone）兩種劑量 vs Mometasone 單藥 52 週研究，評估固定劑量組合對肺功能改善與氣喘控制的優越性 |
| [NCT00941798](https://clinicaltrials.gov/study/NCT00941798) | Phase 2 | 完成 | 2,283 | QMF149 Twisthaler 大型安全性試驗，以嚴重氣喘惡化（住院／插管／死亡）為事件驅動終點，評估 IND/MF 固定劑量組合的安全性 |
| [NCT03158311](https://clinicaltrials.gov/study/NCT03158311) | Phase 3 | 完成 | 1,426 | QVM149 vs Salmeterol/Fluticasone + Tiotropium 自由三合一組合 24 週非劣效性研究，支持固定劑量三合一製劑替代自由組合的可行性 |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | 完成 | 805 | Indacaterol 300/600μg vs Salmeterol 26 週長期安全性比較，中至重度持續性氣喘患者，雙盲雙模擬設計 |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | 完成 | 335 | Indacaterol acetate 75μg/150μg 12 週療效、安全性及藥動學研究，為 QMF149 固定劑量組合的劑量選擇提供依據 |
| [NCT01156844](https://clinicaltrials.gov/study/NCT01156844) | Phase 2 | 完成 | 191 | 多中心雙盲重複給藥研究，比較三種 Indacaterol 劑量方案（含每日一次）於持續性氣喘的支氣管擴張療效 |
| [NCT04259164](https://clinicaltrials.gov/study/NCT04259164) | Phase 3 | 完成 | 28 | 雙盲交叉研究，評估於 Indacaterol/Mometasone 基礎上加入 Glycopyrronium 對過敏原誘發晚期氣喘反應的抗炎效果 |
| [NCT05274425](https://clinicaltrials.gov/study/NCT05274425) | 觀察性 | 進行中 | 600 | Enerzair（QVM149）24 週上市後真實世界觀察性研究，在常規臨床實務下評估長期安全性與有效性 |
| [NCT03100825](https://clinicaltrials.gov/study/NCT03100825) | Phase 3 | 完成 | 96 | QVM149 在日本氣喘患者的 52 週長期安全性研究，支持日本地區藥品許可申請 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | RCT | Lancet Respiratory Medicine | IRIDIUM 研究：MF-IND-GLY 每日一次三合一吸入製劑對控制不佳氣喘患者的療效優於 ICS-LABA 雙合一，Phase 3 隨機對照設計 |
| [33711782](https://pubmed.ncbi.nlm.nih.gov/33711782/) | 2021 | Meta-analysis | Respiratory Medicine | 匯整多項 Phase 3 試驗，分析 MF/IND 及 MF/IND/GLY 的心血管安全性，結果未見顯著風險增加 |
| [34783265](https://pubmed.ncbi.nlm.nih.gov/34783265/) | 2022 | RCT | Expert Review of Respiratory Medicine | 系統評估 IND/GLY/MF 三合一製劑在中重度氣喘的療效、安全性及與現行指引的臨床定位 |
| [32967685](https://pubmed.ncbi.nlm.nih.gov/32967685/) | 2020 | RCT | Respiratory Research | 比較 Indacaterol maleate 與 acetate 鹽型的肺功能、藥動學及耐受性（含吸入後咳嗽），支持固定劑量組合劑型開發 |
| [34329722](https://pubmed.ncbi.nlm.nih.gov/34329722/) | 2021 | Cohort | Pulmonary Pharmacology & Therapeutics | MF/IND 與 MF/IND/GLY 固定劑量組合的 Mometasone 劑量橋接數據，確認不同劑型間的生物等效性 |
| [31404293](https://pubmed.ncbi.nlm.nih.gov/31404293/) | 2019 | Cohort | Frontiers in Pharmacology | COPD 患者中嗜酸球性炎症與氣道過度反應表型分析，探討吸入性皮質類固醇在支氣管疾病的適用性 |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Review | Drugs | IND/GLY/MF（Enerzair Breezhaler）於氣喘的全面藥物評論：藥理機轉、關鍵臨床試驗及 EU 核准情況 |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Review | Respiratory Medicine | Ultra-LABA 類藥物（abediterol、indacaterol、olodaterol、vilanterol）用於氣喘的療效、安全性及 ICS 合用證據回顧 |
| [24247039](https://pubmed.ncbi.nlm.nih.gov/24247039/) | 2014 | Review | Current Opinion in Pulmonary Medicine | 支氣管疾病中新型支氣管擴張劑的藥理特性與臨床開發進展，含 β2 激動劑與蕈毒鹼拮抗劑最新比較 |
| [22611179](https://pubmed.ncbi.nlm.nih.gov/22611179/) | 2012 | Review | Pharmacological Reviews | 支氣管擴張劑藥理學與治療學全面回顧，深入解析 β2-AR 激動劑作用機轉、分子特性及臨床應用 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028048號 | 艾能舒吸入膠囊150/50/80微克 | 吸入用膠囊劑 | 適用於併用吸入性長效型β2-腎上腺受體作用劑和吸入性皮質類固醇治療氣喘仍控制不佳的成年病人，做為氣喘維持治療。 |
| 衛部藥輸字第028049號 | 艾能舒吸入膠囊150/50/160微克 | 吸入用膠囊劑 | 適用於併用吸入性長效型β2-腎上腺受體作用劑和吸入性皮質類固醇治療氣喘仍控制不佳的成年病人，做為氣喘維持治療。 |

> 台灣共有 19 張相關許可證，涵蓋 Indacaterol 單藥（COPD 適應症）及多種複方劑量規格，上表為目前可取得的代表性品項。

---

## 安全性考量

**藥物交互作用**（DDInter 資料庫共計 440 筆，以下列出主要警示項目）：

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Epinephrine | Moderate | 兩者均具腎上腺素能作用，合用可能加強心血管效應（心跳加速、血壓變化） |
| Clarithromycin | Moderate | CYP 酵素及 P-gp 抑制劑，可能提高 Indacaterol 血中濃度 |
| Metformin | Moderate | β2 激動劑可升高血糖，可能對抗雙胍類降血糖效果 |
| Canagliflozin | Moderate | β2 激動劑影響血糖調控，與 SGLT2 抑制劑合用需監測血糖 |
| Dapagliflozin | Moderate | 同上，需監測血糖變化 |
| Acarbose | Moderate | β2 激動劑的升糖效應可能抵銷 α-葡萄糖苷酶抑制劑療效 |
| Alogliptin | Moderate | 需注意心率及血糖的聯合效應 |
| Saxagliptin | Moderate | DPP-4 抑制劑合用時，注意心率與血糖監測 |
| Budesonide | Minor | 常見合用組合；β2 激動劑 + 吸入性皮質類固醇有低血鉀效應加成風險 |
| Dexamethasone | Minor | 全身性皮質類固醇合用時，需監測低血鉀 |

> 安全性完整資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
支氣管疾病是 Indacaterol β2 受體激動機轉的直接治療標靶，多項完成的 Phase 3 RCT（含 IRIDIUM 研究、QVM149 52 週試驗）及大規模上市後安全性資料已建立 L1 最高等級臨床證據，台灣現有 19 張許可證佐證廣泛的臨床使用基礎。其餘 9 項 TxGNN 預測（頭痛疾病、腎臟抗利尿症候群、腱旁炎、鈣化性肌腱炎、多毛症、肌炎、過敏反應、先天性毛髮過多症）均為 L5 等級，缺乏直接臨床或前臨床支持，目前建議暫緩（Hold）。

**若要推進需要：**
- 補充完整作用機轉（MOA）資料（透過 DrugBank API 查詢 DB05039），強化機轉關聯性分析
- 確認不同 Indacaterol 組合製劑（IND 單藥 / IND+GLY / IND+GLY+MF）在特定支氣管疾病亞型（如小兒族群、嗜酸球性表型）中的劑量選擇依據
- 對 9 項 L5 預測適應症，如有探索意願，應優先進行機轉合理性評估及前臨床研究設計，並釐清吸入製劑對非肺部標靶器官的給藥途徑可行性
- 定期更新 DDI 資料（建議每季確認 DDInter 資料庫版本）

---

