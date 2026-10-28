---
layout: default
title: Hydroxyurea
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-16
description: "Hydroxyurea：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L4）。原適應症：慢性骨髓性白血病（治療前期與安寧療護）、復發／轉移／不可開刀之卵巢癌、與放射線併用於除唇外之原發性頭頸部鱗狀細胞癌之局部控制"
monitor_inn: "Hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin E disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
---

# Hydroxyurea
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Hydroxyurea：從慢性骨髓性白血病／卵巢癌／頭頸癌到女性乳癌
{: .text-alpha }

## 一句話總結

Hydroxyurea（羥基脲）是口服抗腫瘤藥物，台灣有效許可證的原適應症包括慢性骨髓性白血病、卵巢癌與頭頸部鱗狀細胞癌的局部控制。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，但目前**沒有任何臨床試驗**，只有以細胞實驗為主的文獻與少數併用化療的早期研究。證據等級僅為 L4。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性骨髓性白血病（治療前期與安寧療護）、復發／轉移／不可開刀之卵巢癌、與放射線併用於除唇外之原發性頭頸部鱗狀細胞癌之局部控制 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 2 張／共 5 張） |
| 許可證數 | 5 張（有效單方 2／有效複方 0／已註銷 3） |
| 建議決策 | Hold |

> **資料注意：** 依規則取第一張有效單方許可證，會得到「骨髓纖維化／真性紅血球增多症」。但這三張「捷可衛錠」的適應症文字提到「接受 hydroxyurea 治療後有抗藥性或無耐受性」，因此很可能是另一種藥物的許可證，被誤併入此藥。本報告的原適應症改採 hydroxyurea 本身的「愛治膠囊」許可證，建議人工核對。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠機轉欄位為空）。根據模型分析所附的機轉推論，hydroxyurea 抑制核糖核苷酸還原酶 (ribonucleotide reductase)，使去氧核糖核苷酸 (dNTP) 庫耗竭，造成 S 期停滯與複製壓力。這是癌細胞的一個弱點，前臨床乳癌研究也在利用這點。

原適應症（卵巢癌、頭頸癌、白血病）都是快速增殖的惡性腫瘤，乳癌同樣屬於增殖活躍的實體腫瘤。因此從機轉上推測，抑制 DNA 合成的策略可能適用。此外，hydroxyurea 兼具放射線增敏作用，與卵巢癌和頭頸癌「併用放療」的使用方式類似。

不過現有文獻多為細胞或藥物遞送研究，例如脂質結合物、奈米載體，以及與 valproic acid 合用增敏。這些只能支持機轉合理，不能證明臨床有效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

文獻中沒有針對乳癌的 RCT，以下為最相關的 10 篇：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | 世代研究（Phase I） | Am J Clin Oncol | 20 位晚期消化道與乳癌病人，使用 5-FU／leucovorin 後接 hydroxyurea 並以 allopurinol 保護的組合方案 |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | 世代研究（Phase I） | Cancer Chemother Pharmacol | 5-FU、hydroxyurea、cisplatin 合併放療，用於需姑息放療的晚期實體腫瘤，探討 cisplatin 最大耐受劑量 |
| [9060546](https://pubmed.ncbi.nlm.nih.gov/9060546/) | 1997 | 世代研究 | J Clin Oncol | 含 hydroxyurea 的多藥組合 (TPDC-FuHu) 用於復發轉移性腦瘤，非乳癌專屬 |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | 體外研究 | DNA Repair | Valproic acid 抑制 RPA2 過度磷酸化所介導的 DNA 修復，使乳癌細胞對 hydroxyurea 更敏感 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | 體外研究 | DNA Repair | 2-hexyl-4-pentynoic acid 作為 valproic acid 的替代候選，同樣影響 RPA2 介導的 DNA 修復 |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | 體外／電腦模擬 | Drug Research | 設計 hydroxyurea 脂質結合物以提高脂溶性與細胞攝取，針對 PI3K/AKT/mTOR 路徑 |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | 體外研究 | Mol Pharmacol | 新型核糖核苷酸還原酶抑制劑 COH29 抑制 DNA 修復，對 BRCA1 缺陷乳癌細胞有作用 |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | 體外研究 | Mol Cancer | EYA4 透過避免複製壓力促進乳癌進展與轉移（間接相關） |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | 體外研究 | Naunyn-Schmiedeberg's Arch Pharmacol | 載有 hydroxyurea 的磁性奈米粒子具 pH 依賴性釋放，並影響細胞週期與 p53 表現 |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | 病例報告 | Case Rep Hematol | 乳癌合併原發性血小板增多症的治療挑戰 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Hydroxyurea 的不重複許可證共 **5 張**：有效單方 2 張、有效複方 0 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第023135號 | 愛治膠囊500 毫克 | 膠囊劑 | 台灣大昌華嘉股份有限公司 | 2031/03/09 | 1. 治療慢性骨髓性白血病（治療前期與安寧療護）。 2. 治療復發、轉移或不可開刀之卵巢癌。 3. 與輻射線治療併用於除唇外之原發性頭及頸鱗狀細胞癌之局部控制。 |
| 衛部藥輸字第029076號 | 愛得靈膠囊500毫克 | 膠囊劑 | 韋淳貿易股份有限公司 | 2030/12/29 | 1.治療慢性骨髓性白血病（治療前期與安寧療護）。 2.治療復發、轉移或不可開刀之卵巢癌。 3.與輻射線治療併用於除唇外之原發性頭及頸鱗狀細胞癌之局部控制。 |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第044501號</td><td>"生達"羥化尿素</td><td>HYDROXYUREA</td><td>2017/02/09</td></tr><tr><td>衛署藥輸字第017468號</td><td>愛治膠囊５００公絲</td><td>HYDROXYUREA</td><td>1995/05/05</td></tr><tr><td>衛署藥輸字第020757號</td><td>愛治膠囊５００公絲</td><td>HYDROXYUREA</td><td>2005/06/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗代謝物／核糖核苷酸還原酶抑制劑） |
| 骨髓抑制風險 | 高（為主要劑量限制性毒性；知識圖譜亦列出白血球減少、血小板減少、貧血為相關禁忌疾病） |
| 致吐性分級 | 低 |
| 監測項目 | CBC（含分類與血小板）、腎功能、肝功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

以上分級依藥物類別判斷，詳細內容請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**（非仿單文字）：腎臟疾病、輸尿管積膿、血小板減少、貧血、巨球性貧血、白血球減少、皮膚血管炎。
- **藥物交互作用**：共查得 309 筆。列出的項目多數等級為「未知」，僅 Levofloxacin 為輕度。其他包括 Doxycycline、Amphotericin B、Hydrocortisone、Prednisone、Acetylsalicylic acid、Metformin、Omeprazole、Simvastatin 等，實際臨床意義需逐一查證。

仿單的警語與禁忌症全文請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 乳癌方向沒有臨床試驗，文獻以細胞實驗和早期併用化療研究為主，證據僅屬 L4。
- 乳癌已有成熟的標準治療，hydroxyurea 骨髓抑制風險高，需要更明確的臨床價值才值得推進。

**若要推進需要：**
- 補齊並確認作用機轉資料。
- 進行乳癌專屬的臨床前驗證，例如與 PARP 抑制劑或其他 DNA 修復抑制劑的併用；並設計小規模 Phase 2 試驗。
- 核對許可證資料，釐清「捷可衛錠」是否誤列於本藥之下。
- 補充仿單的警語、禁忌症與重要藥物交互作用。

**其他預測的參考：** 在同一批預測中，**鐮狀細胞-血紅素 C 病 (HbSC)** 的證據明顯較強，已有一項 Phase 2 試驗 (NCT00532883，因提前終止而說服力受限)、一篇 NEJM Evidence 2025 RCT (PMID 39647172) 以及多項世代研究，模型評為 L2 且建議 Proceed with Guardrails。若優先考量證據強度，建議先評估該方向。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」列入骨髓纖維化、真性紅血球增多症 | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列為 hydroxyurea 許可證原文，並註明捷可衛錠是誤併的另一種藥；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 一句話總結寫原本用於骨髓纖維化及真性紅血球增多症 | 報告重生後已無此錯誤（2026-10-15：新報告一句話總結為慢性骨髓性白血病、卵巢癌與頭頸部鱗狀細胞癌；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「捷可衛錠」一列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

