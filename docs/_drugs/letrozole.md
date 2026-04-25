---
layout: default
title: Letrozole
parent: 高證據等級 (L1-L2)
nav_order: 153
evidence_level: L1
indication_count: 10
---

# Letrozole
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

# Letrozole：從停經後乳癌到女性乳癌

## 一句話總結

Letrozole（立妥芙）是第三代非固醇性芳香化酶抑制劑，台灣已核准用於停經後荷爾蒙受體陽性乳癌的多種治療情境，包括末期治療、第一線晚期/轉移性治療，以及輔助與延伸輔助治療。
TxGNN 模型預測它對**女性乳癌 (Female Breast Carcinoma)** 有效，預測分數高達 **99.98%**，此結果確認並延伸了現有核准適應症的廣泛適用範疇，
目前有超過 **40 個臨床試驗**和 **20 篇文獻**支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 停經後末期乳癌、局部晚期/轉移性乳癌第一線、荷爾蒙受體陽性初期乳癌輔助治療 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

DrugBank 正式作用機轉（MOA）欄位目前缺乏資料，但根據現有文獻，Letrozole 是第三代非固醇性芳香化酶抑制劑，透過選擇性且可逆地抑制 **CYP19A1（芳香化酶）**，阻斷腎上腺雄激素（如雄烯二酮、睪固酮）轉化為雌二醇的生化路徑，使停經後婦女體內雌激素水平大幅下降（降幅超過 95%），直接剝奪雌激素受體（ER）陽性乳癌細胞的增殖信號。

TxGNN 預測 Letrozole 對「女性乳癌」有效，實質上是對其核准適應症的模型確認。台灣現行核准範圍涵蓋停經後 ER 陽性乳癌的末期、局部晚期/轉移性（第一線）、輔助及延伸輔助治療等多個情境；而「女性乳癌」作為更廣義的病理類別，代表模型捕捉到 Letrozole 在乳癌治療體系中的核心地位。

值得注意的是，Letrozole 近年已成為多個 CDK4/6 抑制劑（Palbociclib、Ribociclib、Abemaciclib）的標準內分泌治療搭配藥物。大型 Phase 3 試驗（MONALEESA-2、PALOMA-2、BIG 1-98）不斷擴展其在 HR+/HER2− 乳癌各臨床情境中的標準治療地位，這些豐富的機轉與臨床證據正是 TxGNN 給出 99.98% 高分的基礎。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02297438](https://clinicaltrials.gov/study/NCT02297438) | Phase 3 | 完成 | 340 | PALOMA-2 亞洲族群：比較 Palbociclib+Letrozole vs 安慰劑+Letrozole，用於未治療 ER+/HER2− 停經後晚期乳癌 |
| [NCT01958021](https://clinicaltrials.gov/study/NCT01958021) | Phase 3 | 完成 | 668 | MONALEESA-2：評估 Ribociclib 合併 Letrozole 於 HR+/HER2− 晚期乳癌一線治療的無進展存活期 |
| [NCT00265759](https://clinicaltrials.gov/study/NCT00265759) | Phase 3 | 完成 | 622 | 停經後 Stage II-III ER+ 乳癌：比較 Exemestane、Letrozole、Anastrozole 16-18 週新輔助療效 |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | 已終止 | 123 | DBCG 試驗：評估 Letrozole 4 個月作為停經後 HR+ 早期乳癌初始治療 vs 手術優先策略 |
| [NCT00171314](https://clinicaltrials.gov/study/NCT00171314) | Phase 3 | 完成 | 527 | 停經後乳癌接受 Letrozole 輔助治療期間，比較立即 vs 延遲 Zoledronic acid 預防骨密度流失 |
| [NCT01573442](https://clinicaltrials.gov/study/NCT01573442) | Phase 3 | 完成 | 227 | Anastrozole 或 Letrozole 引起的關節痛：睪固酮 vs 安慰劑輔助治療的隨機對照試驗 |
| [NCT05183828](https://clinicaltrials.gov/study/NCT05183828) | Phase 4 | 招募中 | 68 | 評估 HSD3B1 基因型（1245C 突變）是否降低 Letrozole 術前治療療效（Stage I-III ER+/HER2−） |
| [NCT00535418](https://clinicaltrials.gov/study/NCT00535418) | Phase 2/3 | 完成 | 35 | 停經後 ER/PgR 陽性乳癌術前 Letrozole 最適治療時間評估，並建立療效替代標記的相關性 |
| [NCT03111615](https://clinicaltrials.gov/study/NCT03111615) | Phase 4 | 未知 | 90 | 探討組織確診後立即啟動 Letrozole 治療對腫瘤生物特性的潛在影響 |
| [NCT02679755](https://clinicaltrials.gov/study/NCT02679755) | Phase 4 | 完成 | 252 | Palbociclib+Letrozole 用於 HR+/HER2− 停經後晚期乳癌的真實世界療效與安全性觀察 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Res Treat | PALOMA-1 整體存活分析：Palbociclib+Letrozole vs Letrozole 單藥，中位 PFS 20.2 vs 10.2 個月 |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | RCT | Comput Math Methods Med | Tamoxifen 序貫治療 vs Letrozole 單藥治療乳癌的療效、安全性與患者預後比較 |
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | N Engl J Med | BIG 1-98 試驗：Letrozole 優於 Tamoxifen 作為停經後早期 HR+ 乳癌的輔助治療 |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Letrozole 藥理機轉、毒性及潛在治療效果的全面性系統回顧 |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Letrozole 藥動學、藥效學及臨床療效與安全性的專家完整評述 |
| [35378469](https://pubmed.ncbi.nlm.nih.gov/35378469/) | 2022 | Cohort | Curr Probl Cancer | Palbociclib+Letrozole 於 HR+ 晚期乳癌：反應預測因子與預後因子的多因素分析 |
| [34645649](https://pubmed.ncbi.nlm.nih.gov/34645649/) | 2022 | Cohort | Clin Cancer Res | ER+/HER2− 乳癌中 Palbociclib+Letrozole 的抗增殖反應、藥動效應及抗藥性生物標記 |
| [29229198](https://pubmed.ncbi.nlm.nih.gov/29229198/) | 2017 | Cohort | Arch Med Res | Raloxifene 合併 Letrozole 對 MCF-7 乳癌細胞株及 HEK 細胞的細胞毒性效應評估 |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast | Letrozole 開發歷程、晚期乳癌應用與新輔助治療情境的全面性回顧 |
| [27235140](https://pubmed.ncbi.nlm.nih.gov/27235140/) | 2016 | In vitro | Med Oncol | Letrozole 誘導腫瘤相關纖維母細胞（CAF）功能改變，進而影響乳癌細胞的內分泌療效 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028712號 | 立妥芙膜衣錠2.5毫克 | 膜衣錠 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥... |
| 衛部藥輸字第027594號 | 利妥唑 | （粉） | 非固醇性抗雌激素藥 |
| 衛部藥輸字第026313號 | 萊特汝膜衣錠2.5毫克 | 膜衣錠 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥... |
| 衛部藥輸字第026333號 | 艾爾芬膜衣錠2.5毫克 | 膜衣錠 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥... |
| 衛部藥輸字第027448號 | 法萌樂膜衣錠 | 膜衣錠 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥... |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶內分泌治療（非固醇性芳香化酶抑制劑）；**非傳統細胞毒性化療藥物** |
| 骨髓抑制風險 | 低（不具骨髓毒性，不直接抑制造血功能） |
| 致吐性分級 | 低 |
| 監測項目 | 骨密度（DXA 掃描，建議每 1-2 年）、血脂（LDL/HDL）、肝功能（ALT/AST）、骨折風險評估 |
| 處置防護 | 一般口服固體製劑，無需細胞毒性藥物特殊防護規範 |

---

## 安全性考量

**藥物交互作用**（共 259 筆紀錄，以下列出主要項目）：

| 交互藥物 | 嚴重程度 | 說明 |
|---------|---------|------|
| Aprepitant | **中度 (Moderate)** | NK1 受體拮抗劑，可能影響 CYP3A4 代謝路徑，與 Letrozole 合用時需注意血藥濃度變化 |
| Simvastatin | 未知 | 同為 CYP 受質，潛在代謝交互作用有待臨床確認 |
| Prednisone | 未知 | 乳癌患者常合用類固醇，建議監測 |
| Metformin | 未知 | 常見合併症（糖尿病）用藥，潛在影響不明 |
| Omeprazole | 未知 | 常見胃腸道保護劑，潛在影響不明 |

其餘主要警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TxGNN 模型以 99.98% 的高分預測 Letrozole 對女性乳癌有效，完全一致於其台灣現有核准適應症，並獲得多項已完成 Phase 3 RCT（MONALEESA-2、PALOMA-2、BIG 1-98 等）的 L1 等級證據支持。Letrozole 在台灣擁有 20 張許可證，已是乳癌內分泌治療的主流用藥，近年更成為 CDK4/6 抑制劑組合療法的核心搭配藥物，臨床應用持續擴展。

**若要推進需要：**
- 補充正式 DrugBank 作用機轉（MOA）欄位，強化機轉層級的科學論述
- 查閱並更新原廠仿單，填補目前缺漏的主要警語與禁忌症資料
- 建立長期使用者（輔助治療 5-10 年）的骨密度監測與骨折風險管理計畫
- 評估 Letrozole 在特定亞型擴展情境中的定位：停經前合併卵巢抑制、HR+/HER2+ 雙受體陽性、以及新興 CDK4/6 抑制劑後線治療等組合策略
---

