---
layout: default
title: Levamisole
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
monitor_inn: "levamisole"
predicted_indications: ["drug-induced osteoporosis", "benign neoplasm of tongue", "cervical neuroblastoma", "benign neoplasm of buccal mucosa", "epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of floor of mouth", "schwannoma of jugular foramen", "benign neoplasm of hypopharynx", "inner ear neoplasm"]
last_modified_at: 2026-10-23
description: "Levamisole：預測新適應症為藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：驅除蛔蟲、鉤蟲、糞圓蟲"
---

# Levamisole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Levamisole：從驅蟲治療到藥物誘發性骨質疏鬆
{: .text-alpha }

## 一句話總結

Levamisole（左旋咪唑）在台灣核准的主要用途是驅除蛔蟲、鉤蟲與糞圓蟲，過去也曾作為氟嘧啶類藥物的輔助抗腫瘤藥。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)** 有效，但目前**沒有臨床試驗，也沒有直接研究此疾病的文獻**，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 驅除蛔蟲、鉤蟲、糞圓蟲 |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 4 張／共 21 張） |
| 許可證數 | 21 張（有效單方 4／有效複方 0／已過期 1／已註銷 16） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Levamisole 是一種免疫調節劑兼驅蟲藥，與骨代謝或糖皮質素引起的骨質流失之間沒有已知的機轉關聯。

這項預測的分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據，也無法由現有資料找出合理的生物學路徑。分數雖高，但不應被視為療效證據。在現有資料下，這個預測的可信度有限，應視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（本次預測的排名較後面幾項候選適應症雖有少量文獻，但皆屬其他疾病，並未直接研究藥物誘發性骨質疏鬆。）

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Levamisole 的不重複許可證共 **21 張**：有效單方 4 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 16 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第023387號 | "生達"立得舒膠衣錠（樂瓦米索） | 膜衣錠 | 生達化學製藥股份有限公司 | 2028/05/15 | 驅除蛔蟲、鈎蟲、糞圓蟲 |
| 衛署藥製字第025466號 | "成大"力維舒錠40毫克（樂瓦米索) | 錠劑 | 成大藥品股份有限公司 | 2029/05/25 | 驅腸蟲（蛔蟲、鉤蟲、糞圓蟲） |
| 衛署藥製字第025725號 | "新喜"代卡力錠５０毫克（樂瓦米索） | 錠劑 | 新喜國際企業股份有限公司 | 2029/05/25 | 驅蟲劑（驅除蛔蟲、鉤蟲） |
| 衛署藥製字第035158號 | 第卡舒錠１５０公絲（樂瓦米索） | 錠劑 | 新喜國際企業股份有限公司 | 2031/04/30 | 蛔蟲、鉤蟲、糞圓蟲等驅蟲劑、復發性鵝口瘡治療劑、刺激身體產生免疫性、增加人體免疫力 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥陸輸字第000468號</td><td>鹽酸利惟嘧嗦</td><td>Levamisole Hydrochloride</td><td>2026/09/13</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（16 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第021331號</td><td>利凡得膜衣錠（樂瓦米索）</td><td>LEVAMISOLE (HCL)</td><td>2003/04/25</td></tr><tr><td>衛署藥製字第021459號</td><td>"英城"奧可迪錠（樂瓦米索）</td><td>TETRAMISOLE L(-)- HCL (LEVAMISOLE HCL)</td><td>2023/07/05</td></tr><tr><td>衛署藥製字第022837號</td><td>發密索錠（樂瓦米索）</td><td>TETRAMISOLE L(-)- (LEVAMISOLE)</td><td>2000/08/25</td></tr><tr><td>衛署藥製字第023425號</td><td>第卡舒錠（樂瓦米索）</td><td>TETRAMISOLE L(-)- (LEVAMISOLE)</td><td>1992/10/17</td></tr><tr><td>衛署藥製字第023560號</td><td>舒可錠（樂瓦米索）</td><td>TETRAMISOLE L(-)- HCL (LEVAMISOLE HCL)</td><td>2013/10/01</td></tr><tr><td>衛署藥製字第023876號</td><td>樂利得錠（樂瓦米索）</td><td>LEVAMISOLE (HCL)</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第024387號</td><td>迪卡斯糖衣錠（樂瓦米索）</td><td>LEVAMISOLE (HCL)</td><td>2016/09/07</td></tr><tr><td>衛署藥製字第024946號</td><td>染必舒錠５０公絲（樂瓦米索）</td><td>LEVAMISOLE (HCL)</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第026286號</td><td>得克蟲錠劑４０公絲（樂瓦米索）</td><td>LEVAMISOLE (HCL)</td><td>1992/02/13</td></tr><tr><td>衛署藥輸字第001886號</td><td>鹽酸提都拉咪則</td><td>TETRAMISOLE L(-)- HCL (LEVAMISOLE HCL)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005827號</td><td>得可利錠（兒童用）</td><td>Levamisole</td><td>2020/04/16</td></tr><tr><td>衛署藥輸字第006690號</td><td>得可利膜衣錠（成人用）</td><td>LEVAMISOLE (HCL)</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第007699號</td><td>（－）２，３，５，６－四氫基６－苯基異二氮二烯伍圜－〔２，１</td><td>TETRAMISOLE L(-)- HCL (LEVAMISOLE HCL)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第008553號</td><td>四氫乙/唑鹽酸</td><td>TETRAMISOLE L(-)- HCL (LEVAMISOLE HCL)</td><td>1999/09/22</td></tr><tr><td>衛署藥陸輸字第000082號</td><td>鹽酸左旋咪唑</td><td>TETRAMISOLE L(-)- HCL (LEVAMISOLE HCL)</td><td>2010/09/27</td></tr><tr><td>衛署藥陸輸字第000172號</td><td>鹽酸利惟嘧嗦</td><td>TETRAMISOLE L(-)- HCL (LEVAMISOLE HCL)</td><td>2019/03/15</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 73 筆交互作用紀錄，列舉的部分包括：
  - 嚴重（Major）：Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib、Certolizumab pegol、Cladribine
  - 中度（Moderate）：Ethanol、Warfarin、Zidovudine、Azathioprine、Chloramphenicol、Alemtuzumab、Anakinra，以及多種疫苗與免疫抑制劑

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測疾病沒有任何臨床試驗或直接相關文獻，證據等級僅為 L5。
- 缺乏作用機轉資料，也找不到 levamisole 與骨代謝的合理關聯。

**若要推進需要：**
- 補充 levamisole 的作用機轉資料，評估其與骨代謝的可能路徑
- 進行前臨床研究（如糖皮質素誘發骨質流失的動物模型）
- 評估與免疫抑制劑、糖皮質素併用時的安全性（交互作用多為中度至嚴重）
- 確認文獻回顧中是否有任何直接研究此疾病的報告
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

