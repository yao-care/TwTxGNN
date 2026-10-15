---
layout: default
title: Daptomycin
parent: 中證據等級 (L3-L4)
nav_order: 79
evidence_level: L4
indication_count: 10
---

# Daptomycin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Daptomycin：從複雜性皮膚感染與菌血症到骨關節炎

## 一句話總結

Daptomycin 是環狀脂肽類抗生素，原本用於治療革蘭氏陽性菌引起的複雜性皮膚和皮膚組織感染（cSSSI）及金黃色葡萄球菌菌血症。
TxGNN 模型預測它可能對**骨關節炎 (osteoarthritis)** 有效，但目前**沒有臨床試驗**，文獻僅有 10 篇，且多數談的是骨關節「感染」而非退化性骨關節炎，因此證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 成人及兒童（1至17歲）革蘭氏陽性菌引起的複雜性皮膚和皮膚組織感染（cSSSI）；成人金黃色葡萄球菌菌血症（含右側感染性心內膜炎）；兒童金黃色葡萄球菌菌血症 |
| 預測新適應症 | 骨關節炎 (osteoarthritis) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L4 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張（有效單方 5／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Daptomycin 是環狀脂肽類抗生素，可使革蘭氏陽性菌的細胞膜去極化而殺菌。這是抗菌作用，與退化性骨關節炎的病理（軟骨退化、關節慢性發炎）沒有直接關聯。

模型給出高分，較可能是「疾病標籤重疊」所致：文獻中的 Daptomycin 研究主要是骨關節感染（如人工關節感染、骨髓炎），檢索時被歸到「osteoarthritis」相關詞彙。這些研究支持的是**感染性**骨關節疾病的治療，不能推論到**退化性**骨關節炎。

值得留意的是，同一份預測清單中排名第 2 的**類風濕性關節炎**有 2025 年的動物研究（膠原誘導關節炎模型），顯示 Daptomycin 可能透過抑制發炎細胞激素與 NF-κB 路徑產生抗發炎作用。但這僅是動物證據，且不屬於本報告主要預測的骨關節炎。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | 世代研究 | International Orthopaedics | 評估高劑量 Daptomycin 併用 rifampicin 治療革蘭氏陽性菌骨關節感染的安全性與療效 |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | 世代研究 | J Antimicrob Chemother | 比較 Daptomycin 與標準治療用於金黃色葡萄球菌菌血症相關骨關節感染的結果 |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | 世代研究 | Int J Antimicrob Agents | 高劑量（>6 mg/kg）Daptomycin 用於複雜骨關節及植入物相關感染 |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | 世代研究 | Medicina Clinica | 西班牙 EU-CORE 資料庫，Daptomycin 於各類革蘭氏陽性菌感染的實際使用結果 |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | 世代研究 | Surgical Infections | 十年間骨關節感染葡萄球菌的微生物特性變化 |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | 病例系列 | J Antimicrob Chemother | Daptomycin 用於膝、髖人工關節感染的臨床經驗 |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | 調查/綜述 | Int J Antimicrob Agents | 美國感染症醫師處理人工關節感染的用藥偏好調查 |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | 體外研究 | J Antibiotics | 人工關節感染分離菌株的體外藥物感受性 |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | 病例報告 | Case Reports in Orthopedics | 一名疑似骨關節炎病人，實為慢性紋狀棒狀桿菌化膿性關節炎 |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | 病例報告 | ASM Case Reports | 原生關節滑液分離出 Corynebacterium propinquum 的化膿性關節炎 |

以上文獻皆屬骨關節感染或微生物學研究，沒有任何一篇評估 Daptomycin 對退化性骨關節炎的療效。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Daptomycin 的不重複許可證共 **6 張**：有效單方 5 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第024565號 | 救必辛注射劑 | 凍晶注射劑 | 台灣東洋藥品工業股份有限公司 | 2031/11/14 | 1. 治療成人及兒童（1至17歲）病人因下列感受性革蘭氏陽性菌引起的複雜性皮膚和皮膚組織感染 (cSSSI)：Staphylococcus aureus（包括methicillin… |
| 衛部藥製字第062130號 | 救必優凍晶注射劑350毫克 | 凍晶注射劑 | 台灣東洋藥品工業股份有限公司 | 2031/03/06 | 1.治療成人及兒童（1至17歲）病人因下列感受性革蘭氏陽性菌引起的複雜性皮膚和皮膚組織感染(cSSSI):Staphylococcus aureus (包括 methicillin… |
| 衛部藥輸字第028622號 | 安托幸 凍晶注射劑 500毫克 | 凍晶注射劑 | 佑立康藥業生技有限公司 | 2028/11/30 | 1. 治療成人及兒童（1至17歲）病人因下列感受性革蘭氏陽性菌引起的複雜性皮膚和皮膚組織感染 (cSSSI)：Staphylococcus aureus（包括methicillin… |
| 衛部藥輸字第028939號 | 欣達效注射劑 | 凍晶注射劑 | 意欣國際有限公司 | 2030/04/10 | 1. 治療成人及兒童（1至17歲）病人因下列感受性革蘭氏陽性菌引起的複雜性皮膚和皮膚組織感染 (cSSSI)： Staphylococcus aureus（包括methicilli… |
| 衛部藥陸輸字第001072號 | 癸醯環肽絲菌素 | （粉） | 誠品貿易股份有限公司 | 2027/10/07 | 抗生素 |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第024700號</td><td>可倍行注射劑</td><td>DAPTOMYCIN</td><td>2019/03/28</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 12 項交互作用，多為中度，主要包括：
  - 他汀類（Rosuvastatin、Simvastatin）：中度
  - 非類固醇消炎藥（Ibuprofen、Diclofenac、Celecoxib）：中度
  - Cyclosporine、Mycophenolic acid、Ethinylestradiol、Picosulfuric acid、Iobenguane (I-131)：中度
  - Warfarin、Dicoumarol：輕度
- **知識圖譜標示的禁忌相關疾病**（非仿單文字）：肌病變、骨骼肌疾病、家族性週期性麻痺、腹瀉性疾病、困難梭菌結腸炎、新生兒壞死性腸炎、嗜酸性肺炎、肺嗜酸性球增多症、周邊神經病變。
- 文獻中也有 Daptomycin 引起橫紋肌溶解的病例（併發急性痛風性關節炎），顯示肌肉相關安全性須留意，特別是與他汀類併用時。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗，文獻皆為骨關節「感染」研究，無法支持退化性骨關節炎的療效。作用機轉（膜去極化抗菌）與疾病病理缺乏合理連結，高分較可能來自疾病標籤重疊。
- 安全性上，肌肉毒性風險與骨關節炎常用的 NSAID、他汀類存在交互作用顧慮，在無療效證據下不宜推進。

**若要推進需要：**
- 補齊 Daptomycin 的作用機轉資料，並釐清與退化性骨關節炎病理的關聯。
- 先以細胞或動物的骨關節炎模型驗證抗發炎或軟骨保護效果。
- 若要探索免疫調節方向，類風濕性關節炎（已有膠原誘導關節炎動物證據）可能是較合理的研究問題，但仍屬早期階段。
- 若仍有興趣於骨關節領域，應將「骨關節感染」與「骨關節炎」明確區分，前者本就屬於抗生素的既有用途範疇。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

