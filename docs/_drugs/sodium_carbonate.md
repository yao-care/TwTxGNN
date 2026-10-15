---
layout: default
title: Sodium Carbonate
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 6
---

# Sodium Carbonate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# 碳酸鈉（Sodium carbonate）：從制酸劑／無菌製劑鹼化輔助劑到乾眼症

## 一句話總結

碳酸鈉是一種鹼化劑與制酸劑，在台灣常用於制酸、無菌製劑的 pH 調整，也作為多種注射用抗生素的緩衝成分。
TxGNN 模型預測分數最高的新適應症為**海綿尾症候群（馬尾症候群，Cauda Equina Syndrome）**，但完全沒有臨床試驗或文獻支持。
相對較有線索的是**乾眼症（Dry Eye Syndrome）**，目前僅有 **1 篇**間接相關文獻（探討口乾，而非乾眼）。整體證據非常薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無菌製劑輔助劑(鹼化藥)（唯一單方原料藥許可證「展旺無菌碳酸鈉」，2023-06-30 已註銷）；現行有效許可證中為 ceftazidime 注射劑的賦形劑及複方點眼液、胃散的成分 |
| 預測新適應症 | 馬尾症候群（Cauda Equina Syndrome）；排名第 1 |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L5（僅有模型預測） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 26 張（有效單方 1／有效複方 5／已註銷 20） |
| 建議決策 | Hold |

<!-- review:begin sodium-carbonate-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／制酸劑（取自單方且仍有效的許可證，其適應症為「抗生素」，屬於含碳酸鈉的抗生素粉劑；另有已註銷的單方許可證適應症為「無菌製劑輔助劑（鹼化藥）」與「制酸劑」）」。2026-10-15 報告重生後此列仍以「制酸劑」為原適應症。「制酸劑」出自碳酸氫鈉、三矽酸鎂等其他成分；sodium carbonate 唯一單方許可證（無菌製劑輔助劑(鹼化藥)）已於 2023-06-30 註銷，現行有效許可證中它是抗生素注射劑的賦形劑或複方點眼液、胃散的成分。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end sodium-carbonate-original-indication-2026-10-03 -->

> 備註：排名第 1 的預測缺乏任何證據。若以證據面向挑選，排名第 5 的乾眼症（L4）是唯一較值得進一步探討的方向，詳見下文。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，碳酸鈉是鹼化劑與制酸劑，作用為中和胃酸、調整溶液 pH，並在多種注射用抗生素粉劑（如 Meropenem、Ceftazidime 製劑）中作為緩衝成分。

針對各預測適應症，機轉上的合理性評估如下：

- **馬尾症候群**：碳酸鈉沒有任何與馬尾神經壓迫性神經病變相關的已知藥理機轉，此關聯僅來自 TxGNN 預測。
- **過敏性休克、食物依賴運動誘發過敏性休克**：碳酸鈉最多只是腎上腺素製劑中的 pH 調整賦形劑，沒有直接抗過敏作用，第一線治療仍是腎上腺素。
- **神經源性膀胱（已過時的疾病詞條）**：碳酸鈉對逼尿肌或括約肌的神經控制無已知作用，且該疾病詞條已廢止，進一步削弱預測可信度。
- **乾眼症**：碳酸鈉在眼用製劑中作為緩衝與鹼化劑（台灣已有含碳酸鈉的點眼液，適應症包含淚液補充與結膜囊清淨），具有微弱的間接合理性。但這僅說明其為製劑成分，不代表有治療乾眼的療效。
- **心室頻脈**：用於鈉通道阻斷劑中毒合併心律不整的是碳酸氫鈉，而非碳酸鈉；沒有證據支持碳酸鈉用於心室頻脈，且全身性鹼化有電解質風險。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為各預測適應症中唯一檢索到的文獻（均非直接支持碳酸鈉治療該疾病）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27813150](https://pubmed.ncbi.nlm.nih.gov/27813150/) | 2017 | Cohort | Gerodontology | 評估碳酸氫鈉＋木糖醇噴霧搭配非手術牙周治療用於原發性乾燥症（Sjögren's syndrome）患者，屬口腔乾燥的探索性研究，並非乾眼症研究（對應乾眼症預測） |
| [34600046](https://pubmed.ncbi.nlm.nih.gov/34600046/) | 2021 | In vitro | Eur J Pharm Sci | 探討腎上腺素舌下錠的穩定性與通透路徑，以及調整舌下微環境 pH 的影響；為體外配方研究，與碳酸鈉治療過敏性休克無直接關係（對應過敏性休克預測） |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sodium Carbonate 的不重複許可證共 **26 張**：有效單方 1 張、有效複方 5 張、已註銷 20 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第041013號 | "濟生"賜達注射劑 | 乾粉注射劑 | 濟生醫藥生技股份有限公司 | 2027/04/03 | ＣＥＦＴＡＺＩＤＩＭＥ 是殺菌性頭孢子菌抗生素、對多種乙醢鑄、有抵抗力、並對廣泛之革蘭氏陽性及陰性細菌有效。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（5 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛成製字第001353號 | "明通"保身散 | GLYCYRRHIZA POWDER、CITRUS、CLOVE POWDER、SODIUM CARBONATE、SODI… | 散劑 | 胃痛、消化不良、飽脹、胃酸過多 |
| 衛署藥製字第004068號 | 視麗兒點眼液 | SODIUM PHOSPHATE MONOBASIC (EQ TO MONOSODIUM PHOSPHATE)(EQ T… | 點眼液劑 | 暫時緩解因眼睛乾澀所引起灼熱感與刺激感。 |
| 衛署藥製字第038508號 | "杏輝"旺滴點眼液 | SODIUM CHLORIDE、BORIC ACID、SODIUM PHOSPHATE DIBASIC HEPTAHYD… | 點眼液劑 | 淚液之補充、眼睛疲勞結膜囊的清淨化（如清淨塵埃、灰塵微粒子、細菌）。 |
| 衛署藥製字第041754號 | "生達" 孢妥注射劑（西他利汀） | STERILE CEFTAZIDIME (SODIUM CARBONATE)、STERILE CEFTAZIDIME (… | 注射劑 | ＣＥＦＴＡＺＩＤＩＭＥ 是殺菌性頭孢子菌抗生素、對多種乙內醯胺有抵抗力、並對廣範圍的革蘭氏陽性及陰性細菌有效。 |
| 衛署藥製字第057227號 | "派頓"滴潤人工淚液 | SODIUM CARBONATE ANHYDROUS、POTASSIUM CHLORIDE、SODIUM CHLORID… | 點眼液劑 | 暫時緩解因眼睛乾澀所引起灼熱感與刺激感。 |

<details><summary><strong>已註銷</strong>（20 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛成製字第003209號</td><td>三和胃散</td><td>FENNEL POWDER (FOENICULI POWDER)、CINNAMON POWDER (CINNAMON C…</td><td>1996/04/16</td></tr><tr><td>內衛成製字第003546號</td><td>養胃散</td><td>SODIUM CARBONATE、MAGNESIUM CARBONATE、CINNAMON POWDER (CINNAM…</td><td>2012/10/15</td></tr><tr><td>內衛藥製字第002553號</td><td>胃舒樂片</td><td>BENZOCAINE (ETHYL AMINOBENZOATE)、SODIUM CARBONATE、ALUMINUM S…</td><td>2015/07/14</td></tr><tr><td>衛署藥製字第013654號</td><td>明瞳眼藥水</td><td>POTASSIUM CHLORIDE、SODIUM CHLORIDE、SODIUM CARBONATE、SODIUM P…</td><td>1993/12/30</td></tr><tr><td>衛署藥製字第026918號</td><td>西平黴素注射劑１０００公絲（西華定）</td><td>SODIUM CARBONATE、CEPHRADINE</td><td>1991/10/05</td></tr><tr><td>衛署藥製字第036645號</td><td>旺滴舒點眼液</td><td>POTASSIUM CHLORIDE、BORIC ACID、SODIUM CHLORIDE、SODIUM PHOSPHA…</td><td>1995/06/26</td></tr><tr><td>衛署藥輸字第006789號</td><td>緩衝性西華孟多甲酸酯鈉</td><td>CEFAMANDOLE、SODIUM CARBONATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第007818號</td><td>喜洛巴注射劑</td><td>SODIUM CARBONATE、SODIUM HYDROXIDE、TEGAFUR (FTORAFUR)</td><td>1987/06/13</td></tr><tr><td>衛署藥輸字第008050號</td><td>德泰固命注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、ASPARTATE…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008051號</td><td>德泰復生注射液</td><td>ARGININE HCL L-、PANTHENOL、L-ARGININE、NIACINAMIDE (NICOTINAMI…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008052號</td><td>德泰利多注射液</td><td>ORNITHINE L- ASPARTATE L-、SODIUM CHLORIDE、CYANOCOBALAMIN (VI…</td><td>1988/01/28</td></tr><tr><td>衛署藥輸字第008053號</td><td>德泰安命注射液</td><td>CYSTINE L-、GLUTAMIC ACID L-、SODIUM CARBONATE MONOHYDRATE、SOR…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008054號</td><td>德泰氨美注射液</td><td>L-ARGININE、NIACINAMIDE (NICOTINAMIDE)、PANTHENOL、L-TRYPTOPHAN…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第011982號</td><td>康脈得注射液</td><td>L-ISOLEUCINE、L-VALINE、POTASSIUM CHLORIDE、L-PHENYLALANINE、L-A…</td><td>1988/01/18</td></tr><tr><td>衛署藥輸字第016134號</td><td>康脈得注射液</td><td>L-VALINE、HISTIDINE L- HCL (EQ TO L-HISTIDINE HYDROCHLORIDE)、…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016457號</td><td>紐賽發注射劑１０００公絲</td><td>CEFAMANDOLE (NAFATE)、SODIUM CARBONATE ANHYDROUS</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第017704號</td><td>德泰氨美注射液</td><td>XYLITOL、THIAMINE HYDROCHLORIDE、RIBOFLAVIN PHOSPHATE SODIUM、L…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017706號</td><td>德泰固命注射液</td><td>SODIUM CHLORIDE、GLUTAMIC ACID L-、SORBITOL、INOSITOL (MESO-INO…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017726號</td><td>德泰安命注射液</td><td>L-ARGININE、L-TYROSINE、L-TRYPTOPHAN、MAGNESIUM CHLORIDE、PYRIDO…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017727號</td><td>德泰復生注射液</td><td>CYANOCOBALAMIN (VIT B12)、ORNITHINE L- ASPARTATE L-、GLUTAMIC…</td><td>2000/09/04</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（約 99.2%–99.8%），但所有預測適應症均缺乏臨床試驗，且機轉上無合理連結，屬於純模型訊號。
- 最接近可探討的是乾眼症（L4，標示為研究問題），但唯一文獻研究的是口乾而非乾眼，且使用的是碳酸氫鈉。

**若要推進需要：**
- 補齊碳酸鈉的作用機轉資料（目前為資料缺口）。
- 針對乾眼症，檢索並評估眼用碳酸鈉／鹼化緩衝製劑的直接證據，必要時設計前臨床或探索性研究。
- 確認含碳酸鈉的既有點眼液之配方角色（緩衝劑或活性成分），避免將賦形劑功能誤判為療效。
- 其他預測（馬尾症候群、過敏性休克、神經源性膀胱、心室頻脈）在缺乏機轉依據下，不建議投入資源。
- 補充安全性資料（警語、禁忌症、藥物交互作用），並確認各劑型與給藥途徑的相容性。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市資訊表：sodium carbonate 在所列許可證中是賦形劑 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症「制酸劑」等取自其他成分 | 更正（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L4） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

