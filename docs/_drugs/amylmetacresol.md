---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 27
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

# Amylmetacresol：從口腔殺菌/咽喉炎到馬尾症候群

## 一句話總結

Amylmetacresol（舒立效口含錠）是一種局部口腔殺菌劑，在台灣核准用於口腔殺菌及咽喉炎治療。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，
目前**無任何臨床試驗或文獻**支持這個方向，整體屬於純模型預測結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 口腔殺菌劑、咽喉炎 |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 0／有效複方 4／已註銷 0） |
| 建議決策 | Hold |

---

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

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Amylmetacresol 是一種親脂性酚類化合物，作用於口咽黏膜表面，透過干擾細菌細胞膜結構發揮局部殺菌效果。其應用形式為口含錠，藥物主要停留在口腔與咽喉局部，全身吸收量極低。

馬尾症候群是一種由腰椎間盤突出、腫瘤或外傷引起脊髓馬尾神經根受壓的急症，病理機轉涉及神經根壓迫、缺血與局部發炎。Amylmetacresol 作為局部表面抗菌劑，目前**無任何已知的全身性抗發炎、神經保護或解壓機轉**，與馬尾症候群的病理過程缺乏生物學上的合理聯繫。

此預測分數雖高達 99.99%，但 TxGNN 知識圖譜模型的預測結果需以現有文獻與機轉研究交叉驗證。在完全無臨床或基礎研究佐證的情況下，高分數本身不代表臨床可行性，僅代表圖譜結構上存在某種關聯信號，**需謹慎解讀**。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Amylmetacresol 的不重複許可證共 **4 張**：有效單方 0 張、有效複方 4 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥輸字第022195號 | 舒立效口含錠 | DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL)、DYBENAL (DICHLOROBENZY… | 口含錠 | 口腔殺菌劑、咽喉炎。 |
| 衛署藥輸字第022196號 | 舒立效口含錠舒緩蜂蜜檸檬 | AMYLMETACRESOL、DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL) | 口含錠 | 口腔殺菌劑、咽喉炎。 |
| 衛署藥輸字第022197號 | 舒立效口含錠 酷涼薄荷 | MENTHOL、DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL)、AMYLMETACRESOL | 口含錠 | 口腔殺菌劑、咽喉炎。 |
| 衛署藥輸字第024072號 | 舒立效口含錠柑橘維他命Ｃ | AMYLMETACRESOL、DYBENAL (DICHLOROBENZYL 2,4- ALCOHOL)、VITAMIN… | 口含錠 | 口腔殺菌劑、咽喉炎。 |

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Amylmetacresol 為局部口腔用藥，與馬尾症候群（及其餘所有前 10 項預測適應症）均缺乏機轉關聯性，且全部 10 項預測均無任何臨床試驗或文獻支持（均為 L5），現階段不建議推進再利用評估。

**若要推進需要：**
- 補充完整的作用機轉資料（MOA），釐清 Amylmetacresol 是否具有全身性抗發炎或神經相關活性
- 進行體外細胞毒性及神經細胞活性篩選實驗，確認是否有任何臨床前依據
- 重新評估 TxGNN 知識圖譜中產生此預測的圖譜路徑，確認是否為雜訊或有意義的關聯
- 若欲探索 Amylmetacresol 的再利用潛力，建議優先考慮更具生物合理性的方向（如呼吸道感染、口咽黏膜炎等）

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [emc：Strepsils Honey and Lemon SmPC §5.1](https://www.medicines.org.uk/emc/product/5606/smpc) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

