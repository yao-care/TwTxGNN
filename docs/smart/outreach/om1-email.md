---
layout: default
title: OM1 (Major Depression Outcomes) 聯繫信件
parent: 可整合應用程式評估
grand_parent: SMART on FHIR
nav_exclude: true
---

# OM1 (Major Depression Outcomes) 聯繫信件

**目標**：探討精神科用藥合作
**優先級**：中（Phase 3）
**聯繫方式**：透過 SMART App Gallery 聯繫

---

## 信件內容

**Subject:** Collaboration Inquiry: AI Drug Repurposing for Treatment-Resistant Depression

---

Dear OM1 Team,

I am writing regarding a potential collaboration between TwTxGNN and your Major Depression Outcomes application, which tracks PHQ-9 scores and treatment responses.

### About TwTxGNN

TwTxGNN is an open-source drug repurposing platform that uses Harvard's TxGNN knowledge graph model to predict new therapeutic uses for existing medications.

**Psychiatric Coverage:**
- 14 drugs with psychiatric disease predictions
- 8 predicted indications
- Includes depression, anxiety, and related conditions
- Evidence levels from L1 (RCTs) to L5 (AI prediction)

**Platform Stats:**
- 189 total drugs analyzed
- 1,268 predicted new indications
- 222,391 DDI records for safety checking

**Website:** https://twtxgnn.yao.care/
**GitHub:** https://github.com/yao-care/TwTxGNN

### Integration Opportunity

The Major Depression Outcomes app's longitudinal tracking of PHQ-9 scores creates a unique opportunity:

1. **Treatment Response Monitoring**
   - When PHQ-9 scores indicate inadequate treatment response
   - TwTxGNN can suggest drug repurposing candidates
   - Support shared decision-making with evidence-based alternatives

2. **Personalized Suggestions**
   - Based on patient's medication history
   - Avoiding drugs with known interactions
   - Prioritizing candidates with clinical trial support

3. **Outcome Validation**
   - Track PHQ-9 changes in patients receiving repurposed drugs
   - Generate real-world evidence for AI predictions
   - Contribute to research on treatment-resistant depression

### Proposed Integration Flow

```
PHQ-9 Assessment
       ↓
Score Indicates Poor Response
       ↓
Query TwTxGNN for Alternatives
       ↓
Display Candidates with Evidence
       ↓
Shared Decision-Making
       ↓
Track Outcomes (PHQ-9 Changes)
```

### Safety Considerations

We understand the sensitivity of psychiatric medications. TwTxGNN includes:

| Safety Feature | Implementation |
|----------------|----------------|
| DDI Checking | 222,391 drug pairs from DDInter |
| Evidence Levels | L1-L5 classification |
| Disclaimers | Clear research-only labeling |
| References | ClinicalTrials.gov + PubMed links |

All predictions are clearly labeled as research findings requiring clinical validation.

### Technical Compatibility

| Item | TwTxGNN | OM1 Major Depression |
|------|---------|---------------------|
| FHIR Version | R4 | R4 (also DSTU2, STU3) |
| Integration | REST API | SMART on FHIR |
| Data Format | FHIR JSON | Standard FHIR |

### Next Steps

Would you be interested in:

1. A technical discussion on integration options?
2. Reviewing our psychiatric drug predictions?
3. Exploring a pilot study for treatment-resistant depression?

We believe this collaboration could provide valuable additional options for patients who have not responded to first-line treatments.

Best regards,

**TwTxGNN Team**
https://twtxgnn.yao.care/

---

## 附件清單

- [ ] 英文版專案簡介：[project-intro-en.md](../project-intro-en)
- [ ] FHIR API 規格：[api-spec.md](../api-spec)
- [ ] 精神疾病藥物預測清單
- [ ] 免責聲明文件

---

## 背景資料

### OM1

- 健康科技公司，專注於真實世界資料分析
- Major Depression Outcomes 應用追蹤 PHQ-9 評分
- 支援多種 FHIR 版本

### PHQ-9 評分

- Patient Health Questionnaire-9
- 抑鬱症嚴重程度評估
- 0-4: 無或極輕
- 5-9: 輕度
- 10-14: 中度
- 15-19: 中重度
- 20-27: 重度

### 安全考量

精神科用藥需特別注意：
- 藥物交互作用（特別是 MAOI、SSRI、抗精神病藥）
- 自殺風險（特別是青少年）
- 戒斷症狀
- QT 延長風險

**必須包含免責聲明**：所有預測僅供研究參考，不構成醫療建議。

---

## 待辦事項

- [ ] 透過 SMART App Gallery 聯繫
- [ ] 整理精神疾病相關藥物預測
- [ ] 評估精神科用藥安全性考量
- [ ] 準備免責聲明
- [ ] 追蹤回覆
- [ ] 安排技術討論

---

*建立日期：2026-03-01*
