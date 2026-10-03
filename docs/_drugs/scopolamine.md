---
layout: default
title: Scopolamine
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 6
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Scopolamine：從解痙劑到神經及眼科疾病探索

## 一句話總結

Scopolamine 主要用於胃腸道、膽道及尿路痙攣的緩解。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 及**神經源性膀胱**有效，
但目前缺乏臨床試驗及文獻支持這些新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃腸痙攣、膽管痙攣、尿路痙攣、女性生殖器痙攣 |
| 預測新適應症 | Cauda Equina Syndrome（馬尾症候群） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 179 張（有效單方 22／有效複方 35／已註銷 122） |
| 建議決策 | Hold |

<!-- review:begin scopolamine-butylscopolamine-licenses-2026-10-03 -->

> **查核加註（2026-10-03）**：上列適應症與下方許可證表的產品，主成分都是丁基東莨菪鹼（butylscopolamine bromide／hyoscine-N-butylbromide），例如內衛藥製字第010222號「南光」胃使可胖注射液、內衛藥製字第000509號「保賜康膠囊」。它是 scopolamine 的四級銨衍生物，與 scopolamine 本身是不同藥品（scopolamine 中樞作用較多）。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)；[NLM MeSH：Butylscopolammonium Bromide（D002086）](https://meshb.nlm.nih.gov/record/ui?ui=D002086)；[NLM MeSH：Scopolamine（D012601）](https://meshb.nlm.nih.gov/record/ui?ui=D012601)。

<!-- review:end scopolamine-butylscopolamine-licenses-2026-10-03 -->

## 為什麼這個預測合理？

Scopolamine（東莨菪鹼）是一種抗膽鹼藥物，作為毒蕈鹼受體拮抗劑，
能抑制副交感神經活動，達到解痙及減少分泌的效果。

**TxGNN 預測的新適應症與機轉關聯性分析：**

| 排名 | 預測適應症 | 預測分數 | TxGNN 排名 | 機轉關聯性 |
|------|-----------|---------|-----------|----------|
| 1 | Cauda Equina Syndrome（馬尾症候群） | 99.99% | 548 | 可能緩解神經壓迫引起的膀胱痙攣 |
| 2 | Neurogenic Bladder（神經源性膀胱） | 99.98% | 909 | 抗膽鹼作用可緩解膀胱過動 |
| 3 | Papillary Conjunctivitis（乳頭狀結膜炎） | 99.98% | 1,025 | 關聯性不明確 |
| 4 | Atopic Conjunctivitis（異位性結膜炎） | 99.80% | 4,736 | 關聯性不明確 |
| 5 | Rosacea Conjunctivitis（酒糟結膜炎） | 99.40% | 11,144 | 關聯性不明確 |
| 6 | Vernal Conjunctivitis（春季結膜炎） | 99.08% | 15,822 | 關聯性不明確 |

馬尾症候群及神經源性膀胱的預測較為合理，因為 Scopolamine 的抗膽鹼作用可緩解膀胱過動及痙攣症狀。
然而，結膜炎相關預測與已知機轉關聯性較弱。

## 臨床試驗證據

目前無針對預測適應症的相關臨床試驗登記。

## 文獻證據

目前無針對預測適應症的相關 PubMed 文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Scopolamine 的不重複許可證共 **179 張**：有效單方 22 張、有效複方 35 張、已註銷 122 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（22 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第002211號 | "強生"舒胃糖衣錠１０毫克 | 錠劑 | 強生化學製藥廠股份有限公司 | 2029/05/25 | 胃炎、十二指腸炎、腸疝痛、膽管痙攣、膽石疝痛、膽管炎、膽石症、膽囊剔除後之症候群 |
| 內衛藥製字第003516號 | "華琳"必息痛糖衣錠 | 糖衣錠 | 華琳實業有限公司 | 2028/05/25 | 胃腸潰瘍 |
| 內衛藥製字第007734號 | 施可保寧注射液 | 注射劑 | 安星製藥股份有限公司 | 2028/05/25 | 胃潰瘍、十二指腸潰瘍、胃炎、胃賁門痙攣、食道痙攣、膽囊炎、膽管炎、膀胱痛 |
| 內衛藥製字第009840號 | 勿賜痛注射液 | 注射劑 | 壽元化學工業股份有限公司 | 2028/05/25 | 腸疝痛、膽管之痙攣、膽石疝痛、膽管炎、痙攣性月經困難症 |
| 衛署藥製字第001735號 | "優生" 嘉平膜衣錠 | 膜衣錠 | 優生製藥廠股份有限公司 | 2028/05/25 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管、尿路痙攣 |
| 衛署藥製字第002635號 | 肚朗伴糖衣錠 | 糖衣錠 | 約克製藥股份有限公司 | 2028/05/25 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣 |
| 衛署藥製字第005612號 | 百痛賜安糖衣錠 | 糖衣錠 | 聯邦化學製藥股份有限公司 | 2024/05/25 | 胃、十二指腸潰瘍、胃、十二指腸炎、膽管、尿路之痙攣 |
| 衛署藥製字第007944號 | "福元" 得達息糖衣錠１０毫克 | 糖衣錠 | 福元化學製藥股份有限公司 | 2029/05/25 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣 |
| 衛署藥製字第011124號 | 腹茲方糖衣錠 | 糖衣錠 | 明德製藥股份有限公司 | 2029/05/25 | 胃、十二指腸潰瘍、胃炎、十二指胃腸炎、腸疝痛、膽石疝痛、膽管炎 |
| 衛署藥製字第014746號 | 普斯克膠囊 | 膠囊劑 | 永吉製藥股份有限公司 | 2024/05/25 | 胃腸管之痙攣及其運動機能亢進、膽管之痙攣及其運動障礙、尿路痙攣、女性生殖器之痙攣性疾患。 |
| 衛署藥製字第019505號 | "生達" 普治使可注射液（普斯克） | 注射劑 | 生達化學製藥股份有限公司 | 2029/11/24 | 抑制胃腸管、膽管、尿路、女性生殖器等之痙攣 |
| 衛署藥製字第020286號 | "皇佳" 舒痙平膠衣錠（普斯克） | 膜衣錠 | 皇佳化學製藥股份有限公司 | 2025/01/24 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽囊炎、膽道炎、膽石症 |
| 衛署藥製字第021614號 | 斯撲痙糖衣錠（普斯克） | 糖衣錠 | 衛肯生技製藥股份有限公司 | 2028/05/25 | 胃、十二指腸潰瘍、食道痙攣、胃炎、腸炎、膽囊、膽管炎、膽石症、尿路結石症、膀胱炎 |
| 衛署藥製字第033598號 | "大豐"寶賜可安注射液２０毫克/毫升 | 注射劑 | 大豐製藥股份有限公司 | 2029/05/25 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管痙攣、膽石疝痛 |
| 衛署藥製字第034079號 | 〝井田〞必舒痛膜衣錠10毫克(東茛菪  ) | 膜衣錠 | 井田國際醫藥廠股份有限公司 | 2028/05/25 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管、尿道之痙攣 |
| 衛署藥製字第035285號 | "羅得"順胃錠１０公絲（東莨菪生僉) | 錠劑 | 羅得化學製藥股份有限公司 | 2027/05/27 | 胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣。 |
| 衛署藥製字第037656號 | "永勝"舒可平膜衣錠１０公絲（普斯克） | 膜衣錠 | 永勝藥品工業股份有限公司 | 2029/06/07 | 下列疾患之痙攣及運動機能亢進：胃、十二指腸潰瘍、食道痙攣、幽門痙攣、胃炎、腸炎、腸疝痛、痙攣性便秘、機能性下痢、膽囊、膽管炎、膽石症、膽道運動障礙、膽囊切除後遺症、尿路結石症、膀胱… |
| 衛署藥製字第039561號 | 立好痙膜衣錠１０公絲（澳化丁基東茛菪　） | 膜衣錠 | 中國化學製藥股份有限公司新豐工廠 | 2030/11/22 | 下列疾患之痙攣及運動機能亢進、胃、十二指腸潰瘍、食道痙攣、幽門痙攣、胃炎、腸炎、腸疝痛、痙攣性便秘、機能性下痢、膽囊、膽管炎、膽石症、膽道運動障礙、膽囊切除後道症、尿路結石症、膀胱… |
| 衛署藥製字第044712號 | 暈得寧防暈貼片劑1.5毫克(東茛菪儉) | 穿皮貼片劑 | 華健醫藥生技股份有限公司湖口廠 | 2026/11/20 | 預防或緩解動暈症(暈車、暈船、暈機)引起之頭暈、噁心、嘔吐、頭痛等症狀。 |
| 衛署藥輸字第022727號 | 補斯可胖注射液 | 注射劑 | 台灣大昌華嘉股份有限公司 | 2029/12/31 | 胃腸痙攣及運動亢進、膽管痙攣及其運動障礙、尿路痙攣、女性生殖器之痙攣症狀。 |
| 衛署藥輸字第025341號 | 溴化丁基東莨菪鹼 | （粉） | 川聖貿易股份有限公司 | 2031/01/24 | 副交感神經抑制劑 |
| 衛部藥輸字第027154號 | "艾卡羅"溴化丁基東莨菪鹼 | （粉） | 新雙隆生技股份有限公司 | 2027/08/18 | 副交感神經抑制劑 |

<details><summary><strong>有效・複方（適應症屬整個複方，不是本藥單獨的適應症）</strong>（35 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>劑型</th><th>核准適應症</th></tr></thead><tbody><tr><td>內衛藥製字第000370號</td><td>"永信" 使莫痛錠</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>錠劑</td><td>胃酸過多、胃痛、賁門痙攣、幽門痙攣、胃、十二指腸潰瘍、胃炎、腸炎、腎石絞痛、月經痛、膽石絞痛、支氣管性氣喘等</td></tr><tr><td>內衛藥製字第000978號</td><td>舒百林錠</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、ATROPINE SULFATE、SCOPOLAMI…</td><td>錠劑</td><td>胃腸痙攣、胃潰瘍、十二指腸潰瘍、膽管膽囊痙攣、膽結石痛、腎結石痛、月經痛、胃痛、胃酸過多</td></tr><tr><td>內衛藥製字第005458號</td><td>Ａ．Ｄ．Ａ．胃片</td><td>PHENOBARBITAL、DIHYDROXYALUMINUM AMINOACETATE、SCOPOLAMINE HBR</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃疼痛、胃痙攣、胃酸過多、腸胃充氣</td></tr><tr><td>內衛藥製字第013417號</td><td>速立舒錠</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE S…</td><td>錠劑</td><td>胃痛、賁門或幽門痙攣、胃、十二指腸潰瘍、腎、膽結石、絞痛、尿道結石痛、支氣管性氣喘</td></tr><tr><td>衛署藥製字第002086號</td><td>胃爾寧片</td><td>ALUMINUM SILICATE、CHLORDIAZEPOXIDE HCL、MAGNESIUM OXIDE、ALUMI…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、胃炎</td></tr><tr><td>衛署藥製字第002328號</td><td>"中國化學製藥" 防暈片</td><td>DIPHENHYDRAMINE TANNATE、CHLORPHENIRAMINE MALEATE、SCOPOLAMINE…</td><td>錠劑</td><td>坐車、船或飛機所引起之頭暈、噁心和嘔吐</td></tr><tr><td>衛署藥製字第003773號</td><td>"永吉"助胃康錠</td><td>SCOPOLAMINE BROMOBUTYLATE、DICYCLOMINE HCL、MAGNESIUM ALUMINUM…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、胃炎</td></tr><tr><td>衛署藥製字第006236號</td><td>"嘉林" 哺順痛糖衣錠</td><td>SCOPOLAMINE BROMOBUTYLATE、SCOPOLAMINE BROMOBUTYLATE</td><td>糖衣錠</td><td>胃、十二指腸潰瘍、胃炎、十二指腸炎、腸疝痛、膽管尿路痙攣</td></tr><tr><td>衛署藥製字第009312號</td><td>"黃氏" 紓躁整腸錠</td><td>BERBERINE TANNATE、SCOPOLAMINE METHYL BROMIDE、ALUMINUM SILICA…</td><td>錠劑</td><td>痢疾、腹瀉、腸炎、腹痛</td></tr><tr><td>衛署藥製字第010172號</td><td>治痢錠</td><td>BERBERINE TANNATE、CHLORPHENIRAMINE MALEATE、ETHACRIDINE LACTA…</td><td>錠劑</td><td>急、慢性腹瀉、細菌性腹瀉、食物中毒、神經性腹瀉、消化不良性腹瀉、急慢性腸炎、鼓腸、過敏性腸疾患</td></tr><tr><td>衛署藥製字第010487號</td><td>"華興" 華舒胃錠</td><td>MAGNESIUM OXIDE、CHLORDIAZEPOXIDE、MAGNESIUM ALUMINUM HYDROXID…</td><td>錠劑</td><td>胃、十二指潰瘍、胃痛、胃酸過多、胃痙攣、胃炎</td></tr><tr><td>衛署藥製字第011007號</td><td>"派頓" 來克痢錠</td><td>ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)、BERBERINE TANNATE、…</td><td>錠劑</td><td>下痢、腸炎、腹痛、消化不良、鼓腸、腸內異常醱酵</td></tr><tr><td>衛署藥製字第012340號</td><td>“光南”金胃錠</td><td>ALUMINUM SILICATE、CHLORDIAZEPOXIDE HCL、MAGNESIUM OXIDE、CHLOR…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、急、慢性胃炎。</td></tr><tr><td>衛署藥製字第012868號</td><td>適腸錠</td><td>BERBERINE TANNATE、ALUMINUM SILICATE、ETHACRIDINE LACTATE MONO…</td><td>錠劑</td><td>痢疾、腹瀉、腸炎、腹痛</td></tr><tr><td>衛署藥製字第013931號</td><td>痛立寧錠</td><td>SCOPOLAMINE HBR、CAFFEINE、ERGOTAMINE TARTRATE、PHENOBARBITAL</td><td>錠劑</td><td>偏頭痛</td></tr><tr><td>衛署藥製字第014832號</td><td>"永信"胃必朗粉末</td><td>CHLORDIAZEPOXIDE HCL、MAGNESIUM OXIDE、MAGNESIUM ALUMINUM HYDR…</td><td>粉劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、胃炎。</td></tr><tr><td>衛署藥製字第016594號</td><td>"歐業"胃勇安錠</td><td>MAGNESIUM OXIDE、CHLORDIAZEPOXIDE HCL、ALUMINUM SILICATE、DICYC…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、急慢性胃炎</td></tr><tr><td>衛署藥製字第017124號</td><td>"明大"胃雅錠</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>錠劑</td><td>消化性潰瘍、過敏性腸疾患（過敏性結腸、痙攣性結腸、粘液性結腸炎）急性腸結腸炎</td></tr><tr><td>衛署藥製字第019115號</td><td>"派頓"派暈吐錠</td><td>DIPROPHYLLINE、DIMENHYDRINATE、PYRIDOXINE HCL、SCOPOLAMINE HBR</td><td>錠劑</td><td>暈動病（噁心、暈眩、頭痛）噁心、嘔吐之預防及治療</td></tr><tr><td>衛署藥製字第019929號</td><td>"中菱"鎮暈錠</td><td>DIMENHYDRINATE、SCOPOLAMINE HBR、CAFFEINE ANHYDROUS</td><td>錠劑</td><td>預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀。</td></tr><tr><td>衛署藥製字第020019號</td><td>"長安"腸胃炎痛膠囊</td><td>ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)、CHLORPHENIRAMINE M…</td><td>膠囊劑</td><td>腸炎、腹痛、消化不良、腸內異常醱酵</td></tr><tr><td>衛署藥製字第021231號</td><td>"長安"立百舒糖衣錠</td><td>PHENOBARBITAL、ERGOTAMINE TARTRATE、CAFFEINE ANHYDROUS、SCOPOLA…</td><td>糖衣錠</td><td>偏頭痛</td></tr><tr><td>衛署藥製字第022023號</td><td>服舒寧錠</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE S…</td><td>錠劑</td><td>胃腸痙攣、胃腸炎、胃、十二指腸潰瘍、胃酸過多、膽囊炎、膽結石、膀胱炎、月經痛、遺尿症、頻尿</td></tr><tr><td>衛署藥製字第022219號</td><td>克暈明錠</td><td>DIPROPHYLLINE、DIMENHYDRINATE、PYRIDOXINE HCL、SCOPOLAMINE HBR</td><td>錠劑</td><td>暈動病（噁心、暈眩、頭痛）噁心、嘔吐之預防及治療</td></tr><tr><td>衛署藥製字第023313號</td><td>"中美" 潰胃爽錠</td><td>DICYCLOMINE HCL、SCOPOLAMINE BROMOBUTYLATE、ALUMINUM SILICATE、…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多症、胃痙攣、急、慢性胃炎。</td></tr><tr><td>衛署藥製字第023415號</td><td>"健康"胃安寧錠</td><td>DICYCLOMINE HCL、CHLORDIAZEPOXIDE HCL、SCOPOLAMINE BROMOBUTYLA…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、急、慢性胃炎</td></tr><tr><td>衛署藥製字第025571號</td><td>舒痛錠</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、HYOSCYAMINE SULFATE、PHENOBA…</td><td>錠劑</td><td>胃腸痙攣、胃腸炎、胃、十二指腸潰瘍</td></tr><tr><td>衛署藥製字第029418號</td><td>"大豐" 必胃健錠</td><td>MAGNESIUM OXIDE、CHLORDIAZEPOXIDE、MAGNESIUM ALUMINUM HYDROXID…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、胃炎</td></tr><tr><td>衛署藥製字第033157號</td><td>"井田" 胃舒服錠</td><td>CHLOROPHYLL SODIUM COPPER、CHLORDIAZEPOXIDE HCL、MAGNESIUM HYD…</td><td>錠劑</td><td>胃、十二指腸潰瘍、胃痛、胃酸過多、胃痙攣、胃炎。</td></tr><tr><td>衛署藥製字第035398號</td><td>多樂滅暈錠</td><td>CAFFEINE ANHYDROUS、MECLIZINE HCL ( EQ TO MECLIZINE HYDROCHLO…</td><td>錠劑</td><td>暈動引起之目眩、噁心、嘔吐、頭痛之預防及緩和。</td></tr><tr><td>衛署藥製字第038592號</td><td>"黃氏"富旅安錠</td><td>DIMENHYDRINATE、CAFFEINE、SCOPOLAMINE HBR</td><td>錠劑</td><td>預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐、頭痛等症狀。</td></tr><tr><td>衛署藥製字第040049號</td><td>雅寧錠</td><td>CAFFEINE ANHYDROUS、SCOPOLAMINE HBR、DIMENHYDRINATE</td><td>錠劑</td><td>預防或緩解暈車、暈船、暈機所引起之頭暈、嘔吐、頭痛、噁心．</td></tr><tr><td>衛署藥製字第040067號</td><td>舒胃膠囊</td><td>BENZOCAINE (ETHYL AMINOBENZOATE)、PAPAVERINE HCL、SCOPOLAMINE…</td><td>膠囊劑</td><td>腹痛、腸絞痛（疝痛）、胃痛、胃酸過多</td></tr><tr><td>衛署藥製字第046047號</td><td>施克錠</td><td>SCOPOLAMINE HBR、CAFFEINE、PROMETHAZINE HCL</td><td>錠劑</td><td>暈動病(噁心、眩暈)之預防與治療。</td></tr><tr><td>衛署藥製字第050067號</td><td>抗暈 錠</td><td>DIPROPHYLLINE、DIMENHYDRINATE、SCOPOLAMINE HBR、PYRIDOXINE HCL</td><td>錠劑</td><td>暈動病(惡心、暈眩、頭痛)、噁心、嘔吐之預防及治療。</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（122 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000161號</td><td>益舒錠</td><td>SCOPOLAMINE HBR、BENZOCAINE (ETHYL AMINOBENZOATE)、ETHAVERINE…</td><td>1989/11/24</td></tr><tr><td>內衛藥製字第000463號</td><td>速舒鎮膠囊</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE S…</td><td>1999/08/23</td></tr><tr><td>內衛藥製字第000794號</td><td>痙泰片</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、HYOSCYAMINE SULFATE、PHENOBA…</td><td>1997/02/26</td></tr><tr><td>內衛藥製字第000979號</td><td>普治使可糖衣錠</td><td>SCOPOLAMINE-N-BUTYLBROMIDE</td><td>2025/04/25</td></tr><tr><td>內衛藥製字第001293號</td><td>百泰適片</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、DIASTASE A…</td><td>1998/07/06</td></tr><tr><td>內衛藥製字第002333號</td><td>富仕伴注射液</td><td>SCOPOLAMINE BROMOBUTYLATE、SULPYRINE (EQ TO DIPYRONE )</td><td>1998/08/17</td></tr><tr><td>內衛藥製字第002337號</td><td>多託寧錠</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE S…</td><td>1989/06/20</td></tr><tr><td>內衛藥製字第002601號</td><td>"好漢賓" 速克痙錠</td><td>SCOPOLAMINE HBR、ATROPINE、PHENOBARBITAL、HYOSCYAMINE SULFATE</td><td>2014/05/15</td></tr><tr><td>內衛藥製字第003376號</td><td>"應元" 快胃胖注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2024/04/19</td></tr><tr><td>內衛藥製字第003675號</td><td>"強生" 抑痛錠</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>2023/10/26</td></tr><tr><td>內衛藥製字第004508號</td><td>胃樂康錠</td><td>CHLOROPHYLL SODIUM COPPER、MAGNESIUM ALUMINUM HYDROXIDE CO-DR…</td><td>2016/09/08</td></tr><tr><td>內衛藥製字第005352號</td><td>胃津－Ｂ膠囊</td><td>BENACTYZINE METHOBROMIDE (BENACTYZINE METHYLBROMIDE)、SCOPOLA…</td><td>2023/07/07</td></tr><tr><td>內衛藥製字第006963號</td><td>維胃膠囊</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、HYOSCYAMINE SULFATE、PHENOBA…</td><td>1999/12/30</td></tr><tr><td>內衛藥製字第007845號</td><td>抗痛注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1993/05/24</td></tr><tr><td>內衛藥製字第008012號</td><td>克痛糖衣錠</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1992/03/18</td></tr><tr><td>內衛藥製字第008973號</td><td>速拔痛片</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>2010/11/18</td></tr><tr><td>內衛藥製字第009771號</td><td>阿托拍注射液</td><td>SCOPOLAMINE HBR、ETHAVERINE HCL (eq to BALBONIN) (eq to Ethyl…</td><td>2025/04/29</td></tr><tr><td>內衛藥製字第012060號</td><td>速克痛注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2013/10/14</td></tr><tr><td>內衛藥製字第012089號</td><td>"人生"必舒痛錠</td><td>HYOSCYAMINE SULFATE、PHENOBARBITAL、ATROPINE SULFATE、SCOPOLAMI…</td><td>2026/08/17</td></tr><tr><td>內衛藥製字第012958號</td><td>氫溴酸東莨菪鹼注射液</td><td>SCOPOLAMINE HBR</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第015667號</td><td>司力多寧片</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、ATROPINE SULFATE、SCOPOLAMI…</td><td>1991/07/24</td></tr><tr><td>內衛藥製字第016982號</td><td>丁溴化東莨菪/</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2010/02/08</td></tr><tr><td>內衛藥輸字第000981號</td><td>氫溴酸東莨/</td><td>SCOPOLAMINE HBR</td><td>1986/03/15</td></tr><tr><td>內衛藥輸字第002192號</td><td>胃劑壯片</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1985/11/01</td></tr><tr><td>內衛藥輸字第002404號</td><td>胃齊壯針</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第002785號</td><td>治暈克</td><td>SCOPOLAMINE HBR</td><td>1987/05/14</td></tr><tr><td>內衛藥輸字第003861號</td><td>速可寶胃命</td><td>PHENOBARBITAL、SCOPOLAMINE METHYLNITRATE</td><td>1987/05/14</td></tr><tr><td>內衛藥輸字第004339號</td><td>愛達爾</td><td>SCOPOLAMINE HBR、MECLIZINE HCL ( EQ TO MECLIZINE HYDROCHLORID…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第004597號</td><td>長效速麻林</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、HYOSCYAMINE SULFATE、PHENOBA…</td><td>1987/05/14</td></tr><tr><td>內衛藥輸字第005759號</td><td>施克片</td><td>PROMETHAZINE HCL、SCOPOLAMINE、CAFFEINE</td><td>1986/01/18</td></tr><tr><td>內衛藥輸字第005917號</td><td>百宿納</td><td>SCOPOLAMINE HCL、DIHYDROERGOCORNINE METHANESULPHONATE、PHENOBA…</td><td>1991/02/01</td></tr><tr><td>內衛藥輸字第006024號</td><td>酵母源</td><td>PROTASE (PROTEOLYTIC ENZYME)、AMYLOLYTIC ENZYME、HYOSCYAMINE H…</td><td>1999/09/22</td></tr><tr><td>衛署藥製字第000230號</td><td>蒙汝康恩須古布羅命注射液</td><td>EPINEPHRINE HCL、DIMETHYLAMINOETHYL-BETA-BENZILAMIDE HCL、SCOP…</td><td>1991/05/06</td></tr><tr><td>衛署藥製字第000693號</td><td>和瓏錠</td><td>SYNTHETIC ALUMINUM SILICATE、ALUMINUM MAGNESIUM HYDROXIDE GEL…</td><td>2023/12/07</td></tr><tr><td>衛署藥製字第002144號</td><td>必舒痛糖衣錠</td><td>SCOPOLAMINE</td><td>1991/09/03</td></tr><tr><td>衛署藥製字第002330號</td><td>快寧胃糖衣錠</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第002955號</td><td>"永新" 克胃痛膠囊</td><td>HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S…</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第005571號</td><td>希斯伴糖衣錠</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1993/12/15</td></tr><tr><td>衛署藥製字第005855號</td><td>鹽酸全阿片素東莨菪/注射液</td><td>PANTOPON HCL、SCOPOLAMINE HBR</td><td>2014/01/22</td></tr><tr><td>衛署藥製字第006774號</td><td>百痛賜安注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2023/08/15</td></tr><tr><td>衛署藥製字第006859號</td><td>信可伴注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2013/04/08</td></tr><tr><td>衛署藥製字第007053號</td><td>痢必益錠</td><td>ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)、SCOPOLAMINE METHOB…</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第008492號</td><td>必胃健錠</td><td>MAGNESIUM ALUMINUM HYDROXIDE CO-DRIED GEL、CHLOROPHYLL SODIUM…</td><td></td></tr><tr><td>衛署藥製字第008534號</td><td>舒可補痙注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2023/09/13</td></tr><tr><td>衛署藥製字第010538號</td><td>保舒康寧注射液</td><td>SCOPOLAMINE HBR、PAPAVERINE HCL</td><td>1989/06/20</td></tr><tr><td>衛署藥製字第011456號</td><td>"德星" 佛賜佳因注射液</td><td>CAFFEINE、SCOPOLAMINE HBR、PROCAINE HCL、ATROPINE SULFATE、PYRAB…</td><td>1997/12/22</td></tr><tr><td>衛署藥製字第011912號</td><td>理克痙栓劑１０公絲</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1998/07/28</td></tr><tr><td>衛署藥製字第012087號</td><td>痢癒速錠</td><td>ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)、BERBERINE TANNATE、…</td><td>1991/06/22</td></tr><tr><td>衛署藥製字第012325號</td><td>衛吾胃錠</td><td>CHLOROPHYLL SODIUM COPPER、MAGNESIUM ALUMINUM HYDROXIDE CO-DR…</td><td>2013/10/11</td></tr><tr><td>衛署藥製字第012694號</td><td>"明德" 癒胃全錠</td><td>SCOPOLAMINE BROMOBUTYLATE、DICYCLOMINE HCL、ALUMINUM HYDROXIDE…</td><td>2015/09/11</td></tr><tr><td>衛署藥製字第013548號</td><td>"中菱" 好胃舒錠</td><td>SYNTHETIC ALUMINUM SILICATE、MAGNESIUM ALUMINUM HYDROXIDE CO-…</td><td>2026/08/18</td></tr><tr><td>衛署藥製字第015206號</td><td>"美時" 衛吾胃顆粒</td><td>MAGNESIUM ALUMINUM HYDROXIDE CO-DRIED GEL、CHLORDIAZEPOXIDE、C…</td><td>2013/10/11</td></tr><tr><td>衛署藥製字第015466號</td><td>阿羅使爾必拉注射液</td><td>ATROPINE SULFATE、PYRABITAL (AMINOPYRINE+BARBITAL)、SCOPOLAMIN…</td><td>1999/08/05</td></tr><tr><td>衛署藥製字第016204號</td><td>"井田" 維他安痙錠</td><td>VITAMIN B6 (HCL)、SCOPOLAMINE HBR、RIBOFLAVIN (VIT B2)、THIAMIN…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第018187號</td><td>舒鎮痙錠</td><td>HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S…</td><td>1987/06/02</td></tr><tr><td>衛署藥製字第018262號</td><td>滋胃錠</td><td>ALUMINUM SILICATE、MAGNESIUM OXIDE、CHLORDIAZEPOXIDE、MAGNESIUM…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第019356號</td><td>百痢安錠</td><td>BERBERINE TANNATE、CHLORPHENIRAMINE MALEATE、ETHACRIDINE LACTA…</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第019762號</td><td>豐克膠囊</td><td>PHENYLEPHRINE HCL、PHENYLEPHRINE HCL、CHLORPHENIRAMINE MALEATE…</td><td>2009/04/15</td></tr><tr><td>衛署藥製字第020322號</td><td>複方甘氨酸鋁錠</td><td>PHENOBARBITAL、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCO…</td><td>1998/06/01</td></tr><tr><td>衛署藥製字第020632號</td><td>胃比好錠</td><td>SCOPOLAMINE HCL、PHENOBARBITAL</td><td>2016/09/20</td></tr><tr><td>衛署藥製字第020869號</td><td>奇克錠</td><td>DIMENHYDRINATE、SCOPOLAMINE HBR、CAFFEINE</td><td>2016/09/20</td></tr><tr><td>衛署藥製字第023288號</td><td>可得平注射液（東莨菪鹼）</td><td>SCOPOLAMINE-N-BUTYLBROMIDE</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第023910號</td><td>胃多力錠</td><td>CHLOROPHYLL SODIUM COPPER、SCOPOLAMINE BROMOBUTYLATE、DICYCLOM…</td><td>1991/02/13</td></tr><tr><td>衛署藥製字第024064號</td><td>胃多力散</td><td>MAGNESIUM (OXIDE)、SCOPOLAMINE BROMOBUTYLATE、DICYCLOMINE HCL、…</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第024083號</td><td>胃多力膠囊</td><td>SCOPOLAMINE BROMOBUTYLATE、DICYCLOMINE HCL、MAGNESIUM ALUMINUM…</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第024599號</td><td>安治錠</td><td>HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第024679號</td><td>"壽元"安得樂錠</td><td>DICYCLOMINE HCL、SCOPOLAMINE HBR、PHENOBARBITAL、ETHAVERINE HCL…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第025350號</td><td>頭暈痛錠</td><td>SCOPOLAMINE HBR、CAFFEINE ANHYDROUS、DIMENHYDRINATE</td><td>1999/12/10</td></tr><tr><td>衛署藥製字第026742號</td><td>胃必寧錠</td><td>MAGNESIUM ALUMINUM HYDROXIDE CO-DRIED GEL、CHLOROPHYLL SODIUM…</td><td>2025/04/29</td></tr><tr><td>衛署藥製字第026757號</td><td>胃寧錠</td><td>CHLORDIAZEPOXIDE HCL、MAGNESIUM ALUMINUM HYDROXIDE CO-DRIED G…</td><td>2023/07/12</td></tr><tr><td>衛署藥製字第030576號</td><td>喜胃隆錠</td><td>DICYCLOMINE HCL、SCOPOLAMINE BROMOBUTYLATE、ALUMINUM HYDROXIDE…</td><td>2004/10/06</td></tr><tr><td>衛署藥製字第033141號</td><td>胃多力錠</td><td>SCOPOLAMINE BROMOBUTYLATE、DICYCLOMINE HCL、MAGNESIUM ALUMINUM…</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第033611號</td><td>痢癒速錠</td><td>ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)、SCOPOLAMINE METHOB…</td><td>1997/09/23</td></tr><tr><td>衛署藥製字第033759號</td><td>蒙汝康恩須古布羅命注射液</td><td>EPINEPHRINE HCL、DIMETHYLAMINOETHYL-BETA-BENZILAMIDE HCL、PROC…</td><td>1992/01/13</td></tr><tr><td>衛署藥製字第033869號</td><td>司力多寧錠</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>2026/08/03</td></tr><tr><td>衛署藥製字第034820號</td><td>滋胃錠</td><td>SCOPOLAMINE BROMOBUTYLATE、DICYCLOMINE HCL、ALUMINUM SILICATE、…</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第036715號</td><td>希斯伴糖衣錠１０公絲（東莨菪＊）</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第040432號</td><td>痙泰錠</td><td>HYOSCYAMINE (SULFATE)、PHENOBARBITAL、ATROPINE SULFATE、SCOPOLA…</td><td>1998/10/08</td></tr><tr><td>衛署藥製字第041263號</td><td>痢癒速錠</td><td>SCOPOLAMINE METHOBROMIDE、BERBERINE TANNATE、SYNTHETIC ALUMINU…</td><td>2019/03/22</td></tr><tr><td>衛署藥輸字第001286號</td><td>溴化丁基莨菪鹼</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第002124號</td><td>氫溴酸東莨菪/</td><td>SCOPOLAMINE HBR</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003182號</td><td>丁溴化東莨菪/</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第003463號</td><td>丁溴化東莨菪/</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第004594號</td><td>補斯可胖糖衣錠</td><td>CALCIUM PHOSPHATE DIBASIC、SCOPOLAMINE BROMOBUTYLATE</td><td>1986/04/07</td></tr><tr><td>衛署藥輸字第004596號</td><td>補斯可胖注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第004699號</td><td>補斯可胖坐劑</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第005725號</td><td>腸賴泰錠劑</td><td>HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005746號</td><td>腸賴泰膠囊劑</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、PHENOBARBITAL、HYOSCYAMINE S…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005809號</td><td>腸賴泰酏劑</td><td>CALCIUM OXIDE ISOLATE、HYOSCYAMINE SULFATE、PHENOBARBITAL、ATRO…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第005826號</td><td>保妥錠</td><td>DIPROPHYLLINE、DIMENHYDRINATE、PYRIDOXINE HCL、SCOPOLAMINE HBR</td><td>1999/03/11</td></tr><tr><td>衛署藥輸字第006186號</td><td>莨菪素氮－丁基溴</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第006952號</td><td>溴化丁基東莨菪/</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第006955號</td><td>甲基硝酸東莨菪鹼</td><td>SCOPOLAMINE METHYLNITRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006962號</td><td>氫溴酸東莨菪鹼</td><td>SCOPOLAMINE HBR</td><td>2006/09/25</td></tr><tr><td>衛署藥輸字第007595號</td><td>不使胃潰糖衣錠</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第007847號</td><td>立治痙潰糖衣錠</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第007948號</td><td>立治痙潰注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第009733號</td><td>達羅明顆粒</td><td>DEHYDROCHOLIC ACID、CINNAMON OIL (OLEUM CINNAMOMI)、FENNEL OIL…</td><td>1986/01/21</td></tr><tr><td>衛署藥輸字第009823號</td><td>普樂斯伴糖衣錠</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1993/07/06</td></tr><tr><td>衛署藥輸字第010048號</td><td>感適平膠囊</td><td>PHENYLPROPANOLAMINE HCL (DL-NOREPHEDRINE HCL)、ATROPINE SULFA…</td><td>1989/07/19</td></tr><tr><td>衛署藥輸字第010644號</td><td>安神錠</td><td>ATROPINE SULFATE、SCOPOLAMINE HBR、PHENOBARBITAL、BELLADONNA LE…</td><td>1986/05/12</td></tr><tr><td>衛署藥輸字第011017號</td><td>安治達持續性膠囊</td><td>HYOSCYAMINE SULFATE、PHENIRAMINE MALEATE、CHLORPHENIRAMINE MAL…</td><td>1986/03/28</td></tr><tr><td>衛署藥輸字第011025號</td><td>優治胃錠</td><td>ATROPINE SULFATE、SCOPOLAMINE HBR、HYOSCYAMINE SULFATE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第011087號</td><td>腸納格懸液</td><td>SCOPOLAMINE HBR、ATROPINE SULFATE、LIME ISOLATE、PECTIN、KAOLIN…</td><td>1993/12/20</td></tr><tr><td>衛署藥輸字第012334號</td><td>益斯壯粉劑</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1985/08/28</td></tr><tr><td>衛署藥輸字第012717號</td><td>巴斯碰注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第012884號</td><td>克暈貼片</td><td>SCOPOLAMINE</td><td>1993/05/19</td></tr><tr><td>衛署藥輸字第014156號</td><td>胃齊壯注射液</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2004/12/10</td></tr><tr><td>衛署藥輸字第014259號</td><td>胃齊壯錠</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2004/12/10</td></tr><tr><td>衛署藥輸字第014674號</td><td>達羅明顆粒</td><td>INOSITOL (MESO-INOSITOL)、GLYCYRRHETATE AMMONIUM、AMYLASE ALPH…</td><td>1993/07/30</td></tr><tr><td>衛署藥輸字第014683號</td><td>施克錠</td><td>CAFFEINE、SCOPOLAMINE HBR、PROMETHAZINE HCL</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第014952號</td><td>賜妥錠</td><td>PHENOBARBITAL、ERGOTAMINE TARTRATE、HYOSCYAMINE SULFATE、ATROPI…</td><td>1994/04/25</td></tr><tr><td>衛署藥輸字第015636號</td><td>丁溴化東莨菪鹼</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第017231號</td><td>感適平膠囊</td><td>CHLORPHENIRAMINE MALEATE、PHENIRAMINE MALEATE、HYOSCYAMINE SUL…</td><td>1992/12/21</td></tr><tr><td>衛署藥輸字第017759號</td><td>氫溴酸東莨菪/</td><td>SCOPOLAMINE HCL</td><td>2014/01/24</td></tr><tr><td>衛署藥輸字第017763號</td><td>丁溴化東莨菪/</td><td>SCOPOLAMINE BROMOBUTYLATE</td><td>2014/01/24</td></tr><tr><td>衛署藥輸字第019207號</td><td>腸賴泰膠囊劑</td><td>HYOSCYAMINE SULFATE、PHENOBARBITAL、SCOPOLAMINE HBR、ATROPINE S…</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019215號</td><td>腸賴泰錠劑</td><td>PHENOBARBITAL、HYOSCYAMINE SULFATE、SCOPOLAMINE HBR、ATROPINE S…</td><td>2002/06/13</td></tr><tr><td>衛署藥輸字第019893號</td><td>氫溴酸東莨菪鹼</td><td>SCOPOLAMINE HBR</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第023064號</td><td>東莨菪鹼〝百靈佳〞</td><td>SCOPOLAMINE</td><td>2001/11/12</td></tr><tr><td>衛部藥輸字第027634號</td><td>氫溴酸東莨菪鹼</td><td>Scopolamine Hydrobromide</td><td>2025/03/21</td></tr><tr><td>衛部藥輸字第027699號</td><td>溴化丁基東莨菪鹼</td><td>Scopolamine Butylbromide</td><td>2025/03/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

- **主要藥物交互作用（重大）**：
  - Topiramate、Zonisamide：可能增加體溫調節障礙風險

- **中度藥物交互作用**：
  - 鴉片類藥物：Fentanyl、Morphine、Codeine、Hydrocodone、Tramadol、Buprenorphine 等
  - 抗膽鹼藥物：Atropine、Hyoscyamine、Glycopyrronium、Benzatropine 等
  - 抗精神病藥物：Aripiprazole、Asenapine、Brexpiprazole 等
  - 抗組織胺藥物：Chlorpheniramine、Brompheniramine 等
  - 乙型阻斷劑：Atenolol、Bisoprolol、Acebutolol 等
  - 其他：Ethanol、Amantadine、Amitriptyline、Loperamide

- **輕度藥物交互作用**：
  - Acetaminophen、Hydrochlorothiazide

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測的馬尾症候群及神經源性膀胱適應症與 Scopolamine 的抗膽鹼作用機轉有一定關聯，
但目前缺乏臨床試驗及文獻支持。結膜炎相關預測則與已知機轉關聯性較弱。

**若要推進需要：**
- 針對神經源性膀胱的臨床試驗數據
- 探索 Scopolamine 在馬尾症候群相關膀胱功能障礙的應用
- 評估長期使用的安全性，特別是與其他抗膽鹼藥物併用時

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」與許可證表皆為丁基東莨菪鹼（butylscopolamine） | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)；[NLM MeSH：Butylscopolammonium Bromide（D002086）](https://meshb.nlm.nih.gov/record/ui?ui=D002086)；[NLM MeSH：Scopolamine（D012601）](https://meshb.nlm.nih.gov/record/ui?ui=D012601) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

