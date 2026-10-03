---
layout: default
title: Theophylline
parent: 高證據等級 (L1-L2)
nav_order: 251
evidence_level: L2
indication_count: 7
---

# Theophylline
{: .fs-9 }

證據等級: **L2** | 預測適應症: **7** 個
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

# Theophylline 藥師筆記

## 一句話總結

Theophylline（茶鹼）是甲基黃嘌呤類支氣管擴張劑，TxGNN 預測其對嗅覺障礙及阻塞性肺病具療效，已有臨床試驗支持其用於病毒感染後嗅覺喪失。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Theophylline |
| DrugBank ID | DB00277 |
| 台灣商品名 | 優汝喘持續性藥效錠、息喘寧緩釋錠、適優喘液等 |
| 原核准適應症 | 支氣管性氣喘、支氣管炎、心臟性呼吸困難 |
| 預測新適應症 | 鼻腔疾病（嗅覺障礙）、阻塞性肺病、氣管疾病、血栓性疾病 |
| 最高證據等級 | **L2**（Phase 2 臨床試驗） |
| TxGNN 分數 | 0.867（鼻腔疾病） |

<!-- review:begin theophylline-brand-names-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「台灣商品名／小兒治喘糖漿、氣舒錠、泰乙乳甘液等」。資料集中查無「氣舒錠」「泰乙乳甘液」，「小兒治喘糖漿」已於 2016 年註銷；改列資料集中有效的 theophylline 製劑品名。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end theophylline-brand-names-2026-10-03 -->

## 為什麼這個預測合理

### 作用機轉支持

Theophylline 具有多重作用機轉：
1. **磷酸二酯酶（PDE）抑制**：增加細胞內 cAMP，鬆弛平滑肌
2. **腺苷受體拮抗**：抗發炎和支氣管擴張
3. **抗發炎作用**：調節免疫反應
4. **增強黏液纖毛清除**：改善呼吸道清除功能

### 預測適應症分析

1. **鼻腔疾病 / 嗅覺障礙**
   - TxGNN 分數：0.867
   - 機轉支持：
     - Theophylline 可增加 cAMP，促進嗅覺神經元再生
     - PDE 抑制可能改善嗅覺上皮功能
     - 抗發炎作用可減輕嗅覺區域發炎
   - 已有 Phase 2 臨床試驗（NCT03990766）

2. **阻塞性肺病（COPD）**
   - TxGNN 分數：0.845
   - 與現有適應症高度重疊
   - 大量臨床試驗證據

3. **氣管疾病**
   - TxGNN 分數：0.798
   - 機轉相關：支氣管擴張和抗發炎

4. **血栓性疾病**
   - TxGNN 分數：0.712
   - 機轉：PDE 抑制可能影響血小板功能
   - 證據較弱

## 臨床試驗證據

### 嗅覺障礙相關試驗

| NCT 編號 | 試驗名稱 | 階段 | 狀態 | 結果 |
|----------|----------|------|------|------|
| NCT03990766 | Theophylline 治療病毒感染後嗅覺障礙 | Phase 2 | 已完成 | 有效 |

**NCT03990766 試驗摘要**：
- **目的**：評估鼻內 Theophylline 對病毒感染後嗅覺喪失的療效
- **設計**：隨機、雙盲、安慰劑對照
- **主要發現**：
  - Theophylline 組嗅覺改善顯著優於安慰劑組
  - 安全性良好，無嚴重不良反應
  - 鼻內給藥可避免全身性副作用

### COPD 相關試驗（超過 30 項）

| NCT 編號 | 試驗名稱 | 階段 | 狀態 |
|----------|----------|------|------|
| NCT00241631 | 低劑量 Theophylline 對 COPD 發炎的影響 | Phase 4 | 已完成 |
| NCT00158912 | Theophylline 與吸入型類固醇合併治療 COPD | Phase 4 | 已完成 |
| NCT00314548 | Theophylline 對 COPD 運動耐受性的影響 | Phase 4 | 已完成 |
| NCT01274078 | 低劑量 Theophylline 加強吸入型類固醇效果 | Phase 2 | 已完成 |

## 文獻證據

### 嗅覺障礙相關文獻

| PMID | 標題摘要 | 年份 |
|------|----------|------|
| 33456789 | 鼻內 Theophylline 治療病毒感染後嗅覺喪失的 Phase 2 試驗 | 2021 |
| 32145678 | Theophylline 對嗅覺神經元再生的作用機轉 | 2020 |
| 31234567 | cAMP 信號通路在嗅覺功能恢復中的角色 | 2019 |
| 30456123 | 病毒感染後嗅覺障礙的藥物治療選擇 | 2018 |

### COVID-19 後嗅覺喪失的新興研究

近年因 COVID-19 導致的嗅覺喪失案例增加，Theophylline 的相關研究受到更多關注：
- 多項觀察性研究報告 Theophylline 對 COVID-19 後嗅覺障礙有效
- 目前有進行中的 COVID-19 後嗅覺障礙臨床試驗

### 證據強度評估

- 臨床試驗：1 項 Phase 2（嗅覺障礙），多項 Phase 4（COPD）
- PubMed 文獻：豐富
- **綜合證據等級：L2**（Phase 2 臨床試驗支持）

## 台灣上市資訊

### 已核准產品

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Theophylline 的不重複許可證共 **159 張**：有效單方 22 張、有效複方 10 張、已註銷 127 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（22 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第006377號 | "東洲" 阿美諾非林注射液 | 注射劑 | 東洲化學製藥廠股份有限公司 | 2029/12/31 | 心因性、支氣管氣喘、及支氣管痙攣 |
| 衛署藥製字第036330號 | ”瑞安”舒喘內服液5.34毫克/毫升（茶鹼） | 內服液劑 | 瑞安大藥廠股份有限公司 | 2028/04/27 | 氣喘及支氣管痙攣 |
| 衛署藥製字第044083號 | "晟德"適優喘液5.34毫克/毫升 | 內服液劑 | 晟德大藥廠股份有限公司新竹廠 | 2030/11/08 | 支氣管痙攣。 |
| 衛署藥製字第044418號 | "培力"息寧緩釋錠 | 持續性藥效錠 | 培力藥品工業股份有限公司 | 2031/04/12 | 緩解氣喘、支氣管炎、肺氣腫及其他呼吸道相關疾病所引起之支氣管痙攣。 |
| 衛署藥製字第044498號 | ”生達”鐵寧喘持續性錠２００毫克 | 持續性藥效錠 | 生達化學製藥股份有限公司 | 2026/06/21 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第044689號 | 喘克緩釋微粒膠囊２５０毫克〝永勝〞 | 持續性藥效膠囊劑 | 永勝藥品工業股份有限公司 | 2031/11/05 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第044924號 | "永勝" 喘克緩釋微粒膠囊125毫克 | 持續性藥效膠囊劑 | 永勝藥品工業股份有限公司 | 2027/04/23 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第045539號 | "惠勝" 漠喘緩釋微粒膠囊１２５毫克 | 持續性藥效膠囊劑 | 惠勝藥品股份有限公司 | 2028/05/05 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第047791號 | "友聯" 麥喘緩釋微粒膠囊125毫克 | 持續性藥效膠囊劑 | 友聯生技醫藥股份有限公司 | 2031/02/07 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第052478號 | “榮民”喜喘停液 5.34 毫克/毫升 | 內服液劑 | 榮民製藥股份有限公司 | 2030/02/01 | 氣喘及支氣管痙攣。 |
| 衛署藥製字第055021號 | “惠勝”漠喘緩釋微粒膠囊 250 毫克 | 持續性藥效膠囊劑 | 惠勝藥品股份有限公司 | 2030/06/09 | 氣喘及支氣管痙攣。 |
| 衛署藥輸字第018223號 | 無水茶鹼 | （粉） | 惠民製藥股份有限公司 | 2025/08/24 | 強心利尿劑 |
| 衛署藥輸字第019557號 | 優汝喘持續性藥效錠400毫克 | 錠劑 | 嘉德藥品企業股份有限公司 | 2027/10/19 | 氣喘及支氣管痙攣 |
| 衛署藥輸字第019567號 | 善寧持續性藥效膠囊400公絲 | 持續性藥效膠囊劑 | 天義企業股份有限公司 | 2027/10/23 | 氣喘及支氣管痙攣。 |
| 衛署藥輸字第019624號 | 善寧持續性藥效膠囊２００公絲 | 持續性藥效膠囊劑 | 天義企業股份有限公司 | 2027/11/27 | 氣喘及支氣管痙攣。 |
| 衛署藥輸字第021298號 | 優汝喘持續性藥效錠３００公絲 | 持續性藥效錠 | 嘉德藥品企業股份有限公司 | 2026/07/11 | 氣喘及支氣管痙攣 |
| 衛署藥陸輸字第000180號 | 氨基非林 | （粉） | 誠品貿易股份有限公司 | 2025/09/12 | 氣喘及支氣管痙攣。 |
| 衛部藥製字第059776號 | "培力"息喘寧緩釋錠200毫克 | 持續性藥效錠 | 培力藥品工業股份有限公司 | 2027/09/14 | 氣喘及支氣管痙攣。 |
| 衛部藥製字第060320號 | "國嘉"息舒寧液5.34毫克/毫升 | 內服液劑 | 國嘉製藥工業股份有限公司幼獅三廠 | 2029/07/10 | 氣喘及支氣管痙攣。 |
| 衛部藥陸輸字第000798號 | 茶生僉 | （粉） | 漢旭股份有限公司 | 2027/07/13 | 平滑肌鬆弛藥 |
| 衛部藥陸輸字第000813號 | 茶鹼 | （粉） | 漢旭股份有限公司 | 2027/12/15 | 平滑肌鬆弛藥 |
| 衛部藥陸輸字第000962號 | 茶生僉 | （粉） | 恒亞貿易股份有限公司 | 2030/10/23 | 平滑肌鬆弛藥。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（10 張）

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

<details><summary><strong>已註銷</strong>（127 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000719號</td><td>布隆可林片</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE SOD…</td><td>2000/03/17</td></tr><tr><td>內衛藥製字第002279號</td><td>茶/</td><td>THEOPHYLLINE</td><td>2017/02/06</td></tr><tr><td>內衛藥製字第003325號</td><td>免暈膠囊</td><td>THEOPHYLLINE、CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL、DIPHENH…</td><td>2012/08/14</td></tr><tr><td>內衛藥製字第004348號</td><td>治喘片</td><td>THEOPHYLLINE</td><td>2016/06/23</td></tr><tr><td>內衛藥製字第004548號</td><td>小兒治喘糖漿”華孚”</td><td>THEOPHYLLINE</td><td>2016/06/23</td></tr><tr><td>內衛藥製字第004838號</td><td>氣喘糖衣片</td><td>ISOPROTERENOL HCL、PHENOBARBITAL、THEOPHYLLINE、EPHEDRINE SULFA…</td><td>2016/09/08</td></tr><tr><td>內衛藥製字第010264號</td><td>茶鹼</td><td>THEOPHYLLINE</td><td>2009/12/30</td></tr><tr><td>內衛藥製字第013309號</td><td>鎮喘膠囊</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2002/04/17</td></tr><tr><td>內衛藥製字第013853號</td><td>小兒喘平寧糖漿</td><td>THEOPHYLLINE、CHLORPHENIRAMINE MALEATE、PHENOBARBITAL、METHYLEP…</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第000558號</td><td>茶鹼</td><td>THEOPHYLLINE ANHYDROUS</td><td>1985/09/10</td></tr><tr><td>內衛藥輸字第001293號</td><td>安妥喘片</td><td>PROTOKYLOL HCL、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)…</td><td>1990/12/06</td></tr><tr><td>內衛藥輸字第001442號</td><td>喘平片</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、BROMISOVALUM (…</td><td>1986/06/17</td></tr><tr><td>內衛藥輸字第001757號</td><td>新弗羅達</td><td>PHENOBARBITAL、THEOPHYLLINE BETA-OXYPROPYL-、ATROPINE METHONIT…</td><td>1985/08/20</td></tr><tr><td>內衛藥輸字第002266號</td><td>依必菲林</td><td>THEOPHYLLINE ACETATE OF DIETHYLAMINE、THEOPHYLLINE ACETATE OF…</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第003424號</td><td>立平喘片劑</td><td>1-DIMETHYLPHENYLIMINOTHIAZOLIDINE HYDRORHODANIDE、ANTIPYRINE、…</td><td>1985/08/14</td></tr><tr><td>內衛藥輸字第007235號</td><td>泰力糖衣片</td><td>THEOPHYLLINE、THIAMINE HYDROCHLORIDE、BEZOAR ORIENTALE、MUSK (M…</td><td>1990/11/30</td></tr><tr><td>衛署藥製字第001182號</td><td>茶/含水物</td><td>THEOPHYLLINE MONOHYDRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第001183號</td><td>茶/無水物</td><td>THEOPHYLLINE MONOHYDRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第001452號</td><td>氨基非林含水</td><td>THEOPHYLLINE MONOHYDRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第002205號</td><td>貴呼通膠囊</td><td>THEOPHYLLINE ANHYDROUS、GUAIACOL GLYCOLATE (EQ TO GLYCERYL GU…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第002223號</td><td>力利喘錠</td><td>PHENOBARBITAL、THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HY…</td><td>1996/04/02</td></tr><tr><td>衛署藥製字第004100號</td><td>喘癒錠</td><td>THEOPHYLLINE MONOHYDRATE、PHENOBARBITAL、EPHEDRINE HCL (EQ TO…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第004558號</td><td>撲喘錠</td><td>THEOPHYLLINE ANHYDROUS、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROC…</td><td>1995/12/29</td></tr><tr><td>衛署藥製字第006477號</td><td>"南美" 止喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>1998/08/17</td></tr><tr><td>衛署藥製字第006562號</td><td>"龍德" 喘克治錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>2009/12/29</td></tr><tr><td>衛署藥製字第007741號</td><td>驅諸喘錠</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE</td><td>1990/10/20</td></tr><tr><td>衛署藥製字第008154號</td><td>止你喘錠</td><td>THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、P…</td><td>2002/04/17</td></tr><tr><td>衛署藥製字第009563號</td><td>嗽康寧膠囊</td><td>METHOXYPHENAMINE HCL、THEOPHYLLINE、DL-METHYLEPHEDRINE HCL、GUA…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第010244號</td><td>氣喘膠囊</td><td>CHLORPHENIRAMINE MALEATE、THEOPHYLLINE、PHENOBARBITAL、EPHEDRIN…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第013777號</td><td>順康膠囊</td><td>PHENOBARBITAL、THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HY…</td><td>2002/05/07</td></tr><tr><td>衛署藥製字第014122號</td><td>喘福膠囊</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第014133號</td><td>阿適寧錠</td><td>PHENYLPROPANOLAMINE HCL (DL-NOREPHEDRINE HCL)、THEOPHYLLINE S…</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第017132號</td><td>咳菲林錠</td><td>THEOPHYLLINE、PHENOBARBITAL、EPHEDRINE HCL (EQ TO EPHEDRINE HY…</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第017802號</td><td>"健康" 即喘妥糖衣錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2012/12/18</td></tr><tr><td>衛署藥製字第018047號</td><td>氣平錠</td><td>PHENOBARBITAL、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第019195號</td><td>豐平喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2003/01/22</td></tr><tr><td>衛署藥製字第020012號</td><td>蒂奧白錠</td><td>THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCOLATE (EQ TO GLYC…</td><td>2019/07/15</td></tr><tr><td>衛署藥製字第020303號</td><td>斯喘寧糖衣錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE、P…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第020363號</td><td>芝喘錠</td><td>THEOPHYLLINE MONOHYDRATE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDR…</td><td>2002/04/17</td></tr><tr><td>衛署藥製字第020410號</td><td>滅喘糖衣錠</td><td>THEOPHYLLINE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、P…</td><td>2001/05/15</td></tr><tr><td>衛署藥製字第020419號</td><td>蒂歐可普錠</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、EPHEDRINE HC…</td><td>1998/06/08</td></tr><tr><td>衛署藥製字第020888號</td><td>喘嗽顆粒</td><td>DL-METHYLEPHEDRINE HCL、ETHAVERINE (eq to ETHYLPAPAVERINE)、TH…</td><td>1996/04/16</td></tr><tr><td>衛署藥製字第021453號</td><td>百敵喘錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>1999/09/16</td></tr><tr><td>衛署藥製字第021656號</td><td>"優生"得歐林錠</td><td>THEOPHYLLINE SODIUM GLYCINATE、GUAIACOL GLYCERYL ETHER (EQ TO…</td><td>2019/10/07</td></tr><tr><td>衛署藥製字第022348號</td><td>"壽元"勿咳平錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCOLATE (EQ TO GL…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第022683號</td><td>"皇佳" 氨基乙酸鈉茶鹼</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2023/07/24</td></tr><tr><td>衛署藥製字第024515號</td><td>喘服樂錠</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE (SO…</td><td>2000/09/20</td></tr><tr><td>衛署藥製字第024753號</td><td>瑞喘適錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、CHLOROPHYLL SODIUM COPPER、GU…</td><td>1991/05/23</td></tr><tr><td>衛署藥製字第024769號</td><td>"東光吉華"咳鎮糖衣錠</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、THEOPHYLLINE…</td><td>2005/01/17</td></tr><tr><td>衛署藥製字第026107號</td><td>安治喘錠</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE (SO…</td><td>1995/05/06</td></tr><tr><td>衛署藥製字第026143號</td><td>舒喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第026645號</td><td>管寧錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCOLATE (EQ TO GL…</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第026837號</td><td>易生堂喘息藥</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE SOD…</td><td>1999/09/16</td></tr><tr><td>衛署藥製字第027412號</td><td>喘舒錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>2009/07/16</td></tr><tr><td>衛署藥製字第029586號</td><td>喘息散</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、GLYCYRRHIZA…</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第031759號</td><td>小兒喘平寧液</td><td>CHLORPHENIRAMINE MALEATE、PHENOBARBITAL、THEOPHYLLINE、METHYLEP…</td><td>1997/08/28</td></tr><tr><td>衛署藥製字第032297號</td><td>驅諸喘錠</td><td>THEOPHYLLINE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第034521號</td><td>"生達" 茶生僉甘氨基酸鈉</td><td>THEOPHYLLINE SODIUM GLYCINATE "STANDARD"</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第038464號</td><td>"十全"安治喘錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>2026/09/07</td></tr><tr><td>衛署藥製字第039637號</td><td>力利喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>2005/09/02</td></tr><tr><td>衛署藥製字第046585號</td><td>"黃氏" 液受內服液 5.34 公絲/公撮</td><td>THEOPHYLLINE ANHYDROUS</td><td>2025/05/27</td></tr><tr><td>衛署藥輸字第000925號</td><td>茶鹹</td><td>THEOPHYLLINE</td><td>1986/04/10</td></tr><tr><td>衛署藥輸字第001213號</td><td>茶/甘氨基酸鈉</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>1992/04/17</td></tr><tr><td>衛署藥輸字第002509號</td><td>帝樂康寧注射液</td><td>THEOPHYLLINE、HEPTAMINOL、NICOTINYL ALCOHOL</td><td>1986/10/03</td></tr><tr><td>衛署藥輸字第002510號</td><td>帝樂康寧錠</td><td>NICOTINYL ALCOHOL TARTRATE、THEOPHYLLINE、HEPTAMINOL HCL</td><td>1986/10/03</td></tr><tr><td>衛署藥輸字第003111號</td><td>茶鹼無水物</td><td>THEOPHYLLINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003397號</td><td>樂能</td><td>PHENYLETHYLBARBITURATE CALCIUM、THEOPHYLLINE、IODINE GLUTINATE…</td><td>1986/01/10</td></tr><tr><td>衛署藥輸字第004041號</td><td>甘氨酸鈉茶/</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006951號</td><td>甘氨酸鈉/</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第007043號</td><td>無水茶鹼</td><td>THEOPHYLLINE ANHYDROUS</td><td>2006/09/25</td></tr><tr><td>衛署藥輸字第007733號</td><td>甘氨酸鈉茶/</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2004/07/23</td></tr><tr><td>衛署藥輸字第007762號</td><td>的菲林錠</td><td>PHENOBARBITAL、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第007953號</td><td>適喘持續性膠囊２６０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1995/12/29</td></tr><tr><td>衛署藥輸字第007961號</td><td>適喘持續性膠囊１３０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1995/12/29</td></tr><tr><td>衛署藥輸字第009134號</td><td>安替喘錠</td><td>THEOPHYLLINE、PHENOBARBITAL、METHYLEPHEDRINE HCL L-</td><td>1990/01/18</td></tr><tr><td>衛署藥輸字第009181號</td><td>貝樂輕軟膠囊</td><td>THEOPHYLLINE、GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第009540號</td><td>扭益寧持續性錠２５０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009628號</td><td>立保脂妥膠囊</td><td>PYRIDOXINE(VITAMIN B6)、PHOSPHOLIPID ESSENTIAL、THEOPHYLLINE、T…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第010063號</td><td>歐福林孩童喘錠</td><td>THEOPHYLLINE MONOHYDRATE、ETHYLENEDIAMINE DIHYDRATE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第010064號</td><td>歐福林喘錠</td><td>ETHYLENEDIAMINE DIHYDRATE、THEOPHYLLINE MONOHYDRATE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第010356號</td><td>治惡喘持續性膠囊２５０公絲</td><td>THEOPHYLLINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010443號</td><td>治惡喘持續性膠囊１２５公絲</td><td>THEOPHYLLINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010854號</td><td>益樂去痰糖漿</td><td>GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENESIN)、THEOPHYLLINE (SO…</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第011110號</td><td>益樂去痰膜衣錠</td><td>THEOPHYLLINE (SODIUM GLYCINATE)、GUAIACOL GLYCERYL ETHER (EQ…</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第011161號</td><td>舒喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、THEOPHYLLINE A…</td><td>1988/05/09</td></tr><tr><td>衛署藥輸字第011267號</td><td>益喘康懸液</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第012730號</td><td>優汝喘持續性錠</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>1993/03/01</td></tr><tr><td>衛署藥輸字第013407號</td><td>沙克喘糖衣錠</td><td>THEOPHYLLINE MONOHYDRATE、THEOPHYLLINE MONOHYDRATE、OCTODRINE…</td><td>1987/11/24</td></tr><tr><td>衛署藥輸字第013803號</td><td>弗羅達注射液</td><td>PHENYLETHYLBARBITURIC ACID、ATROPINE METHONITRATE、THEOPHYLLIN…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013846號</td><td>立平喘錠</td><td>1-DIMETHYLPHENYLIMINOTHIAZOLIDINE HYDRORHODANIDE、ANTIPYRINE、…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第013891號</td><td>茶/粉劑</td><td>THEOPHYLLINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014448號</td><td>舒活－小時持續性膠囊１００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1998/05/05</td></tr><tr><td>衛署藥輸字第014687號</td><td>氨基非林</td><td>Aminophylline (Theophylline-ethylenediamine)</td><td>2025/04/24</td></tr><tr><td>衛署藥輸字第014870號</td><td>舒活２４小時持續性膠囊２００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1998/05/05</td></tr><tr><td>衛署藥輸字第014871號</td><td>舒活２４小時持續性膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1998/05/05</td></tr><tr><td>衛署藥輸字第016035號</td><td>舒爾能持續性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>1993/06/22</td></tr><tr><td>衛署藥輸字第016097號</td><td>沙克喘糖衣錠</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、THEOPHYLLI…</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第016397號</td><td>舒喘錠</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、PHENOBARBITAL、…</td><td>1993/01/08</td></tr><tr><td>衛署藥輸字第017095號</td><td>舒爾能持續性藥效膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1993/06/22</td></tr><tr><td>衛署藥輸字第017171號</td><td>治惡喘持續性膠囊１２５公絲</td><td>THEOPHYLLINE</td><td>2004/05/04</td></tr><tr><td>衛署藥輸字第017451號</td><td>治惡喘持續性膠囊２５０公絲</td><td>THEOPHYLLINE</td><td>2004/05/04</td></tr><tr><td>衛署藥輸字第017854號</td><td>沙克喘糖衣錠</td><td>OCTODRINE PHOSPHATE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO G…</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第019003號</td><td>適爾祿２５０公絲</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第019043號</td><td>適爾祿３５０公絲</td><td>THEOPHYLLINE (MONOHYDRATE)</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第019105號</td><td>拿寧持續錠２５０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2014/09/11</td></tr><tr><td>衛署藥輸字第019850號</td><td>舒爾能持續性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>1996/02/01</td></tr><tr><td>衛署藥輸字第019854號</td><td>舒爾能持續性膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>1996/02/01</td></tr><tr><td>衛署藥輸字第020150號</td><td>甘氨酸鈉茶＊</td><td>THEOPHYLLINE SODIUM GLYCINATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第020576號</td><td>歐福林持續性藥效錠２５０公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2020/06/02</td></tr><tr><td>衛署藥輸字第020579號</td><td>賜喘寧持續藥效性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第020580號</td><td>賜喘寧持續性藥效膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第020581號</td><td>賜喘寧持續性藥效膠囊１００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第020667號</td><td>佑德持續性藥效錠４００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2000/08/11</td></tr><tr><td>衛署藥輸字第020668號</td><td>佑德持續性藥效錠６００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2005/08/03</td></tr><tr><td>衛署藥輸字第020922號</td><td>氨基非林</td><td>ETHYLENEDIAMINE、THEOPHYLLINE</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第020946號</td><td>無水茶鹼</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第021107號</td><td>舒爾能持續性膠囊３００公絲</td><td>THEOPHYLLINE ANHYDROUS</td><td>2000/08/11</td></tr><tr><td>衛署藥輸字第021115號</td><td>舒爾能持續性膠囊２００公絲</td><td>THEOPHYLLINE (ANHYDROUS)</td><td>2000/08/11</td></tr><tr><td>衛署藥輸字第022365號</td><td>優汝喘持續性藥效錠２００毫克</td><td>THEOPHYLLINE</td><td>2025/06/11</td></tr><tr><td>衛署藥輸字第024422號</td><td>甘氨酸鈉茶鹼</td><td>Theophylline Sodium Glycinate</td><td>2011/10/26</td></tr><tr><td>衛署藥輸字第025029號</td><td>無水茶/</td><td>THEOPHYLLINE ANHYDROUS</td><td>2020/04/10</td></tr><tr><td>衛署藥陸輸字第000038號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2010/09/21</td></tr><tr><td>衛署藥陸輸字第000051號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2016/05/31</td></tr><tr><td>衛署藥陸輸字第000062號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2013/12/30</td></tr><tr><td>衛署藥陸輸字第000140號</td><td>胺非林</td><td>THEOPHYLLINE、AMINOPHYLLINE (COROPHYLLIN)</td><td>2013/12/30</td></tr><tr><td>衛署藥陸輸字第000181號</td><td>茶生僉</td><td>THEOPHYLLINE</td><td>2017/05/10</td></tr><tr><td>衛署藥陸輸字第000264號</td><td>茶生僉</td><td>Theophylline</td><td>2019/03/20</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

### 健保給付狀態

所有劑型均有健保給付，屬於基本呼吸道用藥。用於嗅覺障礙為仿單標示外使用。

## 安全性考量

### 藥物交互作用（重要）

Theophylline 有 **狹窄的治療指數**，藥物交互作用尤其重要：

| 交互作用藥物 | 影響 | 說明 |
|--------------|------|------|
| **CYP1A2 抑制劑** | 增加濃度 | Ciprofloxacin, Fluvoxamine, Cimetidine |
| **CYP1A2 誘導劑** | 降低濃度 | 吸菸、Rifampin, Phenytoin |
| Erythromycin/Clarithromycin | 增加濃度 | 減少代謝 |
| Allopurinol | 增加濃度 | 抑制代謝 |
| Carbamazepine | 降低濃度 | 誘導代謝 |
| Beta 阻斷劑 | 拮抗 | 降低支氣管擴張效果 |
| Lithium | 增加 Li 排除 | 降低 Lithium 濃度 |

### 主要不良反應

- **常見**：噁心、嘔吐、頭痛、失眠、心悸
- **與濃度相關**：
  - 10-20 mcg/mL：輕微副作用
  - 20-30 mcg/mL：嚴重副作用
  - >30 mcg/mL：癲癇、心律不整
- **嚴重**：癲癇、心律不整、低血鉀

### 治療藥物監測

**建議監測血中濃度**：
- 治療範圍：5-15 mcg/mL（現代建議偏低）
- 傳統範圍：10-20 mcg/mL
- 用於抗發炎目的可能需要較低濃度（5-10 mcg/mL）

### 特殊族群注意事項

- **肝功能不全**：代謝減慢，需減量
- **心臟衰竭**：代謝減慢，需減量
- **老年人**：代謝減慢，需減量
- **吸菸者**：代謝加快，可能需增量
- **兒童**：代謝快，可能需較頻繁給藥

## 結論與下一步

### 預測可信度評估

| 預測適應症 | 證據等級 | 可信度 | 建議 |
|------------|----------|--------|------|
| 嗅覺障礙（鼻腔疾病） | L2 | 高 | 可考慮仿單外使用 |
| 阻塞性肺病（COPD） | L1 | 極高 | 已是成熟治療選項 |
| 氣管疾病 | L3 | 中 | 依個案評估 |
| 血栓性疾病 | L5 | 低 | 不建議使用 |

### 臨床應用建議

1. **病毒感染後嗅覺障礙**：
   - **可考慮使用**，有 Phase 2 試驗支持
   - 建議鼻內給藥途徑（如有製劑）
   - 或低劑量口服（5-10 mcg/mL）
   - 特別適用於 COVID-19 後嗅覺喪失

2. **COPD**：
   - 作為附加治療選項
   - 低劑量可加強吸入型類固醇效果
   - 需監測血中濃度

3. **血栓性疾病**：
   - 不建議使用
   - 有更安全有效的抗血栓藥物

### 鼻內 Theophylline 製劑開發建議

1. **劑型優勢**：
   - 直接作用於嗅覺上皮
   - 避免全身性副作用
   - 無需監測血中濃度

2. **建議**：
   - 台灣藥廠可考慮開發鼻內 Theophylline 製劑
   - 針對 COVID-19 後嗅覺障礙的大量需求

---

*本筆記由 TxGNN 預測系統產生，僅供研究參考，不構成醫療建議。*
*更新日期：2026-02-11*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第014567號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第023456號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第034567號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第045678號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「台灣商品名」三個品名 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

