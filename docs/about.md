---
layout: default
title: 關於專案
nav_order: 6
description: "TwTxGNN 是基於哈佛 TxGNN 模型的老藥新用預測平台，整合臨床試驗、文獻等多來源證據，提供 191 個台灣健保藥品的完整驗證報告。"
permalink: /about/
---

# 關於本專案

用 AI 加速老藥新用的證據驗證

---

## 專案背景

**TwTxGNN** 是一個藥物再利用（Drug Repurposing）研究輔助平台，基於哈佛大學 Zitnik Lab 發表於 *Nature Medicine* 的 TxGNN 模型，針對台灣健保核准藥品進行適應症擴展預測。

不同於其他預測工具，本平台不僅提供 AI 預測分數，更整合 ClinicalTrials.gov、PubMed 等來源的臨床證據，讓研究人員能快速評估預測的可信度。

---

## 作者與團隊

| 項目 | 資訊 |
|------|------|
| 專案維護 | Yao.Care |
| 模型基礎 | Harvard TxGNN (Zitnik Lab) |
| 最後更新 | 2026 年 2 月 |

### 學術依據

本專案的 AI 預測模型基於以下論文：

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## 什麼是老藥新用？

**老藥新用（Drug Repurposing）** 是指發現現有藥物的新治療用途。相較於從頭開發新藥：

| 比較項目 | 新藥開發 | 老藥新用 |
|---------|---------|---------|
| 開發時間 | 10-15 年 | 3-5 年 |
| 開發成本 | 10-20 億美元 | 1-3 億美元 |
| 安全性資料 | 需重新建立 | 已有人體資料 |
| 失敗風險 | 極高 (>90%) | 較低 |

老藥新用的優勢在於：藥物的安全性、藥物動力學、製程都已經過驗證，可以直接進入臨床療效試驗。

---

## 什麼是 TxGNN？

[TxGNN](https://www.nature.com/articles/s41591-023-02233-x) 是由哈佛醫學院團隊開發的深度學習模型，專門用於預測藥物與疾病的新關聯。

### 技術特點

- **知識圖譜**：整合藥物、疾病、基因、蛋白質等 17,080 個節點
- **圖神經網路**：學習節點間的複雜關聯
- **預測能力**：可預測藥物對哪些疾病可能有效

---

## 資料來源

本平台整合以下公開資料來源：

| 資料類型 | 來源 | 說明 |
|---------|------|------|
| AI 預測 | [TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) | 哈佛大學知識圖譜預測模型 |
| 臨床試驗 | [ClinicalTrials.gov](https://clinicaltrials.gov/) | 全球臨床試驗登記資料庫 |
| 學術文獻 | [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | 生物醫學文獻資料庫 |
| 藥物資訊 | [DrugBank](https://go.drugbank.com/) | 藥物與靶點資料庫 |
| 台灣上市 | [TFDA](https://data.fda.gov.tw/) | 衛福部食藥署開放資料 |
| 藥物交互作用 | [DDInter](https://ddinter2.scbdd.com/) | 藥物交互作用資料庫 |

---

## 專案規模

| 項目 | 數量 |
|------|------|
| 藥物報告 | 191 份 |
| 老藥新用候選 | 142,328 筆 |
| DDI 資料 | 222,391 筆 |

---

## 如何引用

如需引用本平台資料，請使用以下格式：

### APA 格式

```
TwTxGNN. (2026). TwTxGNN 老藥新用驗證報告. https://twtxgnn.yao.care/
```

### BibTeX 格式

```bibtex
@misc{twtxgnn2026,
  title = {TwTxGNN 老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/},
  note = {Accessed: 2026-02-19}
}
```

### 引用原始模型

如使用 TxGNN 預測結果，請同時引用原始論文：

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## 聯絡與回饋

如有問題或建議，歡迎透過以下管道聯繫：

- **GitHub Issues**: [https://github.com/yao-care/TwTxGNN/issues](https://github.com/yao-care/TwTxGNN/issues)
- **專案首頁**: [https://twtxgnn.yao.care/](https://twtxgnn.yao.care/)

---

<div style="background: #f5f5f5; padding: 1rem; margin-top: 2rem; border-left: 4px solid #e0e0e0;">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，不構成醫療建議。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
</div>
