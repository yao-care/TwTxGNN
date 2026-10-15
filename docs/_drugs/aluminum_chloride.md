---
layout: default
title: Aluminum Chloride
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Aluminum Chloride
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

# Aluminum chloride：從多汗症到脂漏性角化症

## 一句話總結

Aluminum chloride（氯化鋁）是外用止汗收斂劑，在台灣原本核准用於**抗多汗**。
TxGNN 模型預測它可能對**脂漏性角化症 (Seborrheic Keratosis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗多汗 |
| 預測新適應症 | 脂漏性角化症 (Seborrheic Keratosis) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 1／有效複方 0／已註銷 3） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，氯化鋁是外用收斂劑與蛋白質沉澱劑，能阻塞汗腺導管而減少出汗，並已有研究顯示它會誘導角質形成細胞凋亡及角化異常。

不過，這些特性與脂漏性角化症（一種良性表皮增生病灶）之間並沒有文獻或臨床資料證實的關聯。這項預測目前只是 TxGNN 模型的推論，原適應症（多汗）與預測新適應症的相似度尚待評估，機轉上是否適用仍屬未知。

此外，同一份預測清單中，分數接近的其他項目（如先天性凝血酶原缺乏症、痤瘡）在機轉上更難以成立，顯示高分並不等於生物學上合理，解讀時需保守。

## 臨床試驗證據

針對脂漏性角化症本身，目前無相關臨床試驗登記。

下列為模型排名第 6 的較廣泛預測「皮膚疾病」所對應的試驗，僅供參考，不能視為支持脂漏性角化症的證據：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02028208](https://clinicaltrials.gov/study/NCT02028208) | Phase 2 | 完成 | 56 | 汞、鋁、鈀金屬過敏原斑貼試驗劑量反應研究，屬鋁的皮膚反應（安全性訊號），非治療效益 |
| [NCT03416348](https://clinicaltrials.gov/study/NCT03416348) | Phase 1 | 完成 | 95 | 截肢者殘肢多汗症的治療流程研究，該適應症已是核准用途 |
| [NCT07401277](https://clinicaltrials.gov/study/NCT07401277) | Phase 1 | 招募中 | 32 | 5-氟尿嘧啶加鋁用於光線性角化症的探索性研究，鋁的形式與角色尚不明確 |

## 文獻證據

針對脂漏性角化症本身，目前無相關文獻。

下列為「皮膚疾病」預測項下的文獻（精選），多數與多汗症或鋁的皮膚反應有關：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30710603](https://pubmed.ncbi.nlm.nih.gov/30710603/) | 2019 | Review | J Am Acad Dermatol | 止汗劑為原發性局部多汗症的第一線治療 |
| [25152341](https://pubmed.ncbi.nlm.nih.gov/25152341/) | 2014 | Review | Dermatol Clin | 鋁鹽藉由在汗腺導管形成栓塞而發揮作用 |
| [30215934](https://pubmed.ncbi.nlm.nih.gov/30215934/) | 2018 | Review | Am Fam Physician | 多汗症的處置選項 |
| [41839170](https://pubmed.ncbi.nlm.nih.gov/41839170/) | 2026 | Review | Skin Therapy Letter | 氯化鋁六水合物為多汗症的傳統藥物，並回顧新療法 |
| [35029347](https://pubmed.ncbi.nlm.nih.gov/35029347/) | 2022 | Review | Dermatitis | 鋁過敏的臨床表現包括搔癢性皮下結節與濕疹樣皮膚炎 |
| [31567135](https://pubmed.ncbi.nlm.nih.gov/31567135/) | 2020 | Case series | Am J Dermatopathol | 小鼠塗抹 20% 氯化鋁會引發細胞凋亡、角化停滯與顆粒性角化不全 |
| [37142953](https://pubmed.ncbi.nlm.nih.gov/37142953/) | 2023 | 單臂試驗 | BMC Cancer | 外用氯化鋁用於瑞戈非尼相關的嚴重手足皮膚反應 |
| [40396355](https://pubmed.ncbi.nlm.nih.gov/40396355/) | 2025 | 比較研究 | J Cutan Med Surg | 比較氯化鋁、oxybutynin 與肉毒桿菌毒素治療原發性局部多汗症 |
| [3771053](https://pubmed.ncbi.nlm.nih.gov/3771053/) | 1986 | 個案報告 | Int J Dermatol | 20% 氯化鋁乙醇溶液對 Frey 氏症候群個案有效 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Aluminum Chloride 的不重複許可證共 **4 張**：有效單方 1 張、有效複方 0 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第043123號 | 克狐　止汗劑〝汎生〞 | 外用液劑 | 臺灣汎生製藥廠股份有限公司 | 2029/07/23 | 抗多汗。 |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第009014號</td><td>純露糖漿</td><td>CHLORPHENIRAMINE MALEATE、ALUMINUM CHLORIDE、POTASSIUM GUAIACO…</td><td>2023/07/24</td></tr><tr><td>衛署藥輸字第009331號</td><td>牙齦止血液</td><td>ALUMINUM CHLORIDE HYDRATED、OXYQUINOLINE SULFATE</td><td>1987/08/29</td></tr><tr><td>衛署藥輸字第009332號</td><td>牙齦收縮止血劑</td><td>ALUMINUM CHLORIDE HYDRATED、OXYQUINOLINE SULFATE、LIDOCAINE</td><td>1987/08/29</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**：皮疹 (exanthem)、皮膚炎 (dermatitis)。此資訊來自模型知識圖譜，並非仿單內容。
- **文獻中的安全訊號**：鋁可能引起接觸性過敏（搔癢性結節、濕疹樣皮膚炎），動物研究顯示高濃度外用可造成角化異常。
- **藥物交互作用**：查無相關資料。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 脂漏性角化症的預測僅有模型分數，無任何臨床試驗或文獻支持（L5），也沒有機轉依據。
- 氯化鋁可能引起皮膚刺激與接觸性過敏，且知識圖譜顯示對皮膚炎、皮疹屬禁忌，風險效益尚不明朗。

**若要推進需要：**
- 補齊氯化鋁的作用機轉資料，並建立其與脂漏性角化症的機轉關聯
- 進行前臨床或小規模探索性研究，評估對該病灶的實際效果
- 釐清外用安全性，特別是皮膚刺激與過敏風險
- 評估劑型與給藥途徑的相容性（目前尚待確認）
- 若要探索其他方向，可優先關注已有初步訊號的皮膚相關議題（如手足皮膚反應、光線性角化症的後續試驗結果）

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「牙齦止血液」「牙齦收縮止血劑」「純露糖漿」三列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L3） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

