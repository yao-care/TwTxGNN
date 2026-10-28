---
layout: default
title: Pralatrexate
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
monitor_inn: "Pralatrexate"
predicted_indications: ["pleural adenomatoid tumor", "relapsing-remitting multiple sclerosis", "pleural biphasic mesothelioma", "pleural epithelioid mesothelioma", "lymphohistiocytoid mesothelioma", "pericardium cancer", "pleural sarcomatoid mesothelioma", "malignant peritoneal mesothelioma", "well differentiated papillary mesothelioma", "pleural mesothelioma"]
last_modified_at: 2026-10-27
description: "Pralatrexate：預測新適應症為胸膜腺瘤樣瘤 (pleural adenomatoid tumor)（證據等級 L5）。原適應症：治療復發或頑固型周邊T細胞淋巴瘤(PTCL)。適應症依據為腫瘤反應率，目前沒有資料證實無惡化存活期或整體存活期改善等臨床效益"
---

# Pralatrexate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Pralatrexate：抗葉酸代謝藥物 → 胸膜腺瘤樣瘤 (pleural adenomatoid tumor)
{: .text-alpha }

## 一句話總結

Pralatrexate 是一種抗葉酸類（二氫葉酸還原酶抑制劑）抗腫瘤藥物。
TxGNN 模型預測它可能對**胸膜腺瘤樣瘤 (pleural adenomatoid tumor)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療復發或頑固型周邊T細胞淋巴瘤(PTCL)。適應症依據為腫瘤反應率，目前沒有資料證實無惡化存活期或整體存活期改善等臨床效益 |
| 預測新適應症 | 胸膜腺瘤樣瘤 (pleural adenomatoid tumor) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pralatrexate 屬於抗葉酸類藥物，會抑制二氫葉酸還原酶（DHFR），並透過還原型葉酸載體 1（RFC-1）進入細胞，因此理論上可能影響增生活躍的間皮來源細胞。

不過，腺瘤樣瘤屬於良性腫瘤，增生活性低，使用具細胞毒性的藥物，其風險與效益是否合理令人存疑。目前沒有任何臨床或文獻證據支持此用途，預測僅來自模型分數。

另外值得一提的是，資料中同為胸膜間皮來源的其他預測（例如胸膜上皮樣間皮瘤、胸膜間皮瘤）有一項針對無法切除惡性胸膜間皮瘤的 Phase 2 研究，但那些並非本報告的主要預測疾病，不能視為對胸膜腺瘤樣瘤的直接證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Pralatrexate 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第026419號 | 服瘤停注射劑 | 注射劑 | 健喬信元醫藥生技股份有限公司 | 2029/12/27 | 治療復發或頑固型周邊T細胞淋巴瘤(PTCL)。適應症依據為腫瘤反應率，目前沒有資料證實無惡化存活期或整體存活期改善等臨床效益 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗葉酸代謝拮抗劑） |
| 骨髓抑制風險 | 中至高（血小板低下、嗜中性白血球低下、貧血為常見的相關風險） |
| 致吐性分級 | 低至中 |
| 監測項目 | CBC（含分類）、肝腎功能、口腔黏膜狀況 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

細部警語請參考原廠仿單的警語與注意事項。

## 安全性考量

- **藥物交互作用**：共查得 136 筆交互作用紀錄，其中包含嚴重等級者，例如 Deferiprone、Samarium (153Sm) lexidronam；中度等級者包含 Acetylsalicylic acid、Ibuprofen、Diclofenac、Ketorolac、Flurbiprofen、Pyrimethamine、Zidovudine、Chloramphenicol 等（NSAID 類藥物可能影響腎臟排除，需特別留意）。
- **需留意的相關風險**：血小板低下、嗜中性白血球低下、顆粒球缺乏、貧血、腎功能不全與口腔炎，為此藥相關的需注意情況，這些並非來自仿單文字，使用時應仔細評估。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測疾病為良性腫瘤，且沒有任何直接針對它的臨床試驗或文獻，證據等級僅為 L5。
- 細胞毒性藥物用於良性疾病，風險效益比不明確。

**若要推進需要：**
- 取得 Pralatrexate 詳細的作用機轉資料
- 針對胸膜腺瘤樣瘤的前臨床或病例層級研究
- 評估良性疾病使用細胞毒性藥物的風險效益與替代治療（如手術切除）
- 建立血液學與黏膜毒性的監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證數寫 2 張 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

