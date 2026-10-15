---
layout: default
title: Cyclandelate
parent: 高證據等級 (L1-L2)
nav_order: 76
evidence_level: L2
indication_count: 10
---

# Cyclandelate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Cyclandelate：從末梢血管循環障礙到偏頭痛

## 一句話總結

Cyclandelate（杏仁酸三甲環己酯）是一種血管擴張劑與平滑肌鬆弛劑，原本用於末梢血管循環障礙。
TxGNN 模型預測它可能對**偏頭痛 (migraine disorder)** 有效，
目前有 **0 個臨床試驗登記**，但有 **12 篇文獻**支持這個方向，其中包含多項針對偏頭痛預防的雙盲隨機對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 末梢血管循環障礙 |
| 預測新適應症 | 偏頭痛 (migraine disorder)；此為證據最完整的預測，TxGNN 排名第 3，排名第 1 為 Prinzmetal 心絞痛 |
| TxGNN 預測分數 | 99.69%（偏頭痛）；排名第 1 的 Prinzmetal 心絞痛為 99.80% |
| 證據等級 | L2（偏頭痛） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 42 張（有效單方 1／有效複方 0／已註銷 41） |
| 建議決策 | Proceed with Guardrails |

> 說明：排名第 1 的 Prinzmetal 心絞痛僅有模型預測、沒有任何研究，證據等級為 L5。因此本報告以證據最完整的偏頭痛作為主要評估對象，其他預測於下方簡要說明。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。根據已知資訊，Cyclandelate 是直接作用於血管平滑肌的血管擴張劑，帶有類似鈣離子拮抗劑的活性。文獻指出它能抑制鈣離子誘發的血管平滑肌收縮，也能抑制血小板聚集及血清素（5-HT）釋放。

原適應症為末梢與腦循環障礙，偏頭痛則與腦血管張力及神經興奮性異常有關。同屬鈣離子拮抗劑類的 flunarizine 已被用於偏頭痛預防，因此從機轉上推論，Cyclandelate 可能調節腦血管張力與神經興奮性，具有預防偏頭痛的潛力。

<!-- review:begin cyclandelate-why-indication-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：這句推論的前提與台灣許可證資料不完全相符：現行唯一有效的 cyclandelate 許可證適應症只有「末梢血管循環障礙」，含「腦」血行障礙的安保平膠囊已於 1985-07-01 註銷。推論原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cyclandelate-why-indication-premise-2026-10-03 -->

不過要留意，臨床結果並非一面倒的正面。其中一項 251 人的安慰劑對照研究（2001 年）顯示，主要療效指標（偏頭痛天數減少）與多數次要指標並未達到預期差異。這點是推進時的主要疑慮。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為偏頭痛相關文獻（依 RCT > 回顧 排序，列出前 10 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8902255](https://pubmed.ncbi.nlm.nih.gov/8902255/) | 1996 | RCT | Cephalalgia | 214 位患者，雙盲多中心，比較 Cyclandelate 與安慰劑、propranolol 預防偏頭痛的療效與耐受性 |
| [11298666](https://pubmed.ncbi.nlm.nih.gov/11298666/) | 2001 | RCT | Cephalalgia | 251 位患者，1600 mg Cyclandelate 對比安慰劑 16 週；主要終點與多數次要終點未見明顯優勢 |
| [1573338](https://pubmed.ncbi.nlm.nih.gov/1573338/) | 1992 | RCT | Journal of Medicine | 84 位患者，雙盲 16 週，比較 Cyclandelate 與 pizotifen 的預防效果與耐受性 |
| [7649498](https://pubmed.ncbi.nlm.nih.gov/7649498/) | 1995 | RCT | Functional Neurology | Cyclandelate 對比 propranolol 與安慰劑，進行反應者與非反應者分析及劑量關係評估 |
| [9584874](https://pubmed.ncbi.nlm.nih.gov/9584874/) | 1998 | RCT | Functional Neurology | 雙盲安慰劑對照，以 CNV 探討 Cyclandelate 在偏頭痛的中樞作用機轉 |
| [3304950](https://pubmed.ncbi.nlm.nih.gov/3304950/) | 1987 | 隨機雙盲試驗 | Drugs | 40 位患者，Cyclandelate 800 mg 每日兩次對比 flunarizine，兩者皆較基線與安慰劑明顯減輕症狀 |
| [11121368](https://pubmed.ncbi.nlm.nih.gov/11121368/) | 2000 | 回顧性分析 | Eur J Med Res | 以 qEEG 探討偏頭痛的神經功能異常與臨床藥物反應之關聯 |
| [10463349](https://pubmed.ncbi.nlm.nih.gov/10463349/) | 1999 | Review | J Neurol | 偏頭痛急性發作治療新選項綜述 |
| [9829155](https://pubmed.ncbi.nlm.nih.gov/9829155/) | 1998 | Review | Drugs | 偏頭痛處置與預防的實務指引 |
| [2684591](https://pubmed.ncbi.nlm.nih.gov/2684591/) | 1989 | Review | Drugs | Flunarizine（鈣離子拮抗劑）用於神經疾病的藥理特性與療效回顧，可作為機轉類比參考 |

### 其他預測適應症概況

| 預測適應症 | TxGNN 分數 | 證據等級 | 現有證據 | 建議 |
|-----------|-----------|---------|---------|------|
| Prinzmetal 心絞痛 | 99.80% | L5 | 無，僅有模型預測；機轉上血管痙攣可能相關 | Hold |
| 雷諾氏病 | 99.73% | L4 | 僅一篇 1965 年病例系列（[14258038](https://pubmed.ncbi.nlm.nih.gov/14258038/)） | Research Question |
| 伴腦幹先兆偏頭痛 | 99.62% | L4 | 僅有一般偏頭痛研究，無針對此亞型的研究 | Research Question |
| 肺動脈高壓 | 99.50% | L5 | 無；全身性血管擴張劑有通氣灌流失配風險 | Hold |
| 痛風 | 99.43% | L5 | 無；機轉上缺乏合理連結 | Hold |
| 脊柱後側彎性心臟病 | 99.36% | L5 | 無；連結屬推測 | Hold |
| 良性前列腺增生 | 99.08% | L5 | 無；缺乏相關標靶活性 | Hold |
| 外生骨疣 | 99.06% | L5 | 無；無合理機轉 | Hold |
| 周邊血管疾病 | 99.04% | L3 | 多為回顧與小型研究，結果不一致；一項安慰劑對照交叉試驗（[6364892](https://pubmed.ncbi.nlm.nih.gov/6364892/)）報告無療效 | Research Question |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cyclandelate 的不重複許可證共 **42 張**：有效單方 1 張、有效複方 0 張、已註銷 41 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第001045號 | 脈速朗膠囊 | 膠囊劑 | 新喜國際企業股份有限公司 | 2031/05/25 | 末梢血管循環障礙 |

<details><summary><strong>已註銷</strong>（41 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第001567號</td><td>適通膠囊</td><td>CYCLANDELATE</td><td>1989/05/29</td></tr><tr><td>內衛藥製字第002324號</td><td>益寧膠囊</td><td>CYCLANDELATE</td><td>2000/08/08</td></tr><tr><td>內衛藥製字第016639號</td><td>循通膠囊</td><td>CYCLANDELATE</td><td>1988/07/19</td></tr><tr><td>內衛藥輸字第000909號</td><td>安保平膠囊</td><td>CYCLANDELATE</td><td>1985/07/01</td></tr><tr><td>內衛藥輸字第006652號</td><td>杏仁酸三甲環已酯</td><td>CYCLANDELATE</td><td>1986/01/21</td></tr><tr><td>衛署藥製字第003642號</td><td>佳泌朗膠囊</td><td>CYCLANDELATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第003674號</td><td>迅通膠囊</td><td>CYCLANDELATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第005230號</td><td>杏仁酸三甲環己酯</td><td>CYCLANDELATE</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第006094號</td><td>助血脈膠囊</td><td>CYCLANDELATE</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第007707號</td><td>展脈能膠囊</td><td>CYCLANDELATE</td><td>2023/07/24</td></tr><tr><td>衛署藥製字第012877號</td><td>絡可舒膠囊</td><td>CYCLANDELATE</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第000540號</td><td>杏仁酸三甲環己酯</td><td>CYCLANDELATE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第000781號</td><td>怡杷瑯膠囊</td><td>CYCLANDELATE</td><td>1986/01/22</td></tr><tr><td>衛署藥輸字第000799號</td><td>杏仁酸三甲環己酯</td><td>CYCLANDELATE</td><td>1999/12/02</td></tr><tr><td>衛署藥輸字第001185號</td><td>杏仁酸三甲環己酯</td><td>CYCLANDELATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第001861號</td><td>理全朗膠囊</td><td>CYCLANDELATE</td><td>1987/03/24</td></tr><tr><td>衛署藥輸字第001989號</td><td>散血可朗膠囊</td><td>CYCLANDELATE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第002009號</td><td>杏仁酸３，３，５，三甲環乙酯</td><td>CYCLANDELATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第002075號</td><td>三甲烷環六烷基</td><td>CYCLANDELATE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第003828號</td><td>敏納路</td><td>SODIUM PHOSPHATE DIBASIC (eq to DISOD. HYDROGEN PHOSPHATE) (…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003852號</td><td>須固拉得膠囊</td><td>CYCLANDELATE</td><td>1986/07/11</td></tr><tr><td>衛署藥輸字第004048號</td><td>惠舒脈通膠囊</td><td>CYCLANDELATE</td><td>1991/03/28</td></tr><tr><td>衛署藥輸字第004196號</td><td>腦塞朗膠囊</td><td>CYCLANDELATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第004200號</td><td>塞固頑膠囊</td><td>CYCLANDELATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004229號</td><td>脈能即補膠囊</td><td>CYCLANDELATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第004695號</td><td>斯克蘭膠囊</td><td>CYCLANDELATE</td><td>1988/08/19</td></tr><tr><td>衛署藥輸字第004761號</td><td>喜久樂得膠囊</td><td>CYCLANDELATE</td><td>1986/07/08</td></tr><tr><td>衛署藥輸字第005362號</td><td>希高累得膠囊</td><td>CYCLANDELATE</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第007653號</td><td>塞克迪拉特膠囊２００公絲</td><td>CYCLANDELATE</td><td>1986/07/08</td></tr><tr><td>衛署藥輸字第008572號</td><td>杏仁酸三甲環己脂</td><td>CYCLANDELATE</td><td>1985/04/18</td></tr><tr><td>衛署藥輸字第009219號</td><td>喜腦明膠囊</td><td>CYCLANDELATE</td><td>1986/11/17</td></tr><tr><td>衛署藥輸字第009222號</td><td>血流循多膠囊</td><td>CYCLANDELATE</td><td>1990/10/08</td></tr><tr><td>衛署藥輸字第009641號</td><td>康拉平膠囊</td><td>CYCLANDELATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第011765號</td><td>舒可通糖衣錠</td><td>CYCLANDELATE</td><td>1988/11/10</td></tr><tr><td>衛署藥輸字第013390號</td><td>安知先</td><td>CYCLANDELATE</td><td>1992/01/09</td></tr><tr><td>衛署藥輸字第013411號</td><td>杏仁酸三甲環己脂粉劑</td><td>CYCLANDELATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第013552號</td><td>安保平膠囊</td><td>CYCLANDELATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第014708號</td><td>塞可朗</td><td>CYCLANDELATE</td><td>1992/02/20</td></tr><tr><td>衛署藥輸字第015657號</td><td>塞可朗膠囊１００公絲</td><td>CYCLANDELATE</td><td>2013/11/26</td></tr><tr><td>衛署藥輸字第015845號</td><td>怡杷瑯膠囊</td><td>CYCLANDELATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第018868號</td><td>安知先膠囊</td><td>CYCLANDELATE</td><td>2004/12/23</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：已查詢到 17 筆交互作用，皆為中度等級，主要涉及下列類別：
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin
  - 前列腺素類血管擴張藥：Selexipag、Treprostinil、Epoprostenol、Iloprost
  - 其他血管活性或降壓相關藥物：Pentoxifylline、Minoxidil（外用）、Brimonidine（眼用及外用）
  - 其他：Amifostine、Promethazine、Nitrous acid、Ozanimod、Procarbazine

  多數合併使用情境涉及血壓下降等加成效應，併用時需留意。

其餘警語與禁忌症資料請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails（針對偏頭痛預防）**

**理由：**
- 偏頭痛已有多項雙盲 RCT 與活性對照試驗，並有回顧文獻提供機轉背景，證據明顯優於其他預測；但最大型的安慰劑對照試驗（2001 年）主要終點未見明顯優勢，療效證據並不一致。
- 其他預測多為 L5 的模型預測（建議 Hold），雷諾氏病與周邊血管疾病證據薄弱或結果不一致，僅宜作為研究問題。
- 台灣目前僅剩 1 張有效單方許可證，且原適應症為末梢血管循環障礙，偏頭痛屬於新適應症。

**若要推進需要：**
- 系統性回顧與統合分析，整合現有偏頭痛 RCT，釐清 2001 年試驗結果與其他陽性研究之間的差異
- 補齊 Cyclandelate 的作用機轉（MOA）資料
- 與現行偏頭痛預防藥物（如 propranolol、flunarizine）進行比較，評估臨床定位
- 確認劑型、劑量（文獻使用高劑量，例如 1600 mg/日）與台灣現有膠囊劑的相容性
- 建立安全性監測計畫，並補齊警語與禁忌症資料
- 在台灣申請新增適應症前，與主管機關討論所需的證據要求

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表 5 張中 4 張已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「原核准用於腦循環及末梢血管循環障礙」 | 報告重生後已無此錯誤（2026-10-15：一句話總結已改寫為「原本用於末梢血管循環障礙」；推論段「原適應症為末梢與腦循環障礙」由 cyclandelate-why-indication-premise 紀錄處理；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 預測理由「已核准用於腦循環障礙改善」 | 加註（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

