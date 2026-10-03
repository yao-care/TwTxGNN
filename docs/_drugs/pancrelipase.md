---
layout: default
title: Pancrelipase
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Pancrelipase
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

# Pancrelipase：從胰腺外分泌不全到粒線體氧化磷酸化障礙

## 一句話總結

Pancrelipase（胰脂酵素）是一種混合消化酵素製劑（含脂解酶、蛋白酶、澱粉酶），原本用於各種原因導致的胰液分泌不全，如囊腫性纖維化、慢性胰臟炎等。
TxGNN 模型預測它可能對**核DNA異常所致粒線體氧化磷酸化障礙 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies)** 有效，
然而目前**無任何臨床試驗或文獻**支持，所有前 10 項預測均停留於模型推論階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 解脂 |
| 預測新適應症 | 核DNA異常所致粒線體氧化磷酸化障礙 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 10 張（有效單方 0／有效複方 2／已註銷 8） |
| 建議決策 | Hold |

<!-- review:begin pancrelipase-original-indication-2026-10-03 -->

> **查核加註（2026-10-03）**：「解脂」取自已於 1985-09-19 註銷的原料藥許可證（衛署藥輸字第007271號）。現行有效的兩張許可證都是含 lipase、protease、amylase 的腸溶微粒膠囊：衛署藥製字第046067號核准囊腫性纖維化、慢性胰臟炎、胰臟切除、胃腸繞道手術及腫瘤造成胰管或膽管阻塞所致的胰液分泌不全，衛署藥製字第055412號寫「幫助消化」。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end pancrelipase-original-indication-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pancrelipase 是豬胰臟萃取物，含有脂解酶（lipase）、蛋白酶（protease）及澱粉酶（amylase）三大成分，主要用途是補充胰腺外分泌功能不足時缺乏的消化酵素，促進腸道消化吸收脂肪、蛋白質與澱粉。

核DNA異常所致粒線體氧化磷酸化障礙屬於罕見代謝遺傳疾病，根本病因為核基因組中與粒線體電子傳遞鏈相關的基因突變，導致 ATP 生成障礙。Pancrelipase 與此適應症的潛在間接關聯在於：改善脂肪與蛋白質吸收後，理論上可提供粒線體氧化磷酸化所需的部分營養受質，例如長鏈脂肪酸、脂溶性輔酶前驅物（如輔酶 Q10 前驅物的吸收底物）。

然而此連結極為間接，缺乏合理的直接藥理機轉。Pancrelipase 作為口服消化酵素，在腸腔內發揮局部消化作用後即失活，幾乎不進入全身循環，對粒線體複合體的結構或功能無已知調節作用。TxGNN 的預測很可能反映知識圖譜中胰腺代謝節點與粒線體疾病節點的拓撲鄰近性，而非真實的直接生物學連結。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Pancrelipase 的不重複許可證共 **10 張**：有效單方 0 張、有效複方 2 張、已註銷 8 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第046067號 | 優妙化腸溶微粒膠囊 | AMYLASE、LIPASE、PANCRELIPASE、PROTEASE | 腸溶微粒膠囊劑 | 囊腫性纖維化疾病、慢性胰臟炎、胰臟切除、胃腸繞道手術及因腫瘤引發胰管式膽管阻塞等疾病所導致的胰液分泌不全。 |
| 衛署藥製字第055412號 | 金妙化腸溶微粒膠囊 | LIPASE、PANCRELIPASE、AMYLASE、PROTEASE | 腸溶微粒膠囊劑 | 幫助消化。 |

<details><summary><strong>已註銷</strong>（8 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第002311號</td><td>新滋肝片</td><td>DIASTASE ASPERGILLUS ORYZAE(DIASTASE TAKA)、PANCRELIPASE、PANC…</td><td>1985/08/31</td></tr><tr><td>內衛藥輸字第003521號</td><td>克達健片</td><td>BILE EXTRACT, OX、PANCRELIPASE、CELLULOSE</td><td>1985/08/22</td></tr><tr><td>衛署藥輸字第007271號</td><td>胰脂酵素</td><td>PANCRELIPASE</td><td>1985/09/19</td></tr><tr><td>衛署藥輸字第010867號</td><td>利食妥安膠囊</td><td>PANCRELIPASE、DIASTASE、PEPSIN、PEPSIN、PANCREATIN (DIASTASE VER…</td><td>2003/12/29</td></tr><tr><td>衛署藥輸字第013850號</td><td>克達健錠</td><td>CELLULOSE、PANCRELIPASE、BILE EXTRACT, OX</td><td>1988/06/16</td></tr><tr><td>衛署藥輸字第013926號</td><td>增滋康錠</td><td>PANCRELIPASE、DIASTASE ASPERGILLUS ORYZAE(DIASTASE TAKA)、PEPS…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第017263號</td><td>平胰素膠囊</td><td>PANCRELIPASE</td><td>1996/07/24</td></tr><tr><td>衛署藥輸字第022643號</td><td>胰酵素</td><td>PANCRELIPASE</td><td>2014/01/28</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

**藥物交互作用**（共 18 項，均為中度）：

| 交互藥物 | 等級 | 說明 |
|---------|------|------|
| Acarbose、Miglitol | 中度 | Alpha-葡萄糖苷酶抑制劑，可能相互削弱療效 |
| Folic acid、Levomefolic acid、Leucovorin、Levomefolic acid (calcium) | 中度 | 葉酸及其衍生物，Pancrelipase 可能影響葉酸吸收 |
| Iron、Ferrous fumarate、Ferrous gluconate、Ferrous sulfate anhydrous、Iron protein succinylate | 中度 | 各類鐵劑，消化酵素可能影響鐵的腸道吸收 |
| Aluminum hydroxide、Calcium carbonate、Magaldrate、Magnesium hydroxide、Sodium bicarbonate | 中度 | 制酸劑，可能改變腸道 pH 而影響酵素活性 |
| Glycerol phenylbutyrate | 中度 | 尿素循環代謝劑 |
| Quinapril | 中度 | ACE 抑制劑，胰蛋白酶可能影響其吸收 |

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.99%），但全數臨床試驗與文獻資料庫查詢均無結果（證據等級 L5），且 Pancrelipase 作為口服消化酵素，其作用局限於腸腔，與核DNA異常所致粒線體氧化磷酸化障礙的基因病因之間缺乏合理的直接藥理連結，現階段不具備推進的科學依據。

**若要推進需要：**
- 補充完整的作用機轉（MOA）資料（建議透過 DrugBank API 查詢 DB00085）
- 評估其他 TxGNN 前 10 項預測中機轉連結較強的候選（如胰臟神經內分泌癌患者的外分泌不全支持療法，rank 10）
- 尋找消化酵素補充對粒線體代謝疾病患者營養吸收影響的前臨床或觀察性研究
- 確認是否存在粒線體疾病合併胰腺外分泌不全的臨床共病文獻，作為間接佐證

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」寫「解脂」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

