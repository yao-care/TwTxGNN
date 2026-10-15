---
layout: default
title: Amcinonide
parent: 高證據等級 (L1-L2)
nav_order: 26
evidence_level: L2
indication_count: 8
---

# Amcinonide
{: .fs-9 }

證據等級: **L2** | 預測適應症: **8** 個
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

# Amcinonide：從急慢性皮膚病到皮膚炎

## 一句話總結

Amcinonide（胺醯諾耐）是一種外用副腎皮質荷爾蒙（類固醇），原本用於急慢性皮膚病，例如異位性皮膚炎、濕疹、牛皮癬及神經性皮膚炎。
TxGNN 模型預測它可能對**皮膚炎 (Dermatitis)** 有效，
目前有 **20 篇文獻**支持這個方向（含 3 篇雙盲 RCT 或對照研究），但沒有登記中的臨床試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚炎群、皮膚搔癢症、癢疹群、蟲螫、濕疹、苔癬化型濕疹、尿布疹、牛皮癬、富貴手、苔癬、頑癬、紅皮症、圓形脫毛症、日光皮膚炎、股癬、體癬等 |
| 預測新適應症 | 皮膚炎 (Dermatitis) |
| TxGNN 預測分數 | 99.30% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張（有效單方 1／有效複方 0／已註銷 5） |
| 建議決策 | Proceed with Guardrails |

> 說明：本報告以排名第一的預測（外陰倒置性毛囊角化症）無任何臨床或文獻證據，故改以證據最完整的第 7 名預測「皮膚炎」作為主要評估對象。排名較前的各項預測（見結論）均僅有模型預測，建議維持 Hold。「證據等級 L2」是依資料庫的評分結果；實際上，納入的雙盲研究都是 1979–1984 年的小型比較試驗，且未標示為 Phase 2/3 登記試驗，因此證據強度應保守解讀。

## 為什麼這個預測合理？

Amcinonide 是中至高效價的外用糖皮質激素。一般而言，這類藥物會結合糖皮質激素受體，抑制發炎細胞激素與免疫細胞活性，進而減輕皮膚發紅、腫脹與搔癢。目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA），以上說明為此類藥物的通則。

皮膚炎（含濕疹性皮膚炎）本來就在 amcinonide 的既有核准範圍內，例如異位性皮膚炎、接觸性或濕疹性皮膚病。因此這項「預測」較接近對現有用途的支持，而非全新的適應症。

多項早期雙盲比較研究顯示，0.1% amcinonide 乳膏對濕疹性皮膚炎的療效與 halcinonide 相當，且在一項研究中優於 betamethasone valerate。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

資料中共有 20 篇相關文獻，以下依 RCT > Review > Case series 優先列出主要項目（部分文獻無摘要）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7030645](https://pubmed.ncbi.nlm.nih.gov/7030645/) | 1981 | RCT | Cutis | 29 位濕疹性皮膚炎患者，雙盲 2 週，amcinonide 與 halcinonide 乳膏療效相當且皆顯著改善 |
| [391500](https://pubmed.ncbi.nlm.nih.gov/391500/) | 1979 | RCT | Cutis | amcinonide 乳膏與 betamethasone valerate 比較，兩組皆顯著改善，amcinonide 整體改善更明顯 |
| [6383735](https://pubmed.ncbi.nlm.nih.gov/6383735/) | 1984 | Cohort（雙盲平行研究） | Cutis | 33 位急性/亞急性濕疹性皮膚炎患者，amcinonide 與 halcinonide 各評估時點無顯著差異 |
| [820519](https://pubmed.ncbi.nlm.nih.gov/820519/) | 1976 | 雙盲比較研究 | Curr Ther Res | amcinonide 與 betamethasone valerate 用於濕疹樣皮膚病的比較（無摘要） |
| [41730175](https://pubmed.ncbi.nlm.nih.gov/41730175/) | 2026 | Review | Med Lett Drugs Ther | 異位性皮膚炎藥物回顧 |
| [32555122](https://pubmed.ncbi.nlm.nih.gov/32555122/) | 2020 | Review | Med Lett Drugs Ther | 異位性皮膚炎藥物回顧 |
| [6233341](https://pubmed.ncbi.nlm.nih.gov/6233341/) | 1984 | Review | J Am Acad Dermatol | 5 例外用類固醇接觸過敏，其中 1 例僅對 amcinonide 過敏 |
| [2530056](https://pubmed.ncbi.nlm.nih.gov/2530056/) | 1989 | Review | Contact Dermatitis | 外用類固醇過敏性接觸皮膚炎病例，amcinonide 為致敏分子之一 |
| [2964991](https://pubmed.ncbi.nlm.nih.gov/2964991/) | 1988 | Case series | Contact Dermatitis | amcinonide 引起接觸性皮膚炎 |
| [3816214](https://pubmed.ncbi.nlm.nih.gov/3816214/) | 1987 | Case series | Contact Dermatitis | amcinonide 引起接觸性皮膚炎 |
| [2144811](https://pubmed.ncbi.nlm.nih.gov/2144811/) | 1990 | Case series | Contact Dermatitis | amcinonide 引起過敏性接觸皮膚炎 |

其餘文獻多為接觸過敏與類固醇交叉反應的個案報告（如 PMID 1834432、3160532、8462297、10894975、2946521、8449700、1831101、11683835）及接觸皮膚炎鑑別診斷（PMID 39652964），這些文獻主要提示安全性風險，而非療效證據。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Amcinonide 的不重複許可證共 **6 張**：有效單方 1 張、有效複方 0 張、已註銷 5 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第027348號 | "長安"舒捷乳膏1公絲/公克(安適諾寧) | 乳膏劑 | 長安化學工業股份有限公司 | 2029/12/31 | 皮膚炎群、皮膚搔癢症、、癢疹群、蟲螫、濕疹、苔癬化型濕疹、尿布疹、牛皮癬、富貴手、苔癬、頑癬、掌蹠膿？症、紅皮症、圓形脫毛症、紅斑症、汗斑、頭癬、日光皮膚炎、股癬、體癬 |

<details><summary><strong>已註銷</strong>（5 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第023167號</td><td>膚滋乳膏０．１％（安適諾寧）</td><td>AMCINONIDE</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第044950號</td><td>安適乳膏0.1%〝應元〞</td><td>AMCINONIDE</td><td>2010/03/18</td></tr><tr><td>衛署藥輸字第009165號</td><td>安適諾寧</td><td>AMCINONIDE</td><td>1993/06/19</td></tr><tr><td>衛署藥輸字第011689號</td><td>胺醯諾耐粉劑</td><td>AMCINONIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014982號</td><td>安適諾寧</td><td>AMCINONIDE</td><td>1999/09/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜顯示的禁忌疾病**（來自 TxGNN 知識圖譜，並非仿單內容）：第 1 型與第 2 型糖尿病、糖尿病酮酸中毒、青光眼、皮膚萎縮、周邊血管疾病（含間歇性跛行、周邊動脈疾病）、皮膚結核。
- **過敏風險**：文獻多次記載 amcinonide 本身可引起過敏性接觸皮膚炎，且可能與其他外用類固醇（如 budesonide、triamcinolone acetonide）交叉反應。若使用後皮膚炎惡化或不改善，應考慮藥物過敏並做斑貼試驗。
- **藥物交互作用**：共記錄 44 項交互作用，皆為 Minor 等級。已列出的項目主要是降血糖藥物，包括 acarbose、metformin、pioglitazone、sitagliptin、canagliflozin、dapagliflozin、empagliflozin、semaglutide、dulaglutide，以及多種胰島素。糖皮質激素可能影響血糖，糖尿病患者需留意。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**（僅限「皮膚炎」此一預測）

**理由：**
- 皮膚炎屬於 amcinonide 既有的核准使用範圍，且有數項雙盲比較研究支持療效，因此可信度高。不過這些研究年代久遠、樣本小，且並非新適應症。
- 其餘預測（外陰倒置性毛囊角化症、各型扁平苔癬、扁平苔癬類天疱瘡、原發性皮膚 B 細胞淋巴瘤、2-羥乙基甲基丙烯酸酯過敏）目前僅有模型預測，無任何臨床試驗或文獻支持，建議維持 **Hold**。其中皮膚 B 細胞淋巴瘤需腫瘤科與皮膚科專家審查，扁平苔癬類天疱瘡通常需要全身性治療。

**若要推進需要：**
- 補充作用機轉資料（MOA）。
- 若要探索扁平苔癬等新適應症，需先做針對 amcinonide 的文獻回顧或小型前導研究。
- 建立接觸過敏的監測與斑貼試驗建議，並確認糖尿病、青光眼、皮膚萎縮等族群的使用限制。
- 以現行仿單為準，確認台灣有效許可證（乳膏劑）的適應症與警語。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

