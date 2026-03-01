---
layout: default
title: Aditus (Lupus Advisor) 聯繫信件
parent: 可整合應用程式評估
grand_parent: SMART on FHIR
nav_exclude: true
---

# Aditus (Lupus Advisor) 聯繫信件

**目標**：探討狼瘡照護整合
**優先級**：中（Phase 3）
**聯繫方式**：
- **開發商**: Point-of-Care Partners (POCP)
- **電話**: (877) 312-7627
- **地址**: 9710 Stirling Rd. Suite 106, Hollywood, FL 33024-8018
- **網站**: https://www.lupusadvisor.com/ (可預約 Demo)

---

## 信件內容

**Subject:** Integration Inquiry: AI Drug Repurposing for Systemic Lupus Erythematosus Care

---

Dear Aditus Team,

I am exploring a potential integration between TwTxGNN and Lupus Advisor to enhance clinical decision support for systemic lupus erythematosus (SLE) patients.

### About TwTxGNN

TwTxGNN is a SMART on FHIR application that provides AI-powered drug repurposing predictions using Harvard's TxGNN knowledge graph model.

**Autoimmune Disease Focus:**
- 17 drugs with autoimmune disease predictions
- 16 predicted indications
- Coverage includes lupus-related conditions
- Validated against ClinicalTrials.gov and PubMed

**Technical Specs:**
- FHIR R4 compatible
- Static FHIR API available
- Open source (MIT license)

**Website:** https://twtxgnn.yao.care/
**GitHub:** https://github.com/yao-care/TwTxGNN

### Proposed Integration

Lupus Advisor's automated EHR assistance workflow could be enhanced with drug repurposing insights:

1. **Treatment Optimization**
   - When guideline-recommended treatments show inadequate response
   - Display AI-predicted alternative candidates with evidence levels
   - Link to supporting clinical trial data

2. **Refractory Case Support**
   - For patients not responding to standard therapies
   - Provide research-backed alternatives for physician consideration
   - Include evidence classification (L1-L5)

3. **Clinical Trial Matching**
   - Connect patients with relevant ongoing trials
   - Integrate ClinicalTrials.gov data for predicted indications

### Technical Integration

Since both applications use FHIR R4, integration should be straightforward:

| Integration Point | Method |
|-------------------|--------|
| Data Exchange | FHIR MedicationKnowledge resources |
| API Access | Static JSON endpoints |
| Trigger | Disease activity / treatment response indicators |

**Example API Call:**
```
GET https://twtxgnn.yao.care/fhir/MedicationKnowledge/hydroxychloroquine.json
```

### Benefits for Lupus Advisor Users

| Benefit | Description |
|---------|-------------|
| **Expanded Options** | AI-identified candidates beyond standard guidelines |
| **Evidence-Based** | Each prediction validated against clinical data |
| **Safety Integrated** | DDI checking for 222,391 drug pairs |
| **Trial Links** | Direct connection to relevant clinical trials |

### Next Steps

Would you be open to:

1. A brief technical call to discuss integration options?
2. A pilot study with select healthcare institutions?
3. Reviewing our lupus-related drug predictions?

We believe this integration could provide valuable additional insights for lupus patients, particularly those with refractory disease.

Best regards,

**TwTxGNN Team**
https://twtxgnn.yao.care/

---

## 附件清單

- [ ] 英文版專案簡介：[project-intro-en.md](../project-intro-en)
- [ ] FHIR API 規格：[api-spec.md](../api-spec)
- [ ] 自體免疫疾病藥物預測清單

---

## 背景資料

### Aditus / Lupus Advisor

- 狼瘡照護自動化 EHR 輔助平台
- SMART on FHIR R4 相容
- 符合 ACR/EULAR 指引

### 狼瘡相關適應症

TwTxGNN 中可能相關的適應症關鍵字：
- lupus
- systemic lupus erythematosus
- autoimmune
- inflammatory

---

## 待辦事項

- [ ] 透過官網聯繫表單發送
- [ ] 整理狼瘡相關藥物預測
- [ ] 準備整合技術方案
- [ ] 追蹤回覆
- [ ] 安排技術討論

---

*建立日期：2026-03-01*
