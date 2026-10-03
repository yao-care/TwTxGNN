---
layout: default
title: Tioconazole
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 3
---

# Tioconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tioconazole (治可那唑) - 藥師評估報告

## 一句話總結

Tioconazole 是一種咪唑類抗黴菌藥物，TxGNN 預測其用於外陰陰道炎獲得豐富臨床試驗與文獻支持，實際上這已是其核准適應症的延伸應用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Tioconazole (治可那唑) |
| DrugBank ID | DB01007 |
| 原適應症 | 感受性黴菌引起之局部感染症 |
| 預測新適應症 | 外陰陰道炎 (vulvovaginitis) |
| TxGNN 分數 | 0.992 (排名 13,733) |
| 證據等級 | 2 項臨床試驗、20+ 篇相關文獻 |
| 台灣上市狀態 | 有效許可證（可寧乳膏、蒂可那乳膏） |

<!-- review:begin tioconazole-trosyd-cancelled-overview-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「台灣上市狀態／有效許可證（妥舒乳膏等）」。妥舒乳膏已於 2013-10-08 註銷；目前有效的是意欣可寧乳膏與黃氏蒂可那乳膏。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end tioconazole-trosyd-cancelled-overview-2026-10-03 -->

---

## 為什麼預測合理？

### 機轉分析

Tioconazole 是廣效咪唑類抗黴菌藥物，其作用機轉為抑制真菌細胞膜麥角固醇合成。預測用於外陰陰道炎完全符合其藥理特性：

1. **抗念珠菌活性**：對 Candida albicans 及其他念珠菌屬具高度活性
2. **抗滴蟲活性**：對 Trichomonas vaginalis 也有一定效果
3. **局部應用優勢**：陰道製劑可達到高局部濃度，全身吸收少

### 預測評估

TxGNN 分數 0.992（排名 13,733）看似較低，但這可能是因為此適應症實際上已是該藥物的標準用途，知識圖譜中已有豐富的既有關聯。

---

## 臨床試驗

### 相關臨床試驗

| 試驗編號 | 標題 | 階段 | 狀態 | 收案數 |
|---------|------|------|------|-------|
| NCT03839875 | Gynomax XL Ovule 治療陰道感染 | Phase 4 | 完成 | 116 |
| NCT06056947 | Fenticonazole + Tinidazole + Lidocaine 組合製劑比較試驗 | Phase 3 | 完成 | 577 |

**NCT03839875 試驗摘要**：
- 開放標籤、單臂設計
- 評估念珠菌外陰陰道炎、細菌性陰道炎、滴蟲陰道炎的療效
- 主要終點：完全緩解率

---

## 文獻證據

### 重要文獻精選 (共 20+ 篇)

1. **Clissold SP, Heel RC (1986)** - *Drugs*
   - 經典綜述：Tioconazole 對皮癬菌、酵母菌具廣效活性
   - 臨床試驗證實對陰道念珠菌病療效與其他咪唑類相當或更佳

2. **Quindos G et al. (2025)** - *Expert Review of Anti-Infective Therapy*
   - 最新綜述：探討非侵入性唑類藥物治療外陰陰道念珠菌病
   - Tioconazole 仍為有效選擇之一

3. **Stein GE et al. (1986)** - *Antimicrobial Agents and Chemotherapy*
   - 隨機對照試驗：單劑 6.5% Tioconazole 軟膏 vs 3 日 Clotrimazole
   - 療效相當（84% vs 85% 症狀緩解率）

4. **Sobel JD (1999)** - *Comprehensive Therapy*
   - 外陰陰道炎診治綜述，Tioconazole 列為標準治療選項

5. **Calvo NL et al. (2019)** - *International Journal of Pharmaceutics*
   - 新型 Tioconazole 陰道膜製劑研發，對念珠菌活性優於傳統製劑

---

## 台灣上市情形

Tioconazole 在台灣有外用製劑許可證：

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tioconazole 的不重複許可證共 **6 張**：有效單方 2 張、有效複方 0 張、已註銷 4 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第043149號 | "意欣"可寧乳膏１％ | 乳膏劑 | 意欣國際有限公司 | 2029/08/06 | 感受性黴菌引起之局部感染。 |
| 衛署藥製字第047752號 | "黃氏" 蒂可那乳膏 | 乳膏劑 | 黃氏製藥股份有限公司 | 2031/01/13 | 感受性黴菌引起之局部感染。 |

<details><summary><strong>已註銷</strong>（4 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第027631號</td><td>妥舒乳膏１％（治可那唑）</td><td>TIOCONAZOLE</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第046418號</td><td>"十全" 汰黴乳膏</td><td>TIOCONAZOLE</td><td>2011/02/22</td></tr><tr><td>衛署藥輸字第012674號</td><td>妥喜得粉劑</td><td>TIOCONAZOLE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第024484號</td><td>治可那唑</td><td>TIOCONAZOLE</td><td>2022/06/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**注意**：台灣目前無陰道專用製劑，如需用於外陰陰道炎，需使用現有外用乳膏。

---

## 安全性考量

### 藥物交互作用

Tioconazole 為局部用藥，全身吸收極少，藥物交互作用風險低。

### 常見不良反應

1. 局部刺激感、搔癢（發生率約 5-30%）
2. 燒灼感
3. 紅疹

### 使用注意事項

1. 月經期間應避免使用陰道製劑
2. 可能損壞乳膠保險套與子宮帽
3. 如 3 天後症狀未改善應就醫

---

## 結論

### 預測適應症評估

| 適應症 | TxGNN 分數 | 臨床試驗 | 文獻 | 建議 |
|-------|-----------|---------|------|------|
| 外陰陰道炎 | 0.992 | 2 項 | 20+ 篇 | **建議（證據充足）** |

### 臨床建議

1. **念珠菌性外陰陰道炎**：Tioconazole 是有效的治療選擇
   - 國際上有單劑量 6.5% 陰道軟膏製劑
   - 療效與 Clotrimazole、Miconazole 相當

2. **台灣使用考量**：
   - 目前僅有外用乳膏劑型
   - 若需治療外陰陰道炎，可考慮其他有陰道製劑的咪唑類藥物

3. **優勢**：
   - 可單劑量治療
   - 局部用藥全身副作用少
   - 對多數念珠菌菌株有效

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 知識圖譜預測、ClinicalTrials.gov、PubMed、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市情形表把已註銷的妥舒乳膏列為有效許可證 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「有效許可證（妥舒乳膏等）」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

