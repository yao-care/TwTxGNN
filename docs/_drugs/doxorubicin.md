---
layout: default
title: Doxorubicin
parent: 高證據等級 (L1-L2)
nav_order: 86
evidence_level: L1
indication_count: 1
---

# Doxorubicin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Doxorubicin：從瀰漫性大型 B 細胞淋巴瘤到 Ewing 肉瘤

## 一句話總結

Doxorubicin（鹽酸多柔比星）是 anthracycline 類傳統細胞毒性化療藥物，在台灣核准用於瀰漫性大型 B 細胞淋巴瘤（DLBCL）等抗腫瘤聯合化療方案。TxGNN 模型預測它可能對 **Ewing 肉瘤（Ewing Sarcoma）** 有效，目前有 **47 個臨床試驗**和 **20 篇文獻**支持這個方向，且多項已完成的 Phase 3 RCT 直接確立其在 Ewing 肉瘤治療中的核心地位。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 瀰漫性大型 B 細胞淋巴瘤（DLBCL） |
| 預測新適應症 | Ewing 肉瘤（Ewing Sarcoma） |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Doxorubicin 透過嵌入 DNA 雙螺旋並抑制拓撲異構酶 IIα（Topoisomerase IIα），造成 DNA 雙鏈斷裂，阻礙腫瘤細胞的 DNA 複製與轉錄，進而誘導細胞凋亡。此機轉對高度增殖的腫瘤細胞具優先細胞毒性，因此理論上適用於任何快速分裂的惡性腫瘤。

Ewing 肉瘤是第二常見的兒童原發骨腫瘤，其特徵為 EWS-FLI1 融合蛋白高度表現，細胞增殖旺盛，對 DNA 損傷機轉的化療藥物尤為敏感。Doxorubicin 自 1970 年代起即是國際 Ewing 肉瘤標準化療方案 **VAC/IE**（vincristine-doxorubicin-cyclophosphamide 交替 ifosfamide-etoposide）的核心藥物，現代多中心 Phase 3 RCT（包括 EURO-E.W.I.N.G. 99、AEWS0031 等）已直接確立其療效地位。

值得注意的是，本次 TxGNN 預測實際上反映了 doxorubicin 在 Ewing 肉瘤中**已建立的標準臨床角色**，預測分數高達 99.90% 與 L1 等級的豐富臨床試驗證據高度吻合，進一步驗證了 TxGNN 模型的預測可靠性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 完成 | 642 | 隨機試驗比較 VTC 加入含 doxorubicin 標準 VDC/IE 方案用於非轉移性 Ewing 肉瘤，為本適應症最高品質直接證據之一 |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 不明 | 1200 | EURO-E.W.I.N.G. 99 大型多中心試驗，doxorubicin 為標準誘導方案核心，係 Ewing 肉瘤最重要的奠基性試驗 |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 完成 | 587 | 隨機比較化療壓縮間隔策略用於 Ewing 肉瘤及 PNET，評估不同含 doxorubicin 方案療效 |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 完成 | 278 | 隨機評估非轉移性 Ewing 肉瘤劑量強化方案（含 doxorubicin 誘導）對無事件存活的影響 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 進行中 | 312 | 隨機評估 IGF-1R 單株抗體 ganitumab 加入含 doxorubicin 間隔壓縮化療用於新確診轉移性 Ewing 肉瘤 |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | 進行中 | 437 | 隨機比較 VIrR 方案聯合 VDC/IE（含 doxorubicin）用於新確診轉移性 Ewing 肉瘤 |
| [NCT01946529](https://clinicaltrials.gov/study/NCT01946529) | Phase 2 | 進行中 | 24 | Ewing 肉瘤家族腫瘤（ESFT）及 DSRCT 治療試驗，依腫瘤特徵分組，doxorubicin 為方案核心藥物 |
| [NCT00002601](https://clinicaltrials.gov/study/NCT00002601) | Phase 2 | 完成 | 13 | 直接評估高劑量 doxorubicin + ifosfamide 序貫 melphalan + cisplatin 用於高危復發 Ewing 肉瘤 |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | 完成 | 155 | 高劑量化療 + 放療 + cyclophosphamide 鞏固治療用於轉移性 Ewing 肉瘤，doxorubicin 為誘導方案成份 |
| [NCT00544778](https://clinicaltrials.gov/study/NCT00544778) | Phase 2 | 已終止 | 7 | 新輔助高劑量 doxorubicin + ifosfamide + irinotecan 用於晚期 Ewing 肉瘤，雖提前終止仍為直接藥物-疾病配對 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 加入 ifosfamide + etoposide 至含 doxorubicin 標準化療顯著改善新確診 Ewing 肉瘤存活率，奠定 VAC/IE 標準方案基礎 |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | AEWS0031：間隔壓縮含 doxorubicin 化療（VDC/IE）較標準間隔顯著改善局部 Ewing 肉瘤無事件存活率 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012 Phase 3 試驗直接比較歐美兩種含 doxorubicin 標準化療方案（VDC/IE vs VIDE）用於新確診 Ewing 肉瘤 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT | Trials | EURO EWING 2012 國際多中心隨機對照試驗完整方案，評估新藥加入含 doxorubicin 誘導方案的療效 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | COG AEWS1221 Phase 3：ganitumab 加入含 doxorubicin 間隔壓縮化療未能改善轉移性 Ewing 肉瘤 EFS |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | RCT | J Clin Oncol | Ewing 2008R3 Phase 3（12 國）：高劑量 TreoMel 鞏固療法用於含 doxorubicin 誘導後之高危 Ewing 肉瘤 |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Cohort | J Clin Oncol | AEWS0031 長期隨訪：間隔壓縮含 doxorubicin 方案局部 Ewing 肉瘤的長期預後更新分析 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Ewing 肉瘤診療綜述：現代多藥化療（含 doxorubicin）將局部腫瘤 5 年存活率從化療前 10% 提升至約 75% |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Ewing 肉瘤多中心協作治療現況綜述，含 doxorubicin 之風險適應性強化化療與局部控制策略 |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Analysis | J Natl Cancer Inst | 劑量強度分析確認 doxorubicin 為 Ewing 肉瘤預後最相關的化療藥物之一，奠定劑量強度策略基礎 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部菌疫輸字第001123號 | 保癌寧 凍晶注射劑 | 凍晶注射劑 | 1. 與 rituximab、cyclophosphamide、doxorubicin 和 prednisone (R-CHP) 併用，適用於治療先前未接受過治療之瀰漫性大型 B 細胞淋巴瘤（DLBCL）成人病人。2. 與 bendamustine 和 rituximab 併用，適用於治療復發型或難治型且不適合造血幹細胞移植的 DLBCL 病人... |

> **資料說明**：Evidence Pack 中所列 20 張許可證均登記為相同許可證號（衛部菌疫輸字第001123號），疑為資料彙整重複。建議查詢 TFDA 資料庫確認 Doxorubicin（鹽酸多柔比星）完整許可證清單，以補充更準確的上市資訊。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Anthracycline 類 / 拓撲異構酶 II 抑制劑） |
| 骨髓抑制風險 | **高度**（常見嗜中性白血球減少、血小板減少、貧血，為劑量限制性毒性） |
| 致吐性分級 | 中至高度（依給藥劑量及方案而定） |
| 監測項目 | CBC（含白血球分類計數）、心臟功能（LVEF / 心臟超音波，治療前及治療中追蹤）、肝腎功能、累積劑量記錄（成人建議 ≤550 mg/m²，有心臟危險因子者 ≤400 mg/m²） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；本藥為**發泡劑（vesicant）**，外滲可導致嚴重組織壞死，靜脈給藥需特別謹慎；心毒性（心肌病變）為累積劑量依賴性長期副作用，必要時考慮 dexrazoxane 心臟保護 |

---

## 安全性考量

**藥物交互作用**（Evidence Pack 顯示共 665 個已知交互作用，以下列出代表性項目）：

| 相互作用藥物 | 嚴重程度 | 備注 |
|------------|---------|------|
| Dolasetron | **Major** | 止吐劑，嚴重交互作用需避免併用 |
| Cisapride | **Major** | 腸胃動力藥，嚴重交互作用需避免併用 |
| Papaverine | **Major** | 血管擴張劑，嚴重交互作用需避免併用 |
| Clarithromycin | Moderate | 大環內酯類抗生素，CYP3A4 抑制劑 |
| Dexamethasone | Moderate | 常用止吐/前置用藥，需注意劑量調整 |
| Ondansetron | Moderate | 5-HT3 拮抗止吐劑，監測 QT 間期延長 |
| Granisetron | Moderate | 5-HT3 拮抗止吐劑，監測 QT 間期延長 |
| Palonosetron | Moderate | 5-HT3 拮抗止吐劑，監測 QT 間期延長 |
| Aprepitant | Moderate | NK1 受體拮抗止吐劑，可能影響代謝 |
| Levofloxacin | Moderate | 氟喹諾酮類抗生素，監測心律 |

> Doxorubicin 已知藥物交互作用達 **665 個**，使用前應全面評估病患完整用藥清單，尤其注意止吐藥（5-HT3 拮抗劑）與心律相關的 QT 延長風險。詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Doxorubicin 在 Ewing 肉瘤治療中具備多項已完成的 Phase 3 RCT 直接支持（L1 等級證據），已是 VAC/IE 國際標準方案的核心藥物，TxGNN 預測結果（99.90%）與現有臨床實踐高度吻合。本案屬**已確立用途的再確認**，而非全新適應症開發，推進時主要聚焦於安全性管理與特定族群的風險評估。

**若要推進需要：**
- 補充完整 DrugBank MOA 資料（目前標記為 Data Gap），以強化機轉關聯性分析
- 建立心毒性監測計畫（治療前基準 LVEF 評估、治療中定期追蹤、累積劑量上限管理）
- 針對 665 個已知 DDI 進行完整用藥核對，尤其是 CYP3A4 抑制劑與 QT 延長風險藥物
- 補充 TFDA 正式 Doxorubicin 許可證清單，釐清 Evidence Pack 中重複登記的資料問題
- 考量 Ewing 肉瘤族群（多為兒童/青少年）的長期心毒性監測與晚期效應追蹤計畫

---

