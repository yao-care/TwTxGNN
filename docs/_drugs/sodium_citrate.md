---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 9
---

# Sodium Citrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Sodium citrate：從輸血抗凝血到乳突性結膜炎

## 一句話總結

Sodium citrate（檸檬酸鈉）原本用於輸血抗凝血、血液貯藏與 CRRT 局部抗凝，另有止咳、祛痰等傳統用途。
TxGNN 模型預測它可能對**乳突性結膜炎 (Papillary Conjunctivitis)** 有效，但目前**沒有臨床試驗與文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 輸血用抗凝結劑 |
| 預測新適應症 | 乳突性結膜炎 (Papillary Conjunctivitis) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 82 張（有效單方 2／有效複方 19／已註銷 61） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，檸檬酸鈉是一種緩衝劑與鈣離子螯合劑，在抗凝血上的用途已獲證實。

乳突性結膜炎通常由長期機械性刺激（例如隱形眼鏡）或過敏引起。檸檬酸鈉的緩衝與鈣螯合作用，和這類眼表發炎之間沒有明確的機轉路徑，這個預測目前只建立在 TxGNN 模型分數上。

排名較前的其他預測（鼻腔疾病、急性喉咽炎）與其標示的祛痰、止咳用途略有關聯，但同樣缺乏直接證據。排名第 4 的「胃部疾病」有較多資料：檸檬酸鈉可中和胃酸，細胞實驗與動物實驗也顯示它搭配 3-溴丙酮酸（3-bromopyruvate）能抑制胃癌細胞糖解並誘導凋亡，不過這些都是間接的前臨床證據，且未針對該疾病在人體測試。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sodium Citrate 的不重複許可證共 **82 張**：有效單方 2 張、有效複方 19 張、已註銷 61 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第002962號 | 輸血用枸櫞酸鈉針 | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 輸血用抗凝結劑 |
| 衛署藥製字第039569號 | "信東" 抗凝血劑枸櫞酸鈉溶液４％ | 注射劑 | 信東生技股份有限公司 | 2030/11/27 | 用於血液之貯藏或輸血時之抗凝血劑 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（19 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第002131號 | 抗血液凝固枸櫞酸鹽葡萄糖液Ｃ | CITRIC ACID、DEXTROSE、SODIUM CITRATE (SODIUM CITRATE TRIBASIC… | 注射劑 | 血液保存 |
| 內衛藥製字第005205號 | 咳停露糖漿 | SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、POTASSIUM GUAIACOLS… | 糖漿劑 | 緩解感冒之各種症狀（流鼻水、鼻塞、打噴嚏、喀痰）。 |
| 內衛藥製字第006711號 | 抗血液凝固枸櫞酸鹽葡萄糖液－甲 | CITRIC ACID、DEXTROSE、SODIUM CITRATE (SODIUM CITRATE TRIBASIC… | 注射劑 | 血液保存劑 |
| 內衛藥製字第007931號 | 哈泰利咳露 | CHLORPHENIRAMINE MALEATE、SODIUM CITRATE (SODIUM CITRATE TRIB… | 糖漿劑 | 感冒諸症狀（流鼻水、鼻塞、打噴嚏、咳嗽、喀痰） |
| 內衛藥製字第016237號 | 咳雅液 | SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、CHLORPHENIRAMINE MA… | 內服液劑 | 鎮咳、袪痰（由支氣管炎、咽候頭炎所引起之咳嗽及喀痰） |
| 衛署藥製字第004759號 | "晟德" 應嗽安糖漿 | GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、PHENYLEPHRIN… | 糖漿劑 | 緩解感冒之各種症狀（鼻塞，流鼻水，打噴嚏，喀痰） |
| 衛署藥製字第004806號 | 和咳林液 | GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、PHENYLEPHRIN… | 內服液劑 | 緩解感冒之各種症狀（流鼻水、鼻塞、打噴嚏、咳嗽、喀痰） |
| 衛署藥製字第011842號 | "美"感能咳全液 | PHENYLEPHRINE HCL、GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACO… | 內服液劑 | 鎮咳、袪痰（咽喉炎、支氣管炎、一般咳嗽感冒引起之咳嗽及喀痰） |
| 衛署藥製字第029076號 | "南光"康富力顆粒 | POTASSIUM CITRATE、SODIUM CHLORIDE、DEXTROSE、SODIUM CITRATE (S… | 內服顆粒劑 | 嘔吐、下痢及其他因體液異常喪失所引起之脫水現象 |
| 衛署藥製字第031768號 | 鎮嗽風液 | CHLORPHENIRAMINE MALEATE、SODIUM CITRATE (SODIUM CITRATE TRIB… | 內服液劑 | 袪痰、緩解咳嗽。 |
| 衛署藥製字第036049號 | 保兒力維持液 | SODIUM CITRATE (DEHYDRATE)、DEXTROSE MONOHYDRATE、POTASSIUM CI… | 內服液劑 | 輕微至中度腹瀉或其他脫水症狀所導致體內水份及物質損失時之補充液。 |
| 衛署藥製字第036229號 | 博視灌洗液 | MAGNESIUM CHLORIDE HEXAHYDRATE (EQ TO MAGNESIUM CHLORIDE 6H2… | 體腔用液劑 | 眼睛、耳朵、鼻子或喉嚨作各種手術過程中之灌洗用。 |
| 衛署藥製字第036755號 | 滋爾健顆粒 | GLUCOSE、SODIUM CITRATE (DIHYDRATE)、SODIUM CHLORIDE、POTASSIUM… | 內服顆粒劑 | 用以治療伴有腹瀉或流汗過度的體液及電解質缺乏。主要適用於早期、輕度及中度脫水。 |
| 衛署藥製字第042265號 | 力視美液 | CALCIUM CHLORIDE DIHYDRATE、POTASSIUM CHLORIDE、MAGNESIUM CHLO… | 體腔用液劑 | 眼睛、耳朵、鼻子或喉嚨作各種手術過程中灌洗用。 |
| 衛署藥製字第044855號 | "歐美嘉" 抗凝血複方檸檬酸鈉溶液A | DEXTROSE MONOHYDRATE、SODIUM CITRATE DIHYDRATE、CITRIC ACID MO… | 注射劑 | 血液抗凝劑。 |
| 衛署藥製字第055410號 | 悅喜滴抗凝血溶液 A | DEXTROSE ANHYDRATE、CITRIC ACID MONOHYDRATE、SODIUM CITRATE DI… | 注射劑 | 血液抗凝劑。 |
| 衛署藥輸字第022849號 | "愛爾康" 均衡鹽溶液 | SODIUM CITRATE (DIHYDRATE)、CALCIUM CHLORIDE (DIHYDRATE)、MAGN… | 眼耳鼻喉用灌洗劑 | 眼睛、耳朵、鼻子或喉嚨作各種外科手術過程中灌注之用。 |
| 衛署藥輸字第025179號 | 必富力得注射液 | L-THREONINE、L-PHENYLALANINE、Sodium L-Lactate Solution、Magnes… | 注射劑 | 經口攝取不足、輕度的低蛋白血症、輕度的營養障礙、手術前後等狀態時的氨基酸、電解質、維生素B1及水分之營養補給。 |
| 衛部藥輸字第027649號 | "萬益特"局部抗凝檸檬酸血液過濾用溶液 | SODIUM CHLORIDE、SODIUM CITRATE | 透析用液劑 | 採用局部檸檬酸鹽抗凝法(regional citrate anticoagulation)來進行連續性腎功能替代治療 (CRRT) 時，可使用 Regiocit 溶液做為過濾器前的… |

<details><summary><strong>已註銷</strong>（61 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000040號</td><td>中華藥典第二版檸檬酸鈉</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>1988/12/03</td></tr><tr><td>內衛藥製字第003076號</td><td>抗血液凝固枸櫞酸鹽葡萄糖液－Ｂ</td><td>DEXTROSE (MONOHYDRATE)、CITRIC ACID (ANHYDROUS)、SODIUM CITRAT…</td><td>2016/09/19</td></tr><tr><td>內衛藥製字第005370號</td><td>合利他命－ＦＢ１２注射液</td><td>HYDROXOCOBALAMIN ACETATE、INOSITOL (MESO-INOSITOL)、SODIUM CIT…</td><td>2010/02/08</td></tr><tr><td>內衛藥製字第007506號</td><td>舒咳露糖漿</td><td>AMMONIUM CHLORIDE、IPECAC EXTRACT、SODIUM CITRATE (SODIUM CITR…</td><td>1990/11/26</td></tr><tr><td>內衛藥製字第012095號</td><td>可安咳糖漿</td><td>AMMONIUM CHLORIDE、DIPHENHYDRAMINE HCL、EPHEDRINE HCL (EQ TO E…</td><td>1990/09/10</td></tr><tr><td>內衛藥製字第013172號</td><td>咳利膠囊</td><td>CAFFEINE、GLYCYRRHIZA EXTRACT、DL-METHYLEPHEDRINE HCL、POTASSIU…</td><td>1990/09/10</td></tr><tr><td>內衛藥製字第016932號</td><td>輸血用檸檬酸鈉注射液</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>2009/12/30</td></tr><tr><td>內衛藥輸字第000495號</td><td>枸櫞酸鈉</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>1985/06/24</td></tr><tr><td>內衛藥輸字第004125號</td><td>美得朗片</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、METHIONINE DL-、BISP…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第006892號</td><td>檸檬酸鈉</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>1987/07/15</td></tr><tr><td>衛署菌疫輸字第000260號</td><td>寶威抗人類Ｔ淋巴細胞病毒分析試劑</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、TETRAMETHYLBENZIDIN…</td><td>2000/08/14</td></tr><tr><td>衛署藥製字第001120號</td><td>理嗽寧糖漿</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、PHENYLEPHRIN…</td><td>2005/12/13</td></tr><tr><td>衛署藥製字第001999號</td><td>咳敏糖漿</td><td>CHLORPHENIRAMINE MALEATE、SODIUM CITRATE (SODIUM CITRATE TRIB…</td><td>2023/07/24</td></tr><tr><td>衛署藥製字第003548號</td><td>咳樂寧糖漿</td><td>CHLORPHENIRAMINE MALEATE、SODIUM CITRATE (SODIUM CITRATE TRIB…</td><td>1988/08/10</td></tr><tr><td>衛署藥製字第003822號</td><td>咳嗽糖漿”政行”　　　　　　　　　　　　　　　　　　　　　　 K</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、CHLORPHENIRAMINE MA…</td><td>1988/11/24</td></tr><tr><td>衛署藥製字第004027號</td><td>抑咳爽糖漿</td><td>PHENYLEPHRINE HCL、GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACO…</td><td>1992/12/10</td></tr><tr><td>衛署藥製字第005567號</td><td>滴爽眼耳滴液</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、DEXAMETHASONE PHOSP…</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第006001號</td><td>能寧嗽液</td><td>CHLORPHENIRAMINE MALEATE、SODIUM CITRATE (SODIUM CITRATE TRIB…</td><td>2013/10/17</td></tr><tr><td>衛署藥製字第007273號</td><td>咳喻液</td><td>AMMONIUM CHLORIDE、DIPHENHYDRAMINE HCL、SODIUM CITRATE (SODIUM…</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第007967號</td><td>嗽功糖漿</td><td>CHLORPHENIRAMINE MALEATE、SODIUM CITRATE (SODIUM CITRATE TRIB…</td><td>2023/08/02</td></tr><tr><td>衛署藥製字第008579號</td><td>克嗽能糖漿</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、PHENYLEPHRIN…</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第008596號</td><td>適安寧糖漿</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、CHLORPHENIRAMINE MA…</td><td>1999/03/30</td></tr><tr><td>衛署藥製字第010226號</td><td>咳嗽液</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、PHENYLEPHRIN…</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第013579號</td><td>檸檬酸鈉葡萄糖抗凝劑</td><td>SODIUM CITRATE (DIHYDRATE)、CITRIC ACID、DEXTROSE (MONOHYDRATE…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第013918號</td><td>金克嗽糖漿</td><td>GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACOLATE)、PHENYLEPHRIN…</td><td>1989/11/14</td></tr><tr><td>衛署藥製字第025068號</td><td>愉寧糖漿</td><td>PHENYLEPHRINE HCL、GUAIACOL GLYCOLATE (EQ TO GLYCERYL GUAIACO…</td><td>2016/09/07</td></tr><tr><td>衛署藥製字第034616號</td><td>比舒液</td><td>CALCIUM CHLORIDE (DIHYDRATE)、MAGNESIUM CHLORIDE (HEXAHYDRATE…</td><td>1998/05/12</td></tr><tr><td>衛署藥製字第039413號</td><td>益力體液補充液〝永豐〞</td><td>SODIUM CHLORIDE、POTASSIUM CITRATE MONOHYDRATE、DEXTROSE ANHYD…</td><td>2015/10/19</td></tr><tr><td>衛署藥製字第041878號</td><td>百適液</td><td>SODIUM CHLORIDE、SODIUM CITRATE (DIHYDRATE)、SODIUM ACETATE (T…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第043742號</td><td>補體鹽顆粒〝優良〞</td><td>POTASSIUM CHLORIDE、SODIUM CITRATE DIHYDRATE、SODIUM CHLORIDE、…</td><td>2010/05/06</td></tr><tr><td>衛署藥輸字第000341號</td><td>檸檬酸鈉</td><td>SODIUM CITRATE DIHYDRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003698號</td><td>保體安民注射液</td><td>L-PROLINE、HISTIDINE L- HCL (EQ TO L-HISTIDINE HYDROCHLORIDE)…</td><td>1988/04/02</td></tr><tr><td>衛署藥輸字第004655號</td><td>活力生糖衣錠</td><td>THIAMINE MONONITRATE、NIACINAMIDE (NICOTINAMIDE)、ASCORBIC ACI…</td><td>1987/03/27</td></tr><tr><td>衛署藥輸字第004707號</td><td>活力生滴劑</td><td>IRON (SODIUM CITRATE)、RIBOFLAVIN (VIT B2)、NIACINAMIDE (NICOT…</td><td>1987/03/27</td></tr><tr><td>衛署藥輸字第006710號</td><td>檸檬酸鈉粉末</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第006968號</td><td>檸檬酸鈉</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>2006/09/25</td></tr><tr><td>衛署藥輸字第007250號</td><td>維克得凍晶注射劑</td><td>POTASSIUM CITRATE ANHYDROUS、PYRIDOXINE HCL、RIBOFLAVIN PHOSPH…</td><td>1987/09/07</td></tr><tr><td>衛署藥輸字第007346號</td><td>維克得栓劑</td><td>COCARBOXYLASE (TETRAHYDRATE)、POTASSIUM CITRATE (MONOHYDRATE)…</td><td>1987/10/02</td></tr><tr><td>衛署藥輸字第008825號</td><td>眼清眠藥水</td><td>PHENYLEPHRINE HCL、SODIUM METABISULFITE (SOD. PYROSULFITE)、BE…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第010888號</td><td>小兒培得賴液</td><td>MAGNESIUM CHLORIDE ANHYDROUS、SODIUM CHLORIDE、SODIUM CITRATE…</td><td>1987/02/04</td></tr><tr><td>衛署藥輸字第011102號</td><td>依他維糖衣錠</td><td>IRON (SODIUM CITRATE)、FERROUS (SULFATE)、RIBOFLAVIN (VIT B2)、…</td><td>1993/01/08</td></tr><tr><td>衛署藥輸字第011625號</td><td>均衡鹽溶液０．６４％</td><td>SODIUM CHLORIDE、SODIUM ACETATE、POTASSIUM CHLORIDE、CALCIUM CH…</td><td>1987/07/23</td></tr><tr><td>衛署藥輸字第011873號</td><td>均衡鹽溶液</td><td>POTASSIUM CHLORIDE、SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、…</td><td>1990/10/05</td></tr><tr><td>衛署藥輸字第011940號</td><td>開明眼藥水０．５％　〝愛舒特〞</td><td>BENZALKONIUM CHLORIDE、WATER DISTILLED (EQ TO DISTILLED WATER…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第012751號</td><td>檸檬酸鈉粒</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第013502號</td><td>枸櫞酸鈉粉劑</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015352號</td><td>均衡鹽溶液〝愛爾康〞</td><td>SODIUM CHLORIDE、WATER FOR INJECTION、POTASSIUM CHLORIDE、MAGNE…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第015367號</td><td>小兒培得賴維持液</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、POTASSIUM CITRATE M…</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第015976號</td><td>維克得栓劑</td><td>POTASSIUM CITRATE (MONOHYDRATE)、PYRIDOXINE HCL、RIBOFLAVIN PH…</td><td>2001/08/02</td></tr><tr><td>衛署藥輸字第015980號</td><td>維克得凍晶注射劑</td><td>SODIUM CITRATE ANHYDROUS、EACH SOLVENT CONTAINS、PYRIDOXINE HC…</td><td>1994/06/27</td></tr><tr><td>衛署藥輸字第016047號</td><td>速補質粉劑</td><td>POTASSIUM CHLORIDE、GLUCOSE ANHYDROUS、SODIUM CITRATE DIHYDRAT…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第016337號</td><td>保體安民注射液</td><td>L-ASPARTIC ACID、L-THREONINE、GLUTAMIC ACID L-、L-SERINE、L-VALI…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016359號</td><td>愛舒特開明眼藥水４％　〝愛爾康比利時廠〞</td><td>BORIC ACID、PILOCARPINE HCL、SODIUM CITRATE (SODIUM CITRATE TR…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第018948號</td><td>均衡鹽溶液</td><td>SODIUM ACETATE (TRIHYDRATE)、MAGNESIUM CHLORIDE (HEXAHYDRATE)…</td><td>1999/06/24</td></tr><tr><td>衛署藥輸字第019189號</td><td>〝愛爾康比利時廠〞愛爾康均衡鹽溶液</td><td>POTASSIUM CHLORIDE、SODIUM CHLORIDE、MAGNESIUM CHLORIDE HEXAHY…</td><td>2023/06/05</td></tr><tr><td>衛署藥輸字第019837號</td><td>樂免敏點眼液　〝愛爾康〞</td><td>SODIUM CITRATE (SODIUM CITRATE TRIBASIC)、TYLOXAPOL (SUPERINO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第022679號</td><td>抗血液凝固枸櫞酸鹽葡萄糖液－Ａ〝百特〞</td><td>CITRIC ACID ANHYDROUS、SODIUM CITRATE DIHYDRATE、DEXTROSE MONO…</td><td>2010/07/05</td></tr><tr><td>衛署藥輸字第025708號</td><td>新派瑞恩12%糖注射液</td><td>RIBOFLAVIN PHOSPHATE SODIUM、L-HISTIDINE、PANTHENOL、FOLIC ACID…</td><td>2021/03/30</td></tr><tr><td>衛署藥輸字第025902號</td><td>新派瑞恩17.5%糖注射液</td><td>ASCORBIC ACID、L-LYSINE ACETATE、TOCOPHEROL ACETATE、L-ASPARTIC…</td><td>2021/03/24</td></tr><tr><td>衛署藥輸字第R00009號</td><td>鎵－６７檸檬酸鎵注射液</td><td>SODIUM CITRATE DIHYDRATE、BENZYL ALCOHOL、GALLIUM GA-67、SODIUM…</td><td>2014/05/07</td></tr><tr><td>衛署藥輸字第R00080號</td><td>澳鎵 Ga-67 檸檬酸鹽注射劑</td><td>GALLIUM GA-67、SODIUM CITRATE (SODIUM CITRATE TRIBASIC)</td><td>2019/03/13</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共收錄 114 筆交互作用。主要包括：
  - **重度**：氫氧化鋁（Aluminum hydroxide）
  - **中度**：Doxycycline、Minocycline、Tetracycline、Levofloxacin、乙醯水楊酸（Aspirin）、鐵劑、Ephedrine、Pseudoephedrine、Rosuvastatin、Acalabrutinib
  - **輕度**：數種磺醯脲類降血糖藥（如 Glipizide、Glyburide）、Lactulose、Misoprostol 等
- **知識圖譜提示的潛在禁忌疾病**（來自 TxGNN 知識圖譜，並非仿單內容）：高血壓、胰臟炎、腎上腺功能不全、無尿、腎功能受損、高鈣血症、代謝性酸中毒、冠狀動脈疾病、心肌梗塞、閉角型青光眼等。實際禁忌請以原廠仿單為準。

## 結論與下一步

**決策：Hold**

**理由：**
- 乳突性結膜炎的預測沒有任何臨床試驗或文獻，也找不到合理的機轉連結，證據等級僅為 L5。
- 缺乏作用機轉資料，且知識圖譜顯示多項潛在禁忌疾病，目前不適合推進。

**若要推進需要：**
- 補充詳細的作用機轉（MOA）資料，並釐清與眼表發炎的關聯
- 進行文獻與前臨床研究，確認是否有支持證據
- 確認眼用給藥途徑與劑型的可行性（目前許可證中沒有眼用劑型）
- 若要評估其他候選適應症，可優先探討「胃部疾病」的酸緩衝與糖解抑制假說，但這僅屬研究問題階段（L4）

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄；頁首證據等級依本頁「快速總覽」的證據等級列重算，模型預測、總覽表與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L3） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

