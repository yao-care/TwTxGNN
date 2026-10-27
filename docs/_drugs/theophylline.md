---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-16
description: "Theophylline：預測新適應症為血栓性疾病 (Thrombotic disease)（證據等級 L5）。原適應症：平滑肌鬆弛藥"
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Theophylline：從氣喘及支氣管痙攣到血栓性疾病
{: .text-alpha }

## 一句話總結

Theophylline（茶鹼）是一種黃嘌呤類支氣管擴張劑，原本用於氣喘及支氣管痙攣。
TxGNN 模型預測分數最高的新適應症是**血栓性疾病 (Thrombotic disease)**，但目前**沒有臨床試驗**，文獻也多屬間接或無關的研究，證據僅停留在模型預測層級。
相較之下，**阻塞性肺疾病 (Obstructive lung disease，如 COPD)** 的證據明顯較充分，有多項已完成的 Phase 3 試驗，值得優先關注。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 平滑肌鬆弛藥（單方有效許可證中最先出現的核准適應症文字） |
| 預測新適應症 | 血栓性疾病 (Thrombotic disease) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L5（僅有模型預測） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 159 張（有效單方 18／有效複方 10／已過期 4／已註銷 127） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Theophylline 是非選擇性磷酸二酯酶（PDE）抑制劑，同時也是腺苷受體拮抗劑，在氣喘與支氣管痙攣中的療效已被長期證實。

理論上，PDE 抑制可提高血小板內 cAMP，進而減弱血小板聚集，這是預測血栓性疾病的可能機轉依據。但腺苷本身透過提高 cAMP 產生抗血小板效果，Theophylline 的腺苷受體拮抗作用可能抵銷這個效果。目前沒有臨床證據支持其抗血栓角色。

值得注意的是，該模型的其他預測中，**阻塞性肺疾病**與原適應症（氣道疾病）的關聯最直接。低劑量 Theophylline 可活化 HDAC2，恢復皮質類固醇敏感性，此機轉在 COPD 與氣喘中有研究支持。**鼻腔疾病（過敏性鼻炎）**與**氣管疾病**也有一定的機轉合理性。

## 臨床試驗證據

血栓性疾病目前無相關臨床試驗登記。

作為對照，以下為排名第 5 的**阻塞性肺疾病**預測中，與 Theophylline 較直接相關的臨床試驗（僅列部分）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01599871](https://clinicaltrials.gov/study/NCT01599871) | Phase 3 | 完成 | 70 | 52 週雙盲安慰劑對照，評估低劑量 Theophylline 加於 LABA+ICS 治療重度 COPD 的急性惡化率 |
| [NCT03984188](https://clinicaltrials.gov/study/NCT03984188) | Phase 3 | 完成 | 100 | 低劑量 Theophylline 用於生質燃料相關 COPD |
| [NCT02340520](https://clinicaltrials.gov/study/NCT02340520) | Phase 3 | 完成 | 13 | 評估 Theophylline 與 roflumilast 對 HDAC 及皮質類固醇療效的增強作用 |
| [NCT02261727](https://clinicaltrials.gov/study/NCT02261727) | Phase 4 | 完成 | 1670 | 低劑量 Theophylline 單用或合併低劑量 prednisone 對 COPD 急性惡化風險的影響 |
| [NCT00299858](https://clinicaltrials.gov/study/NCT00299858) | Phase 2/3 | 完成 | 24 | Theophylline 對已使用長效支氣管擴張劑之 COPD 患者運動耐力與肺功能的影響 |
| [NCT00671151](https://clinicaltrials.gov/study/NCT00671151) | N/A | 完成 | 35 | 低劑量 Theophylline 對 COPD 惡化分子機轉（NF-κB、HDAC）的調節 |
| [NCT01132781](https://clinicaltrials.gov/study/NCT01132781) | Phase 2 | 完成 | 28 | Theophylline 用於過敏性鼻炎 |

## 文獻證據

血栓性疾病的檢索文獻多為血小板生物標記、檢體處理或其他藥物（如 ticlopidine）的研究，並未提供 Theophylline 抗血栓療效的直接證據，因此僅列出較相關者：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | 體外研究 | General Pharmacology | 探討 milrinone 與腺苷對血小板反應的抑制，屬 cAMP 路徑的間接參考 |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | 體外研究 | Br J Haematol | Theophylline 僅作為血漿 PF4 檢測的抗凝劑成分，並非治療研究 |

作為對照，阻塞性肺疾病方面的代表性文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3534060](https://pubmed.ncbi.nlm.nih.gov/3534060/) | 1986 | RCT | J Allergy Clin Immunol | Theophylline 可改善 COPD 患者整體心臟功能並減輕呼吸困難 |
| [23672674](https://pubmed.ncbi.nlm.nih.gov/23672674/) | 2013 | Review | Am J Respir Crit Care Med | 低濃度 Theophylline 在氣喘與 COPD 具抗發炎作用 |
| [16267358](https://pubmed.ncbi.nlm.nih.gov/16267358/) | 2005 | 綜述 | Proc Am Thorac Soc | 低濃度 Theophylline 活化 HDAC，可能逆轉類固醇抗性 |
| [37524492](https://pubmed.ncbi.nlm.nih.gov/37524492/) | 2023 | Review | Adv Pharmacol | PDE 抑制劑在肺部疾病的角色回顧 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Theophylline 的不重複許可證共 **159 張**：有效單方 18 張、有效複方 10 張、已過期 4 張（未註銷但有效日期早於資料集日期）、已註銷 127 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（18 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第006377號 | "東洲" 阿美諾非林注射液 | 注射劑 | 東洲化學製藥廠股份有限公司 | 2029/12/31 | 心因性、支氣管氣喘、及支氣管痙攣 |
| 衛署藥製字第036330號 | ”瑞安”舒喘內服液5.34毫克/毫升（茶鹼） | 內服液劑 | 瑞安大藥廠股份有限公司 | 2028/04/27 | 氣喘及支氣管痙攣 |
| 衛署藥製字第044083號 | "晟德"適優喘液5.34毫克/毫升 | 內服液劑 | 晟德大藥廠股份有限公司新竹廠 | 2030/11/08 | 支氣管痙攣。 |
| 衛署藥製字第044418號 | "培力"息寧緩釋錠 | 持續性藥效錠 | 培力藥品工業股份有限公司 | 2031/04/12 | 緩解氣喘、支氣管炎、肺氣腫及其他呼吸道相關疾病所引起之支氣管痙攣。 |
| 衛署藥製字第044689號 | 喘克緩釋微粒膠囊２５０毫克〝永勝〞 | 持續性藥效膠囊劑 | 永勝藥品工業股份有限公司 | 2031/11/05 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第044924號 | "永勝" 喘克緩釋微粒膠囊125毫克 | 持續性藥效膠囊劑 | 永勝藥品工業股份有限公司 | 2027/04/23 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第045539號 | "惠勝" 漠喘緩釋微粒膠囊１２５毫克 | 持續性藥效膠囊劑 | 惠勝藥品股份有限公司 | 2028/05/05 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第047791號 | "友聯" 麥喘緩釋微粒膠囊125毫克 | 持續性藥效膠囊劑 | 友聯生技醫藥股份有限公司 | 2031/02/07 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第052478號 | “榮民”喜喘停液 5.34 毫克/毫升 | 內服液劑 | 榮民製藥股份有限公司 | 2030/02/01 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第055021號 | “惠勝”漠喘緩釋微粒膠囊 250 毫克 | 持續性藥效膠囊劑 | 惠勝藥品股份有限公司 | 2030/06/09 | 氣喘及支氣管痙攣。 |
| 衛署藥輸字第019557號 | 優汝喘持續性藥效錠400毫克 | 錠劑 | 嘉德藥品企業股份有限公司 | 2027/10/19 | 氣喘及支氣管痙攣 |
| 衛署藥輸字第019567號 | 善寧持續性藥效膠囊400公絲 | 持續性藥效膠囊劑 | 天義企業股份有限公司 | 2027/10/23 | 氣喘及支氣管痙攣。 |
| 衛署藥輸字第019624號 | 善寧持續性藥效膠囊２００公絲 | 持續性藥效膠囊劑 | 天義企業股份有限公司 | 2027/11/27 | 氣喘及支氣管痙攣。 |
| 衛部藥製字第059776號 | "培力"息喘寧緩釋錠200毫克 | 持續性藥效錠 | 培力藥品工業股份有限公司 | 2027/09/14 | 氣喘及支氣管痙攣。 |
| 衛部藥製字第060320號 | "國嘉"息舒寧液5.34毫克/毫升 | 內服液劑 | 國嘉製藥工業股份有限公司幼獅三廠 | 2029/07/10 | 氣喘及支氣管痙攣。 |
| 衛部藥陸輸字第000798號 | 茶生僉 | （粉） | 漢旭股份有限公司 | 2027/07/13 | 平滑肌鬆弛藥 |
| 衛部藥陸輸字第000813號 | 茶鹼 | （粉） | 漢旭股份有限公司 | 2027/12/15 | 平滑肌鬆弛藥 |
| 衛部藥陸輸字第000962號 | 茶生僉 | （粉） | 恒亞貿易股份有限公司 | 2030/10/23 | 平滑肌鬆弛藥。 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（10 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第009094號 | 喘息錠 | THEOPHYLLINE、GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN) | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛署藥製字第010826號 | "永信"喘能錠 | THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCERYL ETHER (EQ TO… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛署藥製字第019549號 | "皇佳" 鐵鎮克錠 | THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛署藥製字第022084號 | 得咳寧錠〝皇佳〞 | GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、THEOPHYLLINE… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛署藥製字第024366號 | "正和"救肺喘錠 | GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE SOD… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛署藥製字第025127號 | 氣喘平錠 | EPHEDRINE SULFATE、THEOPHYLLINE、PHENOBARBITAL、GUAIACOL GLYCOL… | 錠劑 | 氣喘及支氣管痙攣 |
| 衛署藥製字第034314號 | "生達"利咳安寧錠 | THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCERYL ETHER (EQ TO… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛署藥製字第040662號 | 治喘能錠 | THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCERYL ETHER (EQ TO… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛署藥製字第043473號 | 布隆可林　錠 | GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE SOD… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患所引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |
| 衛部藥製字第060240號 | 蒂奧白錠 | THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCOLATE (EQ TO GLYC… | 錠劑 | 急慢性支氣管炎、氣喘性支氣管炎、支氣管性氣喘或其他慢性呼吸器疾患索引起之咳嗽、喀痰、支氣管痙攣或呼吸困難等症狀之緩解。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（4 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第044498號</td><td>”生達”鐵寧喘持續性錠２００毫克</td><td>THEOPHYLLINE</td><td>2026/06/21</td></tr><tr><td>衛署藥輸字第018223號</td><td>無水茶鹼</td><td>THEOPHYLLINE ANHYDROUS</td><td>2025/08/24</td></tr><tr><td>衛署藥輸字第021298號</td><td>優汝喘持續性藥效錠３００公絲</td><td>THEOPHYLLINE</td><td>2026/07/11</td></tr><tr><td>衛署藥陸輸字第000180號</td><td>氨基非林</td><td>THEOPHYLLINE</td><td>2025/09/12</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（127 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000719號</td><td>布隆可林片</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE SOD…</td><td>2000/03/17</td></tr><tr><td>內衛藥製字第002279號</td><td>茶/</td><td>THEOPHYLLINE</td><td>2017/02/06</td></tr><tr><td>內衛藥製字第003325號</td><td>免暈膠囊</td><td>THEOPHYLLINE、CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL、DIPHENH…</td><td>2012/08/14</td></tr><tr><td>內衛藥製字第004348號</td><td>治喘片</td><td>THEOPHYLLINE</td><td>2016/06/23</td></tr><tr><td>內衛藥製字第004548號</td><td>小兒治喘糖漿”華孚”</td><td>THEOPHYLLINE</td><td>2016/06/23</td></tr><tr><td>內衛藥製字第004838號</td><td>氣喘糖衣片</td><td>ISOPROTERENOL HCL、PHENOBARBITAL、THEOPHYLLINE、EPHEDRINE SULFA…</td><td>2016/09/08</td></tr><tr><td>內衛藥製字第010264號</td><td>茶鹼</td><td>THEOPHYLLINE</td><td>2009/12/30</td></tr><tr><td>內衛藥製字第013309號</td><td>鎮喘膠囊</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2002/04/17</td></tr><tr><td>內衛藥製字第013853號</td><td>小兒喘平寧糖漿</td><td>THEOPHYLLINE、CHLORPHENIRAMINE MALEATE、PHENOBARBITAL、METHYLEP…</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第000558號</td><td>茶鹼</td><td>THEOPHYLLINE ANHYDROUS</td><td>1985/09/10</td></tr><tr><td>內衛藥輸字第001293號</td><td>安妥喘片</td><td>PROTOKYLOL HCL、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)…</td><td>1990/12/06</td></tr><tr><td>內衛藥輸字第001442號</td><td>喘平片</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、BROMISOVALUM (…</td><td>1986/06/17</td></tr><tr><td>內衛藥輸字第001757號</td><td>新弗羅達</td><td>PHENOBARBITAL、THEOPHYLLINE BETA-OXYPROPYL-、ATROPINE METHONIT…</td><td>1985/08/20</td></tr><tr><td>內衛藥輸字第002266號</td><td>依必菲林</td><td>THEOPHYLLINE ACETATE OF DIETHYLAMINE、THEOPHYLLINE ACETATE OF…</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第003424號</td><td>立平喘片劑</td><td>1-DIMETHYLPHENYLIMINOTHIAZOLIDINE HYDRORHODANIDE、ANTIPYRINE、…</td><td>1985/08/14</td></tr><tr><td>內衛藥輸字第007235號</td><td>泰力糖衣片</td><td>THEOPHYLLINE、THIAMINE HYDROCHLORIDE、BEZOAR ORIENTALE、MUSK (M…</td><td>1990/11/30</td></tr><tr><td>衛署藥製字第001182號</td><td>茶/含水物</td><td>THEOPHYLLINE MONOHYDRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第001183號</td><td>茶/無水物</td><td>THEOPHYLLINE MONOHYDRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第001452號</td><td>氨基非林含水</td><td>THEOPHYLLINE MONOHYDRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第002205號</td><td>貴呼通膠囊</td><td>THEOPHYLLINE ANHYDROUS、GUAIACOL GLYCOLATE (EQ TO GLYCERYL GU…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第002223號</td><td>力利喘錠</td><td>PHENOBARBITAL、THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HY…</td><td>1996/04/02</td></tr><tr><td>衛署藥製字第004100號</td><td>喘癒錠</td><td>THEOPHYLLINE MONOHYDRATE、PHENOBARBITAL、EPHEDRINE HCL (EQ TO…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第004558號</td><td>撲喘錠</td><td>THEOPHYLLINE ANHYDROUS、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROC…</td><td>1995/12/29</td></tr><tr><td>衛署藥製字第006477號</td><td>"南美" 止喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>1998/08/17</td></tr><tr><td>衛署藥製字第006562號</td><td>"龍德" 喘克治錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>2009/12/29</td></tr><tr><td>衛署藥製字第007741號</td><td>驅諸喘錠</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE</td><td>1990/10/20</td></tr><tr><td>衛署藥製字第008154號</td><td>止你喘錠</td><td>THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、P…</td><td>2002/04/17</td></tr><tr><td>衛署藥製字第009563號</td><td>嗽康寧膠囊</td><td>METHOXYPHENAMINE HCL、THEOPHYLLINE、DL-METHYLEPHEDRINE HCL、GUA…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第010244號</td><td>氣喘膠囊</td><td>CHLORPHENIRAMINE MALEATE、THEOPHYLLINE、PHENOBARBITAL、EPHEDRIN…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第013777號</td><td>順康膠囊</td><td>PHENOBARBITAL、THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HY…</td><td>2002/05/07</td></tr><tr><td>衛署藥製字第014122號</td><td>喘福膠囊</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第014133號</td><td>阿適寧錠</td><td>PHENYLPROPANOLAMINE HCL (DL-NOREPHEDRINE HCL)、THEOPHYLLINE S…</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第017132號</td><td>咳菲林錠</td><td>THEOPHYLLINE、PHENOBARBITAL、EPHEDRINE HCL (EQ TO EPHEDRINE HY…</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第017802號</td><td>"健康" 即喘妥糖衣錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2012/12/18</td></tr><tr><td>衛署藥製字第018047號</td><td>氣平錠</td><td>PHENOBARBITAL、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第019195號</td><td>豐平喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2003/01/22</td></tr><tr><td>衛署藥製字第020012號</td><td>蒂奧白錠</td><td>THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCOLATE (EQ TO GLYC…</td><td>2019/07/15</td></tr><tr><td>衛署藥製字第020303號</td><td>斯喘寧糖衣錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第020363號</td><td>芝喘錠</td><td>THEOPHYLLINE MONOHYDRATE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDR…</td><td>2002/04/17</td></tr><tr><td>衛署藥製字第020410號</td><td>滅喘糖衣錠</td><td>THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、P…</td><td>2001/05/15</td></tr><tr><td>衛署藥製字第020419號</td><td>蒂歐可普錠</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、EPHEDRINE HC…</td><td>1998/06/08</td></tr><tr><td>衛署藥製字第020888號</td><td>喘嗽顆粒</td><td>DL-METHYLEPHEDRINE HCL、ETHAVERINE (eq to ETHYLPAPAVERINE)、TH…</td><td>1996/04/16</td></tr><tr><td>衛署藥製字第021453號</td><td>百敵喘錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>1999/09/16</td></tr><tr><td>衛署藥製字第021656號</td><td>"優生"得歐林錠</td><td>THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCERYL ETHER (EQ TO…</td><td>2019/10/07</td></tr><tr><td>衛署藥製字第022348號</td><td>"壽元"勿咳平錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCOLATE (EQ TO GL…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第022683號</td><td>"皇佳" 氨基乙酸鈉茶鹼</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2023/07/24</td></tr><tr><td>衛署藥製字第024515號</td><td>喘服樂錠</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE (SO…</td><td>2000/09/20</td></tr><tr><td>衛署藥製字第024753號</td><td>瑞喘適錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、CHLOROPHYLL SODIUM COPPER、GU…</td><td>1991/05/23</td></tr><tr><td>衛署藥製字第024769號</td><td>"東光吉華"咳鎮糖衣錠</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、THEOPHYLLINE…</td><td>2005/01/17</td></tr><tr><td>衛署藥製字第026107號</td><td>安治喘錠</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE (SO…</td><td>1995/05/06</td></tr><tr><td>衛署藥製字第026143號</td><td>舒喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第026645號</td><td>管寧錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCOLATE (EQ TO GL…</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第026837號</td><td>易生堂喘息藥</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE SOD…</td><td>1999/09/16</td></tr><tr><td>衛署藥製字第027412號</td><td>喘舒錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>2009/07/16</td></tr><tr><td>衛署藥製字第029586號</td><td>喘息散</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、GLYCYRRHIZA…</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第031759號</td><td>小兒喘平寧液</td><td>CHLORPHENIRAMINE MALEATE、PHENOBARBITAL、THEOPHYLLINE、METHYLEP…</td><td>1997/08/28</td></tr><tr><td>衛署藥製字第032297號</td><td>驅諸喘錠</td><td>THEOPHYLLINE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第034521號</td><td>"生達" 茶生僉甘氨基酸鈉</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第038464號</td><td>"十全"安治喘錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>2026/09/07</td></tr><tr><td>衛署藥製字第039637號</td><td>力利喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>2005/09/02</td></tr><tr><td>衛署藥製字第046585號</td><td>"黃氏" 液受內服液 5.34 公絲/公撮</td><td>THEOPHYLLINE ANHYDROUS</td><td>2025/05/27</td></tr><tr><td>衛署藥輸字第000925號</td><td>茶鹹</td><td>THEOPHYLLINE</td><td>1986/04/10</td></tr><tr><td>衛署藥輸字第001213號</td><td>茶/甘氨基酸鈉</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>1992/04/17</td></tr><tr><td>衛署藥輸字第002509號</td><td>帝樂康寧注射液</td><td>THEOPHYLLINE、HEPTAMINOL、NICOTINYL ALCOHOL</td><td>1986/10/03</td></tr><tr><td>衛署藥輸字第002510號</td><td>帝樂康寧錠</td><td>NICOTINYL ALCOHOL TARTRATE、THEOPHYLLINE、HEPTAMINOL HCL</td><td>1986/10/03</td></tr><tr><td>衛署藥輸字第003111號</td><td>茶鹼無水物</td><td>THEOPHYLLINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003397號</td><td>樂能</td><td>PHENYLETHYLBARBITURATE CALCIUM、THEOPHYLLINE、IODINE GLUTINATE…</td><td>1986/01/10</td></tr><tr><td>衛署藥輸字第004041號</td><td>甘氨酸鈉茶/</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006951號</td><td>甘氨酸鈉/</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第007043號</td><td>無水茶鹼</td><td>THEOPHYLLINE ANHYDROUS</td><td>2006/09/25</td></tr><tr><td>衛署藥輸字第007733號</td><td>甘氨酸鈉茶/</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2004/07/23</td></tr><tr><td>衛署藥輸字第007762號</td><td>的菲林錠</td><td>PHENOBARBITAL、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第007953號</td><td>適喘持續性膠囊２６０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1995/12/29</td></tr><tr><td>衛署藥輸字第007961號</td><td>適喘持續性膠囊１３０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1995/12/29</td></tr><tr><td>衛署藥輸字第009134號</td><td>安替喘錠</td><td>THEOPHYLLINE、PHENOBARBITAL、METHYLEPHEDRINE HCL L-</td><td>1990/01/18</td></tr><tr><td>衛署藥輸字第009181號</td><td>貝樂輕軟膠囊</td><td>THEOPHYLLINE、GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第009540號</td><td>扭益寧持續性錠２５０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009628號</td><td>立保脂妥膠囊</td><td>PYRIDOXINE(VITAMIN B6)、PHOSPHOLIPID ESSENTIAL、THEOPHYLLINE、T…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第010063號</td><td>歐福林孩童喘錠</td><td>THEOPHYLLINE MONOHYDRATE、ETHYLENEDIAMINE DIHYDRATE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第010064號</td><td>歐福林喘錠</td><td>ETHYLENEDIAMINE DIHYDRATE、THEOPHYLLINE MONOHYDRATE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第010356號</td><td>治惡喘持續性膠囊２５０公絲</td><td>THEOPHYLLINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010443號</td><td>治惡喘持續性膠囊１２５公絲</td><td>THEOPHYLLINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010854號</td><td>益樂去痰糖漿</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE (SO…</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第011110號</td><td>益樂去痰膜衣錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第011161號</td><td>舒喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE A…</td><td>1988/05/09</td></tr><tr><td>衛署藥輸字第011267號</td><td>益喘康懸液</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第012730號</td><td>優汝喘持續性錠</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>1993/03/01</td></tr><tr><td>衛署藥輸字第013407號</td><td>沙克喘糖衣錠</td><td>THEOPHYLLINE MONOHYDRATE、THEOPHYLLINE MONOHYDRATE、OCTODRINE…</td><td>1987/11/24</td></tr><tr><td>衛署藥輸字第013803號</td><td>弗羅達注射液</td><td>PHENYLETHYLBARBITURIC ACID、ATROPINE METHONITRATE、THEOPHYLLIN…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013846號</td><td>立平喘錠</td><td>1-DIMETHYLPHENYLIMINOTHIAZOLIDINE HYDRORHODANIDE、ANTIPYRINE、…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第013891號</td><td>茶/粉劑</td><td>THEOPHYLLINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014448號</td><td>舒活－小時持續性膠囊１００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1998/05/05</td></tr><tr><td>衛署藥輸字第014687號</td><td>氨基非林</td><td>Aminophylline (Theophylline-ethylenediamine)</td><td>2025/04/24</td></tr><tr><td>衛署藥輸字第014870號</td><td>舒活２４小時持續性膠囊２００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1998/05/05</td></tr><tr><td>衛署藥輸字第014871號</td><td>舒活２４小時持續性膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1998/05/05</td></tr><tr><td>衛署藥輸字第016035號</td><td>舒爾能持續性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>1993/06/22</td></tr><tr><td>衛署藥輸字第016097號</td><td>沙克喘糖衣錠</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、THEOPHYLLI…</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第016397號</td><td>舒喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>1993/01/08</td></tr><tr><td>衛署藥輸字第017095號</td><td>舒爾能持續性藥效膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1993/06/22</td></tr><tr><td>衛署藥輸字第017171號</td><td>治惡喘持續性膠囊１２５公絲</td><td>THEOPHYLLINE</td><td>2004/05/04</td></tr><tr><td>衛署藥輸字第017451號</td><td>治惡喘持續性膠囊２５０公絲</td><td>THEOPHYLLINE</td><td>2004/05/04</td></tr><tr><td>衛署藥輸字第017854號</td><td>沙克喘糖衣錠</td><td>OCTODRINE PHOSPHATE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO G…</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第019003號</td><td>適爾祿２５０公絲</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第019043號</td><td>適爾祿３５０公絲</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第019105號</td><td>拿寧持續錠２５０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2014/09/11</td></tr><tr><td>衛署藥輸字第019850號</td><td>舒爾能持續性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>1996/02/01</td></tr><tr><td>衛署藥輸字第019854號</td><td>舒爾能持續性膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1996/02/01</td></tr><tr><td>衛署藥輸字第020150號</td><td>甘氨酸鈉茶＊</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第020576號</td><td>歐福林持續性藥效錠２５０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2020/06/02</td></tr><tr><td>衛署藥輸字第020579號</td><td>賜喘寧持續藥效性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第020580號</td><td>賜喘寧持續性藥效膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第020581號</td><td>賜喘寧持續性藥效膠囊１００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第020667號</td><td>佑德持續性藥效錠４００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2000/08/11</td></tr><tr><td>衛署藥輸字第020668號</td><td>佑德持續性藥效錠６００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2005/08/03</td></tr><tr><td>衛署藥輸字第020922號</td><td>氨基非林</td><td>ETHYLENEDIAMINE、THEOPHYLLINE</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第020946號</td><td>無水茶鹼</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第021107號</td><td>舒爾能持續性膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2000/08/11</td></tr><tr><td>衛署藥輸字第021115號</td><td>舒爾能持續性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2000/08/11</td></tr><tr><td>衛署藥輸字第022365號</td><td>優汝喘持續性藥效錠２００毫克</td><td>THEOPHYLLINE</td><td>2025/06/11</td></tr><tr><td>衛署藥輸字第024422號</td><td>甘氨酸鈉茶鹼</td><td>Theophylline Sodium Glycinate</td><td>2011/10/26</td></tr><tr><td>衛署藥輸字第025029號</td><td>無水茶/</td><td>THEOPHYLLINE ANHYDROUS</td><td>2020/04/10</td></tr><tr><td>衛署藥陸輸字第000038號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2010/09/21</td></tr><tr><td>衛署藥陸輸字第000051號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2016/05/31</td></tr><tr><td>衛署藥陸輸字第000062號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2013/12/30</td></tr><tr><td>衛署藥陸輸字第000140號</td><td>胺非林</td><td>THEOPHYLLINE、AMINOPHYLLINE (COROPHYLLIN)</td><td>2013/12/30</td></tr><tr><td>衛署藥陸輸字第000181號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2017/05/10</td></tr><tr><td>衛署藥陸輸字第000264號</td><td>茶生僉</td><td>Theophylline</td><td>2019/03/20</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **禁忌症（知識圖譜推論，非仿單內容）**：知識圖譜列出的相關疾病包括高血壓、肝衰竭、癲癇、焦慮症、紫質症、腎臟疾病、肝病、膽囊疾病、血小板低下、甲狀腺功能低下、消化性潰瘍、開角型青光眼、精神病性疾患、糖尿病（含酮酸中毒）、良性攝護腺肥大、嗜中性白血球低下及顆粒球缺乏症等，使用前須審慎評估。
- **藥物交互作用**：共記錄 371 筆交互作用。主要包括：
  - 重度：Bupropion
  - 中度：Famotidine、Ranitidine、Cimetidine、Omeprazole、Rabeprazole、Clarithromycin、Doxycycline、Tetracycline、Minocycline、多種皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide）、活性碳等
  - 輕度：Ephedrine

此外，Theophylline 治療濃度範圍狹窄，且主要經 CYP1A2 代謝，使用時需監測血中濃度。其餘警語請參考原廠仿單。

## 結論與下一步

**決策：Hold**（針對首要預測「血栓性疾病」）

**理由：**
- 血栓性疾病僅有模型預測，無臨床試驗，文獻亦無直接證據；且腺苷受體拮抗作用可能抵銷理論上的抗血小板效果。
- 相對地，阻塞性肺疾病（COPD）有多項已完成的 Phase 3 試驗與機轉支持，若要推進，建議改以此方向評估，並採 Proceed with Guardrails。

**若要推進需要：**
- 血栓性疾病：先進行前臨床研究（如血小板聚集試驗），釐清 PDE 抑制與腺苷拮抗的淨效應。
- 取得完整作用機轉資料（MOA）。
- COPD 方向：整理已完成 Phase 3 試驗的結果，確認低劑量療效，並建立血中濃度監測與藥物交互作用管理計畫。
- 確認台灣有效許可證的核准適應症是否涵蓋擬申請的新適應症。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第014567號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第023456號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第034567號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第045678號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「台灣商品名」三個品名 | 報告重生後已無此錯誤（2026-10-15：新報告未再出現「氣舒錠」「泰乙乳甘液」；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

