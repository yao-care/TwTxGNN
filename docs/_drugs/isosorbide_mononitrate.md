---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 1
---

# Isosorbide Mononitrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Isosorbide mononitrate：從狹心症到多毛症

## 一句話總結

Isosorbide mononitrate（單硝酸異山梨酯）是長效有機硝酸酯類藥物，原本用於預防狹心症發作。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，
目前**無臨床試驗**、**無文獻**直接支持這個方向，預測純粹來自模型拓樸推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防狹心症發作 |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.995% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Isosorbide mononitrate 屬於有機硝酸酯類藥物，以 NO 供體角色釋放一氧化氮（NO），透過 **NO → cGMP → PKG** 路徑促進血管平滑肌舒張，用於預防狹心症的療效已被廣泛驗證。

從概念上推測，NO 引發的局部血管舒張理論上可改善毛囊微循環，與 minoxidil 誘發多毛症的現象有一定相似性。然而，minoxidil 促進毛髮生長的機轉主要透過開放 K⁺ 通道（而非 NO/cGMP），兩條路徑本質不同，機轉類比十分間接。

目前對於 Isosorbide mononitrate 用於多毛症，**無任何前臨床、臨床試驗或文獻支持**。此預測純粹基於 TxGNN 圖神經網路的知識圖譜拓樸關聯，尚需前臨床實驗驗證其生物學合理性。

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
| 衛部藥陸輸字第000756號 | 單硝酸異山梨酯 | 原料藥結晶性粉末 | 預防狹心症發作。 |
| 衛部藥輸字第026499號 | 稀硝酸異山梨酯 | （粉） | 預防狹心症之發作。 |
| 衛部藥輸字第027723號 | 稀硝酸異山梨酯 | （粉） | 預防狹心症之發作。 |
| 衛署藥輸字第024730號 | 愛心明持續性藥效錠 60 毫克 | 持續性藥效錠 | 預防狹心症發作。 |

---

## 安全性考量

**藥物交互作用**：共收錄 **189 筆**交互作用記錄（來源：DDInter），以下列出主要交互藥物：

| 交互藥物 | 嚴重程度 | 備註 |
|---------|---------|------|
| Bupropion | 中度 (Moderate) | 抗憂鬱/戒菸用藥 |
| Morphine | 中度 (Moderate) | 鴉片類止痛藥 |
| Canagliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Dapagliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Empagliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Ertugliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Dronabinol | 中度 (Moderate) | 大麻素類 |
| Nabilone | 中度 (Moderate) | 大麻素類 |
| Opium | 中度 (Moderate) | 鴉片類 |
| Rosiglitazone | 中度 (Moderate) | TZD 類降血糖藥 |
| Omeprazole | 輕度 (Minor) | 質子幫浦抑制劑 |

> ⚠️ **特別提醒**：Isosorbide mononitrate 與 PDE5 抑制劑（sildenafil、tadalafil 等）合併使用為**已知臨床禁忌**，可能導致嚴重低血壓，規劃任何再利用研究時需嚴格排除此用藥組合。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 TxGNN 模型預測（L5），完全無前臨床或臨床研究支持 Isosorbide mononitrate 用於多毛症治療。機轉連結（NO 血管舒張 → 毛囊微循環）屬於間接推論，且與已知促毛髮生長機轉（K⁺ 通道）不同，生物學合理性待驗證。

**若要推進需要：**
- 補充完整 MOA 資料（從 DrugBank API 查詢 DB01020）
- 執行前臨床毛囊細胞模型研究（毛乳頭細胞體外 NO 刺激實驗）
- 驗證 NO/cGMP 路徑對毛囊生長週期的直接影響
- 評估外用劑型可行性（現有許可劑型為口服及原料藥，全身性低血壓風險限制口服用於皮膚科適應症的可行性）
- 若機轉驗證成功，考慮與 IND 申請前顧問會議（Pre-IND meeting）確認監管路徑

---

