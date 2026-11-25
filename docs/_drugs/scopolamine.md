---
layout: default
title: Scopolamine
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 6
monitor_inn: "Scopolamine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
last_modified_at: 2026-11-20
description: "Scopolamine：預測新適應症為脊髓馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣"
---

# Scopolamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Scopolamine：從胃腸痙攣到脊髓馬尾症候群
{: .text-alpha }

## 一句話總結

Scopolamine（東莨菪鹼）是一種抗膽鹼藥物，原本用於胃腸、膽管及尿路的痙攣性疼痛。
TxGNN 模型預測它可能對**脊髓馬尾症候群 (Cauda Equina Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣 |
| 預測新適應症 | 脊髓馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 20 張／共 82 張） |
| 許可證數 | 82 張（有效單方 1／有效複方 19／已過期 2／已註銷 60） |
| 建議決策 | Hold |

<!-- review:begin scopolamine-butylscopolamine-licenses-2026-10-03 -->

> **查核更正（2026-11-25）**：原寫「原適應症／胃潰瘍、十二指腸潰瘍、胃炎、十二指腸炎、賁門痙攣、食道痙攣、膽囊炎、膽管炎、膽結石、尿路結石、膀胱痙攣、排尿困難及頻尿、分娩時子宮下部弛緩之遲延、切迫流產、痙攣性月經困難等痙攣性疼痛及炎症性疼痛」。原文取自內衛藥製字第000509號「保賜康膠囊」，主成分是丁基東莨菪鹼（butylscopolamine，scopolamine 的四級銨衍生物），是另一個藥；改為 scopolamine 本身現行有效單方許可證衛署藥製字第007944號「福元」得達息糖衣錠（SCOPOLAMINE HBR）的核准適應症。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)；[NLM MeSH：Butylscopolammonium Bromide（D002086）](https://meshb.nlm.nih.gov/record/ui?ui=D002086)；[NLM MeSH：Scopolamine（D012601）](https://meshb.nlm.nih.gov/record/ui?ui=D012601)。

<!-- review:end scopolamine-butylscopolamine-licenses-2026-10-03 -->

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Scopolamine 仿單（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Scopolamine 為一種顛茄生物鹼，屬抗膽鹼藥物。Scopolamine 的作用：i) 作為副交感神經系統節後蕈毒鹼受體部位的競爭性抑制劑，以及 ii) 作用於對乙醯膽鹼有反應但缺乏膽鹼性神經支配的平滑肌。」英文原文："Scopolamine, a belladonna alkaloid, is an anticholinergic. Scopolamine acts: i) as a competitive inhibitor at postganglionic muscarinic receptor sites of the parasympathetic nervous system, and ii) on smooth muscles that respond to acetylcholine but lack cholinergic innervation."（[DailyMed: Transderm Scop (scopolamine) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b877a694-a1d0-4280-937a-a06820b12a88)，版本日期 2025-06-10；查閱日期 2026-11-19）。根據已知資訊，Scopolamine 屬於蕈毒鹼受體拮抗劑（抗膽鹼藥物），
在痙攣性疼痛，包括尿路痙攣的療效已被臨床使用證實。

理論上，抗膽鹼作用可降低膀胱逼尿肌的活性，可能緩解馬尾症候群相關神經性膀胱功能障礙所導致的膀胱過動。
這是 TxGNN 預測與原適應症（尿路痙攣）之間較合理的連結。

但這個連結相當有限。馬尾症候群是因神經根受壓所致的外科急症，核心處置是儘早手術減壓；
抗膽鹼藥物無法處理根本的神經壓迫，最多只能針對部分症狀。目前沒有任何臨床或文獻證據支持此用途。

### 其他預測適應症

資料中另有 5 項預測，同樣只有模型分數，沒有試驗或文獻：

| 排名 | 預測疾病 | TxGNN 分數 | 評估 |
|------|---------|-----------|------|
| 2 | 神經性膀胱（已淘汰的疾病名稱） | 0.9998 | 抗膽鹼阻斷逼尿肌 M3 受體是神經性逼尿肌過動的既定機轉，與原適應症「尿路痙攣」相符，機轉上最合理；但疾病名稱已過時，需先對應到現行術語 |
| 3 | 乳突狀結膜炎 | 0.9998 | 非已知作用路徑，僅為推測 |
| 4 | 異位性結膜炎 | 0.9980 | 屬 IgE 介導的過敏發炎，缺乏機轉支持，並有乾眼與瞳孔放大風險 |
| 5 | 酒糟性結膜炎 | 0.9940 | 可能加重淚膜不穩與乾眼，方向可能不利 |
| 6 | 春季結膜炎 | 0.9908 | 屬 Th2 及肥大細胞介導，抗膽鹼不針對其病因，且有耐受性疑慮 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-11-24），主成分含 Scopolamine 的不重複許可證共 **82 張**：有效單方 1 張、有效複方 19 張、已過期 2 張（未註銷但有效日期早於資料集日期）、已註銷 60 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-11-24）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第007944號 | "福元" 得達息糖衣錠１０毫克 | 糖衣錠 | 福元化學製藥股份有限公司 | 2029/05/25 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣 |

**有效・複方（截至資料集日期 2026-11-24；適應症屬整個複方，不是本藥單獨的適應症）**（19 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第000370號 | "永信" 使莫痛錠 | HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S… | 錠劑 | 胃酸過多、胃痛、賁門痙攣、幽門痙攣、胃、十二指腸潰瘍、胃炎、腸炎、腎石絞痛、月經痛、膽石絞痛、支氣管性氣喘等 |
| 內衛藥製字第000978號 | 舒百林錠 | PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S… | 錠劑 | 胃腸痙攣、胃潰瘍、十二指腸潰瘍、膽管膽囊痙攣、膽結石痛、腎結石痛、月經痛、胃痛、胃酸過多 |
| 內衛藥製字第005458號 | Ａ．Ｄ．Ａ．胃片 | DIHYDROXYALUMINUM AMINOACETATE、PHENOBARBITAL、SCOPOLAMINE HBR | 錠劑 | 胃、十二指腸潰瘍、胃疼痛、胃痙攣、胃酸過多、腸胃充氣 |
| 內衛藥製字第013417號 | 速立舒錠 | ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMI… | 錠劑 | 胃痛、賁門或幽門痙攣、胃、十二指腸潰瘍、腎、膽結石、絞痛、尿道結石痛、支氣管性氣喘 |
| 衛署藥製字第002328號 | "中國化學製藥" 防暈片 | CHLORPHENIRAMINE MALEATE、SCOPOLAMINE HBR、CAFFEINE ANHYDROUS、… | 錠劑 | 坐車、船或飛機所引起之頭暈、噁心和嘔吐 |
| 衛署藥製字第013931號 | 痛立寧錠 | ERGOTAMINE TARTRATE、CAFFEINE、PHENOBARBITAL、SCOPOLAMINE HBR | 錠劑 | 偏頭痛 |
| 衛署藥製字第017124號 | "明大"胃雅錠 | HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S… | 錠劑 | 消化性潰瘍、過敏性腸疾患（過敏性結腸、痙攣性結腸、粘液性結腸炎）急性腸結腸炎 |
| 衛署藥製字第019115號 | "派頓"派暈吐錠 | DIMENHYDRINATE、DIPROPHYLLINE、SCOPOLAMINE HBR、PYRIDOXINE HCL | 錠劑 | 暈動病（噁心、暈眩、頭痛）噁心、嘔吐之預防及治療 |
| 衛署藥製字第019929號 | "中菱"鎮暈錠 | SCOPOLAMINE HBR、DIMENHYDRINATE、CAFFEINE ANHYDROUS | 錠劑 | 預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀。 |
| 衛署藥製字第021231號 | "長安"立百舒糖衣錠 | PHENOBARBITAL、ERGOTAMINE TARTRATE、SCOPOLAMINE HBR、CAFFEINE A… | 糖衣錠 | 偏頭痛 |
| 衛署藥製字第022023號 | 服舒寧錠 | SCOPOLAMINE HBR、PHENOBARBITAL、HYOSCYAMINE SULFATE、ATROPINE S… | 錠劑 | 胃腸痙攣、胃腸炎、胃、十二指腸潰瘍、胃酸過多、膽囊炎、膽結石、膀胱炎、月經痛、遺尿症、頻尿 |
| 衛署藥製字第022219號 | 克暈明錠 | DIPROPHYLLINE、SCOPOLAMINE HBR、DIMENHYDRINATE、PYRIDOXINE HCL | 錠劑 | 暈動病（噁心、暈眩、頭痛）噁心、嘔吐之預防及治療 |
| 衛署藥製字第025571號 | 舒痛錠 | ATROPINE SULFATE、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、PHENOBA… | 錠劑 | 胃腸痙攣、胃腸炎、胃、十二指腸潰瘍 |
| 衛署藥製字第035398號 | 多樂滅暈錠 | CAFFEINE ANHYDROUS、MECLIZINE HCL ( EQ TO MECLIZINE HYDROCHLO… | 錠劑 | 暈動引起之目眩、噁心、嘔吐、頭痛之預防及緩和。 |
| 衛署藥製字第038592號 | "黃氏"富旅安錠 | CAFFEINE、DIMENHYDRINATE、SCOPOLAMINE HBR | 錠劑 | 預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀。 |
| 衛署藥製字第040049號 | 雅寧錠 | CAFFEINE ANHYDROUS、SCOPOLAMINE HBR、DIMENHYDRINATE | 錠劑 | 預防或緩解暈車、暈船、暈機所引起之頭暈、嘔吐、頭痛、噁心． |
| 衛署藥製字第040067號 | 舒胃膠囊 | PAPAVERINE HCL、SCOPOLAMINE HBR、BENZOCAINE (ETHYL AMINOBENZOA… | 膠囊劑 | 腹痛、腸絞痛（疝痛）、胃痛、胃酸過多 |
| 衛署藥製字第046047號 | 施克錠 | CAFFEINE、SCOPOLAMINE HBR、PROMETHAZINE HCL | 錠劑 | 暈動病(噁心、眩暈)之預防與治療。 |
| 衛署藥製字第050067號 | 抗暈 錠 | SCOPOLAMINE HBR、DIPROPHYLLINE、DIMENHYDRINATE、PYRIDOXINE HCL | 錠劑 | 暈動病(惡心、暈眩、頭痛)、噁心、嘔吐之預防及治療。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-11-24）</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第005612號</td><td>百痛賜安糖衣錠</td><td>SCOPOLAMINE HBR</td><td>2024/05/25</td></tr><tr><td>衛署藥製字第044712號</td><td>暈得寧防暈貼片劑1.5毫克(東茛菪儉)</td><td>SCOPOLAMINE</td><td>2026/11/20</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（60 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000161號</td><td>益舒錠</td><td>ETHAVERINE HCL (eq to BALBONIN) (eq to Ethylpapaverine HCl)、…</td><td>1989/11/24</td></tr><tr><td>內衛藥製字第000463號</td><td>速舒鎮膠囊</td><td>ATROPINE SULFATE、SCOPOLAMINE HBR、HYOSCYAMINE SULFATE、PHENOBA…</td><td>1999/08/23</td></tr><tr><td>內衛藥製字第000794號</td><td>痙泰片</td><td>SCOPOLAMINE HBR、PHENOBARBITAL、HYOSCYAMINE SULFATE、ATROPINE S…</td><td>1997/02/26</td></tr><tr><td>內衛藥製字第001293號</td><td>百泰適片</td><td>HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、PHENOBARBITAL、DIASTASE A…</td><td>1998/07/06</td></tr><tr><td>內衛藥製字第002337號</td><td>多託寧錠</td><td>ATROPINE SULFATE、HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMI…</td><td>1989/06/20</td></tr><tr><td>內衛藥製字第002601號</td><td>"好漢賓" 速克痙錠</td><td>ATROPINE、HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR</td><td>2014/05/15</td></tr><tr><td>內衛藥製字第003675號</td><td>"強生" 抑痛錠</td><td>ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMI…</td><td>2023/10/26</td></tr><tr><td>內衛藥製字第005352號</td><td>胃津－Ｂ膠囊</td><td>ETHAVERINE HCL (eq to BALBONIN) (eq to Ethylpapaverine HCl)、…</td><td>2023/07/07</td></tr><tr><td>內衛藥製字第006963號</td><td>維胃膠囊</td><td>ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMI…</td><td>1999/12/30</td></tr><tr><td>內衛藥製字第008973號</td><td>速拔痛片</td><td>SCOPOLAMINE HBR、PHENOBARBITAL、HYOSCYAMINE SULFATE、ATROPINE S…</td><td>2010/11/18</td></tr><tr><td>內衛藥製字第009771號</td><td>阿托拍注射液</td><td>ETHAVERINE HCL (eq to BALBONIN) (eq to Ethylpapaverine HCl)、…</td><td>2025/04/29</td></tr><tr><td>內衛藥製字第012089號</td><td>"人生"必舒痛錠</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>2026/08/17</td></tr><tr><td>內衛藥製字第012958號</td><td>氫溴酸東莨菪鹼注射液</td><td>SCOPOLAMINE HBR</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第015667號</td><td>司力多寧片</td><td>HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、PHENOBARBITAL、ATROPINE S…</td><td>1991/07/24</td></tr><tr><td>內衛藥輸字第000981號</td><td>氫溴酸東莨/</td><td>SCOPOLAMINE HBR</td><td>1986/03/15</td></tr><tr><td>內衛藥輸字第002785號</td><td>治暈克</td><td>SCOPOLAMINE HBR</td><td>1987/05/14</td></tr><tr><td>內衛藥輸字第004339號</td><td>愛達爾</td><td>SCOPOLAMINE HBR、MECLIZINE HCL ( EQ TO MECLIZINE HYDROCHLORID…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第004597號</td><td>長效速麻林</td><td>ATROPINE SULFATE、HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMI…</td><td>1987/05/14</td></tr><tr><td>內衛藥輸字第005759號</td><td>施克片</td><td>CAFFEINE、PROMETHAZINE HCL、SCOPOLAMINE</td><td>1986/01/18</td></tr><tr><td>內衛藥輸字第005917號</td><td>百宿納</td><td>DIHYDROERGOCORNINE METHANESULPHONATE、PHENOBARBITAL SODIUM、IS…</td><td>1991/02/01</td></tr><tr><td>內衛藥輸字第006024號</td><td>酵母源</td><td>AMYLOLYTIC ENZYME、DEHYDROCHOLIC ACID、PROTASE (PROTEOLYTIC EN…</td><td>1999/09/22</td></tr><tr><td>衛署藥製字第000230號</td><td>蒙汝康恩須古布羅命注射液</td><td>SCOPOLAMINE HBR、EPINEPHRINE HCL、PYRABITAL (AMINOPYRINE+BARBI…</td><td>1991/05/06</td></tr><tr><td>衛署藥製字第002144號</td><td>必舒痛糖衣錠</td><td>SCOPOLAMINE</td><td>1991/09/03</td></tr><tr><td>衛署藥製字第002955號</td><td>"永新" 克胃痛膠囊</td><td>SCOPOLAMINE HBR、PHENOBARBITAL、HYOSCYAMINE SULFATE、ATROPINE S…</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第005855號</td><td>鹽酸全阿片素東莨菪/注射液</td><td>PANTOPON HCL、SCOPOLAMINE HBR</td><td>2014/01/22</td></tr><tr><td>衛署藥製字第010538號</td><td>保舒康寧注射液</td><td>SCOPOLAMINE HBR、PAPAVERINE HCL</td><td>1989/06/20</td></tr><tr><td>衛署藥製字第011456號</td><td>"德星" 佛賜佳因注射液</td><td>ATROPINE SULFATE、PROCAINE HCL、BARBITAL SODIUM、SCOPOLAMINE HB…</td><td>1997/12/22</td></tr><tr><td>衛署藥製字第015466號</td><td>阿羅使爾必拉注射液</td><td>PYRABITAL (AMINOPYRINE+BARBITAL)、SCOPOLAMINE HBR、ATROPINE SU…</td><td>1999/08/05</td></tr><tr><td>衛署藥製字第016204號</td><td>"井田" 維他安痙錠</td><td>PANTOTHENATE CALCIUM、ATROPINE SULFATE、NIACINAMIDE (NICOTINAM…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第018187號</td><td>舒鎮痙錠</td><td>ATROPINE SULFATE、SCOPOLAMINE HBR、PHENOBARBITAL、HYOSCYAMINE S…</td><td>1987/06/02</td></tr><tr><td>衛署藥製字第020322號</td><td>複方甘氨酸鋁錠</td><td>SCOPOLAMINE HBR、PHENOBARBITAL、GLYCINE (EQ TO AMINOACETIC ACI…</td><td>1998/06/01</td></tr><tr><td>衛署藥製字第020632號</td><td>胃比好錠</td><td>SCOPOLAMINE HCL、PHENOBARBITAL</td><td>2016/09/20</td></tr><tr><td>衛署藥製字第020869號</td><td>奇克錠</td><td>CAFFEINE、DIMENHYDRINATE、SCOPOLAMINE HBR</td><td>2016/09/20</td></tr><tr><td>衛署藥製字第024599號</td><td>安治錠</td><td>SCOPOLAMINE HBR、PHENOBARBITAL、HYOSCYAMINE SULFATE、ATROPINE S…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第024679號</td><td>"壽元"安得樂錠</td><td>DICYCLOMINE HCL、SCOPOLAMINE HBR、PHENOBARBITAL、ETHAVERINE HCL…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第025350號</td><td>頭暈痛錠</td><td>SCOPOLAMINE HBR、DIMENHYDRINATE、CAFFEINE ANHYDROUS</td><td>1999/12/10</td></tr><tr><td>衛署藥製字第033759號</td><td>蒙汝康恩須古布羅命注射液</td><td>SCOPOLAMINE HBR、EPINEPHRINE HCL、PROCAINE HCL、DIMETHYLAMINOET…</td><td>1992/01/13</td></tr><tr><td>衛署藥製字第033869號</td><td>司力多寧錠</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>2026/08/03</td></tr><tr><td>衛署藥製字第040432號</td><td>痙泰錠</td><td>PHENOBARBITAL、HYOSCYAMINE (SULFATE)、SCOPOLAMINE HBR、ATROPINE…</td><td>1998/10/08</td></tr><tr><td>衛署藥輸字第002124號</td><td>氫溴酸東莨菪/</td><td>SCOPOLAMINE HBR</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005725號</td><td>腸賴泰錠劑</td><td>HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005746號</td><td>腸賴泰膠囊劑</td><td>ATROPINE SULFATE、SCOPOLAMINE HBR、PHENOBARBITAL、HYOSCYAMINE S…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005809號</td><td>腸賴泰酏劑</td><td>HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、PHENOBARBITAL、ATROPINE S…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005826號</td><td>保妥錠</td><td>SCOPOLAMINE HBR、DIPROPHYLLINE、PYRIDOXINE HCL、DIMENHYDRINATE</td><td>1999/03/11</td></tr><tr><td>衛署藥輸字第006962號</td><td>氫溴酸東莨菪鹼</td><td>SCOPOLAMINE HBR</td><td>2006/09/25</td></tr><tr><td>衛署藥輸字第010048號</td><td>感適平膠囊</td><td>ATROPINE SULFATE、BELLADONNA ALKALOID、PHENYLPROPANOLAMINE HCL…</td><td>1989/07/19</td></tr><tr><td>衛署藥輸字第010644號</td><td>安神錠</td><td>BELLADONNA LEAF ALKALOID TOTAL、ERGOTAMINE TARTRATE、PHENOBARB…</td><td>1986/05/12</td></tr><tr><td>衛署藥輸字第011017號</td><td>安治達持續性膠囊</td><td>CHLORPHENIRAMINE MALEATE、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR…</td><td>1986/03/28</td></tr><tr><td>衛署藥輸字第011025號</td><td>優治胃錠</td><td>SCOPOLAMINE HBR、HYOSCYAMINE SULFATE、ATROPINE SULFATE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第011087號</td><td>腸納格懸液</td><td>ATROPINE SULFATE、PECTIN、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、…</td><td>1993/12/20</td></tr><tr><td>衛署藥輸字第012884號</td><td>克暈貼片</td><td>SCOPOLAMINE</td><td>1993/05/19</td></tr><tr><td>衛署藥輸字第014683號</td><td>施克錠</td><td>SCOPOLAMINE HBR、CAFFEINE、PROMETHAZINE HCL</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第014952號</td><td>賜妥錠</td><td>PHENOBARBITAL、ERGOTAMINE TARTRATE、HYOSCYAMINE SULFATE、BELLAD…</td><td>1994/04/25</td></tr><tr><td>衛署藥輸字第017231號</td><td>感適平膠囊</td><td>HYOSCYAMINE SULFATE、PHENIRAMINE MALEATE、SCOPOLAMINE HBR、CHLO…</td><td>1992/12/21</td></tr><tr><td>衛署藥輸字第017759號</td><td>氫溴酸東莨菪/</td><td>SCOPOLAMINE HCL</td><td>2014/01/24</td></tr><tr><td>衛署藥輸字第019207號</td><td>腸賴泰膠囊劑</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019215號</td><td>腸賴泰錠劑</td><td>ATROPINE SULFATE、SCOPOLAMINE HBR、HYOSCYAMINE SULFATE、PHENOBA…</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019893號</td><td>氫溴酸東莨菪鹼</td><td>SCOPOLAMINE HBR</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第023064號</td><td>東莨菪鹼〝百靈佳〞</td><td>SCOPOLAMINE</td><td>2001/11/12</td></tr><tr><td>衛部藥輸字第027634號</td><td>氫溴酸東莨菪鹼</td><td>Scopolamine Hydrobromide</td><td>2025/03/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物與疾病禁忌關聯，並非仿單內容）：
  - 心血管與代謝：高血壓、糖尿病、糖尿病酮酸中毒
  - 肝腎與胰膽：肝衰竭、肝病、肝昏迷、腎病、胰臟炎、膽囊疾病、膿輸尿管
  - 眼部與呼吸：開角型青光眼、慢性阻塞性肺病
  - 神經精神：癲癇、焦慮症、神經症、輕度憂鬱症、精神病、類精神分裂症、情感性精神分裂症、精神疾患
  - 血液與代謝：紫質症（含遺傳性）、血小板低下、嗜中性白血球低下、顆粒球缺乏症
  - 其他：胃潰瘍、良性攝護腺肥大
- **藥物交互作用**：資料庫共收錄 298 筆交互作用。列出的項目多為中度，包括：
  - 鴉片類與中樞抑制劑：Fentanyl、Alfentanil、Codeine、Dihydrocodeine、Tramadol、乙醇
  - 其他抗膽鹼或具抗膽鹼作用藥物：Hyoscyamine、Aclidinium、Amitriptyline、Chlorpheniramine、Amantadine、Loperamide
  - 其他：Botulinum toxin type A、Phenylephrine、Acebutolol、Acetylcholine
  - 輕度：Acetaminophen、Hydrochlorothiazide

主要警語與禁忌症的仿單資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 六項預測皆僅有模型分數，沒有臨床試驗或文獻（L5）。馬尾症候群的主因是神經壓迫，抗膽鹼藥物無法處理，機轉支持薄弱。
- 排名第 2 的神經性膀胱機轉較合理，但疾病名稱已過時，需先釐清。

**若要推進需要：**
- 取得 Scopolamine 的作用機轉資料（MOA）
- 將「神經性膀胱」對應到現行疾病術語，並以該適應症重新檢索臨床試驗與文獻
- 評估是否應將神經性膀胱作為優先候選，而非馬尾症候群
- 若有文獻支持，先進行系統性文獻回顧，再考慮探索性臨床研究
- 針對目標族群（如高齡、青光眼、攝護腺肥大、中樞神經疾病患者）擬定安全性評估
- 確認給藥途徑與劑型是否適合新適應症

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯與英文原文）。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-11-25 | 「原適應症」取自丁基東莨菪鹼許可證，改為 scopolamine 本身的許可證適應症 | 更正（2026-11-25 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)；[NLM MeSH：Butylscopolammonium Bromide（D002086）](https://meshb.nlm.nih.gov/record/ui?ui=D002086)；[NLM MeSH：Scopolamine（D012601）](https://meshb.nlm.nih.gov/record/ui?ui=D012601) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國仿單節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Transderm Scop (scopolamine) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b877a694-a1d0-4280-937a-a06820b12a88) |
| 2026-11-25 | description 的原適應症取自丁基東莨菪鹼許可證 | 頁面描述（description）更正：原「原適應症：胃潰瘍、十二指腸潰瘍、胃炎、十二指腸炎、賁門痙攣、食道痙攣、膽囊炎、膽管炎、膽結石、尿路結石、膀胱痙攣、排尿困難及頻尿…」→「原適應症：胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣」 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-11-24；2026-11-25 程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

