---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

# Fluorescein：從診斷試劑到 Prinzmetal 心絞痛

## 一句話總結

Fluorescein（螢紅鈉）是眼科廣泛使用的惰性螢光染料，台灣核准用途包括眼底血管螢光造影、眼壓測量及角膜病變評估，屬於純診斷性試劑，不具治療性藥理活性。
TxGNN 模型預測它可能對 **Prinzmetal 心絞痛 (Prinzmetal angina)** 有效，
目前有 **0 個臨床試驗**和 **0 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 診斷試劑 |
| 預測新適應症 | Prinzmetal 心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 14 張（有效單方 1／有效複方 0／已註銷 13） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Fluorescein 是一種惰性有機螢光染料，本身不與人體組織發生藥理交互作用，在體內會快速代謝為 fluorescein monoglucuronide，原形與代謝物主要經腎臟排出。其臨床應用完全集中於診斷領域：靜脈注射後可使視網膜與脈絡膜血管顯影（眼底血管螢光造影）；局部點眼則用於角膜上皮損傷染色與眼壓測量。

<!-- review:begin fluorescein-metabolism-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「在體內幾乎不被代謝即原形排出」。仿單載明 fluorescein 會快速代謝為 fluorescein monoglucuronide（靜脈注射 1 小時後血漿中約 80% 已轉為葡萄糖醛酸結合物），原形與代謝物主要經腎臟排出。本次只更正這個藥理事實，推論與結論未改。依據：[DailyMed：FLUORESCITE（fluorescein injection, USP）10% 美國仿單 §12.3](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebb3883c-71f6-4fd0-a7e6-0ba8e1136dd9)。

<!-- review:end fluorescein-metabolism-2026-10-03 -->

Prinzmetal 心絞痛（變異性心絞痛）由冠狀動脈痙攣引起，主要發作於休息狀態，治療核心在於舒張冠狀動脈平滑肌，臨床標準用藥為鈣離子通道阻斷劑及長效硝酸鹽類。此適應症與 Fluorescein 的眼科診斷用途在解剖部位、疾病機轉及給藥途徑上均無任何重疊。

Fluorescein 對冠狀動脈平滑肌、血管痙攣或相關訊號傳遞路徑無任何已知藥理機轉。TxGNN 的預測極可能源於知識圖譜中「血管造影劑 → 血管相關疾病群集」的遠端路徑雜訊，**不具備任何臨床或基礎研究的支持**。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Fluorescein 的不重複許可證共 **14 張**：有效單方 1 張、有效複方 0 張、已註銷 13 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025806號 | "愛爾康"服攝得注射劑10% | 注射劑 | 瑞士商愛爾康大藥廠股份有限公司台灣分公司 | 2027/08/27 | 血管造影劑。 |

<details><summary><strong>已註銷</strong>（13 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第006158號</td><td>螢紅鈉</td><td>FLUORESCEIN SODIUM (URANIN)(URANIN YELLOW)</td><td>1985/10/16</td></tr><tr><td>衛署藥輸字第000616號</td><td>復露條－Ａ．Ｔ．</td><td>FLUORESCEIN SODIUM (URANIN)(URANIN YELLOW)</td><td>1986/06/16</td></tr><tr><td>衛署藥輸字第001090號</td><td>螢光紅</td><td>FLUORESCEIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第003874號</td><td>服攝得注射劑１０％</td><td>FLUORESCEIN (SODIUM)、SODIUM BICARBONATE ( EQ TO SODIUM HYDRO…</td><td>1986/07/08</td></tr><tr><td>衛署藥輸字第006450號</td><td>複樂力淨診斷用注射劑１０％Ｗ/Ｖ</td><td>FLUORESCEIN SODIUM (URANIN)(URANIN YELLOW)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014228號</td><td>螢紅鈉</td><td>FLUORESCEIN SODIUM (URANIN)(URANIN YELLOW)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第014877號</td><td>服攝得注射劑１０％</td><td>FLUORESCEIN</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第017676號</td><td>２％服攝得點眼液</td><td>SODIUM HYDROXIDE、FLUORESCEIN</td><td>1997/06/07</td></tr><tr><td>衛署藥輸字第019218號</td><td>愛爾康服攝得注射劑　１０％</td><td>FLUORESCEIN</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第019617號</td><td>服攝得注射劑〝愛爾康〞</td><td>HYDROCHLORIC ACID、WATER FOR INJECTION、FLUORESCEIN</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第022242號</td><td>服攝得點眼液２％</td><td>FLUORESCEIN SODIUM (URANIN)(URANIN YELLOW)</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第024616號</td><td>服攝得注射劑10%</td><td>FLUORESCEIN</td><td>2019/03/22</td></tr><tr><td>衛署藥輸字第024943號</td><td>服眼欣注射劑</td><td>FLUORESCEIN SODIUM (URANIN)(URANIN YELLOW)</td><td>2020/04/07</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Fluorescein 為純診斷性惰性染料，缺乏任何藥理活性或治療機轉，針對 Prinzmetal 心絞痛的 TxGNN 預測無任何臨床試驗或文獻佐證，屬知識圖譜遠端路徑雜訊（L5），不具老藥新用的可行性基礎。

**若要推進需要：**
- Fluorescein 對冠狀動脈平滑肌或血管張力影響的前臨床（體外 / 動物）研究數據
- 補充 DrugBank API 完整的作用機轉（MOA）資料（目前為 Data Gap）
- 至少一篇具機轉連結的基礎研究文獻，方可升級至 L4 並重新評估優先級

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「在體內幾乎不被代謝即原形排出」 | 更正 | [DailyMed：FLUORESCITE（fluorescein injection, USP）10% 美國仿單 §12.3](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebb3883c-71f6-4fd0-a7e6-0ba8e1136dd9) |
| 2026-10-03 | 許可證表 5 張全數已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

