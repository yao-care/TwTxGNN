---
layout: default
title: Vonoprazan
parent: 高證據等級 (L1-L2)
nav_order: 304
evidence_level: L2
indication_count: 10
monitor_inn: "Vonoprazan"
predicted_indications: ["active peptic ulcer disease", "peptic ulcer perforation", "gastrojejunal ulcer", "hiatus hernia (disease)", "achlorhydria", "pylorospasm", "Dieulafoy lesion", "gastric dilatation", "cascade stomach", "hemorrhagic duodenitis"]
last_modified_at: 2026-10-16
description: "Vonoprazan：預測新適應症為活動性消化性潰瘍 (Active Peptic Ulcer Disease)（證據等級 L2）。原適應症：糜爛性食道炎(EE)的治療及維持治療"
---

# Vonoprazan
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

# Vonoprazan：從糜爛性食道炎與消化性潰瘍到活動性消化性潰瘍

## 一句話總結

Vonoprazan（福星定）是一種鉀離子競爭性胃酸阻斷劑（P-CAB），原本用於糜爛性食道炎、胃潰瘍、十二指腸潰瘍及輔助根除幽門螺旋桿菌。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前**無登記的臨床試驗**，但有 **17 篇文獻**支持這個方向。
需要特別說明：胃潰瘍與十二指腸潰瘍本來就是台灣核准的適應症，這個預測屬於仿單內適應症，並非真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糜爛性食道炎(EE)的治療及維持治療；治療胃潰瘍；治療十二指腸潰瘍；輔助根除幽門螺旋桿菌 |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2（依資料彙整的評分；本次資料未登記臨床試驗，主要依賴文獻中的 RCT 與統合分析） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 3／有效複方 0／已註銷 1） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。根據文獻，Vonoprazan 是首創的鉀離子競爭性胃酸阻斷劑，可逆地抑制胃壁細胞的 H+/K+-ATPase（質子泵），提供強效且持久的胃酸抑制，且不需酸活化，起效快，較不受進食時間及 CYP2C19 基因多型性影響。

消化性潰瘍屬於酸依賴性疾病，持續而強效的胃酸抑制有助於潰瘍癒合並降低復發。Vonoprazan 在日本自 2015 年起已用於胃十二指腸潰瘍，台灣許可證也已核准胃潰瘍與十二指腸潰瘍的治療，因此這項預測與現有適應症一致，屬於「模型驗證了已知用途」，並非新用途開發。

TxGNN 同時預測了其他相關疾病，其中證據較有限者包括消化性潰瘍穿孔、胃空腸吻合口潰瘍、食道裂孔疝、出血性十二指腸炎，皆屬以胃酸抑制作為輔助的間接用途，證據多由未併發潰瘤或 GERD 的資料外推。其餘如無胃酸症、幽門痙攣、Dieulafoy 病灶、胃擴張、瀑布狀胃，機轉上缺乏合理連結，且幾乎沒有臨床證據，建議暫緩。特別是無胃酸症，本身已缺乏胃酸，再抑制胃酸並無治療意義，應視為模型的假陽性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列為與活動性消化性潰瘍較直接相關的文獻（資料彙整中另有多篇為 H. pylori 綜述、植物萃取物動物研究，與 Vonoprazan 的直接關聯較低，未列入）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28988197](https://pubmed.ncbi.nlm.nih.gov/28988197/) | 2018 | 隨機對照試驗 | Gut | 以 lansoprazole 為對照，評估 Vonoprazan 預防長期 NSAID 治療期間潰瘍復發的非劣效性及延長使用的安全性 |
| [28267236](https://pubmed.ncbi.nlm.nih.gov/28267236/) | 2017 | 前瞻性隨機對照試驗 | Digestive Endoscopy | 評估 Vonoprazan 對內視鏡黏膜下剝離術後人工胃潰瘍的癒合效果 |
| [26369775](https://pubmed.ncbi.nlm.nih.gov/26369775/) | 2016 | Review | Clinical Pharmacokinetics | 說明首創 P-CAB 的藥動與藥效，涵蓋胃十二指腸潰瘍、逆流性食道炎等適應症的用法 |
| [39156336](https://pubmed.ncbi.nlm.nih.gov/39156336/) | 2024 | Review | Cureus | 回顧 Vonoprazan 在胃酸相關疾病（GERD、消化性潰瘍、H. pylori）的療效與安全性 |
| [32998241](https://pubmed.ncbi.nlm.nih.gov/32998241/) | 2020 | Review | Pharmaceuticals | 討論 Vonoprazan 用於 H. pylori 感染治療的潛在益處 |
| [42084149](https://pubmed.ncbi.nlm.nih.gov/42084149/) | 2026 | Review | Polish Archives of Internal Medicine | P-CAB 用於糜爛性逆流疾病與壓力性潰瘍預防的敘述性回顧 |
| [37066678](https://pubmed.ncbi.nlm.nih.gov/37066678/) | 2023 | 藥動/藥效研究 | Aliment Pharmacol Ther | 轉譯性 PK/PD 分析支持糜爛性食道炎與 H. pylori 感染的最佳劑量 |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 統合分析 | Am J Gastroenterol | 比較 P-CAB 與 PPI 治療 C/D 級食道炎的療效與安全性（針對食道炎，非潰瘍） |

另有文獻針對相關子題：Vonoprazan 與 PPI 治療及預防胃或十二指腸潰瘍的系統性回顧與統合分析（PMID 39294424，2024，Digestive Diseases and Sciences），摘要指出其對潰瘍的療效「仍有爭議」，這一點需要審慎看待。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Vonoprazan 的不重複許可證共 **4 張**：有效單方 3 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027623號 | 福星定膜衣錠20毫克 | 膜衣錠 | 台灣武田藥品工業股份有限公司 | 2029/08/12 | 1. 糜爛性食道炎(EE)的治療及維持治療。 2. 治療胃潰瘍。 3. 治療十二指腸潰瘍。 4. 輔助根除幽門螺旋桿菌(Helicobacter pylori)。 |
| 衛部藥輸字第029115號 | 芙諾抑瘍延胡索酸鹽 | （粉） | 丞泰企業有限公司 | 2031/03/12 | 胃潰瘍治療藥 |
| 衛部藥陸輸字第001272號 | 芙諾抑瘍反丁烯二酸鹽 | （粉） | 丞泰企業有限公司 | 2031/04/23 | 胃潰瘍治療藥 |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027622號</td><td>福星定膜衣錠10毫克</td><td>Vonoprazan Fumarate</td><td>2026/04/27</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料中僅有藥理標的資訊（作用於胃 H+/K+-ATPase，ATP4A），並無具體的藥物交互作用條目。
- **文獻中的安全訊號**：
  - 長期使用（如 6 年）的病例報告顯示有明顯的胃黏膜變化、血清胃泌素升高及停藥後反彈性胃酸過度分泌。
  - 有 Vonoprazan 相關的胃黏膜紅斑與白色球狀病灶（white globe appearance）病例報告。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 活動性消化性潰瘍已涵蓋於台灣核准的胃潰瘍與十二指腸潰瘍適應症，並有 RCT 及統合分析等文獻支持，模型預測與臨床現況一致。
- 但本次資料沒有登記的臨床試驗，也缺乏作用機轉的結構化資料與完整安全性資料，Vonoprazan 對潰瘍的療效相較 PPI 在文獻中仍有爭議，且長期使用有反彈性胃酸過度分泌等訊號，因此需設置使用上的護欄。

**若要推進需要：**
- 補充 DrugBank 作用機轉資料及原廠仿單的警語與禁忌症。
- 取得 Vonoprazan 與 PPI 治療潰瘍的 Phase 3 RCT 完整數據，釐清相對療效。
- 訂定長期使用的監測計畫（胃泌素、胃黏膜變化、停藥後反彈）。
- 其他預測疾病（潰瘍穿孔、胃空腸吻合口潰瘍、食道裂孔疝、出血性十二指腸炎）可列為研究問題，需先有直接證據；無胃酸症、幽門痙攣、Dieulafoy 病灶、胃擴張、瀑布狀胃則建議暫緩。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市資訊表「衛部藥輸字（待確認）福星定膜衣錠10毫克」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「許可證數：1 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

