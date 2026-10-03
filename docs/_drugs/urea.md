---
layout: default
title: Urea
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 0
---

# Urea
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Urea 藥師評估報告

## 一句話總結

Urea (尿素) 是一種滲透性利尿劑和角質溶解劑，目前 TxGNN 預測系統未發現任何新適應症預測，反映此藥物在知識圖譜中缺乏與新疾病的顯著連結。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Urea (尿素) |
| DrugBank ID | DB03904 |
| 原核准適應症 | 創傷護理、消毒、乾燥皮膚治療等 |
| 預測新適應症數量 | 0 項 |
| 最高預測分數適應症 | 無 |
| 臨床試驗支持 | 不適用 |
| 文獻證據 | 不適用 |
| 台灣上市狀態 | 有效許可證（以去角質用尿素乳膏為主） |

<!-- review:begin urea-tw-status-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「台灣上市狀態／多為已註銷；少數含 urea 衍生物藥品有效」。TFDA 資料集中主成分含 urea 的許可證 70 張，其中 43 張未註銷，多為去角質用尿素乳膏；頁面所說的「urea 衍生物」DPP-4 抑制劑並不含 urea。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end urea-tw-status-2026-10-03 -->

---

## 為什麼無預測適應症

### 分析說明

1. **藥物特性**
   - Urea 是人體正常代謝產物
   - 作用機轉相對單純：滲透性利尿、角質溶解
   - 在 TxGNN 知識圖譜中可能缺乏與其他疾病的顯著關聯邊

2. **預測篩選結果**
   - 所有預測分數可能低於 0.99 的篩選閾值
   - 或完全無符合新適應症定義的預測

3. **可能原因**
   - Urea 主要為外用製劑，系統性藥理作用有限
   - 作為天然代謝物，與疾病的特異性關聯較弱

---

## 臨床試驗

**不適用** - 無預測適應症需要評估

---

## 文獻證據

**不適用** - 無預測適應症需要評估

---

## 台灣上市資訊

### 歷史許可證 (大部分已註銷)

台灣 FDA 搜尋結果顯示共有 456 筆含 "urea" 相關產品紀錄，包括：

| 類別 | 代表性品名 | 適應症 | 狀態 |
|------|------------|--------|------|
| 外用消毒 | 阿克利諾兒錠 | 創傷、化膿性疾患 | 已註銷 |
| 鎮靜催眠 | 異纈草酸溴 (Bromvalerylurea) | 失眠、焦慮 | 已註銷 |
| 糖尿病 | 磺胺丁基 | 糖尿病 | 已註銷 |
| 泌尿系統 | 優福尼爾 | 尿道炎、膀胱炎 | 已註銷 |

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Urea 的不重複許可證共 **80 張**：有效單方 16 張、有效複方 29 張、已註銷 35 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（16 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第027289號 | 允消優膚乳膏 | 乳膏劑 | 永信藥品工業股份有限公司 | 2029/07/21 | 去角質 |
| 衛署藥製字第032481號 | 優親水軟膏１５０公絲/公克（尿素） | 軟膏劑 | 美西製藥有限公司 | 2030/03/21 | 可溶解角質、使乾裂魚鱗化等表皮軟化、防止乾裂 |
| 衛署藥製字第034533號 | "衛達"潤膚舒乳膏１０％ | 乳膏劑 | 衛達化學製藥股份有限公司 | 2031/11/06 | 去角質 |
| 衛署藥製字第042451號 | 膚蓉蜜去角質凝膠１０％ | 外用凝膠劑 | 中美兄弟製藥股份有限公司 | 2028/07/21 | 去角質。 |
| 衛署藥製字第047432號 | 歐婷嫩滋乳膏40% | 乳膏劑 | 永信藥品工業股份有限公司 | 2030/07/13 | 去角質。 |
| 衛署藥製字第048177號 | "元宙" 雅細雅乳膏 | 乳膏劑 | 元宙化學製藥股份有限公司 | 2031/08/18 | 去角質。 |
| 衛署藥製字第048437號 | 優倍滋乳膏40.0% | 乳膏劑 | 中生生技製藥股份有限公司淡水廠 | 2026/12/01 | 去角質。 |
| 衛署藥製字第048700號 | “應元”質化乳膏 10% | 乳膏劑 | 應元化學製藥股份有限公司 | 2027/04/30 | 去角質。 |
| 衛署藥製字第049050號 | ”福元”優麗雅乳膏 40% | 乳膏劑 | 福元化學製藥股份有限公司 | 2027/09/26 | 去角質。 |
| 衛署藥製字第049471號 | 〝永勝〞柔雅麗乳膏 40% | 乳膏劑 | 永勝藥品工業股份有限公司 | 2028/06/06 | 去角質。 |
| 衛署藥製字第049888號 | “杏輝”杏化去角質乳膏 40% | 乳膏劑 | 杏輝藥品工業股份有限公司 | 2028/12/24 | 去角質。 |
| 衛署藥製字第050051號 | “華興”芮妮乳膏 40% | 乳膏劑 | 華興化學製藥廠股份有限公司 | 2029/03/17 | 去角質。 |
| 衛部藥製字第058228號 | 膚可優乳膏 | 乳膏劑 | 壽元化學工業股份有限公司 | 2029/03/14 | 去角質。 |
| 衛部藥製字第060928號 | 芙澤適乳膏 | 乳膏劑 | 健康化學製藥股份有限公司 | 2031/07/21 | 去角質。 |
| 衛部藥輸字第027094號 | 脲 | （粉） | 台灣默克股份有限公司 | 2027/03/20 | 利尿藥 |
| 衛部藥輸字第R00111號 | [碳-13]脲 | （粉） | 台灣默克股份有限公司 | 2031/05/13 | 幽門螺旋桿菌感染檢查 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（29 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第012764號 | 汎舒軟膏 | UREA、MAFENIDE (HOMOSULFAMINE) | 軟膏劑 | 急救、預防及減緩皮膚刀傷、刮傷、燙傷之感染。 |
| 衛署藥製字第013105號 | 優皮爽水溶性軟膏 | HYDROCORTISONE ACETATE、UREA | 軟膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |
| 衛署藥製字第014096號 | 優汝膚水溶性乳膏 | UREA、HYDROCORTISONE ACETATE | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |
| 衛署藥製字第019614號 | "杏輝" 杏化潤柔滋霜 | UREA、HYDROCORTISONE ACETATE | 霜劑 | 暫時緩解濕疹、蚊蟲咬傷、皮膚炎、皮膚搔癢等疾患的症狀。 |
| 衛署藥製字第020892號 | "杏輝" 杏化乳膏 | UREA、UREA | 乳膏劑 | 去角質 |
| 衛署藥製字第023018號 | "恆安"陶美乳膏 | HYDROCORTISONE ACETATE、UREA | 乳膏劑 | 濕疹或皮膚炎及去角質。 |
| 衛署藥製字第025573號 | "嘉林"潤膚乳膏 | HYDROCORTISONE ACETATE、UREA | 乳膏劑 | 濕疹或皮膚炎 |
| 衛署藥製字第027386號 | 富貴爽乳膏 | UREA、HYDROCORTISONE ACETATE | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。(Urea作用:可暫時緩解皮膚刺激或角質軟化) |
| 衛署藥製字第027699號 | 麗膚容乳膏 | UREA、HYDROCORTISONE | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |
| 衛署藥製字第029173號 | 手福乳膏 | HYDROCORTISONE ACETATE、UREA | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀 |
| 衛署藥製字第033377號 | 優膚松乳膏 | HYDROCORTISONE、UREA | 乳膏劑 | 濕疹或皮膚炎、去角質。 |
| 衛署藥製字第033967號 | "明德" 欣保潤乳膏 | UREA、UREA、HYDROCORTISONE、HYDROCORTISONE | 乳膏劑 | 暫時緩解尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |
| 衛署藥製字第036582號 | 富麗康乳膏 | UREA、HYDROCORTISONE ACETATE | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患症狀。 |
| 衛署藥製字第041315號 | "壽元"膚優乳膏１００毫克（脲） | UREA、UREA、UREA | 乳膏劑 | 去角質。 |
| 衛署藥製字第041801號 | "生達" 優樂乳膏 | UREA、HYDROCORTISONE ACETATE | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |
| 衛署藥製字第041984號 | 優利爽乳膏 | HYDROCORTISONE ACETATE、UREA | 乳膏劑 | 溼疹、皮膚炎、去角質。 |
| 衛署藥製字第042245號 | "中美"呼呼止癢消炎液 | DIBUCAINE、DIBUCAINE、DIBUCAINE、FLUOCINOLONE ACETONIDE、FLUOCIN… | 外用液劑 | 濕疹或皮膚炎，昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢，暫時緩解皮膚搔癢，去角質。 |
| 衛署藥製字第042392號 | 允消手悅乳膏 | UREA、DIPHENHYDRAMINE HCL | 乳膏劑 | 暫時緩解尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |
| 衛署藥製字第042504號 | 潤膚乳膏〝井田〞 | UREA、HYDROCORTISONE ACETATE | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀 |
| 衛署藥製字第042696號 | 百膚安乳膏 | SALICYLIC ACID、FLUOCINOLONE ACETONIDE、CLOTRIMAZOLE、UREA | 乳膏劑 | 治療皮膚表淺性黴菌感染，如：足癬（香港腳）、股癬、汗斑，及濕疹或皮膚炎、去角質。 |
| 衛署藥製字第042761號 | "天仙"雅可隆乳膏 | SALICYLIC ACID、CLOTRIMAZOLE、BETAMETHASONE VALERATE、UREA | 乳膏劑 | 治療皮膚表淺黴菌感染、如：足癬（香港腳）、股癬、汗斑、濕疹或皮膚炎、去角質層。 |
| 衛署藥製字第042809號 | 保膚癬乳膏 | UREA、CLOTRIMAZOLE | 乳膏劑 | 治療皮膚表淺性黴菌感染，如：足癬（香港腳）、體癬、股癬、汗斑。 |
| 衛署藥製字第043332號 | "天仙"蚊蚤蟲傷乳膏 | FLUOCINOLONE ACETONIDE、FLUOCINOLONE ACETONIDE、FLUOCINOLONE A… | 乳膏劑 | 濕疹、皮膚炎、去角質、昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢。 |
| 衛署藥製字第043936號 | 勇膚乳膏 | DIBUCAINE、DIPHENHYDRAMINE HCL、FLUOCINOLONE ACETONIDE、UREA | 乳膏劑 | 暫時緩解昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢、濕疹、去角質。 |
| 衛署藥製字第044077號 | 玉麗乳膏〝溫士頓〞 | HYDROCORTISONE ACETATE、UREA | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |
| 衛署藥製字第044377號 | 〝救人〞去癢乳膏 | BETAMETHASONE VALERATE、DIPHENHYDRAMINE HCL、DIBUCAINE、UREA | 乳膏劑 | 暫時緩解皮膚搔癢、濕疹、皮膚炎、昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢、去角質。 |
| 衛署藥製字第046752號 | 雪美乳膏 | UREA、HYDROCORTISONE ACETATE | 乳膏劑 | 溼疹或皮膚炎、去角質。 |
| 衛署藥製字第048449號 | 膚史固乳膏 | HYDROCORTISONE ACETATE、UREA | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀 |
| 衛部藥製字第059264號 | 柔緹淨乳膏 | HYDROCORTISONE ACETATE、UREA | 乳膏劑 | 暫時緩解濕疹、尿布疹、蚊蟲咬傷、皮膚搔癢、皮膚炎等皮膚疾患的症狀。 |

<details><summary><strong>已註銷</strong>（35 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛成製字第000494號</td><td>阿克利諾兒錠０．１克</td><td>UREA、ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)</td><td>1988/12/31</td></tr><tr><td>內衛成製字第003807號</td><td>阿克利諾兒錠（外用）”人生”　　　　　　　　　　　　　　　　 A</td><td>UREA、ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)</td><td>1989/08/17</td></tr><tr><td>內衛藥製字第007107號</td><td>麥那鈣－Ｈ注射液</td><td>UREA、CHLORPHENIRAMINE MALEATE、THIAMINE (VITAMIN B1)、CALCIUM…</td><td>1997/12/22</td></tr><tr><td>內衛藥製字第007131號</td><td>維他命Ｂ複合注射液</td><td>THIAMINE (VITAMIN B1)、UREA、TAURINE (EQ TO 2-AMINOETHANE SULF…</td><td>1991/06/05</td></tr><tr><td>內衛藥輸字第003309號</td><td>德米安軟膏</td><td>SULFISOMIDINE、SODIUM OXYMETHANE SULFONATE、UREA</td><td>2005/06/16</td></tr><tr><td>衛署菌疫輸字第000234號</td><td>肝保定康ＡＮＴＩ－ＨＡＶ　ＩＧＭ</td><td>UREA PEROXIDASE、HEPATITIS A, ANTIGEN、SERUM, HUMAN NORMAL、PHO…</td><td>2006/09/08</td></tr><tr><td>衛署菌疫輸字第000236號</td><td>肝保定康ＨＢＳＡＧ單株抗體</td><td>UREA PEROXIDASE、HEPATITIS B, ANTIBODY, SURFACE, PEROXIDASE、H…</td><td>2006/09/08</td></tr><tr><td>衛署菌疫輸字第000237號</td><td>肝保定康ＨＢＥＡＧ/ＡＮＴＩ－ＨＢＥ</td><td>HEPATITIS B, ANTIBODY, E, PEROXIDASE、SERUM, HBEAG、SERUM, HUM…</td><td>2006/09/08</td></tr><tr><td>衛署菌疫輸字第000238號</td><td>肝保定康ＡＮＴＩ－ＨＢＣ　ＩＧＭ</td><td>SERUM, ANTIBODY, HUMAN IGG、TETRAMETHYLBENZIDINE(TMB)、SERUM,…</td><td>2006/09/08</td></tr><tr><td>衛署菌疫輸字第000239號</td><td>肝保康ＡＮＴＩ－ＨＢＣ</td><td>HEPATITIS B, ANTIBODY, CORE, PEROXIDASE、UREA PEROXIDASE、SERU…</td><td>2006/09/08</td></tr><tr><td>衛署菌疫輸字第000241號</td><td>肝保定康ＨＡＶ</td><td>O-PHENYLENEDIAMINE 2HCL (OPD)、SERUM, ANTI-HAV、SERUM, ANTI-HA…</td><td>2006/08/23</td></tr><tr><td>衛署藥製字第021398號</td><td>優利爽乳膏　〝久保〞</td><td>UREA、HYDROCORTISONE ACETATE</td><td>1998/07/24</td></tr><tr><td>衛署藥製字第027553號</td><td>安寧膚乳膏</td><td>UREA</td><td>2016/09/10</td></tr><tr><td>衛署藥製字第030773號</td><td>優親水軟膏１５０公絲/公克（尿素）</td><td>UREA</td><td>1990/07/31</td></tr><tr><td>衛署藥製字第033455號</td><td>希膚麗液２０％</td><td>UREA</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第033472號</td><td>"優生"優您雅乳膏</td><td>UREA、HYDROCORTISONE ACETATE</td><td>2019/10/15</td></tr><tr><td>衛署藥製字第037655號</td><td>愛尼乳膏</td><td>HYDROCORTISONE、UREA</td><td>2015/08/18</td></tr><tr><td>衛署藥製字第048332號</td><td>蜜娜思去角質乳膏</td><td>UREA、HYDROCORTISONE ACETATE</td><td>2016/12/20</td></tr><tr><td>衛署藥製字第055053號</td><td>“大豐”優綺乳膏</td><td>UREA、HYDROCORTISONE ACETATE</td><td>2023/07/03</td></tr><tr><td>衛署藥輸字第004255號</td><td>擦而康水溶性軟膏</td><td>UREA、HYDROCORTISONE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第005249號</td><td>抹舒藥膏</td><td>UREA PEROXIDE、OXYQUINOLINE SULFATE、AMINACRINE、ALLANTOIN、PYRU…</td><td>1987/04/23</td></tr><tr><td>衛署藥輸字第006403號</td><td>勞克寧－必注射液</td><td>MEPRYLCAINE HCL、UREA、ACETYLCHOLINE CHLORIDE、CYSTINE L-</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008205號</td><td>肝保得佳診斷試劑</td><td>SERUM, HBSAG、BUFFER SOLUTION、UREA PEROXIDASE、SERUM, HUMAN NO…</td><td>1988/09/23</td></tr><tr><td>衛署藥輸字第009019號</td><td>帝拔癲液</td><td>UREA、VALPROATE SODIUM</td><td>1986/06/17</td></tr><tr><td>衛署藥輸字第009099號</td><td>愛耳液</td><td>DIPHENHYDRAMINE HCL、CHLORPHENESIN、CHLOROBUTANOL (TRICHLORISO…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009690號</td><td>益皮能軟膏</td><td>ZINC OXIDE、UREA、COD LIVER OIL、MAFENIDE (HOMOSULFAMINE)、BUTYL…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009958號</td><td>施滅炎軟膏</td><td>TRYPSIN、UREA、NEOMYCIN (SULFATE)、HYDROCORTISONE ACETATE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第011005號</td><td>尿素粉劑</td><td>UREA</td><td>1990/06/23</td></tr><tr><td>衛署藥輸字第017963號</td><td>尿素粉劑</td><td>UREA</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第022162號</td><td>膚樂斯乳劑10%</td><td>UREA</td><td>2019/03/15</td></tr><tr><td>衛署藥輸字第022163號</td><td>膚樂斯乳膏１０％</td><td>UREA</td><td>2019/03/15</td></tr><tr><td>衛署藥輸字第022213號</td><td>優麗膏乳膏</td><td>UREA</td><td>2004/05/17</td></tr><tr><td>衛署藥輸字第022758號</td><td>使你康乳膏１０％</td><td>UREA</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第023268號</td><td>金亮軟膏</td><td>HYDROCORTISONE ACETATE、ZINC OXIDE、UREA、LIDOCAINE</td><td>2010/08/24</td></tr><tr><td>衛署藥輸字第024814號</td><td>德佑黴克舒軟膏</td><td>GLYCYRRHETIC ACID (EQ TO GLYCYRRHETINIC ACID)、ECONAZOLE NITR…</td><td>2024/05/09</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**備註**：上表 4 張是 DPP-4 抑制劑，主成分不含 urea，也不是 urea 衍生物；目前有效的 urea 製劑主要是去角質用的尿素乳膏（如優親水軟膏、膚可優乳膏）。

<!-- review:begin urea-dpp4-not-urea-derivative-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「**備註**：現行有效藥品多為含有 urea 結構衍生物的 DPP-4 抑制劑，與純 urea 的藥理作用不同。」。上表 4 張 DPP-4 抑制劑主成分不含 urea，依 NLM MeSH 也不是 urea 衍生物（vildagliptin 為 pyrrolidine-carbonitrile 衍生物、sitagliptin 為 pyrazine 衍生物、linagliptin 為 purine／quinazoline 衍生物）。TFDA 資料集中目前有效的 urea 製劑是去角質用尿素乳膏，如 衛署藥製字第032481號 優親水軟膏、衛部藥製字第058228號 膚可優乳膏。依據：[NLM MeSH：Vildagliptin（D000077597）](https://meshb.nlm.nih.gov/record/ui?ui=D000077597)；[NLM MeSH：Sitagliptin Phosphate（D000068900）](https://meshb.nlm.nih.gov/record/ui?ui=D000068900)；[NLM MeSH：Linagliptin（D000069476）](https://meshb.nlm.nih.gov/record/ui?ui=D000069476)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end urea-dpp4-not-urea-derivative-2026-10-03 -->

---

## 安全性資訊

### 藥物交互作用 (DDI)

**重大交互作用 (Major)：1 項**
- Dinoprostone (topical) - 前列腺素類，局部使用

**中度交互作用 (Moderate)：50+ 項**

主要類別包括：
- **滲透性/刺激性瀉劑**：Bisacodyl、Picosulfuric acid、Lactulose、Lactitol
- **SGLT2 抑制劑**：Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin
- **顯影劑**：Iothalamic acid、Iopromide、Iopamidol、Iohexol、Ioversol、Iodixanol
- **SNRI/SSRI 類**：Citalopram、Escitalopram、Fluoxetine、Sertraline、Duloxetine、Venlafaxine
- **其他**：Desmopressin、Lithium carbonate、Vasopressin

**輕度交互作用 (Minor)：2 項**
- Lithium carbonate
- Garlic

### 使用注意事項

1. **電解質失衡**：滲透性利尿作用可能導致脫水和電解質紊亂
2. **腎功能不全**：應謹慎使用，可能加重腎負擔
3. **顯影劑使用**：與碘顯影劑併用需注意腎毒性風險
4. **抗利尿激素相關藥物**：可能拮抗 Desmopressin、Vasopressin 的作用

---

## 結論

### 整體評估

Urea 作為一種結構簡單的天然代謝物，在 TxGNN 知識圖譜預測系統中未顯示出老藥新用的潛力。這可能反映：

1. 藥物作用機轉過於單純
2. 缺乏與新疾病適應症的網路連結
3. 主要為外用製劑，系統性藥理效應有限

### 建議

1. **維持現有適應症使用** - 外用角質溶解、保濕劑用途
2. **不建議進行老藥新用探索** - 缺乏預測基礎
3. **注意藥物交互作用** - 特別是與利尿劑、SGLT2 抑制劑併用時

### 證據等級

| 類別 | 評級 |
|------|------|
| 預測可信度 | 不適用 (無預測) |
| 臨床證據 | 不適用 |
| 安全性顧慮 | 低至中等 (主要為外用) |
| 老藥新用潛力 | 極低 |

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 知識圖譜、PubMed、ClinicalTrials.gov、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 備註「現行有效藥品多為含有 urea 結構衍生物的 DPP-4 抑制劑」 | 更正 | [NLM MeSH：Vildagliptin（D000077597）](https://meshb.nlm.nih.gov/record/ui?ui=D000077597)；[NLM MeSH：Sitagliptin Phosphate（D000068900）](https://meshb.nlm.nih.gov/record/ui?ui=D000068900)；[NLM MeSH：Linagliptin（D000069476）](https://meshb.nlm.nih.gov/record/ui?ui=D000069476)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「多為已註銷；少數含 urea 衍生物藥品有效」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

