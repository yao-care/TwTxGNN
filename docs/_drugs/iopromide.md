---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 1
---

# Iopromide
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

Using `txgnn-pipeline` to confirm context — this is a TwTxGNN evidence report generation task. The system prompt contains the full output specification. Now generating the report.

---

# Iopromide：從電腦斷層造影到骨關節炎易感性

## 一句話總結

Iopromide（優照維斯）是非離子型碘化顯影劑，原本用於電腦斷層攝影、血管造影術及各類放射診斷程序。
TxGNN 模型預測它可能對**骨關節炎易感性 (Osteoarthritis Susceptibility)** 有效，
但目前**無臨床試驗**且**無相關文獻**支持這個治療方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 電腦斷層攝影、數位化減影血管造影術、靜脈內尿路造影、動脈造影及心血管造影 |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Iopromide 是非離子型碘化顯影劑（nonionic iodinated contrast medium），於影像診斷中經靜脈注射或直接注入體腔（包含關節腔）以增強 X 光或 CT 的對比度，本身不具藥理治療活性。

TxGNN 的預測可能源自知識圖譜中的間接連結：Iopromide 在關節攝影（arthrography）中直接進入關節腔，因此在圖譜中與「骨骼/關節疾病」節點存在解剖位置上的共用節點路徑，模型據此推論其與骨關節炎易感性的關聯。

然而，這是**診斷用途的地理重疊，而非治療機轉的生物學合理性**。目前無任何已知機轉支持 Iopromide 對軟骨代謝、滑膜微環境、軟骨下骨重塑或骨關節炎易感相關基因通路（如 GDF5、ALDH1A2 等）具有任何治療或保護作用。此預測被判定為知識圖譜拓樸鄰近性（topological proximity）所產生的假陽性訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥輸字第016018號 | 優照維斯碘含量３７０毫克/毫升 | 注射劑 | 電腦斷層攝影、數位化減影血管造影術、靜脈內尿路造影、動脈造影、特別是心血管造影及身體空腔部份；成人對比增強乳房攝影... |
| 衛署藥輸字第016019號 | 優照維斯碘含量３００毫克/毫升 | 注射劑 | 電腦斷層攝影、數位化減影血管造影術、靜脈內尿路造影、末梢靜脈造影、動脈造影及身體空腔部份；成人對比增強乳房攝影... |
| 衛署藥輸字第016804號 | 優照維斯碘含量２４０毫克/毫升注射液 | 注射劑 | 電腦斷層攝影、數位化減影血管造影術、靜脈造影、尿路造影、末梢靜脈Ｘ－光造影及身體空腔部份... |

## 安全性考量

**藥物交互作用**（資料庫共收錄 202 筆，以下列出 Major 等級交互作用）：

| 交互作用藥物 | 等級 | 備註 |
|------------|------|------|
| Metformin | Major | 顯影劑使用前後需暫停，以避免顯影劑誘發的腎毒性引發乳酸酸中毒 |
| Amphotericin B（含 lipid complex、cholesteryl sulfate、liposomal 劑型） | Major | 兩藥合用可能加重腎毒性 |
| Vancomycin | Major | 可能增加腎毒性風險 |
| Mesalazine / Balsalazide / Olsalazine / Sulfasalazine | Major | 5-ASA 類藥物與顯影劑合用的腎功能交互作用 |
| Kanamycin / Neomycin / Streptomycin / Polymyxin B | Major | 胺基醣苷類與多黏菌素類抗生素可能疊加腎毒性 |

## 結論與下一步

**決策：Hold**

**理由：**
Iopromide 為純診斷用途的顯影劑，無任何已知治療性藥理機轉。TxGNN 分數達 99.57% 但此高分反映的是知識圖譜拓樸結構（關節攝影與關節疾病節點的共鄰居），而非真實的生物活性關聯。證據等級僅為 L5（純模型預測），無臨床試驗或文獻支持，不具備推進再利用研究的生物學依據。

**若要推進需要：**
- 提出可驗證的藥理學機轉假說（例如：碘化苯環結構是否對軟骨細胞具有任何直接生物活性）
- 前臨床細胞/動物實驗以排除假陽性可能
- 分析 TxGNN 知識圖譜中此預測的完整節點路徑，確認是否為非特異性拓樸連結所致

---

