---
layout: default
title: Oteracil
parent: 高證據等級 (L1-L2)
nav_order: 27
evidence_level: L1
indication_count: 1
---

# Oteracil
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Oteracil：從胃癌到大腸腫瘤

## 一句話總結

Oteracil 是 S-1 複方的成分之一，原本用於胃癌治療。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，
目前有 **8 個臨床試驗**和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌 |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Oteracil 是 S-1 複方的一部分，
其成分在胃癌中的療效已被證實，機轉上可能適用於大腸腫瘤。

胃癌和大腸腫瘤同屬消化道腫瘤，S-1 通過抑制嘧啶代謝來增強氟尿嘧啶的抗腫瘤效果，
這進一步支持了 TxGNN 模型的預測合理性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | 完成 | 161 | S-1 vs Capecitabine 用於轉移性結直腸癌 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 未知 | 40 | S-1 + Bevacizumab 用於復發性結直腸癌 |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fuquinitinib + S-1 用於晚期結腸癌 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 未知 | 82 | Raltitrexed + S-1 用於轉移性結腸癌 |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | 未知 | 42 | S-1 + Oxaliplatin 用於轉移性結腸癌 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | S-1 作為 III 期結腸癌的輔助治療 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 未知 | 1191 | SOX vs XELOX 用於 Stage III 結腸癌 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 終止 | 20 | S-1 + Oxaliplatin 用於結腸癌 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Cancer Res | SOX 輔助化療在高風險 Stage III 結腸癌有效 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | 亞洲轉移性結直腸癌治療指引 |
| [20500514](https://pubmed.ncbi.nlm.nih.gov/20500514/) | 2010 | Animal | Cancer Science | S-1 與 UFT/LV 的抗淋巴結轉移效力比較 |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case report | J Oncol Pharm Pract | S-1 引起的高三酸甘油酯血症 |
| [26805106](https://pubmed.ncbi.nlm.nih.gov/26805106/) | 2015 | Case report | Gan To Kagaku Ryoho | 使用 S-1 治療結腸轉移和腹膜復發的成功案例 |

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥製字第061956號 | "杏輝"氮尿嘧啶酸鉀鹽 | （粉） | 胃癌用藥。 |
| 衛部藥製字第058552號 | "台耀"歐特拉西兒 | 粉劑 | 胃癌用藥。 |
| 衛署藥輸字第025243號 | 愛斯萬膠囊20毫克 | 膠囊劑 | 胃癌、胰臟癌、大腸直腸癌、非小細胞肺癌... |
| 衛部藥製字第060480號 | "杏輝"剋伏膠囊25毫克 | 膠囊劑 | 胃癌、胰臟癌、大腸直腸癌、非小細胞肺癌 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有多個 Phase 2/3 臨床試驗支持 S-1 用於結直腸癌的療效，
且 S-1 複方已在台灣取得大腸直腸癌適應症，證據充分。

**若要推進需要：**
- 詳細的藥物作用機轉資料（MOA）
- 特定族群的安全性監測計畫

---

