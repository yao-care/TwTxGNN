---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol：從口腔殺菌與咽喉炎到脊髓馬尾症候群（預測）

## 一句話總結

Amylmetacresol 是口含錠中的局部殺菌成分，原本用於口腔殺菌及咽喉炎。
TxGNN 模型預測它可能對**脊髓馬尾症候群 (Cauda Equina Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 口腔殺菌劑、咽喉炎 |
| 預測新適應症 | 脊髓馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 0／有效複方 4／已註銷 0） |
| 建議決策 | Hold |

<!-- review:begin amylmetacresol-moa-2026-10-03 -->

## Amylmetacresol 的作用

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Amylmetacresol（AMC）是喉嚨含片常用的局部抗菌成分，常與 2,4-二氯苄醇（DCBA）併用；體外試驗顯示兩者都有抗細菌（殺菌與抑菌）、抗真菌與抗病毒的性質。（[仿單](https://www.medicines.org.uk/emc/product/5606/smpc)）
- 兩種成分合併時有協同的抗菌作用，因此合併劑量可以較低。（[仿單](https://www.medicines.org.uk/emc/product/5606/smpc)）
- 體外試驗中，接觸 1 分鐘就能殺死部分引起喉嚨痛的細菌，例如 Streptococcus pyogenes、Staphylococcus aureus、Haemophilus influenzae、Moraxella catarrhalis；接觸 1–2 分鐘對 A 型流感病毒、呼吸道融合病毒、冠狀病毒等有套膜病毒也有作用。（[仿單](https://www.medicines.org.uk/emc/product/5606/smpc)）
- 臨床試驗中，這類含片能減輕喉嚨痛與吞嚥困難，約 5 分鐘開始見效、最長可維持 2 小時。（[仿單](https://www.medicines.org.uk/emc/product/5606/smpc)）
- 英國仿單的藥物動力學段寫「None available」，也就是沒有提供吸收與代謝資料。（[仿單](https://www.medicines.org.uk/emc/product/5606/smpc)）

**來源**：[英國 emc：Strepsils Honey and Lemon（amylmetacresol 0.6 mg＋2,4-dichlorobenzyl alcohol 1.2 mg）產品特性摘要（SmPC）§5.1、§5.2](https://www.medicines.org.uk/emc/product/5606/smpc)；查閱日期 2026-10-03。

---

<!-- review:end amylmetacresol-moa-2026-10-03 -->

<!-- review:begin amylmetacresol-original-indication-combo-2026-10-03 -->

> **查核加註（2026-10-03）**：台灣含 amylmetacresol 的 4 張許可證都是與 2,4-dichlorobenzyl alcohol 的複方口含錠，「口腔殺菌劑、咽喉炎」是複方的適應症，台灣沒有 amylmetacresol 單方許可證。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end amylmetacresol-original-indication-combo-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Amylmetacresol 是口含錠複方的一部分，屬局部抗菌劑，據報導在咽喉部具有類似局部麻醉的鈉離子通道阻斷作用。

<!-- review:begin amylmetacresol-moa-pk-claim-sodium-channel-2026-10-16 -->

> **查核加註（2026-10-16）**：仿單（Strepsils SmPC §5.1）只寫 amylmetacresol 與 2,4-dichlorobenzyl alcohol 為防腐殺菌劑、體外具抗菌、抗黴菌與抗病毒作用，未記載鈉離子通道阻斷或局部麻醉作用；這屬於文獻中的實驗觀察，不是仿單所載的作用機轉。原文保留。依據：[emc：Strepsils Honey and Lemon（amylmetacresol 0.6 mg＋2,4-dichlorobenzyl alcohol 1.2 mg）SmPC §5.1、§5.2](https://www.medicines.org.uk/emc/product/5606/smpc)。

<!-- review:end amylmetacresol-moa-pk-claim-sodium-channel-2026-10-16 -->

然而，馬尾症候群是腰薦神經根受壓迫所造成的損傷，與咽喉局部殺菌之間並無已知的藥理關聯。這項預測目前僅來自 TxGNN 的圖譜推論，高分可能反映的是知識圖譜中的鄰近關係，而非真實的療效訊號。

此外，該藥為口腔咽喉局部使用，全身暴露量極低，難以在神經根病變部位達到有效濃度。因此，這個預測的合理性**偏低**，需要先有機轉或前臨床證據才值得進一步投入。

<!-- review:begin amylmetacresol-moa-pk-claim-2026-10-03 -->

> **查核加註（2026-10-03）**：仿單只寫 amylmetacresol 是防腐殺菌劑、體外具抗菌（殺菌與抑菌）、抗黴菌與抗病毒作用；藥動學段為「無資料」，「全身暴露量極低」沒有仿單依據。原文保留。依據：[emc：Strepsils Honey and Lemon（amylmetacresol 0.6 mg＋2,4-dichlorobenzyl alcohol 1.2 mg）SmPC §5.1、§5.2](https://www.medicines.org.uk/emc/product/5606/smpc)。

<!-- review:end amylmetacresol-moa-pk-claim-2026-10-03 -->

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 其他候選預測適應症

TxGNN 另預測下列適應症，皆同為 L5、建議 Hold，且均無臨床試驗與文獻：

| 排名 | 預測適應症 | TxGNN 分數 | 備註 |
|------|-----------|-----------|------|
| 2 | 神經源性膀胱（本體論中已標示為過時術語） | 99.96% | 無已知機轉連結 |
| 3 | 腸躁症 (Irritable Bowel Syndrome) | 99.89% | 僅有推測性的局部離子通道調節假說，且藥物全身暴露極低 |
| 4 | 睫狀體疾病 | 99.70% | 藥物無眼科用途 |
| 5 | 全葡萄膜炎 | 99.68% | 殺菌作用無法處理免疫性發炎，亦無法到達眼內組織 |
| 6 | 虹膜疾病 | 99.63% | 可能反映葡萄膜相關疾病在圖譜中的鄰近性 |
| 7 | 感染性前葡萄膜炎 | 99.57% | 抗菌活性看似相關，但無眼內穿透與眼部安全性資料 |
| 8 | 葡萄膜炎 | 99.53% | 無抗發炎或免疫調節證據 |
| 9 | 睫狀體癌 | 99.46% | 無抗腫瘤機轉，高分疑為圖譜假象 |
| 10 | 睫狀體良性腫瘤 | 99.45% | 無機轉與資料支持 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Amylmetacresol 的不重複許可證共 **4 張**：有效單方 0 張、有效複方 4 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥輸字第022195號 | 舒立效口含錠 | DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL)、DYBENAL (DICHLOROBENZY… | 口含錠 | 口腔殺菌劑、咽喉炎。 |
| 衛署藥輸字第022196號 | 舒立效口含錠舒緩蜂蜜檸檬 | AMYLMETACRESOL、DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL) | 口含錠 | 口腔殺菌劑、咽喉炎。 |
| 衛署藥輸字第022197號 | 舒立效口含錠 酷涼薄荷 | MENTHOL、DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL)、AMYLMETACRESOL | 口含錠 | 口腔殺菌劑、咽喉炎。 |
| 衛署藥輸字第024072號 | 舒立效口含錠柑橘維他命Ｃ | AMYLMETACRESOL、DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL)、VITAMIN… | 口含錠 | 口腔殺菌劑、咽喉炎。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有 TxGNN 模型分數支持，沒有臨床試驗、文獻或明確機轉，證據等級均為 L5。
- 預測的疾病（神經、眼部等）與藥物的口咽局部使用差異很大，缺乏合理的藥理路徑。

**若要推進需要：**
- 補齊 Amylmetacresol 的作用機轉資料（MOA），確認鈉離子通道阻斷是否具臨床意義。
- 以前臨床研究驗證其對神經或相關病理模型的作用。
- 評估全身暴露與給藥途徑的可行性（目前為口含錠，與預測疾病部位不相容）。
- 若仍想探索，建議優先從合理性相對較高的候選（如腸躁症）進行文獻與機轉的系統性檢視。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [emc：Strepsils Honey and Lemon SmPC §5.1](https://www.medicines.org.uk/emc/product/5606/smpc) |
| 2026-10-03 | 原適應症屬於複方 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 說作用為干擾細菌細胞膜、全身吸收量極低 | 加註（2026-10-16 修訂，前版保留於紀錄） | [emc：Strepsils Honey and Lemon（amylmetacresol 0.6 mg＋2,4-dichlorobenzyl alcohol 1.2 mg）SmPC §5.1、§5.2](https://www.medicines.org.uk/emc/product/5606/smpc) |
| 2026-10-16 | 機轉寫鈉離子通道阻斷 | 加註 | [emc：Strepsils Honey and Lemon（amylmetacresol 0.6 mg＋2,4-dichlorobenzyl alcohol 1.2 mg）SmPC §5.1、§5.2](https://www.medicines.org.uk/emc/product/5606/smpc) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

