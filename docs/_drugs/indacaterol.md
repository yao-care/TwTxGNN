---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Indacaterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Indacaterol：從慢性阻塞性肺疾到腎因性抗利尿激素不適當分泌症候群

## 一句話總結

Indacaterol 是一種超長效 β2 腎上腺受體作用劑（ultra-LABA），原本用於慢性阻塞性肺疾（COPD）的維持治療。
TxGNN 模型預測它可能對**腎因性抗利尿激素不適當分泌症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效。
但目前**沒有任何臨床試驗或文獻**支持這個方向，且機轉上可能適得其反。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性阻塞性肺疾之維持治療 |
| 預測新適應症 | 腎因性抗利尿激素不適當分泌症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 7 張（有效單方 1／有效複方 3／已註銷 3） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。根據已知資訊，Indacaterol 是吸入型長效 β2 受體作用劑。它會提高細胞內 cAMP，使氣道平滑肌持續放鬆，因此用於 COPD 與氣喘。

NSIAD 的成因是 AVPR2（血管加壓素 V2 受體）的功能獲得型突變，使 cAMP 訊號持續過度活化，導致腎臟不當地濃縮尿液。Indacaterol 同樣會提高 cAMP，所以**機轉上看不出治療關聯，反而可能加劇 cAMP 訊號而適得其反**。

因此，這個預測目前只能視為模型分數的結果，缺乏機轉與臨床支持，很可能是知識圖譜中的關聯假象。

另外，預測清單中排名第 7 的「支氣管疾病 (bronchial disease)」有較多研究。但那與藥物原本的 COPD 與氣喘適應症高度重疊，不算真正的藥物再利用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Indacaterol 的不重複許可證共 **7 張**：有效單方 1 張、有效複方 3 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025282號 | 昂舒吸入膠囊150微克 | 吸入用膠囊劑 | 台灣諾華股份有限公司 | 2030/10/19 | 慢性阻塞性肺疾之維持治療 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（3 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第026301號 | 昂帝博吸入膠囊110/50微克 | INDACATEROL MALEATE、Glycopyrronium bromide | 吸入用膠囊劑 | 慢性阻塞性肺疾 (COPD; 包括慢性支氣管炎及肺氣腫 ) 之維持治療。降低有惡化病史病人之COPD 惡化。 |
| 衛部藥輸字第028048號 | 艾能舒吸入膠囊150/50/80微克 | Glycopyrronium bromide、Indacaterol acetate、MOMETASONE FUROAT… | 吸入用膠囊劑 | 適用於併用吸入性長效型β2-腎上腺受體作用劑和吸入性皮質類固醇治療氣喘仍控制不佳的成年病人，做為氣喘維持治療。 |
| 衛部藥輸字第028049號 | 艾能舒吸入膠囊150/50/160微克 | Glycopyrronium bromide、Indacaterol acetate、MOMETASONE FUROAT… | 吸入用膠囊劑 | 適用於併用吸入性長效型β2-腎上腺受體作用劑和吸入性皮質類固醇治療氣喘仍控制不佳的成年病人，做為氣喘維持治療。 |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第028050號</td><td>愛克喘吸入膠囊150/160微克</td><td>Indacaterol acetate、MOMETASONE FUROATE</td><td>2026/04/22</td></tr><tr><td>衛部藥輸字第028051號</td><td>愛克喘吸入膠囊150/320微克</td><td>Indacaterol acetate、MOMETASONE FUROATE</td><td>2026/04/22</td></tr><tr><td>衛部藥輸字第028052號</td><td>愛克喘吸入膠囊150/80微克</td><td>Indacaterol acetate、MOMETASONE FUROATE</td><td>2026/04/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，非仿單文字）：高血壓、長 QT 症候群（含家族性）、癲癇、高血糖、缺鉀症、糖尿病、糖尿病酮酸中毒、心因性猝死、心臟傳導疾病、甲狀腺毒症／甲狀腺功能亢進／葛瑞夫茲氏病、冠狀動脈疾病。
- **藥物交互作用**：共記錄 440 筆。
  - 中度：Epinephrine、Clarithromycin、Famotidine、Isometheptene，以及多種降血糖藥（Acarbose、Metformin、Pioglitazone、Alogliptin、Saxagliptin、Albiglutide、Canagliflozin、Dapagliflozin、Chlorpropamide）。
  - 輕度：多種皮質類固醇（Hydrocortisone、Dexamethasone、Budesonide 等）與 Aprepitant。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有臨床試驗與文獻支持（證據等級 L5）。
- Indacaterol 的 cAMP 提升作用與 NSIAD 的病理機轉方向一致，可能使病情惡化，沒有合理的治療依據。

**若要推進需要：**
- 取得 Indacaterol 的作用機轉資料，並實際評估它對 AVPR2 訊號與腎臟集尿管水分再吸收的影響。
- 先做前臨床研究（細胞或動物模型），確認不會加劇 cAMP 過度活化。
- 若要重新評估，建議改以排名較高、機轉較合理的候選，或把重點放在已有證據的呼吸道適應症。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」寫氣喘維持治療 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

