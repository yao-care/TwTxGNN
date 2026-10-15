---
layout: default
title: Cyclizine
parent: 中證據等級 (L3-L4)
nav_order: 77
evidence_level: L4
indication_count: 9
---

# Cyclizine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **9** 個
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

# Cyclizine：從動暈症與過敏性疾患到過敏性蕁麻疹

## 一句話總結

Cyclizine（環立淨）是一種 H1 抗組織胺藥物，原本用於預防或緩解動暈症（暈車、暈船、暈機）引起的頭暈、噁心與嘔吐。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效。
目前針對此適應症**沒有臨床試驗與文獻**支持，僅有模型預測與機轉推論，且蕁麻疹本來就屬於仿單已載明的適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀 |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L4 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 9 張（有效單方 1／有效複方 0／已註銷 8） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cyclizine 屬於 H1 受體拮抗劑（抗組織胺）類藥物。阻斷組織胺受體後，可減輕組織胺引起的風團與紅斑反應，這也是蕁麻疹的主要病理機轉。

原適應症（動暈症）與新適應症（蕁麻疹）看似不同，但台灣許可證上，Cyclizine 單方產品已列有蕁麻疹、濕疹、過敏性鼻炎、支氣管氣喘等過敏性疾患的適應症。因此這項預測大致屬於**仿單內適應症**，不算是真正的藥物再利用。

需要留意的是，目前針對 Cyclizine 本身，並無蕁麻疹的試驗或文獻資料。臨床上蕁麻疹通常優先使用第二代抗組織胺。

### 其他預測適應症（TxGNN 排名 2–9）

| 排名 | 預測適應症 | 分數 | 證據等級 | 說明 |
|------|-----------|------|---------|------|
| 2 | 鼻腔疾病 (Nasal cavity disease) | 99.96% | L5 | 範圍過廣，僅有模型預測 |
| 3 | 急性喉咽炎 (Acute laryngopharyngitis) | 99.95% | L5 | 多為感染性，機轉依據不明確 |
| 4 | 寒冷性蕁麻疹 (Cold urticaria) | 99.84% | L5 | 機轉合理，但僅有預測 |
| 5 | 酒糟性結膜炎 (Rosacea conjunctivitis) | 99.75% | L5 | 病因以發炎為主，與組織胺關聯弱 |
| 6 | 頭痛疾患 (Headache disorder) | 99.49% | L4 | 僅有間接文獻 |
| 7 | 三叉自主神經性頭痛 | 99.43% | L5 | 僅可能有症狀性關聯 |
| 8 | 鼻炎 (Rhinitis) | 99.35% | L4 | 屬仿單內適應症 |
| 9 | 頑固性異位性皮膚炎 | 99.28% | L5 | 抗組織胺對頑固型療效有限 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首要預測適應症（過敏性蕁麻疹），目前無相關文獻。

以下為排名第 6 的「頭痛疾患」所檢索到的文獻，僅提供間接參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3926322](https://pubmed.ncbi.nlm.nih.gov/3926322/) | 1985 | RCT | Cephalalgia | 114 名患者隨機分組，比較 naproxen sodium 與含 cyclizine 的麥角胺複方（ergotamine 2 mg + caffeine + cyclizine 50 mg）治療急性偏頭痛發作；因 cyclizine 僅為複方成分之一，無法單獨評估其療效 |
| [20420788](https://pubmed.ncbi.nlm.nih.gov/20420788/) | 2010 | Cohort | Int J Clin Pharmacol Ther | 偏頭痛處方模式與費用的藥局資料庫分析，聚焦 triptan 類，與 cyclizine 僅間接相關 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cyclizine 的不重複許可證共 **9 張**：有效單方 1 張、有效複方 0 張、已註銷 8 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第002658號 | 旅暈平錠 | 錠劑 | 華盛頓製藥廠股份有限公司 | 2029/05/25 | 預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀。 |

<details><summary><strong>已註銷</strong>（8 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第003276號</td><td>邁可抗黴酊</td><td>CYCLIZINE HCL、SALICYLIC ACID</td><td>1986/02/04</td></tr><tr><td>內衛藥輸字第004700號</td><td>鹽酸環立淨</td><td>CYCLIZINE HCL</td><td>1985/07/12</td></tr><tr><td>衛署藥製字第022713號</td><td>肝克寧膠囊</td><td>CYCLIZINE、RIBOFLAVIN(5-PHOSPHATE SODIUM)、THIAMINE HYDROCHLOR…</td><td>1996/04/16</td></tr><tr><td>衛署藥輸字第009561號</td><td>滅暈錠</td><td>CYCLIZINE HCL</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第010504號</td><td>二苯甲基４－甲基呱/鹽酸鹽</td><td>CYCLIZINE HCL</td><td>1998/09/29</td></tr><tr><td>衛署藥輸字第011158號</td><td>邁克寧錠</td><td>CYCLIZINE HCL、CAFFEINE (HYDRATE)、ERGOTAMINE TARTRATE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第013612號</td><td>鹽酸環立淨粉劑</td><td>CYCLIZINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014591號</td><td>邁可抗黴酊</td><td>CYCLIZINE HCL、SALICYLIC ACID</td><td>1999/10/25</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示之潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單文字），主要包括：
  - 心血管：高血壓、冠狀動脈疾病、心肌梗塞、動脈粥樣硬化
  - 神經與眼科：癲癇、高眼壓
  - 代謝與內分泌：糖尿病、糖尿病酮酸中毒、甲狀腺功能低下、腎上腺皮質功能不全（Addison 病）
  - 消化與泌尿：消化性潰瘍、發炎性腸道疾病、胰臟炎、肝病、膽囊疾病、攝護腺肥大、困難梭狀芽孢桿菌結腸炎
  - 腎臟：腎臟疾病、輸尿管積膿
- **藥物交互作用**：資料庫共收錄 239 筆交互作用。
  - 嚴重（Major）：Potassium chloride、Potassium citrate
  - 中度（Moderate）：多為抗膽鹼藥物（Atropine、Scopolamine、Hyoscyamine、Dicyclomine、Glycopyrronium 等）、鴉片類（Morphine、Opium、Loperamide）、大麻素類（Dronabinol、Nabilone）及促腸胃蠕動藥物（Metoclopramide、Prucalopride）

詳細警語與禁忌請以原廠仿單為準。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（過敏性蕁麻疹）已屬仿單內適應症，並非新的再利用機會；而針對 Cyclizine 本身沒有任何臨床試驗或文獻，證據僅止於機轉推論（L4）。
- 其他預測多為 L5（僅有模型預測），且臨床上已有療效與安全性更佳的第二代抗組織胺可選用。

**若要推進需要：**
- 補齊 Cyclizine 的作用機轉資料（MOA）
- 搜尋 Cyclizine 用於蕁麻疹的直接臨床證據，並與第二代抗組織胺比較
- 確認目前有效的 3 張單方許可證所核准的適應症範圍，以及是否需要新增適應症
- 取得原廠仿單的警語與禁忌，並評估抗膽鹼作用對高風險族群（如高眼壓、攝護腺肥大、心血管疾病）的安全性影響

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測原文未改寫；證據等級與決策只依重審結果（降級或撤回）更新，原值列在下表。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原核准適應症混入其他成分與已註銷複方的適應症 | 更正（2026-10-03 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 主要製劑表列入 homochlorcyclizine、chlorcyclizine 製劑 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 對照表「已核准 (蕁麻疹)」「已核准 (偏頭痛)」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)；[emc：Valoid 50 mg Tablets（cyclizine hydrochloride）SmPC §4.1](https://www.medicines.org.uk/emc/product/4318/smpc) |
| 2026-10-03 | 蕁麻疹、鼻腔疾病、頭痛預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 蕁麻疹、鼻腔疾病、頭痛預測重審結果 | 重審：降級，證據等級 L2–L3→頭痛疾患 L4；過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病 L5；快速總覽「證據等級」：原「證據等級／L2-L3 (已有臨床使用經驗)」→「證據等級／頭痛疾患 L4；過敏性蕁麻疹、冷蕁麻疹、鼻腔疾病 L5（2026-10-03 重審降級）」；結論「整體證據等級」：原「整體證據等級／**L2-L3 (已有臨床經驗)**」→「整體證據等級／**L4**（頭痛疾患；其餘三筆 L5，2026-10-03 重審降級）」 | [PubMed：Acute migraine attack therapy: comparison of naproxen sodium and an ergotamine tartrate compound（PMID 3926322）](https://pubmed.ncbi.nlm.nih.gov/3926322/)；[PubMed：Migraine treated with an antihistamine-analgesic combination（PMID 4148490）](https://pubmed.ncbi.nlm.nih.gov/4148490/)；[PubMed：Detection of action, inhibition and augmentation spectra in solar urticaria（PMID 8573923）](https://pubmed.ncbi.nlm.nih.gov/8573923/)；[PubMed：Standard treatment: the role of antihistamines（PMID 11764306）](https://pubmed.ncbi.nlm.nih.gov/11764306/)；[PubMed：Cyclizine anaphylaxis, when administered with propanidid（PMID 5762012）](https://pubmed.ncbi.nlm.nih.gov/5762012/) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L4） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

