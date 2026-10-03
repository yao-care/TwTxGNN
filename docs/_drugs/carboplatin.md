---
layout: default
title: Carboplatin
parent: 高證據等級 (L1-L2)
nav_order: 53
evidence_level: L2
indication_count: 10
---

# Carboplatin
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

# Carboplatin：從化療基石到女性乳腺癌的新探索

## 一句話總結

Carboplatin 是鉑類抗癌藥物，已廣泛用於多種癌症治療。
TxGNN 模型預測它可能對**女性乳腺癌 (female breast carcinoma)** 有效，
目前有超過 **50 個臨床試驗**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌（台灣許可證核准適應症） |
| 預測新適應症 | 女性乳腺癌 (female breast carcinoma) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2 |
| 台灣上市 | 已上市（為多種複方治療的一部分） |
| 許可證數 | 16 張（有效單方 3／有效複方 0／已註銷 13） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin carboplatin-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／HER2 陽性早期乳癌、轉移性乳癌、黑色素瘤、非小細胞肺癌、何杰金氏淋巴瘤、頭頸部鱗狀細胞癌、泌尿道上皮癌等」。原文列的是 trastuzumab、pembrolizumab 等其他藥品許可證中與 carboplatin 併用的適應症；台灣有效的 carboplatin 許可證（衛署藥輸字第024074號佳鉑帝、第024804號爾定康、衛署藥製字第057314號杏輝剋鉑停）核准適應症都是「卵巢癌」。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end carboplatin-original-indication-2026-10-03 -->

## 為什麼這個預測合理？

Carboplatin 是一種鉑類抗癌藥物，透過與 DNA 形成交叉連結來抑制腫瘤細胞增殖。其作用機轉包括：

1. **DNA 損傷機制**：Carboplatin 與 DNA 形成鉑-DNA 加合物，干擾 DNA 複製與轉錄
2. **細胞週期阻滯**：誘導細胞週期停滯，促進腫瘤細胞凋亡
3. **對三陰性乳腺癌的特殊療效**：研究顯示 carboplatin 對 BRCA 突變相關的三陰性乳腺癌具有良好療效

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | ACTIVE_NOT_RECRUITING | 36 | 評估 trilaciclib、pembrolizumab、gemcitabine 和 carboplatin 在轉移性三陰性乳腺癌中的療效 |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | COMPLETED | 263 | 比較 docetaxel/trastuzumab 與 docetaxel/carboplatin/trastuzumab 在 HER2 陽性轉移性乳腺癌的療效 |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | COMPLETED | 191 | 評估 nab-paclitaxel 與 gemcitabine 或 carboplatin 在三陰性轉移性乳腺癌的療效 |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | COMPLETED | 101 | 評估含 carboplatin 化療方案在三陰性乳腺癌新輔助治療中的病理完全緩解率 |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | COMPLETED | 103 | 研究 PARP 抑制劑 AZD2281 與 carboplatin 併用在 BRCA1/2 突變攜帶者乳腺癌中的安全性 |

## 文獻證據

Carboplatin 在乳腺癌治療中的應用已有多項研究支持，尤其在以下領域：

1. **三陰性乳腺癌 (TNBC)**：多項臨床試驗顯示 carboplatin 可提高 TNBC 的病理完全緩解率
2. **BRCA 突變相關乳腺癌**：carboplatin 對 DNA 修復缺陷的腫瘤細胞具有較高敏感性
3. **HER2 陽性乳腺癌**：與 trastuzumab 併用已被證實有效

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Carboplatin 的不重複許可證共 **16 張**：有效單方 3 張、有效複方 0 張、已註銷 13 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第057314號 | "杏輝"剋鉑停靜脈注射液10毫克/毫升 | 注射劑 | 杏輝藥品工業股份有限公司 | 2027/07/30 | 卵巢癌。 |
| 衛署藥輸字第024074號 | 佳鉑帝靜脈注射液 | 注射液劑 | 台灣大昌華嘉股份有限公司 | 2029/09/29 | 卵巢癌。 |
| 衛署藥輸字第024804號 | 爾定康靜脈注射液 | 注射劑 | 台灣費森尤斯卡比股份有限公司 | 2028/03/17 | 卵巢癌。 |

<details><summary><strong>已註銷</strong>（13 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第017782號</td><td>佳鉑帝注射液</td><td>CARBOPLATIN、CARBOPLATIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第018696號</td><td>佳鉑帝凍晶注射劑</td><td>CARBOPLATIN、CARBOPLATIN、CARBOPLATIN</td><td>2008/12/22</td></tr><tr><td>衛署藥輸字第018768號</td><td>佳鉑帝注射液</td><td>CARBOPLATIN、WATER DISTILLED FOR INJECTION</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第020725號</td><td>卡伯拉丁注射液</td><td>CARBOPLATIN</td><td>1997/09/01</td></tr><tr><td>衛署藥輸字第020966號</td><td>克本瘤注射液</td><td>CARBOPLATIN</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第021047號</td><td>克本瘤注射液１０公絲/公撮</td><td>CARBOPLATIN</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第021701號</td><td>卡伯拉丁注射液</td><td>CARBOPLATIN</td><td>2022/09/22</td></tr><tr><td>衛署藥輸字第023368號</td><td>克鉑定 "立可用安全型注射液"</td><td>CARBOPLATIN</td><td>2022/06/30</td></tr><tr><td>衛署藥輸字第024591號</td><td>貝福卡鉑靜脈注射液10毫克/毫升</td><td>CARBOPLATIN</td><td>2014/04/08</td></tr><tr><td>衛署藥輸字第025626號</td><td>卡蒲鉑定"山德士"注射劑10毫克/毫升</td><td>CARBOPLATIN</td><td>2021/07/05</td></tr><tr><td>衛部藥輸字第026387號</td><td>艾鉑霆靜脈注射液10毫克/毫升</td><td>CARBOPLATIN</td><td>2026/08/12</td></tr><tr><td>衛部藥輸字第027083號</td><td>可鉑注射液10毫克/毫升</td><td>CARBOPLATIN</td><td>2026/02/02</td></tr><tr><td>衛部藥陸輸字第000936號</td><td>卡鉑定</td><td>Carboplatin</td><td>2026/06/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物 |
| 骨髓抑制風險 | 高度（血小板減少為劑量限制毒性） |
| 致吐性分級 | 中度至高度 |
| 監測項目 | CBC（含分類）、腎功能（肌酸酐清除率）、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

**重要警語**：
- Carboplatin 主要經腎臟排泄，腎功能不全患者需調整劑量
- 骨髓抑制為主要毒性，需定期監測血球計數
- 可能引起過敏反應，尤其是多次使用後

**藥物交互作用**：
- 與其他骨髓抑制藥物併用可能增加血液毒性
- 與腎毒性藥物（如 aminoglycoside 抗生素）併用需謹慎
- 避免與活性疫苗同時使用

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Carboplatin 在乳腺癌治療中已有大量臨床試驗證據支持，尤其在三陰性乳腺癌和 BRCA 突變相關乳腺癌中顯示良好療效。多項 Phase 2/3 試驗已完成或正在進行中。

**若要推進需要：**
- 密切監測骨髓抑制和腎功能
- 針對特定分子亞型（如 BRCA 突變、三陰性）的個體化用藥策略
- 與腫瘤科團隊密切合作，制定適當的併用方案

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」列成 trastuzumab／pembrolizumab 等併用方案的適應症 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「許可證數」寫成其他藥品適應症中的併用藥物 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「衛部藥輸字第027591號」列 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「衛署藥輸字第027591號」列 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「衛部藥輸字第028264號」列 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

