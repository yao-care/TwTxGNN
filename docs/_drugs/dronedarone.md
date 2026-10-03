---
layout: default
title: Dronedarone
parent: 高證據等級 (L1-L2)
nav_order: 88
evidence_level: L2
indication_count: 10
---

# Dronedarone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Dronedarone：從心房纖維顫動到中風疾病

## 一句話總結

Dronedarone 原本用於治療陣發性或持續性心房纖維顫動/心房撲動。
TxGNN 模型預測它可能對**中風疾病 (stroke disorder)** 有效，
目前有 **多個臨床試驗**和 **多篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房纖維顫動、心房撲動 |
| 預測新適應症 | 中風疾病 (stroke disorder) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 台灣上市 | 已上市 |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Dronedarone 是 amiodarone 的衍生物，具有多通道阻斷作用，能維持竇性心律。
心房纖維顫動是中風的主要危險因素，透過維持竇性心律可減少心房血栓形成。
ATHENA 試驗的事後分析顯示 dronedarone 可降低中風和暫時性腦缺血發作風險，
且研究發現其具有獨立於抗心律不整作用之外的抗凝血和抗血小板效應。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | TERMINATED | 3236 | PALLAS 試驗評估 dronedarone 在永久性心房纖維顫動預防主要心血管事件 |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | COMPLETED | 2789 | EAST 試驗證實早期節律控制可預防心血管死亡和中風 |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | COMPLETED | 339 | 評估首發心房纖維顫動患者早期使用 dronedarone 的效果 |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | NOT_YET_RECRUITING | 1746 | 急性中風合併心房纖維顫動患者的早期節律控制 |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | COMPLETED | 2204 | CABANA 試驗比較導管消融與抗心律不整藥物治療 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | 心房纖維顫動治療進展，包括 dronedarone 的角色 |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | In vitro | Atherosclerosis | Dronedarone 具有獨立於抗心律不整作用的抗凝血和抗血小板效應 |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT analysis | Clin Res Cardiol | EAST-AFNET 4 試驗中 amiodarone 和 dronedarone 用於早期節律控制的安全性和療效 |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Dronedarone 獲批及其在心房纖維顫動治療中的療效 |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post-hoc analysis | Eur J Heart Fail | ATHENA 試驗事後分析評估 dronedarone 在 HFpEF/HFmrEF 合併心房纖維顫動的效果 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dronedarone 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025224號 | 脈泰克膜衣錠400毫克 | 膜衣錠 | 賽諾菲股份有限公司 | 2030/06/28 | MULTAQ適用於最近6個月內有陣發性或持續性心房纖維顫動 (AF) 或心房撲動 (AFL)，且目前處於竇性節律（sinus rhythm）狀態的患者，可降低病患發生心房顫動而住院… |
| 衛部藥輸字第029026號 | 決奈達隆鹽酸鹽 | （粉） | 漢旭股份有限公司 | 2030/09/18 | 血管擴張劑。 |

<!-- tfda-licenses:end -->

## 安全性考量

- **黑框警告**：永久性心房纖維顫動、嚴重心衰竭患者禁用
- **主要不良反應**：腹瀉、噁心、腹痛、血清肌酐升高
- **肝毒性**：罕見但嚴重，需監測肝功能
- **藥物交互作用**：與 digoxin 併用時會增加 digoxin 血中濃度

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Dronedarone 透過維持竇性心律和潛在的抗血栓機制，可能對中風預防有效。
ATHENA 試驗已顯示其在中風/TIA 預防方面的益處，但需注意適應症限制。

**若要推進需要：**
- 排除永久性心房纖維顫動和嚴重心衰竭患者
- 嚴格的肝功能監測計畫
- 與抗凝血藥物併用策略的優化研究

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表品名「決奈達隆鹽酸鹽」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證數「1 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

