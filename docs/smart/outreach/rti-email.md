---
layout: default
title: RTI International 聯繫信件
parent: 可整合應用程式評估
grand_parent: SMART on FHIR
nav_exclude: true
---

# RTI International (RTI Wellmine) 聯繫信件

**目標**：探討罕見疾病老藥新用合作
**優先級**：高（Phase 1）
**聯繫方式**：https://wellmine.rti.org

---

## 信件內容

**Subject:** Collaboration Inquiry: Drug Repurposing for Rare Diseases - TwTxGNN x RTI Wellmine

---

Dear RTI Wellmine Team,

I am writing to explore a potential collaboration between TwTxGNN and RTI Wellmine for rare disease drug repurposing research.

### About TwTxGNN

TwTxGNN is an open-source SMART on FHIR application that provides AI-powered drug repurposing predictions based on Harvard's TxGNN knowledge graph model published in *Nature Medicine* (2023).

**Key Statistics:**
- 189 drugs with validated repurposing predictions
- 1,268 predicted new indications
- **101 drugs with rare disease predictions**
- 101 rare disease indications covered
- Five-level evidence classification (L1-L5)
- FHIR R4 compatible API

**Website:** https://twtxgnn.yao.care/
**GitHub:** https://github.com/yao-care/TwTxGNN

### Proposed Collaboration

We believe TwTxGNN's drug repurposing predictions can complement RTI Wellmine's patient data collection platform in the following ways:

1. **API Integration**
   - Integrate TwTxGNN FHIR API into the Wellmine platform
   - Enable rare disease patients to view potential repurposed drug candidates for their conditions
   - Provide evidence levels and supporting clinical trial references

2. **Research Validation**
   - Leverage Wellmine's patient-reported outcomes to validate AI predictions
   - Identify high-priority candidates based on patient interest and need
   - Facilitate research collaborations with academic institutions

3. **Data Enrichment**
   - TwTxGNN provides drug predictions with ClinicalTrials.gov and PubMed evidence
   - Wellmine provides real-world patient data and feedback
   - Combined data can accelerate rare disease treatment discovery

### Technical Specifications

| Item | TwTxGNN Capability |
|------|-------------------|
| FHIR Version | R4 (4.0.1) |
| API Format | Static JSON (FHIR resources) |
| Endpoints | `/fhir/MedicationKnowledge/{drug}.json`, `/fhir/ClinicalUseDefinition/{prediction}.json` |
| Authentication | None required (public data) |

### Next Steps

Would you be available for a brief call to discuss this opportunity? We would be happy to:

1. Provide a technical demonstration of TwTxGNN
2. Share our rare disease drug prediction dataset
3. Discuss API integration requirements
4. Explore research collaboration frameworks

We believe this collaboration could accelerate rare disease treatment discovery while leveraging Wellmine's unique patient data collection capabilities.

Thank you for your consideration. We look forward to hearing from you.

Best regards,

**TwTxGNN Team**
https://twtxgnn.yao.care/

---

## 附件清單

準備發送時，請附上以下資料：

- [ ] 英文版專案簡介：[project-intro-en.md](../project-intro-en)
- [ ] FHIR API 規格：[api-spec.md](../api-spec)
- [ ] 罕見疾病藥物預測統計（見下方）

---

## 罕見疾病相關統計

根據 TwTxGNN 資料庫（search-index.json）：

| 指標 | 數值 |
|------|------|
| 涉及罕見疾病的藥物數 | 101 |
| 罕見疾病預測適應症數 | 101 |
| L1-L2 高證據預測 | 7 |
| L3-L4 中證據預測 | 25 |
| L5 模型預測 | 159 |

**分類關鍵字**：syndrome, deficiency, inherited, congenital, genetic

---

## 待辦事項

- [ ] 發送聯繫信件至 RTI Wellmine
- [ ] 追蹤回覆
- [ ] 安排視訊會議
- [ ] 準備技術展示
- [ ] 討論 API 整合方案
- [ ] 草擬合作備忘錄

---

*建立日期：2026-03-01*
