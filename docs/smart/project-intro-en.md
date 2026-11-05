---
layout: default
title: Project Introduction (English)
parent: 🏥 SMART on FHIR
nav_order: 10
---

# TwTxGNN: AI-Powered Drug Repurposing for Taiwan NHI Drugs

## Executive Summary

**TwTxGNN** is an open-source drug repurposing platform that leverages Harvard's TxGNN deep learning model to predict potential new indications for Taiwan National Health Insurance (NHI) approved drugs. Unlike prediction-only tools, TwTxGNN provides a complete evidence validation pipeline, integrating clinical trials, literature, and safety data to generate actionable reports.

---

## Key Differentiators

| Feature | Description |
|---------|-------------|
| **Evidence-Based Predictions** | Every prediction is validated against ClinicalTrials.gov, PubMed, and other authoritative sources |
| **Five-Level Evidence Classification** | L1 (multiple Phase 3 RCTs) to L5 (AI prediction only) |
| **SMART on FHIR Integration** | Ready-to-use app for EHR integration |
| **FHIR R4 API** | Static FHIR resources for external system integration |
| **Comprehensive Safety Data** | {{ site.data.ddi_sources.display.ddinter_rows }} DDI records, {{ site.data.ddi_sources.display.ddsi_records }} DDSI records |

---

## Data Overview

| Metric | Count |
|--------|-------|
| Drug Reports | {{ site.data.drug_stats.total_drugs }} |
| Predicted New Indications (known uses excluded) | {{ site.data.drug_stats.total_indications }} |
| Drug-Drug Interactions (DDI) | {{ site.data.ddi_sources.display.ddinter_rows }} |
| Drug-Disease Contraindications (DDSI) | {{ site.data.ddi_sources.display.ddsi_records }} |

### Evidence Distribution

{% comment %}Counts come from docs/_data/drug_stats.json (scripts/generate_drug_stats.py); do not hard-code them.{% endcomment %}
{% assign lc = site.data.drug_stats.level_counts %}{% assign n_lv = lc.L1 | plus: lc.L2 | plus: lc.L3 | plus: lc.L4 | plus: lc.L5 %}{% assign n_na = site.data.drug_stats.total_drugs | minus: n_lv %}

| Level | Definition | Drug Count |
|-------|------------|------------|
| L1 | Multiple Phase 3 RCTs | {{ lc.L1 }} |
| L2 | Single RCT or Phase 2 trials | {{ lc.L2 }} |
| L3 | Observational studies | {{ lc.L3 }} |
| L4 | Preclinical / mechanistic | {{ lc.L4 }} |
| L5 | AI prediction only | {{ lc.L5 }} |
| N/A | [Known uses only / main prediction withdrawn]({{ '/known-uses/' | relative_url }}) | {{ n_na }} |

---

## Technology Stack

### Prediction Model

- **TxGNN**: Published in *Nature Medicine* (2024) by Harvard Zitnik Lab
- **Method**: Graph neural network trained on a biomedical knowledge graph; scores drug–disease pairs
- **Source**: [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x)

### Evidence Sources

| Source | Data Type |
|--------|-----------|
| ClinicalTrials.gov | Clinical trial data (NCT IDs) |
| PubMed | Biomedical literature (PMIDs) |
| DrugBank | Drug properties and interactions |
| TFDA | Taiwan FDA approval status |
| DDInter (DDI download files; DDSI and DFI from the DDInter 2.0 API) | Drug interactions |
| Disease Ontology | Disease classification (DOIDs) |

### Technical Implementation

- **Frontend**: Static site (Jekyll) + JavaScript
- **FHIR Version**: R4 (4.0.1)
- **Data Format**: JSON, CSV
- **Hosting**: GitHub Pages
- **Open Source**: [GitHub Repository](https://github.com/yao-care/TwTxGNN)

---

## SMART on FHIR Integration

TwTxGNN provides a fully functional SMART on FHIR application that can be integrated into any FHIR R4-compliant EHR system.

### Capabilities

1. **Patient Medication Retrieval**: Reads MedicationRequest/MedicationStatement from EHR
2. **Drug Mapping**: Maps RxNorm codes to TwTxGNN database via RxNorm API
3. **Repurposing Lookup**: Displays predicted new indications for each medication
4. **Evidence Display**: Shows evidence level and supporting references

### Technical Specifications

| Item | Value |
|------|-------|
| FHIR Version | R4 |
| OAuth | OAuth 2.0 with PKCE |
| Scopes | `launch`, `patient/Patient.read`, `patient/MedicationRequest.read`, `patient/MedicationStatement.read`, `openid`, `fhirUser` |
| Launch URI | `https://twtxgnn.yao.care/smart/launch.html` |
| Standalone URI | `https://twtxgnn.yao.care/smart/standalone.html` |

### FHIR API Endpoints

{% comment %}Resource counts are the files actually published under docs/fhir/; do not hard-code them.{% endcomment %}
{% assign fhir_mk = site.static_files | where_exp: "f", "f.path contains '/fhir/MedicationKnowledge/'" %}{% assign fhir_cud = site.static_files | where_exp: "f", "f.path contains '/fhir/ClinicalUseDefinition/'" %}

| Endpoint | Description |
|----------|-------------|
| `/fhir/metadata` | CapabilityStatement |
| `/fhir/MedicationKnowledge/{drug-slug}.json` | Drug resource ({{ fhir_mk.size }} drugs) |
| `/fhir/ClinicalUseDefinition/{drug-indication}.json` | Prediction resource ({{ fhir_cud.size }} predictions) |
| `/fhir/Bundle/all-predictions.json` | Complete dataset |

---

## Collaboration Opportunities

We are seeking collaboration with:

### 1. EHR Vendors & Healthcare Institutions

- Pilot deployment of SMART App
- Integration with clinical decision support workflows
- Feedback for usability improvements

### 2. Clinical Trial Platforms

- Enrichment of clinical trial data with AI predictions
- Patient cohort identification

### 3. Drug-Drug Interaction Systems

- Integration of TwTxGNN predictions as supplementary data layer
- Combined DDI + repurposing alerts

### 4. Disease-Specific Research Teams

- Custom analysis for specific therapeutic areas
- Collaboration on validation studies

---

## Disease Coverage

TwTxGNN covers predictions across multiple therapeutic areas:

| Therapeutic Area | Example Indications |
|------------------|---------------------|
| Oncology | Breast carcinoma, colorectal cancer, lung cancer |
| Neurology | Epilepsy, migraine, Parkinson's disease |
| Cardiology | Hypertension, heart failure, arrhythmia |
| Infectious Disease | Viral infections, bacterial infections |
| Autoimmune | Rheumatoid arthritis, lupus, psoriasis |
| Metabolic | Diabetes, obesity, dyslipidemia |
| Rare Diseases | Various orphan diseases |

---

## How to Get Started

### For Developers

```bash
# Clone the repository
git clone https://github.com/yao-care/TwTxGNN.git

# Install dependencies
uv sync

# Extract known drug–disease relations from the knowledge graph (known uses, not predictions)
uv run python scripts/run_kg_prediction.py
```

### For Healthcare Institutions

1. **Test the SMART App**: Use [SMART Launcher](https://launch.smarthealthit.org/) with our launch URL
2. **Explore the Data**: Visit [twtxgnn.yao.care](https://twtxgnn.yao.care/) to browse drug reports
3. **Contact Us**: Reach out for integration discussions

### For Researchers

- **Download Data**: [CSV/JSON exports available](https://twtxgnn.yao.care/downloads/)
- **API Access**: Use FHIR endpoints for programmatic access
- **Cite Us**: Reference our methodology page

---

## Contact Information

- **Website**: [https://twtxgnn.yao.care/](https://twtxgnn.yao.care/)
- **GitHub**: [https://github.com/yao-care/TwTxGNN](https://github.com/yao-care/TwTxGNN)
- **Issues**: [GitHub Issues](https://github.com/yao-care/TwTxGNN/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yao-care/TwTxGNN/discussions)

---

## Disclaimer

This platform is intended for **research purposes only** and does not constitute medical advice. All drug repurposing predictions require clinical validation before application. Healthcare decisions should be made in consultation with qualified medical professionals.
