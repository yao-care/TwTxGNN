---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

# Ivermectin：從疥瘡到外陰陰道念珠菌病

## 一句話總結

Ivermectin 是廣效抗寄生蟲藥，核准用於疥瘡、糞小桿線蟲感染及蟠尾絲蟲感染，外用製劑亦已核准用於酒槽鼻。
TxGNN 模型預測它可能對**外陰陰道念珠菌病 (Vulvovaginal Candidiasis)** 有效，
然而目前**無任何臨床試驗或文獻**直接支持此預測，預測依據主要來自知識圖譜中的共病網絡關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 驅蟲劑（疥瘡、糞小桿線蟲感染、蟠尾絲蟲感染） |
| 預測新適應症 | 外陰陰道念珠菌病 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 列為高嚴重度數據缺口）。根據已知資訊，Ivermectin 屬於大環內酯類抗寄生蟲藥，其主要機轉為活化無脊椎動物麩胺酸閘控氯離子通道（GluCl），導致寄生蟲神經肌肉麻痺死亡，此機轉對真菌（Candida）並無直接作用。

然而，部分體外研究顯示 Ivermectin 具有廣泛的抗病毒及免疫調節活性，包括抑制 importin α/β 核輸送路徑，理論上可干擾多種病原體的細胞內複製過程。此外，Ivermectin 外用製劑（Soolantra）已核准用於玫瑰斑丘疹膿皰型，顯示其在皮膚黏膜部位具有一定的抗炎潛力。

TxGNN 預測外陰陰道念珠菌病的依據，很可能來自知識圖譜中「免疫受損宿主→機會性感染→念珠菌病」的共病節點連結，而非藥理直接性。亦即模型捕捉到疥瘡患者（常見免疫抑制族群）與念珠菌感染在臨床資料庫中的共現關係，而非真實的抗念珠菌效果。**此預測目前缺乏前臨床或臨床直接支持，機轉合理性存疑。**

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻（針對外陰陰道念珠菌病此預測適應症）。

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥陸輸字第001017號 | 二氫阿維菌素 | （粉） | 驅蟲劑 |
| 衛部藥陸輸字第001053號 | 伊維菌素 | （粉） | 寄生蟲感染用藥 |
| 衛部藥輸字第027060號 | 舒利達乳膏 | 乳膏劑 | Soolantra 適用於成人酒槽（丘疹膿皰皮疹）發炎病灶的局部治療。 |

---

## 安全性考量

**藥物交互作用（共 101 筆，以下列出中度以上項目）：**

| 交互藥物 | 風險等級 | 來源 |
|---------|---------|------|
| Warfarin | Moderate | DDInter |
| Clarithromycin | Moderate | DDInter |
| Cobicistat | Moderate | DDInter |
| Aprepitant | Moderate | DDInter |
| Deferasirox | Moderate | DDInter |
| Dicoumarol | Moderate | DDInter |
| Fostamatinib | Moderate | DDInter |
| Ethanol | Moderate | DDInter |
| Abametapir (topical) | Moderate | DDInter |
| Iodide I-123 | Moderate | DDInter |
| Iodide I-131 | Moderate | DDInter |

> 其餘警語、禁忌症資訊請參考原廠仿單。完整 DDI 清單共 101 筆，需特別注意與抗凝血劑（Warfarin、Dicoumarol）及 CYP3A4 強抑制劑（Clarithromycin、Cobicistat）的中度交互作用。

---

## 結論與下一步

**決策：Hold**

**理由：**
Ivermectin 對 Candida 屬真菌無已知直接抗菌機轉，TxGNN 的預測分數雖高（99.95%），但完全缺乏前臨床體外試驗、動物模型、或任何臨床試驗數據支持；目前僅為 L5（純模型預測）等級，不具備推進再利用研究的科學基礎。

**若要重新評估需要：**
- 補充 DrugBank MOA 完整資料，確認 Ivermectin 是否對 Candida 有任何已知生物活性
- 進行體外抗念珠菌最小抑菌濃度（MIC）測試，確認是否具基礎抗真菌活性
- 評估知識圖譜的共病連結是否源自混淆因子（confounding），例如免疫抑制族群同時發生疥瘡與念珠菌感染
- 若體外試驗顯示陽性訊號，再考慮動物模型驗證後升級為 L4
---

