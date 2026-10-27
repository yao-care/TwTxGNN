---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-16
description: "Caplacizumab：預測新適應症為血小板釋放障礙 (Primary release disorder of platelets)（證據等級 L5）。原適應症：合併血漿置換術及免疫抑制劑，治療成人及 12 歲以上且體重 40 公斤以上青少年的後天性血栓性血小板低下紫斑症（aTTP）"
monitor_inn: "Caplacizumab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia", "platelet-type bleeding disorder"]
---

# Caplacizumab
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

## Caplacizumab：從後天性血栓性血小板低下紫斑症到血小板釋放障礙
{: .text-alpha }

## 一句話總結

Caplacizumab 是抗 von Willebrand 因子（vWF）A1 結構域的奈米抗體，原本與血漿置換術及免疫抑制劑合併使用，治療後天性血栓性血小板低下紫斑症（aTTP）。
TxGNN 模型預測它可能對**血小板釋放障礙（primary release disorder of platelets）**有效，但目前**沒有相關臨床試驗與文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 合併血漿置換術及免疫抑制劑，治療成人及 12 歲以上且體重 40 公斤以上青少年的後天性血栓性血小板低下紫斑症（aTTP） |
| 預測新適應症 | 血小板釋放障礙 (Primary release disorder of platelets) |
| TxGNN 預測分數 | 99.9998% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Caplacizumab 結合 vWF 的 A1 結構域，阻斷 vWF 與血小板 GPIb-IX-V 的交互作用。在 ADAMTS13 缺乏的 TTP 中，超大型 vWF 多聚體會造成微血管血栓，caplacizumab 可預防這個過程。目前缺乏 DrugBank 的詳細作用機轉資料，以上機轉來自 vWF 抑制劑的已知藥理。

血小板釋放障礙的核心問題是血小板顆粒分泌缺陷，也就是血小板功能不足。這與 TTP 的過度血小板黏附正好相反。Caplacizumab 的作用等同抑制血小板黏附，不僅無法修復顆粒分泌缺陷，還可能加重出血傾向。

因此，從機轉角度看，這個預測缺乏明確的合理性。模型分數很高，但不能取代生物學與臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Caplacizumab 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001243號 | 可利康凍晶注射劑10毫克 | 注射劑 | 賽諾菲股份有限公司 | 2028/10/16 | 適用於合併血漿置換術及免疫抑制劑，治療患有後天性血栓性血小板低下紫班症(acquired thrombotic thrombocytopenic purpura; aTTP)之成人… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 139 筆交互作用，以下為部分重要項目。
  - **Major 等級**：Acetylsalicylic acid（阿斯匹靈）、Abciximab、Fondaparinux、Alteplase、Anagrelide、Acalabrutinib、Deferasirox、Trastuzumab emtansine、Ibritumomab tiuxetan、Tositumomab
  - **Moderate 等級**：Ibuprofen、Ketorolac、Celecoxib、Fluvoxamine、Fenfluramine、Dexfenfluramine、Sibutramine
- 上述藥物多為抗血小板、抗凝血、血栓溶解或 NSAID 類，與 caplacizumab 併用時出血風險可能增加。
- 若用於原本就有出血傾向的血小板疾病，出血風險更需謹慎評估。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數，沒有任何臨床試驗或文獻佐證（L5）。
- 機轉上 caplacizumab 抑制血小板黏附，與血小板釋放障礙的病理方向不符，且可能加重出血。

**補充說明：**
同一份預測清單中，「血栓性血小板低下紫斑症」的證據完整，有 HERCULES 等 Phase 3 試驗（證據等級 L1）。但那是 caplacizumab 已核准的原適應症，屬於對預測的驗證，不是新的藥物再利用機會。清單中其他預測（如 Glanzmann 血小板無力症、血友病等）同樣缺乏機轉支持與臨床證據。

**若要推進需要：**
- 先釐清血小板釋放障礙是否有任何機轉上可行的假說，目前看來可能性低。
- 前臨床研究（如血小板功能與出血模型）評估 vWF–GPIb 阻斷在此疾病中的影響。
- 完整的作用機轉資料（MOA）與出血風險評估。
- 建議把資源優先放在機轉上較可信的候選適應症，而非此項預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

