---
layout: default
title: Sulfamerazine
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 4
monitor_inn: "Sulfamerazine"
predicted_indications: ["gout", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "conjunctivitis"]
last_modified_at: 2026-10-16
description: "Sulfamerazine：預測新適應症為痛風 (Gout)（證據等級 L5）。原適應症：肺炎球菌、鏈球菌、葡萄球菌、腦膜炎菌感染症"
---

# Sulfamerazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Sulfamerazine：從細菌感染症到痛風
{: .text-alpha }

## 一句話總結

Sulfamerazine（磺胺甲嘧啶）是磺胺類抗菌藥物，原本用於肺炎球菌、鏈球菌、葡萄球菌、腦膜炎菌等革蘭氏陽性及陰性菌感染症。
TxGNN 模型預測它可能對**痛風 (Gout)** 有效，但目前**沒有任何臨床試驗或文獻**支持，證據僅來自模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺炎球菌、鏈球菌、葡萄球菌、腦膜炎菌感染症 |
| 預測新適應症 | 痛風 (Gout) |
| TxGNN 預測分數 | 99.35% |
| 證據等級 | L5 |
| 台灣上市 | 已無有效許可證（僅有已註銷許可證） |
| 許可證數 | 40 張（有效單方 0／有效複方 0／已過期 1／已註銷 39） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Sulfamerazine 是磺胺類抗菌藥物，一般認為其作用是抑制細菌的二氫蝶酸合成酶（dihydropteroate synthase），干擾細菌葉酸合成。

這個機轉與尿酸代謝或痛風的病理生理（尿酸結晶沉積引發的發炎反應）之間，**沒有已知的明確關聯**。TxGNN 的高分預測（99.35%）可能反映知識圖譜中的網路相似性，而非實際的生物學依據，需要審慎看待。

其他排名較前的預測也有類似情形：

| 排名 | 預測疾病 | 分數 | 評估 |
|------|---------|------|------|
| 2 | 體染色體顯性家族性血尿-視網膜小動脈迂曲-攣縮症候群 | 99.19% | 為膠原蛋白 IV 相關的遺傳性血管疾病，與抗菌機轉無明顯關聯 |
| 3 | 腦小血管疾病 1 型（合併或不合併眼部異常） | 99.19% | 為單基因遺傳疾病，可能反映網路相似性而非生物學依據 |
| 4 | 結膜炎 (Conjunctivitis) | 99.02% | 磺胺類曾用於細菌感染（含眼部感染），抗菌邏輯上較合理，但無任何證據 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sulfamerazine 的不重複許可證共 **40 張**：有效單方 0 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 39 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第027573號</td><td>"聯邦"鐵多拉三種磺胺錠</td><td>SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE、SULFADIAZINE</td><td>2024/05/25</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（39 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第002472號</td><td>三合治炎片</td><td>SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE、SULFADIAZINE</td><td>2013/10/15</td></tr><tr><td>內衛藥製字第003373號</td><td>複合磺胺錠</td><td>SULFATHIAZOLE、SULFAMERAZINE、SULFADIAZINE</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第006799號</td><td>三磺胺片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007330號</td><td>磺胺多利精片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFATHIAZOLE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007751號</td><td>磺胺保利精顆粒</td><td>SULFADIAZINE、SULFATHIAZOLE、SULFAMERAZINE、SULFISOXAZOLE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第009912號</td><td>胺氯素片</td><td>SULFATHIAZOLE、SULFAMERAZINE、SULFADIAZINE</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第011129號</td><td>三磺片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第012066號</td><td>立消寧膠囊</td><td>SULFATHIAZOLE、SULFAMERAZINE、SULFADIAZINE</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第013670號</td><td>治消炎片</td><td>SULFAMERAZINE、SULFATHIAZOLE、BERBERINE HCL、SULFADIAZINE</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第014459號</td><td>消炎片</td><td>BERBERINE HCL、SULFADIAZINE、TALC (FRENCH CHALK)、SULFATHIAZOLE…</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第014867號</td><td>美美消炎片</td><td>BERBERINE HCL、SULFADIAZINE、SULFAMERAZINE、SULFATHIAZOLE</td><td>1998/03/16</td></tr><tr><td>內衛藥輸字第000554號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1985/08/28</td></tr><tr><td>內衛藥輸字第000560號</td><td>磺胺甲嘧啶鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/01/28</td></tr><tr><td>內衛藥輸字第001988號</td><td>消發米拉錚鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/06/04</td></tr><tr><td>內衛藥輸字第002113號</td><td>消發米拉錚</td><td>SULFAMERAZINE</td><td>1986/02/26</td></tr><tr><td>內衛藥輸字第003040號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1986/01/16</td></tr><tr><td>內衛藥輸字第003252號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1985/08/28</td></tr><tr><td>內衛藥輸字第004207號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1986/02/20</td></tr><tr><td>內衛藥輸字第004210號</td><td>磺胺甲嘧啶鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/05/12</td></tr><tr><td>內衛藥輸字第007097號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1986/07/14</td></tr><tr><td>內衛藥輸字第007103號</td><td>磺胺甲嘧啶鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/07/14</td></tr><tr><td>衛署藥製字第000380號</td><td>泛須如法控注射液</td><td>SULFAMERAZINE SODIUM、SULFADIAZINE SODIUM、SULFISOMIDINE SODIU…</td><td>1991/07/16</td></tr><tr><td>衛署藥製字第005533號</td><td>三磺胺錠</td><td>SULFADIAZINE、SULFATHIAZOLE、SULFAMERAZINE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第006509號</td><td>三磺懸浮液</td><td>SULFADIAZINE、SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE</td><td>1992/12/10</td></tr><tr><td>衛署藥製字第033874號</td><td>泛須如法控注射液</td><td>SULFAMERAZINE SODIUM、SULFADIAZINE SODIUM、SULFISOMIDINE SODIU…</td><td>2000/08/04</td></tr><tr><td>衛署藥輸字第000225號</td><td>磺胺甲噠/</td><td>SULFAMERAZINE</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第000298號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002114號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004278號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第004570號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第004870號</td><td>磺胺美拉純鈉鹽</td><td>SULFAMERAZINE SODIUM</td><td>1994/06/10</td></tr><tr><td>衛署藥輸字第010343號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1992/01/17</td></tr><tr><td>衛署藥輸字第013906號</td><td>美拉磺胺粉劑</td><td>SULFAMERAZINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第013908號</td><td>美拉磺胺粉劑</td><td>SULFAMERAZINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014642號</td><td>美拉磺胺</td><td>SULFAMERAZINE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第014726號</td><td>美拉磺胺</td><td>SULFAMERAZINE SODIUM</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014765號</td><td>美拉磺胺</td><td>SULFAMERAZINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014771號</td><td>美拉磺胺</td><td>SULFAMERAZINE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第015043號</td><td>美拉磺胺鈉</td><td>SULFAMERAZINE SODIUM</td><td>1999/09/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物-疾病禁忌關聯，非仿單內容）：遺傳性卟啉症、卟啉代謝疾病、卟啉症、腎臟疾病、輸尿管積膿、血液疾病、肝臟疾病、膽囊疾病、葉酸缺乏性貧血。
- **藥物交互作用**：查詢無相關紀錄。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 痛風的預測完全來自模型，沒有臨床試驗或文獻佐證，且磺胺類抗菌機轉與痛風病理之間沒有已知關聯。
- 台灣目前沒有有效許可證，缺乏可直接取得的上市產品。
- 知識圖譜顯示腎臟、肝臟、血液疾病等禁忌，而這些共病在痛風族群中並不少見，需更謹慎。

**若要推進需要：**
- 取得 Sulfamerazine 的作用機轉資料（例如從 DrugBank 補齊），評估是否與尿酸代謝或痛風發炎路徑有任何關聯。
- 進行系統性文獻檢索與前臨床研究（如尿酸轉運體或黃嘌呤氧化酶相關試驗），確認生物學合理性。
- 若仍想探索抗感染方向，可優先評估預測排名 4 的結膜炎，但需先確認磺胺類在現代治療中的定位，以及已有更多選擇的替代藥物。
- 釐清台灣上市與供應狀況（目前許可證皆已註銷）。

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

