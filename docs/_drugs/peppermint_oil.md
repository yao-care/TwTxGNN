---
layout: default
title: Peppermint Oil
parent: 中證據等級 (L3-L4)
nav_order: 197
evidence_level: L3
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil（薄荷油）：從外用止痛到心血管疾病

## 一句話總結

薄荷油（Peppermint Oil，如意油）是台灣傳統常備藥物，原本以外用劑型廣泛用於跌打損傷、肌肉痛、神經痛等止痛用途，部分劑型亦可內服緩解腸胃不適。
TxGNN 模型共提出 10 項新適應症預測，其中唯一具有臨床試驗支持的是**心血管疾病（Cardiovascular Disease）**，TxGNN 分數達 **99.13%**，
目前有 **2 個已完成的隨機試驗**（共 76 名受試者）及 **8 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腳部跌打、腰背痠痛、止痛消腫、外用傷口護理（如意油） |
| 預測新適應症 | 心血管疾病（Cardiovascular Disease） |
| TxGNN 預測分數 | 99.13% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 37 張（有效單方 3／有效複方 8／已註銷 26） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin peppermint_oil-original-indication-combo-2026-10-03 -->

> **查核加註（2026-10-03）**：此為複方許可證的適應症（內衛成製字第003166號「如意油」，含丁香油、桂皮油、麻油與薄荷油），該證已於 1998-01-12 註銷，不是薄荷油單方的適應症；現行單方許可證例如衛部成製字第016950號「洸洋」藥用薄荷油，核准切傷、刀傷、創傷、火傷、蟲咬傷、頭暈。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end peppermint_oil-original-indication-combo-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏 Peppermint Oil 的詳細作用機轉資料（DrugBank MOA 尚無記錄）。根據已知資訊，Peppermint Oil 是以**薄荷醇（Menthol）**和**薄荷酮（Menthone）**為主的萜烯類天然精油，並含有多酚類黃酮成分；其在外用止痛與消化道不適中的療效已有長期臨床使用依據。

薄荷醇是 TRPM8（Transient Receptor Potential Melastatin 8）冷感受器的天然活化劑。已有生理學佇列研究（PMID 30070742）直接驗證：薄荷醇刺激胃部後，可顯著增強心臟副交感神經活性（迷走神經張力上升）並降低心率。這一機轉在理論上可延伸至調節周邊血管張力，為血壓改善提供生物學基礎。

此外，薄荷油中的多酚類抗氧化成分可能有助於降低氧化應激、改善血管內皮功能與血脂指標，進一步強化心血管保護的生物學合理性。以上機轉推論已促成近年兩項針對高血壓受試者的隨機對照試驗（NCT05071833、NCT05561543），兩者均已完成收案。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05071833](https://clinicaltrials.gov/study/NCT05071833) | NA | 已完成 | 36 | 口服薄荷補充劑對心臟代謝參數（血壓、血脂、血糖等）之隨機試驗；前期非隨機干預已顯示潛在改善效益 |
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | NA | 已完成 | 40 | 薄荷油對輕中度高血壓患者心臟代謝指標的影響；為 NCT05071833 的延伸隨機試驗，前期數據顯示收縮壓與血脂指標有改善趨勢 |

> NCT04966546（硬膜下血腫術後擴散性去極化研究，已撤回，n=0）與薄荷油或心血管疾病無直接關聯，不納入分析。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | RCT Protocol | PLoS One | 薄荷油用於前高血壓與第一期高血壓患者之安慰劑對照 RCT 計畫書；薄荷醇與類黃酮成分具潛在降壓效益 |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Cohort | Exp Physiology | 薄荷醇與胃部冷卻共同作用可顯著增強心臟副交感神經活性、降低心率，直接驗證 TRPM8 介導的心臟自律調節機轉 |
| [25037671](https://pubmed.ncbi.nlm.nih.gov/25037671/) | 2014 | Review | Explore | 多種替代療法系統回顧，含薄荷油用於腸躁症的評估；心血管直接相關性有限，提供背景脈絡 |
| [27277875](https://pubmed.ncbi.nlm.nih.gov/27277875/) | 2016 | In vitro | Bioanalysis | 口服薄荷油膠囊後呼氣薄荷酮的即時質譜監測，提供口服吸收與代謝動力學基礎數據 |
| [19198983](https://pubmed.ncbi.nlm.nih.gov/19198983/) | 2009 | Review | Int Emerg Med | 一般科與心血管科新興證據回顧，背景文獻 |

> PMID 39139335、28889028 係以薄荷油作為藥物傳輸系統的賦形劑（自乳化系統），非直接療效評估；PMID 17577363 為接觸性皮膚炎病例報告，均不納入主要分析。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Peppermint Oil 的不重複許可證共 **37 張**：有效單方 3 張、有效複方 8 張、已註銷 26 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署成製字第011018號 | 〝派頓〞廣益油 | 外用液劑 | 臺灣派頓化學製藥股份有限公司 | 2029/06/21 | 外用：蟲咬傷、頭暈、頭痛、肌肉痛、牙神經痛及口腔黏膜發炎。內服：緩解腸胃道所引起之不適。吸入：緩解感冒之鼻塞症狀。 |
| 衛署藥製字第000664號 | "應元"薄荷水 | 外用液劑 | 應元化學製藥股份有限公司 | 2029/05/25 | 液劑之矯味、矯臭劑、驅風劑 |
| 衛部成製字第016950號 | "洸洋"藥用薄荷油 | 外用液劑 | 洸洋化學製藥股份有限公司 | 2028/01/10 | 切傷、刀傷、創傷、火傷、蟲咬傷、頭暈。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（8 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第001049號 | "美"解癢藥膏 | PHENOL (CARBOLIC ACID)、METHYL SALICYLATE、DL-METHYLEPHEDRINE… | 軟膏劑 | 急、慢性濕疹、皮膚搔癢症、汗疹、癢疹、蕁麻疹、肛門陰部部搔癢症、蚊蟲咬刺傷、痱子疹 |
| 衛署成製字第005716號 | "德山"青皮藥膠布 | METHYL SALICYLATE、L-MENTHOL、PEPPERMINT OIL (OLEUM MENTH PIP)… | 藥膠布 | 神經痛、腰痛、打撲痛、筋肉痛、挫傷、腫脹、扭傷、肩膀酸痛、關節痛 |
| 衛署成製字第005910號 | "德山"象印膏藥膠布 | METHYL SALICYLATE、L-MENTHOL、ZINC OXIDE、PEPPERMINT OIL (OLEUM… | 藥膠布 | 肩痛、腰痛、打撲傷、肌肉痛、神經痛、齒痛、頭痛、關節痛之消炎鎮痛 |
| 衛署成製字第009417號 | “艾力特”金象油 | PEPPERMINT OIL (OLEUM MENTH PIP)、CLOVE OIL、L-MENTHOL、EUCALYP… | 軟膏劑 | 切傷、刀傷、創傷、蚊蟲咬傷、頭暈 |
| 衛署藥製字第021676號 | 諾得胃腸藥散 | CLOVE OIL、MAGNESIUM CARBONATE HEAVY、SWERTIA POWDER、SCOPOLIA… | 散劑 | 緩解胃部不適或灼熱感、或經診斷為胃及十二指腸潰瘍、胃炎、食道炎所伴隨之胃酸過多 |
| 衛署藥製字第023893號 | 晶涼軟膏 | PEPPERMINT OIL (OLEUM MENTH PIP)、D-CAMPHOR、CLOVE OIL、L-MENTH… | 軟膏劑 | 切傷、刀傷、創傷、火傷、蟲咬傷、頭暈 |
| 衛署藥製字第028231號 | "德山"祛風濕藥膠布 | MENTHOL、CAMPHOR、SCOPOLIA EXTRACT、PEPPERMINT OIL (OLEUM MENTH… | 藥膠布 | 神經痛、關節痛、風濕、打撲傷、腰痛、齒痛。 |
| 衛署藥製字第045173號 | "德山" 舒痠痛藥布 | EUCALYPTUS OIL (OLEUM EUCALYPTI)、CAMPHOR、L-MENTHOL、PEPPERMIN… | 藥膠布 | 打撲、捻挫、肌肉痛、肩膀痠痛、腰痛、關節痛、肌肉疲勞。 |

<details><summary><strong>已註銷</strong>（26 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛成製字第001012號</td><td>消腫膏</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、EUCALYPTUS OIL (OLEUM EUCAL…</td><td>2000/08/08</td></tr><tr><td>內衛成製字第003097號</td><td>虎標永安堂八卦丹</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、GLYCYRRHIZA POWDER</td><td>1992/10/28</td></tr><tr><td>內衛成製字第003166號</td><td>如意油</td><td>CLOVE OIL、CASSIA OIL、SESAME OIL、PEPPERMINT OIL (OLEUM MENTH…</td><td>1998/01/12</td></tr><tr><td>內衛藥輸字第000507號</td><td>薄荷油</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)</td><td>2005/06/16</td></tr><tr><td>內衛藥輸字第002925號</td><td>尼可散</td><td>PYRIDOXINE HCL、THIAMINE NITRATE、RIBOFLAVIN (VIT B2)、CINNAMON…</td><td>1986/06/14</td></tr><tr><td>衛署成製字第003328號</td><td>爭虎油</td><td>CLOVE OIL、PEPPERMINT OIL (OLEUM MENTH PIP)、ROSEMARY OIL (OLE…</td><td>1998/02/27</td></tr><tr><td>衛署成製字第003836號</td><td>百珍膏布</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、METHYL SALICYLATE、GARDENIA…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第004211號</td><td>金龍藥膏布</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、L-MENTHOL、THYMOL、GARDENIA F…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第004435號</td><td>黃金膏</td><td>DIPHENHYDRAMINE、METHYL SALICYLATE、PEPPERMINT OIL (OLEUM MENT…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第004906號</td><td>李施德美漱口藥水</td><td>ETHANOL ( EQ TO ETHYL ALCOHOL) (EQ TO ALCOHOL)、METHYL SALICY…</td><td>1998/07/06</td></tr><tr><td>衛署成製字第005021號</td><td>金象油</td><td>JASMINE OIL、PEPPERMINT OIL (OLEUM MENTH PIP)、CLOVE OIL、L-MEN…</td><td>1993/11/10</td></tr><tr><td>衛署成製字第005666號</td><td>大維貼痠痛藥布</td><td>METHYL SALICYLATE、OLIVE OIL、EUCALYPTUS OIL (OLEUM EUCALYPTI)…</td><td>2013/10/03</td></tr><tr><td>衛署成製字第005830號</td><td>耐斯藥膠布</td><td>PHELLODENDRON BARK POWDER (EQ TO POWDERED PHELLODENDRON BARK…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第006647號</td><td>疼痛膏</td><td>DL-CAMPHOR、THYMOL、MENTHOL、SALICYL ETHYLENE GLYCOL、PEPPERMINT…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第009123號</td><td>金獅牌香口丹</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、GLYCYRRHIZA (LIQUORICE)</td><td>1998/09/09</td></tr><tr><td>衛署成製字第009759號</td><td>薄荷李施德霖漱口水</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、METHYL SALICYLATE、SPEARMINT…</td><td>2007/05/09</td></tr><tr><td>衛署成製字第010407號</td><td>清涼油</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、CLOVE OIL、ANISE OIL、CINNAMO…</td><td>2022/05/05</td></tr><tr><td>衛署成製字第015032號</td><td>“杏輝”晶涼軟膏</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、L-MENTHOL、EUCALYPTUS OIL (O…</td><td>2023/07/07</td></tr><tr><td>衛署藥製字第009248號</td><td>咳香糖錠</td><td>THYME OIL、PEPPERMINT OIL (OLEUM MENTH PIP)、EUCALYPTUS OIL (O…</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第011334號</td><td>"三陽" 痠痛萬金膏</td><td>METHYL SALICYLATE、PHELLODENDRON EXTRACT、MENTHOL、CAMPHOR、CHLO…</td><td>2015/01/15</td></tr><tr><td>衛署藥製字第018223號</td><td>鎮痢懸浮液</td><td>KAOLIN (WHITE)(BOLUS ALBA)、BENZOIC ACID、PECTIN、PEPPERMINT OI…</td><td>1992/12/10</td></tr><tr><td>衛署藥製字第019683號</td><td>健樂仙壹錠</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、ALUMINUM HYDROXIDE DRIED GE…</td><td>2017/02/03</td></tr><tr><td>衛署藥製字第023884號</td><td>寶安藥膠布</td><td>EUCALYPTUS OIL (OLEUM EUCALYPTI)、SCOPOLIA EXTRACT、CAMPHOR、L-…</td><td>2015/01/15</td></tr><tr><td>衛署藥製字第027213號</td><td>健胃仙錠</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、SIMETHICONE (ACTIVE DIMETHI…</td><td>2023/06/30</td></tr><tr><td>衛署藥輸字第009198號</td><td>莎膚納軟膏</td><td>CAMPHOR、L-MENTHOL、PEPPERMINT OIL (OLEUM MENTH PIP)、DIPHENHYD…</td><td>2022/07/20</td></tr><tr><td>衛署藥輸字第010094號</td><td>維時利軟膠囊</td><td>INOSITOL (MESO-INOSITOL)、VITAMIN B1 (MONONITRATE)、ASCORBATE…</td><td>2020/04/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
兩項已完成的小型隨機試驗（共 76 名受試者）直接測試薄荷油對高血壓患者心臟代謝指標的影響，薄荷醇活化 TRPM8 的生理學機轉亦有佇列研究佐證。然而目前證據等級僅 L3、樣本數偏小，且完整試驗結果尚待正式發表，暫不宜直接進入臨床應用，應在更嚴格的研究設計下推進驗證。

**若要推進需要：**
- 取得 NCT05071833 與 NCT05561543 兩項已完成試驗的完整數據（主要終點、安全性與不良事件）
- 補充 DrugBank MOA 資訊，特別是薄荷醇與 TRPM8 受體的結合動力學數據
- 確認最適有效給藥途徑（口服膠囊 vs 吸入）與劑量範圍
- 規劃至少 1 個樣本數充足的 Phase 2 RCT，設定明確的心血管終點（如收縮壓變化 ≥ 5 mmHg）
- 評估長期口服薄荷油的安全性，尤其是肝功能監測（部分萜烯類精油有潛在肝毒性疑慮）

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」取自如意油 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

