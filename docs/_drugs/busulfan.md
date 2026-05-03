---
layout: default
title: Busulfan
parent: 高證據等級 (L1-L2)
nav_order: 47
evidence_level: L1
indication_count: 10
---

# Busulfan
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Busulfan：從慢性骨髓性白血病到骨髓增生異常症候群

## 一句話總結

> Busulfan（白血寧）是一種雙功能烷化劑，原用於慢性骨髓性白血病治療及造血前驅細胞移植前的清髓條件療法。
> TxGNN 模型預測它可能對**骨髓增生異常症候群 (Myelodysplastic Syndrome, MDS)** 有效，
> 目前有 **50 個臨床試驗登記**（含多個 Phase 3 RCT）和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性、亞急性骨髓性白血病 |
| 預測新適應症 | 骨髓增生異常症候群 (Myelodysplastic Syndrome) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Busulfan 是一種雙功能烷化劑，透過將 DNA 鹼基烷化形成 DNA 鏈間交叉鏈接（interstrand cross-links），引發無法修復的 DNA 損傷，進而達到深度骨髓消融效果。正是這一機轉，使其成為異體造血幹細胞移植（allo-HSCT）前清髓條件療法（myeloablative conditioning）的核心藥物。

慢性骨髓性白血病（CML）與骨髓增生異常症候群（MDS）同屬造血幹細胞的克隆性疾病，皆源自造血前驅細胞的基因異常，具有高度相似的病理生理基礎。在 HSCT 情境下，Busulfan 透過清除患者骨髓中所有殘存的異常造血克隆，並為供者幹細胞植入騰出骨髓空間，從機轉上直接契合 MDS 的治療需求。

值得注意的是，Busulfan 在台灣已取得「造血前驅細胞移植前條件療法」的核准適應症（涵蓋急性骨髓性白血病、慢性骨髓性白血病、淋巴瘤等），而 MDS 在生物學特性及臨床管理上與這些已核准適應症高度重疊。多個大型 Phase 2/3 RCT 直接針對 MDS 患者進行 Busulfan 條件療法的研究，進一步強化了 TxGNN 模型預測的合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | 前瞻性 RCT | 招募中 | 138 | 比較 Venetoclax 強化 BUCY vs 標準 BUCY 條件療法用於高風險 MDS/AML 異體 HSCT，評估療效與安全性 |
| [NCT00002989](https://clinicaltrials.gov/study/NCT00002989) | Phase 3 | 未知 | 207 | Phase 3 RCT 比較異體幹細胞移植條件療法強化策略（含 Idarubicin）用於高復發風險白血病及 MDS |
| [NCT05457556](https://clinicaltrials.gov/study/NCT05457556) | Phase 3 | 進行中（已停招） | 435 | 大型 Phase 3 RCT 比較 MUD vs 半相合供者骨髓消融 HCT，治療兒童及青少年急性白血病與 MDS |
| [NCT00774280](https://clinicaltrials.gov/study/NCT00774280) | Phase 3 | 完成 | 130 | 隨機比較一日一次靜脈 Busulfan+Cyclophosphamide vs Busulfan+Fludarabine 用於白血病及 MDS 異體 HCT |
| [NCT01339910](https://clinicaltrials.gov/study/NCT01339910) | Phase 3 | 終止 | 272 | Phase 3 多中心 RCT（BMT CTN #0901）比較骨髓消融 vs 減毒強度條件療法用於 MDS/AML 異體 HSCT |
| [NCT00322101](https://clinicaltrials.gov/study/NCT00322101) | Phase 3 | 完成 | 25 | Phase 3 多中心 RCT 比較骨髓消融（含 Busulfan）vs 非骨髓消融移植條件療法用於 MDS/AML |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | 完成 | 68 | Busulfan+Fludarabine 減毒強度條件療法加 Azacitidine 用於高風險 MDS 及老年 AML 異體移植 |
| [NCT00024050](https://clinicaltrials.gov/study/NCT00024050) | Phase 2 | 完成 | N/A | Phase 2 直接研究異體 PBSC 移植治療「低風險 MDS」，評估化療後幹細胞移植有效性 |
| [NCT00629798](https://clinicaltrials.gov/study/NCT00629798) | Phase 2 | 完成 | 64 | Busulfan+Melphalan+Fludarabine 加 Palifermin 保護後接 T 細胞去除 HSCT 用於進展期 MDS/AML |
| [NCT02221310](https://clinicaltrials.gov/study/NCT02221310) | Phase 2 | 完成 | 25 | Gemtuzumab Ozogamicin 聯合 Busulfan/Cyclophosphamide 條件療法後異體移植用於高風險 AML/MDS |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT | Am J Hematol | Phase 3 最終分析（476 人）：Treosulfan 條件療法無劣效於 Busulfan，兩者均可有效用於老年 MDS/AML HSCT |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT | Lancet Haematol | Phase 3 RCT（MC-FludT.14/L）：Treosulfan+Flu 對比 Busulfan+Flu 療效不劣，但毒性較低，為 MDS 老年患者提供選項 |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Cohort | Lancet Haematol | Phase 3 開放標籤 RCT：G-CSF+Decitabine+Bu/Cy 條件療法顯著降低 MDS-RAEB/sAML 患者 HSCT 後復發率 |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Cohort | J Clin Oncol | Phase 3 RCT（BMT CTN）：骨髓消融 vs 減毒強度 HCT 用於 AML/MDS，總存活率相近，但條件療法強度影響復發率 |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Cohort | Transplant Cell Ther | Busulfan+Fludarabine 骨髓消融條件療法聯合體內 T 細胞去除，對 AML 及 MDS 患者安全有效 |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Cohort | Bone Marrow Transplant | 日本全國資料庫傾向評分分析：Flu/Bu4 vs Bu4/Cy 骨髓消融條件療法用於 MDS HSCT 結果比較 |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Cohort | Transplant Cell Ther | 單中心回顧性傾向評分匹配研究（138 人）：Treosulfan vs Busulfan 條件療法用於 MDS HSCT 療效對比 |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Cohort | Cancer | 分次靜脈 Busulfan 骨髓消融條件療法可安全應用於老年 AML/MDS 患者，且不增加非復發死亡率 |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | 當代回顧：異體 HSCT 仍是 MDS 唯一潛在根治性療法，基因組分析驅動個別化條件療法選擇 |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Cohort | Front Oncol | 系統性回顧與 Meta 分析：Treosulfan vs Busulfan 條件療法在 MDS/AML HSCT 長期結果之比較 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥輸字第002940號 | 白血寧 | 散劑 | 慢性、亞急性骨髓性白血病 |
| 衛署藥輸字第011705號 | 補素芬錠2公絲 | 膜衣錠 | 慢性骨髓性白血病、真性紅血球增多症、自發性血小板增多症 |
| 衛署藥輸字第009115號 | 邁樂寧錠2毫克 | 膜衣錠 | 慢性骨髓細胞白血病 |
| 衛署藥輸字第023785號 | 補束剋注射劑 | 注射劑 | 併用化療藥物及/或放射線治療，作為下列患者進行造血前驅細胞移植前之條件療法：急性淋巴性白血病，急性非淋巴性白血病，急性骨髓性白血病，慢性骨髓性白血病，非何杰... |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（雙功能烷化劑，Bifunctional Alkylating Agent） |
| 骨髓抑制風險 | **高度**（為設計目的之骨髓消融藥物，必然引發嚴重全血球減少；為 HSCT 前預期療效而非副作用） |
| 致吐性分級 | 低至中度（口服低劑量方案較低；靜脈高劑量移植條件方案可達中度） |
| 監測項目 | CBC（含分類計數）、肝功能（ALT/AST/總膽紅素）、腎功能、靜脈注射時建議進行藥物血中濃度監測（TDM）以達到目標 AUC |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈製劑需使用特殊稀釋溶液（二甲基乙醯胺/DMA）及設備，並注意對操作人員的職業暴露防護 |

---

## 安全性考量

**主要藥物交互作用**（資料庫共收錄 228 筆）：

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Metronidazole | **重大 (Major)** | 可能顯著增加 Busulfan 毒性（抑制代謝），應避免合用 |
| Aprepitant | 中度 (Moderate) | 作為 CYP3A4 抑制劑，可能影響 Busulfan 清除率 |
| Miconazole | 中度 (Moderate) | 唑類抗黴菌藥可能抑制 Busulfan 代謝，需監測毒性 |
| Levofloxacin | 輕度 (Minor) | 移植情境下常用之預防性抗生素，需注意合用安全性 |

其餘 224 筆交互作用（等級 Unknown）涵蓋移植常用輔助藥物，包括質子幫浦抑制劑（Omeprazole、Pantoprazole、Lansoprazole）、止吐藥（Ondansetron、Granisetron）、類固醇（Dexamethasone、Prednisone）等，建議於處方前逐一確認。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Busulfan 在 MDS 的 HSCT 條件療法情境下，已有包含多個 Phase 3 RCT 在內的直接且高品質臨床證據支持，證據等級達 L1。其作用機轉（骨髓消融清除異常造血克隆）與 MDS 的治療需求高度契合，且台灣已核准鄰近適應症的移植條件療法使用，整體風險效益評估具備充足依據。

**若要推進需要：**
- 補充完整 MOA 文獻資料（DrugBank DB01008 API 查詢）以強化機轉論述
- 建立 MDS 亞型分層療效資料（依 IPSS-R 風險群分別評估移植時機與條件療法選擇）
- 制定老年族群及高 HCT-CI 評分患者的個別化安全性監測計畫
- 評估台灣臨床實務中 Busulfan 與常用輔助藥物（PPIs、唑類抗黴菌藥）交互作用的管理策略
- 確認靜脈製劑（補束剋注射劑）之藥物血中濃度監測（TDM）在台灣的可及性與標準化流程
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

