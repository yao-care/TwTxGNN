---
layout: default
title: Carbenoxolone
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-16
description: "Carbenoxolone：預測新適應症為非症候群型食道畸形 (Non-syndromic Esophageal Malformation)（證據等級 L5）。原適應症：胃潰瘍"
---

# Carbenoxolone
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

# Carbenoxolone：從胃潰瘍到先天性食道畸形（非症候群型）

## 一句話總結

Carbenoxolone（卡變諾）是甘草次酸的衍生物，原本用於胃潰瘍、十二指腸潰瘍及口內潰瘍的治療。
TxGNN 模型預測它可能對**非症候群型食道畸形 (Non-syndromic Esophageal Malformation)** 有效，
但目前**沒有任何臨床試驗與直接相關文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃潰瘍（單方許可證中，目前仍有效者為口內潰瘍：緩解及治療口內潰瘍） |
| 預測新適應症 | 非症候群型食道畸形 (Non-syndromic Esophageal Malformation) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 29 張（有效單方 5／有效複方 0／已註銷 24） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。就一般藥理知識，carbenoxolone 是甘草次酸衍生物，可促進胃黏液分泌，並具有抑制間隙連接（gap junction）與 11-β-羥類固醇脫氫酶（11-β-HSD）的作用。

原適應症為消化道潰瘍與口腔黏膜潰瘍，屬於黏膜保護的範疇。然而，先天性食道畸形是胚胎發育期的結構異常，與黏膜保護或潰瘍癒合沒有已知的機轉關聯。因此，此高分預測目前**缺乏機轉上的支持**，僅來自知識圖譜的關聯推論。

其他排名較高的預測（如維生素缺乏症、生物素代謝疾病、絲蟲病、膽管疾病、膽管腫瘤、黑癬）同樣沒有臨床或前臨床證據，也沒有合理的作用機轉連結。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首位預測（非症候群型食道畸形）目前無相關文獻。

附帶說明：排名第 5 的「膽管疾病」僅有 1 篇文獻，內容如下，但它探討的是 sucralfate 而非 carbenoxolone，因此不構成直接證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1715672](https://pubmed.ncbi.nlm.nih.gov/1715672/) | 1991 | 動物研究 | The American Journal of Medicine | 豬膽管結紮後會造成食道部潰瘍，sucralfate 可延長存活並促進潰瘍癒合；與 carbenoxolone 無直接關係 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Carbenoxolone 的不重複許可證共 **29 張**：有效單方 5 張、有效複方 0 張、已註銷 24 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第021999號 | "優良"炎立治口內軟膏（卡變諾） | 軟膏劑 | 優良化學製藥股份有限公司 | 2028/08/19 | 緩解及治療口內潰瘍 |
| 衛署藥製字第026232號 | "西德有機"口舒爽口內膏２０毫克（卡變諾） | 口內膏 | 西德有機化學藥品股份有限公司 | 2028/09/17 | 口內炎性潰瘍、糜爛性口疾患、潰瘍性之口內傷害 |
| 衛署藥製字第043620號 | 妙潔口內膏２０公絲/公克（卡變諾）〝溫士頓〞 | 口內膏 | 溫士頓醫藥股份有限公司 | 2030/03/21 | 口內炎性潰瘍、糜爛性口疾患、潰瘍性之口內傷害。 |
| 衛署藥製字第046353號 | "黃氏" 治炎寧口內膏 | 口內膏 | 黃氏製藥股份有限公司 | 2029/06/28 | 口內炎性潰瘍、糜爛性口疾患、潰瘍性之口內傷害。 |
| 衛部藥製字第059858號 | 明炎優口內膏2% | 口內膏 | 天下生物科技股份有限公司 | 2028/02/01 | 口內炎性潰瘍、糜爛性口疾患、潰瘍性之口內傷害。 |

<details><summary><strong>已註銷</strong>（24 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第010499號</td><td>加爽朗錠</td><td>CARBENOXOLONE SODIUM</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第010842號</td><td>潰佳錠</td><td>CARBENOXOLONE SODIUM</td><td>1999/08/20</td></tr><tr><td>衛署藥製字第013117號</td><td>卡變諾錠</td><td>CARBENOXOLONE SODIUM</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第014186號</td><td>卡變諾錠</td><td>CARBENOXOLONE SODIUM</td><td>1990/08/13</td></tr><tr><td>衛署藥製字第014872號</td><td>卡變諾錠”人生”　　　　　　　　　　　　　　　　　　　　　　 C</td><td>CARBENOXOLONE SODIUM</td><td>1989/08/17</td></tr><tr><td>衛署藥製字第020288號</td><td>佳胃朗錠（卡變諾）</td><td>CARBENOXOLONE SODIUM</td><td>2023/07/24</td></tr><tr><td>衛署藥製字第020980號</td><td>優胃瘍錠（卡變諾）</td><td>CARBENOXOLONE SODIUM</td><td>1989/10/16</td></tr><tr><td>衛署藥製字第025472號</td><td>克潰隆錠５０公絲（卡變諾）</td><td>CARBENOXOLONE SODIUM</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第027431號</td><td>益潰康錠５０公絲（卡變諾）</td><td>CARBENOXOLONE SODIUM</td><td>1989/09/29</td></tr><tr><td>衛署藥製字第032363號</td><td>卡變諾錠５０公絲</td><td>CARBENOXOLONE SODIUM</td><td>2019/05/14</td></tr><tr><td>衛署藥輸字第002783號</td><td>腸嘉實多膠囊</td><td>CARBENOXOLONE SODIUM、SODIUM BICARBONATE ( EQ TO SODIUM HYDRO…</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第002784號</td><td>胃嘉實多錠</td><td>CARBENOXOLONE SODIUM</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第003875號</td><td>佳胃賜爾顆粒</td><td>MAGNESIUM TRISILICATE、CARBENOXOLONE SODIUM、ALUMINUM HYDROXID…</td><td>1988/06/22</td></tr><tr><td>衛署藥輸字第003876號</td><td>佳胃賜爾錠</td><td>ALUMINUM HYDROXIDE (ALUMINA HYDRATED)、CARBENOXOLONE SODIUM、M…</td><td>1988/06/22</td></tr><tr><td>衛署藥輸字第004036號</td><td>羧丙醯氧油酸鈉鹽</td><td>CARBENOXOLONE SODIUM</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第004682號</td><td>/苯索酮鈉</td><td>CARBENOXOLONE SODIUM</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第011642號</td><td>保胃壯錠５０公絲</td><td>CARBENOXOLONE SODIUM</td><td>1986/11/11</td></tr><tr><td>衛署藥輸字第011643號</td><td>杜潰能膠囊</td><td>CARBENOXOLONE SODIUM</td><td>1986/12/23</td></tr><tr><td>衛署藥輸字第015364號</td><td>保胃壯錠５０公絲</td><td>CARBENOXOLONE SODIUM</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015474號</td><td>杜潰能膠囊</td><td>CARBENOXOLONE SODIUM</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015832號</td><td>遏保勝膠漿</td><td>CARBENOXOLONE SODIUM</td><td>1988/02/01</td></tr><tr><td>衛署藥輸字第016233號</td><td>克寶勝膠漿</td><td>CARBENOXOLONE SODIUM</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第017076號</td><td>倍爾癒膠漿２％Ｗ/Ｗ</td><td>CARBENOXOLONE SODIUM</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第020059號</td><td>可必勝凝膠</td><td>CARBENOXOLONE SODIUM</td><td>2009/12/10</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

另外，本次資料查詢中未發現藥物交互作用紀錄。這代表資料庫查無資料，並不等於沒有交互作用。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測雖然分數很高（99.999%），但沒有臨床試驗、沒有文獻，機轉上也找不到合理連結，證據等級僅為 L5。
- 預測疾病為先天性結構畸形，與藥物的黏膜保護作用性質差異大，現階段不建議投入資源推進。

**若要推進需要：**
- 補齊 carbenoxolone 的作用機轉資料（MOA）。
- 進行文獻與前臨床研究檢索，確認是否有任何食道發育或食道黏膜相關的證據。
- 釐清此預測是否為知識圖譜的雜訊，並與排名較後的預測（如膽管疾病）交叉比對。
- 評估臨床上是否存在可治療的目標族群與合理的給藥途徑（目前途徑相容性尚未評估）。
- 補充安全性資料（警語、禁忌症）；已知此藥有影響電解質與血壓的風險，須以原廠仿單為準。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

