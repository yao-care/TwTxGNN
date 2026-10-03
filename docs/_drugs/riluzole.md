---
layout: default
title: Riluzole
parent: 中證據等級 (L3-L4)
nav_order: 227
evidence_level: L4
indication_count: 10
---

# Riluzole
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

# Riluzole：從 ALS 到運動神經元相關疾病

## 一句話總結

Riluzole 是一種谷氨酸拮抗劑，原本用於肌萎縮脊髓側索硬化症（ALS）的治療。TxGNN 模型預測它可能對多種運動神經元相關疾病有效，包括**下運動神經元症候群 (Lower Motor Neuron Syndrome)** 和 **ALS 易感性**，目前有 **多篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肌萎縮脊髓側索硬化症（ALS） |
| 預測新適應症 | 雙側旁矢狀頂枕多小腦回畸形、下運動神經元症候群、Mills 症候群、ALS 易感性 |
| TxGNN 預測分數 | 99.94%-99.98% |
| 證據等級 | L4 |
| 台灣上市 | 已上市 |
| 許可證數 | 5 張（有效單方 4／有效複方 0／已註銷 1） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Riluzole 是核准用於 ALS 治療的藥物之一（台灣另有 edaravone 許可證）。它的主要作用機轉包括：
- 抑制谷氨酸釋放
- 阻斷電壓依賴性鈉離子通道
- 減少興奮性毒性（excitotoxicity）

<!-- review:begin riluzole-not-only-als-drug-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「Riluzole 是目前唯一被核准用於 ALS 治療的藥物。」。Riluzole 不是唯一核准用於 ALS 的藥物；台灣另有 edaravone 許可證（衛部藥製字第062121號，適應症寫「用於減緩肌肉萎縮性側索硬化症」）。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end riluzole-not-only-als-drug-2026-10-03 -->

ALS 的特徵是上下運動神經元的進行性退化。TxGNN 預測的幾個適應症與 ALS 在病理機轉上有密切關聯：

1. **下運動神經元症候群（晚發型）**：與 ALS 共享下運動神經元退化的特徵
2. **Mills 症候群**：一種以單側進行性肢體無力為特徵的運動神經元疾病
3. **ALS 易感性**：代表可能發展為 ALS 的高風險狀態
4. **單肢肌萎縮症（Monomelic Amyotrophy）**：一種局限性的運動神經元疾病

這些疾病都涉及運動神經元的退化，riluzole 的神經保護作用可能對這些疾病有類似的療效。

## 臨床試驗證據

目前無針對這些特定適應症的臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review | J Neurol | 谷氨酸、興奮性毒性與 ALS 的關係，riluzole 作為治療選擇 |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Review | Expert Rev Mol Med | ALS 的病理機轉和治療途徑，riluzole 是唯一延長存活的藥物 |
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | ALS 的病理生理學、診斷和治療管理 |
| [20942786](https://pubmed.ncbi.nlm.nih.gov/20942786/) | 2010 | Review | CNS Neurol Disord Drug Targets | ALS 的診斷、發病機制和治療標靶 |
| [19593125](https://pubmed.ncbi.nlm.nih.gov/19593125/) | 2009 | Review | Curr Opin Neurol | 運動神經元疾病的最新進展 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Riluzole 的不重複許可證共 **5 張**：有效單方 4 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第044485號 | 解凍膜衣錠５０毫克 | 膜衣錠 | 吉帝藥品股份有限公司 | 2031/06/19 | 肌萎縮脊髓側索硬化症（ＡＭＹＯＴＲＯＰＨＩＣ ＬＡＴＥＲＡＬ ＳＣＬＥＲＯＳＩＳ，ＡＬＳ）。 |
| 衛署藥製字第056777號 | "台灣神隆"瑞隆首 | （粉） | 台灣神隆股份有限公司 | 2032/01/19 | 肌萎縮脊髓側索硬化症。 |
| 衛署藥輸字第021905號 | 銳力得膜衣錠 | 膜衣錠 | 賽諾菲股份有限公司 | 2027/09/22 | 肌萎縮脊髓側索硬化症（ＡＭＹＯＴＲＯＰＨＩＣ ＬＡＴＥＲＡＬＳＣＬＥＲＯＳＩＳ，ＡＬＳ） |
| 衛部藥輸字第028266號 | 特魯希口服懸浮液 5毫克/毫升 | 口服懸液劑 | 台灣李氏藥業有限公司 | 2027/03/18 | 肌萎縮脊髓側索硬化症(AMYOTROPHIC LATERL SCLEROSIS, ALS) |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第044452號</td><td>瑞如諾〝健亞〞</td><td>RILUZOLE</td><td>2014/12/19</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

**主要警語：**
- 肝毒性：需定期監測肝功能
- 間質性肺病：罕見但嚴重

**禁忌症：**
- 嚴重肝功能損害

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TxGNN 預測的適應症與 ALS 在病理機轉上高度相關，都涉及運動神經元的退化。Riluzole 的神經保護作用機轉（抗谷氨酸毒性）在理論上可能對這些疾病有效。然而，由於缺乏針對這些特定適應症的臨床試驗數據，需要謹慎評估。

**若要推進需要：**
- 對 Mills 症候群、單肢肌萎縮症等運動神經元疾病進行小規模臨床研究
- 收集真實世界證據（如 ALS 門診中其他運動神經元疾病患者使用 riluzole 的經驗）
- 定期監測肝功能
- 評估長期療效和安全性

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證字號寫成「衛部藥輸字第XXXXXX號」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「Riluzole 是目前唯一被核准用於 ALS 治療的藥物」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

