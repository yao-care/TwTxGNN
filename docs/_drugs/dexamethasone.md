---
layout: default
title: Dexamethasone
parent: 高證據等級 (L1-L2)
nav_order: 80
evidence_level: L2
indication_count: 10
---

# Dexamethasone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Dexamethasone：從風濕性關節炎到圓禿（Alopecia Areata）

## 一句話總結

Dexamethasone 是一種強效合成糖皮質素，台灣許可適應症涵蓋風濕性關節炎、過敏症、支氣管氣喘等炎症性疾病，在台灣已有 20 張許可證上市。
TxGNN 模型預測它可能對**圓禿（Alopecia Areata）** 有效，目前有 **20 篇文獻**直接支持此方向（含 1 個 RCT、多項前瞻性世代研究），另有 13 筆臨床試驗登記提供 Dexamethasone 在不同情境下的安全性背景資料。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏症、關節炎、風濕痛 |
| 預測新適應症 | 圓禿（Alopecia Areata） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

圓禿（Alopecia Areata）是一種自體免疫性非瘢痕性脫髮，核心病理為 **CD8⁺ T 細胞及 NKG2D⁺ 細胞**對毛囊的免疫攻擊，導致正常毛囊「免疫特赦」（immune privilege）狀態崩潰，促炎細胞激素 **IFN-γ 及 IL-2** 的過度分泌是驅動疾病進展的關鍵機轉。

Dexamethasone 作為強效糖皮質素，透過廣泛的免疫抑制作用——下調 IFN-γ、IL-2 等促炎細胞激素，抑制 T 細胞對毛囊的自體免疫攻擊——理論上可恢復毛囊的免疫特赦狀態，進而促進毛髮再生。此機轉與圓禿的核心病理**高度契合**。

在臨床上，「Dexamethasone Mini-Pulse 療法」（每週連續兩日口服脈衝，或間歇性靜脈脈衝）已在皮膚科實踐中廣泛用於治療廣泛性圓禿，並有直接的 RCT 及多項前瞻性世代研究驗證療效，屬於有具體療效數據支撐的合理再利用方向。

---

## 臨床試驗證據

> ⚠️ **說明**：以下 13 筆臨床試驗登記均為 Dexamethasone 在癌症治療中作為止吐或支持性用藥的試驗（相關性等級 C），尚非直接研究圓禿的試驗。針對圓禿的直接療效證據請見下方「文獻證據」章節。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要情境 |
|---------|------|------|------|---------|
| [NCT01126736](https://clinicaltrials.gov/study/NCT01126736) | Phase 1/2 | 完成 | 98 | Eribulin + Pemetrexed 治療非小細胞肺癌，Dexamethasone 作為化療前驅藥 |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | 完成 | 380 | 探討類固醇代謝異常對骨密度及體組成的影響（MACS 患者，提供長期皮質素安全性資料） |
| [NCT01866449](https://clinicaltrials.gov/study/NCT01866449) | Phase 2 | 完成 | 24 | Cabazitaxel 治療復發性膠質母細胞瘤，Dexamethasone 控制腦水腫 |
| [NCT01215916](https://clinicaltrials.gov/study/NCT01215916) | Phase 1 | 完成 | 39 | LY573636 + Pemetrexed 治療實體腫瘤，Dexamethasone 作為化療前驅藥 |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | 完成 | 56 | Durvalumab + Lenalidomide ± Dexamethasone 治療新診斷多發性骨髓瘤 |
| [NCT02004275](https://clinicaltrials.gov/study/NCT02004275) | Phase 1/2 | 未知 | 118 | Pomalidomide + Dexamethasone ± Ixazomib 治療復發性多發性骨髓瘤 |
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | 未知 | 74 | Dexamethasone 預防 Regorafenib 引起的疲勞（大腸直腸癌，安慰劑對照） |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | 完成 | 19 | Cisplatin + Pemetrexed + Imatinib 治療惡性間皮瘤，Dexamethasone 為標準前驅藥 |
| [NCT01055496](https://clinicaltrials.gov/study/NCT01055496) | Phase 1 | 完成 | 103 | R-CVP/R-GDP + Inotuzumab Ozogamicin 治療 CD22⁺ 非霍奇金淋巴瘤 |
| [NCT00282087](https://clinicaltrials.gov/study/NCT00282087) | Phase 2 | 完成 | 47 | Gemcitabine/Docetaxel + Doxorubicin 輔助化療治療高危子宮平滑肌肉瘤 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | 低劑量 Dexamethasone OMP 與 DPCP 接觸致敏在兒童重度圓禿療效的隨機對照比較 |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | 系統性回顧／網絡統合分析 | Archives of Dermatological Research | 全身性類固醇、JAK 抑制劑、接觸免疫療法治療重度圓禿的比較療效網絡統合分析 |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | 前瞻性世代研究 | Journal of Clinical Medicine | Dexamethasone Mini-Pulse 療法的真實世界療效及治療反應相關因子 |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | 世代研究 | Dermatologic Therapy | 口服 Dexamethasone Mini-Pulse 治療中重度圓禿多中心研究結果 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | 文獻回顧 | Pediatric Dermatology | 兒童圓禿脈衝劑量皮質素療法的劑量方案與副作用文獻整理 |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | 前瞻性世代研究 | Dermatologic Therapy | 靜脈 Dexamethasone 脈衝（1 天 vs 3 天方案）治療重度兒童圓禿的療效比較 |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | 世代研究 | Dermatologic Therapy | 口服脈衝聯合局部皮質素治療重度兒童圓禿長期追蹤（中位追蹤 96 個月） |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | 病例系列 | Journal of Dermatological Treatment | JAK 抑制劑禁忌時，Dexamethasone OMP 誘導嚴重圓禿持久緩解的案例與文獻回顧 |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | 比較研究 | Dermatology (Basel) | 三種全身性皮質素療法治療廣泛性圓禿的療效、復發率及副作用比較 |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | 病例系列 | Journal of Dermatology | 每週 5 mg Dexamethasone 口服脈衝治療廣泛性圓禿 30 例，完全再生率 57% |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第004497號 | "華琳"敵掃風濕錠 | 錠劑 | 過敏症、關節炎、風濕痛 |
| 內衛藥製字第004512號 | "福元"得美爽錠 0.5 毫克 | 錠劑 | 風濕熱、風濕性關節炎、斯替耳氏病、支氣管氣喘、過敏性皮炎 |
| 內衛藥製字第006657號 | 利解痛 1MG/ML 注射液 | 注射劑 | 風濕性關節炎、氣喘、慢性皮膚炎 |
| 內衛藥製字第006720號 | 得確素寧片 | 錠劑 | 風濕性關節炎、風濕熱、支氣管性氣喘、皮膚炎、天疱瘡、肉芽腫、侵襲性休克... |
| 內衛藥輸字第004760號 | 歐樂得爽注射劑 | 注射劑 | 風濕性關節炎、休克 |

---

## 安全性考量

**藥物交互作用**（DDInter 資料庫，共 913 筆，以下列出主要交互作用）：

| 等級 | 藥物 |
|------|------|
| **Major** | Fentanyl、Adalimumab |
| **Moderate** | Paclitaxel、Ibuprofen、Ketorolac、Nifedipine、Acarbose（血糖影響）、Zidovudine、Acebutolol、Abemaciclib、Isotretinoin、Acetazolamide、Dihydrocodeine、Codeine |
| **Minor** | Dolutegravir、Lidocaine、Formoterol |

> 完整 DDI 資訊（913 筆）請查閱 DDInter 2.0 資料庫或諮詢臨床藥師。其他安全性警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Dexamethasone Mini-Pulse 療法已有直接 RCT（Mahajan et al., 2022）及多項前瞻性世代研究支持其在中重度圓禿中的療效，抑制毛囊自體免疫攻擊的機轉與圓禿病理高度吻合，達到 L2 證據等級；惟長期全身性皮質素使用具已知安全性疑慮，需設定監測護欄後方可推進。

**若要推進需要：**
- 補充 Dexamethasone 完整 DrugBank MOA 資料，強化機轉關聯性說明
- 制定標準化療效監測計畫（建議採用 SALT score 評估毛髮再生比例）
- 建立長期使用全身性皮質素的安全性監測方案（骨密度、HPA 軸功能、血糖、眼壓、感染風險）
- 明確界定目標族群：重度/廣泛性圓禿（SALT ≥ 50%）且 JAK 抑制劑禁忌或無法取得的患者
- 評估與已核准 JAK 抑制劑（Baricitinib、Ritlecitinib）的競爭定位及組合使用潛力
---

