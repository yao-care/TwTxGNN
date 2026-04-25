---
layout: default
title: Methylprednisone
parent: 中證據等級 (L3-L4)
nav_order: 164
evidence_level: L3
indication_count: 1
---

# Methylprednisone
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Methylprednisolone：從急性病症到血小板減少症

> **本報告為多適應症評估（TW-DB12952-multi）**，涵蓋 TxGNN 預測排名前 10 之適應症，並以臨床證據最充分之**血小板減少症**為主要分析標的。

---

## 一句話總結

Methylprednisolone 是廣泛使用的合成糖皮質激素，台灣核准用於急性病症、支氣管性氣喘、休克、過敏反應及膠原疾病等多種適應症。TxGNN 模型共預測 10 個新適應症，其中**血小板減少症 (Thrombocytopenia)** 的臨床證據最為充分，現有 **1 個臨床試驗**和 **13 篇文獻**支持，機轉清晰且與現行臨床實踐高度吻合，建議優先推進評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性病症（氣喘、休克、虛脫、過敏性疾患） |
| 主要預測新適應症 | 血小板減少症 (Thrombocytopenia) |
| TxGNN 預測分數 | 98.91% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Proceed with Guardrails |

---

## 多適應症預測總覽

本次評估共涵蓋 10 個預測適應症，依證據等級排序如下：

| 原始排名 | 適應症（英文） | 適應症（中文） | TxGNN 分數 | 證據等級 | 決策建議 |
|---------|-------------|-------------|-----------|---------|---------|
| 8 | Thrombocytopenia | 血小板減少症 | 98.91% | L3 | ✅ Proceed with Guardrails |
| 2 | Coronary Artery Disease | 冠狀動脈疾病 | 99.37% | L3 | 🔬 Research Question |
| 4 | Myocardial Ischemia | 心肌缺血 | 99.23% | L3 | 🔬 Research Question |
| 1 | Leprosy | 麻風病 | 99.49% | L5 | ⏸ Hold |
| 5 | Pneumocystosis | 肺囊蟲肺炎 | 99.15% | L5 | ⏸ Hold |
| 6 | Anomalous Left Coronary Artery from the Pulmonary Artery | 肺動脈起源異常左冠狀動脈 (ALCAPA) | 99.12% | L5 | ⏸ Hold |
| 7 | Bacteroidaceae Infectious Disease | 擬桿菌科感染症 | 99.12% | L5 | ⏸ Hold |
| 3 | Candidiasis | 念珠菌症 | 99.28% | L5 | ⏸ Hold |
| 9 | Anaerobic Bacteria Infectious Disease | 厭氧菌感染症 | 98.83% | L5 | ⏸ Hold |
| 10 | Macrothrombocytopenia with Mitral Valve Insufficiency | 巨血小板減少症合併二尖瓣閉鎖不全 | 98.74% | L5 | ⏸ Hold |

> **注意**：TxGNN 預測分數越高不代表臨床可行性越高；念珠菌症（排名第 3，分數 99.28%）因糖皮質激素的免疫抑制特性反而可能**加重感染**，存在明顯機轉矛盾，評估時需審慎。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Methylprednisolone 是合成糖皮質激素，透過結合胞內糖皮質激素受體影響基因轉錄，廣泛抑制免疫細胞活化與炎症介質釋放，在多種自體免疫與過敏性疾病中已有確立的療效。

免疫性血小板減少症（ITP）的核心病理在於：自體免疫系統產生抗血小板抗體（以抗 GPIIb/IIIa 之 IgG 為主），致使脾臟巨噬細胞透過 Fc 受體大量清除血小板，引發血小板計數驟降。Methylprednisolone 對此具有雙重作用機轉：其一是**抑制脾臟巨噬細胞 Fc 受體的表達**，直接降低血小板清除速率；其二是**壓制 B 細胞活化、減少自體抗體生成**，從根源降低免疫媒介的血小板破壞。

Methylprednisolone 的原核准適應症涵蓋膠原疾病、過敏反應等多種免疫媒介疾病，而 ITP 同屬免疫媒介疾病，藥理機轉上的延伸具備充分依據。糖皮質激素（包含 Methylprednisolone）在國際多個血液學指引中已被列為成人及兒童 ITP 的**一線治療選項**，此次 TxGNN 預測在一定程度上是對既有臨床實踐的模型驗證與確認。

---

## 臨床試驗證據（血小板減少症）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03154385](https://clinicaltrials.gov/study/NCT03154385) | 前瞻開放性試驗（Phase IIa） | 完成 | 15 | 評估 Rituximab 合併 Belimumab 治療持續性 ITP 的療效與安全性；皮質類固醇（含 Methylprednisolone）作為聯合治療基礎，追蹤期 1 年 |

---

## 臨床試驗證據（冠狀動脈疾病 / 心肌缺血）

兩個心血管適應症共享同一臨床試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00650468](https://clinicaltrials.gov/study/NCT00650468) | Phase 4 多中心雙盲 RCT | 完成 | 397 | 比較腎移植患者早期停用類固醇 vs. 長期維持方案（Prograf + CellCept）；皮質類固醇與心血管結果為次要觀察終點，屬間接相關 |

---

## 文獻證據（血小板減少症）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40316774](https://pubmed.ncbi.nlm.nih.gov/40316774/) | 2025 | Case series | Oral Maxillofac Surg | 局部注射 Methylprednisolone 合併尿素治療嬰兒顏面部 Kasabach-Merritt 症候群（伴隨血小板減少），療效與安全性分析 |
| [38681008](https://pubmed.ncbi.nlm.nih.gov/38681008/) | 2024 | Case series | Indian J Nephrology | 慢性 ITP 合併末期腎病患者成功接受腎移植；術中使用 Methylprednisolone + IVIg 維持血小板水平，預後良好 |
| [36533358](https://pubmed.ncbi.nlm.nih.gov/36533358/) | 2022 | Case series | J Peking Univ Health Sci | 5 例皮肌炎合併巨噬細胞活化症候群（含繼發性血小板減少）；Methylprednisolone 為主要免疫抑制治療方案 |
| [36523319](https://pubmed.ncbi.nlm.nih.gov/36523319/) | 2022 | Case report | Transl Cancer Res | Trastuzumab 治療 HER2+ 乳癌引發血小板減少等不良反應之處置，Methylprednisolone 用於支持性治療 |
| [15795920](https://pubmed.ncbi.nlm.nih.gov/15795920/) | 2005 | Case series | Am J Hematol | Rituximab 治療難治性成人 ITP，整體反應率約 50%；多數患者同步接受皮質類固醇（含 Methylprednisolone）維持 |
| [14719177](https://pubmed.ncbi.nlm.nih.gov/14719177/) | 2003 | Cohort | Semin Thromb Hemost | 兒童急性 ITP 20 年回顧；糖皮質激素為確立的標準一線治療，顱內出血發生率 <1% |
| [11204325](https://pubmed.ncbi.nlm.nih.gov/11204325/) | 2000 | Case series | Polski Merkur Lek | 15 例類固醇治療失敗的 ITP 患者行腹腔鏡脾切除術；術前以 Prednisone/Methylprednisolone 橋接治療 |
| [11212156](https://pubmed.ncbi.nlm.nih.gov/11212156/) | 2001 | Case report | Arthritis Rheum | SLE 相關自體免疫血小板減少症以重組 IL-11 治療，與標準糖皮質激素方案比較 |
| [9543364](https://pubmed.ncbi.nlm.nih.gov/9543364/) | 1998 | Review | Pediatr Nephrol | 兒童溶血性尿毒症候群（HUS）中 Methylprednisolone（5 mg/kg/day）隨機雙盲安慰劑對照試驗；92 例患者分析，神經學、血液學及腎臟學結果無顯著差異 |
| [2029911](https://pubmed.ncbi.nlm.nih.gov/2029911/) | 1991 | Case report | Eur J Pediatrics | Onyalai（ITP 特殊口腔黏膜出血表現）1.5 個月大嬰兒，大劑量靜脈 Methylprednisolone（30 mg/kg × 3 天）治療後血小板計數迅速回升 |

---

## 文獻證據（冠狀動脈疾病 / 心肌缺血）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26361889](https://pubmed.ncbi.nlm.nih.gov/26361889/) | 2016 | Cohort | J Magn Reson Imaging | 豬冠狀動脈微栓塞模型中，Methylprednisolone 治療組以心臟 MRI（心肌灌注 + 延遲釓顯影）評估急性療效；結果顯示可改善微灌注，縮小缺血面積 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥輸字第003633號 | 歐巴生針劑２０公絲 | 乾粉注射劑 | 急性病症（氣喘、休克、虛脫、過敏性疾患） |
| 衛署藥製字第048248號 | "永信" 甲基普立朗 注射劑500毫克 | 乾粉注射劑 | 腎上腺皮質機能不全，劇烈休克、支氣管性氣喘、膠原疾病、過敏反應、泛發性感染 |
| 衛署藥輸字第002451號 | 猛加斯特２０公絲注射劑 | 凍晶注射劑 | 膠原質病（類風濕性關節炎、風濕性關節炎）過敏症（支氣管性氣喘、花粉過敏症、鼻炎、濕疹） |
| 衛署藥輸字第000974號 | 微粒甲基乙醯去氫羥化腎上腺皮質素 | （粉） | 風濕性關節炎 |
| 衛署藥輸字第004922號 | 舒汝美卓佑注射劑 | 凍晶注射劑 | 腎上腺皮質機能不全、劇烈休克、支氣管性氣喘、膠原疾病、過敏反應、泛發性感染 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **特別提醒（多適應症評估）**：TxGNN 預測中包含多個**感染性疾病**適應症（念珠菌症、擬桿菌科感染症、厭氧菌感染症），而 Methylprednisolone 的免疫抑制特性在活動性感染情境下屬重要禁忌，存在明顯機轉矛盾，**不建議推進這些方向的再利用評估**。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對血小板減少症）

**理由：**
Methylprednisolone 透過抑制 Fc 受體介導的血小板清除及自體抗體生成，機轉明確且與 ITP 一線治療實踐高度一致；現有文獻（13 篇）及臨床試驗提供 L3 等級支持，反映糖皮質激素在血小板減少症臨床應用的廣泛基礎。

**若要推進需要：**
- 補充完整的 DrugBank MOA 資料及藥物安全性警語（需查詢 DrugBank API，目前為 Data Gap）
- 確認目標 ITP 次族群（急性 ITP vs. 慢性/難治性 ITP）及現行台灣指引中 Methylprednisolone 的地位
- 評估相較口服 Prednisolone 的劑量等效性與給藥途徑（台灣現有許可為注射劑型）
- 建立用藥監測計畫（血糖、血壓、骨質疏鬆等糖皮質激素長期使用風險）

**冠狀動脈疾病 / 心肌缺血（Research Question）：**
需設計以 CAD/心肌缺血為主要終點的前瞻性研究；現有間接證據（腎移植 RCT、動物模型）尚不足以支持臨床推進，且長期糖皮質激素本身亦為 CAD 危險因子，效益風險權衡複雜。

**L5 Hold 適應症（麻風病、肺囊蟲肺炎、ALCAPA 等）：**
建議暫不推進，待更多機轉或前臨床研究資料出現後重新評估。

---

