---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 2
monitor_inn: "vasopressin"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
last_modified_at: 2026-10-29
description: "Vasopressin：預測新適應症為先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)（證據等級 L4）。原適應症：尿崩症"
---

# Vasopressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Vasopressin：從尿崩症到先天性凝血酶原缺乏症
{: .text-alpha }

## 一句話總結

Vasopressin（血管加壓素）原本用於尿崩症治療。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，
但目前**無臨床試驗**，僅有 **3 篇間接相關文獻**（多為凝血因子 V/VIII 缺乏或後天性血友病的病例與回顧），證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尿崩症 |
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 0.9963 |
| 證據等級 | L5 |
| 台灣上市 | 僅有已註銷許可證（目前無有效上市） |
| 許可證數 | 4 張（有效單方 0／有效複方 0／已註銷 4） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，vasopressin 與其類似物 desmopressin (DDAVP) 可經由 V2 受體促使內皮細胞釋放 von Willebrand 因子與第 VIII 凝血因子，因此在 FVIII/FV 相關的出血性疾病中有一定作用。

然而，這個機轉並不會直接提高凝血酶原（第 II 因子）的量。因此，vasopressin 與先天性凝血酶原缺乏症之間的關聯是間接且推測性的。原適應症（尿崩症）屬於水分平衡調節，和凝血疾病的病理也無明顯相似之處。

高分的 TxGNN 預測目前僅是模型輸出，尚無直接的臨床或機轉證據支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | 後天性血友病 A 的診斷、病因、臨床表現與治療選項；屬於 FVIII 自體抗體疾病，與凝血酶原缺乏無直接關係 |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case series | Rinsho Ketsueki | 先天性 FV/FVIII 合併缺乏個案使用 DDAVP 的經驗 |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case series | Rinsho Ketsueki | FV/FVIII 合併缺乏孕婦以 FVIII 濃縮製劑支持剖腹產的處置 |

以上文獻皆非針對凝血酶原缺乏症，僅屬間接參考。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Vasopressin 的不重複許可證共 **4 張**：有效單方 0 張、有效複方 0 張、已註銷 4 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（4 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第009756號</td><td>必壓生５單位/公撮注射劑</td><td>VASOPRESSIN TANNATE</td><td>1997/12/05</td></tr><tr><td>衛署藥輸字第009774號</td><td>利度痛注射液３％</td><td>L-NOREPINEPHRINE、LIDOCAINE HCL、VASOPRESSIN</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第013329號</td><td>紐利度痛注射劑</td><td>L-NOREPINEPHRINE、LIDOCAINE HCL、VASOPRESSIN</td><td>1994/11/01</td></tr><tr><td>衛署藥輸字第020506號</td><td>８－氨胍戊酸血管加壓素注射用粉劑</td><td>VASOPRESSIN</td><td>2010/08/24</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 121 筆交互作用，其中較需注意的 Major 等級包括：
  - Dolasetron
  - Cisapride
  - Papaverine
  - Macimorelin
  
  Moderate 等級包括 famotidine、epinephrine、loperamide、chlorpropamide、clarithromycin、levofloxacin、ondansetron、granisetron、heparin、cilostazol 等。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有臨床試驗，文獻也只是 FVIII/FV 相關的間接證據，機轉上無法直接提升凝血酶原。
- 台灣僅剩已註銷的許可證，且 TxGNN 高分只是模型預測。

**若要推進需要：**
- 補齊 vasopressin 的作用機轉資料（MOA）。
- 釐清是否有針對凝血酶原缺乏症的機轉或前臨床研究。
- 蒐集直接以該疾病為對象的臨床或病例證據。
- 確認製劑可取得性（現無有效許可證）及給藥途徑是否適用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

