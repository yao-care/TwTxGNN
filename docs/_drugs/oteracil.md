---
layout: default
title: Oteracil
parent: 高證據等級 (L1-L2)
nav_order: 200
evidence_level: L2
indication_count: 10
---

# Oteracil
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

# Oteracil：從胃癌到大腸腫瘤

## 一句話總結

Oteracil 是 S-1 複方（tegafur／gimeracil／oteracil）的成分之一，原本用於胃癌治療。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，
目前有 **6 個臨床試驗**和 **10 篇文獻**與此方向相關，但這些證據針對的是 S-1 複方，而非 Oteracil 單一成分。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌用藥 |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張（有效單方 2／有效複方 4／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Oteracil 是 S-1 中負責保護腸胃道的成分。它會抑制腸道黏膜中的 OPRT 酶，減少 5-FU 在腸道局部被活化，進而降低腸胃道毒性。Oteracil 本身沒有抗腫瘤活性，大腸直腸癌的療效來自 tegafur（5-FU 前驅藥）與 gimeracil（DPD 抑制劑）。目前缺乏 Oteracil 單一成分的詳細作用機轉資料。

胃癌與大腸腫瘤同屬消化道腫瘤，且皆為氟化嘧啶類藥物的常見治療對象。台灣核准的 S-1 複方製劑已包含「與 Irinotecan 合併使用於已使用含 Oxaliplatin 化療失敗之轉移性大腸直腸癌」的適應症，這支持了預測方向的合理性。

需要注意：現有臨床證據評估的是整個 S-1 方案，不能直接解讀為 Oteracil 單獨對大腸腫瘤有效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 已完成 | 1535 | UFT＋leucovorin 對比 S-1 用於 Stage III 結腸癌術後輔助治療 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 狀態未知 | 1191 | SOX（Oxaliplatin＋S-1）對比 XELOX 用於 Stage III 大腸直腸癌輔助化療，尚無結果 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 狀態未知 | 40 | S-1＋Bevacizumab 用於先前化療失敗的無法切除或復發大腸直腸癌 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 狀態未知 | 82 | Raltitrexed＋S-1 用於標準化療失敗的轉移性癌症，主要終點為無惡化存活期 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 已終止 | 20 | S-1 或 Capecitabine＋Oxaliplatin 對冠狀動脈血流的影響（心臟安全性，非療效） |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fruquintinib＋S-1 複方用於晚期轉移性大腸直腸癌三線治療，尚無資料 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Cohort | Gan To Kagaku Ryoho | 87 位晚期或復發結腸癌患者使用 S-1＋Irinotecan，3-4 級血液毒性率為 16.1%，並分析風險因子 |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | 動物研究 | Oncol Rep | Irinotecan 可透過下調腫瘤內 thymidylate synthase，克服結腸癌異種移植對 5-FU 的抗藥性 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | 病例報告 | Anticancer Res | S-1＋CPT-11 用於結腸癌肝轉移，達到並維持完全緩解 |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | 病例報告 | Gan To Kagaku Ryoho | SOX＋Panitumumab 降階治療後，成功進行兩階段肝切除 |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | 病例報告 | J Oncol Pharm Pract | S-1 引起高三酸甘油酯血症 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | 病例報告 | Eur J Dermatol | TS-1 引起紅皮症、廣泛黏膜受累及手足症候群 |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | 病例報告 | Gan To Kagaku Ryoho | Oxaliplatin 引起急性周邊神經病變合併尿滯留 |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | 病例報告 | Gan To Kagaku Ryoho | 大腸直腸癌切除後腹膜復發，以腹腔鏡反覆切除 |
| [30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/) | 2018 | 病例報告 | Gan To Kagaku Ryoho | 結腸癌術後復發疼痛，經電腦斷層導引腹腔神經叢神經解離術獲完全緩解 |
| [34650027](https://pubmed.ncbi.nlm.nih.gov/34650027/) | 2021 | 病例報告 | Am J Case Rep | 局部晚期胰尾癌合併結腸穿孔，新輔助化療後成功整塊切除 |

目前沒有 RCT 發表文獻，文獻以病例報告為主，直接支持療效的證據有限。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Oteracil 的不重複許可證共 **6 張**：有效單方 2 張、有效複方 4 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥製字第058552號 | "台耀"歐特拉西兒 | 粉劑 | 台耀化學股份有限公司 | 2029/12/08 | 胃癌用藥。 |
| 衛部藥製字第061956號 | "杏輝"氮尿嘧啶酸鉀鹽 | （粉） | 杏輝藥品工業股份有限公司 | 2030/03/31 | 胃癌用藥。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥輸字第025242號 | 愛斯萬膠囊25毫克 | TEGAFUR (FTORAFUR)、OTERACIL POTASSIUM、GIMERACIL | 膠囊劑 | 1. 胃癌： (１) 胃癌術後輔助性化療，用於罹患TNM Stage II (排除TI)、IIIA或IIIB胃癌且接受過胃癌根除性手術之成年病人。 (２) 適用於治療無法切除之晚期… |
| 衛署藥輸字第025243號 | 愛斯萬膠囊20毫克 | TEGAFUR (FTORAFUR)、OTERACIL POTASSIUM、GIMERACIL | 膠囊劑 | 1. 胃癌： (１) 胃癌術後輔助性化療，用於罹患TNM Stage II (排除TI)、IIIA或IIIB胃癌且接受過胃癌根除性手術之成年病人。 (２) 適用於治療無法切除之晚期… |
| 衛部藥製字第060480號 | "杏輝"剋伏膠囊25毫克 | TEGAFUR (FTORAFUR)、WATER PURIFIED ( EQ TO AQUEOUS PURIFIED O… | 膠囊劑 | (一)胃癌：1、胃癌術後輔助性化療，本品用於罹患TNM STAGE II (排除TI)，IIIA或IIIB胃癌且接受過胃癌根除性手術之成年患者。2、本品適用於治療無法切除之晚期胃癌… |
| 衛部藥製字第060482號 | "杏輝"剋伏膠囊20毫克 | GIMERACIL、OTERACIL POTASSIUM、TEGAFUR (FTORAFUR)、WATER PURIFI… | 膠囊劑 | (一)胃癌：1、胃癌術後輔助性化療，本品用於罹患TNM STAGE II (排除TI)，IIIA或IIIB胃癌且接受過胃癌根除性手術之成年患者。2、本品適用於治療無法切除之晚期胃癌… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

Oteracil 本身無抗腫瘤活性，但它是抗腫瘤複方 S-1（氟化嘧啶類）的成分，使用時需考量整體方案的細胞毒性。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氟化嘧啶類複方 S-1 的成分） |
| 骨髓抑制風險 | 中度（S-1＋Irinotecan 研究中 3-4 級血液毒性率為 16.1%） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 請參考原廠仿單與細胞毒性藥物處置規範 |

## 安全性考量

安全性資訊請參考原廠仿單。

依現有文獻，S-1 方案相關的不良反應包括手足症候群、皮膚與黏膜反應、高三酸甘油酯血症及血液毒性。另有試驗在評估氟化嘧啶類的潛在心臟毒性（NCT02216149，已終止，無結果可引用）。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有已完成的 Phase 3 隨機試驗（NCT00660894）及多個 Phase 2/3 試驗，在大腸／結腸癌中評估含 S-1 的方案，且台灣 S-1 複方已核准用於轉移性大腸直腸癌。
- 但證據針對整個 S-1 複方，Oteracil 只是保護腸胃道的成分、無自身抗腫瘤作用，所以不宜視為 Oteracil 單獨的新適應症；其他預測疾病（如良性腫瘤）僅有模型預測，建議 Hold。

**若要推進需要：**
- 補充 Oteracil 的作用機轉資料，並釐清其在複方中的角色
- 取得 NCT00660894 等已完成試驗的結果，確認 S-1 在結腸癌的療效與安全性
- 確認推進對象是 S-1 複方而非 Oteracil 單方，並核對現有許可證適應症是否已涵蓋
- 制定血液學、皮膚與腸胃道毒性的監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證數寫 8 張 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

