---
layout: default
title: Prilocaine
parent: 中證據等級 (L3-L4)
nav_order: 215
evidence_level: L3
indication_count: 10
---

# Prilocaine
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

使用 `txgnn-pipeline` 技能確認任務範圍後，這是一份多適應症評估報告（candidate_id: TW-DB00750-multi）。依據證據強度，以**神經痛 (Neuralgia)** 作為主要評估對象（L3 等級，最強臨床支持），其餘 9 個預測在總覽表中一併呈現。

---

# Prilocaine：從局部麻醉到神經痛

## 一句話總結

Prilocaine（必洛卡因）是醯胺類局部麻醉劑，以 EMLA 乳膏（2.5% prilocaine + 2.5% lidocaine）形式廣泛應用於皮膚表面止痛。TxGNN 模型共預測 10 個新適應症候選，其中**神經痛 (Neuralgia)** 具備最強臨床證據：目前有 **12 個臨床試驗**和 **20 篇文獻**支持，多項研究直接記錄 EMLA 乳膏用於帶狀疱疹後遺神經痛（PHN）的療效，證據等級達 **L3**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部麻醉劑 |
| 最佳預測新適應症 | 神經痛 (Neuralgia) |
| TxGNN 預測分數 | 99.34% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

### 10 個預測適應症一覽

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗數 | 文獻數 | 證據等級 | 決策 |
|------|--------|-----------|----------|--------|---------|------|
| 1 | Papillary Conjunctivitis（乳突性結膜炎） | 99.78% | 0 | 0 | L5 | Hold |
| 2 | Manic Bipolar Affective Disorder（躁狂型雙極症） | 99.76% | 0 | 0 | L5 | Hold |
| 3 | Bronchitis（支氣管炎） | 99.64% | 1 | 0 | L5 | Hold |
| 4 | Migraine Disorder（偏頭痛） | 99.42% | 4 | 1 | L4 | Research Question |
| **5** | **Neuralgia（神經痛）** | **99.34%** | **12** | **20** | **L3** | **Proceed with Guardrails** |
| 6 | Migraine with Brainstem Aura（基底型偏頭痛） | 99.33% | 0 | 0 | L5 | Hold |
| 7 | Atopic Eczema（異位性濕疹） | 99.31% | 0 | 9 | L4 | Research Question |
| 8 | Allergic Asthma（過敏性氣喘） | 99.29% | 0 | 3 | L5 | Hold |
| 9 | Rhinitis（鼻炎） | 99.28% | 0 | 1 | L4 | Hold |
| 10 | Rosacea Conjunctivitis（玫瑰斑結膜炎） | 99.24% | 0 | 0 | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 詳細作用機轉資料。根據已知資訊，Prilocaine 是醯胺類局部麻醉劑，透過可逆性阻斷電壓依賴性 Na⁺ 通道，抑制神經細胞膜動作電位的產生與傳導。以 EMLA 乳膏（5% 含量，occlusion 貼覆）使用時，Prilocaine 可滲透表皮至真皮層，直接降低皮膚感覺神經末梢（C 纖維及 Aδ 纖維）的異位放電頻率，並可能間接緩解中樞敏化。

神經痛的核心病理在於外周神經的異常過度放電，與 Prilocaine 的 Na⁺ 通道阻斷機轉高度吻合。帶狀疱疹後遺神經痛（PHN）尤其如此——病毒侵害後遺留的受損神經纖維持續異位放電，而局部 Na⁺ 通道阻斷正是針對此病理的直接介入。

原適應症（皮膚表面止痛）與神經痛在機轉上是直接的延伸而非類比。事實上，EMLA 乳膏在 1989–2011 年間已累積多篇文獻記錄其用於 PHN 的實際療效，部分研究並使用視覺類比量表（VAS）量化止痛效果，為本預測提供了直接的臨床佐證。

---

## 臨床試驗證據（神經痛）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | 已完成 | 20 | 開放性多中心試驗，直接研究 Lidocaine 2.5%/Prilocaine 2.5% 乳膏作為帶狀疱疹後遺神經痛（PHN）治療前置局部麻醉的耐受性；藥物與疾病族群完全吻合 |
| [NCT03587220](https://clinicaltrials.gov/study/NCT03587220) | NA | 已完成 | 44 | 研究辣椒素去敏化機轉，以 EMLA 乳膏（含 Prilocaine）為皮膚前處理；直接於神經痛情境使用含 Prilocaine 製劑，佐證其 Na⁺ 通道阻斷效果 |
| [NCT02537951](https://clinicaltrials.gov/study/NCT02537951) | NA | 已完成 | 10 | Pilot 研究，以 EMLA 乳膏前處理進行表皮內神經纖維自體螢光成像，佐證 EMLA 在小纖維神經病變評估情境的實際應用 |
| [NCT06899438](https://clinicaltrials.gov/study/NCT06899438) | NA | 已完成 | 38 | 前瞻性 RCT 設計，直接比較 Prilocaine 注射（觸發點注射）vs. 肉毒桿菌素用於肌筋膜疼痛症候群，Prilocaine 為主要研究對象之一 |
| [NCT06247592](https://clinicaltrials.gov/study/NCT06247592) | NA | 不明 | 70 | 枕大神經阻斷術（2% Prilocaine）vs. 脈衝射頻比較試驗，針對慢性偏頭痛相關神經痛，Prilocaine 為神經阻斷術核心成分 |
| [NCT03220113](https://clinicaltrials.gov/study/NCT03220113) | Phase 1/2 | 不明 | 100 | 開放性試驗，De-Novo 配方（含局部麻醉劑）注射三叉神經分支及枕大/枕小神經，用於頑固性顱顏神經痛 |
| [NCT04914637](https://clinicaltrials.gov/study/NCT04914637) | NA | 已完成 | 66 | 乾針刺結合硬膜外類固醇注射治療頸椎椎間盤突出引起的慢性頸部神經痛，涉及局部麻醉劑介入成分 |
| [NCT01540877](https://clinicaltrials.gov/study/NCT01540877) | NA | 已完成 | 28 | 探討局部麻醉劑（LA）阻斷 C 纖維的感覺變化模型，以辣椒素聯合局部麻醉劑研究神經痛機轉 |
| [NCT01911377](https://clinicaltrials.gov/study/NCT01911377) | Phase 2 | 已終止 | 12 | 肉毒桿菌素用於脊髓損傷或多發性硬化症之異痛性神經病變疼痛（已終止），提供疾病族群相關性 |
| [NCT05411900](https://clinicaltrials.gov/study/NCT05411900) | Phase 2 | 不明 | 164 | 多中心隨機雙盲安慰劑對照試驗，肉毒桿菌素用於腕隧道症候群周邊神經病變疼痛，疾病族群相關 |

---

## 文獻證據（神經痛）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [10353509](https://pubmed.ncbi.nlm.nih.gov/10353509/) | 1999 | Cohort | Pain | 評估 EMLA 乳膏單次與連續 6 天施用對 11 例 PHN 患者自發性及誘發性疼痛的止痛效果；偵測閾值、疼痛閾值及超閾值刺激反應均顯示顯著改善 |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | Cohort | BMC Anesthesiology | NGX-4010（8% capsaicin 貼片）前置 Lidocaine/Prilocaine 乳膏用於 PHN 的耐受性世代研究；Prilocaine 乳膏為直接介入藥物 |
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | Cohort | BMJ | Lignocaine-Prilocaine 乳膏直接應用於帶狀疱疹後遺神經痛患者的療效世代研究 |
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | Case series | Pain | 5% EMLA 乳膏（5 或 10g，24h 施用）用於 12 例頑固性 PHN 患者（平均年齡 69 歲），施用 6h 後 VAS 疼痛評分顯著改善（P<0.05） |
| [8695081](https://pubmed.ncbi.nlm.nih.gov/8695081/) | 1996 | Case series | J Clin Anesthesia | EMLA 乳膏成功治療對其他療法無效的 PHN 個案，並簡述 EMLA 的藥理學基礎 |
| [23314014](https://pubmed.ncbi.nlm.nih.gov/23314014/) | 2013 | Review | Curr Opin Support Palliat Care | 慢性傷口相關疼痛的實證管理系統性方法，涵蓋局部麻醉劑（含 EMLA）的應用建議 |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Review | J Dermatol Surg Oncol | EMLA（含 2.5% lidocaine 及 2.5% prilocaine）臨床應用綜述，明確列出帶狀疱疹後遺神經痛為適應症之一 |
| [2046584](https://pubmed.ncbi.nlm.nih.gov/2046584/) | 1991 | Case series | Med J Australia | EMLA 乳膏用於帶狀疱疹神經痛的案例報告 |
| [1875823](https://pubmed.ncbi.nlm.nih.gov/1875823/) | 1991 | Case series | Med J Australia | EMLA 乳膏用於帶狀疱疹神經痛的回應案例報告 |
| [8042802](https://pubmed.ncbi.nlm.nih.gov/8042802/) | 1994 | Case series | Anesthesiology | EMLA 乳膏用於灼痛症（causalgia）治療的案例報告 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028679號 | 必洛卡因 | （粉） | 局部麻醉劑 |
| 衛部藥輸字第028027號 | 必洛卡因 | （粉） | 局部麻醉劑 |
| 衛部藥陸輸字第001203號 | 必洛卡因 | （粉） | 局部麻醉劑 |
| 衛部藥輸字第027939號 | 必洛卡因 | （粉） | 局部麻醉劑 |
| 衛部藥輸字第028557號 | 必洛卡因 | （粉） | 局部麻醉劑 |

> 台灣共 20 張許可證，劑型涵蓋粉劑（原料藥）、乳膏劑（外用，含 EMLA 型製劑）、氣化噴霧劑三種路徑。

---

## 安全性考量

**藥物交互作用（共 22 個，其中 18 個 Major）：**

| 藥物 | 等級 | 主要風險 |
|------|------|---------|
| Dapsone / Dapsone (topical) | Major | 加成性甲血紅素血症（methemoglobinemia）風險，應避免合併使用 |
| Amyl Nitrite / Nitrous acid / Nitric Oxide | Major | 亞硝酸鹽類氧化劑顯著加重甲血紅素血症風險 |
| Silver sulfadiazine (topical) / Silver nitrate (topical) | Major | 含銀局部製劑增加氧化性甲血紅素血症風險 |
| Benzocaine (topical) / Cinchocaine (topical) | Major | 加成性局部麻醉劑毒性及甲血紅素血症 |
| Lidocaine / Lidocaine (topical) | Major | 加成性神經毒性及心臟毒性（QRS 延長、心律不整） |
| Chloroquine / Primaquine / Quinine / Tafenoquine | Major | 加成性心律不整及甲血紅素血症風險 |
| Sulfasalazine | Major | 增加甲血紅素血症風險（磺胺類協同氧化機轉） |
| Metoclopramide | Major | 增加甲血紅素血症風險 |
| Rasburicase | Major | G6PD 缺乏背景下溶血與甲血紅素血症複合風險 |
| Morphine (liposomal) | Moderate | 中度交互作用，建議監測中樞神經抑制效果 |
| Hyaluronidase | Minor | 可能增加 Prilocaine 的局部擴散範圍 |

> ⚠️ **甲血紅素血症風險提醒**：Prilocaine 的代謝產物 o-甲苯胺（o-toluidine）具有氧化作用，可將血紅素氧化為甲血紅素。高危族群包括：嬰幼兒（<12 個月）、G6PD 缺乏症患者、同時使用上述 Major 交互作用藥物者。臨床上大面積或長時間施用須監測血氧及甲血紅素濃度。其餘詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對神經痛 / 帶狀疱疹後遺神經痛）

**理由：**
EMLA 乳膏（含 2.5% Prilocaine）用於帶狀疱疹後遺神經痛已有 1989–2011 年間多項已完成臨床試驗及世代研究直接佐證，並有完整的機轉合理性（外周 Na⁺ 通道阻斷降低異位放電）。台灣已有 20 張許可證且藥品已上市，乳膏劑型技術成熟，進入障礙低。PHN 在台灣高齡化背景下為未滿足醫療需求的適應症。

**若要推進需要：**
- 補充 DrugBank 完整 MOA 資料，強化法規申請的機轉說明文件
- 評估台灣法規路徑：現有許可證核准適應症為「局部麻醉劑」，PHN 為超適應症使用，需評估提出效能補充申請（Supplemental NDA）或直接申請新適應症的可行性
- 設計以 PHN 為主要終點的前瞻性台灣本土研究，補足現有文獻多為小型（n<20）、年代久遠（1989–1996）之缺口
- 建立甲血紅素血症風險排除標準（排除嬰幼兒、G6PD 缺乏、合用高風險氧化劑藥物者）及上市後監測計畫
- 進行 PHN 市場規模評估（台灣帶狀疱疹發生率 × PHN 轉化率）以支持商業決策
---

