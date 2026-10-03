---
layout: default
title: Methylprednisolone
parent: 中證據等級 (L3-L4)
nav_order: 164
evidence_level: L3
indication_count: 10
---

# Methylprednisolone
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Methylprednisolone：從抗炎性皮質固醇到圓禿症

## 一句話總結

Methylprednisolone（甲基培尼皮質醇）是廣泛使用的合成糖皮質固醇，原本核准用於風濕性關節炎、氣喘、過敏性疾患等抗炎與免疫抑制治療。TxGNN 模型預測它可能對**圓禿症 (Alopecia Areata)** 有效，目前有 **1 個直接相關的 Phase 4 臨床試驗**及多項觀察性研究，加上 **20 篇文獻**（含多篇直接研究 methylprednisolone 脈衝療法用於圓禿症）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗炎性皮質固醇（風濕性關節炎、氣喘、過敏性疾患） |
| 預測新適應症 | 圓禿症 (Alopecia Areata) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 86 張（有效單方 33／有效複方 3／已註銷 50） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Methylprednisolone 是強效合成糖皮質固醇，透過與細胞內糖皮質固醇受體（GR）結合後，抑制 NF-κB 和 AP-1 等促炎轉錄因子，廣泛下調 IL-1、IL-6、TNF-α 等多種細胞激素，同時抑制 T 細胞活化與增殖。其抗炎效價約為 hydrocortisone 的 5 倍，可口服或靜脈給藥，適合需要快速系統性免疫抑制的急性病程。

圓禿症的核心病理為自體免疫性毛囊破壞：CD8⁺ NKG2D⁺ T 細胞失去對毛囊的「免疫豁免（follicular immune privilege）」，浸潤並攻擊生長期毛囊髮母細胞，導致毛囊微型化與非疤痕性脫髮。Methylprednisolone 的免疫抑制機轉直接針對這條病理路徑——透過抑制 T 細胞媒介的自體免疫浸潤，減少毛囊周圍的炎症環境，脈衝給藥（pulse therapy）可快速阻斷正在進行的活動性免疫攻擊，避免長期低劑量類固醇帶來的全身副作用。

目前文獻中已有多篇臨床研究直接評估 methylprednisolone 口服或靜脈脈衝療法治療廣泛型、難治型圓禿症，顯示此預測並非純粹的演算法推論，而是有臨床實踐基礎的老藥新用候選。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | 完成 | 42 | 直接研究口服大劑量脈衝 methylprednisolone 用於重度難治性圓禿症，探討更高劑量、更高頻率脈衝方案是否能改善全頭禿及全身禿的療效 |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | 觀察性 | 完成 | 296 | Tofacitinib（JAK 抑制劑，±輔助 prednisolone）用於圓禿症的真實世界安全性與療效評估 |
| [NCT03616964](https://clinicaltrials.gov/study/NCT03616964) | Phase 3 | 完成 | 778 | Baricitinib（JAK1/2 抑制劑）用於圓禿症疾病族群的雙盲安慰劑對照大型 RCT，代表同疾病領域最高等級試驗背景 |
| [NCT03845517](https://clinicaltrials.gov/study/NCT03845517) | Phase 2b | 完成 | 350 | PF-06700841（TYK2/JAK1 抑制劑）用於中重度活躍性圓禿症族群的雙盲隨機劑量探索研究 |
| [NCT05162586](https://clinicaltrials.gov/study/NCT05162586) | Phase 2 | 完成 | 456 | Enpatoran 用於圓禿症族群的隨機雙盲安慰劑對照劑量探索平行研究 |
| [NCT04680637](https://clinicaltrials.gov/study/NCT04680637) | Phase 2b | 終止 | 168 | Efavaleukin alfa（IL-2 路徑免疫調節劑）用於圓禿症族群的有效性與安全性研究 |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | 未知 | 20 | 比較 DERMOJET 與傳統注射針用於圓禿症局部類固醇（皮內注射）給藥方式的療效與便利性 |
| [NCT04582136](https://clinicaltrials.gov/study/NCT04582136) | Phase 3 | 進行中 | 146 | Sirolimus 加上背景類固醇治療活躍性自體免疫疾患的 Phase 3 雙盲 RCT，提供類固醇聯合免疫抑制劑的設計參考 |
| [NCT06046534](https://clinicaltrials.gov/study/NCT06046534) | N/A | 完成 | 46 | Anifrolumab 早期使用計畫的回顧性病歷審查，評估真實世界系統性免疫抑制治療的用藥型態與患者經驗 |
| [NCT06653556](https://clinicaltrials.gov/study/NCT06653556) | Early Phase 1 | 招募中 | 34 | LCAR-AIO 用於復發/難治性重度自體免疫疾患的開放標籤安全性、耐受性、PK/PD 探索研究 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Meta-analysis | Dermatology and Therapy | 系統性回顧 Cyclosporine ± 系統性皮質固醇治療圓禿症，評估不同組合方案的療效與安全性 |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohort | Dermatologic Therapy | 26 例廣泛型圓禿症回顧性分析：比較 methylprednisolone 單藥 vs. 合併 methotrexate 的療效 |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Cohort | Indian J Dermatol Venereol Leprol | 靜脈脈衝 methylprednisolone 用於重度圓禿症的臨床療效與安全性評估 |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Cohort | Indian J Dermatology | 回顧性研究：類固醇脈衝療法治療圓禿症的性別差異分析，評估復發與預後因子 |
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | Cohort | Open Access Macedonian J Med Sci | Methotrexate 合併 mini-pulse methylprednisolone 治療重度圓禿症（含全頭禿、全身禿）的越南臨床經驗 |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Cohort | Saudi Medical Journal | 口服大劑量脈衝 methylprednisolone 用於重度難治性圓禿症：強化療程方案的有效性系列評估 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | 皮質固醇脈衝療法治療圓禿症的療效、復發率、副作用及預後因子綜合文獻回顧 |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Case series | J Dermatological Treatment | Cyclosporine 合併 methylprednisolone 用於重度慢性圓禿症，兼顧療效與控制單藥復發率 |
| [28378336](https://pubmed.ncbi.nlm.nih.gov/28378336/) | 2017 | Review | Int J Dermatology | 全頭禿（AT）與全身禿（AU）治療選項系統性回顧，涵蓋脈衝糖皮質固醇療法的地位評估 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | 兒童圓禿症使用脈衝劑量皮質固醇療法（PDCT）的劑量方案、療效與副作用文獻彙整 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Methylprednisolone 的不重複許可證共 **86 張**：有效單方 33 張、有效複方 3 張、已註銷 50 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>有效・單方</strong>（33 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>劑型</th><th>申請商</th><th>有效日期</th><th>核准適應症</th></tr></thead><tbody><tr><td>衛署藥製字第026167號</td><td>欣普列錠４毫克（甲基培尼皮質醇）</td><td>錠劑</td><td>藥一藥業股份有限公司</td><td>2028/04/30</td><td>膠原病：慢性關節僂麻質斯、僂麻質熱、播種性紅斑性狼瘡、過敏性疾患：氣喘、血清病、蕁麻疹、血液疾患：紫斑病、白血病、急、慢性淋巴性白血病、腎性症候群之腎疾患、重症感染症（危急時）潰瘍…</td></tr><tr><td>衛署藥製字第029085號</td><td>命得生注射劑</td><td>乾粉注射劑</td><td>南光化學製藥股份有限公司</td><td>2028/08/06</td><td>腎上腺機能不全、劇烈休克、支氣管性氣喘、膠原疾病、過敏反應、泛發性感染</td></tr><tr><td>衛署藥製字第029465號</td><td>"成大"蒙治爽錠2毫克（甲基培尼皮質醇）</td><td>錠劑</td><td>成大藥品股份有限公司</td><td>2029/02/28</td><td>副腎皮腎機能不全、慢性風濕關節炎、多發性肌炎、支氣管氣喘、藥物化學品過敏性藥疹中毒疹、血清病、重症感染症、濕疹皮膚炎、癢疹、乾癬、潰瘍性大腸炎、重症消耗性疾患、血管運動性鼻炎</td></tr><tr><td>衛署藥製字第035835號</td><td>"華興"每得寧錠４公絲（甲基培尼皮質醇）</td><td>錠劑</td><td>華興化學製藥廠股份有限公司</td><td>2027/10/19</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第038766號</td><td>“永信”甲基普立朗錠４毫克（甲基培尼皮質醇）</td><td>錠劑</td><td>永信藥品工業股份有限公司</td><td>2030/04/21</td><td>風濕性熱、風濕樣關節炎及過敏性症狀</td></tr><tr><td>衛署藥製字第038955號</td><td>"成大"蒙治爽錠4毫克</td><td>錠劑</td><td>成大藥品股份有限公司</td><td>2030/06/15</td><td>風濕性熱、風濕樣關節炎及過敏性症狀</td></tr><tr><td>衛署藥製字第041020號</td><td>〝十全〞甲適寧錠２公絲(甲基培尼皮質醇)</td><td>錠劑</td><td>十全實業股份有限公司</td><td>2027/04/07</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第041358號</td><td>"國嘉"美得寧錠４毫克（甲基培尼皮質醇）</td><td>錠劑</td><td>國嘉製藥工業股份有限公司幼獅三廠</td><td>2029/03/28</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第041918號</td><td>"培力" 美尼松錠４公絲（甲基培尼皮質醇）</td><td>錠劑</td><td>培力藥品工業股份有限公司</td><td>2028/02/12</td><td>風濕性熱、風濕樣關節炎及過敏性症狀</td></tr><tr><td>衛署藥製字第043474號</td><td>美舒朗錠16毫克</td><td>錠劑</td><td>鎰浩貿易股份有限公司</td><td>2030/01/19</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第043726號</td><td>"政德" 美普隆乾粉注射劑</td><td>乾粉注射劑</td><td>政德製藥股份有限公司</td><td>2030/05/05</td><td>腎上腺皮質機能不全、劇烈休克、支氣管性氣喘、膠原疾病、過敏反應、泛發性感染。</td></tr><tr><td>衛署藥製字第043727號</td><td>”華興”每得寧錠２公絲 (甲基培尼皮質醇)</td><td>錠劑</td><td>華興化學製藥廠股份有限公司</td><td>2030/05/05</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第043761號</td><td>敏疫朗錠4毫克(甲基培尼皮質醇）</td><td>錠劑</td><td>華樺生技藥品股份有限公司</td><td>2030/05/22</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第043939號</td><td>美利錠</td><td>錠劑</td><td>壽元化學工業股份有限公司</td><td>2030/08/31</td><td>副腎皮質機能不全、慢性風濕關節炎、多發性肌炎、支氣管氣喘、藥物化學品過敏性藥疹中毒疹、血清病、重症感染症、濕疹、皮膚炎、癢疹、乾癬、潰瘍性大腸炎、重症消耗性疾患、血管運動性鼻炎。</td></tr><tr><td>衛署藥製字第045677號</td><td>美蒂舒錠２毫克 (甲基培尼皮質醇)</td><td>錠劑</td><td>健喬信元醫藥生技股份有限公司</td><td>2028/07/22</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第045923號</td><td>美蒂舒錠４毫克(甲基培尼皮質醇)</td><td>錠劑</td><td>健喬信元醫藥生技股份有限公司</td><td>2028/11/10</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第046461號</td><td>"元宙" 美爽蒙錠</td><td>錠劑</td><td>元宙化學製藥股份有限公司</td><td>2029/08/18</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第046697號</td><td>"台裕" 欣敏錠4公絲</td><td>錠劑</td><td>台裕化學製藥廠股份有限公司</td><td>2029/12/13</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第046938號</td><td>"培力" 美尼松錠 2 公絲</td><td>錠劑</td><td>培力藥品工業股份有限公司</td><td>2030/01/20</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第047772號</td><td>"元宙" 蓓妮錠</td><td>錠劑</td><td>元宙化學製藥股份有限公司</td><td>2031/01/23</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第048169號</td><td>"安星" 立可隆錠4毫克</td><td>錠劑</td><td>安星製藥股份有限公司</td><td>2031/08/16</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第048267號</td><td>"永信" 甲基普立朗 注射劑40毫克</td><td>乾粉注射劑</td><td>永信藥品工業股份有限公司</td><td>2031/09/25</td><td>腎上腺皮質機能不全，劇烈 休克、支氣管性氣喘、膠原疾病、過敏反應、泛發性感染。</td></tr><tr><td>衛署藥製字第048272號</td><td>"元宙" 美禾錠</td><td>錠劑</td><td>元宙化學製藥股份有限公司</td><td>2031/09/27</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥製字第055920號</td><td>“永勝”百利朗膜衣錠 8 毫克</td><td>膜衣錠</td><td>永勝藥品工業股份有限公司</td><td>2031/01/14</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛署藥輸字第024384號</td><td>甲基培尼皮質醇</td><td>（粉）</td><td>川聖貿易股份有限公司</td><td>2031/02/20</td><td>抗炎性皮質固醇。</td></tr><tr><td>衛署藥輸字第024635號</td><td>琥珀酸鈉去氧氫化可體松粉劑</td><td>（粉）</td><td>宇直泰貿易股份有限公司</td><td>2027/05/02</td><td>副腎皮質荷爾蒙劑。</td></tr><tr><td>衛署藥陸輸字第000506號</td><td>甲基培尼皮質醇</td><td>（粉）</td><td>川聖貿易股份有限公司</td><td>2027/03/13</td><td>抗炎性皮質固醇。</td></tr><tr><td>衛署藥陸輸字第000559號</td><td>甲基培尼皮質醇</td><td>（粉）</td><td>台灣荃新股份有限公司</td><td>2028/03/04</td><td>抗炎性皮質固醇</td></tr><tr><td>衛部藥製字第058821號</td><td>"嘉林"美力錠4毫克</td><td>錠劑</td><td>嘉林藥品有限公司</td><td>2030/09/01</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛部藥製字第060828號</td><td>"元宙"美炎錠</td><td>錠劑</td><td>元宙化學製藥股份有限公司</td><td>2026/02/23</td><td>風濕性熱、風濕樣關節炎及過敏性症狀。</td></tr><tr><td>衛部藥輸字第027141號</td><td>甲基培尼皮質醇</td><td>原料藥粉末</td><td>宣泓貿易有限公司</td><td>2027/05/01</td><td>抗炎性皮質固醇</td></tr><tr><td>衛部藥陸輸字第000619號</td><td>甲基培尼皮質醇</td><td>（粉）</td><td>宣泓貿易有限公司</td><td>2028/07/24</td><td>抗炎性皮質固醇</td></tr><tr><td>衛部藥陸輸字第000824號</td><td>甲基培尼皮質醇</td><td>（粉）</td><td>菩鏹股份有限公司</td><td>2028/03/06</td><td>抗炎性皮質固醇</td></tr></tbody></table></details>

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（3 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第045443號 | "東洲" 美樂乾粉注射劑 | METHYLPREDNISOLONE、METHYLPREDNISOLONE | 乾粉注射劑 | 腎上腺皮質機能不全、劇烈休克、支氣管性氣喘、膠原疾病、過敏反應、泛發性感染。 |
| 衛署藥製字第047537號 | 敏克素注射劑 | METHYLPREDNISOLONE、METHYLPREDNISOLONE | 乾粉注射劑 | 腎上腺機能不全，劇烈休克，支氣管性氣喘，膠原疾病，過敏反應，泛發性感染。 |
| 衛署藥輸字第004248號 | 舒汝美卓佑滅菌注射粉劑４０毫克 | METHYLPREDNISOLONE、METHYLPREDNISOLONE、METHYLPREDNISOLONE 21-… | 凍晶注射劑 | 腎上腺皮質機能不全、劇烈休克、支氣管性氣喘、膠原疾病、過敏反應、泛發性感染 |

<details><summary><strong>已註銷</strong>（50 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第003391號</td><td>歐巴生針劑４０公絲</td><td>METHYLPREDNISOLONE 6-ALPHA HEMISSUCCINATE (SODIUM)</td><td>1986/01/08</td></tr><tr><td>內衛藥輸字第003631號</td><td>歐巴生結晶性懸濁液注射劑</td><td>METHYLPREDNISOLONE 21-ACETATE</td><td>1985/12/31</td></tr><tr><td>內衛藥輸字第003634號</td><td>歐巴生錠劑</td><td>METHYLPREDNISOLONE</td><td>1985/12/31</td></tr><tr><td>衛署藥製字第022268號</td><td>免多敏凍晶注射劑</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第022610號</td><td>免多敏凍晶注射劑５００公絲</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第024284號</td><td>延效美卓爾添加利度卡因注射液</td><td>METHYLPREDNISOLONE 21-ACETATE、LIDOCAINE HCL</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第024321號</td><td>延效美卓爾注射液４０公絲/公撮（乙酸甲基培尼皮質醇）</td><td>METHYLPREDNISOLONE 21-ACETATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第029084號</td><td>命得生注射劑５００公絲（甲基培尼皮質醇）</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>1998/04/23</td></tr><tr><td>衛署藥製字第037380號</td><td>美得寧錠４公絲（甲基培尼皮質醇）</td><td>METHYLPREDNISOLONE</td><td>1997/10/02</td></tr><tr><td>衛署藥製字第039045號</td><td>"富生"百寧炎錠４毫克（甲基培尼皮質醇）</td><td>METHYLPREDNISOLONE</td><td>2023/07/17</td></tr><tr><td>衛署藥製字第040906號</td><td>普雷錠４公絲（甲基培尼皮質醇）</td><td>METHYLPREDNISOLONE</td><td>2020/10/05</td></tr><tr><td>衛署藥製字第042577號</td><td>敏倍爽錠８公絲（甲基培尼皮質醇）〝新豐〞</td><td>METHYLPREDNISOLONE</td><td>2013/10/16</td></tr><tr><td>衛署藥製字第043052號</td><td>"嘉林" 美力錠４毫克</td><td>METHYLPREDNISOLONE</td><td>2015/11/18</td></tr><tr><td>衛署藥輸字第000999號</td><td>琥珀酸鈉甲基乙醯去氫羥化腎上腺皮質素</td><td>METHYLPREDNISOLONE 21-SODIUM SUCCINATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002746號</td><td>磷酸鈉甲基乙醯去氫羥化腎上腺皮質素</td><td>METHYLPREDNISOLONE 21-SODIUM PHOSPHATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004249號</td><td>舒汝美卓佑滅菌注射粉劑１２５毫克</td><td>METHYLPREDNISOLONE、METHYLPREDNISOLONE、METHYLPREDNISOLONE 21-…</td><td>2019/03/22</td></tr><tr><td>衛署藥輸字第008210號</td><td>佳美得寧懸濁注射液８０公絲</td><td>METHYLPREDNISOLONE 21-ACETATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第012097號</td><td>甲基培尼皮質醇粉劑</td><td>METHYLPREDNISOLONE 6-ALPHA</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第012239號</td><td>甲基普利得尼梭隆粉劑</td><td>METHYLPREDNISOLONE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第013064號</td><td>甲基去氧氫化可體松粉劑</td><td>METHYLPREDNISOLONE</td><td>2014/01/24</td></tr><tr><td>衛署藥輸字第013302號</td><td>琥珀酸鈉去氧氫化可體松粉劑</td><td>METHYLPREDNISOLONE 21-SODIUM SUCCINATE</td><td>2014/01/24</td></tr><tr><td>衛署藥輸字第013373號</td><td>乙醯甲基去氧氫化可體松粉劑</td><td>METHYLPREDNISOLONE 21-ACETATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第014532號</td><td>歐巴生針劑４０公絲</td><td>METHYLPREDNISOLONE 6-ALPHA HEMISSUCCINATE (SODIUM)</td><td>1987/03/21</td></tr><tr><td>衛署藥輸字第014533號</td><td>歐巴生結晶性懸濁液注射劑</td><td>METHYLPREDNISOLONE 21-ACETATE</td><td>1987/03/21</td></tr><tr><td>衛署藥輸字第014534號</td><td>歐巴生錠</td><td>METHYLPREDNISOLONE</td><td>1987/04/20</td></tr><tr><td>衛署藥輸字第015172號</td><td>敏得適凍晶注射劑１２５公絲</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015414號</td><td>甲基培尼皮質醇</td><td>METHYLPREDNISOLONE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第015676號</td><td>歐巴生結晶性懸濁液注射劑</td><td>METHYLPREDNISOLONE 21-ACETATE</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015678號</td><td>歐巴生注射劑４０公絲</td><td>METHYLPREDNISOLONE 6-ALPHA HEMISSUCCINATE (SODIUM)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015679號</td><td>歐巴生注射劑２０公絲</td><td>METHYLPREDNISOLONE 6-ALPHA HEMISSUCCINATE (SODIUM)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015733號</td><td>歐巴生錠</td><td>METHYLPREDNISOLONE</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第015835號</td><td>歐巴生乾粉靜脈注射劑１０００公絲</td><td>METHYLPREDNISOLONE 6-ALPHA HEMISSUCCINATE (SODIUM)</td><td>1997/06/18</td></tr><tr><td>衛署藥輸字第016016號</td><td>歐巴生乾粉注射劑２５０公絲</td><td>METHYLPREDNISOLONE 6-ALPHA HEMISSUCCINATE (SODIUM)</td><td>2000/09/20</td></tr><tr><td>衛署藥輸字第016425號</td><td>甲基培尼皮質醇半琥珀酸醯</td><td>METHYLPREDNISOLONE 21- HEMISUCCINATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第018415號</td><td>美卓佑錠１００公絲</td><td>METHYLPREDNISOLONE</td><td>2010/08/24</td></tr><tr><td>衛署藥輸字第019571號</td><td>美腺龍凍晶注射劑</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>1998/08/03</td></tr><tr><td>衛署藥輸字第020029號</td><td>亥彌寇特４０公絲</td><td>METHYLPREDNISOLONE</td><td>1997/08/13</td></tr><tr><td>衛署藥輸字第020030號</td><td>亥彌寇特注射劑１２５公絲</td><td>METHYLPREDNISOLONE</td><td>1997/08/13</td></tr><tr><td>衛署藥輸字第020031號</td><td>亥彌寇特注射劑２公克</td><td>METHYLPREDNISOLONE</td><td>1997/08/13</td></tr><tr><td>衛署藥輸字第020417號</td><td>舒汝美卓佑乾粉注射劑</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>2013/10/08</td></tr><tr><td>衛署藥輸字第020850號</td><td>延效美卓爾懸浮注射劑</td><td>METHYLPREDNISOLONE 21-ACETATE</td><td>2014/08/11</td></tr><tr><td>衛署藥輸字第020918號</td><td>延效美卓爾添加利度卡因懸浮注射劑</td><td>LIDOCAINE HCL、METHYLPREDNISOLONE 21-ACETATE</td><td>2014/08/11</td></tr><tr><td>衛署藥輸字第021572號</td><td>歐巴生乾粉靜脈注射劑１０００公絲</td><td>METHYLPREDNISOLONE 6-ALPHA HEMISSUCCINATE (SODIUM)</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第021799號</td><td>亥彌寇特注射劑１２５公絲</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>2004/12/16</td></tr><tr><td>衛署藥輸字第022134號</td><td>美腺龍凍晶注射劑</td><td>METHYLPREDNISOLONE (SODIUM SUCCINATE)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第023387號</td><td>培尼皮質醇</td><td>METHYLPREDNISOLONE</td><td>2023/06/06</td></tr><tr><td>衛署藥輸字第023822號</td><td>"新微科技" 甲基培尼皮質醇</td><td>METHYLPREDNISOLONE</td><td>2006/09/25</td></tr><tr><td>衛署藥陸輸字第000117號</td><td>甲基培尼皮質醇</td><td>METHYLPREDNISOLONE</td><td>2016/05/30</td></tr><tr><td>衛署藥陸輸字第000466號</td><td>甲基培尼皮質醇</td><td>Methylprednisolone</td><td>2019/03/12</td></tr><tr><td>衛部藥輸字第027124號</td><td>甲基培尼皮質醇琥珀酸鈉</td><td>Methylprednisolone sodium succinate</td><td>2024/09/27</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

**藥物交互作用（資料庫共 688 筆，以下列出代表性項目）：**

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Bupropion | **Major** | 合用可能降低癲癇發作閾值，需高度警惕 |
| Clarithromycin | **Major** | CYP3A4 強效抑制劑，可顯著提升 methylprednisolone 血中濃度 |
| Metformin | Moderate | 皮質固醇可拮抗降血糖效果，合用需監測血糖 |
| Acarbose | Moderate | 同上，需監測血糖控制 |
| Pioglitazone | Moderate | 同上，需監測血糖控制 |
| Canagliflozin / Dapagliflozin / Empagliflozin | Moderate | 皮質固醇可降低 SGLT2 抑制劑療效，需加強監測 |
| Amphotericin B | Moderate | 合用增加低鉀血症風險，需監測電解質 |
| Acetylsalicylic acid | Moderate | 合用可能增加消化道潰瘍及出血風險 |

> 完整 688 筆 DDI 清單請查閱 DDInter 資料庫。主要警語、禁忌症及用藥監測詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Methylprednisolone 脈衝療法治療圓禿症已有多項臨床觀察性研究、1 個已完成的 Phase 4 直接試驗（NCT01167946）及 1 篇 meta-analysis 支持，藥物免疫抑制機轉與圓禿症的自體免疫發病路徑高度吻合，生物學合理性充分；加上台灣現有多種劑型（口服錠劑、注射劑）上市，可及性高。

**若要推進需要：**
- 補充 DrugBank MOA 詳細資料（目前為資料缺口），以強化機轉關聯性分析
- 訂定標準化脈衝給藥方案（oral mega-pulse vs. IV pulse：劑量、頻率、療程週數）
- 規劃亞洲族群（含台灣患者）的安全性監測計畫，重點關注：血糖上升、骨質疏鬆、感染風險及腎上腺抑制
- 設計前瞻性觀察研究或隨機對照試驗，以填補 Phase 2/3 RCT 層級的關鍵證據缺口
- 若目標為取得台灣核准適應症，需準備完整有效性與安全性資料，依藥品查驗登記流程提交衛福部審查
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

