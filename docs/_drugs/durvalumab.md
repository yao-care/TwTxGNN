---
layout: default
title: Durvalumab
parent: 中證據等級 (L3-L4)
nav_order: 90
evidence_level: L3
indication_count: 10
---

# Durvalumab
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Durvalumab：從非小細胞肺癌到泌尿道上皮癌

## 一句話總結

Durvalumab 原本用於治療非小細胞肺癌、小細胞肺癌、膽道癌、肝細胞癌及子宮內膜癌。
TxGNN 模型預測它可能對**泌尿道上皮癌 (urothelial carcinoma)** 相關腫瘤有效，
目前有 **多個臨床試驗**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、小細胞肺癌、膽道癌、肝細胞癌、子宮內膜癌、膀胱癌 |
| 預測新適應症 | 前列腺尿道泌尿道上皮癌 (prostatic urethra urothelial carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L3 |
| 台灣上市 | 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Durvalumab 是一種 PD-L1 抑制劑，透過阻斷 PD-L1 與 PD-1/CD80 的結合，
恢復 T 細胞對腫瘤細胞的免疫監視功能。泌尿道上皮癌通常表現較高的 PD-L1 表現，
且已有其他 PD-1/PD-L1 抑制劑在泌尿道上皮癌獲得核准。
Durvalumab 已核准用於肌肉侵犯型膀胱癌的前導性治療，
其療效可能延伸至其他部位的泌尿道上皮癌。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Phase 1 | ACTIVE_NOT_RECRUITING | 54 | 評估 durvalumab+tremelimumab 在無法接受 cisplatin 的高風險泌尿道上皮癌術前治療 |
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | TERMINATED | 7 | 評估 durvalumab 聯合新輔助化療在變異組織型膀胱癌的療效 |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | COMPLETED | 20 | 低分次放療聯合 durvalumab 和 tremelimumab 治療復發/轉移性婦科癌症 |
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | RECRUITING | 174 | ATARI 試驗：ATR 抑制劑聯合 olaparib/durvalumab 治療 ARID1A 缺失婦科癌症 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomed J | 子宮頸小細胞神經內分泌癌的分子基礎和治療進展，包括 durvalumab 的應用 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Durvalumab 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001088號 | 抑癌寧注射劑 | 注射劑 | 臺灣阿斯特捷利康股份有限公司 | 2028/10/11 | １、非小細胞肺癌(NSCLC)： (１)與含鉑化療藥物併用，作為可切除(腫瘤大小>4公分且/或(and/or)淋巴結分期N1及N2)、無已知的表皮生長因子受體(EGFR)突變或間變… |

<!-- tfda-licenses:end -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療 (PD-L1 抑制劑) |
| 骨髓抑制風險 | 低度 |
| 致吐性分級 | 低度 |
| 監測項目 | 甲狀腺功能、肝腎功能、免疫相關不良反應 |
| 處置防護 | 標準生物製劑處置規範 |

## 安全性考量

- **免疫相關不良反應**：肺炎、肝炎、結腸炎、內分泌病變、皮疹
- **藥物交互作用**：
  - 與皮質類固醇（Hydrocortisone、Dexamethasone、Prednisone 等）有中度交互作用
  - 與 Adalimumab 有重大交互作用
- **特殊族群**：自體免疫疾病患者需謹慎使用

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Durvalumab 已核准用於膀胱癌，且 PD-L1 抑制劑在泌尿道上皮癌的療效已被證實。
預測適應症與原適應症具有相同組織學特徵和免疫學機轉。

**若要推進需要：**
- 針對不同部位泌尿道上皮癌的療效評估
- PD-L1 表現水平與療效的相關性研究
- 與其他免疫檢查點抑制劑的頭對頭比較試驗

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證數「13 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

