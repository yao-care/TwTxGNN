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
| 許可證數 | 10 張（有效單方 2／有效複方 2／已註銷 6） |
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

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cholic Acid 的不重複許可證共 **10 張**：有效單方 2 張、有效複方 2 張、已註銷 6 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部罕藥輸字第000054號 | 酷立酸 膠囊250毫克 | 膠囊劑 | 吉帝藥品股份有限公司 | 2028/06/06 | 治療由於單一酵素缺乏所造成之先天性膽酸 (cholic acid) 合成障礙。輔助治療過氧化體代謝異常（包括Zellweger spectrum disorders）病人呈現之肝病… |
| 衛部罕藥輸字第000055號 | 酷立酸 膠囊50毫克 | 膠囊劑 | 吉帝藥品股份有限公司 | 2028/06/07 | 治療由於單一酵素缺乏所造成之先天性膽酸 (cholic acid) 合成障礙。輔助治療過氧化體代謝異常（包括Zellweger spectrum disorders）病人呈現之肝病… |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第011108號 | "人生"胃立爽顆粒 | SODIUM COPPER CHLOROPHYLLIN、POLYMIGEL (AL.HYDROXIDE +CACO3 +… | 內服顆粒劑 | 急慢性胃炎、胃酸過多、噁心、嘔吐、胃潰瘍、十二指腸潰瘍 |
| 衛署藥製字第018650號 | 力保體康膠囊 | LECITHIN(LECITHOL)、VITAMIN B1 (NITRATE)、CYANOCOBALAMIN (VIT… | 膠囊劑 | 發育不良、營養補給、虛弱體質、熱性消耗性疾患之補助治療、妊娠婦之營養補給、維護肝臟正常功能 |

<details><summary><strong>已註銷</strong>（6 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第004256號</td><td>胃好實錠</td><td>SCOPOLIA EXTRACT、MAGNESIUM CARBONATE、CHOLIC ACID、BENACTYZINE…</td><td>2012/11/30</td></tr><tr><td>內衛藥輸字第003265號</td><td>利保力體片</td><td>PYRIDOXINE(VITAMIN B6)、NIACINAMIDE (NICOTINAMIDE)、PANTOTHENA…</td><td>1990/09/13</td></tr><tr><td>衛署藥製字第004579號</td><td>爽胃王顆粒</td><td>CHOLIC ACID、SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBO…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第016203號</td><td>爽胃王錠</td><td>CHOLIC ACID、SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBO…</td><td>1999/09/06</td></tr><tr><td>衛署藥輸字第002730號</td><td>膽酸</td><td>CHOLIC ACID</td><td>1988/09/02</td></tr><tr><td>衛署藥輸字第003007號</td><td>膽酸</td><td>CHOLIC ACID</td><td>1999/09/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

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
| 2026-10-03 | 許可證表所列皆非 cholic acid | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

