---
layout: default
title: DDI-CDS.org 聯繫信件
parent: 可整合應用程式評估
grand_parent: SMART on FHIR
nav_exclude: true
---

# DDI-CDS.org 聯繫信件

**目標**：請求技術合作或 API 存取
**優先級**：高（Phase 2）
**聯繫方式**：Dr. Richard Boyce (rdb20@pitt.edu) - 匹茲堡大學生物醫學資訊系，DDI-CDS 專案共同研究者
**備註**：info@ddi-cds.org 已失效

---

## 信件內容

**Subject:** Technical Collaboration Request: DDI-CDS Integration with TwTxGNN Drug Repurposing Platform

---

Dear DDI-CDS Research Team,

I am reaching out regarding a potential technical collaboration for integrating drug-drug interaction (DDI) alerts into TwTxGNN, a SMART on FHIR drug repurposing application.

### About TwTxGNN

TwTxGNN is an open-source platform that provides AI-powered drug repurposing predictions using Harvard's TxGNN knowledge graph model. Our goal is to help clinicians identify potential new therapeutic uses for existing medications while ensuring patient safety.

**Current DDI Capabilities:**
- DDInter 2.0: 222,391 drug-drug interactions
- Guide to PHARMACOLOGY: 4,636 approved drug interactions
- Drug-Disease Contraindications (DDSI): 8,359 records

**Platform Stats:**
- 189 drugs with repurposing predictions
- 1,268 predicted new indications
- FHIR R4 compatible SMART App
- Five-level evidence classification (L1-L5)

**Website:** https://twtxgnn.yao.care/
**GitHub:** https://github.com/yao-care/TwTxGNN

### Why DDI-CDS Integration Matters

When recommending repurposed drug candidates, ensuring drug-drug interaction safety is critical. Your research on clinical decision support for DDIs aligns perfectly with our mission to provide evidence-based, safe drug repurposing recommendations.

### Collaboration Goals

We are interested in the following areas of collaboration:

1. **Alert Design Patterns**
   - Reference DDI-CDS alert design patterns for clinical decision support
   - Learn from DDInteract's shared decision-making UI design
   - Implement appropriate severity indicators and clinical context

2. **Technical Documentation**
   - Access to DDI algorithm documentation (Colchicine, Tizanidine, Warfarin-NSAID)
   - CDS Hooks implementation guidance
   - CQL rule structure examples

3. **HL7 PDDI-CDS Implementation Guide**
   - We plan to implement the HL7 PDDI-CDS IG (CC0 licensed)
   - Would appreciate technical guidance on best practices
   - Interested in contributing back to the community

4. **Potential Future Collaboration**
   - Integrate TwTxGNN predictions into DDI-CDS workflow
   - Provide "alternative drug suggestions" when DDI alerts fire
   - Collaborate on research publications

### Our Specific Interests

| DDI-CDS App | Our Interest |
|-------------|-------------|
| **DDInteract** | Shared decision-making UI design for bleeding risk (Warfarin + NSAIDs) |
| **Colchicine DDI-CDS** | CYP3A4/PGP inhibitor interaction algorithms |
| **Tizanidine DDI-CDS** | CYP1A2 inhibitor interaction algorithms |

### Technical Compatibility

| Item | TwTxGNN | DDI-CDS |
|------|---------|---------|
| FHIR Version | R4 | R4 |
| CDS Implementation | In development | CDS Hooks |
| Authorization | PKCE | Standard OAuth |

### Next Steps

Would it be possible to:

1. Schedule a technical discussion call?
2. Access any available API documentation or technical specifications?
3. Discuss potential research collaboration opportunities?

We are committed to proper attribution and would be happy to contribute back to the DDI-CDS community.

Thank you for considering this collaboration. We greatly admire your AHRQ-funded research and believe our work in drug repurposing can complement your DDI safety initiatives.

Best regards,

**TwTxGNN Team**
https://twtxgnn.yao.care/

---

## 附件清單

準備發送時，請附上以下資料：

- [ ] 英文版專案簡介：[project-intro-en.md](../project-intro-en)
- [ ] FHIR API 規格：[api-spec.md](../api-spec)
- [ ] DDI 資料統計（見下方）

---

## TwTxGNN DDI 資料統計

| 資料來源 | 筆數 | 涵蓋範圍 |
|----------|------|----------|
| DDInter 2.0 | 222,391 | 2,310 藥物的 DDI |
| Guide to PHARMACOLOGY | 4,636 | 核准藥物交互作用 |
| DDSI（藥物-疾病禁忌） | 8,359 | 疾病禁忌用藥 |
| DFI（藥物-食物） | 857 | 食物交互作用 |
| DHI（藥物-草藥） | 35 | 草藥交互作用 |

---

## 背景研究

### HL7 PDDI-CDS Implementation Guide

- **GitHub**: https://github.com/HL7/PDDI-CDS
- **授權**: CC0-1.0（公共領域）
- **內容**:
  - CDS Hooks 服務規格
  - 警示嚴重程度分級
  - 臨床情境處理

### DDI-CDS 研究團隊

- AHRQ 資助的學術專案
- 多所大學合作（University of Pittsburgh 等）
- 專注於臨床可用的 DDI 警示系統

---

## 待辦事項

- [ ] 發送聯繫信件至 info@ddi-cds.org
- [ ] 追蹤回覆
- [ ] 研究 HL7 PDDI-CDS IG（CC0 授權，可自行開始）
- [ ] 評估 CDS Hooks 實作需求
- [ ] 準備 DDI 整合技術方案
- [ ] 安排技術討論會議

---

*建立日期：2026-03-01*
