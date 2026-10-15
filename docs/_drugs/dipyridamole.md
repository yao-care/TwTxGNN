---
layout: default
title: Dipyridamole
parent: 中證據等級 (L3-L4)
nav_order: 87
evidence_level: L4
indication_count: 10
---

# Dipyridamole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Dipyridamole：從慢性狹心症到 Prinzmetal 狹心症

## 一句話總結

Dipyridamole（雙嘧達莫，台灣商品名如「百心康」）原本用於慢性狹心症與冠狀動脈不全的治療，也用於取代心肌造影時的運動試驗。
TxGNN 模型預測排名第一的新適應症是 **Prinzmetal 狹心症 (Prinzmetal angina)**，但目前**沒有相關臨床試驗**，僅有 **10 篇文獻**，且多為診斷用途或個案報告，證據偏弱。
同一份預測清單中，**中風 (stroke disorder)** 與**短暫性腦缺血 (TIA)** 的證據明顯較強（有大型 RCT 與統合分析），詳見下方補充說明。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 取代心肌造影時所需之運動試驗（另有慢性狹心症之治療、血小板集結降低藥等適應症） |
| 預測新適應症 | Prinzmetal 狹心症 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 166 張（有效單方 56／有效複方 0／已註銷 110） |
| 建議決策 | Hold |

---

<!-- review:begin dipyridamole-moa-2026-10-03 -->

## Dipyridamole 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Dipyridamole 會抑制血小板、血管內皮細胞與紅血球回收 adenosine，使局部 adenosine 濃度升高。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a18b2af5-7c4a-4b7f-92c7-8a76e34da373)）
- 升高的 adenosine 作用在血小板的 A2 受體，活化 adenylate cyclase、提高血小板內的 cAMP，因而抑制 PAF、膠原、ADP 等刺激引起的血小板凝集。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a18b2af5-7c4a-4b7f-92c7-8a76e34da373)）
- 它也抑制多種組織的磷酸二酯酶（PDE）：對 cAMP-PDE 的抑制很弱，但在治療濃度下會抑制 cGMP-PDE，加強一氧化氮（EDRF）帶來的 cGMP 上升。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a18b2af5-7c4a-4b7f-92c7-8a76e34da373)）
- 狗的試驗中，dipyridamole 會依劑量降低全身與冠狀動脈的血管阻力，使血壓下降、冠狀動脈血流增加。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a18b2af5-7c4a-4b7f-92c7-8a76e34da373)）

**來源**：[DailyMed：Dipyridamole Tablets, USP 仿單（Amneal Pharmaceuticals of New York），Clinical Pharmacology／Mechanism of Action 段](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a18b2af5-7c4a-4b7f-92c7-8a76e34da373)，版本日期 2026-04-15；查閱日期 2026-10-03。

---

<!-- review:end dipyridamole-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏來自 DrugBank 的詳細作用機轉資料。就文獻所述，Dipyridamole 會抑制腺苷（adenosine）再攝取並抑制磷酸二酯酶（PDE），使血小板與血管平滑肌內的 cAMP/cGMP 上升，產生冠狀動脈擴張與抗血小板作用。

Prinzmetal 狹心症（變異型狹心症）由冠狀動脈痙攣引起，與原適應症同屬冠心症範疇。不過，Dipyridamole 在血管痙攣型狹心症中主要用於**診斷性的負荷影像檢查**，治療效益尚未證實。1988 年的一份報告（PMID 3421166）甚至指出，Dipyridamole 負荷試驗後以 aminophylline 終止，可能誘發變異型狹心症患者的冠狀動脈痙攣。此外，血管擴張也可能引起冠狀動脈「竊血」現象。因此，這個預測在機轉上有合理之處，但同時存在明確的安全疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記（針對 Prinzmetal 狹心症）。

> **補充：** 預測清單中的其他適應症有較多試驗，列於此供參考。

**中風 (stroke disorder)，TxGNN 分數 99.95%：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | 完成 | 4500 | ESPRIT：比較 aspirin 加 dipyridamole 與單用 aspirin 於腦缺血後的療效與安全性 |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | 完成 | 551 | EARLY：急性缺血性中風 24 小時內開始 Aggrenox 與先用 aspirin 7 天後再用 Aggrenox 的比較 |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Phase 3 | 完成 | 250 | 頸動脈剝離中風：抗血小板與抗凝血治療的可行性研究（Dipyridamole 僅為可選藥物之一） |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | 完成 | 664 | 卵圓孔未閉：關閉術、抗凝血與抗血小板預防中風復發（Dipyridamole 非主要測試藥物） |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N/A | 完成 | 664 | Gore REDUCE：卵圓孔未閉關閉術加抗血小板治療 vs. 單用抗血小板治療 |
| [NCT06053021](https://clinicaltrials.gov/study/NCT06053021) | N/A | 未知 | 1200 | 急性缺血性中風合併血小板低下的抗血小板治療 |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | 完成 | 240 | 頸動脈血管重建後的氧化壓力與抗血栓治療效果（僅支持機轉） |
| [NCT06983795](https://clinicaltrials.gov/study/NCT06983795) | N/A | 尚未招募 | 1000 | 亞太地區卵圓孔未閉合併缺血性中風的登錄研究 |

**短暫性腦缺血 (TIA)：** 另有 NCT00161070（ESPRIT）與 NCT00738894 支持。

---

## 文獻證據

**Prinzmetal 狹心症（排名第 1）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review | Jpn Circ J | 26 位靜息型狹心症患者（含 13 位變異型）測試多種藥物，其中包含 dipyridamole 50 mg |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Case series | Am J Cardiol | Dipyridamole 負荷試驗後以 aminophylline 終止，可能誘發變異型狹心症的冠狀動脈痙攣 |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Cohort | Br Heart J | ST 段上升患者對 dipyridamole 試驗的不同反應與運動試驗再現性 |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Cohort | J Am Coll Cardiol | 不同機轉誘發的缺血中，心肌回音密度增加的超音波徵象 |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Cohort | Jpn Circ J | Dipyridamole 負荷鉈-201 心肌造影對冠心症的診斷準確度為 66%；合併運動負荷可提高敏感度至 87% |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | 冠狀動脈狹窄非侵入性功能評估的病理生理基礎 |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Case series | Zhonghua Xin Xue Guan Bing Za Zhi | 非典型冠狀動脈痙攣患者的臨床特徵 |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Cohort | Rev Port Cardiol | 鉈-dipyridamole 心肌掃描正常者的 3 年預後 |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Review | Clin Nucl Med | 「心臟型偏頭痛」是否為獨立臨床實體的個案討論 |

以上文獻多為診斷性使用或個案報告，並**無**證明 Dipyridamole 能治療 Prinzmetal 狹心症的對照試驗。

**中風／TIA 的高階證據（補充）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis | Stroke | 以個別病人資料整合 RCT，評估 dipyridamole 預防缺血性中風復發 |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Meta-analysis | Cochrane Database Syst Rev | 單一試驗中加入 dipyridamole 使風險再降 22%；但整體抗血小板試驗彙整顯示 aspirin 合併 dipyridamole 與其他抗血小板藥差異不大 |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Meta-analysis | J Neurol Sci | aspirin 加 dipyridamole 與單用 aspirin 於 TIA／中風二級預防的 RCT 統合分析 |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | 高風險患者抗血小板治療預防死亡、心肌梗塞與中風的合作統合分析 |
| [31177983](https://pubmed.ncbi.nlm.nih.gov/31177983/) | 2019 | Meta-analysis | Stroke | 非心因性栓塞中風後抗血小板藥物的網絡統合分析（6 個 RCT） |
| [34211246](https://pubmed.ncbi.nlm.nih.gov/34211246/) | 2021 | Review | Aust Prescr | aspirin、clopidogrel 或 aspirin 加 dipyridamole 為無心房顫動者二級預防的第一線選項 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dipyridamole 的不重複許可證共 **166 張**：有效單方 56 張、有效複方 0 張、已註銷 110 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>有效・單方</strong>（56 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>劑型</th><th>申請商</th><th>有效日期</th><th>核准適應症</th></tr></thead><tbody><tr><td>內衛藥製字第006489號</td><td>保心丁注射液</td><td>注射劑</td><td>南光化學製藥股份有限公司</td><td>2028/07/25</td><td>取代心肌造影時所需之運動試驗。</td></tr><tr><td>內衛藥製字第015343號</td><td>心妙健注射液</td><td>注射劑</td><td>應元化學製藥股份有限公司</td><td>2028/05/25</td><td>取代心肌造影時所需之運動試驗</td></tr><tr><td>衛署藥製字第001941號</td><td>"優生"滋心膜衣錠</td><td>膜衣錠</td><td>優生製藥廠股份有限公司</td><td>2029/10/04</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第005200號</td><td>平心糖衣錠２５公絲</td><td>糖衣錠</td><td>強生化學製藥廠股份有限公司</td><td>2029/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第006394號</td><td>沛心寧膜衣錠25毫克</td><td>膜衣錠</td><td>健喬信元醫藥生技股份有限公司</td><td>2029/05/25</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第008380號</td><td>"利達"倍利心糖衣錠</td><td>糖衣錠</td><td>利達製藥股份有限公司</td><td>2028/12/09</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第009983號</td><td>"豐田"即安心糖衣錠</td><td>糖衣錠</td><td>豐田藥品股份有限公司</td><td>2027/08/20</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第010802號</td><td>碧克多寧糖衣錠２５毫克</td><td>糖衣錠</td><td>福元化學製藥股份有限公司</td><td>2024/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第013634號</td><td>"永信"待匹力達糖衣錠</td><td>糖衣錠</td><td>永信藥品工業股份有限公司</td><td>2029/10/26</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第013801號</td><td>"生達" 待匹力達糖衣錠</td><td>糖衣錠</td><td>生達化學製藥股份有限公司</td><td>2029/11/11</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第014256號</td><td>待匹力達糖衣錠</td><td>糖衣錠</td><td>信東生技股份有限公司</td><td>2029/02/01</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第014261號</td><td>待匹力達注射液</td><td>注射劑</td><td>信東生技股份有限公司</td><td>2030/02/01</td><td>取代心肌造影時所需之運動試驗</td></tr><tr><td>衛署藥製字第017350號</td><td>"生達"待匹力達注射液</td><td>注射劑</td><td>生達化學製藥股份有限公司</td><td>2029/04/28</td><td>取代心肌造影時所需之運動試驗。</td></tr><tr><td>衛署藥製字第017737號</td><td>"優良"優心寧錠（待匹力達）</td><td>錠劑</td><td>優良化學製藥股份有限公司</td><td>2029/06/05</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第019138號</td><td>"信隆"待匹力達糖衣錠</td><td>糖衣錠</td><td>信隆藥品工業股份有限公司</td><td>2029/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第019627號</td><td>培心寧膜衣錠（二吡待摩）</td><td>膜衣錠</td><td>皇佳化學製藥股份有限公司</td><td>2024/12/04</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第019895號</td><td>"榮民"心康寧糖衣錠25毫克(待匹力達)</td><td>糖衣錠</td><td>榮民製藥股份有限公司</td><td>2029/12/21</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第021400號</td><td>心肌正糖衣錠</td><td>糖衣錠</td><td>約克製藥股份有限公司</td><td>2028/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第021566號</td><td>彼達猛糖衣錠25毫克（待匹力達）</td><td>糖衣錠</td><td>衛肯生技製藥股份有限公司</td><td>2028/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第021711號</td><td>普多心定糖衣錠（待匹力達）</td><td>糖衣錠</td><td>中美兄弟製藥股份有限公司</td><td>2029/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第022723號</td><td>舒必緩錠（待匹力達）</td><td>錠劑</td><td>台裕化學製藥廠股份有限公司</td><td>2030/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第023321號</td><td>彼達猛糖衣錠１２．５毫克（待匹力達）</td><td>糖衣錠</td><td>衛肯生技製藥股份有限公司</td><td>2028/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第023644號</td><td>"元宙"弘心寧錠（待匹力達）</td><td>錠劑</td><td>元宙化學製藥股份有限公司</td><td>2024/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第024772號</td><td>"東洲"維心定注射液５公絲/公撮（待匹力達）</td><td>注射劑</td><td>東洲化學製藥廠股份有限公司</td><td>2029/12/31</td><td>取代心肌造影時所需之運動試驗。</td></tr><tr><td>衛署藥製字第025272號</td><td>"正和"得利達蒙糖衣錠２５公絲（待匹力達）</td><td>糖衣錠</td><td>正和製藥股份有限公司新營廠</td><td>2029/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第025406號</td><td>"正和"保爾心膜衣錠７５公絲</td><td>膜衣錠</td><td>正和製藥股份有限公司新營廠</td><td>2028/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第025431號</td><td>"東洲"奧力舒心糖衣錠７５公絲（待匹力達）</td><td>糖衣錠</td><td>東洲化學製藥廠股份有限公司</td><td>2028/12/31</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第025686號</td><td>"華興"博心寧膜衣錠25毫克</td><td>膜衣錠</td><td>華興化學製藥廠股份有限公司</td><td>2029/12/31</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第025851號</td><td>"聯邦"優利心糖衣錠２５公絲（待匹力達）</td><td>糖衣錠</td><td>聯邦化學製藥股份有限公司</td><td>2024/05/25</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第026770號</td><td>血栓淨糖衣錠25毫克(待匹力達)</td><td>糖衣錠</td><td>華樺生技藥品股份有限公司</td><td>2029/12/31</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第027445號</td><td>“衛達”心滴舒糖衣錠５０毫克（待匹力達）</td><td>糖衣錠</td><td>衛達化學製藥股份有限公司</td><td>2029/10/17</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第028592號</td><td>"優生"維諾心膜衣錠75毫克（待匹力達）</td><td>膜衣錠</td><td>優生製藥廠股份有限公司</td><td>2028/04/21</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第031228號</td><td>惠心糖衣錠５０毫克”國嘉”　　　　　　　　　　　　　　　　　 E</td><td>糖衣錠</td><td>國嘉製藥工業股份有限公司幼獅三廠</td><td>2029/01/20</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第031323號</td><td>心耐膜衣錠75公絲（二比待摩）</td><td>膜衣錠</td><td>中國化學製藥股份有限公司新豐工廠</td><td>2029/03/27</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第032046號</td><td>"永信"待匹力達糖衣錠７５公絲</td><td>糖衣錠</td><td>永信藥品工業股份有限公司</td><td>2030/01/04</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第032530號</td><td>心耐糖衣錠25公絲（二比待摩）</td><td>糖衣錠</td><td>中國化學製藥股份有限公司新豐工廠</td><td>2028/12/06</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第034584號</td><td>"羅得"怡心膜衣錠２５公絲（待匹力達）</td><td>膜衣錠</td><td>羅得化學製藥股份有限公司</td><td>2026/11/19</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第037644號</td><td>惠心糖衣錠25毫克 "國嘉"</td><td>糖衣錠</td><td>國嘉製藥工業股份有限公司幼獅三廠</td><td>2029/05/31</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第038495號</td><td>"生達" 待匹力達膜衣錠７５公絲</td><td>膜衣錠</td><td>生達化學製藥股份有限公司</td><td>2030/01/17</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第039042號</td><td>"永勝"心脈順糖衣錠２５毫克</td><td>糖衣錠</td><td>永勝藥品工業股份有限公司</td><td>2030/07/14</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第040976號</td><td>〝應元〞利冠心糖衣錠２５毫克（待匹力達）</td><td>糖衣錠</td><td>應元化學製藥股份有限公司</td><td>2027/03/21</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第041548號</td><td>"瑞安 " 立達脈膜衣錠２５毫克（二吡待摩）</td><td>膜衣錠</td><td>瑞安大藥廠股份有限公司</td><td>2027/09/10</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第041550號</td><td>"瑞安" 立達脈膜衣錠75毫克（二吡待摩）</td><td>膜衣錠</td><td>瑞安大藥廠股份有限公司</td><td>2027/09/10</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第041877號</td><td>普心寧膜衣錠７５公絲（二吡待摩）</td><td>膜衣錠</td><td>世達藥品工業股份有限公司</td><td>2028/01/23</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第041898號</td><td>“新喜”倍心進糖衣錠２５公絲</td><td>糖衣錠</td><td>新喜國際企業股份有限公司</td><td>2028/12/31</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第042535號</td><td>"十全" 暢心膜衣錠５０毫克（二吡待摩）</td><td>膜衣錠</td><td>十全實業股份有限公司</td><td>2028/08/20</td><td>對於慢性狹心症之治療可能有效</td></tr><tr><td>衛署藥製字第043040號</td><td>"十全"沛暢膜衣錠７５公絲（二吡待摩）</td><td>膜衣錠</td><td>十全實業股份有限公司</td><td>2029/06/23</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第043630號</td><td>勇心膜衣錠７５錠</td><td>膜衣錠</td><td>井田國際醫藥廠股份有限公司</td><td>2030/04/01</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第045312號</td><td>"十全" 力心達膜衣錠</td><td>膜衣錠</td><td>十全實業股份有限公司</td><td>2028/01/15</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥製字第057891號</td><td>所雷帝糖衣錠25毫克</td><td>糖衣錠</td><td>中化裕民健康事業股份有限公司</td><td>2028/04/11</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥輸字第023385號</td><td>備鎮心注射液</td><td>注射劑</td><td>裕利股份有限公司</td><td>2027/02/19</td><td>取代心肌造影時所需之運動試驗。</td></tr><tr><td>衛署藥輸字第025628號</td><td>備鎮心®糖衣錠75毫克 (法國廠)</td><td>錠劑</td><td>裕利股份有限公司</td><td>2027/02/20</td><td>對於慢性狹心症之治療可能有效。</td></tr><tr><td>衛署藥陸輸字第000426號</td><td>二吡待摩</td><td>（粉）</td><td>誠品貿易股份有限公司</td><td>2031/03/21</td><td>血小板集結降低藥</td></tr><tr><td>衛部藥輸字第027759號</td><td>二吡待摩</td><td>原料藥結晶性粉末</td><td>宇直泰貿易股份有限公司</td><td>2029/11/12</td><td>血小板集結降低藥</td></tr><tr><td>衛部藥陸輸字第000951號</td><td>二吡待摩</td><td>（粉）</td><td>台灣荃新股份有限公司</td><td>2030/08/25</td><td>血小板集結降低藥。</td></tr><tr><td>衛部藥陸輸字第001036號</td><td>二吡待摩</td><td>（粉）</td><td>漢旭股份有限公司</td><td>2027/01/10</td><td>血小板集結降低藥</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（110 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000163號</td><td>平心糖衣錠１２．５公絲</td><td>DIPYRIDAMOLE</td><td>2010/03/05</td></tr><tr><td>內衛藥製字第001036號</td><td>博心定糖衣片</td><td>DIPYRIDAMOLE</td><td>2014/09/04</td></tr><tr><td>內衛藥製字第004907號</td><td>心治寧注射液</td><td>DIPYRIDAMOLE</td><td>2009/12/30</td></tr><tr><td>內衛藥製字第008511號</td><td>保心糖衣錠</td><td>DIPYRIDAMOLE</td><td>1999/07/30</td></tr><tr><td>內衛藥製字第011074號</td><td>"人生"維心寧糖衣錠12.5毫克</td><td>DIPYRIDAMOLE</td><td>2026/08/17</td></tr><tr><td>內衛藥製字第013361號</td><td>培心正糖衣錠</td><td>DIPYRIDAMOLE</td><td>2013/07/11</td></tr><tr><td>內衛藥製字第014866號</td><td>爽爾心錠</td><td>DIPYRIDAMOLE</td><td>1998/03/16</td></tr><tr><td>內衛藥輸字第002575號</td><td>百心康</td><td>DIPYRIDAMOLE</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第008013號</td><td>百心康</td><td>DIPYRIDAMOLE</td><td>2000/10/20</td></tr><tr><td>衛署藥製字第003853號</td><td>心治寧錠</td><td>DIPYRIDAMOLE</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第004063號</td><td>永舒心平糖衣錠</td><td>DIPYRIDAMOLE</td><td>2016/09/19</td></tr><tr><td>衛署藥製字第004780號</td><td>扶爾心糖衣錠</td><td>DIPYRIDAMOLE</td><td>1991/05/27</td></tr><tr><td>衛署藥製字第005414號</td><td>隱心寧糖衣錠１２．５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2023/07/17</td></tr><tr><td>衛署藥製字第007799號</td><td>心修注射劑</td><td>DIPYRIDAMOLE</td><td>2013/04/08</td></tr><tr><td>衛署藥製字第011026號</td><td>暢冠錠</td><td>DIPYRIDAMOLE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第012383號</td><td>"易陽" 心能糖衣錠25毫克</td><td>DIPYRIDAMOLE</td><td>2019/02/23</td></tr><tr><td>衛署藥製字第013752號</td><td>待匹力達糖衣錠</td><td>DIPYRIDAMOLE</td><td>1999/09/30</td></tr><tr><td>衛署藥製字第014279號</td><td>待匹力達錠</td><td>DIPYRIDAMOLE</td><td>1989/06/20</td></tr><tr><td>衛署藥製字第015092號</td><td>待匹力達糖衣錠</td><td>DIPYRIDAMOLE</td><td>2023/07/07</td></tr><tr><td>衛署藥製字第015351號</td><td>待匹力達注射液</td><td>DIPYRIDAMOLE</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第015511號</td><td>培心正糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>2013/07/11</td></tr><tr><td>衛署藥製字第015734號</td><td>待匹力達糖衣錠１２．５公絲</td><td>DIPYRIDAMOLE</td><td>2005/11/14</td></tr><tr><td>衛署藥製字第015990號</td><td>保心糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>1999/07/30</td></tr><tr><td>衛署藥製字第016124號</td><td>舒爾心糖衣錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>1990/07/11</td></tr><tr><td>衛署藥製字第017573號</td><td>心冠暢糖衣錠（特匹力達）</td><td>DIPYRIDAMOLE</td><td>2015/04/15</td></tr><tr><td>衛署藥製字第017872號</td><td>"壽元"佑心循注射液（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第018776號</td><td>必賜平糖衣錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第018784號</td><td>舒必緩注射液（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第019034號</td><td>代比達脈錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2000/09/27</td></tr><tr><td>衛署藥製字第019502號</td><td>"杏輝"派達脈糖衣錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2023/07/07</td></tr><tr><td>衛署藥製字第019796號</td><td>心妙健錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2005/11/30</td></tr><tr><td>衛署藥製字第019894號</td><td>倍力進糖衣錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>1998/06/01</td></tr><tr><td>衛署藥製字第020095號</td><td>沛心寧糖衣錠７５公絲（特匹力達）</td><td>DIPYRIDAMOLE</td><td>2010/03/18</td></tr><tr><td>衛署藥製字第022187號</td><td>“成大”冠心糖衣錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2023/07/27</td></tr><tr><td>衛署藥製字第022802號</td><td>平心糖衣錠（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2006/04/19</td></tr><tr><td>衛署藥製字第023317號</td><td>待匹力達注射液</td><td>DIPYRIDAMOLE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第024356號</td><td>康樂待糖衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2010/05/24</td></tr><tr><td>衛署藥製字第024512號</td><td>心達平糖衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>1991/01/29</td></tr><tr><td>衛署藥製字第025197號</td><td>心脈順糖衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第025746號</td><td>配舒心糖衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第026008號</td><td>暢心寧糖衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2023/12/05</td></tr><tr><td>衛署藥製字第026521號</td><td>順心錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第027511號</td><td>恩福那糖衣錠１２．５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>1997/07/11</td></tr><tr><td>衛署藥製字第027512號</td><td>恩福那糖衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2007/06/15</td></tr><tr><td>衛署藥製字第028454號</td><td>備鎮心糖衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2017/02/09</td></tr><tr><td>衛署藥製字第028507號</td><td>備鎮心糖衣錠７５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2017/02/09</td></tr><tr><td>衛署藥製字第029432號</td><td>備鎮心糖衣錠５０公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2023/07/12</td></tr><tr><td>衛署藥製字第029765號</td><td>配達膜衣錠２５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2004/05/20</td></tr><tr><td>衛署藥製字第029766號</td><td>"大豐"配達膜衣錠75公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第030336號</td><td>固心糖衣錠</td><td>DIPYRIDAMOLE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第033622號</td><td>扶爾心糖衣錠１２．５公絲（待匹力達）</td><td>DIPYRIDAMOLE</td><td>1997/09/23</td></tr><tr><td>衛署藥製字第041288號</td><td>扶爾心糖衣錠１２．５公絲（二比待摩）</td><td>DIPYRIDAMOLE</td><td>2018/03/06</td></tr><tr><td>衛署藥製字第041726號</td><td>心平糖衣錠５０公絲（二比待摩）〝順生〞</td><td>DIPYRIDAMOLE</td><td>2013/11/04</td></tr><tr><td>衛署藥製字第041733號</td><td>心寧糖衣錠７５公絲（二比待摩）〝順生〞</td><td>DIPYRIDAMOLE</td><td>2013/11/04</td></tr><tr><td>衛署藥輸字第000634號</td><td>敵匹利汰毛兒</td><td>DIPYRIDAMOLE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004010號</td><td>雙/利摩</td><td>DIPYRIDAMOLE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第004606號</td><td>備鎮心注射液</td><td>DIPYRIDAMOLE</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第006165號</td><td>敵匹利汰毛兒</td><td>DIPYRIDAMOLE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第006401號</td><td>備鎮心糖衣錠７５公絲</td><td>CALCIUM PHOSPHATE DIBASIC、DIPYRIDAMOLE</td><td>1986/05/27</td></tr><tr><td>衛署藥輸字第006405號</td><td>備鎮心糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>1986/04/07</td></tr><tr><td>衛署藥輸字第006595號</td><td>心得寧糖衣錠</td><td>DIPYRIDAMOLE</td><td>1987/11/25</td></tr><tr><td>衛署藥輸字第008134號</td><td>敵匹利汰毛兒</td><td>DIPYRIDAMOLE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第008232號</td><td>心必利旦錠</td><td>DIPYRIDAMOLE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第008358號</td><td>固樂心錠７５公絲</td><td>DIPYRIDAMOLE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第008679號</td><td>泰彼心糖衣錠</td><td>DIPYRIDAMOLE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008853號</td><td>雙/利摩</td><td>DIPYRIDAMOLE</td><td>1992/12/22</td></tr><tr><td>衛署藥輸字第009073號</td><td>補心寧糖衣錠</td><td>DIPYRIDAMOLE</td><td>2013/01/04</td></tr><tr><td>衛署藥輸字第009510號</td><td>複合備鎮（Ｒ）心膠囊</td><td>DIPYRIDAMOLE</td><td>1991/02/12</td></tr><tr><td>衛署藥輸字第009693號</td><td>路佳斯糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>1995/02/15</td></tr><tr><td>衛署藥輸字第009694號</td><td>路佳斯糖衣錠１２．５公絲</td><td>DIPYRIDAMOLE</td><td>1995/02/15</td></tr><tr><td>衛署藥輸字第010334號</td><td>２，６－雙（二乙醇氨基）－４，８－二呱啶基嘧啶並－〔５，４右</td><td>DIPYRIDAMOLE</td><td>1998/09/15</td></tr><tr><td>衛署藥輸字第010371號</td><td>敵匹利汰毛兒</td><td>DIPYRIDAMOLE</td><td>1995/01/31</td></tr><tr><td>衛署藥輸字第010944號</td><td>德必他糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第010973號</td><td>冠循舒妥錠</td><td>DIPYRIDAMOLE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第010982號</td><td>利心康糖衣錠１２．５公絲</td><td>DIPYRIDAMOLE</td><td>1988/01/18</td></tr><tr><td>衛署藥輸字第010987號</td><td>冠循舒妥愛扶錠</td><td>DIPYRIDAMOLE</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第010997號</td><td>格利心糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>1988/11/10</td></tr><tr><td>衛署藥輸字第011002號</td><td>利心康錠２５公絲</td><td>DIPYRIDAMOLE</td><td>1987/10/30</td></tr><tr><td>衛署藥輸字第011104號</td><td>心脈藥通糖衣錠</td><td>DIPYRIDAMOLE</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第011365號</td><td>保心吉膠囊</td><td>DIPYRIDAMOLE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第013267號</td><td>心必利旦注射液</td><td>DIPYRIDAMOLE</td><td>2004/12/10</td></tr><tr><td>衛署藥輸字第013318號</td><td>心必利旦錠２５公絲</td><td>DIPYRIDAMOLE</td><td>2004/12/10</td></tr><tr><td>衛署藥輸字第013590號</td><td>克絡塞錠７５公絲</td><td>DIPYRIDAMOLE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第014345號</td><td>利心諾注射液</td><td>DIPYRIDAMOLE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第014346號</td><td>敵匹利達莫</td><td>DIPYRIDAMOLE</td><td>1987/01/10</td></tr><tr><td>衛署藥輸字第014602號</td><td>利心諾糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第016012號</td><td>達心平糖衣錠７５公絲</td><td>DIPYRIDAMOLE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第016064號</td><td>利心康錠２５公絲</td><td>DIPYRIDAMOLE</td><td>2009/11/11</td></tr><tr><td>衛署藥輸字第016081號</td><td>利心康糖衣錠１２．５公絲</td><td>DIPYRIDAMOLE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第016102號</td><td>心惠康糖衣錠</td><td>DIPYRIDAMOLE</td><td>2001/08/02</td></tr><tr><td>衛署藥輸字第016141號</td><td>安吉蒙糖衣錠</td><td>DIPYRIDAMOLE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第016152號</td><td>待匹力達</td><td>DIPYRIDAMOLE</td><td>1999/12/02</td></tr><tr><td>衛署藥輸字第016505號</td><td>待匹利達</td><td>DIPYRIDAMOLE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第016646號</td><td>格利奧斯汀注射液</td><td>DIPYRIDAMOLE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017834號</td><td>待匹力達</td><td>DIPYRIDAMOLE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第018442號</td><td>可博膜衣錠７５公絲</td><td>DIPYRIDAMOLE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第018471號</td><td>可博膜衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第018509號</td><td>倍加適糖衣錠</td><td>DIPYRIDAMOLE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第018616號</td><td>待匹力達</td><td>DIPYRIDAMOLE</td><td>2005/05/11</td></tr><tr><td>衛署藥輸字第019305號</td><td>待匹力達</td><td>DIPYRIDAMOLE</td><td>1999/06/24</td></tr><tr><td>衛署藥輸字第019603號</td><td>雙/利摩</td><td>DIPYRIDAMOLE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第019902號</td><td>黛德利那糖衣錠１２．５公絲</td><td>DIPYRIDAMOLE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019905號</td><td>黛德劉那糖衣錠２５公絲</td><td>DIPYRIDAMOLE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第020244號</td><td>達樂爾錠</td><td>DIPYRIDAMOLE</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第022742號</td><td>二比待摩</td><td>DIPYRIDAMOLE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第023919號</td><td>腦康平持續性藥效膠囊</td><td>ACETYLSALICYLIC ACID、DIPYRIDAMOLE</td><td>2019/10/02</td></tr><tr><td>衛署藥陸輸字第000004號</td><td>二口比待摩</td><td>DIPYRIDAMOLE</td><td>2010/09/21</td></tr><tr><td>衛部藥陸輸字第000919號</td><td>二吡待摩</td><td>Dipyridamole</td><td>2026/06/03</td></tr><tr><td>衛部藥陸輸字第000932號</td><td>二吡待摩</td><td>Dipyridamole</td><td>2026/07/27</td></tr><tr><td>衛部藥陸輸字第000938號</td><td>二吡待摩</td><td>Dipyridamole</td><td>2025/06/12</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **知識圖譜中的禁忌關聯**（來自 TxGNN 知識圖譜，非仿單內容）：腎臟疾病、肝臟疾病、膽囊疾病、血小板低下、消化性潰瘍、低血壓、痛風、急性冠心症、心肌梗塞、血友病、貧血、胃炎等。這些屬於模型關聯，實際禁忌請以仿單為準。
- **藥物交互作用**：資料庫共收錄 321 筆。其中 Moderate 等級包括 Dexfenfluramine、Sibutramine、Fenfluramine；其餘如 Acetylsalicylic acid（aspirin）、Cimetidine、Omeprazole、Metformin、Simvastatin、Morphine 等的分級為 Unknown。併用抗血小板或抗凝血藥物時須特別留意出血風險。
- **針對預測適應症的特殊疑慮**：在血管痙攣型狹心症中，血管擴張可能造成冠狀動脈竊血或誘發痙攣；Dipyridamole 提高腺苷濃度，也可能抑制竇房結功能。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（針對首位預測：Prinzmetal 狹心症）**

**理由：**
- Prinzmetal 狹心症沒有任何臨床試驗，文獻多為診斷用途或個案報告，且有報告顯示可能誘發冠狀動脈痙攣，證據等級僅 L4，療效未證實且有安全疑慮。
- 相較之下，**中風**與 **TIA** 有 ESPRIT（n=4500）等 RCT 與多項統合分析支持，證據等級為 L1，建議決策為 **Proceed with Guardrails**。不過 aspirin 加 dipyridamole 用於二級預防在國際上已屬既有用法，其「再利用」的新穎性有限；若在台灣推進，主要是適應症與劑型（如緩釋複方）的取得問題。

**若要推進需要：**
- Prinzmetal 狹心症：需有設計良好的對照試驗，並先釐清血管痙攣與竊血風險；在此之前不建議推進。
- 中風／TIA：確認台灣現有許可證的適應症範圍（現行多為狹心症與診斷用途），評估是否需要補充適應症或引進 aspirin 加緩釋 dipyridamole 的複方劑型。
- 補齊 DrugBank 作用機轉資料，並完整審視 321 筆交互作用，建立併用抗血栓藥物的出血監測方案。
- 其餘低排名預測（如 sarcoglycanopathy、Wildervanck 症候群等）無任何證據或合理機轉，建議維持 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：Dipyridamole Tablets, USP 仿單（Amneal）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a18b2af5-7c4a-4b7f-92c7-8a76e34da373) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

