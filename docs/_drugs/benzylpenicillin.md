---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 7
---

# Benzylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Benzylpenicillin：從細菌感染症到牙冠周炎

## 一句話總結

Benzylpenicillin（青黴素 G）是 β-內醯胺類抗生素，原本用於治療對青黴素敏感的細菌感染症。
TxGNN 模型預測它可能對**牙冠周炎 (Pericoronitis)** 有效，
但目前**沒有臨床試驗和文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急慢性感染症（由葡萄球菌、鏈球菌、肺炎球菌、髓膜炎菌、放線菌、紡錘狀菌等引起的化膿性疾患）、髓膜炎、亞急性細菌性心內膜炎、淋病、梅毒、手術後感染預防 |
| 預測新適應症 | 牙冠周炎 (Pericoronitis) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 僅有已註銷許可證 |
| 許可證數 | 180 張（有效單方 2／有效複方 1／已註銷 177） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Benzylpenicillin 屬於 β-內醯胺類抗生素，一般認為其作用是抑制細菌細胞壁合成，對許多革蘭氏陽性菌及厭氧菌有活性。

牙冠周炎是智齒周圍軟組織的細菌感染，常涉及口腔內的革蘭氏陽性菌與厭氧菌。從抗菌譜來看，青黴素類藥物與此類感染有合理的關聯，因此模型的預測在生物學上說得通。

不過目前沒有任何臨床試驗或文獻佐證，原藥物的作用機轉資料也缺漏，這個預測仍停留在假說階段。

**其他預測適應症（皆為 L5，僅有模型預測，建議 Hold）：**

| 排名 | 預測疾病 | TxGNN 分數 | 機轉合理性簡評 |
|------|---------|-----------|---------------|
| 2 | 牙齦萎縮 (Gingival recession) | 99.31% | 主要為機械或解剖性問題，抗菌機轉關聯很弱 |
| 3 | 口腔潰瘍 (Canker sore) | 99.27% | 多屬免疫相關，僅可能用於預防續發感染 |
| 4 | 潰瘍性口炎 (Ulcerative stomatitis) | 99.26% | 可能處理續發細菌感染，但病因多樣，關聯間接 |
| 5 | 義齒性口炎 (Denture stomatitis) | 99.26% | 以念珠菌生物膜為主，青黴素無抗黴菌活性，合理性弱 |
| 6 | 化療引起的口腔黏膜炎 (Chemotherapy-induced oral mucositis) | 99.26% | 主要為黏膜損傷與發炎，抗菌作用僅間接相關 |
| 7 | 牙齦白斑症 (Leukoplakia of gingiva) | 99.06% | 屬潛在癌前病變，非感染性，無明確機轉依據 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Benzylpenicillin 的不重複許可證共 **180 張**：有效單方 2 張、有效複方 1 張、已註銷 177 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第015845號 | "永豐"芐基青黴素鈉注射劑 | 乾粉注射劑 | 永豐製藥股份有限公司 | 2028/05/25 | 葡萄球菌、鏈球菌、肺炎雙球菌、腦膜炎球菌及其他具有感受性細菌引起之感染症 |
| 衛署藥製字第023250號 | 鉀西林注射劑２０，０００，０００單位（/基青黴素鉀） | 乾粉注射劑 | 榮民製藥股份有限公司 | 2029/04/28 | 葡萄球菌、鏈球菌、肺炎雙炎菌、腦膜炎球菌及其他具有感受性細菌引起之感染症 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第004466號 | 三青黴素注射劑 | PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL… | 乾粉注射劑 | 對青黴素敏感之細菌引起之傳染病、如淋病、肺炎球菌性傳染和溶血性鏈球菌傳染、葡萄球菌傳染 |

<details><summary><strong>已註銷</strong>（177 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第001853號</td><td>混青黴素針</td><td>PENICILLIN G POTASSIUM BUFFERED、PENICILLIN G PROCAINE (EQ TO…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第001899號</td><td>配尼黴素－Ｓ針</td><td>STREPTOMYCIN (SULFATE)、PENICILLIN G PROCAINE (EQ TO BENZYLPE…</td><td>1991/04/26</td></tr><tr><td>內衛藥製字第002284號</td><td>普魯卡因青黴素Ｇ注射劑１５０萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第003712號</td><td>康必安注射液</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、STRE…</td><td>2018/05/11</td></tr><tr><td>內衛藥製字第004008號</td><td>“永豐”芐基青黴素鉀注射劑</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL…</td><td>2023/09/12</td></tr><tr><td>內衛藥製字第004458號</td><td>博西林注四十萬單位</td><td>PENICILLIN G POTASSIUM BUFFERED、PENICILLIN G PROCAINE (EQ TO…</td><td>2018/05/11</td></tr><tr><td>內衛藥製字第005174號</td><td>青黴素錠２５萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1989/05/29</td></tr><tr><td>內衛藥製字第006616號</td><td>強西林肌內注射劑</td><td>PENICILLIN G BENZATHINE、PENICILLIN G PROCAINE (EQ TO BENZYLP…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006629號</td><td>/基青黴素鉀針二十萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006630號</td><td>/基青黴素鉀針－百萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第008044號</td><td>普魯卡因青黴素Ｇ針三十萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第008965號</td><td>/基青黴素普魯卡因滅菌粉劑３０萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第009019號</td><td>長速西林肌肉注射劑</td><td>PENICILLIN G BENZATHINE、PENICILLIN G PROCAINE (EQ TO BENZYLP…</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011374號</td><td>/基青黴素普魯卡因滅菌劑１５０萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011780號</td><td>/基青黴素鉀針２０萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011781號</td><td>/基青黴素鈉針一百萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011782號</td><td>/基青黴素鈉針４０萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第013425號</td><td>配尼西林片五萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1987/06/25</td></tr><tr><td>內衛藥製字第015984號</td><td>普魯卡因盤尼西林Ｇ注射液</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第016245號</td><td>普樂卡西林注射劑４０萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1989/11/21</td></tr><tr><td>內衛藥輸字第000099號</td><td>薩羅平</td><td>PENICILLIN G (BENZYLPENICILLIN)</td><td>1984/03/01</td></tr><tr><td>內衛藥輸字第000361號</td><td>配尼西林片５０萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第000581號</td><td>安健黴素</td><td>PENICILLIN G CLEMIZOLE、PENICILLIN G POTASSIUM (BENZYLPENICIL…</td><td>1984/12/31</td></tr><tr><td>內衛藥輸字第000776號</td><td>配尼西林粉針一千萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第000914號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1986/01/08</td></tr><tr><td>內衛藥輸字第000968號</td><td>納普西林４，０００，０００ＩＵ</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第001199號</td><td>喜保黴素注射劑１００萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL…</td><td>1989/11/21</td></tr><tr><td>內衛藥輸字第001201號</td><td>喜保黴素注射劑８００，０００Ｉ．Ｕ．</td><td>PENICILLIN G CLEMIZOLE、PENICILLIN G POTASSIUM (BENZYLPENICIL…</td><td>1989/11/21</td></tr><tr><td>內衛藥輸字第001221號</td><td>普樂西林（３，０００，０００ＩＵ）</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1984/12/31</td></tr><tr><td>內衛藥輸字第002031號</td><td>普魯卡因盤尼西林Ｇ</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第002296號</td><td>盤尼西林Ｇ鉀鹽</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第002418號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第002443號</td><td>雅克白黴素針</td><td>PENICILLIN V BENZATHINE、PENICILLIN G SODIUM ( EQ TO BENZYLPE…</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第002572號</td><td>鉍黴素針劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第002644號</td><td>亞德白黴素針</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1986/11/07</td></tr><tr><td>內衛藥輸字第003469號</td><td>青黴混合黴素（原料）</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL…</td><td>1984/12/31</td></tr><tr><td>內衛藥輸字第003473號</td><td>/基青黴素普魯卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1985/10/01</td></tr><tr><td>內衛藥輸字第003474號</td><td>青黴素普魯卡因及青黴素鉀</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1986/01/10</td></tr><tr><td>內衛藥輸字第003475號</td><td>/基青黴鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第004056號</td><td>愛文白黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第004508號</td><td>白徽素針</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第004609號</td><td>水性懸濁配尼西林針</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/08/20</td></tr><tr><td>內衛藥輸字第004872號</td><td>配尼西林油針</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/08/20</td></tr><tr><td>內衛藥輸字第004873號</td><td>配尼西林粉針</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1990/08/20</td></tr><tr><td>內衛藥輸字第005030號</td><td>白黴素針２４０萬</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第005110號</td><td>克利斯妥盼２０萬單位注射劑</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1985/09/13</td></tr><tr><td>內衛藥輸字第005111號</td><td>克利斯妥盼１００萬單位注射劑</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1985/08/09</td></tr><tr><td>內衛藥輸字第005399號</td><td>晶青素</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1985/11/01</td></tr><tr><td>內衛藥輸字第005400號</td><td>可利斯得盼</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1987/03/27</td></tr><tr><td>內衛藥輸字第005404號</td><td>可利斯得盼</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1987/03/27</td></tr><tr><td>內衛藥輸字第005507號</td><td>保那西林</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005508號</td><td>盤尼西林Ｇ</td><td>PENICILLIN G (BENZYLPENICILLIN)</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005620號</td><td>配尼西林油劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1985/11/01</td></tr><tr><td>內衛藥輸字第005750號</td><td>必治９６</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005754號</td><td>妙黴素１００萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、1-(P-CH…</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005755號</td><td>妙黴素５０萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005757號</td><td>保那西林四十萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005869號</td><td>油質配尼西林</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第005872號</td><td>懸濁水性盤尼西林</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PROC…</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第005874號</td><td>複合水性配尼西林Ｇ</td><td>PENICILLIN G POTASSIUM BUFFERED、PENICILLIN G PROCAINE (EQ TO…</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第005924號</td><td>趨普樂盼</td><td>PENICILLIN G BENETHAMINE、PENICILLIN G SODIUM ( EQ TO BENZYLP…</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第006038號</td><td>油性結晶普羅卡因盤尼西林Ｇ</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1985/08/02</td></tr><tr><td>內衛藥輸字第006040號</td><td>複合水性盤尼西林</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>2004/12/23</td></tr><tr><td>內衛藥輸字第006043號</td><td>白西林複合懸濁針</td><td>PENICILLIN G BENZATHINE、PENICILLIN G PROCAINE (EQ TO BENZYLP…</td><td>2004/12/23</td></tr><tr><td>內衛藥輸字第006126號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第006127號</td><td>普魯卡因/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL…</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第006186號</td><td>斯可樂盼</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第006250號</td><td>盤尼西林Ｇ二十萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第006533號</td><td>青黴素Ｇ鉀粉末</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1987/03/17</td></tr><tr><td>內衛藥輸字第007108號</td><td>懸濁配尼西林針</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/08/20</td></tr><tr><td>內衛藥輸字第007757號</td><td>亞德青黴素油劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第007930號</td><td>美克西林注射劑－百萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1990/11/15</td></tr><tr><td>內衛藥輸字第007943號</td><td>利得黴素注射劑Ｄ/Ｆ　１２０萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL…</td><td>1990/11/15</td></tr><tr><td>衛署藥製字第000021號</td><td>施貴寶結晶盤尼西林Ｇ鉀片２０萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1999/09/30</td></tr><tr><td>衛署藥製字第000129號</td><td>普魯卡因/基青黴素油性注射液</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第001246號</td><td>普魯卡因/基青黴素注射劑３０萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第001247號</td><td>普魯卡因/基青黴素注射劑１５０萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第001369號</td><td>/基青黴素鉀注射劑２千萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第003894號</td><td>青徽素Ｇ鉀緩衝注射劑１００萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2014/09/30</td></tr><tr><td>衛署藥製字第004467號</td><td>普魯卡因青黴素水性注射劑一百五十萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2014/09/25</td></tr><tr><td>衛署藥製字第004477號</td><td>普魯卡因青黴素水性注射劑三十萬單位</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2014/09/25</td></tr><tr><td>衛署藥製字第012308號</td><td>/基青黴素鉀注射劑５百萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第012312號</td><td>/基青黴素鉀注射劑二百萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第012376號</td><td>/基青黴素鉀注射劑１千萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第014756號</td><td>"永豐" 苄基青黴素鈉注射液用粉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>2023/09/22</td></tr><tr><td>衛署藥製字第016221號</td><td>/基青黴素鈉注射劑　〝榮民〞</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2014/09/25</td></tr><tr><td>衛署藥製字第022782號</td><td>雙西林注射劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>2014/09/25</td></tr><tr><td>衛署藥輸字第000145號</td><td>普魯卡因/基青黴素、</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第000905號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1987/04/24</td></tr><tr><td>衛署藥輸字第000992號</td><td>/基青黴素普魯卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1987/04/20</td></tr><tr><td>衛署藥輸字第001045號</td><td>赫司特西林混合物</td><td>ALUMINUM MONOSTEARATE、PENICILLIN G PROCAINE (EQ TO BENZYLPEN…</td><td>1986/06/10</td></tr><tr><td>衛署藥輸字第001055號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1986/06/10</td></tr><tr><td>衛署藥輸字第001056號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1986/06/10</td></tr><tr><td>衛署藥輸字第001586號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第001622號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第001753號</td><td>普羅卡因/基青黴素（注射用粉）</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1988/11/08</td></tr><tr><td>衛署藥輸字第002076號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1987/03/20</td></tr><tr><td>衛署藥輸字第002077號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002078號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002335號</td><td>漢洛配尼西林錠（五十萬單位）</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1986/06/12</td></tr><tr><td>衛署藥輸字第002637號</td><td>/基青黴素鉀（非注射用）</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002669號</td><td>盤黴素針</td><td>PENICILLIN G (BENZYLPENICILLIN)、PENICILLIN G CLEMIZOLE、PHYSI…</td><td>1986/04/14</td></tr><tr><td>衛署藥輸字第004001號</td><td>/青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1991/05/14</td></tr><tr><td>衛署藥輸字第004018號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1991/05/14</td></tr><tr><td>衛署藥輸字第004035號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1991/05/14</td></tr><tr><td>衛署藥輸字第004708號</td><td>普魯卡因青黴素Ｇ（水劑用）</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第004709號</td><td>普魯卡因青黴素Ｇ（佛特化）</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1986/10/28</td></tr><tr><td>衛署藥輸字第004710號</td><td>青黴素Ｇ鉀鹽</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第004711號</td><td>青黴素Ｇ鈉鹽</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第004712號</td><td>微粒子化普魯卡因青黴素Ｇ（油劑用）</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第004732號</td><td>青黴素鉀鹽</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第004897號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005317號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第005642號</td><td>必醫你舒１ＫＥ注射劑</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、STREPTO…</td><td>1993/06/17</td></tr><tr><td>衛署藥輸字第005643號</td><td>必醫你舒０．５ＫＥ注射劑</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、STREPTO…</td><td>1993/06/17</td></tr><tr><td>衛署藥輸字第005644號</td><td>必醫你舒０．２ＫＥ注射劑</td><td>STREPTOCOCCUS PYROGENE SU STRAIN TX WITH PN G POTASSIUM、PENI…</td><td>1993/06/17</td></tr><tr><td>衛署藥輸字第005654號</td><td>必醫你舒５ＫＥ注射劑</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、STREPTO…</td><td>1993/06/19</td></tr><tr><td>衛署藥輸字第005722號</td><td>苯甲基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第006570號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006586號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006958號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第006960號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第007863號</td><td>/基青黴素普魯卡因注射劑（三百萬單位）</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/03/24</td></tr><tr><td>衛署藥輸字第009372號</td><td>鉀青黴素Ｇ錠</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009968號</td><td>白黴素注射劑</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL…</td><td>1992/01/17</td></tr><tr><td>衛署藥輸字第010917號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第010918號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010937號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第012071號</td><td>能克青黴素注射劑</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>1996/08/05</td></tr><tr><td>衛署藥輸字第012872號</td><td>普利林</td><td>LIDOCAINE HCL、PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN S…</td><td>2000/06/05</td></tr><tr><td>衛署藥輸字第013195號</td><td>青黴素Ｇ注射劑１０，０００，０００國際單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1988/03/14</td></tr><tr><td>衛署藥輸字第013224號</td><td>利達平６：３：３注射劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1989/01/09</td></tr><tr><td>衛署藥輸字第013450號</td><td>喜保黴素注射劑１００萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )、PENICIL…</td><td>1992/09/25</td></tr><tr><td>衛署藥輸字第013451號</td><td>喜保黴素注射劑８００，０００Ｉ．Ｕ．</td><td>PENICILLIN G CLEMIZOLE、PENICILLIN G POTASSIUM (BENZYLPENICIL…</td><td>1992/09/25</td></tr><tr><td>衛署藥輸字第013752號</td><td>克利斯妥盼１００萬單位注射劑</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1990/03/24</td></tr><tr><td>衛署藥輸字第014070號</td><td>趨普樂盼注射劑</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)、PENICIL…</td><td>1990/03/24</td></tr><tr><td>衛署藥輸字第014129號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014130號</td><td>青黴素普魯卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014131號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014147號</td><td>斯可樂盼注射劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1990/03/24</td></tr><tr><td>衛署藥輸字第014237號</td><td>克利斯得盼注射劑６公克</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1990/03/24</td></tr><tr><td>衛署藥輸字第014238號</td><td>青黴素普魯卡因油性注射液</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/03/24</td></tr><tr><td>衛署藥輸字第014377號</td><td>青黴素普魯卡因及青黴素鉀</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014611號</td><td>強化青黴素普卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1987/03/20</td></tr><tr><td>衛署藥輸字第015033號</td><td>配尼西林錠５０萬單位</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1991/12/26</td></tr><tr><td>衛署藥輸字第015108號</td><td>/基青黴素鈉注射劑一千萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1987/04/20</td></tr><tr><td>衛署藥輸字第015109號</td><td>/基青黴素鈉注射劑一百萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1987/03/21</td></tr><tr><td>衛署藥輸字第015484號</td><td>/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第015675號</td><td>/基青黴素鈉注射劑１００萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015689號</td><td>赫司特/基青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>1998/02/21</td></tr><tr><td>衛署藥輸字第015691號</td><td>強化青黴素普卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015727號</td><td>/基青黴素鈉注射劑１０００萬單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015744號</td><td>/基青黴素普魯卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015769號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1992/07/01</td></tr><tr><td>衛署藥輸字第016131號</td><td>青黴素Ｇ注射劑１０，０００，０００國際單位</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016975號</td><td>利達平６：３：３注射劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1999/01/12</td></tr><tr><td>衛署藥輸字第017080號</td><td>/基青徽素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第017505號</td><td>趨普樂盼注射劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1990/03/15</td></tr><tr><td>衛署藥輸字第017506號</td><td>斯可樂盼注射劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1990/03/15</td></tr><tr><td>衛署藥輸字第017507號</td><td>克利斯得盼注射劑６公克</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1990/03/15</td></tr><tr><td>衛署藥輸字第017508號</td><td>克利斯妥盼１００萬單位注射劑</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>1990/03/15</td></tr><tr><td>衛署藥輸字第017509號</td><td>青黴素普魯卡因油性注射液</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/03/15</td></tr><tr><td>衛署藥輸字第017510號</td><td>/基青黴素普魯卡因注射劑（三百萬單位）</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>1990/03/15</td></tr><tr><td>衛署藥輸字第018547號</td><td>普魯卡因/基青黴素</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第018553號</td><td>/青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第018554號</td><td>/基青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第018896號</td><td>白黴素注射劑</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PENI…</td><td>1995/05/27</td></tr><tr><td>衛署藥輸字第020833號</td><td>素徽素Ｇ鉀鹽</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2005/01/12</td></tr><tr><td>衛署藥輸字第021969號</td><td>芐青黴素納</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第021979號</td><td>芐青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第021995號</td><td>青黴素普卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第022038號</td><td>/基青黴素鉀赫司特　〝赫司特〞</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2006/05/23</td></tr><tr><td>衛署藥陸輸字第000152號</td><td>芐青黴素普卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2013/12/16</td></tr><tr><td>衛署藥陸輸字第000159號</td><td>芐青黴素普卡因</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)</td><td>2016/06/01</td></tr><tr><td>衛署藥陸輸字第000169號</td><td>卞青黴素鉀</td><td>PENICILLIN G POTASSIUM (BENZYLPENICILLIN POTASSIUM )</td><td>2017/04/14</td></tr><tr><td>衛署藥陸輸字第000170號</td><td>卞青黴素鈉</td><td>PENICILLIN G SODIUM ( EQ TO BENZYLPENICILLIN SODIUM)</td><td>2017/04/14</td></tr><tr><td>衛署藥陸輸字第000221號</td><td>芐青黴素普卡因</td><td>Benzylpenicillin Procaine</td><td>2013/12/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自 TxGNN 知識圖譜，非仿單內容）：腎臟疾病、輸尿管積膿、困難梭狀桿菌結腸炎、新生兒壞死性腸炎、傳染性單核球增多症、慢性 Epstein-Barr 病毒感染症候群。
- **藥物交互作用**：共查得 21 筆，主要如下：
  - **重大 (Major)**：Methotrexate
  - **中度 (Moderate)**：Doxycycline、Minocycline、Tetracycline、Demeclocycline、Oxytetracycline（四環黴素類）、Chloramphenicol、Warfarin、Dicoumarol、Ethinylestradiol、Mycophenolic acid、Picosulfuric acid、Iodide I-123、Iodide I-131
  - **輕微 (Minor)**：Clarithromycin、Erythromycin
  - **等級未明**：Salbutamol、Acyclovir、Gentamicin、Levothyroxine

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆只有模型分數，沒有臨床試驗與文獻支持（證據等級 L5）。
- 台灣目前沒有有效的許可證（20 張皆已註銷），且作用機轉資料缺漏。

**若要推進需要：**
- 補充 Benzylpenicillin 的作用機轉資料（DrugBank）。
- 針對牙冠周炎進行文獻與臨床試驗的系統性檢索，並評估與現行口腔感染治療（如其他口服青黴素類）的比較價值。
- 確認給藥途徑的可行性：現有劑型皆為注射劑，是否適合牙冠周炎這類局部、門診型感染需評估。
- 釐清台灣的法規路徑，因為目前並無有效許可證。
- 針對腎臟疾病等族群及 Methotrexate 等交互作用藥物，制定安全性監測計畫。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表代表品項「博西林注四十萬單位」 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L5，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L3）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

