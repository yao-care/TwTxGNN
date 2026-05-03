---
layout: default
title: Hyaluronic Acid
parent: 高證據等級 (L1-L2)
nav_order: 124
evidence_level: L1
indication_count: 10
---

# Hyaluronic Acid
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

# Hyaluronic Acid：從生物材料（眼科/關節/皮膚）到乾眼症

## 一句話總結

Hyaluronic Acid（玻尿酸，HA）是人體天然存在的高分子量糖胺聚醣，廣泛應用於眼科手術黏彈劑、關節腔潤滑注射及皮膚填充，目前在台灣無已登記之藥品許可證。
TxGNN 模型預測它可能對**乾眼症 (Dry Eye Syndrome)** 有效，目前有 **超過 30 個臨床試驗**（含多個已完成的 Phase 2-4 RCT）和 **20 篇文獻**（含 2 篇 Meta 分析）支持這個方向，是本次評估中證據最充分的預測適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無台灣許可證登記（國際用途包含眼科黏彈劑、關節腔注射、皮膚填充） |
| 預測新適應症 | 乾眼症 (Dry Eye Syndrome) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L1 |
| 台灣上市 | ✗ 未上市（許可證 0 張） |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Hyaluronic Acid 是人體玻璃體、關節滑液與角膜前淚膜中天然存在的成分，其分子結構賦予它極強的保水能力——每公克 HA 可結合自身重量約 1,000 倍的水分，並形成穩定的黏彈性薄膜。正因如此，HA 天生就具備補充淚液水相層、延長液體在眼表停留時間的物理特性，與乾眼症的治療需求高度契合。

目前缺乏 DrugBank 登記的詳細作用機轉資料。根據現有研究，HA 在乾眼症中的作用涉及三個層次：（1）**機械性保水**：黏彈性薄膜穩定淚膜結構，減少蒸發；（2）**生物性修復**：透過 CD44 受體介導角膜上皮細胞遷移，促進損傷修復；（3）**抗炎調節**：高分子量 HA 可能透過 CD44/NF-κB 路徑抑制眼表局部炎症反應，緩解乾眼症相關的角結膜損傷。

從適應症關聯性來看，HA 眼藥水（玻璃酸鈉眼藥水）已在日本、歐洲及多個亞洲國家取得乾眼症治療的正式核准，且在多個大型隨機對照試驗中被用作標準對照組（active comparator），說明其療效已獲醫學界高度認可。TxGNN 模型的預測不僅合理，更可說是對一個已有強力臨床證據的治療方向進行「補完驗證」。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01101984](https://clinicaltrials.gov/study/NCT01101984) | N/A | 完成 | 400 | 大型多國隨機平行對照試驗，直接以 DE-089（0.1% 玻尿酸鈉眼藥水）對比標準眼藥水用於乾眼症，為高品質直接療效證據 |
| [NCT03223909](https://clinicaltrials.gov/study/NCT03223909) | Phase 4 | 完成 | 326 | 含 HA 的 PRO-087 眼藥水 vs Systane Ultra 用於輕中度淚膜功能障礙，評估眼表解剖與生理恢復 |
| [NCT03888183](https://clinicaltrials.gov/study/NCT03888183) | Phase 4 | 未知 | 334 | 隨機雙盲對照試驗，評估無防腐劑低濃度 HA 含鹽眼藥水對乾眼症的短期輔助效果（334 人大樣本） |
| [NCT06478134](https://clinicaltrials.gov/study/NCT06478134) | Phase 2/3 | 完成 | 124 | 以 HA 淚液替代品為對照組的隨機雙盲 RCT，評估多效淚液替代品的非劣效性 |
| [NCT07097922](https://clinicaltrials.gov/study/NCT07097922) | N/A | 未開始 | 140 | 直接比較 3% Diquafosol 與 0.1% HA 用於 LASIK 術後乾眼症，提供頭對頭療效比較數據 |
| [NCT06517667](https://clinicaltrials.gov/study/NCT06517667) | Phase 2/3 | 完成 | 30 | 隨機單盲試驗，比較不同 HA 淚液替代品配方（分子量、濃度）用於蒸發型乾眼症的療效差異 |
| [NCT07245836](https://clinicaltrials.gov/study/NCT07245836) | Phase 4 | 完成 | 30 | 評估含 HA 成分的 Thealoz Total 眼藥水對慢性乾眼症伴眼表炎症患者的抗炎效果 |
| [NCT00809198](https://clinicaltrials.gov/study/NCT00809198) | Phase 4 | 完成 | 67 | Kynex（含 HA）vs Refresh Plus 用於輕中度乾眼症的平行組隨機遮蔽試驗 |
| [NCT06146881](https://clinicaltrials.gov/study/NCT06146881) | Phase 2 | 未知 | 70 | 比較 Diquafosol 3% 與 HA 0.1% 預防白內障術後乾眼症發生率，HA 組為對照 |
| [NCT06317922](https://clinicaltrials.gov/study/NCT06317922) | N/A | 進行中 | 60 | 評估含海藻糖與 HA（0.15g）的 Thealoz Duo 眼藥水緩解玻璃體內注射患者眼部不適症狀的療效 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33804439](https://pubmed.ncbi.nlm.nih.gov/33804439/) | 2021 | Meta-analysis | Int J Environ Res Public Health | Meta 分析（8 個資料庫）確認 HA 眼藥水在改善乾眼症症狀與體徵上優於生理食鹽水及傳統人工淚液 |
| [38895674](https://pubmed.ncbi.nlm.nih.gov/38895674/) | 2024 | Meta-analysis | Int J Ophthalmology | 系統性回顧並 Meta 分析不同濃度 HA 眼藥水（高濃度 vs 低濃度）對乾眼症的療效差異，提供最佳濃度建議 |
| [39260878](https://pubmed.ncbi.nlm.nih.gov/39260878/) | 2024 | RCT | BMJ | 非劣效性隨機對照試驗，以 0.1% HA 眼藥水為對照，評估笑聲練習對乾眼症的療效，確立 HA 的臨床療效基準 |
| [37117131](https://pubmed.ncbi.nlm.nih.gov/37117131/) | 2023 | RCT | Contact Lens Anterior Eye | RCT 評估含海藻糖與 HA 複合人工淚液對不同年齡層停經期婦女中重度乾眼症的 3 個月療效 |
| [34562113](https://pubmed.ncbi.nlm.nih.gov/34562113/) | 2022 | Cohort | Graefe's Arch Clin Exp Ophthalmol | 停經婦女中度乾眼症使用 HA 0.3%、氰鈷胺與電解質複方眼藥水的臨床療效評估 |
| [35514082](https://pubmed.ncbi.nlm.nih.gov/35514082/) | 2022 | Review | Acta Ophthalmologica | 系統性文獻回顧評估含 HA 人工淚液在乾眼症治療中的安全性與有效性，包含濃度、分子量等關鍵因素分析 |
| [37042308](https://pubmed.ncbi.nlm.nih.gov/37042308/) | 2024 | Review | Acta Ophthalmologica | 全面比較 HA 與其他所有已在乾眼症 RCT 中被直接對照之單一成分眼藥水，確立 HA 的標準療效地位 |
| [32070808](https://pubmed.ncbi.nlm.nih.gov/32070808/) | 2020 | Review | Carbohydrate Research | 回顧 HA 在眼科（含乾眼症）、風濕科及皮膚科的應用機轉，說明保水與潤滑特性的生物化學基礎 |
| [33923222](https://pubmed.ncbi.nlm.nih.gov/33923222/) | 2021 | Review | Molecules | 綜述 HA 在眼科（玻璃體注射、乾眼治療）及隱形眼鏡領域的應用，分析生物安全性與適用性 |
| [27324942](https://pubmed.ncbi.nlm.nih.gov/27324942/) | 2016 | Review | J Cosmetic Dermatology | 系統性回顧 HA 物化特性及多領域醫學應用，為乾眼症使用提供跨領域的機轉理論基礎 |

---

## 台灣上市資訊

根據查詢結果，Hyaluronic Acid（DB08818）目前在台灣無任何藥品許可證登記，市場狀態為**未上市**。

> 需注意：HA 相關產品可能以**醫療器材**（如玻尿酸眼藥水為 Class II 醫材）而非藥品申請許可，建議同步確認 TFDA 醫材資料庫的登記狀況。

---

## 安全性考量

**藥物交互作用（中等強度，共 2 筆）：**

| 交互藥物 | 風險等級 | 資料來源 | 說明 |
|---------|---------|---------|------|
| Cetylpyridinium（外用） | 中等 | DDInter | 常見眼藥水防腐劑，合用時可能影響 HA 配方穩定性或局部刺激性 |
| Benzalkonium（外用） | 中等 | DDInter | 廣泛使用的眼科防腐劑，已知對眼表細胞具潛在毒性，與 HA 合用需審慎 |

其他安全性資訊（仿單警語、禁忌症）請參考原廠仿單。建議優先選用**無防腐劑**製劑以降低上述交互作用風險。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多個已完成的 Phase 2-4 隨機對照試驗（含 400 人大型試驗）與 2 篇 Meta 分析直接支持 HA 眼藥水用於乾眼症的安全性與療效，且 HA 在日本、歐洲等多個國家已取得乾眼症相關核准，證據等級達 L1。台灣雖無現行藥品許可證，但市場需求明確，申請途徑可行。

**若要推進需要：**
- 確認申請途徑：HA 眼藥水可能以**醫療器材**（而非藥品）申請，需向 TFDA 確認分類（建議同時查詢藥品及醫材資料庫）
- 確定製劑規格：優先考量已有充分臨床證據的濃度（0.1%、0.15%、0.18%、0.3%），並決定是否採無防腐劑設計
- 補充 TFDA 仿單警語與禁忌症資料（目前 Data Gap，屬 Blocking 等級缺口）
- 建立特定高風險族群（糖尿病、術後、老年患者）的安全性監測計畫
- 評估與眼科防腐劑（Benzalkonium、Cetylpyridinium）配方相容性，建議單位劑量無防腐劑設計以規避交互作用風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

