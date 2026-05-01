---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Palbociclib
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

The `txgnn-pipeline` skill confirms this is TxGNN context work. The skill focuses on pipeline operations, not report writing — the system prompt provides the complete report format. Proceeding to generate the report.

---

# Palbociclib：從乳癌到甲狀腺功能亢進

## 一句話總結

Palbociclib（IBRANCE/愛乳適）是一種 CDK4/6 抑制劑，原本用於治療荷爾蒙受體（HR）陽性、HER2 陰性的局部晚期或轉移性乳癌（合併內分泌治療）。
TxGNN 模型預測它可能對**甲狀腺功能亢進 (Hyperthyroidism)** 有效，
目前**無臨床試驗**和**無文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HR+/HER2- 局部晚期或轉移性乳癌（合併芳香環轉化酶抑制劑或 fulvestrant） |
| 預測新適應症 | 甲狀腺功能亢進 (Hyperthyroidism) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Palbociclib 是一種 CDK4/6 抑制劑，透過阻斷細胞週期蛋白依賴激酶 4/6（CDK4/6）的活性來抑制腫瘤細胞從 G1 期進入 S 期，其療效在 HR+/HER2- 乳癌中已被多項臨床試驗確立。

從理論角度而言，Palbociclib 抑制 CDK4/6 可能影響甲狀腺濾泡細胞的增殖週期，存在潛在的間接關聯。然而，甲狀腺功能亢進（如 Graves 病或毒性甲狀腺腺瘤）的核心病生理機制為甲狀腺激素合成與分泌的失調，屬於功能性疾病而非典型增殖性疾病，CDK4/6 路徑與其治療無直接已知機轉連結。

此預測目前無任何臨床試驗或文獻佐證，生物學合理性欠缺直接支持。TxGNN 模型可能透過知識圖譜節點的間接計算關聯而產生此預測，但尚不具備轉化研究的基礎條件。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028005號 | 愛乳適膜衣錠75毫克 | 膜衣錠 | (1) 對於荷爾蒙受體為陽性、第二型人類表皮生長因子接受體(HER2)呈陰性之局部晚期或轉移性乳癌之婦女或男性，IBRANCE 可與芳香環轉化酶抑制劑合併使用... |
| 衛部藥輸字第028006號 | 愛乳適膜衣錠100毫克 | 膜衣錠 | (1) 對於荷爾蒙受體為陽性、第二型人類表皮生長因子接受體(HER2)呈陰性之局部晚期或轉移性乳癌之婦女或男性，IBRANCE 可與芳香環轉化酶抑制劑合併使用... |
| 衛部藥輸字第028007號 | 愛乳適膜衣錠125毫克 | 膜衣錠 | (1) 對於荷爾蒙受體為陽性、第二型人類表皮生長因子接受體(HER2)呈陰性之局部晚期或轉移性乳癌之婦女或男性，IBRANCE 可與芳香環轉化酶抑制劑合併使用... |

> 總計 18 張許可證（另包含膠囊劑及注射劑劑型），上表僅列出部分代表性許可證。

---

## 細胞毒性

Palbociclib 為抗腫瘤藥物（原適應症含乳癌，屬 CDK4/6 標靶治療），本章節適用。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（CDK4/6 抑制劑） |
| 骨髓抑制風險 | 高（嗜中性白血球減少為最常見不良反應，Grade 3/4 發生率顯著，治療期間需定期監測） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC 含白血球分類計數（每次給藥週期開始前及第 14 天）、肝腎功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

**藥物交互作用**（305 筆總交互作用，以下列出主要等級）：

| 交互作用藥物 | 嚴重程度 | 資料來源 |
|------------|---------|---------|
| Clarithromycin | Major | DDInter |
| Cobicistat | Major | DDInter |
| Deferiprone | Major | DDInter |
| Samarium (153Sm) lexidronam | Major | DDInter |
| Aprepitant | Moderate | DDInter |
| Dexamethasone | Moderate | DDInter |
| Cimetidine | Moderate | DDInter |
| Simvastatin | Moderate | DDInter |
| Miconazole | Moderate | DDInter |
| Clotrimazole | Moderate | DDInter |

> 完整 305 筆交互作用請查詢 DDInter 資料庫。其餘警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測為純模型輸出（L5），甲狀腺功能亢進的核心病生理（激素合成/分泌失調）與 CDK4/6 抑制機轉無直接關聯，目前零臨床試驗、零文獻，生物學合理性薄弱，不具備進入轉化研究的基礎。

**若要重新評估需要：**
- 基礎研究確認 CDK4/6 在甲狀腺細胞功能調控中的角色（體外/體內實驗）
- 明確的作用機轉資料（MOA，可查詢 DrugBank API）
- 至少一篇探討 CDK4/6 抑制劑與甲狀腺功能關聯的前臨床研究
---

