---
layout: default
title: Sulfamerazine
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 4
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Sulfamerazine（磺胺甲嘧啶）：從抗菌劑到眼部感染治療之回顧

## 一句話總結

Sulfamerazine 是傳統磺胺類抗菌劑，TxGNN 預測其可能對結膜炎（conjunctivitis）有治療潛力，歷史文獻支持其曾用於砂眼治療，但所有台灣許可證均已註銷。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 磺胺劑、革蘭氏陽性及陰性菌感染症 |
| 預測新適應症 | 結膜炎（conjunctivitis）、痛風（gout） |
| TxGNN 預測分數 | 0.990（conjunctivitis） |
| 證據等級 | L4（有歷史 PubMed 文獻） |
| 台灣上市 | 所有許可證已註銷 |
| 許可證數 | 40 張（有效單方 0／有效複方 1／已註銷 39） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

### 結膜炎（Conjunctivitis）- TxGNN 分數 0.990

**機轉假說：**
Sulfamerazine 作為磺胺類抗菌劑，可抑制細菌二氫葉酸合成酶，阻斷葉酸合成途徑。此機轉對引起結膜炎的常見細菌具有抑制作用，尤其對砂眼披衣菌（Chlamydia trachomatis）有效。

**文獻支持：**
1. **1972 年 Revue internationale du trachome（PMID: 4563744）**：砂眼化療臨床試驗評估研究，證實 Sulfamerazine 在砂眼治療中的應用。

2. **1947 年 Journal of the Royal Naval Medical Service（PMID: 20248693）**：早期砂眼病例報告，顯示 Sulphamerazine 治療早期砂眼的成效。

3. **1974 年 Archives of Ophthalmology（PMID: 4852056）**：San Xavier Papago 印第安人砂眼五年追蹤研究，記錄了磺胺類藥物在社區砂眼防治中的角色。

### 痛風（Gout）- TxGNN 分數 0.993

**機轉假說：**
雖然 TxGNN 預測分數較高，但目前無直接文獻或機轉支持 Sulfamerazine 治療痛風。此預測可能為假陽性。

## 臨床試驗

目前無進行中或已完成的 Sulfamerazine 治療結膜炎臨床試驗。歷史試驗多為 1970 年代之前的砂眼防治計畫。

## 相關文獻

| PMID | 標題 | 年份 | 相關性 |
|------|------|------|--------|
| 4563744 | Controlled trachoma chemotherapy trial evaluation | 1972 | 高 |
| 20248693 | Early trachoma treated with sulphamerazine | 1947 | 高 |
| 4852056 | Five-year perspective on trachoma | 1974 | 中 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sulfamerazine 的不重複許可證共 **40 張**：有效單方 0 張、有效複方 1 張、已註銷 39 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第027573號 | "聯邦"鐵多拉三種磺胺錠 | SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE、SULFADIAZINE | 錠劑 | 葡萄狀球菌、鏈鎖球菌、肺炎雙球菌、大腸菌、赤痢菌及綠膿菌引起感染症 |

<details><summary><strong>已註銷</strong>（39 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第002472號</td><td>三合治炎片</td><td>SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE、SULFADIAZINE</td><td>2013/10/15</td></tr><tr><td>內衛藥製字第003373號</td><td>複合磺胺錠</td><td>SULFATHIAZOLE、SULFAMERAZINE、SULFADIAZINE</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第006799號</td><td>三磺胺片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007330號</td><td>磺胺多利精片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFATHIAZOLE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007751號</td><td>磺胺保利精顆粒</td><td>SULFADIAZINE、SULFATHIAZOLE、SULFAMERAZINE、SULFISOXAZOLE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第009912號</td><td>胺氯素片</td><td>SULFATHIAZOLE、SULFAMERAZINE、SULFADIAZINE</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第011129號</td><td>三磺片</td><td>SULFADIAZINE、SULFAMERAZINE、SULFAMETHAZINE (SULFADIMIDINE)</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第012066號</td><td>立消寧膠囊</td><td>SULFATHIAZOLE、SULFAMERAZINE、SULFADIAZINE</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第013670號</td><td>治消炎片</td><td>SULFAMERAZINE、SULFATHIAZOLE、BERBERINE HCL、SULFADIAZINE</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第014459號</td><td>消炎片</td><td>BERBERINE HCL、SULFADIAZINE、TALC (FRENCH CHALK)、SULFATHIAZOLE…</td><td>2007/05/09</td></tr><tr><td>內衛藥製字第014867號</td><td>美美消炎片</td><td>BERBERINE HCL、SULFADIAZINE、SULFAMERAZINE、SULFATHIAZOLE</td><td>1998/03/16</td></tr><tr><td>內衛藥輸字第000554號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1985/08/28</td></tr><tr><td>內衛藥輸字第000560號</td><td>磺胺甲嘧啶鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/01/28</td></tr><tr><td>內衛藥輸字第001988號</td><td>消發米拉錚鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/06/04</td></tr><tr><td>內衛藥輸字第002113號</td><td>消發米拉錚</td><td>SULFAMERAZINE</td><td>1986/02/26</td></tr><tr><td>內衛藥輸字第003040號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1986/01/16</td></tr><tr><td>內衛藥輸字第003252號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1985/08/28</td></tr><tr><td>內衛藥輸字第004207號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1986/02/20</td></tr><tr><td>內衛藥輸字第004210號</td><td>磺胺甲嘧啶鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/05/12</td></tr><tr><td>內衛藥輸字第007097號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1986/07/14</td></tr><tr><td>內衛藥輸字第007103號</td><td>磺胺甲嘧啶鈉</td><td>SULFAMERAZINE SODIUM</td><td>1986/07/14</td></tr><tr><td>衛署藥製字第000380號</td><td>泛須如法控注射液</td><td>SULFAMERAZINE SODIUM、SULFADIAZINE SODIUM、SULFISOMIDINE SODIU…</td><td>1991/07/16</td></tr><tr><td>衛署藥製字第005533號</td><td>三磺胺錠</td><td>SULFADIAZINE、SULFATHIAZOLE、SULFAMERAZINE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第006509號</td><td>三磺懸浮液</td><td>SULFADIAZINE、SULFAMETHAZINE (SULFADIMIDINE)、SULFAMERAZINE</td><td>1992/12/10</td></tr><tr><td>衛署藥製字第033874號</td><td>泛須如法控注射液</td><td>SULFAMERAZINE SODIUM、SULFADIAZINE SODIUM、SULFISOMIDINE SODIU…</td><td>2000/08/04</td></tr><tr><td>衛署藥輸字第000225號</td><td>磺胺甲噠/</td><td>SULFAMERAZINE</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第000298號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002114號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004278號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第004570號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第004870號</td><td>磺胺美拉純鈉鹽</td><td>SULFAMERAZINE SODIUM</td><td>1994/06/10</td></tr><tr><td>衛署藥輸字第010343號</td><td>磺胺甲嘧啶</td><td>SULFAMERAZINE</td><td>1992/01/17</td></tr><tr><td>衛署藥輸字第013906號</td><td>美拉磺胺粉劑</td><td>SULFAMERAZINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第013908號</td><td>美拉磺胺粉劑</td><td>SULFAMERAZINE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014642號</td><td>美拉磺胺</td><td>SULFAMERAZINE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第014726號</td><td>美拉磺胺</td><td>SULFAMERAZINE SODIUM</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014765號</td><td>美拉磺胺</td><td>SULFAMERAZINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014771號</td><td>美拉磺胺</td><td>SULFAMERAZINE</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第015043號</td><td>美拉磺胺鈉</td><td>SULFAMERAZINE SODIUM</td><td>1999/09/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**注意：所有 Sulfamerazine 相關許可證均已註銷，最後有效期多在 1990 年代前。**

## 安全性考量

- **警語與禁忌症**：
  - 磺胺類藥物可能引起過敏反應
  - Stevens-Johnson 症候群風險
  - 對磺胺過敏者禁用

- **藥物交互作用**：
  - 可能增強 warfarin 的抗凝血作用
  - 與口服降血糖藥併用需注意低血糖風險

- **特殊族群**：
  - G6PD 缺乏症患者需謹慎使用
  - 妊娠末期避免使用（新生兒核黃疸風險）

## 結論與下一步

**決策：Hold**

**理由：**
雖然歷史文獻支持 Sulfamerazine 在砂眼（披衣菌性結膜炎）治療中的應用，但此藥物在台灣已無有效許可證，且現已有更安全有效的抗生素選擇（如 Azithromycin）。砂眼在台灣已非主要公共衛生問題，重新開發此藥物的臨床價值有限。

**若要推進需要：**
- 重新申請藥品許可證
- 與現代抗生素進行頭對頭比較研究
- 評估成本效益（相較於現有治療選項）
- 考量抗藥性問題

**建議：**
除非有特殊需求（如特定抗藥性菌株治療），否則不建議投入資源開發此藥物的新適應症。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「全部已註銷」 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

