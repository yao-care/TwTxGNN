---
layout: default
title: Terbutaline
parent: 高證據等級 (L1-L2)
nav_order: 269
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-16
description: "Terbutaline：預測新適應症為阻塞性肺病 (Obstructive Lung Disease)（證據等級 L1）。原適應症：支氣管喘息引起之支氣管閉塞性障害、和呼吸困難諸症狀之緩解"
---

# Terbutaline
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
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

# Terbutaline：從支氣管氣喘到阻塞性肺病

## 一句話總結

Terbutaline（特必林）是一種選擇性 β2 腎上腺素受體促效劑，原本用於緩解支氣管氣喘、支氣管炎與肺氣腫所伴隨的支氣管痙攣。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，
目前有 **14 個臨床試驗**和 **20 篇文獻**支持這個方向，其中多項為已完成的 Phase 3 試驗。
這個新適應症與現有核准適應症高度重疊，實質上接近既有用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 支氣管喘息引起之支氣管閉塞性障害、和呼吸困難諸症狀之緩解 |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 52 張（有效單方 17／有效複方 0／已過期 1／已註銷 34） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Terbutaline 屬於 β2 腎上腺素受體促效劑類別。這類藥物已知可使氣道平滑肌細胞內的 cAMP 上升，進而使氣道平滑肌放鬆而擴張支氣管（此為文獻中對 β2 促效劑的一般性描述，並非來自本報告所整理的藥物機轉資料）。

台灣核准適應症包含支氣管氣喘、慢性支氣管炎、氣喘性支氣管炎、支氣管擴張症與肺氣腫，這些疾病都屬於氣道阻塞性疾病。因此「阻塞性肺病」與原適應症高度重疊，預測合理性高，臨床上屬於既有用途的延伸。

排名第 2 的「呼吸道畸形 (Respiratory Malformation)」僅有間接證據，且支氣管擴張無法矯正結構性異常；排名第 3 的「Rienhoff 症候群」只有模型分數，兩者皆建議暫緩（Hold），以下內容以排名第 1 的預測為主。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | 完成 | 4215 | Symbicort 隨需使用 vs. Pulmicort 每日兩次＋隨需 terbutaline，用於氣喘 |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | 完成 | 3850 | Symbicort 隨需使用 vs. 隨需 terbutaline vs. Pulmicort＋隨需 terbutaline |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | 完成 | 2091 | Symbicort SMART vs. Symbicort＋隨需 terbutaline 0.4 mg，12 個月 |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | 完成 | 1970 | 真實世界氣喘醫療成本比較，terbutaline（Bricanyl）為隨需對照 |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | 完成 | 1600 | Symbicort 單一吸入器療法 vs. 常規最佳治療，26 週 |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | 完成 | 860 | 隨需 vs. 規則使用 budesonide/formoterol＋隨需 terbutaline |
| [NCT00421122](https://clinicaltrials.gov/study/NCT00421122) | Phase 3 | 完成 | 315 | Symbicort 用於中國慢性阻塞性肺病 (COPD) 患者的療效與安全性 |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | 完成 | 120 | 靜脈注射硫酸鎂 vs. terbutaline，用於兒童急性氣喘發作 |
| [NCT00567476](https://clinicaltrials.gov/study/NCT00567476) | Phase 4 | 完成 | 116 | Omalizumab 附加治療對重度過敏性氣喘生活品質的影響（terbutaline 僅為背景治療） |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | 完成 | 95 | Bricanyl Turbuhaler M3 vs. M2 對乙醯甲膽鹼誘發支氣管收縮的保護效果 |

另有 NCT04973345（Phase 2/3，terbutaline 暴露－反應研究）已撤回、登記人數為 0，未提供任何證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | 輕度氣喘以隨需使用吸入型糖皮質激素加速效 β2 促效劑，可作為傳統治療的替代方案 |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | 口服 terbutaline 使 COPD 患者的吸氣口壓與經橫膈壓上升，改善橫膈收縮力 |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | 雙盲兩週比較口服 clenbuterol 與 terbutaline 在慢性阻塞性肺病的支氣管擴張效果 |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | 統合分析 | Naunyn Schmiedebergs Arch Pharmacol | 系統性回顧 terbutaline 在人體的藥動學，涵蓋給藥途徑、年齡、吸菸等影響因素 |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Review | Am J Respir Crit Care Med | β2 促效劑（含 terbutaline）可提供快速的隨需症狀緩解 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Review | Basic Clin Pharmacol Toxicol | 芬蘭穩定期 COPD 診斷與藥物治療指引 |
| [26963310](https://pubmed.ncbi.nlm.nih.gov/26963310/) | 2015 | Review | Tuberkuloz ve Toraks | 氣喘－COPD 重疊症候群的臨床與氣道發炎特徵 |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | Cohort | Chest | 評估 β 阻斷劑與口服 terbutaline 併用於 COPD 合併缺血性心臟病或高血壓患者的作用與交互作用 |
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | 隨機雙盲對照試驗 | Acad Emerg Med | 霧化 terbutaline 加 ipratropium 對比單用 terbutaline，用於需非侵襲性通氣的 COPD 急性惡化 |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | 隨機雙盲交叉試驗 | Lung | 單次吸入 terbutaline 對 COPD 患者肺功能與運動能力的影響 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Terbutaline 的不重複許可證共 **52 張**：有效單方 17 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 34 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（17 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第020022號 | 喘力定錠（特必林） | 錠劑 | 衛肯生技製藥股份有限公司 | 2028/05/25 | 下列疾患的氣道閉塞性障礙所伴隨呼吸困難諸症狀的緩解、支氣管氣喘、慢性支氣管炎、氣喘性支氣管炎、肺氣腫 |
| 衛署藥製字第024817號 | 喘舒寧錠２．５毫克（特必林） | 錠劑 | 元宙化學製藥股份有限公司 | 2029/05/25 | 支氣管氣喘、支氣管炎、肺氣腫、支氣管擴張症 |
| 衛署藥製字第034922號 | 喘利錠２．５毫克（硫酸特必林） | 錠劑 | 永信藥品工業股份有限公司 | 2032/02/15 | 支氣管氣喘、慢性支氣管炎、氣喘性支氣管炎、支氣管擴張症、肺氣腫。 |
| 衛署藥製字第035184號 | "瑪科隆〞喘必克錠２．５毫克（硫酸特必林) | 錠劑 | 盛雲藥品股份有限公司 | 2027/04/29 | 支氣管氣喘、支氣管炎、氣喘性支氣管炎、支氣管擴張症及肺氣腫。 |
| 衛署藥製字第037396號 | 鎮喘錠２．５毫克（硫酸特必林） | 錠劑 | 中國化學製藥股份有限公司新豐工廠 | 2029/03/30 | 支氣管氣喘、支氣管炎、氣喘性支氣管炎、支氣管擴張症，及肺氣腫。 |
| 衛署藥製字第038162號 | "汎生"喘克錠５毫克（硫酸特必林） | 錠劑 | 臺灣汎生製藥廠股份有限公司 | 2029/10/04 | 下列疾患的氣道閉塞性障礙所伴隨呼吸困難諸症狀的緩解、支氣管氣喘、慢性支氣管炎、氣喘性支氣管炎、肺氣腫 |
| 衛署藥製字第040123號 | "十全"喘必寧錠２．５公絲（硫酸特必林） | 錠劑 | 十全實業股份有限公司 | 2031/07/15 | 支氣管氣喘、慢性支氣管炎、氣喘性支氣管炎、支氣管擴張症及肺氣腫 |
| 衛署藥製字第041454號 | "井田"舒管錠2.5毫克(硫酸特必林) | 錠劑 | 井田國際醫藥廠股份有限公司 | 2027/07/11 | 支氣管氣喘、支氣管炎、氣喘性支氣管炎、支氣管擴張症及肺氣腫。 |
| 衛署藥製字第043735號 | "信東"必坦寧吸入液2.5毫克/毫升 | 吸入用液劑 | 信東生技股份有限公司 | 2030/05/08 | 支氣管氣喘、支氣管炎及肺氣腫所伴隨之支氣管痙攣之緩解。 |
| 衛署藥製字第046487號 | 特剋寧吸入液2.5毫克/毫升 | 口腔吸入劑 | 科進製藥科技股份有限公司 | 2029/09/13 | 支氣管氣喘、支氣管炎及肺氣腫所伴隨之支氣管痙攣之緩解。 |
| 衛署藥製字第048343號 | "強生" 撲喘寧錠2.5毫克 | 錠劑 | 強生化學製藥廠股份有限公司 | 2026/10/30 | 支氣管氣喘、支氣管炎、氣喘性支氣管炎、支氣管擴張症及肺氣腫。 |
| 衛署藥製字第048385號 | "晟德" 泰坦尼吸入液2.5毫克/毫升 | 口腔吸入劑 | 晟德大藥廠股份有限公司 | 2031/11/15 | 支氣管氣喘、支氣管炎及肺氣腫所伴隨之支氣管痙攣之緩解。 |
| 衛署藥製字第049183號 | 抑安喘吸入液 2.5 毫克/毫升 | 口腔吸入劑 | 瑩碩生技醫藥股份有限公司 | 2027/12/03 | 支氣管氣喘、支氣管炎及肺氣腫所伴隨之支氣管痙攣之緩解。 |
| 衛署藥製字第049788號 | “台裕”解喘安錠 2.5 毫克 | 錠劑 | 台裕化學製藥廠股份有限公司 | 2028/11/11 | 支氣管氣喘、慢性支氣管炎、氣喘性支氣管炎、肺氣腫、支氣管擴張症。 |
| 衛署藥製字第055901號 | “元宙”喘博寧錠 | 錠劑 | 元宙化學製藥股份有限公司 | 2031/01/04 | 下列疾患的氣道閉塞性障礙所伴隨呼吸困難諸症狀的緩解：支氣管氣喘、慢性支氣管炎、氣喘性支氣管炎、肺氣腫。 |
| 衛部藥製字第058325號 | "汎生"喘克注射液0.2毫克/毫升(特必林) | 注射劑 | 臺灣汎生製藥廠股份有限公司 | 2029/03/01 | 支氣管喘息引起之支氣管閉塞性障害、和呼吸困難諸症狀之緩解。 |
| 衛部藥輸字第027797號 | 硫酸特布泰林 | （粉） | 丸聖貿易股份有限公司 | 2030/01/07 | 支氣管擴張劑 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第029499號</td><td>"利達"特舒喘錠2.5毫克（特必林）</td><td>TERBUTALINE SULFATE</td><td>2024/03/18</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（34 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第026899號</td><td>"汎生"喘克注射液０．２毫克/毫升（特必林）</td><td>TERBUTALINE SULFATE</td><td>2014/12/24</td></tr><tr><td>衛署藥製字第040718號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第047571號</td><td>氣呼舒 吸入液 2.5 毫克/毫升</td><td>TERBUTALINE SULFATE</td><td>2016/09/07</td></tr><tr><td>衛署藥製字第048569號</td><td>"強生" 撲喘寧錠5毫克</td><td>TERBUTALINE SULFATE</td><td>2024/04/29</td></tr><tr><td>衛署藥輸字第007269號</td><td>１－（３，５雙羥苯基）２－四－丁胺基乙醇硫酸鹽</td><td>TERBUTALINE SULFATE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第009433號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第011442號</td><td>撲咳喘錠劑２．５公絲</td><td>TERBUTALINE SULFATE</td><td>1989/06/06</td></tr><tr><td>衛署藥輸字第011466號</td><td>撲咳喘吸入劑</td><td>TERBUTALINE SULFATE</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第012985號</td><td>撲咳喘酏劑０．３公絲/公撮</td><td>TERBUTALINE SULFATE</td><td>1989/07/25</td></tr><tr><td>衛署藥輸字第013516號</td><td>撲咳喘持續錠５公絲</td><td>TERBUTALINE SULFATE</td><td>1989/06/06</td></tr><tr><td>衛署藥輸字第013961號</td><td>撲咳喘持續錠７．５公絲</td><td>TERBUTALINE SULFATE</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第013976號</td><td>撲咳喘注射劑０．５公絲/公撮</td><td>TERBUTALINE SULFATE</td><td>1989/07/25</td></tr><tr><td>衛署藥輸字第014876號</td><td>撲咳喘吸入液２．５公絲/公撮</td><td>TERBUTALINE SULFATE、SODIUM CHLORIDE</td><td>1989/06/06</td></tr><tr><td>衛署藥輸字第015659號</td><td>硫酸特比林</td><td>TERBUTALINE SULFATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第017206號</td><td>撲咳喘吸入劑</td><td>TERBUTALINE SULFATE</td><td>1992/04/17</td></tr><tr><td>衛署藥輸字第017207號</td><td>撲咳喘注射劑０．５公絲/公撮</td><td>TERBUTALINE SULFATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第017209號</td><td>撲咳喘錠２．５公絲</td><td>TERBUTALINE SULFATE</td><td>2007/08/03</td></tr><tr><td>衛署藥輸字第017210號</td><td>撲咳喘持續錠５公絲</td><td>TERBUTALINE SULFATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第017211號</td><td>撲咳喘持續錠７．５公絲</td><td>TERBUTALINE SULFATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第017214號</td><td>撲咳喘吸入液２．５毫克／毫升</td><td>TERBUTALINE SULFATE</td><td>2022/09/28</td></tr><tr><td>衛署藥輸字第017229號</td><td>撲咳喘酏劑０．３公絲/公撮</td><td>TERBUTALINE SULFATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第017299號</td><td>克喘寧</td><td>TERBUTALINE SULFATE</td><td>2003/08/20</td></tr><tr><td>衛署藥輸字第017948號</td><td>撲咳喘定量粉狀吸入劑０．５公絲/劑量</td><td>TERBUTALINE SULFATE</td><td>1998/03/18</td></tr><tr><td>衛署藥輸字第018914號</td><td>撲咳喘吸入劑</td><td>TERBUTALINE SULFATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第020136號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第020386號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第020520號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第021537號</td><td>撲咳喘吸入劑５公絲/２公撮</td><td>TERBUTALINE SULFATE</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第021878號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第022082號</td><td>撲咳喘都保定量粉狀吸入劑0.5毫克/劑量</td><td>TERBUTALINE SULFATE</td><td>2022/07/08</td></tr><tr><td>衛署藥輸字第022964號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2016/09/21</td></tr><tr><td>衛署藥輸字第022969號</td><td>硫酸特必林</td><td>TERBUTALINE SULFATE</td><td>2005/08/16</td></tr><tr><td>衛署藥輸字第023662號</td><td>硫酸特比林</td><td>TERBUTALINE SULFATE</td><td>2008/09/30</td></tr><tr><td>衛部藥輸字第026418號</td><td>硫酸特必林</td><td>Terbutaline Sulfate</td><td>2026/05/22</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自藥物－疾病關聯資料，非仿單文字）：高血壓、癲癇、高血糖、缺鉀症、糖尿病、糖尿病酮酸中毒、心因性猝死、心臟傳導疾病、呼吸衰竭、甲狀腺機能亢進（含葛瑞夫茲氏病）、肺水腫、心肌缺血、冠狀動脈疾病、胎盤早期剝離。
- **藥物交互作用**：共記錄 406 筆。中度交互作用包括 acarbose、epinephrine、famotidine、isometheptene、pioglitazone、canagliflozin、clarithromycin 等；輕度交互作用包括 hydrocortisone、dexamethasone、budesonide 等皮質類固醇。降血糖藥物與 β2 促效劑併用需留意血糖變化；其他經研究者評估需特別留意的包括 β 阻斷劑、可能延長 QT 的藥物與降鉀藥物。

仿單中的主要警語與正式禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多項已完成的 Phase 3 試驗（部分樣本數逾千人）涉及 terbutaline 用於氣道阻塞性疾病，且該適應症與台灣已核准用途高度重疊。但多數試驗中 terbutaline 為對照或隨需藥物，而非主要試驗藥物，直接證據強度需審慎解讀。
- 心血管效應（心搏過速、低血鉀、QT 延長）與大量藥物交互作用需要管控。

**若要推進需要：**
- 補充詳細的作用機轉（MOA）資料
- 確認各劑型（注射、口服、吸入）對應的目標族群與給藥途徑
- 建立心血管與血鉀監測計畫，並針對併用 β 阻斷劑、降血糖藥物、QT 延長藥物制定處置原則
- 對排名第 2（呼吸道畸形）與第 3（Rienhoff 症候群）的預測維持 Hold，除非有新增的直接證據

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第041766號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第026805號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第019714號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表許可證 衛署藥製字第033582號 與品名不符 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 快速總覽「特必林錠、布乃可錠」 | 報告重生後已無此錯誤（2026-10-15：新報告未再出現「特必林錠」「布乃可錠」；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

