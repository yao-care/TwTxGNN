---
layout: default
title: Fludarabine
parent: 中證據等級 (L3-L4)
nav_order: 105
evidence_level: L3
indication_count: 10
---

# Fludarabine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Fludarabine：從慢性淋巴球性白血病到漿細胞骨髓瘤

## 一句話總結

Fludarabine 是一種嘌呤核苷酸類似物，原本用於治療慢性淋巴球性白血病（CLL）及低惡度 B 細胞非何杰金氏淋巴瘤。
TxGNN 模型預測它可能對**漿細胞骨髓瘤 (Plasma Cell Myeloma)** 有效，
目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性淋巴球性白血病（CLL）、濾泡性淋巴瘤 |
| 預測新適應症 | 漿細胞骨髓瘤 (Plasma Cell Myeloma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Fludarabine 的詳細作用機轉資料目前缺乏（MOA 待補充）。根據已知臨床與基礎研究資料，Fludarabine 屬於嘌呤核苷酸類似物，可抑制 DNA 聚合酶及核糖核苷酸還原酶，阻斷 DNA 合成，並可誘導淋巴球及漿細胞凋亡，同時具有強效免疫抑制作用。

漿細胞骨髓瘤（多發性骨髓瘤，MM）為異常漿細胞克隆增生所致的血液惡性腫瘤，與 Fludarabine 原始適應症（CLL、B 細胞淋巴瘤）同屬 B 細胞譜系來源的血液腫瘤，在細胞生物學上具有直接關聯性。體外及動物實驗（PMID 17976186）已直接證實 Fludarabine 對骨髓瘤細胞株 RPMI8226 具有細胞毒性，並伴隨 Akt 磷酸化降低，揭示可能的細胞訊號干預機轉。

在臨床上，Fludarabine 是異體造血幹細胞移植（allo-HSCT）非骨髓清除性及減低強度調理方案（RIC）的標準核心藥物之一，已廣泛用於含骨髓瘤患者的 HSCT 調理。透過免疫抑制促進植入，並藉由移植物抗骨髓瘤（Graft-versus-Myeloma, GVM）效應清除殘餘病灶。此外，Fludarabine/Cyclophosphamide 組合亦是 BCMA CAR-T 細胞治療前淋巴清除（lymphodepletion）的主流方案之一，直接在骨髓瘤治療流程中佔有核心角色。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00006379](https://clinicaltrials.gov/study/NCT00006379) | Phase 2 | 已完成 | 58 | 以嘌呤類似物（Fludarabine）為基礎的非骨髓清除性異體 SCT，適應症直接涵蓋多發性骨髓瘤，為最高相關性試驗 |
| [NCT00074490](https://clinicaltrials.gov/study/NCT00074490) | Phase 2 | 已終止 | 442 | 低強度含 Fludarabine 調理的異體 HSCT（含 Sirolimus），適應症含骨髓瘤、淋巴瘤及 MDS，提供直接可行性資料 |
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | 已終止 | 6 | Busulfan+Fludarabine 加供者幹細胞移植直接用於多發性骨髓瘤及骨髓纖維化，雖提前終止仍有直接試驗紀錄 |
| [NCT00781170](https://clinicaltrials.gov/study/NCT00781170) | Phase 2 | 已完成 | 20 | Melphalan/Fludarabine 減量異體移植後評估移植物抗骨髓瘤效應，適應症 Stage II/III MM |
| [NCT00615589](https://clinicaltrials.gov/study/NCT00615589) | Phase 2 | 已終止 | 22 | 含 Fludarabine 減低毒性骨髓清除調理方案用於高風險多發性骨髓瘤異體 HSCT |
| [NCT00078065](https://clinicaltrials.gov/study/NCT00078065) | Phase 2 | 已完成 | 30 | 隨機比較 Xcellerated T 細胞有無 Fludarabine 前處理用於多發性骨髓瘤，直接檢驗 Fludarabine 在 MM 的作用 |
| [NCT04579523](https://clinicaltrials.gov/study/NCT04579523) | Phase 1 | 尚未招募 | 30 | ²¹¹At 標記抗 CD38 抗體合併 Fludarabine 調理用於高風險多發性骨髓瘤 HCT |
| [NCT03524235](https://clinicaltrials.gov/study/NCT03524235) | Phase 1 | 已完成 | 20 | Bendamustine+Fludarabine+Rituximab 調理用於半相合 SCT，適應症含 MM 及 CLL |
| [NCT05767359](https://clinicaltrials.gov/study/NCT05767359) | Phase 2 | 活躍中（未招募） | 20 | Cilta-cel 用於高風險冒煙型骨髓瘤，調理方案明確使用 Cyclophosphamide+Fludarabine |
| [NCT00305682](https://clinicaltrials.gov/study/NCT00305682) | Phase 2 | 已完成 | 295 | 非親屬臍帶血移植治療血液惡性疾病（含 MM），Fludarabine+Cyclophosphamide 骨髓清除方案 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | Am J Clin Oncol | Bortezomib+Fludarabine+Melphalan（含/不含全骨髓照射）作為高風險/復發難治性 MM 異體 HSCT 調理方案，直接檢驗 Fludarabine 在骨髓瘤的安全性 |
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | 體外/動物 | Eur J Haematol | Fludarabine 在體外及動物實驗中對骨髓瘤細胞株具直接抗腫瘤活性，同時降低 Akt 磷酸化，提供機轉依據 |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leuk Res Rep | 分次 Busulfan+Fludarabine+post-transplant Cyclophosphamide 骨髓清除性方案用於 MM 及骨髓纖維化異體 SCT，1 年存活率 50% |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | 多中心回顧 | Bone Marrow Transplant | 34 例 Fludarabine+Treosulfan 減毒調理用於多發性骨髓瘤異體 SCT，評估可行性與毒性 |
| [15389436](https://pubmed.ncbi.nlm.nih.gov/15389436/) | 2004 | 多中心研究 | Biol Blood Marrow Transplant | 120 例 Melphalan/Fludarabine 減量異體移植 MM 資料，1 年 TRM 18%，確立復發後移植為最強預後不良因子 |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | 回顧性研究 | Blood Cancer J | 比較 Fludarabine/Cyclophosphamide 與 Bendamustine 作為 BCMA CAR-T 前淋巴清除方案，直接確立 Flu/Cy 在骨髓瘤 CAR-T 流程中的核心地位 |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | 病例報告 | Eur J Haematol | 最早報告 Fludarabine 用於漿細胞性白血病（plasma cell leukemia），奠定 Fludarabine 在漿細胞疾病的應用基礎 |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | Phase 1/2 隨訪 | J Clin Oncol | BCMA+CD19 雙靶向 CAR-T 長期隨訪（復發/難治 MM），Fludarabine 用於淋巴清除前處理，顯示高反應率 |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | 世代研究 | Blood | 16 家美國學術中心 236 例標準治療 Cilta-cel 真實世界數據，Fludarabine 為調理方案核心，92.5% 完成輸注 |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 | Nature Medicine | 異體 BCMA CAR-T（ALLO-715）加含 ALLO-647 淋巴清除方案用於復發/難治 MM（UNIVERSAL 試驗），43 例安全性資料 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部菌疫輸字第000973號 | 癌即瓦注射劑 | 注射液劑 | 1.慢性淋巴球性白血病：與chlorambucil 併用，適用於先前未曾接受過治療，且具有合併症而不適合含fludarabine治療的CD20陽性CLL病人。2.濾泡性淋巴瘤...4.狼瘡性腎炎... |
| 衛部菌疫輸字第000948號 | 瑞樂靶注射劑 | 注射劑 | 非何杰金氏淋巴瘤：用於復發或對化學療法有抗性之低惡度B-細胞非何杰金氏淋巴瘤。併用CVP化學療法用於未經治療之和緩性B細胞非何杰金氏淋巴瘤... |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Purine Nucleoside Analog / 嘌呤核苷酸類似物） |
| 骨髓抑制風險 | 高度（嘌呤類似物為已知強效骨髓抑制劑，中性白血球及淋巴球減少為常見劑量限制性毒性） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含分類計數）、肝腎功能（特別是腎功能，劑量調整依據）、感染指標（因免疫抑制風險高）、神經毒性評估 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；因強效免疫抑制，需警惕 CMV、PCP 等機會性感染並考慮預防性投藥 |

---

## 安全性考量

**藥物交互作用**（資料庫共收錄 369 筆，以下列出已確認的主要交互作用）：

| 交互藥物 | 嚴重程度 | 資料來源 |
|---------|---------|---------|
| Metronidazole | 中度 | DDInter |
| Rosuvastatin | 中度 | DDInter |
| Simvastatin | 中度 | DDInter |
| Tinidazole | 中度 | DDInter |
| Levofloxacin | 輕度 | DDInter |

主要警語及禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Fludarabine 在漿細胞骨髓瘤有直接的體外抗腫瘤證據（PMID 17976186），並作為 HSCT 調理方案及 CAR-T 前淋巴清除的核心藥物廣泛用於骨髓瘤臨床流程；多個 Phase 1/2 試驗已確認其在骨髓瘤患者的安全性與可行性，但目前缺乏以 Fludarabine 為主角（非調理輔助角色）的 Phase 3 骨髓瘤隨機對照試驗，整體證據等級為 L3。

**若要推進需要：**
- 補充 Fludarabine 詳細作用機轉（MOA）資料（DrugBank API）
- 釐清 Fludarabine 在骨髓瘤治療中的精準定位：直接抗腫瘤用藥 vs. HSCT 調理 vs. CAR-T 前處理
- 評估在現代骨髓瘤治療背景（蛋白酶體抑制劑、IMiD、CD38 抗體）下 Fludarabine 的加乘或互補潛力
- 確認台灣許可證資料完整性（現有資料疑含 CD20 靶向抗體之許可證，建議重新比對 TFDA 資料庫）
- 規劃高度免疫抑制情境下的機會性感染監測計畫與風險管理方案
---

