---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Mannitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Mannitol (甘露醇) - 藥師筆記

## 一句話總結

Mannitol 為滲透性利尿劑，TxGNN 預測其可用於多種罕見疾病如惡性高熱、週期性麻痺及腎源性尿崩症等，部分預測有文獻支持 (低血鉀週期性麻痺 L3)，其他為純預測階段 (L5)。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Mannitol (甘露醇、木密醇) |
| DrugBank ID | DB00742 |
| 台灣商品名 | 信東美立妥、滿乃通、濟生邁尼妥等 |
| 原核准適應症 | 利尿、降顱內壓、腦水腫、促進毒物排除、腎小球過濾速率測定 |
| 預測新適應症 | 腎源性抗利尿不當症候群、惡性高熱、家族性週期性麻痺、低血鉀週期性麻痺、腎源性尿崩症、King-Denborough 症候群等 |
| TxGNN 預測分數 | 0.997-0.999 |
| 證據等級 | **L3** (低血鉀週期性麻痺)、**L5** (其他 - 僅預測或文獻薄弱) |
| 臨床試驗 | 無直接相關 |
| PubMed 文獻 | 部分有 |

---

## 為什麼這個預測合理？

### 機轉推論

1. **滲透性利尿作用**：Mannitol 為滲透性利尿劑，可增加血漿滲透壓，促進水分從組織轉移至血管內，並增加腎臟水分排泄。

2. **各預測適應症分析**：

| 預測適應症 | 機轉關聯性 | 說明 |
|-----------|-----------|------|
| 腎源性抗利尿不當症候群 (NSIAD) | 低 | 此為遺傳性 V2 受體突變，Mannitol 理論上可對抗水分滯留，但非根本治療 |
| 急性肺心病 | 中 | 有文獻支持 Mannitol 可降低肺血管阻力，但非標準治療 |
| 惡性高熱 | 低-中 | 文獻提及 Mannitol 作為輔助治療使用，但 Dantrolene 為首選 |
| 家族性週期性麻痺 | 中 | 作為靜脈輸注溶劑，避免葡萄糖誘發發作 |
| 低血鉀週期性麻痺 | 中-高 | **有文獻直接支持**作為 KCl 靜脈給藥的溶劑 |
| 腎源性尿崩症 | 低 | 機轉不合理，可能加重脫水 |
| King-Denborough 症候群 | 低 | 與惡性高熱相關的罕見疾病 |

---

## 臨床試驗證據

### 與預測適應症相關的臨床試驗

**無直接針對預測適應症的臨床試驗**

但資料庫中存在多項 Mannitol 相關試驗，主要集中於：
- 顱內壓控制 (原適應症)
- 腸道通透性測試 (診斷用途)
- COVID-19 相關研究 (ACTT-2, ACTT-3, ACTT-4 試驗中作為對照組溶劑)

### 相關但非治療目的的試驗

| 試驗編號 | 用途 | 說明 |
|---------|------|------|
| NCT05502653 | 腸道通透性測試 | Lactulose/mannitol 糖吸收試驗 |
| NCT01108744 | 高張鹽水 vs Mannitol 降顱內壓 | 原適應症比較研究 (已撤回) |

---

## 文獻證據

### 低血鉀週期性麻痺 (HypoPP) - 證據等級 L3

| PMID | 標題 | 年份 | 重點發現 |
|------|------|------|---------|
| **6412669** | 低血鉀週期性麻痺的靜脈治療 | 1983 | **關鍵文獻**：研究確認使用 5% 葡萄糖稀釋 KCl 反而使症狀惡化並降低血鉀；改用 **5% Mannitol 作為溶劑**則可使血鉀上升並改善肌力 |
| 18426576 | 低血鉀週期性麻痺的實務管理 | 2008 | 回顧提及若需靜脈給藥，可使用 **mannitol 溶劑**代替葡萄糖 |
| 32585385 | 術後首發低血鉀週期性麻痺 | 2020 | 病例報告 |

**關鍵發現**：低血鉀週期性麻痺患者靜脈補充 KCl 時，**禁用葡萄糖溶液**（會誘發發作），應使用 **Mannitol 溶液**稀釋。

### 惡性高熱 - 證據等級 L5

| PMID | 標題 | 年份 | 重點發現 |
|------|------|------|---------|
| 33863282 | Dantrolene 無法取得時的惡性高熱處置 | 2021 | 提及支持性治療包括 Mannitol 利尿 |
| 1148076 | Dantrolene 控制惡性高熱症候群 | 1975 | 動物實驗中 Mannitol 與 Dantrolene 併用 |
| 15637010 | Dantrolene 對人類子宮平滑肌收縮的影響 | 1995 | Mannitol 為 Dantrolene 製劑的輔料，非治療成分 |

**評估**：Mannitol 僅作為惡性高熱的**輔助支持治療**（利尿、預防急性腎衰竭），**非主要治療**，Dantrolene 仍是首選。

### 腎源性尿崩症 - 證據等級 L5

| PMID | 標題 | 年份 | 說明 |
|------|------|------|------|
| 4723655 | 血管攝影後的氮質血症與腎源性尿崩症 | 1973 | 提及 Mannitol 但非治療脈絡 |
| 13677953 | 鋰中毒引起腎源性尿崩症 | 2003 | 病例報告使用 Mannitol 增加鋰清除 |

**評估**：Mannitol 用於增加毒物（如鋰）清除，非腎源性尿崩症本身的治療。

### 急性肺心病 - 證據等級 L5

| PMID | 標題 | 年份 | 重點發現 |
|------|------|------|---------|
| 324415 | 高張 Mannitol 用於急性呼吸窘迫症候群 | 1977 | 研究顯示 Mannitol 可降低肺血管阻力、增加心輸出量、減少生理死腔 |

**評估**：僅有單一老舊研究，非目前標準治療。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Mannitol 的不重複許可證共 **83 張**：有效單方 9 張、有效複方 1 張、已註銷 73 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（9 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第012343號 | "信東" 美立妥注射劑 | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定(診斷用) |
| 衛署藥製字第009633號 | 滿乃通注射液 | 注射劑 | 杏林新生製藥股份有限公司 | 2028/05/10 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第013354號 | "濟生"邁尼妥注射液２０％ | 注射劑 | 濟生醫藥生技股份有限公司 | 2028/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第015561號 | 邁尼妥注射液２０％　〝順華〞 | 注射劑 | 順華藥品工業股份有限公司 | 2028/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第016476號 | "台裕"甘露醇注射液（邁尼妥） | 注射劑 | 台裕化學製藥廠股份有限公司 | 2030/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第033425號 | "南光"舒而通輸注液20%(甘露醇) | 注射劑 | 南光化學製藥股份有限公司 | 2025/12/21 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定。 |
| 衛署藥製字第042601號 | 〝安星〞安露注射液２００毫克/毫升（甘露醇） | 注射劑 | 安星製藥股份有限公司 | 2028/09/30 | 利尿、降顱內壓、腦水腫，促進毒物之尿中排除、腎小球過濾速率之測定(診斷用)。 |
| 衛署藥製字第043768號 | 滿乃通　注射液　１５Ｗ／Ｖ％ | 注射劑 | 杏林新生製藥股份有限公司 | 2030/05/26 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用）。 |
| 衛署藥輸字第016930號 | "羅貴特" 甘露醇 | （粉） | 法台化學股份有限公司 | 2028/11/23 | 利尿劑 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥輸字第022202號 | 舒得寧長效凍晶注射劑30公絲 | MANNITOL、LANREOTIDE (ACETATE)、WATER FOR INJECTION | 凍晶注射劑 | 治療肢端肥大症。改善類癌瘤（CARCINOID TUMORS）的臨床症狀。不適合手術之甲促素細胞腺瘤病人之症狀治療或是手術前之預備治療。 |

<details><summary><strong>已註銷</strong>（73 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第003275號</td><td>得利通注射液</td><td>MANNITOL</td><td>1989/01/24</td></tr><tr><td>內衛藥製字第006610號</td><td>凍結輔/美達民針５公絲</td><td>COCARBOXYLASE (THIAMINE PYROPHOSPHATE)、MANNITOL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006612號</td><td>凍結輔/美達民針２０公絲</td><td>COCARBOXYLASE (THIAMINE PYROPHOSPHATE)、MANNITOL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006617號</td><td>凍結輔/美達民針１０公絲</td><td>MANNITOL、COCARBOXYLASE (THIAMINE PYROPHOSPHATE)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006619號</td><td>旅爽片</td><td>DIPHENHYDRAMINE HCL、MANNITOL、CHLORPHENIRAMINE MALEATE、DYPHYL…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007899號</td><td>木蜜醇注射液５％</td><td>D-MANNITOL、GLUCOSE、CALCIUM CHLORIDE、SODIUM CHLORIDE</td><td>2013/10/03</td></tr><tr><td>內衛藥輸字第000441號</td><td>木蜜醇注</td><td>D-MANNITOL</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第000881號</td><td>奧斯莫斯他利２０％</td><td>MANNITOL</td><td>1986/10/17</td></tr><tr><td>內衛藥輸字第002102號</td><td>木密醇</td><td>MANNITOL</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第004205號</td><td>甘露醇</td><td>MANNITOL</td><td>1985/08/02</td></tr><tr><td>內衛藥輸字第005218號</td><td>望你通針</td><td>MANNITOL</td><td>1999/10/25</td></tr><tr><td>內衛藥輸字第008242號</td><td>滿汝託注射液</td><td>D-MANNITOL</td><td>1990/12/05</td></tr><tr><td>衛署藥製字第004997號</td><td>"壽元"壽力醣注射液</td><td>D-MANNITOL</td><td>2025/04/29</td></tr><tr><td>衛署藥製字第006512號</td><td>壽力醣注射液</td><td>D-MANNITOL</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第009345號</td><td>利斯妥－利注射液</td><td>SODIUM CHLORIDE、CALCIUM CHLORIDE、DEXTRAN 70、GLUCOSE、MANNITOL</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第009745號</td><td>"永豐"邁力通注射液</td><td>MANNITOL</td><td>2023/09/19</td></tr><tr><td>衛署藥製字第009996號</td><td>利斯妥－優注射液</td><td>SODIUM CHLORIDE、GLUCOSE、CALCIUM CHLORIDE、MANNITOL</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第012532號</td><td>血清哥娜荷爾蒙注射劑</td><td>MANNITOL、GONADOTROPIN SERUM</td><td></td></tr><tr><td>衛署藥製字第015562號</td><td>邁尼妥舒注射液　〝順華〞</td><td>SORBITOL、MANNITOL</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第028498號</td><td>克酸胃寧－鎂錠</td><td>MANNITOL、ALUMINUM HYDROXIDE (ALUMINA HYDRATED)、MAGNESIUM HYD…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第031033號</td><td>福樂滿注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第031387號</td><td>甘露醇注射液２００公絲/公撮</td><td>MANNITOL</td><td>2006/04/19</td></tr><tr><td>衛署藥製字第035943號</td><td>維喜鈣錠</td><td>PANTOTHENATE CALCIUM、MANNITOL、ASCORBIC ACID (VIT C)、SODIUM A…</td><td>2013/04/08</td></tr><tr><td>衛署藥製字第041553號</td><td>維達豪錠</td><td>CYANOCOBALAMIN (VIT B12)、VITAMIN A、NICOTINAMIDE、VITAMIN A (V…</td><td>2016/09/19</td></tr><tr><td>衛署藥輸字第000638號</td><td>腦能寧－果注射液</td><td>FRUCTOSE (LAEVULOSE)、MANNITOL</td><td>1985/06/24</td></tr><tr><td>衛署藥輸字第001387號</td><td>甘露糖醇</td><td>MANNITOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第002038號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002633號</td><td>每益多１５％注射液</td><td>D-MANNITOL</td><td>1985/11/22</td></tr><tr><td>衛署藥輸字第002690號</td><td>木蜜醇</td><td>MANNITOL</td><td>1993/02/16</td></tr><tr><td>衛署藥輸字第003208號</td><td>安世木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003419號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003483號</td><td>越速明診斷用注射劑</td><td>BENZALKONIUM CHLORIDE、GIRACTIDE ACETATE、MANNITOL</td><td>1986/02/13</td></tr><tr><td>衛署藥輸字第003847號</td><td>甘露醇１０％</td><td>MANNITOL</td><td>1988/07/06</td></tr><tr><td>衛署藥輸字第003979號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第004563號</td><td>木蜜醇</td><td>MANNITOL</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第004665號</td><td>木蜜醇</td><td>MANNITOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第004802號</td><td>木蜜醇</td><td>MANNITOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第005552號</td><td>木蜜醇</td><td>D-MANNITOL</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第005753號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006028號</td><td>甘露醇</td><td>MANNITOL</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第006159號</td><td>表使得利注射液</td><td>MANNITOL</td><td>1986/04/30</td></tr><tr><td>衛署藥輸字第007303號</td><td>甘露醇２０％注射液</td><td>MANNITOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第007304號</td><td>甘露醇２５％注射液</td><td>MANNITOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第009214號</td><td>德達滿通注射液</td><td>EDETATE DISODIUM DIHYDRATE (EQ TO DISODIUM EDETATE DIHYDRATE…</td><td>1988/03/09</td></tr><tr><td>衛署藥輸字第009513號</td><td>貝樂斯發泡顆粒</td><td>MANNITOL、SORBITAN FATTY ACID ESTERS、SODIUM BICARBONATE ( EQ…</td><td>1988/03/01</td></tr><tr><td>衛署藥輸字第009936號</td><td>曼寧脫兒注射液</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第012025號</td><td>邁力多果糖注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012548號</td><td>木蜜醇</td><td>D-MANNITOL</td><td>1999/12/02</td></tr><tr><td>衛署藥輸字第012778號</td><td>木蜜醇</td><td>MANNITOL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第013768號</td><td>甘露醇粉劑</td><td>MANNITOL</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第014379號</td><td>每益多１５％注射液</td><td>D-MANNITOL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第014508號</td><td>速必瑞１０公絲咀嚼錠</td><td>MANNITOL MIXTURE 25% ISND</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014841號</td><td>安痛速注射液</td><td>COCARBOXYLASE (THIAMINE PYROPHOSPHATE)、PYRIDOXINE HCL、CYANOC…</td><td>1997/01/09</td></tr><tr><td>衛署藥輸字第014868號</td><td>敏立舒注射液</td><td>NITROGLYCERIN、D-MANNITOL</td><td>1992/03/12</td></tr><tr><td>衛署藥輸字第014880號</td><td>莫拿克錠</td><td>ALLOPURINOL、D-MANNITOL</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第016289號</td><td>貝樂斯發泡顆粒</td><td>MANNITOL、SORBITAN FATTY ACID ESTERS、SODIUM BICARBONATE ( EQ…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第016302號</td><td>德達滿通注射液</td><td>EDETATE DISODIUM DIHYDRATE (EQ TO DISODIUM EDETATE DIHYDRATE…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016432號</td><td>邁力多果糖注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>1993/07/29</td></tr><tr><td>衛署藥輸字第016697號</td><td>甘露醇１０％</td><td>MANNITOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016905號</td><td>甘露醇注射液２０％</td><td>MANNITOL</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第016923號</td><td>"辛法" 甘露醇注射液１５％</td><td>MANNITOL</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第017170號</td><td>郝士曼木蜜醇注射液２０％</td><td>MANNITOL</td><td>1994/03/24</td></tr><tr><td>衛署藥輸字第017374號</td><td>安舒明注射液</td><td>D-MANNITOL、MECOBALAMIN</td><td>1991/08/05</td></tr><tr><td>衛署藥輸字第017923號</td><td>木蜜醇</td><td>D-MANNITOL</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第019837號</td><td>樂免敏點眼液　〝愛爾康〞</td><td>MANNITOL、LODOXAMIDE TROMETHAMINE、CITRIC ACID MONOHYDRATE、TYL…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第019862號</td><td>邁力多果糖注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第020322號</td><td>木蜜醇注射液２０％</td><td>MANNITOL</td><td>2014/04/28</td></tr><tr><td>衛署藥輸字第021130號</td><td>速挺欣注射劑１００國際單位</td><td>MANNITOL、SALCATONIN</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第023308號</td><td>達菲林長效注射劑３．７５毫克</td><td>TRIPTORELIN ACETATE、WATER FOR INJECTION、MANNITOL</td><td>2014/10/13</td></tr><tr><td>衛署藥輸字第025971號</td><td>甘露醇</td><td>Pearlitol PF (Mannitol)</td><td>2024/07/17</td></tr><tr><td>衛署藥輸字第R00082號</td><td>普特幽門螺旋桿菌測試劑</td><td>C-13 UREA、CITRIC ACID ANHYDROUS、MANNITOL、ORANGE FLAVOR</td><td>2004/12/20</td></tr><tr><td>衛署藥輸字第R00083號</td><td>大塚優比特顆粒100毫克</td><td>D-MANNITOL、C-13 UREA</td><td>2016/02/23</td></tr><tr><td>衛署藥陸輸字第000401號</td><td>甘露醇</td><td>Mannitol</td><td>2017/04/14</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

### 核准適應症

1. **利尿**
2. **降顱內壓**
3. **腦水腫**
4. **促進毒物之尿中排除**
5. **腎小球過濾速率之測定（診斷用）**
6. **降低眼壓**
7. **防止溶血**

---

## 安全性考量

### 藥物交互作用 (DDI)

#### 嚴重 (Major) 交互作用

| 併用藥物 | 影響說明 |
|---------|---------|
| Amikacin | 增強耳毒性與腎毒性風險 |
| 其他氨基糖苷類抗生素 | 增強耳毒性與腎毒性風險 |

#### 中度 (Moderate) 交互作用

| 併用藥物類別 | 代表藥物 | 影響 |
|-------------|---------|------|
| 抗凝血劑 | Lamivudine | 可能影響藥物排泄 |
| beta-2 促效劑 | Salbutamol, Formoterol | 低血鉀風險 |
| ACE 抑制劑 | Captopril, Benazepril | 電解質異常風險 |
| 瀉劑 | Bisacodyl | 電解質流失加劇 |
| 抗癲癇藥 | Carbamazepine | 低血鈉風險增加 |
| SSRI | Citalopram | 低血鈉風險增加 |
| 顯影劑 | Diatrizoate, Iothalamic acid | 腎毒性風險 |
| 神經肌肉阻斷劑 | Cisatracurium | 電解質影響神經肌肉功能 |
| SGLT2 抑制劑 | Canagliflozin | 電解質異常與滲透性利尿加成 |

### 重要警語

1. **體液與電解質失衡**：
   - 可導致嚴重脫水與電解質紊亂
   - 需監測血清電解質、滲透壓、腎功能

2. **循環超負荷**：
   - 給藥初期因血漿滲透壓增加，可能導致血容量擴張
   - 心臟衰竭患者需謹慎

3. **腎功能**：
   - 可能導致急性腎損傷
   - 腎功能不全者需調整劑量或避免使用

4. **顱內出血風險**：
   - 腦外傷患者若血腦屏障破損，可能加重腦水腫

### 禁忌症

- 無尿
- 嚴重脫水
- 進行性心衰竭
- 活動性顱內出血（除手術中使用外）
- 嚴重肺水腫或充血

### 特殊族群

- **孕婦**：Category C，權衡利弊使用
- **哺乳婦女**：資料不足，謹慎使用
- **腎功能不全**：可能需避免使用或減量
- **老年人**：需密切監測體液狀態

---

## 結論與下一步

### 藥師評估

| 預測適應症 | 預測可信度 | 機轉合理性 | 證據等級 | 建議優先度 |
|-----------|-----------|-----------|---------|-----------|
| 低血鉀週期性麻痺 | 高 | 高 | **L3** | 建議追蹤 |
| 惡性高熱 | 低 | 低 (僅輔助) | L5 | 不建議 |
| 腎源性抗利尿不當症候群 | 中 | 中 | L5 | 可考慮研究 |
| 急性肺心病 | 低 | 中 | L5 | 不建議 |
| 腎源性尿崩症 | 低 | 低 | L5 | 不建議 |
| 週期性麻痺家族性 | 高 | 高 | L3 | 建議追蹤 |

### 建議

1. **低血鉀週期性麻痺** (建議追蹤)：
   - **臨床應用價值明確**：作為靜脈補充 KCl 的溶劑
   - **重要提醒**：禁用葡萄糖溶液稀釋 KCl
   - 可納入醫院處方建議或臨床指引

2. **惡性高熱** (不建議優先探索)：
   - Mannitol 僅為輔助支持治療
   - **Dantrolene 為首選治療**
   - 無需針對此適應症進行老藥新用

3. **其他預測適應症** (不建議)：
   - 腎源性尿崩症：機轉不合理，可能有害
   - 急性肺心病：證據過於老舊且不足

4. **藥師臨床提醒**：
   - 低血鉀週期性麻痺患者若需靜脈補鉀，建議使用 **Mannitol 或生理食鹽水**稀釋，**避免葡萄糖溶液**

### 證據等級說明

- **L3 (低血鉀週期性麻痺)**：有多篇文獻直接支持使用 Mannitol 作為 KCl 靜脈給藥的溶劑
- **L5 (其他適應症)**：僅有間接文獻提及或純粹預測，缺乏直接臨床證據

---

*本筆記由 TxGNN 老藥新用預測系統生成，僅供研究參考，不構成醫療建議。*

*生成日期：2026-02-11*

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

