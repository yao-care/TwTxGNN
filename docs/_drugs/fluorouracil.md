---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 1
---

# Fluorouracil
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

# Fluorouracil（5-FU）：從消化道腫瘤到陰道葡萄狀胚胎型橫紋肌肉瘤

---

> ## ⚠️ Evidence Pack 資料品質警示
>
> 本報告的核心藥物為 **Fluorouracil（5-FU，DrugBank DB00544）**，但 `taiwan_regulatory.licenses` 及 `drug.original_indications` 所載的許可證與適應症資料，實際上屬於 **曲斯若（Trastuzumab 生物相似藥）** 的核准內容，並非 Fluorouracil。這是資料擷取管道的對應錯誤。
>
> - **台灣上市狀態（✓ 已上市）與許可證總數（20 張）** 視為合理，但個別許可證細節不可直接引用。
> - 正確的 5-FU 台灣許可資訊請逕查詢 [TFDA 藥品查詢系統](https://www.fda.gov.tw/)。
> - 本報告後續的「台灣上市資訊」章節將標示錯誤內容並說明原因。

---

## 一句話總結

Fluorouracil（5-FU）是臨床使用超過 60 年的 Fluoropyrimidine 類抗代謝化療藥，廣泛應用於大腸直腸癌、胃癌、乳癌等消化道及固態腫瘤的標準化療方案。
TxGNN 模型預測它可能對**陰道葡萄狀胚胎型橫紋肌肉瘤 (Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina)** 有效，
然而目前**無任何臨床試驗或文獻**支持此特定亞型，此預測屬純模型預測（L5 等級），建議維持 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ⚠️ 許可證資料錯誤（顯示為 Trastuzumab 適應症）；5-FU 已知核准適應症包含大腸直腸癌、胃癌、乳癌等 |
| 預測新適應症 | 陰道葡萄狀胚胎型橫紋肌肉瘤 (Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張（詳見資料品質警示） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前 Evidence Pack 中 Fluorouracil 的作用機轉（MOA）標記為 Data Gap。根據已知藥理學知識，5-FU 屬於 **Fluoropyrimidine 抗代謝藥物**，其主要機轉為：**抑制胸苷酸合酶（Thymidylate Synthase, TS）**，阻斷去氧尿苷一磷酸（dUMP）轉換為去氧胸苷一磷酸（dTMP），中斷 DNA 合成；同時，5-FU 代謝產物（FUTP）可嵌入 RNA，干擾 RNA 加工與蛋白質合成。這種廣效的核酸代謝干擾機轉，使 5-FU 對所有快速增殖的腫瘤細胞具有潛在的細胞毒性。

陰道葡萄狀胚胎型橫紋肌肉瘤（Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina）是一種極罕見的兒童期婦科惡性腫瘤，腫瘤細胞具有快速增殖特性，理論上對抗代謝藥物具有潛在敏感性。從疾病生物學角度看，RMS 與 5-FU 原始適應症（消化道腫瘤）同樣涉及快速分裂的腫瘤細胞群體，機轉上存在間接關聯性。

然而需要特別指出，橫紋肌肉瘤的標準化療方案為 **VAC（Vincristine + Actinomycin-D + Cyclophosphamide）**，5-FU 並非 RMS 任何亞型的一線或標準治療選項。TxGNN 的高分預測可能反映知識圖譜中 5-FU 廣泛的抗腫瘤活性節點連結，而非疾病特異性的直接生物學關聯。此亞型好發於幼兒，且為婦科局部病灶，5-FU 在 RMS 的特殊解剖位置與給藥路徑上亦無文獻支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 台灣上市資訊

> ⚠️ **以下許可證資料為資料管道錯誤所引入的 Trastuzumab 生物相似藥（曲斯若）資訊，並非 Fluorouracil（5-FU）的台灣許可證。** 此列表僅供識別資料錯誤之用，不應作為 5-FU 法規依據引用。

| 許可證號 | 品名 | 劑型 | 備註 |
|---------|------|------|------|
| 衛部菌疫輸字第001135號 | 曲斯若凍晶注射劑150毫克 | 凍晶注射劑 | ⚠️ 此為 Trastuzumab 生物相似藥，非 Fluorouracil |
| 衛部菌疫輸字第001136號 | 曲斯若凍晶注射劑440毫克 | 凍晶注射劑 | ⚠️ 此為 Trastuzumab 生物相似藥，非 Fluorouracil |

**正確資訊提示**：Fluorouracil 注射劑在台灣確有合法上市，許可證總數約 20 張，劑型以注射劑為主，請透過 TFDA 藥品許可證查詢系統（搜尋關鍵字：fluorouracil / 氟尿嘧啶）取得正確資料。

---

## 細胞毒性

Fluorouracil 屬於抗腫瘤/細胞毒性藥物（Antineoplastic Agents、Antimetabolites），符合本章節適用條件。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類抗代謝劑） |
| 骨髓抑制風險 | 中度（常見嗜中性白血球減少、血小板減少，連續輸注時黏膜炎較顯著） |
| 致吐性分級 | 低至中度（依劑量與給藥方式而異） |
| 監測項目 | CBC（含分類）、肝腎功能（Cr/BUN）、電解質、口腔黏膜狀況、手足症候群評估 |
| 處置防護 | 需依細胞毒性藥物調配與給藥規範操作；連續輸注（持續性靜滴）應使用密閉給藥系統 |

請參考原廠仿單的警語與注意事項，以獲取完整的毒性描述（包含心臟毒性、神經毒性等警示）。

---

## 安全性考量

### 藥物交互作用

共偵測到 **361 筆**交互作用（來源：DDInter 2.0），以下為主要具臨床意義項目：

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Metronidazole | 中度（Moderate） | 可能抑制 5-FU 的二氫嘧啶去氫酶（DPD）代謝路徑，增加 5-FU 暴露量及毒性風險 |
| Tinidazole | 中度（Moderate） | 機轉類似 Metronidazole，同屬硝基咪唑類，需注意毒性疊加 |
| Cimetidine | 輕度（Minor） | 可能輕度影響 5-FU 代謝清除 |
| Levofloxacin | 輕度（Minor） | 需注意 QTc 延長風險的加成效應 |

> 完整 361 筆交互作用清單請參考 DDInter 2.0（https://ddinter2.scbdd.com）。

---

## 結論與下一步

**決策：Hold**

**理由：**
陰道葡萄狀胚胎型橫紋肌肉瘤為極罕見兒科婦科亞型，目前完全無臨床試驗或文獻支持 5-FU 用於此疾病，證據等級僅達 L5（純模型預測）。RMS 的標準化療不含 5-FU，再利用潛力薄弱。

> 📌 **優先建議**：本批次 10 項預測中，**Rank 7：肝臟肉瘤（Liver Sarcoma）** 具有相對最佳的證據基礎（5 個臨床試驗、20 篇文獻、L4 等級、Research Question 建議），建議優先就該適應症重新生成詳細評估報告，以支持後續研究決策。

**若要推進本適應症需要：**
1. **修正資料管道**：確保台灣許可證資料正確對應 Fluorouracil（5-FU），而非 Trastuzumab
2. **補充 MOA 資料**：查詢 DrugBank API 取得 DB00544 完整作用機轉描述
3. **前臨床驗證**：在 RMS 細胞株（如 RD、A204）進行 5-FU 敏感性測試，建立最低可信的前臨床依據後，才可考慮進一步評估

---

