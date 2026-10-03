---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil（5-FU）：從消化道腫瘤到陰道葡萄狀胚胎型橫紋肌肉瘤

---

---

## 一句話總結

Fluorouracil（5-FU）是臨床使用超過 60 年的 Fluoropyrimidine 類抗代謝化療藥，廣泛應用於大腸直腸癌、胃癌、乳癌等消化道及固態腫瘤的標準化療方案。
TxGNN 模型預測它可能對**陰道葡萄狀胚胎型橫紋肌肉瘤 (Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina)** 有效，
然而目前**無任何臨床試驗或文獻**支持此特定亞型，此預測屬純模型預測（L5 等級），建議維持 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消化器癌（如胃癌、直腸癌、結腸癌）、肺癌、乳癌病狀之緩解；結腸癌、直腸癌、乳癌、胃癌、胰臟癌，以及不可以手術之胃腸道、乳部惡性腫瘤的姑息療法 |
| 預測新適應症 | 陰道葡萄狀胚胎型橫紋肌肉瘤 (Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 40 張（有效單方 4／有效複方 0／已註銷 36） |
| 建議決策 | Hold |

<!-- review:begin fluorouracil-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／⚠️ 許可證資料錯誤（顯示為 Trastuzumab 適應症）；5-FU 已知核准適應症包含大腸直腸癌、胃癌、乳癌等」。已依 TFDA 現行有效的 fluorouracil 注射液許可證改寫適應症。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fluorouracil-original-indication-2026-10-03 -->

---

## 為什麼這個預測合理？

目前彙整資料中 Fluorouracil 的作用機轉（MOA）標記為 Data Gap。根據已知藥理學知識，5-FU 屬於 **Fluoropyrimidine 抗代謝藥物**，其主要機轉為：**抑制胸苷酸合酶（Thymidylate Synthase, TS）**，阻斷去氧尿苷一磷酸（dUMP）轉換為去氧胸苷一磷酸（dTMP），中斷 DNA 合成；同時，5-FU 代謝產物（FUTP）可嵌入 RNA，干擾 RNA 加工與蛋白質合成。這種廣效的核酸代謝干擾機轉，使 5-FU 對所有快速增殖的腫瘤細胞具有潛在的細胞毒性。

陰道葡萄狀胚胎型橫紋肌肉瘤（Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina）是一種極罕見的兒童期婦科惡性腫瘤，腫瘤細胞具有快速增殖特性，理論上對抗代謝藥物具有潛在敏感性。從疾病生物學角度看，RMS 與 5-FU 原始適應症（消化道腫瘤）同樣涉及快速分裂的腫瘤細胞群體，機轉上存在間接關聯性。

然而需要特別指出，橫紋肌肉瘤的標準化療方案為 **VAC（Vincristine + Actinomycin-D + Cyclophosphamide）**，5-FU 並非 RMS 任何亞型的一線或標準治療選項。TxGNN 的高分預測可能反映知識圖譜中 5-FU 廣泛的抗腫瘤活性節點連結，而非疾病特異性的直接生物學關聯。此亞型好發於幼兒，且為婦科局部病灶，5-FU 在 RMS 的特殊解剖位置與給藥路徑上亦無文獻支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 台灣上市資訊

> ⚠️ **以下許可證資料為資料管道錯誤所引入的 Trastuzumab 生物相似藥（曲斯若）資訊，並非 Fluorouracil（5-FU）的台灣許可證。** 此列表僅供識別資料錯誤之用，不應作為 5-FU 法規依據引用。

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Fluorouracil 的不重複許可證共 **40 張**：有效單方 4 張、有效複方 0 張、已註銷 36 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第022587號 | 清淨癌注射液 | 注射劑 | 育新企業股份有限公司 | 2028/12/08 | 結腸癌、直腸癌、乳癌、胃癌、胰臟癌、不可以手術之胃腸道乳部惡性腫瘤的姑息療法 |
| 衛部藥製字第058033號 | 好復注射液50毫克/毫升 | 注射劑 | 南光化學製藥股份有限公司 | 2028/07/31 | 消化器癌(如胃癌、直腸癌、結腸癌)、肺癌、乳癌病狀之緩解。 |
| 衛部藥製字第058842號 | 癒復達注射液50毫克/毫升 | 注射劑 | 台灣東洋藥品工業股份有限公司 | 2030/10/01 | 消化器癌(如胃癌、直腸癌、結腸癌)、肺癌、乳癌病狀之緩解。 |
| 衛部藥陸輸字第001022號 | 氟嘧啶二酮 | （粉） | 台灣荃新股份有限公司 | 2026/10/15 | 抗腫瘤藥 |

<details><summary><strong>已註銷</strong>（36 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第009964號</td><td>福爾壽注射液</td><td>FLUOROURACIL 5-</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第014158號</td><td>"居禮" 特復拉西膠囊</td><td>FLUOROURACIL 5-</td><td>2009/04/17</td></tr><tr><td>衛署藥製字第017920號</td><td>富多樂富膠囊（特復拉西）”人生”　　　　　　　　　　　　　　 F</td><td>FLUOROURACIL 5-</td><td>1989/08/17</td></tr><tr><td>衛署藥製字第024978號</td><td>特復拉西注射液４０公絲/公撮</td><td>TEFURACI INJECTION 40MG/ML (FLUOROURACIL) "F.M."</td><td>2002/04/18</td></tr><tr><td>衛署藥製字第024996號</td><td>特復拉西膠囊２００公絲</td><td>FLUOROURACIL 5-</td><td>1992/05/15</td></tr><tr><td>衛署藥輸字第000533號</td><td>癌膚治軟膏</td><td>FLUOROURACIL 5-</td><td>1989/12/26</td></tr><tr><td>衛署藥輸字第003688號</td><td>有利癌內服液</td><td>FLUOROURACIL 5-</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第003908號</td><td>氟嘧啶二酮</td><td>FLUOROURACIL 5-</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第004447號</td><td>氟嘧啶二酮</td><td>FLUOROURACIL 5-</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第005413號</td><td>有利癌２５０公絲膠囊</td><td>FLUOROURACIL 5-</td><td>1990/04/11</td></tr><tr><td>衛署藥輸字第006263號</td><td>康福治糖漿用散劑</td><td>FLUOROURACIL 5-</td><td>1993/06/19</td></tr><tr><td>衛署藥輸字第006337號</td><td>康福治注射液</td><td>FLUOROURACIL 5-</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第006956號</td><td>５－氟尿嘧啶</td><td>FLUOROURACIL 5-</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第007574號</td><td>優樂明糖漿用粉</td><td>FLUOROURACIL 5-</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008249號</td><td>有福注射液</td><td>FLUOROURACIL 5-、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROM…</td><td>1997/05/31</td></tr><tr><td>衛署藥輸字第011095號</td><td>有利癌注射液２５０公絲/１０公撮</td><td>FLUOROURACIL</td><td>1990/04/11</td></tr><tr><td>衛署藥輸字第011924號</td><td>佛羅西注射液</td><td>FLUOROURACIL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013291號</td><td>氟尿嘧啶注射液</td><td>FLUOROURACIL 5-</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013603號</td><td>有利癌注射液２５０公絲/５公撮</td><td>FLUOROURACIL 5- (SODIUM)</td><td>1996/02/12</td></tr><tr><td>衛署藥輸字第014869號</td><td>富優癌注射液</td><td>FLUOROURACIL 5-</td><td>1988/04/14</td></tr><tr><td>衛署藥輸字第015637號</td><td>氟洛拉西</td><td>FLUOROURACIL</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第016423號</td><td>富優癌注射液</td><td>FLUOROURACIL 5-</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第017460號</td><td>宜膚滌</td><td>FLUOROURACIL 5-</td><td>2010/09/13</td></tr><tr><td>衛署藥輸字第019186號</td><td>佛羅西注射液小瓶</td><td>FLUOROURACIL</td><td>1997/09/01</td></tr><tr><td>衛署藥輸字第020406號</td><td>弗洛瑞斯注射液</td><td>FLUOROURACIL</td><td>1997/06/30</td></tr><tr><td>衛署藥輸字第020793號</td><td>服樂癌注射劑２５公絲/公撮</td><td>FLUOROURACIL</td><td>2003/01/03</td></tr><tr><td>衛署藥輸字第020807號</td><td>服樂癌注射液５０公絲／公撮</td><td>FLUOROURACIL</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第021121號</td><td>有利癌注射液２５０公絲/５公撮</td><td>FLUOROURACIL</td><td>2002/09/12</td></tr><tr><td>衛署藥輸字第021689號</td><td>佛羅西注射液小瓶</td><td>FLUOROURACIL</td><td>2021/12/17</td></tr><tr><td>衛署藥輸字第021720號</td><td>弗洛瑞斯注射液</td><td>FLUOROURACIL</td><td>2021/12/17</td></tr><tr><td>衛署藥輸字第023404號</td><td>有利癌</td><td>FLUOROURACIL</td><td>2019/03/28</td></tr><tr><td>衛署藥輸字第023514號</td><td>"瑞士舒克" 艾欣宜膚滌軟膏</td><td>FLUOROURACIL</td><td>2016/05/31</td></tr><tr><td>衛部藥輸字第026372號</td><td>菲芙抗癌注射劑50毫克/毫升</td><td>FLUOROURACIL</td><td>2022/07/06</td></tr><tr><td>衛部藥輸字第026676號</td><td>愛福癌注射液50毫克/毫升</td><td>FLUOROURACIL</td><td>2022/06/21</td></tr><tr><td>衛部藥輸字第027435號</td><td>"山德士"伏樂癌注射劑50毫克/毫升</td><td>FLUOROURACIL</td><td>2021/05/13</td></tr><tr><td>衛部藥輸字第028040號</td><td>福佑瑞欣注射液</td><td>FLUOROURACIL</td><td>2024/08/12</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**正確資訊提示**：Fluorouracil 注射劑在台灣確有合法上市，許可證總數約 20 張，劑型以注射劑為主，請透過 TFDA 藥品許可證查詢系統（搜尋關鍵字：fluorouracil / 氟尿嘧啶）取得正確資料。

<!-- review:begin fluorouracil-tw-license-note-2026-10-03 -->

> **查核加註（2026-10-03）**：查 TFDA 許可證資料：fluorouracil 目前有效的許可證是衛部藥製字第058842號「癒復達注射液50毫克/毫升」、衛署藥製字第022587號「清淨癌注射液」、衛部藥製字第058033號「好復注射液50毫克/毫升」，以及 1 張原料藥許可證；歷年累計共 48 張，其餘已註銷。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end fluorouracil-tw-license-note-2026-10-03 -->

---

## 細胞毒性

Fluorouracil 屬於抗腫瘤/細胞毒性藥物（Antineoplastic Agents、Antimetabolites），符合本章節適用條件。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類抗代謝劑） |
| 骨髓抑制風險 | 中度（常見嗜中性白血球減少、血小板減少，連續輸注時黏膜炎較顯著） |
| 致吐性分級 | 低至中度（依劑量與給藥方式而異） |
| 監測項目 | CBC（含分類）、肝腎功能（Cr/BUN）、電解質、口腔黏膜狀況、手足症候群評估 |
| 處置防護 | 需依細胞毒性藥物調配與給藥規範操作；連續輸注（持續性靜滴）應使用密閉給藥系統 |

請參考原廠仿單的警語與注意事項，以獲取完整的毒性描述（包含心臟毒性、神經毒性等警示）。

---

## 安全性考量

### 藥物交互作用

共偵測到 **361 筆**交互作用（來源：DDInter 2.0），以下為主要具臨床意義項目：

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Metronidazole | 中度（Moderate） | 可能抑制 5-FU 的二氫嘧啶去氫酶（DPD）代謝路徑，增加 5-FU 暴露量及毒性風險 |
| Tinidazole | 中度（Moderate） | 機轉類似 Metronidazole，同屬硝基咪唑類，需注意毒性疊加 |
| Cimetidine | 輕度（Minor） | 可能輕度影響 5-FU 代謝清除 |
| Levofloxacin | 輕度（Minor） | 需注意 QTc 延長風險的加成效應 |

> 完整 361 筆交互作用清單請參考 DDInter 2.0（https://ddinter2.scbdd.com）。

---

## 結論與下一步

**決策：Hold**

**理由：**
陰道葡萄狀胚胎型橫紋肌肉瘤為極罕見兒科婦科亞型，目前完全無臨床試驗或文獻支持 5-FU 用於此疾病，證據等級僅達 L5（純模型預測）。RMS 的標準化療不含 5-FU，再利用潛力薄弱。

> 📌 **優先建議**：本批次 10 項預測中，**Rank 7：肝臟肉瘤（Liver Sarcoma）** 具有相對最佳的證據基礎（5 個臨床試驗、20 篇文獻、L4 等級、Research Question 建議），建議優先就該適應症重新生成詳細評估報告，以支持後續研究決策。

**若要推進本適應症需要：**
1. **修正資料管道**：確保台灣許可證資料正確對應 Fluorouracil（5-FU），而非 Trastuzumab
2. **補充 MOA 資料**：查詢 DrugBank API 取得 DB00544 完整作用機轉描述
3. **前臨床驗證**：在 RMS 細胞株（如 RD、A204）進行 5-FU 敏感性測試，建立最低可信的前臨床依據後，才可考慮進一步評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原適應症改為 TFDA 許可證所載 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證數「20 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 正確資訊提示「許可證總數約 20 張」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

