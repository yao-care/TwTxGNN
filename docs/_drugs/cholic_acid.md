---
layout: default
title: Cholic Acid
parent: 中證據等級 (L3-L4)
nav_order: 62
evidence_level: L4
indication_count: 10
---

# Cholic Acid
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

# Cholic Acid：從膽石症到 HIV 感染性疾病

## 一句話總結

Cholic Acid（膽酸）是人體重要的初級膽汁酸，在台灣以罕藥「酷立酸膠囊」（Cholbam）上市，核准用於單一酵素缺乏造成的先天性膽酸合成障礙，以及過氧化體代謝異常病人肝病表現等併發症的輔助治療。
TxGNN 模型預測它可能對 **HIV 感染性疾病 (HIV infectious disease)** 有效，
目前有 **0 個臨床試驗**及 **9 篇文獻**相關資料，但現有證據主要來自局部外用抗病毒的體外研究，部分文獻甚至顯示膽酸衍生物可能促進病毒複製，整體支持強度有限。

<!-- review:begin cholic-acid-tw-brand-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「在台灣以「得利膽錠」等多種品名上市，原本用於膽石症、膽囊炎及利膽等肝膽相關適應症。」。「得利膽錠」的主成分是 dehydrocholic acid（去氫膽酸），不是 cholic acid，且已於 2016 年註銷；台灣現行的 cholic acid 許可證是罕藥「酷立酸膠囊」（Cholbam，衛部罕藥輸字第000054、000055號），核准用於先天性膽酸合成障礙等。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cholic-acid-tw-brand-2026-10-03 -->

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 單一酵素缺乏造成的先天性膽酸合成障礙；過氧化體代謝異常（含 Zellweger spectrum disorders）之肝病表現、脂肪瀉或脂溶性維生素吸收降低併發症的輔助治療 |
| 預測新適應症 | HIV 感染性疾病 (HIV infectious disease) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L4 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

<!-- review:begin cholic-acid-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／膽石症、預防膽石症、助長維他命之吸收」。原文的適應症來自 dehydrocholic acid 製劑「得利膽錠」（已註銷）；cholic acid 本身的台灣許可證「酷立酸膠囊」核准的是先天性膽酸合成障礙，及過氧化體代謝異常相關併發症的輔助治療。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cholic-acid-original-indication-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cholic Acid 為人體初級膽汁酸，從藥理學資料可知其作用於兩個主要靶點：**GPBA 受體（TGR5/GPBAR1）** 及 **法尼醇 X 受體（Farnesoid X Receptor, FXR）**，兩者在膽汁酸代謝、脂質吸收與腸道穩態調控中扮演關鍵角色。

Cholic Acid 具有兩親性界面活性劑（detergent）特性，早期研究（1986–1993 年）顯示其外用形式（sodium cholate）對 HIV-1 反轉錄酶活性有體外抑制作用，並被納入含殺精劑的避孕海綿（Protectaid）作為局部抗病毒成分。TxGNN 的預測可能部分來自知識圖譜中此類「膽酸–病毒包膜破壞」的連結。

然而，一項 2006 年體外研究（PMID 16610808）明確指出，**胺基化膽酸衍生物反而誘導 HIV-1 在 T 細胞中大量複製並促進合胞體形成**，顯示系統性給藥途徑的機轉存在根本不確定性。原適應症（膽道/肝臟疾病）與 HIV 感染在病理機轉上亦無直接關聯，口服膽酸用於 HIV 治療目前缺乏任何臨床依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32052857](https://pubmed.ncbi.nlm.nih.gov/32052857/) | 2020 | Review | Hepatology | HIV 感染者通常被排除於 NASH 臨床試驗之外，膽汁酸類新藥用於此族群時的 DDI 值得高度關注 |
| [9238301](https://pubmed.ncbi.nlm.nih.gov/9238301/) | 1997 | Review | Ann NY Acad Sci | 綜述含 sodium cholate 的陰道海綿作為抗 STD 避孕方法的研發現況 |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Review | Aust NZ J Obstet Gynaecol | HIV 流行促進新型殺精劑與抗病毒避孕方法研發的政策討論 |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Review | Ann Acad Med Singapore | 物理與化學屏障避孕法（含 sodium cholate 海綿）對 HIV 防護的系統性回顧 |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Cohort | Pharmacotherapy | HIV 感染者接受蛋白酶抑制劑治療時膽汁酸濃度升高，且與肝毒性風險相關 |
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | In vitro | Human Reproduction | Sodium cholate 體外抑制 HIV-1 反轉錄酶活性；Protectaid 海綿具殺精及局部抗病毒效果 |
| [2870224](https://pubmed.ncbi.nlm.nih.gov/2870224/) | 1986 | In vitro | Lancet | TNBP/sodium cholate 組合使 HBV、NANB 及 HTLV-III 病毒失活，適用血液製品滅菌 |
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro | J Med Chem | ⚠️ 胺基化膽酸衍生物**促進** HIV-1 在 T 細胞中複製並誘導合胞體形成（負面發現） |
| [28745428](https://pubmed.ncbi.nlm.nih.gov/28745428/) | 2017 | In vitro | ChemMedChem | 界面活性劑（Triton X-100）顯著降低 HIV-1 蛋白酶抑制劑結合親和力，提示 detergent 特性在分析中的干擾問題 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第004206號 | 得利膽錠 | 錠劑 | 膽石症、預防膽石症、助長維他命之吸收 |
| 內衛藥輸字第004857號 | 脫氫膽酸 | （粉） | 利膽劑 |
| 衛部藥陸輸字第000882號 | 去氧熊膽酸 | （粉） | 利膽藥 |
| 內衛藥製字第002253號 | "大豐"舒肝膽錠50毫克 | 錠劑 | 膽固醇系膽結石之溶解、原發性膽道肝硬化（primary biliary cirrhosis, PBC）之肝功能改善 |
| 內衛藥輸字第002380號 | 復膽利 | 錠劑 | 膽囊病、膽囊炎 |

<!-- review:begin cholic-acid-license-rows-other-bile-acids-2026-10-03 -->

> **查核加註（2026-10-03）**：上表 5 張許可證都不是 cholic acid：「得利膽錠」「脫氫膽酸」「復膽利」是 dehydrocholic acid（去氫膽酸）製劑且都已註銷，「去氧熊膽酸」「"大豐"舒肝膽錠」是 ursodeoxycholic acid（熊去氧膽酸）。Cholic acid 本身的有效許可證是罕藥「酷立酸膠囊」250 毫克／50 毫克（衛部罕藥輸字第000054、000055號）。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cholic-acid-license-rows-other-bile-acids-2026-10-03 -->

---

## 安全性考量

**藥物交互作用**（來源：DDInter，共 10 項，均為中度）：

| 交互藥物 | 等級 | 備註 |
|---------|------|------|
| Cholestyramine | 中度 | 膽酸螯合劑，可能降低 Cholic Acid 腸道吸收 |
| Colesevelam | 中度 | 膽酸螯合劑，同類交互機轉 |
| Colestipol | 中度 | 膽酸螯合劑，同類交互機轉 |
| Aluminum hydroxide | 中度 | 制酸劑，可能影響膽酸吸收 |
| Sucralfate | 中度 | 胃黏膜保護劑，可能影響膽酸吸收 |
| Cyclosporine | 中度 | 免疫抑制劑，可能競爭膽汁酸轉運體 |
| Phenobarbital | 中度 | 肝酶誘導劑，影響膽酸代謝 |
| Tipranavir | 中度 | HIV 蛋白酶抑制劑，若考慮 HIV 適應症需特別評估此交互作用 |
| Ribociclib | 中度 | CDK4/6 抑制劑，注意潛在肝毒性疊加 |
| Sorafenib | 中度 | 多靶點激酶抑制劑，注意潛在肝毒性疊加 |

此外，Cholic Acid 為 **GPBA 受體（TGR5）** 及 **Farnesoid X 受體（FXR）** 的內源性配體，與影響這兩條信號路徑的藥物合用時應注意潛在交互影響。

---

## 結論與下一步

**決策：Hold**

**理由：**
現有文獻支持僅限於局部外用的體外抗病毒效果（1980–1990 年代的避孕海綿研究），且 2006 年關鍵體外研究已明確顯示膽酸衍生物可能**促進 HIV 複製**；口服系統性給藥用於 HIV 治療的機轉依據不足，缺乏任何臨床試驗支持，無法推進。

**若要推進需要：**
- 先釐清口服 Cholic Acid 本身（而非衍生物）對 HIV 複製的影響，排除促進病毒複製的安全疑慮
- 評估膽汁酸-HIV 互動在系統性給藥途徑下的作用機轉（非局部 detergent 效應）
- 確認與抗病毒藥物（特別是 Tipranavir 等蛋白酶抑制劑）的交互作用安全性
- 補充完整的 DrugBank MOA 資料，以強化機轉合理性分析

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「在台灣以「得利膽錠」等多種品名上市」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「原適應症」引自 dehydrocholic acid 製劑 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表所列皆非 cholic acid | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

