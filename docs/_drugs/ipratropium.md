---
layout: default
title: Ipratropium
parent: 高證據等級 (L1-L2)
nav_order: 154
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-16
description: "Ipratropium：預測新適應症為阻塞性肺疾病 (Obstructive Lung Disease)（證據等級 L1）。原適應症：慢性阻塞性支氣管炎、支氣管氣喘"
monitor_inn: "Ipratropium"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "respiratory malformation", "papillary conjunctivitis", "Rienhoff syndrome", "anaphylaxis", "food-dependent exercise-induced anaphylaxis"]
---

# Ipratropium
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Ipratropium：從慢性阻塞性支氣管炎／支氣管氣喘到阻塞性肺疾病

## 一句話總結

Ipratropium（溴化伊普托品）是一種抗膽鹼支氣管擴張劑，原本用於慢性阻塞性支氣管炎與支氣管氣喘。
TxGNN 模型預測它可能對**阻塞性肺疾病 (Obstructive Lung Disease)** 有效，
目前有 **25 個臨床試驗**和 **19 篇文獻**支持這個方向。
需要說明的是，這個預測與現有核准適應症高度重疊，不是典型的「新適應症」再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性阻塞性支氣管炎、支氣管氣喘 |
| 預測新適應症 | 阻塞性肺疾病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 26 張（有效單方 7／有效複方 5／已過期 1／已註銷 13） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料庫欄位。依據已整理的文獻，Ipratropium 是非選擇性的蕈毒鹼受體拮抗劑，
可阻斷 M3 受體介導的膽鹼性支氣管收縮與黏液分泌，抑制副交感神經對氣道平滑肌的作用。

阻塞性肺疾病（含 COPD 與氣喘）的可逆性氣道收縮，部分由迷走神經膽鹼活性驅動，
因此抗膽鹼藥物在機轉上直接對應。台灣已核准的慢性阻塞性支氣管炎與支氣管氣喘適應症，
本質上就屬於阻塞性肺疾病的範疇。

因此這個預測更像是對既有用途的確認，而非跨疾病的新發現。
其他排名較低的預測（如鼻腔疾病、咽炎、氣管疾病等）證據明顯較弱，本報告聚焦於排名第一的預測。

## 臨床試驗證據

以下列出與阻塞性氣道疾病最相關的試驗（共 25 項，列出 10 項）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | 完成 | 1118 | Ipratropium/salbutamol 經 Respimat 吸入器與 COMBIVENT 比較，為期 12 週的 COPD 支氣管擴張療效與安全性試驗 |
| [NCT01136421](https://clinicaltrials.gov/study/NCT01136421) | Phase 3 | 完成 | 124 | 硫酸鎂對比 ipratropium（皆合併 SABA）用於 COPD 急性惡化 |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Phase 3 | 完成 | 215 | Tiotropium 與 Atrovent MDI 在菲律賓 COPD 患者的療效與安全性比較 |
| [NCT00239434](https://clinicaltrials.gov/study/NCT00239434) | Phase 3 | 完成 | 200 | Tiotropium 每日一次與 Atrovent MDI 每日四次的雙盲比較 |
| [NCT02182700](https://clinicaltrials.gov/study/NCT02182700) | Phase 3 | 終止 | 47 | Combivent 氣霧劑加輔助吸入器用於成人中重度氣喘急性發作 |
| [NCT02260011](https://clinicaltrials.gov/study/NCT02260011) | Phase 2 | 完成 | 41 | Ipratropium HFA-134a 與 Atrovent CFC 在 COPD 的單劑交叉比較 |
| [NCT01691482](https://clinicaltrials.gov/study/NCT01691482) | Phase 4 | 完成 | 56 | Albuterol 與 ipratropium 單獨及合併使用，評估 COPD 每日支氣管擴張反應 |
| [NCT06918418](https://clinicaltrials.gov/study/NCT06918418) | Phase 4 | 完成 | 60 | 兒童急性氣喘：salbutamol 單用對比 salbutamol 加 ipratropium |
| [NCT04446637](https://clinicaltrials.gov/study/NCT04446637) | Phase 3 | 撤回 | 0 | Ipratropium/levosalbutamol 固定複方對比自由複方（未收案） |
| [NCT02235428](https://clinicaltrials.gov/study/NCT02235428) | Phase 4 | 終止 | 3 | 幼童急性氣喘加用 ipratropium 的雙盲試驗（僅 3 人，證據力極低） |

**備註：**
- 多項已完成的 Phase 3 試驗中，ipratropium 多作為對照藥或複方成分，並非全部以單方為主要研究對象。
- 部分試驗（如 NCT04446637、NCT02235428）已撤回或提前終止，證據權重有限。
- 另有 NCT00371527（急性支氣管炎、無基礎肺病、200 人，已完成）顯示同一藥物亦在非阻塞性族群中被研究，但不屬阻塞性疾病證據。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35616126](https://pubmed.ncbi.nlm.nih.gov/35616126/) | 2022 | Meta-analysis | Cochrane Database Syst Rev | 評估硫酸鎂作為 COPD 急性惡化輔助治療（與 ipratropium 為同領域背景） |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | 系統性回顧 | Cochrane Database Syst Rev | Tiotropium 與 ipratropium 用於 COPD 的比較（2015 更新版） |
| [24043433](https://pubmed.ncbi.nlm.nih.gov/24043433/) | 2013 | 系統性回顧 | Cochrane Database Syst Rev | Tiotropium 與 ipratropium 用於 COPD 的比較（2013 版） |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | Ann Pharmacother | Ipratropium 與 tiotropium 併用於 COPD 的療效與安全性資料 |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Albuterol、ipratropium 及其複方在 COPD 的機轉、療效與安全性 |
| [10565879](https://pubmed.ncbi.nlm.nih.gov/10565879/) | 1999 | Review | Respir Care Clin N Am | 抗膽鹼支氣管擴張劑；ipratropium 單用或與 albuterol 併用的肺功能改善已獲證實 |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Review | Clin Pharm | Ipratropium 在阻塞性肺疾病的藥理、藥動、療效、不良反應與劑量 |
| [15987237](https://pubmed.ncbi.nlm.nih.gov/15987237/) | 2005 | Review | Treat Respir Med | Ipratropium HFA 吸入劑型用於支氣管痙攣的維持治療 |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | 回溯性研究 | Medicine | 益生菌合併 budesonide 與 ipratropium 治療 COPD（118 人），評估肺功能與腸道菌相 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | 指引 | Basic Clin Pharmacol Toxicol | 芬蘭穩定期 COPD 診斷與藥物治療指引 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Ipratropium 的不重複許可證共 **26 張**：有效單方 7 張、有效複方 5 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 13 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第043943號 | 〝信東〞益撲喘吸入液0.25毫克/毫升 | 吸入用液劑 | 信東生技股份有限公司 | 2030/09/01 | 慢性阻塞性支氣管炎、支氣管氣喘。 |
| 衛署藥製字第048701號 | “晟德”益喘平吸入液 0.25 毫克/毫升 | 吸入用液劑 | 晟德大藥廠股份有限公司 | 2027/05/01 | 慢性阻塞性支氣管炎、支氣管氣喘。 |
| 衛署藥製字第049595號 | 輔安喘吸入液 0.25 毫克/毫升 | 吸入用液劑 | 瑩碩生技醫藥股份有限公司 | 2028/08/13 | 慢性阻塞性支氣管炎、支氣管氣喘。 |
| 衛署藥輸字第018863號 | 定喘樂單一劑量吸入液０．５毫克/２毫升 | 吸入用液劑 | 台灣百靈佳殷格翰股份有限公司 | 2031/11/05 | 慢性阻塞性支氣管炎、支氣管氣喘。 |
| 衛部藥輸字第026375號 | 溴化伊普托品 | （粉） | 川聖貿易股份有限公司 | 2029/08/19 | 慢性阻塞性支氣管炎、支氣管氣喘 |
| 衛部藥輸字第027316號 | 溴化依普托品 | （粉） | 新雙隆生技股份有限公司 | 2027/11/17 | 慢性阻塞性肺疾、支氣管氣喘 |
| 衛部藥輸字第027346號 | 溴化依普托品 | （粉） | 新雙隆生技股份有限公司 | 2027/12/15 | 慢性阻塞性支氣管炎、支氣管氣喘 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（5 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第049369號 | “信東”倍舒美吸入液 | IPRATROPIUM BROMIDE、SALBUTAMOL (SULFATE) | 口腔吸入劑 | 用於治療阻塞性呼吸道疾病併發的可逆性支氣管痙攣，需要一種以上支氣管擴張劑治療者。 |
| 衛署藥製字第055577號 | 〝晟德〞適氣寧吸入液 | SALBUTAMOL SULFATE(ALBUTEROL SULFATE)、IPRATROPIUM BROMIDE | 口腔吸入劑 | 用於治療阻塞性呼吸道疾病併發的可逆性支氣管痙攣，需要一種以上支氣管擴張劑治療者。 |
| 衛署藥輸字第023357號 | 冠喘衛單一劑量吸入液 | IPRATROPIUM BROMIDE、SALBUTAMOL | 口腔吸入劑 | 用於治療阻塞性呼吸道疾病併發的可逆性支氣管痙攣，需要一種以上支氣管擴張劑治療者。 |
| 衛署藥輸字第023473號 | 備喘全定量噴霧液 "德國廠" | IPRATROPIUM BROMIDE、FENOTEROL HYDROBROMIDE | 噴霧劑 | 下列支氣管痙攣疾患之預防和治療:支氣管氣喘、阻塞性支氣管炎、慢性支氣管炎、氣腫和伴支氣管痙攣之肺支氣管障害。 |
| 衛部藥製字第059891號 | 樂佐寧複方噴鼻液 | Ipratropium bromide (monohydrate)、XYLOMETAZOLINE HCL | 鼻用噴液劑 | 一般感冒引起的鼻塞、流鼻水症狀之治療。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第046902號</td><td>宜喘去吸入液 0.25 公絲/公撮</td><td>IPRATROPIUM BROMIDE</td><td>2025/01/13</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（13 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第029201號</td><td>備喘全定量噴霧液</td><td>IPRATROPIUM BROMIDE、FENOTEROL HYDROBROMIDE</td><td>2016/09/19</td></tr><tr><td>衛署藥製字第035504號</td><td>定喘樂定量噴霧液０．４公絲/公撮（溴化伊普托品）</td><td>IPRATROPIUM BROMIDE (ANHYDROUS)</td><td>2016/09/19</td></tr><tr><td>衛署藥製字第036941號</td><td>定喘樂吸入液０．２５公絲/公撮（溴化伊普托品）</td><td>IPRATROPIUM BROMIDE (ANHYDROUS)</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第044074號</td><td>冠喘衛定量噴霧液</td><td>IPRATROPIUM BROMIDE(IPRATROPIUM BROMIDE ANHYDROUS mg)、SALBUT…</td><td>2017/02/09</td></tr><tr><td>衛署藥製字第048365號</td><td>合氣舒 單一劑量吸入液</td><td>IPRATROPIUM BROMIDE、SALBUTAMOL (SULFATE)</td><td>2017/03/28</td></tr><tr><td>衛署藥輸字第009107號</td><td>安喘樂定量噴霧液</td><td>IPRATROPIUM BROMIDE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015291號</td><td>定喘樂吸入液０．０２５％</td><td>IPRATROPIUM BROMIDE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第020703號</td><td>益普芬口腔吸入劑</td><td>FENOTEROL HYDROBROMIDE、IPRATROPIUM BROMIDE、IPRATROPIUM BROMI…</td><td>2010/06/03</td></tr><tr><td>衛署藥輸字第022974號</td><td>抑洛喘吸入液〝岱比博〞</td><td>IPRATROPIUM BROMIDE(IPRATROPIUM BROMIDE ANHYDROUS mg)</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第023512號</td><td>宜克喘吸入液２５０微克／公撮</td><td>IPRATROPIUM BROMIDE</td><td>2021/12/08</td></tr><tr><td>衛署藥輸字第023614號</td><td>定喘樂２０微公克定量噴霧液</td><td>Ipratropium bromide (monohydrate)</td><td>2018/10/22</td></tr><tr><td>衛部藥製字第059642號</td><td>合氣舒單一劑量吸入液</td><td>IPRATROPIUM BROMIDE、SALBUTAMOL SULFATE(ALBUTEROL SULFATE)</td><td>2024/04/27</td></tr><tr><td>衛部藥輸字第026137號</td><td>歐治鼻雙效噴鼻液</td><td>XYLOMETAZOLINE HCL、Ipratropium bromide (monohydrate)</td><td>2025/04/07</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **禁忌／需謹慎的相關疾病（來自知識圖譜，非仿單內容）**：高血壓、長 QT 症候群、癲癇、糖尿病與酮酸中毒、良性攝護腺增生、膀胱頸阻塞、閉角型青光眼與高眼壓、甲狀腺機能亢進、心肌缺血與冠狀動脈疾病、猝死性心跳停止、心臟傳導疾病、酸中毒、低血鉀等。此清單為模型推論的關聯，實際禁忌請以仿單為準。
- **藥物交互作用**：共 106 項已知交互作用，多為中度。主要為其他抗膽鹼藥物，如 atropine、hyoscyamine、scopolamine、glycopyrronium、dicyclomine、aclidinium、trospium 等，重疊使用可能加重抗膽鹼不良反應。另有 promethazine、chlorpheniramine 等抗組織胺，以及 prucalopride、eluxadoline 等。
- **相關安全訊號（文獻）**：曾有吸入 ipratropium 後發生嚴重過敏反應的病例報告，以及吸入後單側瞳孔放大的案例（可能與藥物接觸眼部有關）。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多個已完成的 Phase 3 試驗與多篇系統性回顧支持 ipratropium 在 COPD／氣喘的支氣管擴張療效，且此用途已是台灣核准適應症，證據等級為 L1。
- 這並非真正的新適應症，因此重點在於安全護欄（抗膽鹼不良反應、青光眼與尿滯留風險、與其他抗膽鹼藥併用），而非開發新用途。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA）。
- 若欲評估「新」用途，應另行審視排名較低的預測（鼻腔疾病、咽炎、氣管疾病等）；這些目前僅有間接或前臨床證據，建議 Hold 或列為研究問題。
- 建立與其他抗膽鹼藥物併用、特定族群（青光眼、攝護腺肥大、心血管疾病）的用藥監測計畫。
- 取得完整仿單的警語與禁忌資訊。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

