---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Aliskiren：預測新適應症為肺疾病及（或）缺氧所致的肺高壓 (pulmonary hypertension owing to lung disease and/or…（證據等級 L4）。原適應症：高血壓"
monitor_inn: "aliskiren"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "cerebrovascular disorder"]
---

# Aliskiren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Aliskiren：肺疾病及（或）缺氧所致的肺高壓
{: .text-alpha }

## 一句話總結

Aliskiren 是直接腎素抑制劑，在台灣原本用於治療高血壓。
TxGNN 模型預測它可能對**肺疾病及（或）缺氧所致的肺高壓 (pulmonary hypertension owing to lung disease and/or hypoxia)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇相關的動物實驗文獻**，證據仍屬早期的研究問題階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（台灣目前有效的許可證皆為複方，適應症為無法以 aliskiren 或 hydrochlorothiazide 單一療法控制血壓的高血壓） |
| 預測新適應症 | 肺疾病及（或）缺氧所致的肺高壓 (pulmonary hypertension owing to lung disease and/or hypoxia) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 台灣上市 | 未上市（已註銷許可證 15 張／共 15 張） |
| 許可證數 | 15 張（有效單方 0／有效複方 0／已註銷 15） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，aliskiren 直接抑制腎素 (renin)，也就是腎素-血管收縮素系統 (RAS) 的限速步驟，因此能降低血管收縮素 II。

間歇性缺氧的前臨床模型顯示，血管收縮素 II 與交感神經過度興奮、血管及心房重塑有關。例如大鼠慢性間歇性缺氧模型中，aliskiren 可能對心房重塑有保護作用。這是原適應症（高血壓）與預測適應症（缺氧相關肺高壓）在機轉上的可能連結。

不過目前沒有任何人體肺高壓資料。此外，aliskiren 會降低血壓，對缺氧患者可能造成全身性低血壓，這是需要特別留意的安全疑慮。以上推論目前仍屬假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32982180](https://pubmed.ncbi.nlm.nih.gov/32982180/) | 2020 | 動物實驗 | Drug Des Devel Ther | 在慢性間歇性缺氧大鼠模型中探討 aliskiren 對心房重塑的潛在作用；aliskiren 作為直接腎素抑制劑，先前已顯示有抗心律不整的保護效果 |
| [29645283](https://pubmed.ncbi.nlm.nih.gov/29645283/) | 2018 | 動物實驗 | J Physiol | 間歇性缺氧後的交感神經興奮與循環血管收縮素 II 有關，抑制 RAS 可預防此效應（間接支持，未直接使用 aliskiren） |
| [39133776](https://pubmed.ncbi.nlm.nih.gov/39133776/) | 2024 | 體外研究 | Am J Physiol Regul Integr Comp Physiol | 探討腦部血管收縮素 II 的釋放，與肺高壓關聯較遠 |
| [26502369](https://pubmed.ncbi.nlm.nih.gov/26502369/) | 2016 | 體外研究 | Transplantation | 鈣調神經磷酸酶抑制劑使腎集合管局部腎素上調，與肺高壓關聯較遠 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Aliskiren 的不重複許可證共 **15 張**：有效單方 0 張、有效複方 0 張、已註銷 15 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（15 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第024883號</td><td>絡舒樂適膜衣錠 300 毫克</td><td>ALISKIREN HEMIFUMARATE</td><td>2025/06/11</td></tr><tr><td>衛署藥輸字第024884號</td><td>絡舒樂適膜衣錠 150 毫克</td><td>ALISKIREN HEMIFUMARATE</td><td>2025/06/11</td></tr><tr><td>衛署藥輸字第025161號</td><td>絡舒利適150/25毫克膜衣錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、ALISKI…</td><td></td></tr><tr><td>衛署藥輸字第025162號</td><td>絡舒利適150/12.5毫克膜衣錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、ALISKI…</td><td></td></tr><tr><td>衛署藥輸字第025163號</td><td>絡舒利適300/12.5毫克膜衣錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、ALISKI…</td><td></td></tr><tr><td>衛署藥輸字第025164號</td><td>絡舒利適300/25毫克膜衣錠</td><td>ALISKIREN HEMIFUMARATE、HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDR…</td><td></td></tr><tr><td>衛署藥輸字第025700號</td><td>絡舒優適 150/5 毫克膜衣錠</td><td>AMLODIPINE BESYLATE、ALISKIREN HEMIFUMARATE</td><td>2017/03/20</td></tr><tr><td>衛署藥輸字第025701號</td><td>絡舒優適 150/10 毫克膜衣錠</td><td>AMLODIPINE BESYLATE、ALISKIREN HEMIFUMARATE</td><td>2017/03/20</td></tr><tr><td>衛署藥輸字第025702號</td><td>絡舒優適 300/5 毫克膜衣錠</td><td>AMLODIPINE BESYLATE、ALISKIREN HEMIFUMARATE</td><td>2017/03/20</td></tr><tr><td>衛署藥輸字第025703號</td><td>絡舒優適 300/10 毫克膜衣錠</td><td>AMLODIPINE BESYLATE、ALISKIREN HEMIFUMARATE</td><td>2017/03/20</td></tr><tr><td>衛署藥輸字第025944號</td><td>絡舒安適300/10/25 毫克膜衣錠</td><td>ALISKIREN HEMIFUMARATE、HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDR…</td><td>2017/03/01</td></tr><tr><td>衛署藥輸字第025945號</td><td>絡舒安適300/10/12.5 毫克膜衣錠</td><td>ALISKIREN HEMIFUMARATE、AMLODIPINE BESYLATE、HYDROCHLOROTHIAZI…</td><td>2017/03/01</td></tr><tr><td>衛署藥輸字第025946號</td><td>絡舒安適300/5/25 毫克膜衣錠</td><td>AMLODIPINE BESYLATE、HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCH…</td><td>2017/03/01</td></tr><tr><td>衛署藥輸字第025947號</td><td>絡舒安適300/5/12.5 毫克膜衣錠</td><td>ALISKIREN HEMIFUMARATE、AMLODIPINE BESYLATE、HYDROCHLOROTHIAZI…</td><td>2017/03/01</td></tr><tr><td>衛署藥輸字第025948號</td><td>絡舒安適150/5/12.5 毫克膜衣錠</td><td>AMLODIPINE BESYLATE、HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCH…</td><td>2017/03/01</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 114 筆交互作用，以下為部分中度等級的例子：
  - 皮質類固醇類：hydrocortisone、prednisolone、prednisone、dexamethasone、betamethasone、budesonide
  - SGLT2 抑制劑：canagliflozin、dapagliflozin、empagliflozin、ertugliflozin
  - 鉀補充劑：potassium chloride、potassium citrate、potassium bicarbonate、potassium gluconate
  - 其他：acetylsalicylic acid、aprepitant、clarithromycin、clotrimazole、miconazole、eliglustat
- **知識圖譜標示的潛在禁忌疾病**（來自藥物-疾病關聯資料，非仿單文字）：血管性水腫（含遺傳性、後天性及 RAAS 阻斷劑誘發）、肝衰竭／肝病／肝昏迷／肝性腦病變、胰臟炎、膽囊疾病、全身性紅斑狼瘡、缺鉀、糖尿病及糖尿病酮酸中毒、痛風、高鈣血症、腎鈣質沉著症、嗜中性白血球減少、顆粒性白血球缺乏症、低血壓、無尿、腎動脈阻塞、腎功能不全等。
- **與預測適應症相關的特別提醒**：缺氧患者使用降壓藥可能出現全身性低血壓。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，但目前沒有任何臨床試驗，僅有少數大鼠缺氧模型的前臨床研究，且無人體肺高壓資料，證據停留在 L4。
- 缺氧患者使用降壓藥有低血壓風險，在缺乏療效證據下不宜推進臨床應用。

**若要推進需要：**
- 補充 aliskiren 的作用機轉資料（MOA）。
- 在肺高壓動物模型（如缺氧誘發肺高壓）中直接驗證 aliskiren 對肺血管壓力與重塑的影響。
- 評估低血壓、高血鉀與腎功能風險，並確認與現行肺高壓標準治療的交互作用。
- 若前臨床結果正向，再規劃小規模探索性臨床研究。

## 其他排序較後的預測（僅供參考）

| 預測適應症 | 證據等級 | 說明 |
|-----------|---------|------|
| 腦血管疾病 (cerebrovascular disorder) | L5 | 有 1 個提前終止的 Phase 2/3 動脈粥狀硬化影像試驗（NCT01417104，71 人）及多篇動物中風模型研究，無人體腦血管結局試驗；ALTITUDE 試驗曾出現低血壓與缺血性中風的疑慮 |
| 惡性腎血管性高血壓 | L4 | 機轉合理，但僅有敘述性文獻回顧，且反應性腎素分泌可能限制療效 |
| 惡性高血壓腎病變 | L5 | 僅有間接文獻，無 aliskiren 直接證據 |
| 慢性肺心病 | L5 | 僅為模型預測與間接文獻 |
| 原因不明的多因素肺高壓、Braddock 症候群 | L5 | 僅有模型預測，無相關試驗或文獻 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

