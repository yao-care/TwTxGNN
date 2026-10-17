---
layout: default
title: Paclitaxel
parent: 高證據等級 (L1-L2)
nav_order: 204
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-16
description: "Paclitaxel：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L1）。原適應症：卵巢癌、乳癌、非小細胞肺癌、愛滋病相關卡波西氏肉瘤"
monitor_inn: "Paclitaxel"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Paclitaxel
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Paclitaxel：從卵巢癌、乳癌與非小細胞肺癌到女性乳癌

<!-- review:begin paclitaxel-original-indication-title-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「# Paclitaxel：從 HER2 過度表現乳癌／胃癌（許可證所載）到女性乳癌」。TFDA 許可證資料中，paclitaxel 有多張有效單方許可證，例如衛署藥輸字第021157號汰癌勝注射液、衛署藥製字第044601號「永信」伏摩素注射液（晚期卵巢癌、腋下淋巴轉移之乳癌輔助化療等）、衛部藥輸字第026484號亞伯杉注射劑（轉移性乳癌、非小細胞肺癌等），以及品名為「紫杉醇」的衛署藥輸字第025586號、衛署藥陸輸字第000528號、衛部藥陸輸字第001249號（抗癌藥／抗腫瘤藥）；曲斯若、賀癌平、康癌停、赫珠瑪是 trastuzumab 類許可證，paclitaxel 只是文中的併用藥。汰癌勝、伏摩素的適應症本身也寫明「與 HERCEPTIN 併用時，用於治療未接受過化學治療之轉移性且乳癌過度表現 HER-2 之病人」，但胃癌不在 paclitaxel 的核准適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end paclitaxel-original-indication-title-2026-10-16 -->

## 一句話總結

Paclitaxel（紫杉醇）是抑制細胞有絲分裂的紫杉烷類化療藥，台灣 paclitaxel 單方許可證核准晚期卵巢癌、乳癌、非小細胞肺癌與愛滋病相關卡波西氏肉瘤（白蛋白結合型另核准胰腺癌）。
TxGNN 模型預測它對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **40 個臨床試驗**（多為含 paclitaxel 的併用方案）和 **20 篇文獻**支持這個方向。
需要說明的是，這是已被廣泛使用的既有適應症，並非真正的新用途。

<!-- review:begin paclitaxel-original-indication-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「在台灣許可證資料中主要出現在 HER2 陽性乳癌與轉移性胃癌的治療方案裡。」。TFDA 許可證資料中，paclitaxel 有多張有效單方許可證，例如衛署藥輸字第021157號汰癌勝注射液、衛署藥製字第044601號「永信」伏摩素注射液（晚期卵巢癌、腋下淋巴轉移之乳癌輔助化療等）、衛部藥輸字第026484號亞伯杉注射劑（轉移性乳癌、非小細胞肺癌等），以及品名為「紫杉醇」的衛署藥輸字第025586號、衛署藥陸輸字第000528號、衛部藥陸輸字第001249號（抗癌藥／抗腫瘤藥）；曲斯若、賀癌平、康癌停、赫珠瑪是 trastuzumab 類許可證，paclitaxel 只是文中的併用藥。汰癌勝、伏摩素的適應症本身也寫明「與 HERCEPTIN 併用時，用於治療未接受過化學治療之轉移性且乳癌過度表現 HER-2 之病人」，但胃癌不在 paclitaxel 的核准適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end paclitaxel-original-indication-summary-2026-10-16 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌、乳癌、非小細胞肺癌、愛滋病相關卡波西氏肉瘤；白蛋白結合型另核准胰腺癌 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 25 張（有效單方 14／有效複方 0／已註銷 11） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin paclitaxel-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／HER2 過度表現或 HER2 基因 amplification 之早期乳癌、轉移性乳癌，以及轉移性胃癌（取自第一張有效單方許可證；見下方說明）」。2026-10-15 報告重生後此列改寫成 trastuzumab 許可證的適應症。台灣現行 paclitaxel 許可證核准的是晚期卵巢癌、乳癌、非小細胞肺癌與愛滋病相關卡波西氏肉瘤，白蛋白結合型（亞伯杉注射劑）另核准轉移性胰腺癌；胃癌、食道癌、頭頸癌、膀胱癌、子宮頸癌不在核准適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end paclitaxel-original-indication-2026-10-03 -->

**資料說明：** 原適應症曾取自曲斯若、賀癌平、康癌停、赫珠瑪等 trastuzumab 類許可證，paclitaxel 只是文中的併用藥；paclitaxel 本身另有多張有效單方許可證（如汰癌勝、伏摩素、亞伯杉，以及品名為「紫杉醇」的衛署藥輸字第025586號等）。快速總覽的「原適應症」已改為 paclitaxel 單方許可證的核准範圍。

<!-- review:begin paclitaxel-original-indication-data-note-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「許可證中有效的 6 張，品名為曲斯若、賀癌平、康癌停、赫珠瑪，核准文字都是 trastuzumab 類製劑的適應症，paclitaxel 只是文中的併用藥。唯一以「紫杉醇」為品名的許可證已註銷，適應症僅寫「抗癌藥」。」。TFDA 許可證資料中，paclitaxel 有多張有效單方許可證，例如衛署藥輸字第021157號汰癌勝注射液、衛署藥製字第044601號「永信」伏摩素注射液（晚期卵巢癌、腋下淋巴轉移之乳癌輔助化療等）、衛部藥輸字第026484號亞伯杉注射劑（轉移性乳癌、非小細胞肺癌等），以及品名為「紫杉醇」的衛署藥輸字第025586號、衛署藥陸輸字第000528號、衛部藥陸輸字第001249號（抗癌藥／抗腫瘤藥）；曲斯若、賀癌平、康癌停、赫珠瑪是 trastuzumab 類許可證，paclitaxel 只是文中的併用藥。汰癌勝、伏摩素的適應症本身也寫明「與 HERCEPTIN 併用時，用於治療未接受過化學治療之轉移性且乳癌過度表現 HER-2 之病人」，但胃癌不在 paclitaxel 的核准適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end paclitaxel-original-indication-data-note-2026-10-16 -->

<!-- review:begin paclitaxel-original-indication-data-note-2-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「因此「原適應症」一欄反映的是併用情境，並非 paclitaxel 單方的核准範圍。」。快速總覽的「原適應症」已由查核更正改為 paclitaxel 單方許可證的核准範圍，這句不再成立。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end paclitaxel-original-indication-data-note-2-2026-10-16 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。依已知的藥理特性，paclitaxel 會穩定微管，阻止有絲分裂紡錘體解聚，使細胞停在 G2/M 期並走向凋亡，對快速分裂的乳癌細胞特別有效。

這個機轉不依賴雌激素受體或 HER2 狀態，所以乳癌各亞型（包括 ER 陰性、三陰性、荷爾蒙抗藥性乳癌）原則上都適用。許可證文字也提到，paclitaxel 與 trastuzumab 併用於 HER2 陽性乳癌，並用於 doxorubicin／cyclophosphamide 之後的輔助療法。

因此這個預測與既有臨床用法一致。TxGNN 的高分主要反映它已是乳癌的核心化療骨幹，而不是發現了新用途。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | 完成 | 50 | 每週 1 小時 paclitaxel 併用 trastuzumab，治療轉移性乳癌 |
| [NCT00002826](https://clinicaltrials.gov/study/NCT00002826) | Phase 2 | 完成 | 36 | 以 PSC 833 調節多重藥物抗藥性，併用 paclitaxel 治療復發／轉移性乳癌 |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | 未知 | 未提供 | 比較 docetaxel 或 paclitaxel 兩種給藥時程於轉移性乳癌 |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | 完成 | 652 | 紫杉烷化療搭配 lapatinib 或 trastuzumab，作為 HER2 陽性轉移性乳癌第一線治療 |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | 完成 | 455 | Neo-ALTTO：新輔助 lapatinib、trastuzumab 及兩者併用，皆加每週 paclitaxel |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | 完成 | 未提供 | Paclitaxel 加或不加 gemcitabine，用於晚期乳癌 |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | 完成 | 580 | Lapatinib 加 paclitaxel 對比單用 paclitaxel，用於第一線晚期乳癌 |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | 完成 | 478 | 劑量密集 FE75C 後接 docetaxel 對比 paclitaxel，用於淋巴結陽性乳癌的輔助化療 |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | 完成 | 280 | HER2 陽性可手術乳癌，比較兩種含 paclitaxel／trastuzumab 的新輔助順序 |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | 完成 | 632 | ETNA：新輔助 nab-paclitaxel 對比溶劑型 paclitaxel，比較病理完全緩解率 |

上表列出的是較相關的 10 個試驗。此外，TxGNN 預測的其他乳癌亞型（ER 陰性、ER 陽性、荷爾蒙抗藥性）也有多個含 paclitaxel 的試驗。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | 紫杉烷類（paclitaxel、docetaxel）為晚期乳癌、肺癌、卵巢癌的實證治療成分，paclitaxel 在美國已核准用於淋巴結陽性早期乳癌輔助治療 |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | 回顧 paclitaxel 與 docetaxel 在乳癌及卵巢癌的適應症擴展 |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | 未分類 | Cancer | 乳癌化療的發展概況，含蒽環類與紫杉烷類的角色 |
| [7904376](https://pubmed.ncbi.nlm.nih.gov/7904376/) | 1993 | Review | Semin Oncol Nurs | Paclitaxel 的開發歷程與獨特作用機轉概述 |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort | Cancer | Phase II 多中心研究，評估 doxorubicin 併用 paclitaxel 在轉移性乳癌的療效與毒性，並探討先前輔助蒽環類治療的影響 |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Cohort | Cancer | 探討 paclitaxel 在發炎性乳癌多模式治療中的角色 |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | 未分類 | Ann Oncol | 以 3 小時 paclitaxel 輸注併用 cyclophosphamide 的劑量探索，找出最大耐受劑量 |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | 未分類 | Nat Commun | TEKT4 基因變異與乳癌對 paclitaxel 的抗藥性有關 |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | 未分類 | Chem Biol Drug Des | 以患者來源模型探索 paclitaxel 組合的協同效應與體內生物標記 |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | In vitro | J Cell Physiol | ZD6474 可增強 paclitaxel 在乳癌細胞的抗增殖與促凋亡作用 |

這批文獻以綜述、世代研究與細胞實驗為主，沒有直接以 paclitaxel 為主角的 RCT 文獻。隨機對照證據主要來自上述臨床試驗。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Paclitaxel 的不重複許可證共 **25 張**：有效單方 14 張、有效複方 0 張、已註銷 11 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（14 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第044466號 | "杏輝" 輝克癒蘇注射劑６毫克/毫升 | 注射劑 | 杏輝藥品工業股份有限公司 | 2031/05/24 | 晚期卵巢癌、腋下淋巴轉移之乳癌，作為接續含杜薩魯比辛（DOXORUBICIN）在內之輔助化學療法、已使用合併療法（除非有禁忌，至少應包括使用ANTHRACYCLINE抗癌藥）失敗的… |
| 衛署藥製字第044601號 | "永信" 伏摩素注射液 | 注射劑 | 永信藥品工業股份有限公司 | 2031/08/20 | 晚期卵巢癌、腋下淋巴轉移之乳癌，作為接續含杜薩魯比辛(doxorubicin)在內之輔助化學療法、已使用合併療法（除非有禁忌，至少應包括使用anthracycline抗癌藥）失敗的… |
| 衛署藥製字第044611號 | "政德" 淨癌順注射液６毫克/毫升 | 注射劑 | 政德製藥股份有限公司 | 2031/09/05 | 晚期卵巢癌、腋下淋巴轉移之乳癌，作為接續含杜薩魯比辛（ＤＯＸＯＲＵＢＩＣＩＮ）在內之輔助化學療法、已使用合併療法（除非有禁忌、至少應包括使用ＡＮＴＨＲＡＣＹＣＬＩＮＥ抗癌藥）失敗的… |
| 衛署藥製字第044779號 | "永信" 派立達師 | （粉） | 永信藥品工業股份有限公司 | 2026/12/31 | 抗癌藥物。 |
| 衛署藥製字第045331號 | 欣沛方注射液 6 毫克/毫升 | 注射劑 | 健亞生物科技股份有限公司 | 2028/01/21 | 晚期卵巢癌、腋下淋巴轉移之乳癌，作為接續含杜薩魯比辛（DOXORUBICIN）在內之輔助化學療法、已使用合併療法（除非有禁忌，至少應包括使用ANTHRACYCLINE抗癌藥）失敗的… |
| 衛署藥製字第057266號 | "台灣神隆"倍立守 | 原料藥結晶性粉末 | 台灣神隆股份有限公司 | 2027/06/26 | 抗癌藥物。 |
| 衛署藥輸字第021157號 | 汰癌勝注射液（派立達師） | 注射劑 | 台灣大昌華嘉股份有限公司 | 2031/02/15 | 晚期卵巢癌、腋下淋巴轉移之乳癌，作為接續含杜薩魯比辛（DOXORUBICIN）在內之輔助化學療法、已使用合併療法（除非有禁忌，至少應包括使用ANTHRACYCLINE抗癌藥）失敗的… |
| 衛署藥輸字第024738號 | 癌克平注射液 | 注射劑 | 台灣費森尤斯卡比股份有限公司 | 2027/11/02 | 晚期卵巢癌、液下淋巴轉移之乳癌，作為接續含杜薩魯比辛 (DOXORUBICIN) 在內之輔助化學療法、已使用合併療法 (除非有禁忌，至少應包括使用ANTHRACYCLINE抗癌藥)… |
| 衛署藥輸字第025586號 | 紫杉醇 | （粉） | 新雙隆生技股份有限公司 | 2031/12/13 | 抗癌藥。 |
| 衛署藥陸輸字第000528號 | 紫杉醇 | （粉） | 誠品貿易股份有限公司 | 2027/09/11 | 抗癌藥。 |
| 衛部藥製字第061468號 | "台灣神隆"倍立守二代 | （粉） | 台灣神隆股份有限公司 | 2028/06/01 | 抗腫瘤用藥/ 有絲分裂抑制劑。 |
| 衛部藥輸字第026484號 | 亞伯杉注射劑 | 凍晶注射劑 | 台灣必治妥施貴寶股份有限公司 | 2030/03/19 | 轉移性乳癌 ABRAXANE用於以合併化療治療轉移疾病失敗之乳癌。除非臨床上禁用，否則先前治療應包含一種anthracycline。 非小細胞肺癌 對於無法手術或放射治療的患者，A… |
| 衛部藥輸字第027504號 | 克抑癌注射液 | 注射劑 | 凱沛爾藥品有限公司 | 2028/09/18 | 晚期卵巢癌、腋下淋巴轉移之乳癌，作為接續含杜薩魯比辛(DOXORUBICIN)在內之輔助化學療法、已使用合併療法(除非有禁忌，至少應包括使用ANTHRACYCLINE抗癌藥)失敗的… |
| 衛部藥陸輸字第001249號 | 紫杉醇 | （粉） | 台灣荃新股份有限公司 | 2030/12/19 | 抗腫瘤藥。 |

<details><summary><strong>已註銷</strong>（11 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第042226號</td><td>"永日" 派立達師</td><td>PACLITAXEL</td><td>2018/10/03</td></tr><tr><td>衛署藥製字第043023號</td><td>"健亞" 紫杉醇</td><td>PACLITAXEL</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第046429號</td><td>"天擎" 紫杉醇注射液</td><td>PACLITAXEL</td><td>2013/09/23</td></tr><tr><td>衛署藥輸字第022400號</td><td>安素泰　注射劑</td><td>PACLITAXEL</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第023396號</td><td>安莎德斯注射液</td><td>PACLITAXEL</td><td>2023/06/05</td></tr><tr><td>衛署藥輸字第024463號</td><td>搏克力濃縮輸注液6毫克/毫升</td><td>PACLITAXEL</td><td>2019/03/28</td></tr><tr><td>衛署藥輸字第024476號</td><td>帕特癌注射液6毫克/毫升</td><td>PACLITAXEL</td><td>2017/05/08</td></tr><tr><td>衛部藥輸字第027434號</td><td>"山德士"帕瘤鎖注射劑6毫克/毫升</td><td>PACLITAXEL</td><td>2024/11/22</td></tr><tr><td>衛部藥輸字第028013號</td><td>派力杉注射劑</td><td>PACLITAXEL</td><td>2025/08/26</td></tr><tr><td>衛部藥陸輸字第000692號</td><td>"漢德"紫杉醇</td><td>Paclitaxel</td><td>2022/06/21</td></tr><tr><td>衛部藥陸輸字第000843號</td><td>紫杉醇</td><td>Paclitaxel</td><td>2024/05/06</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（紫杉烷類，微管穩定劑） |
| 骨髓抑制風險 | 高（以嗜中性白血球減少最常見） |
| 致吐性分級 | 低 |
| 監測項目 | CBC（含分類）、肝功能、周邊神經病變症狀、過敏反應 |
| 處置防護 | 需依細胞毒性藥物處置規範操作，並依仿單做好過敏預防 |

以上為依藥物類別判斷的一般資訊，具體數據請參考原廠仿單的警語與注意事項。

## 安全性考量

- **藥物交互作用**：資料庫共收錄 553 筆交互作用。中度交互作用的代表藥物有 aprepitant、cimetidine、clarithromycin、clotrimazole、dexamethasone、eliglustat、metronidazole、miconazole、rolapitant、rosuvastatin、simvastatin、tinidazole、troglitazone。輕度交互作用的有 ascorbic acid、levofloxacin。
- **知識圖譜標示的疾病禁忌關聯**（來自知識圖譜，並非仿單文字，僅供參考）：嗜中性白血球減少、顆粒球缺乏症、血小板減少、貧血、周邊神經病變、肝病、腎病、心肌梗塞、猝死性心臟停止、高膽紅素血症（含 Gilbert 症候群）、氣喘、糖尿病（含酮酸中毒）、低血壓、乾癬等。實際禁忌請以原廠仿單為準。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 乳癌有多個已完成的 Phase 3 隨機試驗，納入含 paclitaxel 的方案，且 paclitaxel 已是乳癌臨床標準化療骨幹，因此預測高度合理。
- 這不算真正的藥物再利用，而是既有適應症的確認。同時，台灣 paclitaxel 單方仍有多張有效許可證（如汰癌勝、伏摩素、亞伯杉），實際供應與給付狀況可另行確認。

<!-- review:begin paclitaxel-original-indication-conclusion-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「同時，台灣有效許可證都是 trastuzumab 類製劑，以 paclitaxel 為品名的許可證已註銷，需要釐清實際供應與給付狀況。」。TFDA 許可證資料中，paclitaxel 有多張有效單方許可證，例如衛署藥輸字第021157號汰癌勝注射液、衛署藥製字第044601號「永信」伏摩素注射液（晚期卵巢癌、腋下淋巴轉移之乳癌輔助化療等）、衛部藥輸字第026484號亞伯杉注射劑（轉移性乳癌、非小細胞肺癌等），以及品名為「紫杉醇」的衛署藥輸字第025586號、衛署藥陸輸字第000528號、衛部藥陸輸字第001249號（抗癌藥／抗腫瘤藥）；曲斯若、賀癌平、康癌停、赫珠瑪是 trastuzumab 類許可證，paclitaxel 只是文中的併用藥。汰癌勝、伏摩素的適應症本身也寫明「與 HERCEPTIN 併用時，用於治療未接受過化學治療之轉移性且乳癌過度表現 HER-2 之病人」，但胃癌不在 paclitaxel 的核准適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end paclitaxel-original-indication-conclusion-2026-10-16 -->

**若要推進需要：**
- 釐清台灣目前 paclitaxel 單方（含 nab-paclitaxel 等劑型）的有效許可證與核准適應症
- 取得 paclitaxel 的作用機轉（MOA）資料，補足機轉分析
- 補充仿單的警語與禁忌資料（過敏反應預防、骨髓抑制與神經毒性監測）
- 針對 ER 陰性、荷爾蒙抗藥性等亞型，整理以 paclitaxel 為主的直接證據
- 建立併用藥（如 CYP3A4／CYP2C8 抑制劑）的交互作用管理計畫

<!-- review:begin paclitaxel-original-indication-next-step-2026-10-16 -->

> **查核加註（2026-10-16）**：TFDA 許可證資料中，paclitaxel 有多張有效單方許可證，例如衛署藥輸字第021157號汰癌勝注射液、衛署藥製字第044601號「永信」伏摩素注射液（晚期卵巢癌、腋下淋巴轉移之乳癌輔助化療等）、衛部藥輸字第026484號亞伯杉注射劑（轉移性乳癌、非小細胞肺癌等），以及品名為「紫杉醇」的衛署藥輸字第025586號、衛署藥陸輸字第000528號、衛部藥陸輸字第001249號（抗癌藥／抗腫瘤藥）；曲斯若、賀癌平、康癌停、赫珠瑪是 trastuzumab 類許可證，paclitaxel 只是文中的併用藥。汰癌勝、伏摩素的適應症本身也寫明「與 HERCEPTIN 併用時，用於治療未接受過化學治療之轉移性且乳癌過度表現 HER-2 之病人」，但胃癌不在 paclitaxel 的核准適應症內。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end paclitaxel-original-indication-next-step-2026-10-16 -->

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原適應症取自 trastuzumab 類許可證 | 更正（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L1） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |
| 2026-10-16 | 標題以 trastuzumab 許可證的適應症為原用途 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結以 trastuzumab 許可證的適應症為原用途 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 資料說明稱有效許可證都是 trastuzumab 類、紫杉醇品名已註銷 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 結論稱台灣有效許可證都是 trastuzumab 類 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 預測理由引用 trastuzumab 許可證文字 | 查核撤回（2026-10-16：查核判斷有誤：paclitaxel 本身的有效單方許可證（衛署藥輸字第021157號汰癌勝、衛署藥製字第044601號伏摩素）就寫明「與 HERCEPTIN 併用時，用於治療未接受過化學治療之轉移性且乳癌過度表現 HER-2 之病人」，這段許可證文字不是只出自 trastuzumab 許可證；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 下一步建議另行釐清 paclitaxel 單方許可證 | 加註（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 資料說明稱原適應症欄反映併用情境 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

