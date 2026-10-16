---
layout: default
title: Magnesium Sulfate
parent: 高證據等級 (L1-L2)
nav_order: 172
evidence_level: L1
indication_count: 10
---

# Magnesium Sulfate
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Magnesium sulfate：從子癇症與緩瀉 到 子癇前症／子癇

## 一句話總結

硫酸鎂（Magnesium sulfate）在台灣原本用於子癇症、子癇前症的預防與治療、體內鎂缺乏的補充，以及抗痙攣與緩瀉。
TxGNN 模型預測它對 **子癇前症／子癇 (preeclampsia/eclampsia)** 有效，目前有 **30 個臨床試驗**和 **19 篇文獻**支持這個方向，其中包含多項已完成的 Phase 2/3 及 Phase 4 隨機試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗痙攣藥；瀉藥 |
| 預測新適應症 | 子癇前症／子癇 (preeclampsia/eclampsia) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L1（資料彙整評級；已完成的 Phase 3 RCT 不足 2 個，但有已完成的 Phase 2/3 RCT 及多項 Phase 4 RCT，且臨床上為標準療法） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 117 張（有效單方 5／有效複方 14／已註銷 98） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin magnesium_sulfate-moa-2026-10-03 -->

## Magnesium Sulfate（硫酸鎂）的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

這份來源是注射劑仿單；口服當瀉劑時的作用方式不在這份仿單範圍內，本段不涵蓋。

- 鎂離子是許多酵素反應的輔因子，在神經化學傳導與肌肉興奮性上扮演重要角色。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)）
- 鎂能預防或控制抽搐，方式是阻斷神經肌肉傳導，並減少運動神經衝動在終板釋放的乙醯膽鹼量。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)）
- 鎂被認為對中樞神經系統有抑制作用。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)）
- 鎂在周邊會造成血管擴張：低劑量時只有潮紅與流汗，較大劑量會使血壓下降。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)）
- 靜脈注射時抗抽搐作用立即出現、約維持 30 分鐘；肌肉注射約 1 小時起效、維持 3 到 4 小時。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)）

**來源**：[DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira），Clinical Pharmacology 段](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)，版本日期 2026-08-24；查閱日期 2026-10-03。

---

<!-- review:end magnesium_sulfate-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中的 MOA 欄位為空）。根據資料彙整的機轉推論，硫酸鎂可拮抗 NMDA 受體、阻斷鈣離子通道，並促進腦血管擴張。這些作用能提高癲癇發作閾值，並對抗子癇時的血管痙攣。

<!-- review:begin magnesium-sulfate-cerebral-perfusion-2026-10-03 -->

> **查核加註（2026-10-03）**：仿單寫硫酸鎂藉阻斷神經肌肉傳導、減少運動神經末梢乙醯膽鹼釋放來預防或控制抽搐，另有中樞抑制與周邊血管擴張作用；本句的 NMDA 受體拮抗、阻斷鈣離子通道與「促進腦血管擴張」都不在仿單內（仿單寫的是周邊血管擴張）。預測的子癇前症／子癇症本身是仿單核准適應症，結論不受影響。原文保留。依據：[DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)。

<!-- review:end magnesium-sulfate-cerebral-perfusion-2026-10-03 -->

<!-- review:begin magnesium-sulfate-cerebral-perfusion-moa-missing-2026-10-16 -->

> **查核加註（2026-10-16）**：本頁「為什麼這個預測合理」上方已附有依仿單整理的作用機轉段（2026-10-03 查核新增）：阻斷神經肌肉傳導、減少乙醯膽鹼釋放、中樞抑制與周邊血管擴張。原文保留。依據：[DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)。

<!-- review:end magnesium-sulfate-cerebral-perfusion-moa-missing-2026-10-16 -->

台灣已核准的硫酸鎂注射液適應症，本來就包含「子癇症、子癇前症、妊娠毒血症、產科全身麻醉輔助」。所以這個預測與既有的核准用途相符，屬於以證據補強既有用途，而非全新的用途。

文獻也支持此看法：多篇回顧指出，硫酸鎂是預防與控制子癇抽搐的首選藥物，其療效與安全性已被長期記錄。

## 臨床試驗證據

資料中共有 30 筆相關試驗，以下列出關聯度最高的 10 筆：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | 完成 | 280 | 嚴重子癇前症產後硫酸鎂 6 小時 vs 24 小時（產前已用藥不足 8 小時者） |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | 完成 | 1114 | 產前已用藥超過 8 小時者，產後 24 小時 vs 不續用 |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | 完成 | 222 | 嚴重子癇前症維持劑量 1 g vs 2 g 的療效與安全性 |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | N/A | 完成 | 114 | 低劑量 vs 標準 Pritchard 療程用於嚴重子癇前症／子癇 |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | 完成 | 2000 | Nimodipine vs 硫酸鎂預防嚴重子癇前症的子癇發作 |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | 未知 | 100 | 產後繼續 vs 停用硫酸鎂 |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | 提前終止 | 62 | 維持劑量 1 g/h vs 2 g/h 預防子癇 |
| [NCT06486025](https://clinicaltrials.gov/study/NCT06486025) | Phase 1/2 | 未知 | 100 | 過重及肥胖子癇前症婦女的替代劑量方案 |
| [NCT03412552](https://clinicaltrials.gov/study/NCT03412552) | N/A | 完成 | 1238 | 嚴重子癇前症／子癇加護照護的觀察性分析（硫酸鎂為整體處置的一部分） |
| [NCT07220902](https://clinicaltrials.gov/study/NCT07220902) | Phase 3 | 尚未招募 | 1240 | Levetiracetam 與硫酸鎂預防子癇發作的等效性比較 |

這些試驗多聚焦於劑量與療程的最佳化，而非「有沒有效」，顯示硫酸鎂已是標準療法。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstetrics and Gynecology | 回顧硫酸鎂預防子癇發作的療效、效益與風險 |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | Am J Obstet Gynecol | 硫酸鎂為子癇前症／子癇的理想抗痙攣藥，療效與安全性已獲長期記錄 |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstet Gynecol Surv | 子癇前症的腦血流動力學，及硫酸鎂替代藥物的理由 |
| [23282276](https://pubmed.ncbi.nlm.nih.gov/23282276/) | 2012 | Review | Rev Med Inst Mex Seguro Soc | 子癇前症／子癇臨床指引 |
| [2672428](https://pubmed.ncbi.nlm.nih.gov/2672428/) | 1989 | Review | Stroke | 硫酸鎂可能透過對抗鈣依賴性動脈收縮而緩解血管痙攣 |
| [41054655](https://pubmed.ncbi.nlm.nih.gov/41054655/) | 2025 | Review | Cureus | 硫酸鎂在兒童急診的藥理與證據 |
| [17441885](https://pubmed.ncbi.nlm.nih.gov/17441885/) | 2007 | Cohort | J Obstet Gynaecol Res | 嚴重子癇前症／子癇治療下游離鎂與總鎂濃度的關係 |
| [1566765](https://pubmed.ncbi.nlm.nih.gov/1566765/) | 1992 | In vitro | Am J Obstet Gynecol | 硫酸鎂對海馬迴癲癇發作具中樞抗痙攣作用 |
| [39110688](https://pubmed.ncbi.nlm.nih.gov/39110688/) | 2024 | Case series | PLoS One | 坦尚尼亞護理助產人員提供硫酸鎂的質性研究 |
| [28301493](https://pubmed.ncbi.nlm.nih.gov/28301493/) | 2017 | 質性研究 | PLoS One | 巴西產科醫師對處方硫酸鎂的風險認知 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Magnesium Sulfate 的不重複許可證共 **117 張**：有效單方 5 張、有效複方 14 張、已註銷 98 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第004771號 | 硫酸鎂注射液 | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 子癇症、子癇前症、妊娠毒血症、產科全身麻醉輔助；體內鎂離子缺乏時之補充 |
| 衛署藥製字第038935號 | 〝中國化學〞硫酸鎂注射液１００公絲/公撮 | 注射劑 | 中國化學製藥股份有限公司新豐工廠 | 2030/05/30 | 子癇症、子癇前症、妊娠毒血症、產科全身麻醉輔助；體內鎂離子缺乏時之補充 |
| 衛部藥製字第062091號 | 美我欣注射液100毫克/毫升 | 注射劑 | 南光化學製藥股份有限公司 | 2030/12/24 | 子癇症、子癇前症、妊娠毒血症、產科全身麻醉補助；體內鎂離子缺乏時之補充。 |
| 衛部藥輸字第027619號 | 硫酸鎂 | （粉） | 宣泓貿易有限公司 | 2029/03/25 | 抗痙攣藥；瀉藥 |
| 衛部藥輸字第028751號 | 七水硫酸鎂 | 原料藥結晶性粉末 | 品承貿易股份有限公司 | 2029/07/23 | 子癇症、子癇前症、妊娠毒血症、產科全身麻醉輔助；體內鎂離子缺乏時之補充。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（14 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第002607號 | 維他利益糖衣錠 | THIAMINE (VITAMIN B1)、INOSITOL (MESO-INOSITOL)、CYANOCOBALAMI… | 糖衣錠 | 發育不良、營養補給、虛弱體質、熱性消耗性疾患之補助治療、妊娠婦之營養補給。 |
| 內衛藥製字第013004號 | "人生"便通樂灌腸 | MAGNESIUM SULFATE、BENZALKONIUM CHLORIDE、SODIUM CHLORIDE、GLYC… | 外用液劑 | 便秘、習慣性便秘、痔疾便秘等之浣腸 |
| 衛署藥製字第023624號 | 百樂蒙多注射液一號 | CALCIUM GLUCONATE MONOHYDRATE、POTASSIUM ACETATE、MAGNESIUM SU… | 注射劑 | 經口、經腸管營養不能或不充分時之水份電解質和熱量的營養補給 |
| 衛署藥製字第023625號 | 百樂蒙多注射液二號 | SODIUM PHOSPHATE MONOBASIC DIHYDRATE、MAGNESIUM SULFATE、SODIU… | 注射劑 | 經口、經腸管營養不能或不充分時之水份電解質和熱量的營養補給 |
| 衛署藥製字第024006號 | 信東八號Ａ點滴注射液 | DEXTROSE MONOHYDRATE、SODIUM ACETATE TRIHYDRATE (EQ TO SODIUM… | 注射劑 | 本劑適於不能或無法充分經口、經腸管補給營養、而經由中心靜脈、營養療法賴以補給水分、電解質和熱量之患者 |
| 衛署藥製字第024990號 | 信東八號Ｂ點滴注射液 | POTASSIUM ACETATE、SODIUM ACETATE TRIHYDRATE (EQ TO SODIUM AC… | 注射劑 | 水分、電解質及熱量之補充 |
| 衛署藥製字第029455號 | "台灣大塚"補樂益一號注射液 | MAGNESIUM SULFATE HEPTAHYDRATE、SODIUM ACETATE ANHYDROUS、CALC… | 注射劑 | 小兒病患經口不能攝食時或不能完全攝食之中心靜脈輸注液、小兒電解質熱能補充 |
| 衛署藥製字第029457號 | "台灣大塚"補樂益二號注射液 | POTASSIUM ACETATE、POTASSIUM PHOSPHATE MONOBASIC(EQ TO POTASS… | 注射劑 | 手術前後及未能進食病人之水份、電解質、熱能補充及磷質補充 |
| 衛署藥製字第029458號 | "台灣大塚"補樂益三號注射液 | SODIUM CHLORIDE、MAGNESIUM SULFATE HEPTAHYDRATE、CALCIUM GLUCO… | 注射劑 | 手術前後及未能進食之病人之水份、電解質、熱能補充及鈣質補充 |
| 衛署藥輸字第025150號 | 斯莫克必恩周邊靜脈輸注液 | SERINE、SERINE、ARGININE、SODIUM ACETATE (TRIHYDRATE)、ARGININE、… | 注射劑 | 靜脈營養輸注，適用於無法由口腔進食或經腸道獲取足夠營養，或禁止由口腔及腸道進食之成年患者及2歲以上兒童。 |
| 衛署藥輸字第025179號 | 必富力得注射液 | Thiamine chloride hydrochloride、L-TRYPTOPHAN、L-ALANINE、GLYCI… | 注射劑 | 經口攝取不足、輕度的低蛋白血症、輕度的營養障礙、手術前後等狀態時的氨基酸、電解質、維生素B1及水分之營養補給。 |
| 衛署藥輸字第025203號 | 斯莫克必恩中心靜脈輸注液 | GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、GLYCINE (E… | 注射劑 | 靜脈營養輸注，適用於無法由口腔進食或經腸道獲取足夠營養，或禁止由口腔及腸道進食之成年患者及2歲以上兒童。 |
| 衛部藥輸字第026371號 | 樂敦乾眼修護人工淚液 | CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE… | 點眼液劑 | 暫時緩解因眼睛乾澀所引起灼熱感與刺激感、眼睛疲勞。 |
| 衛部藥輸字第028197號 | 斯莫克必恩(升氮)中心靜脈輸注液 | L-PROLINE、SODIUM GLYCEROPHOSPHATE ANHYDROUS、SODIUM ACETATE T… | 注射劑 | 靜脈營養輸注，適用於無法由口腔進食或經腸道獲取足夠營養，或禁止由口腔及腸道進食之成年患者及2歲以上兒童。 |

<details><summary><strong>已註銷</strong>（98 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000035號</td><td>日本藥典第六版硫酸鎂</td><td>MAGNESIUM SULFATE</td><td>1988/12/03</td></tr><tr><td>內衛藥製字第011365號</td><td>維他美樂（２７）糖衣片</td><td>NIACINAMIDE (NICOTINAMIDE)、PYRIDOXINE(VITAMIN B6)、POTASSIUM…</td><td>2008/08/07</td></tr><tr><td>內衛藥製字第013893號</td><td>維他可糖衣錠</td><td>THIAMINE (VITAMIN B1)、FERROUS SULFATE、VITAMIN D、VITAMIN A、CU…</td><td>2002/07/24</td></tr><tr><td>內衛藥輸字第004547號</td><td>加扶樂片</td><td>CALCIUM PHOSPHATE DIBASIC、THIAMINE HYDROCHLORIDE、TAURINE (EQ…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第004548號</td><td>補/身</td><td>LYSINE HCL、AMINOACETIC ACID ALPHA-、L-CYSTEINE、CUPRIC SULFATE…</td><td>1991/02/01</td></tr><tr><td>衛署藥製字第014304號</td><td>止咳注射液</td><td>DL-METHYLEPHEDRINE HCL、POTASSIUM GUAIACOLSULFONATE、CAFFEINE…</td><td>2014/07/18</td></tr><tr><td>衛署藥製字第018142號</td><td>血補納膠囊</td><td>PYRIDOXINE HCL、POTASSIUM SULFATE、MANGANESE SULFATE、RIBOFLAVI…</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第022133號</td><td>胖維他Ｍ糖衣錠</td><td>VITAMIN B6 (HCL)、POTASSIUM SULFATE、RIBOFLAVIN (VIT B2)、MANGA…</td><td>1992/04/17</td></tr><tr><td>衛署藥製字第025608號</td><td>善存膜衣錠</td><td>FOLIC ACID、MAGNESIUM (OXIDE)、RIBOFLAVIN (VIT B2)、CUPRIC (OXI…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第030272號</td><td>百樂蒙多注射液三號</td><td>MAGNESIUM SULFATE 7H2O、POTASSIUM ACETATE、CALCIUM GLUCONATE M…</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第032795號</td><td>硫酸鎂５００公絲/公撮注射液</td><td>MAGNESIUM SULFATE</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第040660號</td><td>"南光" 百利得－Ａ注射液</td><td>POTASSIUM ACETATE、CALCIUM GLUCONATE MONOHYDRATE、MAGNESIUM SU…</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第040661號</td><td>百利得－Ｂ注射液</td><td>GLUCOSE、SODIUM CHLORIDE、SODIUM PHOSPHATE MONOBASIC DIHYDRATE…</td><td>2013/10/03</td></tr><tr><td>衛署藥輸字第004825號</td><td>硫酸鎂</td><td>MAGNESIUM SULFATE</td><td>1985/04/18</td></tr><tr><td>衛署藥輸字第005700號</td><td>身得補錠</td><td>FOLIC ACID、POTASSIUM SULFATE、AMMONIUM MOLYBDATE、MANGANESE SU…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第007660號</td><td>維得能軟膠囊</td><td>POTASSIUM (SULFATE)、CYANOCOBALAMIN (VIT B12)、ASCORBIC ACID (…</td><td>1993/05/03</td></tr><tr><td>衛署藥輸字第007669號</td><td>維我百達膠囊</td><td>TOCOPHEROL ACETATE ALPHA (EQ TO VIT E ACETATE) (EQ TO VITAMI…</td><td>1996/01/11</td></tr><tr><td>衛署藥輸字第007748號</td><td>倍健軟膠囊</td><td>NIACINAMIDE (NICOTINAMIDE)、RUTIN、RIBOFLAVIN (VIT B2)、PYRIDOX…</td><td>2020/04/07</td></tr><tr><td>衛署藥輸字第007911號</td><td>多種維他命加礦物質軟膠囊</td><td>VITAMIN B1 (MONONITRATE)、PHOSPHORUS (DICALCIUM PHOSPHATE)、CY…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第008024號</td><td>維他補健糖衣錠</td><td>PYRIDOXINE HCL、CALCIUM PHOSPHATE DIBASIC、MAGNESIUM (SULFATE)…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第008051號</td><td>德泰復生注射液</td><td>ARGININE HCL L-、PANTHENOL、L-ARGININE、NIACINAMIDE (NICOTINAMI…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008052號</td><td>德泰利多注射液</td><td>ORNITHINE L- ASPARTATE L-、SODIUM CHLORIDE、CYANOCOBALAMIN (VI…</td><td>1988/01/28</td></tr><tr><td>衛署藥輸字第008229號</td><td>惠補軟膠囊</td><td>NIACINAMIDE (NICOTINAMIDE)、FOLIC ACID、RIBOFLAVIN (VIT B2)、TH…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008250號</td><td>樂補力軟膠囊</td><td>MENADIONE SODIUM BISULFITE、RIBOFLAVIN (VIT B2)、FOLIC ACID、MA…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008474號</td><td>堅力富糖衣錠</td><td>NIACINAMIDE (NICOTINAMIDE)、MANGANESE (SULFATE)、PYRIDOXINE HC…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第008680號</td><td>滋恩保糖衣錠</td><td>PANTOTHENATE D- CALCIUM、THIAMINE MONONITRATE、CYANOCOBALAMIN…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第008824號</td><td>利大寶軟膠囊</td><td>IODINE (POTASSIUM)、ERGOCALCIFEROL (VIT D2CALCIFEROL)、POTASSI…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第009026號</td><td>赫寶克軟膠囊</td><td>ZINC (ZINC SULFATE)、MANGANESE (SULFATE)、RIBOFLAVIN (VIT B2)、…</td><td>1994/06/08</td></tr><tr><td>衛署藥輸字第009112號</td><td>智明眼藥水</td><td>SODIUM CHLORIDE、POTASSIUM CHLORIDE、MAGNESIUM SULFATE、CALCIUM…</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第009184號</td><td>赫達寶軟膠囊</td><td>RIBOFLAVIN (VIT B2)、VITAMIN B6 (HCL)、ZINC (ZINC SULFATE)、MAN…</td><td>2000/08/09</td></tr><tr><td>衛署藥輸字第009229號</td><td>維安比膠囊</td><td>VITAMIN A、FERROUS SULFATE、POTASSIUM IODIDE、THIAMINE MONONITR…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009238號</td><td>多種維他命軟膠囊</td><td>IRON PHOSPHATE、POTASSIUM (SULFATE)、INOSITOL (MESO-INOSITOL)、…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第009385號</td><td>維蒙力斯膠囊</td><td>RIBOFLAVIN (VIT B2)、FOLIC ACID、RUTIN、METHIONINE、PANTOTHENATE…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009416號</td><td>健力克軟膠囊</td><td>CALCIUM (FLUORIDE)、RUTIN、NIACINAMIDE (NICOTINAMIDE)、PANTOTHE…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第009445號</td><td>維明頓軟膠囊</td><td>PYRIDOXINE(VITAMIN B6)、ZINC (ZINC SULFATE)、NIACINAMIDE (NICO…</td><td>1995/02/15</td></tr><tr><td>衛署藥輸字第009501號</td><td>"得錄" 高卡路里輸液二號（維持液）</td><td>ZINC SULFATE、GLUCOSE、CALCIUM GLUCONATE、POTASSIUM PHOSPHATE M…</td><td>2015/11/04</td></tr><tr><td>衛署藥輸字第009502號</td><td>高卡路里輸液一號（開始液）</td><td>POTASSIUM ACETATE、MAGNESIUM SULFATE、CALCIUM GLUCONATE、POTASS…</td><td>2015/11/04</td></tr><tr><td>衛署藥輸字第009582號</td><td>莫維保軟膠囊</td><td>VITAMIN A (PALMITATE)、IRON (FERROUS FUMARATE)、LECITHIN(LECIT…</td><td>1994/03/07</td></tr><tr><td>衛署藥輸字第009603號</td><td>原命樂軟膠囊</td><td>MAGNESIUM (SULFATE)、ASCORBIC ACID (VIT C)、VITAMIN A (PALMITA…</td><td>1994/03/07</td></tr><tr><td>衛署藥輸字第009677號</td><td>愛必託補軟膠囊</td><td>METHIONINE DL-、MANGANESE SULFATE、TOCOPHEROL (ACETATE ALPHA D…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009829號</td><td>必樂能軟膠囊</td><td>VITAMIN A (PALMITATE)、LECITHIN SOYA、MAGNESIUM (SULFATE)、PHOS…</td><td>2003/12/03</td></tr><tr><td>衛署藥輸字第009889號</td><td>愛必託補軟膠囊</td><td>PYRIDOXINE HCL、GINSENG POWDER、POTASSIUM SULFATE、CALCIUM PHOS…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009927號</td><td>複多命軟膠囊</td><td>PANTOTHENATE (D- CALCIUM)、PHOSPHORUS (DICALCIUM PHOSPHATE)、T…</td><td>1992/09/25</td></tr><tr><td>衛署藥輸字第010411號</td><td>台德多種維生素軟膠囊</td><td>FERROUS FUMARATE、NIACINAMIDE (NICOTINAMIDE)、PANTOTHENATE CAL…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010419號</td><td>力倍挺軟膠囊</td><td>TOCOPHEROL (ACETATE ALPHA DL- )、MANGANESE (SULFATE)、RIBOFLAV…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010514號</td><td>頂維他軟膠囊</td><td>PYRIDOXINE(VITAMIN B6)、RUTIN、NIACINAMIDE (NICOTINAMIDE)、RIBO…</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第010515號</td><td>保麗能軟膠囊</td><td>VITAMIN B1 (MONONITRATE)、CYANOCOBALAMIN (VIT B12)、POTASSIUM…</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第010531號</td><td>維他瑞軟膠囊</td><td>ZINC (ZINC SULFATE)、PYRIDOXINE(VITAMIN B6)、MANGANESE (SULFAT…</td><td>1994/01/21</td></tr><tr><td>衛署藥輸字第010661號</td><td>百惠麗軟膠囊</td><td>CUPRIC SULFATE、NIACINAMIDE (NICOTINAMIDE)、THIAMINE MONONITRA…</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第010747號</td><td>舒喜軟膠囊</td><td>PYRIDOXINE(VITAMIN B6)、MANGANESE (SULFATE)、ZINC (ZINC SULFAT…</td><td>2003/08/25</td></tr><tr><td>衛署藥輸字第010857號</td><td>得維他軟膠囊</td><td>NIACINAMIDE (NICOTINAMIDE)、VITAMIN B6 (HCL)、RIBOFLAVIN (VIT…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第010861號</td><td>得樂蒙軟膠囊</td><td>VITAMIN A (PALMITATE)、ASCORBIC ACID (VIT C)、LECITHIN(LECITHO…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第011189號</td><td>維普健軟膠囊</td><td>PANTOTHENATE (D- CALCIUM)、LECITHIN(LECITHOL)、IODINE (KELP)、C…</td><td>1997/12/01</td></tr><tr><td>衛署藥輸字第011305號</td><td>康得隆軟膠囊</td><td>NIACINAMIDE (NICOTINAMIDE)、MANGANESE (SULFATE)、ZINC (ZINC SU…</td><td>2001/07/26</td></tr><tr><td>衛署藥輸字第011331號</td><td>優得康軟膠囊</td><td>PHOSPHORUS (DICALCIUM PHOSPHATE)、VITAMIN A PALMITATE、CALCIUM…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第011373號</td><td>加利補軟膠囊</td><td>RIBOFLAVIN (VIT B2)、IRON (FERROUS FUMARATE)、VITAMIN B6 (HCL)…</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第011379號</td><td>必健爾軟膠囊</td><td>RIBOFLAVIN (VIT B2)、NIACINAMIDE (NICOTINAMIDE)、ZINC (ZINC SU…</td><td>2003/08/25</td></tr><tr><td>衛署藥輸字第011538號</td><td>維泰軟膠囊</td><td>TOCOPHEROL (ACETATE ALPHA DL- )、RIBOFLAVIN (VIT B2)、MANGANES…</td><td>1987/10/30</td></tr><tr><td>衛署藥輸字第011562號</td><td>維康能糖衣錠〝華貿比〞</td><td>VITAMIN D2 (DRY BEADLET)、RIBOFLAVIN (VIT B2)、TOCOPHEROL (ACE…</td><td>2002/01/14</td></tr><tr><td>衛署藥輸字第011569號</td><td>倍力能軟膠囊</td><td>RIBOFLAVIN (VIT B2)、NIACINAMIDE (NICOTINAMIDE)、TOCOPHEROL (A…</td><td>2003/08/25</td></tr><tr><td>衛署藥輸字第011584號</td><td>利維康軟膠囊</td><td>VITAMIN B6 (HCL)、TOCOPHEROL (ACETATE ALPHA DL- )、NIACINAMIDE…</td><td>2003/10/23</td></tr><tr><td>衛署藥輸字第011632號</td><td>維易納膠囊</td><td>CYANOCOBALAMIN (VIT B12)、PHOSPHORUS (DICALCIUM PHOSPHATE)、FE…</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第011695號</td><td>威沛軟膠囊</td><td>IRON (FERROUS FUMARATE)、CYANOCOBALAMIN (VIT B12)、VITAMIN B1…</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第011948號</td><td>欣捷軟膠囊</td><td>ZINC (ZINC SULFATE)、PYRIDOXINE(VITAMIN B6)、MANGANESE (SULFAT…</td><td>2003/08/25</td></tr><tr><td>衛署藥輸字第011973號</td><td>愛樂力膠囊</td><td>ASCORBIC ACID (VIT C)、CYANOCOBALAMIN (VIT B12)、PANTOTHENIC A…</td><td>2002/01/14</td></tr><tr><td>衛署藥輸字第012026號</td><td>百威軟膠囊</td><td>ZINC OXIDE、VIT D (CALCIFEROL IN OIL)、ASCORBIC ACID (VIT C)、B…</td><td>2004/03/05</td></tr><tr><td>衛署藥輸字第012229號</td><td>優得康軟膠囊</td><td>FERROUS (SULFATE)、POTASSIUM (SULFATE)、PHOSPHORUS (DICALCIUM…</td><td>2001/07/26</td></tr><tr><td>衛署藥輸字第012291號</td><td>倍樂力軟膠囊</td><td>VITAMIN D (ERGOCALCIFEROL)、MAGNESIUM (SULFATE)、VITAMIN A (PA…</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012323號</td><td>雷寶維他軟膠囊</td><td>PHOSPHORUS (DICALCIUM PHOSPHATE)、POTASSIUM (SULFATE)、ERGOCAL…</td><td>1988/03/16</td></tr><tr><td>衛署藥輸字第012370號</td><td>硫酸鎂</td><td>MAGNESIUM SULFATE</td><td>1994/06/27</td></tr><tr><td>衛署藥輸字第012693號</td><td>艾必亞百賜隆軟膠囊</td><td>ERGOCALCIFEROL (VIT D2CALCIFEROL)、COBALTOUS SULFATE、POTASSIU…</td><td>1991/04/25</td></tr><tr><td>衛署藥輸字第013415號</td><td>"富田" 硫酸鎂粉劑</td><td>MAGNESIUM SULFATE</td><td>2020/04/07</td></tr><tr><td>衛署藥輸字第013529號</td><td>威沛軟膠囊</td><td>WAX MIXTURE HYDROGENATED COCONUT OIL、THIAMINE (VITAMIN B1)、C…</td><td>1990/05/22</td></tr><tr><td>衛署藥輸字第013554號</td><td>舒維滿得糖衣錠</td><td>POTASSIUM IODIDE、VITAMIN B12 (0.1% MANNITE)、FERROUS SULFATE、…</td><td>1995/09/21</td></tr><tr><td>衛署藥輸字第014515號</td><td>維礦樂軟膠囊</td><td>CYANOCOBALAMIN (VIT B12)、COBALTOUS SULFATE、POTASSIUM IODIDE、…</td><td>1992/01/14</td></tr><tr><td>衛署藥輸字第016058號</td><td>華泰軟膠囊</td><td>CHOLINE BITARTRATE、MAGNESIUM (SULFATE)、VITAMIN A (PALMITATE)…</td><td>2003/08/25</td></tr><tr><td>衛署藥輸字第016329號</td><td>健寶維他軟膠囊</td><td>ERGOCALCIFEROL (VIT D2CALCIFEROL)、FERROUS SULFATE、CYANOCOBAL…</td><td>2001/07/26</td></tr><tr><td>衛署藥輸字第016393號</td><td>加利補軟膠囊</td><td>VITAMIN B6 (HCL)、NIACINAMIDE (NICOTINAMIDE)、RIBOFLAVIN (VIT…</td><td>1988/09/29</td></tr><tr><td>衛署藥輸字第016723號</td><td>維達補健軟膠囊</td><td>POTASSIUM SULFATE、MAGNESIUM SULFATE、RIBOFLAVIN (VIT B2)、MANG…</td><td>1999/07/05</td></tr><tr><td>衛署藥輸字第016848號</td><td>包清干軟膠囊</td><td>NIACINAMIDE (NICOTINAMIDE)、VITAMIN A (PALMITATE)、CALCIUM (CA…</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第017727號</td><td>德泰復生注射液</td><td>CYANOCOBALAMIN (VIT B12)、ORNITHINE L- ASPARTATE L-、GLUTAMIC…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017771號</td><td>威沛軟膠囊</td><td>IRON (FERROUS FUMARATE)、TOCOPHEROL ACETATE ALPHA DL-、SOYBEAN…</td><td>1991/08/14</td></tr><tr><td>衛署藥輸字第018708號</td><td>威沛軟膠囊</td><td>IRON (FERROUS FUMARATE)、MAGNESIUM (SULFATE)、VITAMIN B12 (CYA…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第018932號</td><td>婦更寶軟膠囊</td><td>MAGNESIUM SULFATE、VITAMIN A PALMITATE、CHOLINE BITARTRATE、ERG…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第020190號</td><td>維他瑞軟膠囊</td><td>TOCOPHEROL ACETATE ALPHA D-、PANTOTHENATE D- CALCIUM、VITAMIN…</td><td>2001/07/26</td></tr><tr><td>衛署藥輸字第021008號</td><td>營養維他糖衣錠</td><td>BETAINE HCL、ASCORBIC ACID (VIT C)、ZINC SULFATE、POTASSIUM IOD…</td><td>2015/02/24</td></tr><tr><td>衛署藥輸字第021946號</td><td>維普健軟膠囊</td><td>PANTOTHENATE (D- CALCIUM)、PHOSPHORUS (DICALCIUM PHOSPHATE)、V…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第022651號</td><td>倍麗多眼藥水</td><td>MAGNESIUM SULFATE、CALCIUM CHLORIDE、POTASSIUM PHOSPHATE MONOB…</td><td>2004/06/29</td></tr><tr><td>衛署藥輸字第023170號</td><td>百源雙利－３號</td><td>L-METHIONINE、POTASSIUM ACETATE、GLYCINE (EQ TO AMINOACETIC AC…</td><td>2004/07/07</td></tr><tr><td>衛署藥輸字第023171號</td><td>百源雙利－１號</td><td>ZINC SULFATE、L-THREONINE、GLUCOSE、L-PROLINE、L-VALINE、L-HISTID…</td><td>2004/07/07</td></tr><tr><td>衛署藥輸字第023172號</td><td>百源雙利－２號</td><td>L-ASPARTIC ACID、L-TRYPTOPHAN、L-ALANINE、L-ARGININE、L-TYROSINE…</td><td>2004/07/07</td></tr><tr><td>衛署藥輸字第023878號</td><td>氨基富液</td><td>L- GLUTAMIC ACID、L-PHENYLALANINE、L-ALANINE、L-LEUCINE、LYSINE…</td><td>2021/03/26</td></tr><tr><td>衛署藥輸字第024329號</td><td>速立恩中心靜脈輸注液</td><td>ZINC SULFATE 7H2O、CALCIUM CHLORIDE DIHYDRATE、LEUCINE、TYROSIN…</td><td>2022/07/07</td></tr><tr><td>衛署藥輸字第024338號</td><td>速立恩周邊靜脈輸注液</td><td>L-PHENYLALANINE、L-ALANINE、L-TYROSINE、LYSINE ACETATE、L-ARGINI…</td><td>2022/07/07</td></tr><tr><td>衛署藥輸字第024838號</td><td>益達健樂維他糖衣錠</td><td>INOSITOL (MESO-INOSITOL)、IODINE (POTASSIUM)、BETAINE HCL、MAGN…</td><td>2014/08/11</td></tr><tr><td>衛署藥輸字第025669號</td><td>立可舒人工淚液</td><td>Calcium chloride hydrate、SODIUM CHLORIDE、POTASSIUM CHLORIDE、…</td><td>2023/06/12</td></tr><tr><td>衛署藥輸字第025708號</td><td>新派瑞恩12%糖注射液</td><td>L-LYSINE ACETATE、Zinc sulfate hydrate、L-VALINE、L-HISTIDINE、L…</td><td>2021/03/30</td></tr><tr><td>衛署藥輸字第025902號</td><td>新派瑞恩17.5%糖注射液</td><td>L-LYSINE ACETATE、L-LEUCINE、RIBOFLAVIN PHOSPHATE SODIUM、GLUCO…</td><td>2021/03/24</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **禁忌症（來自知識圖譜推論，非仿單原文）**：腎臟疾病、高血鈣、腎鈣質沉著症、磷代謝疾病、慢性腹瀉、闌尾炎、房室傳導阻滯、高血鉀型週期性麻痺、低醛固酮症、先天性肌強直、胃輕癱等。
- **藥物交互作用**：共查得 92 筆，主要如下。
  - 重度：Dolutegravir、Amikacin、Bictegravir
  - 中度：Doxycycline、Tetracycline、Ciprofloxacin、Nifedipine、Amlodipine、Cisatracurium、Alendronic acid、Risedronic acid、Ibandronate、Cholecalciferol、Calcitriol 及多種皮質類固醇
- 臨床試驗中也有硫酸鎂延長神經肌肉阻斷劑作用的研究，麻醉時需留意。

其餘警語請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 硫酸鎂用於子癇前症／子癇已有大量隨機試驗與長期臨床經驗，台灣許可證也已涵蓋此適應症。
- 劑量、療程、肥胖族群與腎功能不全者的安全邊界仍在研究中，需要明確的用藥防護措施。

**若要推進需要：**
- 補齊作用機轉（MOA）資料。
- 建立血鎂濃度監測，以及腎功能、反射、呼吸頻率與尿量的監測流程。
- 確認與麻醉與神經肌肉阻斷劑、鈣離子阻斷劑等併用時的處置指引。
- 針對肥胖族群及產後療程長短，參考進行中的試驗結果。
- 其他預測適應症（如偏頭痛／頭痛、術後喉嚨痛）屬研究性問題，應另案評估，不宜與本結論混為一談。

<!-- review:begin magnesium-sulfate-cerebral-perfusion-moa-next-2026-10-16 -->

> **查核加註（2026-10-16）**：本頁已附有依仿單整理的作用機轉段（2026-10-03 查核新增）。原文保留。依據：[DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d)。

<!-- review:end magnesium-sulfate-cerebral-perfusion-moa-next-2026-10-16 -->

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d) |
| 2026-10-03 | 許可證表「衛署藥製字第013386號 濟生硫酸鎂注射液」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「衛署藥製字第047652號 欣滿福注射液」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 核准適應症「靜脈營養輸注」「維他命與礦物質缺乏症」 | 報告重生後已無此錯誤（2026-10-16：重生時 LLM 列的核准適應症清單（含「靜脈營養輸注」「維他命與礦物質缺乏症」）已整段刪除，現由程式化許可證表呈現；不是被許可證表取代；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 機轉寫 NMDA 受體拮抗、阻斷鈣離子通道與促進腦血管擴張 | 加註（2026-10-16 修訂，前版保留於紀錄） | [DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L1） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |
| 2026-10-16 | 稱缺乏作用機轉資料 | 加註 | [DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d) |
| 2026-10-16 | 下一步建議補齊作用機轉 | 加註 | [DailyMed：Magnesium Sulfate in Water for Injection 仿單（Hospira），Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=22ca78b4-f5a3-4144-cf89-5f633acf1e6d) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

