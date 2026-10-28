---
layout: default
title: Prednisolone Acetate
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
monitor_inn: "Prednisolone acetate"
predicted_indications: ["conjunctival folliculosis", "serous conjunctivitis except viral", "chronic follicular conjunctivitis", "parasitic conjunctivitis", "papillary conjunctivitis", "Angelucci syndrome", "pseudomembranous conjunctivitis", "acute hemorrhagic conjunctivitis", "vernal conjunctivitis", "postinfectious vasculitis"]
last_modified_at: 2026-10-29
description: "Prednisolone Acetate：預測新適應症為結膜濾泡增生 (conjunctival folliculosis)（證據等級 L5）。原適應症：僂麻質斯性關節炎、骨關節炎、痛風性關節炎、僂麻質斯性脊椎炎、肌肉僂麻質斯、滑液囊炎"
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Prednisolone acetate：從眼部過敏性炎症疾患到結膜濾泡增生
{: .text-alpha }

## 一句話總結

Prednisolone acetate（乙酸培尼皮質醇）是一種抗炎性皮質類固醇，在台灣原本用於眼瞼炎、結膜炎、角膜炎等眼部過敏性炎症疾患，以及風濕性關節炎等。
TxGNN 模型預測排名第一的新適應症為**結膜濾泡增生 (conjunctival folliculosis)**，但該項僅有模型預測，無任何臨床試驗或文獻。
本報告同時說明證據相對最多的**乳頭狀結膜炎 (papillary conjunctivitis)** 與**春季結膜炎 (vernal conjunctivitis)**，但這兩者的證據都屬間接證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 僂麻質斯性關節炎、骨關節炎、痛風性關節炎、僂麻質斯性脊椎炎、肌肉僂麻質斯、滑液囊炎 |
| 預測新適應症 | 結膜濾泡增生 (conjunctival folliculosis) |
| TxGNN 預測分數 | 0.9974 |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 台灣上市 | 上市中（有效許可證 20 張／共 63 張） |
| 許可證數 | 63 張（有效單方 9／有效複方 11／已註銷 43） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Prednisolone acetate 屬於糖皮質素受體促效劑，可抑制磷脂酶 A2、下調 NF-κB 等發炎介質，進而降低結膜濾泡的發炎反應。

台灣核准適應症本身已涵蓋眼瞼炎、結膜炎、角膜炎、鞏膜炎及虹彩毛樣體炎等眼部過敏性與發炎性疾患。預測的新適應症多為結膜發炎類疾病，與既有的眼科用途在病理上高度相關，因此機轉上有其合理性。

需要注意：排名前幾名的預測（結膜濾泡增生、非病毒性漿液性結膜炎、慢性濾泡性結膜炎）都沒有任何臨床證據。寄生蟲性結膜炎及急性出血性結膜炎（多為病毒性）則有感染惡化風險，使用類固醇須先處理致病原。

---

## 臨床試驗證據

排名第一的預測（結膜濾泡增生）目前無相關臨床試驗登記。以下為證據相對較多的其他預測適應症的試驗，均屬間接證據：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01437982](https://clinicaltrials.gov/study/NCT01437982) | Phase 4 | 完成 | 140 | 針對乳頭狀結膜炎：Loteprednol（同類眼用類固醇，非本藥）上市後監測，評估不良反應與安全性 |
| [NCT04705584](https://clinicaltrials.gov/study/NCT04705584) | 不適用 | 未知 | 180 | 針對春季結膜炎：比較 Cyclosporine A 2% 與 Tacrolimus 0.3%，試驗組不明確包含本藥 |

---

## 文獻證據

排名第一的預測（結膜濾泡增生）目前無相關文獻。以下為其他預測適應症的主要文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24055903](https://pubmed.ncbi.nlm.nih.gov/24055903/) | 2013 | RCT（實驗動物模型） | Cornea | 在實驗性過敏性結膜炎模型中，比較 Cyclosporine A、Epinastine 與 1% Prednisolone acetate 對過敏性發炎的作用 |
| [26984315](https://pubmed.ncbi.nlm.nih.gov/26984315/) | 2016 | Review | Advances in Therapy | 回顧 Loteprednol 對眼壓的影響，眼用類固醇有眼壓升高風險 |
| [18020605](https://pubmed.ncbi.nlm.nih.gov/18020605/) | 1998 | Review | BioDrugs | Loteprednol 用於眼部發炎的臨床潛力 |
| [12931748](https://pubmed.ncbi.nlm.nih.gov/12931748/) | 2003 | Cohort | Asian Pac J Allergy Immunol | 泰國春季角結膜炎患者的臨床特徵與治療結果；嚴重者使用局部類固醇 |
| [9713785](https://pubmed.ncbi.nlm.nih.gov/9713785/) | 1998 | Cohort | J Glaucoma | Loteprednol 長期使用的眼壓變化 |
| [32621983](https://pubmed.ncbi.nlm.nih.gov/32621983/) | 2020 | Case series | J AAPOS | 黴漿菌相關皮疹與黏膜炎的眼部表現，病例使用局部 Prednisolone acetate 合併其他治療 |
| [21434554](https://pubmed.ncbi.nlm.nih.gov/21434554/) | 2011 | 病例報告 | Indian J Tuberculosis | 原發性結膜結核被誤診為過敏性結膜炎，使用 1% Prednisolone acetate 無改善 |
| [15523196](https://pubmed.ncbi.nlm.nih.gov/15523196/) | 2004 | Review | Curr Opin Ophthalmol | 移植物抗宿主病的眼部表現與處置 |

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

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，非仿單內容）：遺傳性紫質症、紫質代謝疾病、單純皰疹病毒角膜炎、開角型青光眼、糖尿病、糖尿病酮酸中毒、高眼壓、G6PD 缺乏症、肝醣儲積症、胱胺酸尿症、半乳糖血症、眼部感染性疾病、結膜炎、眼部真菌感染、病毒性眼部感染、眼部結核、角膜色素沉著。
- **臨床提醒**：文獻顯示眼用類固醇有眼壓升高風險。感染性結膜炎（寄生蟲、病毒、結核等）使用類固醇可能使病情惡化。

其餘警語與藥物交互作用資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（結膜濾泡增生）僅有模型預測，無任何臨床試驗或文獻，證據等級為 L5。
- 乳頭狀結膜炎與春季結膜炎有間接證據，但研究對象為同類藥物（Loteprednol）或其他免疫抑制劑，沒有直接研究本藥於該疾病者，因此仍視為 L5，只能列為研究問題。

**若要推進需要：**
- 取得詳細的作用機轉資料。
- 針對結膜濾泡增生等預測疾病，搜尋或設計直接評估 Prednisolone acetate 的臨床研究。
- 對感染性結膜炎（寄生蟲性、病毒性）先釐清致病原，並評估使用類固醇的風險。
- 擬定眼壓、白內障及感染的監測計畫。
- 確認既有眼用劑型（點眼液劑、點眼懸液劑）與預測疾病的給藥途徑相容。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

