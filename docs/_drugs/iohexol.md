---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Iohexol
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

# Iohexol：從造影劑到失眠

## 一句話總結

Iohexol 是非離子性含碘顯影劑，廣泛用於脊椎造影、血管造影、電腦斷層掃描增強造影及泌尿道造影等影像學檢查。
TxGNN 模型預測它可能對**失眠 (insomnia disease)** 有效，
然而目前**無任何臨床試驗或文獻**支持此方向——此預測僅來自知識圖譜推論，缺乏藥理生物學依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影 |
| 預測新適應症 | 失眠 (insomnia disease) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 18 張（有效單方 2／有效複方 2／已註銷 14） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Iohexol 是非離子性三碘苯環顯影劑，其碘原子以共價鍵結合於苯環上，不具游離碘的生物活性。臨床上作為惰性標記物使用——注射後幾乎完全由腎臟以原形排出，不與蛋白質結合，亦不進行代謝轉化，在體內無已知的受體結合或酵素抑制作用。

失眠的病理機轉涉及 GABA 能神經元抑制減弱、褪黑激素分泌異常及下視丘-腦下垂體-腎上腺軸（HPA axis）失調等中樞神經機制。Iohexol 作為親水性大分子顯影劑，無法穿越血腦屏障，亦無任何已知的中樞神經系統受體結合活性，與上述病理機轉完全無交集。

因此，此預測最可能源自 TxGNN 知識圖譜中的間接關聯路徑（例如共病族群或共同研究脈絡），而非真實的藥理連結。此為典型的圖神經網路高分卻低可信度的預測案例。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Iohexol 的不重複許可證共 **18 張**：有效單方 2 張、有效複方 2 張、已註銷 14 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第022865號 | 〝奇異愛爾蘭廠〞安你拍克 注射劑350毫克碘/公撮 | 注射劑 | 奇異亞洲醫療設備股份有限公司 | 2030/04/27 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影。 |
| 衛署藥輸字第022866號 | "奇異愛爾蘭廠" 安你拍克 注射劑300毫克碘/公撮 | 注射劑 | 奇異亞洲醫療設備股份有限公司 | 2030/04/27 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第044709號 | 威能碘注射液300公絲碘/公撮 | IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL) | 注射劑 | 脊椎造影、血管造影、電腦斷層掃描增強造影劑、泌尿道造影。 |
| 衛署藥製字第044720號 | 威能碘注射液350公絲碘/公撮 | TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL | 注射劑 | 脊椎造影、血管造影、電腦斷層掃瞄增強造影劑、泌尿道造影。 |

<details><summary><strong>已註銷</strong>（14 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第014483號</td><td>安你拍克注射劑３００毫克碘/公撮</td><td>IOHEXOL (ANHYDROUS)</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第014484號</td><td>安你拍克注射劑３５０毫克碘/公撮</td><td>IOHEXOL</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第015944號</td><td>安你拍克注射劑１８０毫克碘/公撮</td><td>TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第015975號</td><td>安你拍克注射劑２４０毫克碘/公撮</td><td>TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL</td><td>1995/02/28</td></tr><tr><td>衛署藥輸字第020621號</td><td>安你拍克注射劑１８０毫克碘/公撮</td><td>TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)、IOHEXOL</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第020622號</td><td>安你拍克注射劑２４０毫克碘/公撮</td><td>IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第020740號</td><td>安你拍克注射劑３５０毫克碘/公撮</td><td>IOHEXOL</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第020741號</td><td>安你拍克注射劑３００毫克碘/公撮</td><td>IOHEXOL (ANHYDROUS)、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO…</td><td>1997/08/19</td></tr><tr><td>衛署藥輸字第021651號</td><td>安你拍克注射劑２４０毫克碘／公撮</td><td>IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第021652號</td><td>安你拍克注射劑３００毫克碘／公撮</td><td>IOHEXOL (ANHYDROUS)</td><td>2023/11/15</td></tr><tr><td>衛署藥輸字第021653號</td><td>安你拍克注射劑３５０毫克碘／公撮</td><td>IOHEXOL</td><td>2023/11/16</td></tr><tr><td>衛署藥輸字第021654號</td><td>安你拍克注射劑１８０毫克碘／公撮</td><td>IOHEXOL、TROMETHAMINE ( EQ TO TROMETAMOL)( EQ TO TROMETHAMOL)</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第023241號</td><td>"奇異愛爾蘭廠" 安你拍克 注射劑180毫克碘/公撮</td><td>IOHEXOL</td><td>2025/09/15</td></tr><tr><td>衛署藥輸字第023242號</td><td>"奇異愛爾蘭廠" 安你拍克 注射劑240毫克碘/公撮</td><td>IOHEXOL</td><td>2025/09/15</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

**藥物交互作用**：共記錄 325 筆交互作用，以下列出主要（Major）交互作用中臨床最相關者：

| 交互藥物 | 等級 | 臨床重要性 |
|---------|------|-----------|
| Metformin | Major | 含碘顯影劑可抑制腎小管排泄 Metformin，顯著增加乳酸酸中毒風險，建議造影前暫停使用 |
| Vancomycin | Major | 合用加重腎毒性，需密切監測腎功能及藥物濃度 |
| Amphotericin B | Major | 合用具累加性腎毒性風險 |
| Amphotericin B (lipid complex) | Major | 同 Amphotericin B，腎毒性風險累加 |
| Kanamycin | Major | 胺基醣苷類抗生素與含碘顯影劑合用增加腎毒性 |
| Levofloxacin | Major | 合用可能影響腎臟清除，需監測腎功能 |
| Hydrocortisone | Major | 皮質類固醇與顯影劑合用需注意過敏預防給藥流程及血流動力學 |
| Dexamethasone | Major | 同 Hydrocortisone，為顯影前預防性用藥常見情境 |
| Betamethasone | Major | 同 Hydrocortisone 注意事項 |
| Triamcinolone | Major | 同 Hydrocortisone 注意事項 |

---

## 結論與下一步

**決策：Hold**

**理由：**
Iohexol 是藥理上的惰性顯影劑，無任何中樞神經系統或睡眠調節機轉，與失眠治療缺乏生物學合理性。預測結果為 L5 等級——僅有 TxGNN 圖譜推論，零臨床試驗、零文獻支持，不具任何推進條件。

**若要推進需要：**
- 補充 Iohexol 的作用機轉（MOA）完整資料，確認是否存在任何中樞神經相關活性（目前為 Data Gap，建議查詢 DrugBank API）
- 進行前臨床機轉研究，確認是否有睡眠調節相關受體（GABA-A、褪黑激素受體等）結合活性
- 評估 TxGNN 圖譜推論路徑，釐清高分的來源是否為資料雜訊或間接共病關聯
- 建議優先評估排名 2–10 中較具機轉合理性的其他適應症（如 rheumatoid arthritis 或 tendinitis 均有 Iohexol 實際應用的間接依據）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

