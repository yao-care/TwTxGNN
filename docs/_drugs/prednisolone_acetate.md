---
layout: default
title: Prednisolone Acetate
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
monitor_inn: "Prednisolone acetate"
predicted_indications: ["parasitic conjunctivitis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral", "conjunctival folliculosis", "papillary conjunctivitis", "Angelucci syndrome", "pseudomembranous conjunctivitis", "acute hemorrhagic conjunctivitis", "vernal conjunctivitis", "postinfectious vasculitis"]
last_modified_at: 2026-10-16
description: "Prednisolone Acetate：預測新適應症為寄生蟲性結膜炎 (Parasitic Conjunctivitis)（證據等級 L5）。原適應症：抗炎性皮質固醇"
---

# Prednisolone Acetate
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

# Prednisolone acetate：從眼部與關節發炎性疾患到寄生蟲性結膜炎

## 一句話總結

Prednisolone acetate（乙酸培尼皮質醇）是一種糖皮質素，原本用於眼瞼炎、結膜炎、角膜炎等眼部過敏性疾患，以及風濕性關節炎等發炎性疾病。
TxGNN 模型預測它可能對**寄生蟲性結膜炎 (Parasitic Conjunctivitis)** 有效，但此預測目前**沒有任何臨床試驗或文獻**支持，僅屬模型推論。
在所有預測中，證據相對較多的是**乳突性結膜炎**與**春季結膜炎**，但這些證據主要來自同類藥物或其他免疫抑制劑，並非本藥本身。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗炎性皮質固醇 |
| 預測新適應症 | 寄生蟲性結膜炎 (Parasitic Conjunctivitis) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 63 張（有效單方 9／有效複方 11／已註銷 43） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Prednisolone acetate 屬於糖皮質素類藥物，一般認為透過糖皮質素受體抑制 NF-κB 及磷脂酶 A2，進而減輕發炎反應。其在台灣的核准適應症涵蓋眼瞼炎、結膜炎、角膜炎、鞏膜炎、虹彩毛樣體炎等眼部發炎與過敏性疾患，因此在機轉上可能適用於結膜發炎相關疾病。

不過，寄生蟲性結膜炎的根本原因是寄生蟲感染，類固醇只能緩解發炎，無法處理病因，甚至可能干擾對感染的控制。因此這個預測目前只有模型分數支持，臨床上的合理性有限。

同一批預測中，多數為結膜炎的各種亞型（慢性濾泡性、漿液性、乳突性、春季、偽膜性等），反映模型主要捕捉到「結膜發炎」這一共通主題。另有少數預測（如急性出血性結膜炎、感染後血管炎）在機轉上較弱，前者為自限性病毒感染，使用類固醇可能影響病毒清除，後者則因眼用製劑全身暴露極低而不合理。

---

## 臨床試驗證據

針對排名第一的預測（寄生蟲性結膜炎），目前無相關臨床試驗登記。

作為參考，同批預測中有臨床試驗登記的適應症如下：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01437982](https://clinicaltrials.gov/study/NCT01928852) | Phase 4 | 完成 | 140 | 乳突性結膜炎：以另一種局部類固醇（loteprednol etabonate 0.5%）進行上市後監測，主要評估不良事件，並非本藥 |
| [NCT04705584](https://clinicaltrials.gov/study/NCT04705584) | 不適用 | 未知 | 180 | 春季結膜炎：比較 cyclosporine 2% 與 tacrolimus 0.3% 作為類固醇替代療法，並非本藥 |

---

## 文獻證據

針對排名第一的預測（寄生蟲性結膜炎），目前無相關文獻。

作為參考，同批預測中較相關的文獻如下：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24055903](https://pubmed.ncbi.nlm.nih.gov/24055903/) | 2013 | RCT（實驗動物模型） | Cornea | 春季結膜炎／過敏性結膜炎：比較 cyclosporine A、epinastine 與 prednisolone acetate 1% 對過敏性發炎的作用 |
| [26984315](https://pubmed.ncbi.nlm.nih.gov/26984315/) | 2016 | Review | Advances in Therapy | 局部眼用類固醇（loteprednol）對眼壓的影響，提醒長期使用的眼壓風險 |
| [18020605](https://pubmed.ncbi.nlm.nih.gov/18020605/) | 1998 | Review | BioDrugs | Loteprednol etabonate 用於眼部發炎的臨床潛力 |
| [9713785](https://pubmed.ncbi.nlm.nih.gov/9713785/) | 1998 | Cohort | Journal of Glaucoma | Loteprednol 長期使用的眼壓變化 |
| [12931748](https://pubmed.ncbi.nlm.nih.gov/12931748/) | 2003 | Case series | Asian Pac J Allergy Immunol | 泰國春季角結膜炎患者的治療結果，嚴重個案使用局部類固醇 |
| [32621983](https://pubmed.ncbi.nlm.nih.gov/32621983/) | 2020 | Case series | J AAPOS | 黴漿菌相關皮疹與黏膜炎合併偽膜性結膜炎，使用局部 prednisolone acetate 治療 |
| [21434554](https://pubmed.ncbi.nlm.nih.gov/21434554/) | 2011 | 個案報告 | Indian J Tuberculosis | 結膜結核被誤診為過敏性結膜炎，使用 prednisolone acetate 1% 後無改善，警示感染性病因誤用類固醇的風險 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Prednisolone Acetate 的不重複許可證共 **63 張**：有效單方 9 張、有效複方 11 張、已註銷 43 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（9 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第002798號 | 樂爾爽注射液 | 注射劑 | 中國化學製藥股份有限公司新豐工廠 | 2028/04/18 | 僂麻質斯性關節炎、骨關節炎、痛風性關節炎、僂麻質斯性脊椎炎、肌肉僂麻質斯、滑液囊炎 |
| 衛署藥製字第010373號 | 樂爾爽注射液２５公絲 | 注射劑 | 中國化學製藥股份有限公司新豐工廠 | 2028/07/27 | 僂麻質斯性關節炎、骨關節炎、痛風性關節炎、僂麻質斯性脊椎炎、肌肉僂麻質斯、滑液囊炎 |
| 衛署藥製字第049561號 | 復眼康眼藥水 1 % | 點眼液劑 | 溫士頓醫藥股份有限公司 | 2028/07/25 | 眼瞼炎、結膜炎、角膜炎、鞏膜炎、虹彩毛樣體炎等過敏性疾患。 |
| 衛署藥輸字第018654號 | 倍力特眼用懸浮液１％ | 點眼懸液劑 | 瑞士商艾伯維藥品有限公司台灣分公司 | 2030/01/08 | 過敏性眼瞼緣炎、結合膜炎、潰瘍性角膜炎、異物入侵所引起之炎症。 |
| 衛署藥陸輸字第000037號 | 乙酸培尼皮質醇 | （粉） | 川聖貿易股份有限公司 | 2029/01/09 | 抗炎性皮質固醇。 |
| 衛署藥陸輸字第000150號 | 乙酸培尼皮質醇 | （粉） | 菩鏹股份有限公司 | 2030/04/19 | 抗炎性皮質固醇。 |
| 衛署藥陸輸字第000363號 | 乙酸培尼皮質醇 | （粉） | 誠品貿易股份有限公司 | 2029/06/30 | 抗炎性皮質固醇。 |
| 衛署藥陸輸字第000576號 | 乙酸培尼皮質醇 | （粉） | 宣泓貿易有限公司 | 2028/04/07 | 抗炎性皮質固醇 |
| 衛部藥輸字第027849號 | 乙酸培尼皮質醇 | （粉） | 丞泰企業有限公司 | 2030/04/06 | 抗炎性皮質固醇 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（11 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第030733號 | 愛膚乳膏 | LIDOCAINE HCL、CHLORPHENIRAMINE MALEATE、D-CAMPHOR、PREDNISOLON… | 乳膏劑 | 搔癢、蚊蟲咬傷、濕疹、皮膚炎、蕁麻疹、汗疹、皮膚感染、打撲傷、凍傷、燙傷 |
| 衛署藥製字第031918號 | 痔福栓劑 | TOCOPHEROL ACETATE ALPHA DL-、CHLORHEXIDINE HCL、LIDOCAINE、PRE… | 栓劑 | 緩解痔核、裂痔、痔腫、痔痒、外痔症狀所產生的痔痛、痔腫、癢及出血現象 |
| 衛署藥製字第032836號 | 非常理痔栓劑 | ALUMINUM CHLORHYDROXYALLANTOINATE (ALCOXA)、PREDNISOLONE ACET… | 栓劑 | 緩解裂痔、痔核、痔腫、痔痒、外痔症狀所產生之痔痛、痔腫、痒及出血現象 |
| 衛署藥製字第039618號 | 痔秘消軟膏 | TOCOPHEROL ACETATE ALPHA DL-、CHLORHEXIDINE HCL、LIDOCAINE、PRE… | 軟膏劑 | 緩解因痔瘡所引起的症狀(疼痛、灼熱、搔癢、腫脹、痔出血)，及預防局部感染。 |
| 衛署藥製字第039941號 | 寧疤寧敏感止癢乳膏 | CHLORHEXIDINE HCL、MENTHOL、CAMPHOR、PREDNISOLONE ACETATE、LIDOC… | 軟膏劑 | 搔癢、蚊蟲咬傷、汗疹、蕁麻疹、斑疹、濕疹、皮膚炎、皮膚感染燙傷、凍傷 |
| 衛署藥製字第041743號 | 〝人生〞拿痔能軟膏 | PREDNISOLONE ACETATE、LIDOCAINE、TOCOPHEROL ACETATE、CHLORHEXID… | 軟膏劑 | 內痔、外痔、痔出血、肛門周圍炎。 |
| 衛署藥製字第045579號 | 利那痛痔軟膏 | ALUMINUM CHLORHYDROXYALLANTOINATE (ALCOXA)、PREDNISOLONE ACET… | 軟膏劑 | 緩解因痔瘡所引起的症狀(疼痛、灼熱、搔癢、腫脹、痔出血)，及預防局部感染。 |
| 衛署藥輸字第024852號 | 保能痔注入軟膏 | ALLANTOIN、PREDNISOLONE ACETATE、TOCOPHEROL ACETATE、LIDOCAINE | 軟膏劑 | 緩解因痔瘡所引起的疼痛、灼熱、搔癢、腫脹、痔出血。 |
| 衛署藥輸字第024954號 | 保能痔栓劑 | TOCOPHEROL ACETATE、ALLANTOIN、LIDOCAINE、PREDNISOLONE ACETATE | 栓劑 | 緩解因痔瘡所引起的疼痛、灼熱、搔癢、腫脹、痔出血。 |
| 衛部藥製字第061111號 | "欣痔平"注入軟膏 | TOCOPHEROL ACETATE、LIDOCAINE、PREDNISOLONE ACETATE、ALLANTOIN | 乳膏劑 | 緩解因痔瘡所引起的疼痛、灼熱、搔癢、腫脹、痔出血。 |
| 衛部藥製字第062347號 | “好能痔”軟膏 | LIDOCAINE、TOCOPHEROL ACETATE、PREDNISOLONE ACETATE、ALLANTOIN | 軟膏劑 | 緩解因痔瘡所引起的疼痛、灼熱、搔癢、腫脹、痔出血。 |

<details><summary><strong>已註銷</strong>（43 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第001116號</td><td>醋酸去氫氫化可體松懸濁液２５公絲/公撮</td><td>PREDNISOLONE ACETATE</td><td>2010/02/08</td></tr><tr><td>內衛藥輸字第003777號</td><td>醋酸腎上腺皮質激素</td><td>PREDNISOLONE ACETATE</td><td>1987/04/07</td></tr><tr><td>內衛藥輸字第005048號</td><td>補力多寧眼軟膏</td><td>PREDNISOLONE ACETATE</td><td>2004/12/23</td></tr><tr><td>內衛藥輸字第005120號</td><td>乙醯去氫羥化腎上腺皮質素</td><td>PREDNISOLONE ACETATE</td><td>1985/11/07</td></tr><tr><td>內衛藥輸字第005886號</td><td>美滴媚眼藥水</td><td>SODIUM THIOSULFATE、SULFACETAMIDE SODIUM、PREDNISOLONE ACETATE</td><td>2004/12/23</td></tr><tr><td>衛署藥製字第030973號</td><td>允消膚快乳膏</td><td>D-CAMPHOR、LIDOCAINE HCL、METHYL SALICYLATE、CHLORHEXIDINE HCL、…</td><td>2015/05/29</td></tr><tr><td>衛署藥製字第035332號</td><td>"一成"消痔栓劑</td><td>CHLORHEXIDINE HCL、LIDOCAINE、PREDNISOLONE ACETATE、ALUMINUM CH…</td><td>2024/04/29</td></tr><tr><td>衛署藥輸字第000503號</td><td>醋酸皮質固醇</td><td>PREDNISOLONE ACETATE</td><td>1998/12/18</td></tr><tr><td>衛署藥輸字第001603號</td><td>"普強" 乙酸去氫氧化可體松</td><td>PREDNISOLONE ACETATE</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第002227號</td><td>施滴明眼藥水</td><td>PREDNISOLONE ACETATE</td><td>1986/11/17</td></tr><tr><td>衛署藥輸字第004163號</td><td>眼舒明</td><td>POLYMYXIN B SULFATE、NEOMYCIN (SULFATE)、PREDNISOLONE ACETATE</td><td>1986/02/21</td></tr><tr><td>衛署藥輸字第004374號</td><td>醋酸去氫羥化腎上腺皮質素</td><td>PREDNISOLONE ACETATE</td><td>2010/09/13</td></tr><tr><td>衛署藥輸字第008782號</td><td>愛世痔斯軟膏</td><td>TOCOPHEROL ACETATE ALPHA DL-、TETRACAINE、ALLANTOIN、BENZOCAINE…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009085號</td><td>保眼點眼液</td><td>PREDNISOLONE ACETATE、SULFACETAMIDE SODIUM、PHENYLEPHRINE HCL</td><td>1986/02/17</td></tr><tr><td>衛署藥輸字第010129號</td><td>視都普眼藥水</td><td>BENZALKONIUM CHLORIDE、PREDNISOLONE ACETATE、SULFACETAMIDE SOD…</td><td>1985/07/10</td></tr><tr><td>衛署藥輸字第010841號</td><td>普利多寧點眼液</td><td>PREDNISOLONE (ACETATE)</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第011647號</td><td>易控炎眼藥水１/８％</td><td>PREDNISOLONE ACETATE</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第011648號</td><td>易控炎眼藥水１％</td><td>PREDNISOLONE ACETATE</td><td>1989/10/12</td></tr><tr><td>衛署藥輸字第012110號</td><td>補力多寧（注）２．５％</td><td>PREDNISOLONE ACETATE</td><td>1994/06/10</td></tr><tr><td>衛署藥輸字第012120號</td><td>補力多寧針（１％）</td><td>PREDNISOLONE ACETATE</td><td>1994/06/10</td></tr><tr><td>衛署藥輸字第012619號</td><td>倍得美眼用懸液</td><td>PREDNISOLONE ACETATE</td><td>1985/09/07</td></tr><tr><td>衛署藥輸字第012620號</td><td>倍力特眼用懸液</td><td>PREDNISOLONE ACETATE</td><td>1985/09/07</td></tr><tr><td>衛署藥輸字第012628號</td><td>補力多寧懸浮注射液２．５％</td><td>PREDNISOLONE ACETATE</td><td>1992/01/17</td></tr><tr><td>衛署藥輸字第012629號</td><td>補力多寧懸浮注射液１％</td><td>PREDNISOLONE ACETATE</td><td>1992/01/17</td></tr><tr><td>衛署藥輸字第013097號</td><td>百利明點眼懸浮液</td><td>BENZALKONIUM CHLORIDE、SULFACETAMIDE SODIUM、PREDNISOLONE ACET…</td><td>1992/01/10</td></tr><tr><td>衛署藥輸字第013338號</td><td>普利多寧點眼液</td><td>PREDNISOLONE (ACETATE)</td><td>1988/06/16</td></tr><tr><td>衛署藥輸字第013556號</td><td>視都普眼藥水</td><td>BENZALKONIUM CHLORIDE、SODIUM THIOSULFATE、SULFACETAMIDE SODIU…</td><td>1991/02/06</td></tr><tr><td>衛署藥輸字第013880號</td><td>倍力特眼用懸浮液１％</td><td>PREDNISOLONE ACETATE</td><td>1991/08/23</td></tr><tr><td>衛署藥輸字第013882號</td><td>倍得美眼用懸浮液０．１２％</td><td>PREDNISOLONE ACETATE</td><td>1991/08/23</td></tr><tr><td>衛署藥輸字第014328號</td><td>乙醯去氫羥化腎上腺皮質素</td><td>PREDNISOLONE ACETATE</td><td>1995/05/26</td></tr><tr><td>衛署藥輸字第015216號</td><td>乙酸培尼皮質醇</td><td>PREDNISOLONE ACETATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第017400號</td><td>易控炎眼藥水１％</td><td>PREDNISOLONE ACETATE</td><td>2024/01/15</td></tr><tr><td>衛署藥輸字第018456號</td><td>視都普眼用懸浮液〝愛爾康比利時廠〞</td><td>PREDNISOLONE ACETATE、SULFACETAMIDE SODIUM</td><td>2013/01/08</td></tr><tr><td>衛署藥輸字第018646號</td><td>百力特點眼懸浮液</td><td>POLYMYXIN B SULFATE、NEOMYCIN (SULFATE)、PREDNISOLONE ACETATE</td><td>2016/12/26</td></tr><tr><td>衛署藥輸字第018666號</td><td>倍得美眼用懸浮液０．１２％</td><td>PREDNISOLONE ACETATE</td><td>2016/12/26</td></tr><tr><td>衛署藥輸字第018839號</td><td>百利明點眼懸浮液</td><td>PREDNISOLONE ACETATE、SULFACETAMIDE SODIUM</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第018934號</td><td>視都普眼軟膏〝愛爾康比利時廠〞</td><td>PREDNISOLONE ACETATE、SULFACETAMIDE SODIUM</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第019354號</td><td>酯酸皮質固醇</td><td>PREDNISOLONE ACETATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第019982號</td><td>利明點眼懸浮液</td><td>SULFACETAMIDE SODIUM、PREDNISOLONE (ACETATE)</td><td>2004/03/10</td></tr><tr><td>衛署藥輸字第020608號</td><td>歐舒炎眼藥水</td><td>PREDNISOLONE ACETATE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第020781號</td><td>乙醯去氫羥化腎上腺皮質素</td><td>PREDNISOLONE ACETATE</td><td>2004/05/04</td></tr><tr><td>衛署藥輸字第024713號</td><td>乙酸培尼皮質醇</td><td>PREDNISOLONE 21 ACETATE (PREDNISOLONE ACETATE)</td><td>2019/03/22</td></tr><tr><td>衛署藥陸輸字第000470號</td><td>乙酸培尼皮質醇</td><td>Prednisolone Acetate</td><td>2022/06/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **藥物交互作用**：本次查詢未找到交互作用資料。
- **知識圖譜標示的禁忌疾病**（來源為 TxGNN 知識圖譜，非仿單內容）：
  - 眼部感染：疱疹性角膜炎、病毒性眼部感染、黴菌性眼部感染、眼部結核、眼部感染性疾病
  - 眼壓相關：開角型青光眼、高眼壓
  - 代謝疾病：糖尿病、糖尿病酮酸中毒
  - 其他：紫質症（遺傳性紫質症、紫質代謝疾病）、G6PD 缺乏症、肝醣儲積症、胱胺酸尿症、半乳糖血症、角膜色素沉著
- 文獻同時提醒，長期局部使用類固醇可能造成眼壓升高與白內障，需要監測。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（寄生蟲性結膜炎）僅有 TxGNN 模型分數，沒有任何臨床試驗或文獻；且類固醇無法處理寄生蟲病因，單用還可能掩蓋或惡化感染。
- 整批預測中，乳突性結膜炎與春季結膜炎有較多間接證據（L4），但證據多來自 loteprednol、cyclosporine 等其他藥物，仍屬研究問題階段，尚不足以支持推進。

**若要推進需要：**
- 取得完整的作用機轉資料（MOA）。
- 優先轉向證據較多的春季結膜炎與乳突性結膜炎，尋找直接使用 prednisolone acetate 的對照研究。
- 釐清各預測疾病的病因（過敏性、感染性、免疫性），建立排除感染後才使用類固醇的流程。
- 規劃眼壓與白內障監測，並對疱疹性角膜炎、青光眼等禁忌族群設定排除條件。
- 確認各預測疾病與既有劑型（眼藥水、眼軟膏）的給藥途徑相容性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

