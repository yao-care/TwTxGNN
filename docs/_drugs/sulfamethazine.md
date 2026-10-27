---
layout: default
title: Sulfamethazine
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-16
description: "Sulfamethazine：預測新適應症為痛風 (Gout)（證據等級 L5）。原適應症：細菌性感染症"
monitor_inn: "Sulfamethazine"
predicted_indications: ["gout", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "conjunctivitis"]
---

# Sulfamethazine
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

## Sulfamethazine：從細菌性感染症到痛風
{: .text-alpha }

## 一句話總結

Sulfamethazine（磺胺二甲嘧啶）是磺胺類抗菌藥，原本用於葡萄球菌、鏈球菌、大腸菌等細菌感染症。
TxGNN 模型預測它可能對**痛風 (Gout)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性感染症 |
| 預測新適應症 | 痛風 (Gout) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 僅有已註銷許可證 |
| 許可證數 | 59 張（有效單方 0／有效複方 0／已過期 1／已註銷 58） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Sulfamethazine 是磺胺類抗菌藥，一般認為它抑制細菌的二氫蝶酸合成酶（dihydropteroate synthase），阻斷葉酸合成而抑制細菌生長。

這個機轉與尿酸代謝或痛風的病理生理（尿酸過度生成或排泄不足、尿酸鈉結晶引發發炎）**沒有已知關聯**。因此，TxGNN 的高分更可能來自知識圖譜中的網絡關聯，而非實際生物學證據，目前不宜視為有機轉支持的預測。

其他排名較前的預測也有類似問題，例如腦小血管疾病、遺傳性血尿合併視網膜小動脈迂曲症候群，皆為罕見遺傳性基底膜或血管疾病，與抗菌機轉無明顯關聯。糖尿病腎病變則因磺胺類藥物本身有腎臟不良反應風險（如結晶尿），需特別謹慎。

相對較合理的是**結膜炎**與**支氣管炎**，因其屬細菌感染相關，與原適應症（呼吸道、胃腸道、尿道感染）在抗菌作用上較為接近。但目前同樣沒有試驗或文獻資料，且支氣管炎多為病毒性，使用抗生素的價值有限。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sulfamethazine 的不重複許可證共 **59 張**：有效單方 0 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 58 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第027573號</td><td>"聯邦"鐵多拉三種磺胺錠</td><td>SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE、SULFADIAZINE</td><td>2024/05/25</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（58 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第001516號</td><td>命多磺淨錠０．５公克</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td></td></tr><tr><td>內衛藥製字第002472號</td><td>三合治炎片</td><td>SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE、SULFADIAZINE</td><td>2013/10/15</td></tr><tr><td>內衛藥製字第003671號</td><td>去腎炎錠</td><td>PHENAZOPYRIDINE HCL、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1989/11/27</td></tr><tr><td>內衛藥製字第004450號</td><td>富可治膠囊</td><td>NITROFURANTOIN、SULFAMETHAZINE (SULFADIMIDINE)</td><td>2013/10/01</td></tr><tr><td>內衛藥製字第005289號</td><td>命多磺淨粉</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td></td></tr><tr><td>內衛藥製字第006799號</td><td>三磺胺片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第011129號</td><td>三磺片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011587號</td><td>磺胺保利精片</td><td>SULFISOXAZOLE、SULFATHIAZOLE、SULFAMETHAZINE (SULFADIMIDINE)、S…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第014772號</td><td>速力輕錠</td><td>SULFADIAZINE、SULFAMETHAZINE (SULFADIMIDINE)、SULFATHIAZOLE</td><td>2004/05/31</td></tr><tr><td>內衛藥輸字第000515號</td><td>磺胺雙甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2005/06/16</td></tr><tr><td>內衛藥輸字第000553號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1985/09/07</td></tr><tr><td>內衛藥輸字第000561號</td><td>磺胺二甲嘧啶鈉</td><td>SULFAMETHAZINE SODIUM</td><td>1985/09/07</td></tr><tr><td>內衛藥輸字第001109號</td><td>磺胺咪叮</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1985/08/20</td></tr><tr><td>內衛藥輸字第001170號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1986/01/21</td></tr><tr><td>內衛藥輸字第001316號</td><td>磺胺二甲嘧啶鈉</td><td>SULFAMETHAZINE SODIUM</td><td>1985/08/12</td></tr><tr><td>內衛藥輸字第001987號</td><td>消發利美淨鈉</td><td>SULFAMETHAZINE SODIUM</td><td>1986/02/27</td></tr><tr><td>內衛藥輸字第002114號</td><td>磺胺二甲密定</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1986/06/04</td></tr><tr><td>內衛藥輸字第003206號</td><td>沙發美星鈉粉</td><td>SULFAMETHAZINE SODIUM</td><td>1990/08/01</td></tr><tr><td>內衛藥輸字第003251號</td><td>磺胺美沙淨</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1985/09/07</td></tr><tr><td>內衛藥輸字第003254號</td><td>磺胺二甲嘧啶鈉</td><td>SULFAMETHAZINE SODIUM</td><td>1985/08/28</td></tr><tr><td>內衛藥輸字第003572號</td><td>美素靈片</td><td>PHENAZOPYRIDINE HCL、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1990/08/01</td></tr><tr><td>內衛藥輸字第003821號</td><td>沙發美星粉</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1990/08/01</td></tr><tr><td>內衛藥輸字第003822號</td><td>沙發美星片</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1990/08/01</td></tr><tr><td>內衛藥輸字第007094號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1986/07/14</td></tr><tr><td>衛署藥製字第001472號</td><td>滅得利錠</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第006509號</td><td>三磺懸浮液</td><td>SULFADIAZINE、SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE</td><td>1992/12/10</td></tr><tr><td>衛署藥製字第019713號</td><td>泄卜菌錠</td><td>TRIMETHOPRIM、SULFAMETHAZINE (SULFADIMIDINE)</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第020401號</td><td>索扶新錠（磺胺二甲氧嘧定）</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第037132號</td><td>美沙磺胺錠５００公絲〝瑞士〞</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第000257號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第000264號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000333號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002190號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002263號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004280號</td><td>磺胺美沙淨</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第004680號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第004690號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第005077號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1995/04/06</td></tr><tr><td>衛署藥輸字第005079號</td><td>磺胺二甲嘧啶鈉</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1995/04/06</td></tr><tr><td>衛署藥輸字第005268號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1995/04/06</td></tr><tr><td>衛署藥輸字第010341號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1992/01/17</td></tr><tr><td>衛署藥輸字第011011號</td><td>"波蘭聯合" 磺胺二甲嘧啶粉劑</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1993/04/15</td></tr><tr><td>衛署藥輸字第013793號</td><td>磺胺二甲嘧啶鈉粉劑</td><td>SULFAMETHAZINE SODIUM</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第013831號</td><td>達嘧磺胺粉劑</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第013900號</td><td>達嘧磺胺鈉粉劑</td><td>SULFAMETHAZINE SODIUM</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第013904號</td><td>達嘧磺胺鈉粉劑</td><td>SULFAMETHAZINE SODIUM</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第013930號</td><td>美沙磺胺粉劑</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1998/07/27</td></tr><tr><td>衛署藥輸字第013936號</td><td>達嘧磺胺粉劑</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014727號</td><td>達嘧磺胺</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014764號</td><td>達嘧磺胺鈉</td><td>SULFAMETHAZINE SODIUM</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015042號</td><td>美沙磺胺</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第018514號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019647號</td><td>磺胺美沙靜</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1998/01/22</td></tr><tr><td>衛署藥輸字第020007號</td><td>磺胺二甲嘧啶</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第022270號</td><td>美沙磺胺</td><td>SULPHADIMIDINE (SULFAMETHAZINE)</td><td>2009/12/31</td></tr><tr><td>衛署藥陸輸字第000190號</td><td>美沙磺胺</td><td>SULFAMETHAZINE (SULFADIMIDINE)</td><td>2019/03/15</td></tr><tr><td>衛署藥陸輸字第000388號</td><td>美沙磺胺</td><td>SULFAMETHAZINE</td><td>2016/05/31</td></tr><tr><td>衛署藥陸輸字第000451號</td><td>美沙磺胺</td><td>Sulfamethazine (Sulfadimidine)</td><td>2017/04/14</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物-疾病禁忌關聯，非仿單文字）：遺傳性紫質症、紫質代謝疾病、紫質症、腎臟疾病、輸尿管積膿、血液疾病、肝臟疾病、膽囊疾病、葉酸缺乏性貧血。

其他警語、禁忌與藥物交互作用資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 痛風預測僅有模型分數，沒有臨床試驗或文獻，且機轉上與磺胺類抗菌作用無已知關聯，證據等級為 L5。
- 台灣目前僅有已註銷的許可證，無有效上市產品，且知識圖譜顯示腎臟、肝臟、血液疾病等潛在禁忌，風險考量較多。

**若要推進需要：**
- 補齊作用機轉資料，確認是否存在與尿酸代謝或發炎反應相關的機制。
- 進行系統性文獻檢索與臨床試驗登記查詢，確認是否有任何支持證據。
- 若仍想探索，建議優先評估結膜炎等與抗菌作用相符的適應症，並先釐清其市場可及性（現無有效許可證）。
- 完成安全性評估，特別是腎臟、肝臟與血液學風險。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「全部已註銷」 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L5，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L4）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

