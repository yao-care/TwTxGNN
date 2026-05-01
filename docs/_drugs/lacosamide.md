---
layout: default
title: Lacosamide
parent: 中證據等級 (L3-L4)
nav_order: 149
evidence_level: L3
indication_count: 10
---

# Lacosamide
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

使用 `txgnn-pipeline` 技能確認工作流程後，現在依照 v5 格式撰寫評估報告：

---

# Lacosamide：從癲癇到躁狂雙極性情感疾患

## 一句話總結

Lacosamide（維帕特®、立剋癇®）是第三代抗癲癇藥，台灣核准用於四歲以上局部癲癇發作的單一或輔助治療。TxGNN 模型預測它最高可能對**躁狂雙極性情感疾患 (Manic Bipolar Affective Disorder)** 有效（TxGNN 分數 99.96%），目前有 **1 個 Phase 3 臨床試驗**（招募中）和 **14 篇文獻**支持這個方向；值得注意的是，本次 Evidence Pack 為多適應症報告，其中**偏頭痛 (Migraine Disorder)** 的整體臨床證據等級達 **L1**，是所有預測中最強的候選。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 四歲以上局部癲癇發作之單一藥物治療；複雜性局部癲癇發作及次發性全身發作之輔助治療 |
| 預測新適應症（Rank 1） | 躁狂雙極性情感疾患 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 多適應症預測摘要（本報告涵蓋 10 項）

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|---------|
| 1 | 躁狂雙極性情感疾患 | 99.96% | L3 | Hold |
| 2 | 妥瑞症候群 | 99.95% | L5 | Hold |
| 3 | 拔毛症 | 99.92% | L5 | Hold |
| 4 | 腎因性不適當抗利尿症候群 | 99.91% | L5 | Hold |
| **5** | **偏頭痛** | **99.87%** | **L1** | **Proceed with Guardrails** |
| 6 | 失眠 | 99.83% | L3 | Hold |
| 7 | 腦幹先兆性偏頭痛 | 99.82% | L4 | Research Question |
| 8 | 肌筋膜疼痛症候群 | 99.81% | L2 | Research Question |
| 9 | 強迫症 | 99.78% | L4 | Hold |
| 10 | 乳突性結膜炎 | 99.72% | L5 | Hold |

> ⚠️ **注意**：Rank 5 偏頭痛擁有 3 個已完成的 Phase 3 RCT 及豐富文獻，為最具開發潛力的候選適應症；以下主要章節依格式規範聚焦於 Rank 1（躁狂雙極性情感疾患），偏頭痛詳細評估請另行生成獨立報告。

---

## 為什麼這個預測合理？

目前缺乏 Lacosamide 的詳細 MOA 官方資料。根據現有藥理文獻，Lacosamide 透過**選擇性增強電壓閘控鈉離子通道（Nav）的慢速失活**，抑制過度興奮神經膜的持續放電。這與臨床上已廣泛用於雙極症情緒穩定的多種抗癲癇藥（丙戊酸鈉、拉莫三嗪、卡馬西平）共享高度相似的機轉邏輯——這些藥物均透過調控膜興奮性發揮情緒穩定作用。

Lacosamide 的**次要標靶 CRMP-2**（collapsin response mediator protein 2）是另一個值得關注的作用點。CRMP-2 廣泛參與神經可塑性調控、突觸形成及神經保護訊號傳遞，可能提供超越純粹離子通道阻斷以外的情緒穩定效益，為其用於雙極症提供額外的生物學合理性。

觀察性臨床資料進一步支持此方向：一項 30 天回顧性對照研究及一項 12 週開放標籤先導試驗均顯示 Lacosamide 可改善雙極症患者（包含無癲癇共病者）的躁狂及抑鬱症狀。然而，現有證據等級屬於 L3（觀察性研究），目前唯一登記的 Phase 3 試驗聚焦於「抑鬱發作」而非本預測的「躁狂發作」，機轉-臨床的精準對應仍待驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | 招募中 | 40 | 隨機、雙盲、平行組設計，評估 Lacosamide 作為一線或二線用藥的增強療法，用於雙極症 I 型與 II 型的中至重度重度抑鬱發作。前期觀察性研究提示 Lacosamide 可改善癲癇共病患者的憂鬱與躁狂症狀，本試驗為首個以 BD 患者為主體的對照試驗 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Cohort | J Clin Psychopharmacol | Lacosamide 用於雙極症抑鬱的 12 週開放標籤先導試驗，初步評估療效與安全性 |
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Cohort | Psychiatry Clin Neurosci | 住院雙極症患者（無癲癇共病）使用 Lacosamide vs 其他抗癲癇藥的 30 天回顧性比較，為最直接的雙極症療效觀察數據 |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Cohort | Epilepsy & Behavior | 前瞻性多中心研究：Lacosamide 輔助治療對局部難治性癲癇患者的憂鬱及焦慮症狀有顯著改善，探討其是否具備獨立的精神作用 |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chem Neurosci | CRMP2 作為神經退化與精神疾病的藥物標靶潛力，涵蓋 Lacosamide 透過 CRMP-2 調控神經可塑性的機轉基礎 |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | AED 治療藥物監測 2018 更新；明確指出 Lacosamide 等 AED 在疼痛與雙極症等非癲癇適應症的應用日益廣泛 |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case series | Acta Bio-Med | 情緒障礙合併 PTSD 及額顳葉癲癇病例報告：使用 Lacosamide 後達到臨床穩定化，提供機轉路徑（Nav 慢速失活→膜穩定→情緒穩定）的臨床佐證 |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case series | Cureus | 雙極症 I 型合併癲癇及物質使用障礙的複雜孕婦病例，記錄 Lacosamide 在多重共病管理中的實際使用情境 |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case series | Indian J Psychol Med | **安全性警訊**：雙極症合併癲癇患者使用 Lacosamide 後誘發嗜中性白血球減少症，提示雙極症適應症擴展時需監測血液學參數 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第028686號 | 立剋癇膜衣錠100毫克 | 膜衣錠 | 四歲以上有或無次發性全身發作的局部癲癇發作病人的單一藥物治療；四歲以上複雜性局部癲癇發作及合併次發性全身發作之輔助治療... |
| 衛部藥輸字第028689號 | 立剋癇膜衣錠200毫克 | 膜衣錠 | 四歲以上有或無次發性全身發作的局部癲癇發作病人的單一藥物治療；四歲以上複雜性局部癲癇發作及合併次發性全身發作之輔助治療... |
| 衛部藥輸字第026284號 | 維帕特 50毫克膜衣錠 | 膜衣錠 | 四歲以上局部癲癇發作之單一藥物治療；輔助治療複雜性局部癲癇發作、次發性全身發作，以及原發性全面強直陣攣發作合併特發性全面癲癇... |

> 本資料僅列出 3 張代表性許可證，台灣共有 **20 張**有效許可證，涵蓋多種劑型（膜衣錠、糖漿劑、粉劑）與廠牌。

---

## 安全性考量

**藥物交互作用**（資料來源：DDInter；共偵測 25 個交互作用）

| 嚴重度 | 藥物 | 主要臨床意義 |
|--------|------|------------|
| **Major** | Dolasetron | 心臟毒性風險增加（QTc 延長） |
| **Major** | Ceritinib | QTc 延長加乘，心律不整風險 |
| **Major** | Siponimod | 心臟傳導抑制加乘，需嚴密監控 |
| Moderate | Clarithromycin | CYP3A4 抑制可能升高 Lacosamide 血中濃度 |
| Moderate | Cobicistat | CYP 抑制導致 Lacosamide 暴露量上升 |
| Moderate | Ketoconazole | CYP3A4 強效抑制劑，同前 |
| Moderate | Chloroquine / Hydroxychloroquine | 加成 QTc 延長風險 |
| Moderate | Mefloquine | 抗瘧藥降低癲癇閾值，潛在拮抗效應 |
| Moderate | Lidocaine | 同類 Nav 通道阻斷劑，心臟傳導加成 |
| Moderate | Fingolimod / Ozanimod | S1P 受體調節劑心臟效應加乘 |
| Moderate | Ethanol（酒精） | 中樞神經抑制加成，加重鎮靜 |

> 其餘 14 個 Moderate 交互作用（Alectinib、Brigatinib、Crizotinib、Idelalisib、Imatinib、Pasireotide、Sunitinib 等）請參考原廠仿單或 DDInter 資料庫完整清單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Rank 1 預測（躁狂雙極性情感疾患）的臨床證據僅達 L3（觀察性研究），目前唯一登記的 Phase 3 試驗（NCT07412132）仍在招募中，且研究對象是「抑鬱發作」而非「躁狂發作」，與本預測的疾病相位直接不符；在更直接的躁狂相臨床數據出現之前，不建議推進。

**偏頭痛（Rank 5）建議優先推進**：多適應症評估中，偏頭痛已有 3 個已完成的 Phase 3 RCT（包含 n=600 直接比較 Lacosamide vs Propranolol 及 Lacosamide vs Topiramate 的試驗），證據等級達 **L1**，建議優先生成偏頭痛獨立報告並評估 Proceed with Guardrails 可行性。

**若要推進躁狂雙極性情感疾患需要：**
- 取得 NCT07412132 完成後的結果數據，尤其需要確認是否有躁狂相評估子分析
- 補充完整 MOA 資料（建議查詢 DrugBank API，候選 ID：DB06218）
- 設計以「躁狂發作（YMRS 量表）」為主要終點的前瞻性 RCT，區別於現有聚焦抑鬱的試驗設計
- 評估與常用雙極症藥物（鋰鹽、valproate、quetiapine）合併使用的 DDI 與安全性矩陣
- 監測血液學參數（CBC），尤其是嗜中性白血球計數（已有個案報告提示風險）
---

