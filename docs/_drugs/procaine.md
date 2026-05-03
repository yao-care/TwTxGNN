---
layout: default
title: Procaine
parent: 中證據等級 (L3-L4)
nav_order: 217
evidence_level: L4
indication_count: 10
---

# Procaine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Procaine：從局部麻醉到高鐵血紅蛋白血症

## 一句話總結

Procaine（普魯卡因）是一種酯類局部麻醉藥，台灣核准用於局部麻醉及作為青黴素注射的載體。
TxGNN 模型預測與 Procaine 關聯性最高的適應症為**高鐵血紅蛋白血症 (Methemoglobinemia)**，
然而現有 **8 篇文獻**顯示此關聯源自 Procaine 代謝物 PABA 誘發此病的**已知不良反應機轉**，而非治療機轉，目前亦無相關臨床試驗登記。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部麻醉 |
| 預測新適應症 | 高鐵血紅蛋白血症 (Methemoglobinemia) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L4 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏完整的 DrugBank 作用機轉資料（高嚴重度資料缺口 DG001）。根據已知藥理，Procaine 是一種酯類局部麻醉藥（代表性商品名：Novocaine），透過**阻斷電壓門控鈉離子通道（Na⁺ channel）**，抑制神經元動作電位的產生與傳導，達到局部麻醉效果。此外，Guide to Pharmacology 資料庫指出 Procaine 與 ryanodine receptor（RyR1、RyR2）存在潛在交互作用，但目前缺乏量化生物活性數據加以支撐。

Procaine 在體內由血漿假性膽鹼酯酶（pseudocholinesterase）快速水解，主要代謝物為**對胺基苯甲酸（PABA）**。PABA 能將血紅素中的亞鐵（Fe²⁺）氧化為高鐵（Fe³⁺），導致血紅蛋白失去攜氧能力，引發高鐵血紅蛋白血症。TxGNN 的知識圖譜因此在 Procaine 節點與此疾病節點之間建立了強連結。

⚠️ **重要臨床解讀**：此高分預測反映的是 Procaine 與高鐵血紅蛋白血症之間的**不良反應因果關聯**，而非治療潛力。現有所有文獻均記錄 Procaine（或其複方）**導致**此病症的案例，而非治療案例。對高鐵血紅蛋白血症患者使用 Procaine 實際上構成臨床用藥禁忌，此預測方向不具再利用價值。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Cohort | Chinese Journal of Surgery | 靜脈 Procaine 麻醉確認可升高患者血中高鐵血紅蛋白濃度 |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | 局部麻醉藥合理使用綜述，涵蓋神經阻斷技術與毒性風險評估 |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Review | Laval Medical | 局部麻醉藥藥理特性全面綜述，含代謝途徑與不良反應描述 |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Review | Fundam Appl Toxicol | 有機磷殺蟲劑抑制非關鍵組織酯酶，間接改變 Procaine 等酯類藥物代謝速率與毒性 |
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case series | Acta Physiol Lat Am | 靜脈注射 Procaine 直接導致高鐵血紅蛋白血症之病案系列報告 |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case series | Lancet | Lignocaine 引發高鐵血紅蛋白血症，機轉與 Procaine 代謝物氧化作用類似 |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case series | Rev Esp Anestesiol Reanim | 全身麻醉中使用 Novocaine 皮下浸潤後，新生兒發生高鐵血紅蛋白血症 |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | In vitro | Am J Obstet Gynecol | Procaine HCl 及代謝物 PABA 均可穿越人類胎盤屏障，具胎兒暴露風險 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第000477號 | 鹽酸普魯卡因注射液２％ | 注射劑 | 局部麻醉 |
| 內衛藥製字第004458號 | 博西林注四十萬單位 | 注射劑 | 葡萄狀球菌、鏈球狀球菌、肺炎雙球菌所引起之感染症 |
| 內衛藥製字第006644號 | 補祿卡因注射液 | 注射劑 | 局部麻醉 |
| 內衛藥輸字第001221號 | 普樂西林（３，０００，０００ＩＵ） | 滅菌懸液注射劑 | 盤尼西林感受性細菌引起之感染症 |
| 內衛藥輸字第002572號 | 鉍黴素針劑 | 乾粉注射劑 | 梅毒、急性扁桃腺炎、喉炎 |

---

## 安全性考量

**藥物交互作用（共 15 筆，依嚴重程度排列）：**

| 交互藥物 | 嚴重程度 |
|---------|---------|
| Nitrous acid | ⚠️ Major |
| Sulfasalazine | Moderate |
| Lidocaine（局部）、Lidocaine（眼科） | Moderate |
| Benzocaine（局部） | Moderate |
| Cocaine（局部）、Cocaine（鼻腔） | Moderate |
| Tetracaine（眼科）、Tetracaine（局部） | Moderate |
| Oxybuprocaine（眼科） | Moderate |
| Cinchocaine（局部） | Moderate |
| Laronidase | Minor |
| Hyaluronidase | Minor |
| Doxorubicin、Doxorubicin（liposomal） | Minor |

> Nitrous acid 與 Procaine 合用具重大交互作用（Major），需特別注意。多種局部麻醉藥合用（同類疊加效應）均列 Moderate 級別，臨床上應避免同時使用多種酯類或醯胺類局部麻醉藥。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 最高分預測適應症（高鐵血紅蛋白血症）是 Procaine 代謝物 PABA 的**已知毒性機轉**，所有相關文獻一致記錄為不良反應，而非治療效益；對高鐵血紅蛋白血症患者使用 Procaine 構成用藥禁忌，此方向完全不具再利用價值。

**若要推進需要：**
- **優先轉向評估 Rank 8（肌腱炎，Tendinitis，L3 證據，建議 Proceed with Guardrails）**：有 1 篇 RCT（PMID [23494116](https://pubmed.ncbi.nlm.nih.gov/23494116/)，2013）及 1 篇 2022 年 Cohort 研究（PMID [35480510](https://pubmed.ncbi.nlm.nih.gov/35480510/)）支持 1% Procaine 局部注射（神經療法）用於棘上肌肌腱病變的止痛效益，是目前最具現代臨床根據的再利用方向
- 同步評估 **Rank 7（纖維肌痛症，Fibromyalgia）**：有歷史性觸發點注射文獻，但需新的現代 RCT 驗證
- 補充完整 DrugBank MOA 資料（資料缺口 DG001），強化後續機轉關聯分析
- 針對肌腱病變適應症設計現代雙盲 RCT，確立 Procaine 神經療法注射的療效與最適劑量、頻次及安全監測標準
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

