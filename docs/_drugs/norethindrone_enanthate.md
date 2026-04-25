---
layout: default
title: Norethindrone Enanthate
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 1
---

# Norethindrone Enanthate
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

# Norethindrone Enanthate：從長效避孕到第二型抗凝血素缺乏症

## 一句話總結

Norethindrone enanthate（炔諾酮庚酸酯）是一種長效注射型黃體素，主要作為避孕藥使用，台灣目前無核准許可證上市。
TxGNN 模型預測它可能對**第二型抗凝血素缺乏症 (Antithrombin Deficiency Type 2)** 有效，
目前**無任何臨床試驗或文獻**支持這個方向，且已知文獻顯示該藥具有促血栓效應，與此適應症的治療目標存在根本性矛盾。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 長效注射型避孕藥（台灣無核准許可證） |
| 預測新適應症 | 第二型抗凝血素缺乏症 (Antithrombin Deficiency Type 2) |
| TxGNN 預測分數 | 98.93% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Norethindrone enanthate 是一種長效注射型黃體素（progestogen），透過抑制排卵、改變子宮頸黏液及子宮內膜環境達到避孕效果，通常每 8 週肌肉注射一次（200 mg）。

從理論角度來看，黃體素類藥物可能透過影響肝臟合成凝血蛋白，間接調節抗凝血素（Antithrombin）路徑。第二型抗凝血素缺乏症為抗凝血素功能型缺損，患者具有較高的靜脈血栓栓塞風險，TxGNN 知識圖譜可能基於「黃體素 → 肝臟凝血蛋白合成 → 抗凝血素調節」的間接節點連結產生此預測。

然而，此預測存在根本性的安全矛盾，無法被合理支持：現有文獻明確記錄 norethindrone enanthate 具有**促血栓效應**，包含降低 HDL、升高 LDL 等不利脂質代謝變化，以及腦靜脈竇血栓（CVST）的個案報告。對於本身即有血栓傾向的第二型抗凝血素缺乏症患者，使用此藥在安全性上顯然相悖，此預測整體評估為生物學合理性極低的純模型推論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **注意**：根據本次蒐集到的其他適應症相關文獻，norethindrone enanthate 已有誘發腦靜脈竇血栓的個案報告（PMID [29141931](https://pubmed.ncbi.nlm.nih.gov/29141931/)），並對血脂代謝（HDL 降低）有不良影響。在進行任何再利用評估前，應優先取得並審閱完整仿單警語與禁忌症資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
排名第 1 的適應症（第二型抗凝血素缺乏症）屬 L5 等級，完全無臨床試驗或文獻支持，且該藥的已知促血栓副作用與治療血栓傾向疾病的目標直接相悖；全部 10 個預測適應症均建議 Hold，其中有 4 個（antithrombin deficiency type 2、factor 5 excess with spontaneous thrombosis、thrombophilia、cardiovascular disease）更存在主動安全性疑慮，不宜推進。

**若要推進需要：**
- 取得 TFDA 仿單 PDF 並解析完整警語與禁忌症（現為阻斷性資料缺口）
- 補充完整作用機轉資料（MOA），確認是否存在任何抗凝血調節效果
- 針對「黃體素促血栓 vs. 假設的抗凝血效益」進行藥理學悖論評估
- 若仍要探索免疫調節相關適應症（如類風濕性關節炎），需先完成上述安全性評估

---

