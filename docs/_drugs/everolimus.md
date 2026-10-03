---
layout: default
title: Everolimus
parent: 高證據等級 (L1-L2)
nav_order: 97
evidence_level: L2
indication_count: 10
---

# Everolimus
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

# Everolimus：從腎細胞癌到脂肉瘤

## 一句話總結

Everolimus 是一種 mTOR 抑制劑，已核准用於腎細胞癌、乳癌、神經內分泌腫瘤、器官移植抗排斥等多項適應症，在台灣擁有 12 張許可證（有效 7 張）。
TxGNN 模型預測它可能對**脂肉瘤 (Liposarcoma)** 有效，
目前有 **1 個臨床試驗**和 **4 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 器官移植抗排斥藥物、治療腎臟癌藥物 |
| 預測新適應症 | 脂肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 12 張（有效單方 7／有效複方 0／已註銷 5） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Everolimus 是哺乳類雷帕黴素靶蛋白（mTOR）抑制劑，透過阻斷 PI3K/Akt/mTOR 信號通路，抑制腫瘤細胞增殖、血管新生及異常代謝。mTOR 通路在多種實體腫瘤中均有異常活化，是目前廣泛應用的抗腫瘤靶點。

去分化脂肉瘤（Dedifferentiated Liposarcoma, DDL）中已記錄 Akt/mTOR 及 MAPK 通路的顯著活化（PMID 26518767），為 Everolimus 介入提供直接的分子機轉依據。DDL 另一個特徵是 CDK4 基因高度擴增，而 CDK4/6 通路與 mTOR 通路之間存在交叉調控，因此 CDK4/6 抑制劑 Ribociclib 與 Everolimus 聯用可發揮協同抑制效應，在多種腫瘤模型中已獲驗證。

目前已有 Phase 2 臨床試驗（NCT03114527）直接研究此聯合策略用於進展性去分化脂肉瘤，並於 2024 年發表結果，是支持 TxGNN 預測合理性的最強直接證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 招募完成（進行中） | 48 | Ribociclib（300 mg/day，3 週開 1 週停）＋Everolimus（2.5 mg）聯合療法，分兩組分別研究進展性去分化脂肉瘤（Arm A）及平滑肌肉瘤（Arm B）；結果已於 2024 年在 Clinical Cancer Research 發表（PMID 37967116） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 Trial | Clinical Cancer Research | CDK4/6 抑制劑 Ribociclib 與 mTOR 抑制劑 Everolimus 在進展性 DDL 和 LMS 中具協同生長抑制效應，Phase 2 試驗（SAR-096）直接驗證此組合療法之抗腫瘤活性 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX 小鼠模型系統性評估 CDK 抑制劑在肉瘤的組合療法，支持 CDK＋mTOR 雙靶點策略的臨床轉化可行性 |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Case series | Tumour Biology | 99 例 DDLS 臨床病理分析確認 Akt/mTOR 及 MAPK 通路活化，並以 in vitro 試驗驗證 mTOR 抑制劑之抗腫瘤效應 |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Animal | Anticancer Research | 脂肉瘤異種移植模型中評估 Eribulin 與不同機轉抗癌藥物（含 mTOR 抑制劑）聯用之廣譜前臨床抗腫瘤活性 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Everolimus 的不重複許可證共 **12 張**：有效單方 7 張、有效複方 0 張、已註銷 5 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署罕藥輸字第000020號 | 愛服妥錠 5 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2027/07/10 | 「結節性硬化症併有腎血管肌脂肪瘤之成年病患」且須符合以下條件：其腎血管肌脂肪瘤最長直徑需≧4cm，且曾有發生臨床上有意義之出血或確認病灶有血管瘤（aneurysm）直徑≧5mm者，… |
| 衛署罕藥輸字第000021號 | 愛服妥錠 2.5 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2027/07/10 | 「結節性硬化症併有腎血管肌脂肪瘤之成年病患」且須符合以下條件：其腎血管肌脂肪瘤最長直徑需≧4cm，且曾有發生臨床上有意義之出血或確認病灶有血管瘤（aneurysm）直徑≧5mm者，… |
| 衛署藥輸字第024770號 | 卓定康錠 0.25 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2028/01/24 | 腎臟及心臟移植 併用減量ciclosporin微乳製劑及類固醇，預防腎臟或心臟移植的成人病患之免疫器官排次作用。 肝臟移植 用於預防肝臟移植病患之器官排斥。Certican應於接受… |
| 衛署藥輸字第024772號 | 卓定康錠 0.5 毫克 | 錠劑 | 台灣諾華股份有限公司 | 2028/01/24 | 腎臟及心臟移植 併用減量ciclosporin微乳製劑及類固醇，預防腎臟或心臟移植的成人病患之免疫器官排次作用。 肝臟移植 用於預防肝臟移植病患之器官排斥。Certican應於接受… |
| 衛署藥輸字第025165號 | 癌伏妥錠5毫克 | 錠劑 | 台灣諾華股份有限公司 | 2030/04/01 | AFINITOR® 合併exemestane 適用於治療荷爾蒙接受體陽性、HER2 受體陰性且之前使用過letrozole 或anastrozole 復發或惡化之停經後晚期乳癌患者… |
| 衛部藥製字第058400號 | "中化合成"依維莫司 B20 | 粉劑 | 中化合成生技股份有限公司山佳工廠 | 2029/09/25 | 器官移植抗排斥藥物、治療腎臟癌藥物。 |
| 衛部藥製字第061853號 | “中化合成”依維莫司 B02 | 粉劑 | 中化合成生技股份有限公司山佳工廠 | 2029/06/21 | 器官移植抗排斥藥物、治療腎臟癌藥物。 |

<details><summary><strong>已註銷</strong>（5 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第024771號</td><td>卓定康錠 0.75 毫克</td><td>EVEROLIMUS</td><td>2026/04/16</td></tr><tr><td>衛署藥輸字第024773號</td><td>卓定康可溶錠 0.25 毫克</td><td>EVEROLIMUS</td><td>2021/03/26</td></tr><tr><td>衛署藥輸字第024774號</td><td>卓定康可溶錠 0.1 毫克</td><td>EVEROLIMUS</td><td>2021/03/23</td></tr><tr><td>衛署藥輸字第024775號</td><td>卓定康錠 1.0 毫克</td><td>EVEROLIMUS</td><td>2021/03/26</td></tr><tr><td>衛署藥輸字第025166號</td><td>癌伏妥錠10毫克</td><td>EVEROLIMUS</td><td>2020/11/09</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（mTOR 抑制劑，Rapalog 類） |
| 骨髓抑制風險 | 低至中度（常見血小板減少、貧血；嚴重嗜中性白血球減少較少見） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含白血球分類）、肝腎功能、空腹血糖、血脂（三酸甘油酯、總膽固醇）、尿液分析 |
| 處置防護 | 依細胞毒性藥物標準處置規範操作；口服錠劑／膠囊應整顆吞服，勿壓碎或咀嚼 |

---

## 安全性考量

**藥物交互作用**（資料庫共收錄 383 筆，以下列出主要交互作用）：

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Clarithromycin | Major | 強效 CYP3A4 抑制劑，可能顯著升高 Everolimus 血中濃度，增加毒性風險 |
| Aprepitant | Major | 中度 CYP3A4 抑制劑，影響 Everolimus 暴露量 |
| Dexamethasone | Major | CYP3A4 誘導劑，可能降低 Everolimus 血中濃度及療效 |
| Amphotericin B | Major | 嚴重交互作用，需評估替代方案或加強監測 |
| Amphotericin B (lipid complex) | Major | 嚴重交互作用，需評估替代方案或加強監測 |
| Metformin | Moderate | mTOR 抑制可影響胰島素訊號，可能削弱 Metformin 降血糖效果 |
| Canagliflozin / Dapagliflozin / Empagliflozin | Moderate | 多種 SGLT2 抑制劑均列中度交互作用，併用時需監測血糖 |
| Glimepiride / Chlorpropamide / Alogliptin 等降血糖藥 | Moderate | Everolimus 可能升高血糖，削弱多種降血糖藥療效 |

> 詳細警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Phase 2 臨床試驗（NCT03114527，n=48）直接研究 Everolimus 聯合 Ribociclib 用於進展性去分化脂肉瘤，結果已於 2024 年正式發表；去分化脂肉瘤的 mTOR 通路活化具文獻記錄，機轉依據充分，整體證據達 L2 等級，支持進一步推進評估。

**若要推進需要：**
- 補全 Everolimus 詳細作用機轉資料（建議查詢 DrugBank API，填補 MOA 缺口）
- 取得 NCT03114527 完整療效數據（ORR、PFS、OS）並與標準化療對比
- 確立脂肉瘤亞型的分子分型策略（DDL mTOR 活化狀態篩選，作為病患選擇依據）
- 確認聯合用藥（Ribociclib）的劑量調整方案及血液毒性監測計畫
- 評估台灣健保給付可行性及罕見腫瘤擴大使用申請途徑

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表列入 lenvatinib 製劑「樂衛瑪膠囊」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

