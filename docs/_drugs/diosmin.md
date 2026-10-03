---
layout: default
title: Diosmin
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 1
---

# Diosmin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Diosmin (地奧司明) - 藥師評估報告

## 一句話總結

Diosmin 是一種類黃酮靜脈活性劑，用於慢性靜脈功能不全和痔瘡；TxGNN 僅預測出一項新適應症（閉經），但分數較低且缺乏任何臨床或文獻支持，老藥新用潛力極為有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Diosmin (地奧司明/香葉木素芸香糖苷) |
| DrugBank ID | DB08995 |
| 台灣商品名 | 艾歐復隆膜衣錠、迪歐明膜衣錠、淨脈舒膜衣錠等 |
| 原適應症 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解（衛部藥製字第060902號等）；靜脈曲張與痔瘡用藥（原料藥，衛部藥陸輸字第001111號） |
| 預測新適應症 | 閉經 (amenorrhea) |
| 最高 TxGNN 分數 | 0.9942 |
| 臨床試驗支持 | 無 |
| 文獻支持 | 無 |

<!-- review:begin diosmin-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／慢性靜脈功能不全、靜脈曲張、痔瘡、機能性月經過多」。台灣現行 diosmin 許可證的適應症為「協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解」（原料藥另載靜脈曲張與痔瘡用藥），不含機能性月經過多。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end diosmin-original-indication-2026-10-03 -->

<!-- review:begin diosmin-amenorrhea-rereview-result-2026-10-03 -->

> **重審結果（2026-10-03）**：**撤回**（證據等級 L5 不變）。原推論中唯一跟本藥有關的理由「原適應症含機能性月經過多症」與台灣許可證不符，剩下的只是血管保護作用可能影響子宮內膜血流的理論推測，原文也寫明機轉連結極為薄弱。PubMed 與 ClinicalTrials.gov 都查無 diosmin 用於閉經的研究。最接近的人體資料是異常子宮出血：diosmin 合併 tranexamic acid 與 mefenamic acid 的隨機對照試驗中，經血量與出血天數減少得更多（[PMID 38029032](https://pubmed.ncbi.nlm.nih.gov/38029032/)），作用方向是減少經血，與閉經的需求相反。大鼠研究顯示 diosmin 可減輕 cyclophosphamide 造成的卵巢損傷（[PMID 33802633](https://pubmed.ncbi.nlm.nih.gov/33802633/)），但沒有評估月經，不能當作閉經的證據。本頁結論「證據等級總結」閉經列已依重審結果更新，原值列在下方查核紀錄。依據：[PubMed：To Study the Efficacy and Safety of Diosmin with Tranexamic Acid and Mefenamic Acid Versus only Tranexamic Acid and Mefenamic Acid in Medical Management of Abnormal Uterine Bleeding: A Randomized Controlled Trial（PMID 38029032）](https://pubmed.ncbi.nlm.nih.gov/38029032/)；[PubMed：Treatment of abnormal uterine bleeding with micronized flavonoids（PMID 15847886）](https://pubmed.ncbi.nlm.nih.gov/15847886/)；[ClinicalTrials.gov：Oral Tranexamic Acid Versus Diosmin for Treatment of Menorrhagia in Women Using Copper IUD（NCT02616731）](https://clinicaltrials.gov/study/NCT02616731)；[PubMed：Diosmin Mitigates Cyclophosphamide Induced Premature Ovarian Insufficiency in Rat Model（PMID 33802633）](https://pubmed.ncbi.nlm.nih.gov/33802633/)；[ClinicalTrials.gov：Evaluation of the Effects of Diosmin/Hespiridin Combination on the Clinical Outcomes in Patients With Polycystic Ovary Syndrome（NCT06083935）](https://clinicaltrials.gov/study/NCT06083935)。

<!-- review:end diosmin-amenorrhea-rereview-result-2026-10-03 -->

## 為什麼預測合理

### 機轉分析

1. **閉經 (amenorrhea)**：
   - TxGNN 分數 0.9942，排名 10904（較低）
   - Diosmin 的原適應症包含「機能性月經過多症」，是一種影響月經的藥物
   - 理論上，具有血管保護和抗發炎作用的藥物可能影響子宮內膜血流
   - 但從「月經過多」到「閉經」的機轉連結極為薄弱
   - 閉經通常由荷爾蒙失調、下視丘-腦垂體-卵巢軸問題或解剖異常引起，與靜脈活性劑的作用無直接關聯

<!-- review:begin diosmin-amenorrhea-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：台灣現行 diosmin 許可證的適應症只有慢性靜脈功能不全引起之腫脹疼痛與痔瘡症狀（原料藥另載靜脈曲張），沒有「機能性月經過多症」，這項推論前提與許可證不符。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end diosmin-amenorrhea-premise-2026-10-03 -->

### 預測品質評估

- 僅有一項預測適應症，顯示 TxGNN 對此藥物的預測能力有限
- 預測分數相對較低（0.99 以下門檻邊緣）
- 無任何臨床試驗或文獻支持
- 機轉連結薄弱

## 臨床試驗

**無相關臨床試驗**

ClinicalTrials.gov 和 WHO ICTRP 均未發現 diosmin 用於閉經的臨床試驗。

## 文獻證據

**無相關文獻**

PubMed 搜尋未發現 diosmin 與閉經治療相關的文獻。

## 台灣上市狀態

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Diosmin 的不重複許可證共 **8 張**：有效單方 8 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（8 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥製字第060902號 | 法迪朗膜衣錠500毫克 | 膜衣錠 | 法諾亞生技藥品股份有限公司 | 2031/06/10 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解。 |
| 衛部藥製字第061185號 | 迪歐明膜衣錠500毫克 | 膜衣錠 | 黃氏製藥股份有限公司 | 2027/12/01 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解。 |
| 衛部藥製字第061418號 | 淨脈舒膜衣錠500毫克 | 膜衣錠 | 易陞植物生技有限公司 | 2028/02/07 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解。 |
| 衛部藥製字第061424號 | 治昌優膜衣錠500毫克 | 膜衣錠 | 瑩碩生技醫藥股份有限公司 | 2028/03/01 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解。 |
| 衛部藥輸字第026665號 | 艾歐復隆膜衣錠500毫克 | 膜衣錠 | 美時化學製藥股份有限公司 | 2031/01/28 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解 。 |
| 衛部藥輸字第027992號 | 地奧司明 | （粉） | 宇直泰貿易股份有限公司 | 2030/11/18 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解 |
| 衛部藥陸輸字第001025號 | 香葉木素芸香糖苷 | （粉） | 東譽興業股份有限公司 | 2031/10/15 | 協助改善慢性靜脈功能不全引起之局部腫脹或疼痛、痔瘡症狀之緩解。 |
| 衛部藥陸輸字第001111號 | 香葉木苷 | （粉） | 誠品貿易股份有限公司 | 2028/07/14 | 靜脈曲張與痔瘡用藥。 |

<!-- tfda-licenses:end -->

**現況**：台灣有多項有效許可證，近年有多家廠商新取得許可，市場競爭活躍。

## 安全性

### 藥物交互作用

**無已知重大藥物交互作用**

DDInter 資料庫未記錄 diosmin 的顯著藥物交互作用。

### 一般安全性

Diosmin 的安全性良好：
- 常見副作用：輕微腸胃不適
- 罕見副作用：頭痛、皮疹
- 禁忌症：對此藥過敏者

## 結論

### 整體評估：極低優先級

Diosmin 的 TxGNN 預測極為有限，僅有一項新適應症（閉經），且完全缺乏機轉支持和臨床證據。此藥物應維持其作為靜脈活性劑的傳統角色，不建議投入資源研究新適應症。

### 建議

1. **不建議**進行任何老藥新用研究
2. 維持其作為慢性靜脈功能不全和痔瘡治療的角色
3. TxGNN 對此藥物的預測能力受限，可能是因為其在知識圖譜中的連結較少

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 閉經 | 0.9942 | 無 | 無 | 極低 | 撤回（2026-10-03 重審） |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測原文未改寫；證據等級與決策只依重審結果（降級或撤回）更新，原值列在下表。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 法迪朗膜衣錠許可證效期 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 香葉木素芸香糖苷許可證效期 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症列入已註銷證的「機能性月經過多」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 閉經預測理由引用「機能性月經過多症」為原適應症 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 閉經預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 閉經預測重審結果 | 重審：撤回，證據等級 L5 不變；結論「證據等級總結」閉經列：原「閉經／0.9942／無／無／極低／不推薦」→「閉經／0.9942／無／無／極低／撤回（2026-10-03 重審）」 | [PubMed：To Study the Efficacy and Safety of Diosmin with Tranexamic Acid and Mefenamic Acid Versus only Tranexamic Acid and Mefenamic Acid in Medical Management of Abnormal Uterine Bleeding: A Randomized Controlled Trial（PMID 38029032）](https://pubmed.ncbi.nlm.nih.gov/38029032/)；[PubMed：Treatment of abnormal uterine bleeding with micronized flavonoids（PMID 15847886）](https://pubmed.ncbi.nlm.nih.gov/15847886/)；[ClinicalTrials.gov：Oral Tranexamic Acid Versus Diosmin for Treatment of Menorrhagia in Women Using Copper IUD（NCT02616731）](https://clinicaltrials.gov/study/NCT02616731)；[PubMed：Diosmin Mitigates Cyclophosphamide Induced Premature Ovarian Insufficiency in Rat Model（PMID 33802633）](https://pubmed.ncbi.nlm.nih.gov/33802633/)；[ClinicalTrials.gov：Evaluation of the Effects of Diosmin/Hespiridin Combination on the Clinical Outcomes in Patients With Polycystic Ovary Syndrome（NCT06083935）](https://clinicaltrials.gov/study/NCT06083935) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

