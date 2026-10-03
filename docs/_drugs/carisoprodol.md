---
layout: default
title: Carisoprodol
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 1
---

# Carisoprodol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Carisoprodol：從肌肉鬆弛到失眠的潛在應用

## 一句話總結

Carisoprodol 是中樞性肌肉鬆弛劑，主要用於緩解肌肉痙攣和疼痛。
TxGNN 模型預測它可能對**失眠 (insomnia)** 有效，
目前有 **1 篇文獻**間接支持其鎮靜作用與睡眠的關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 焦慮緊張症、肌炎、椎間神經痛、坐骨神經痛、頸痛、風濕性關節炎、骨關節炎、肌肉僵硬、肌肉痛 |
| 預測新適應症 | 失眠 (insomnia) |
| TxGNN 預測分數 | 99.02% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 37 張（有效單方 12／有效複方 9／已註銷 16） |
| 建議決策 | Hold |

<!-- review:begin carisoprodol-moa-2026-10-03 -->

## Carisoprodol 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- 仿單寫明：carisoprodol 緩解急性肌肉骨骼疼痛的機轉**尚未明確**；動物試驗中，它造成的肌肉鬆弛與脊髓及腦部下行網狀結構的中間神經元活性改變有關。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6297cf20-830a-11dc-94c8-0002a5d5c51b)）
- Carisoprodol 是中樞作用型骨骼肌鬆弛劑，不會直接讓骨骼肌放鬆。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6297cf20-830a-11dc-94c8-0002a5d5c51b)）
- 它的代謝物 meprobamate 有抗焦慮與鎮靜作用，但這對療效與安全性的貢獻有多少，目前未知。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6297cf20-830a-11dc-94c8-0002a5d5c51b)）

**來源**：[DailyMed：SOMA（carisoprodol）美國仿單（Viatris），§12.1、§12.2](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6297cf20-830a-11dc-94c8-0002a5d5c51b)，版本日期 2025-08-29；查閱日期 2026-10-03。

---

<!-- review:end carisoprodol-moa-2026-10-03 -->

## 為什麼這個預測合理？

Carisoprodol 是一種中樞作用的肌肉鬆弛劑，其作用機轉與預測適應症的關聯：

1. **中樞神經系統抑制作用**：Carisoprodol 在體內部分代謝為 meprobamate（一種具有鎮靜作用的代謝物），可能影響睡眠
2. **GABA 受體調節**：其代謝物 meprobamate 具有類似巴比妥類藥物的 GABA-A 受體調節作用
3. **肌肉痙攣與失眠的關聯**：文獻提到夜間腿部痙攣可導致嚴重失眠，而 carisoprodol 用於緩解肌肉痙攣

然而，這一預測的臨床相關性有限，主要因為：
- 缺乏直接針對失眠適應症的臨床試驗
- 存在濫用和依賴性風險
- 有更安全有效的失眠治療選擇

## 臨床試驗證據

目前無直接針對 carisoprodol 治療失眠的臨床試驗。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Review | American Family Physician | 探討夜間腿部痙攣導致嚴重失眠的問題，提及 carisoprodol 等肌肉鬆弛劑用於緩解症狀 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Carisoprodol 的不重複許可證共 **37 張**：有效單方 12 張、有效複方 9 張、已註銷 16 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（12 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第006638號 | 筋健錠 | 錠劑 | 太田藥品股份有限公司 | 2027/06/10 | 焦慮緊張症、經常緊張、肌炎、椎間神經痛、坐骨神經痛、頸痛、風濕性關節炎、骨關節炎、肌肉僵硬、肌肉痛 |
| 衛署藥製字第029866號 | 比拉寧膠囊３５０公絲（卡利索普杜） | 膠囊劑 | 黃氏製藥股份有限公司 | 2028/05/25 | 腰背痛、四肢痛、筋硬痛、運動後肌肉痛、五十肩、腳跟痛或筋痙攣、筋硬後帶來之異常緊張之疾患 |
| 衛署藥製字第050152號 | 健佳力錠 350 毫克 | 錠劑 | 健亞生物科技股份有限公司 | 2029/05/26 | 焦慮緊張症、經常緊張、肌炎、椎間神經痛、坐骨神經痛、頸痛、風濕性關節炎、骨關節炎、肌肉僵硬、肌肉痛。 |
| 衛署藥製字第055961號 | 卡力舒錠250毫克 | 錠劑 | 健亞生物科技股份有限公司 | 2031/03/14 | 焦慮緊張症, 經常緊張, 肌炎, 椎間神經痛, 坐骨神經痛, 頸痛, 風濕性關節炎, 骨關節炎, 肌肉僵硬, 肌肉痛. |
| 衛署藥輸字第024478號 | 卡利索普若多"佛萊明" | （粉） | 仁友興業股份有限公司 | 2026/07/06 | 骨骼肌弛緩劑。 |
| 衛署藥輸字第025461號 | 卡利索普若多 | （粉） | 新雙隆生技股份有限公司 | 2031/07/18 | 骨骼肌弛緩劑。 |
| 衛署藥輸字第025611號 | 卡利索普若多 | （粉） | 新雙隆生技股份有限公司 | 2027/01/17 | 骨骼肌弛緩劑 |
| 衛部藥製字第058030號 | "元宙"肌舒達錠 | 錠劑 | 元宙化學製藥股份有限公司 | 2028/07/31 | 焦慮緊張症、經常緊張、肌炎、椎間神經痛、坐骨神經痛、頸痛、風濕性關節炎、骨關節炎、肌肉僵硬、肌肉痛。 |
| 衛部藥製字第058244號 | "元宙"緩僵痛錠 | 錠劑 | 元宙化學製藥股份有限公司 | 2029/04/02 | 焦慮緊張症、經常緊張、肌炎、椎間神經痛、坐骨神經痛、頸痛、風濕性關節炎、骨關節炎、肌肉僵硬、肌肉痛。 |
| 衛部藥製字第058303號 | 卡鬆錠250毫克 | 錠劑 | 五洲製藥股份有限公司 | 2029/06/18 | 焦慮緊張症，經常緊張，肌炎，椎間神經痛，坐骨神經痛，頸痛，風濕性關節炎，骨關節炎，肌肉僵硬，肌肉痛。 |
| 衛部藥製字第058551號 | 可舒利筋錠350毫克 | 錠劑 | 滎洋醫藥股份有限公司 | 2029/12/08 | 焦慮緊張症、經常緊張、肌炎、椎間神經痛、坐骨神經痛、頸痛、風濕性關節炎、骨關節炎、肌肉僵硬、肌肉痛。 |
| 衛部藥輸字第028545號 | 卡利索普若多 | （粉） | 新雙隆生技股份有限公司 | 2028/08/14 | 骨骼肌弛緩劑 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（9 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第029037號 | 如來舒膠囊 | CARISOPRODOL、ACETAMINOPHEN (EQ TO PARACETAMOL) | 膠囊劑 | 骨骼肌肉之異常緊張（包括外傷、扭傷、骨折、脫臼、肌炎、風溼性）所引起之各種症狀、如酸痛、痙攣、強直、僵硬 |
| 衛署藥製字第029090號 | 痛福錠 | ACETAMINOPHEN (EQ TO PARACETAMOL)、CARISOPRODOL | 錠劑 | 神經痛、關節痛、腰痛、背痛、扭傷、肌肉痛、脊椎炎、肌肉痙攣、關節周圍炎、斜頸 |
| 衛署藥製字第046682號 | "強生"肌舒錠 | ACETAMINOPHEN (EQ TO PARACETAMOL)、CARISOPRODOL | 錠劑 | 骨骼肌肉之異常緊張(包括外傷、扭傷、骨折、脫臼、肌炎、風濕性)所引起之各種症狀，如痠痛、痙攣、強直、僵硬。 |
| 衛署藥製字第047877號 | 萊世膠囊 | CARISOPRODOL、ACETAMINOPHEN (EQ TO PARACETAMOL) | 膠囊劑 | 骨骼肌肉之異常緊張(包括外傷、扭傷、骨折、脫臼、肌炎、風濕性)所引起之各種症狀，如酸痛、痙攣、強直、僵硬等。 |
| 衛署藥製字第047884號 | 妥痛膠囊 | GELATIN、GELATIN、CARISOPRODOL、ACETAMINOPHEN (EQ TO PARACETAMO… | 膠囊劑 | 骨骼肌肉異常緊張包括外傷、扭傷、骨折、脫臼、肌炎、風濕性所引起之各種症狀，如酸痛、痙攣、強直、僵硬等。 |
| 衛署藥製字第048320號 | "元宙" 肌力康錠 | ACETAMINOPHEN (EQ TO PARACETAMOL)、CARISOPRODOL | 錠劑 | 骨骼肌肉之異常緊張(包括外傷、扭傷、骨折、脫臼、肌炎、風濕性)所引起之各種症狀，如酸痛、痙攣、強直、僵硬。 |
| 衛署藥製字第057404號 | "杏輝"弛筋定錠 | CARISOPRODOL、ACETAMINOPHEN (EQ TO PARACETAMOL) | 錠劑 | 骨骼肌肉之異常緊張(包括外傷、扭傷、骨折、脫臼、肌炎、風濕性)所引起之各種症狀，如酸痛、痙攣、強直、僵硬。 |
| 衛部藥製字第058048號 | 肌倍康錠 | CARISOPRODOL、ACETAMINOPHEN (EQ TO PARACETAMOL) | 錠劑 | 骨骼肌肉之異常緊張(包括外傷、扭傷、骨折、脫臼、肌炎、風濕性)所引起之各種症狀，如酸痛、痙攣、強直、僵硬。 |
| 衛部藥製字第060185號 | "應元"舒穩錠 | CARISOPRODOL、CAFFEINE、ACETAMINOPHEN (EQ TO PARACETAMOL) | 錠劑 | 頸肩腕症候群、肩關節周圍炎、變形性脊椎症之肌肉鬆弛劑。 |

<details><summary><strong>已註銷</strong>（16 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000097號</td><td>司吾朗錠</td><td>PHENACETIN (ACETOPHENETIDIN)、CARISOPRODOL、CAFFEINE ANHYDROUS</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第012220號</td><td>"三東"福濕膠囊</td><td>CARISOPRODOL、PHENYLBUTAZONE (DI-PHENYLBUTAZONE)</td><td>2018/10/17</td></tr><tr><td>衛署藥製字第018330號</td><td>炎制錠</td><td>CARISOPRODOL、PHENYLBUTAZONE (DI-PHENYLBUTAZONE)</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第047963號</td><td>"中化合成生技" 卡利索普若多</td><td>CARISOPRODOL</td><td>2015/10/27</td></tr><tr><td>衛署藥製字第057250號</td><td>克力舒錠350毫克</td><td>CARISOPRODOL</td><td>2023/08/08</td></tr><tr><td>衛署藥輸字第000450號</td><td>卡利索普若多</td><td>CARISOPRODOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005066號</td><td>丙基氨基甲酸鹽</td><td>CARISOPRODOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006031號</td><td>Ｎ－異丙基－２－甲基－２－丙基－１，３－丙二醇二氨基甲酸酯</td><td>CARISOPRODOL</td><td>1999/12/02</td></tr><tr><td>衛署藥輸字第006827號</td><td>卡利異普魯杜</td><td>CARISOPRODOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第008440號</td><td>卡利索普魯道</td><td>CARISOPRODOL</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第011016號</td><td>科發克痛錠</td><td>CHLORTHENOXAZIN、CARISOPRODOL、PHENYLBUTAZONE (DI-PHENYLBUTAZO…</td><td>1987/08/20</td></tr><tr><td>衛署藥輸字第011891號</td><td>可立舒錠３５０公絲</td><td>CARISOPRODOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第011927號</td><td>卡利異普魯杜粉劑</td><td>CARISOPRODOL</td><td>2022/06/21</td></tr><tr><td>衛署藥輸字第012106號</td><td>佳立舒錠</td><td>CAFFEINE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CARISOPRODOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第012447號</td><td>卡利索普洛杜</td><td>CARISOPRODOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第013763號</td><td>卡力蘇波粉劑</td><td>CARISOPRODOL</td><td>1999/10/25</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

**重要警語**：
- Carisoprodol 具有濫用和依賴性風險，在部分國家已被列為管制藥品
- 代謝物 meprobamate 可能累積並導致過度鎮靜
- 不建議長期使用，通常限於 2-3 週短期治療

**藥物交互作用**：
- 與 Morphine（Major）：可能增強中樞神經系統抑制作用，導致呼吸抑制
- 與 Morphine (liposomal)（Major）：同上
- 與 Dronabinol（Moderate）：增強鎮靜作用
- 與 Nabilone（Moderate）：增強鎮靜作用
- 與 Opium（Moderate）：可能增強中樞神經系統抑制
- 與 Metoclopramide（Moderate）：可能增強鎮靜作用

**特殊族群注意事項**：
- 老年患者：因代謝物累積風險，需謹慎使用
- 肝功能不全：可能影響藥物代謝
- 具有藥物濫用史者：不建議使用

## 結論與下一步

**決策：Hold**

**理由：**
雖然 carisoprodol 的鎮靜作用可能對睡眠有一定影響，但缺乏直接的臨床試驗證據支持其用於失眠治療。此外，該藥物存在濫用風險，且有更安全有效的失眠治療選擇。

**若要推進需要：**
- 針對失眠適應症的前瞻性臨床試驗
- 安全性評估，特別是濫用和依賴性風險
- 與現有失眠治療藥物的比較研究
- 考慮其他更安全的治療選項

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：SOMA 美國仿單 §12.1](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6297cf20-830a-11dc-94c8-0002a5d5c51b) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

