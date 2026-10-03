---
layout: default
title: Alpha-Tocopherol Succinate
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Alpha-Tocopherol Succinate
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

# Alpha-Tocopherol Succinate：從維他命Ｅ缺乏症到藥物誘發性骨質疏鬆症

## 一句話總結

Alpha-Tocopherol Succinate（維他命Ｅ琥珀酸鹽）是維他命 E 的生物活性酯化形式，台灣核准用於維他命 E 缺乏症、習慣性流產及末梢血行障礙。
TxGNN 模型預測它對**藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)** 可能有效，
惟目前**尚無臨床試驗及文獻**直接支持，屬純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維他命Ｅ缺乏症 |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 49 張（有效單方 0／有效複方 1／已註銷 48） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 alpha-Tocopherol Succinate 詳細的作用機轉資料。根據已知資訊，alpha-tocopherol 是維他命 E 家族中最具生物活性的脂溶性抗氧化劑，其琥珀酸酯形式（succinate）在體內水解後釋出活性 alpha-tocopherol 發揮療效，在維他命 E 缺乏症及末梢血行障礙治療中的效益已獲臨床使用支持。

藥物誘發性骨質疏鬆症（如類固醇、化療藥物所致）的發病機轉中，氧化壓力是重要環節之一：過量活性氧（ROS）可促進破骨細胞活化、抑制成骨細胞功能，進而導致骨密度下降。Alpha-tocopherol 作為強效脂溶性自由基清除劑，理論上可中斷此氧化損傷路徑，緩解骨質流失速率。

然而，目前僅有 TxGNN 模型預測支持此方向，缺乏任何臨床試驗或前臨床研究的直接佐證，機轉合理性有待進一步實驗驗證。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Alpha-Tocopherol Succinate 的不重複許可證共 **49 張**：有效單方 0 張、有效複方 1 張、已註銷 48 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第048160號 | 美可喜膜衣錠 | PYRIDOXINE HCL、TOCOPHEROL-ALPHA-D ACID SUCCINATE、RIBOFLAVIN… | 膜衣錠 | 營養補充。 |

<details><summary><strong>已註銷</strong>（48 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000795號</td><td>維他命Ｅ糖衣錠</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1997/02/26</td></tr><tr><td>內衛藥製字第000796號</td><td>複方維他命Ｅ膠囊</td><td>VITAMIN A PALMITATE、ASCORBIC ACID (VIT C)、RIBOFLAVIN (VIT B2…</td><td>1997/02/12</td></tr><tr><td>內衛藥製字第001846號</td><td>維他命Ｅ膠囊１００ＭＧ</td><td>TOCOPHEROL-ALPHA-DL ACID SUCCINATE</td><td>2000/08/08</td></tr><tr><td>內衛藥製字第003271號</td><td>益樂健Ｅ膠囊</td><td>RIBOFLAVIN (VIT B2)、TOCOPHEROL-ALPHA-DL ACID SUCCINATE、PYRID…</td><td>2000/08/04</td></tr><tr><td>內衛藥製字第003274號</td><td>益樂健Ｅ膠囊</td><td>THIAMINE MONONITRATE、ASCORBIC ACID (VIT C)、VITAMIN A PALMITA…</td><td>2016/09/10</td></tr><tr><td>內衛藥製字第005664號</td><td>益敏朗膠囊</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE、THIAMINE MONONITRATE、ASCOR…</td><td>2017/02/09</td></tr><tr><td>內衛藥製字第008987號</td><td>維他安糖衣片</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第009063號</td><td>維他安糖衣片</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第011796號</td><td>維他命Ｅ糖衣錠５０公絲</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1999/09/22</td></tr><tr><td>內衛藥製字第013305號</td><td>欲必樂膠囊</td><td>PYRIDOXINE HCL、THIAMINE NITRATE、RIBOFLAVIN (VIT B2)、TOCOPHER…</td><td>1989/08/17</td></tr><tr><td>內衛藥輸字第001156號</td><td>維生素Ｅ琥珀酸鈣</td><td>TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第001307號</td><td>維生素戊</td><td>D-ALPHA TOCOPHERYL ACID SUCCINATE</td><td>1985/06/24</td></tr><tr><td>內衛藥輸字第008280號</td><td>維生素戊琥珀酸鹽</td><td>D-ALPHA TOCOPHERYL ACID SUCCINATE</td><td>1986/11/17</td></tr><tr><td>衛署藥製字第002201號</td><td>立克補膜衣錠</td><td>CYANOCOBALAMIN (VIT B12)、ASCORBIC ACID (VIT C)、THIAMINE MONO…</td><td>2016/09/19</td></tr><tr><td>衛署藥製字第004117號</td><td>欲百朗旺膠囊</td><td>VITAMIN A、ASCORBIC ACID (VIT C)、PYRIDOXINE HCL、THIAMINE NITR…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第006639號</td><td>力得朗膠囊</td><td>VITAMIN A ACETATE、RIBOFLAVIN (VIT B2)、PYRIDOXINE(VITAMIN B6)…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第012110號</td><td>益能膠囊１００單位</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1999/10/05</td></tr><tr><td>衛署藥製字第014919號</td><td>益能糖衣錠</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>2015/06/17</td></tr><tr><td>衛署藥製字第015189號</td><td>爽痔膠囊</td><td>LYSOZYME (CHLORIDE)、TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE…</td><td>2003/05/27</td></tr><tr><td>衛署藥製字第040380號</td><td>複方維他命Ｅ膠囊</td><td>ASCORBIC ACID (VIT C)、VITAMIN A PALMITATE、PROSULTIAMINE (THI…</td><td>1998/08/11</td></tr><tr><td>衛署藥製字第040433號</td><td>維生素Ｅ糖衣錠５０公絲</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1998/08/11</td></tr><tr><td>衛署藥輸字第001052號</td><td>維生素戊琥珀酸鹽</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第001411號</td><td>維生素戊琥珀酸鹽</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1993/07/06</td></tr><tr><td>衛署藥輸字第002396號</td><td>維生素戊琥珀酸鈣</td><td>TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第003545號</td><td>維他命Ｅ琥珀酸醯粉末</td><td>TOCOPHEROL-ALPHA ACID SUCCINATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006852號</td><td>維他命Ｅ糖衣錠</td><td>TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-</td><td>1986/06/21</td></tr><tr><td>衛署藥輸字第007080號</td><td>維他命Ｅ糖衣錠２２５國際單位</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第007166號</td><td>捷力旺錠</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE、NYLIDRIN (SULFONATED STYRO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第007859號</td><td>琥珀酸維他命Ｅ</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008074號</td><td>血滿康錠</td><td>SODIUM ASCORBATE、NIACINAMIDE (NICOTINAMIDE)、PYRIDOXINE HCL、T…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第008458號</td><td>斯補滋膜衣錠</td><td>LECITHIN(LECITHOL)、PANTOTHENATE D- CALCIUM、TOCOPHEROL-ALPHA-…</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第008483號</td><td>艾斯釆維他糖衣錠</td><td>VITAMIN D、LIVER DESICCATED、BONE PHOSPHATE、NIACIN (NICOTINIC…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第009419號</td><td>利施樂－福糖衣錠</td><td>TOCOPHEROL-ALPHA-DL ACID SUCCINATE、RUTIN、AESCULUS HIPPOCASTA…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第009615號</td><td>利施樂糖衣錠</td><td>VITAMIN A (PALMITATE)、TOCOPHEROL-ALPHA-DL ACID SUCCINATE、RUT…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第010632號</td><td>維他命Ｅ琥珀酸鈣</td><td>TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-</td><td>1992/07/01</td></tr><tr><td>衛署藥輸字第010735號</td><td>愛樂敏膠囊</td><td>PYRIDOXINE HCL、TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-、R…</td><td>1992/11/11</td></tr><tr><td>衛署藥輸字第010789號</td><td>維他命Ｅ琥珀酸粉</td><td>TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第011451號</td><td>得克健糖衣錠</td><td>VITAMIN A ACETATE、PYRIDOXINE HCL、RIBOFLAVIN (VIT B2)、PANTOTH…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第011681號</td><td>倍力錠</td><td>THIAMINE MONONITRATE、CYANOCOBALAMIN (VIT B12)、ASCORBIC ACID…</td><td>1987/02/25</td></tr><tr><td>衛署藥輸字第011825號</td><td>益克康糖衣錠</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE、PANTOTHENATE D- CALCIUM、CY…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第012758號</td><td>琥珀醯維生素戊</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第013528號</td><td>維生素戊粉劑</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015057號</td><td>維他命Ｅ糖衣錠</td><td>TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015545號</td><td>倍力錠</td><td>RIBOFLAVIN (VIT B2)、NIACINAMIDE (NICOTINAMIDE)、PANTOTHENATE…</td><td>1988/10/15</td></tr><tr><td>衛署藥輸字第016441號</td><td>維生素戊琥珀酸鈣〝衛采〞</td><td>TOCOPHEROL-ALPHA ACID CALCIUM SUCCINATE DL-</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第016859號</td><td>倍力錠</td><td>CYANOCOBALAMIN (VIT B12)、ASCORBIC ACID (VIT C)、THIAMINE MONO…</td><td>2001/07/26</td></tr><tr><td>衛署藥輸字第018997號</td><td>大正綜合維他命糖衣錠</td><td>FOLIC ACID、PYRIDOXINE HCL、TOCOPHEROL-ALPHA-D ACID SUCCINATE、…</td><td>1996/12/30</td></tr><tr><td>衛署藥輸字第019713號</td><td>普利錠</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE</td><td>2003/09/19</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 所有預測適應症總覽

本次評估屬多適應症候選（TW-DB14001-multi），共涵蓋 10 個 TxGNN 預測方向：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 文獻數 | 建議決策 |
|------|----------|-----------|---------|--------|--------|
| 1 | 藥物誘發性骨質疏鬆症 | 99.997% | L5 | 0 | Hold |
| 2 | 糖尿病性白內障 | 99.992% | L4 | 11 | Hold |
| **3** | **膀胱腫瘤** | **99.991%** | **L3** | **20** | **Research Question** |
| 4 | 強直性白內障 | 99.991% | L5 | 0 | Hold |
| 5 | 不成熟白內障 | 99.991% | L4 | 1 | Hold |
| 6 | 成熟白內障 | 99.991% | L5 | 0 | Hold |
| 7 | 第 2 型糖尿病相關白內障 | 99.991% | L5 | 0 | Hold |
| 8 | 顱縫早閉相關白內障 | 99.991% | L5 | 0 | Hold |
| **9** | **皮質性白內障** | **99.990%** | **L3** | **9** | **Research Question** |
| 10 | 核性老年性白內障 | 99.990% | L4 | 1 | Hold |

**最具研究潛力的兩個方向**：

**膀胱腫瘤（化學預防）**：L3 證據，含 1 篇大型 RCT（ATBC 研究次要終點分析）及 1 篇 Meta-analysis，並有多項前瞻性世代研究，是本次評估中文獻最豐富、證據層次最高的方向。

**皮質性白內障**：L3 證據，含 2 篇 RCT（ATBC 研究、Linxian 介入試驗）及動物劑量反應研究，有直接的人體介入試驗支持，機轉亦最為明確。

---

## 膀胱腫瘤方向補充文獻（最高優先）

由於膀胱腫瘤（Rank 3）具備最高等級的現有文獻，以下列出主要參考文獻供決策參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [11142528](https://pubmed.ncbi.nlm.nih.gov/11142528/) | 2000 | RCT | Cancer Causes & Control | ATBC 大型 RCT 次要終點：alpha-tocopherol 補充對尿路癌症發生率與死亡率的影響分析 |
| [25905583](https://pubmed.ncbi.nlm.nih.gov/25905583/) | 2015 | Meta-analysis | Scientific Reports | 劑量反應 Meta-analysis：維他命 C、D、E 與膀胱癌風險；每增加 10 mg/天 Vit E，相對風險 0.96（90%CI 0.90-1.02） |
| [2790827](https://pubmed.ncbi.nlm.nih.gov/2790827/) | 1989 | Cohort | Cancer Research | 血清 alpha-tocopherol 與後續膀胱癌發展的前瞻性研究，25,802 人追蹤 12 年 |
| [18478342](https://pubmed.ncbi.nlm.nih.gov/18478342/) | 2008 | Case-control | Cancer Causes & Control | 血漿維他命 E（alpha-tocopherol 與 gamma-tocopherol）與膀胱癌風險的病例對照分析 |
| [12434284](https://pubmed.ncbi.nlm.nih.gov/12434284/) | 2002 | Cohort | British Journal of Cancer | ATBC 世代研究：蔬果攝取、類胡蘿蔔素及維他命與膀胱癌風險，追蹤 27,111 名男性吸菸者 |
| [1877596](https://pubmed.ncbi.nlm.nih.gov/1877596/) | 1991 | Nested Case-control | Am J Epidemiology | 芬蘭大型巢式病例對照研究：血清 alpha-tocopherol 與多種低發生率癌症風險 |
| [3567886](https://pubmed.ncbi.nlm.nih.gov/3567886/) | 1987 | Animal | Cancer Letters | 大鼠膀胱致癌模型：alpha-tocopherol 對 BBN 誘發之膀胱癌的修飾效應 |

---

## 皮質性白內障方向補充文獻（次高優先）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [9527321](https://pubmed.ncbi.nlm.nih.gov/9527321/) | 1997 | RCT | Acta Ophthalmologica | ATBC 長期補充試驗：alpha-tocopherol 或 beta-carotene 補充與白內障盛行率及嚴重度 |
| [8363468](https://pubmed.ncbi.nlm.nih.gov/8363468/) | 1993 | RCT | Arch Ophthalmology | Linxian 介入試驗：維他命/礦物質補充對老年性白內障風險的影響（兩項干預試驗） |
| [8512984](https://pubmed.ncbi.nlm.nih.gov/8512984/) | 1993 | Cohort | Epidemiology | Baltimore 老化縱貫研究：血漿抗氧化劑（包含 alpha-tocopherol）與皮質性及核性白內障風險 |
| [7843899](https://pubmed.ncbi.nlm.nih.gov/7843899/) | 1995 | Cohort | Invest Ophthalmol Vis Sci | 血清類胡蘿蔔素與 tocopherol 濃度與核性及皮質性混濁嚴重度的相關性 |
| [21620831](https://pubmed.ncbi.nlm.nih.gov/21620831/) | 2011 | Animal | Exp Eye Research | 大鼠 UV 誘發白內障模型：alpha-tocopherol 保護效果的劑量反應關係 |

---

## 結論與下一步

**決策（主要預測，Rank 1）：Hold**

**理由：**
TxGNN 對藥物誘發性骨質疏鬆症的預測分數雖達 99.997%，但完全缺乏臨床試驗及文獻支持，證據等級僅 L5。在本次評估的 10 個預測適應症中，**膀胱腫瘤（化學預防）**及**皮質性白內障**具備 L3 證據，更值得優先投入研究資源。

**若要推進藥物誘發性骨質疏鬆症方向，需要：**
- 取得完整作用機轉資料（查詢 DrugBank API，DrugBank ID: DB14001）
- 進行系統性文獻回顧，確認 alpha-tocopherol 與骨代謝的間接機轉證據
- 執行前臨床動物實驗（如類固醇誘發骨鬆模型）驗證保護效果

**建議優先評估的替代方向：**
- **膀胱腫瘤（化學預防）**：Rank 3，L3 證據，含 RCT + Meta-analysis，可直接規劃「Alpha-Tocopherol 膀胱癌化學預防」系統性回顧
- **皮質性白內障**：Rank 9，L3 證據，含 2 篇 RCT 及動物劑量反應研究，機轉明確，可評估口服 Vit E 補充延緩白內障進程的臨床研究可行性

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表兩張許可證皆已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

