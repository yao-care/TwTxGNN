---
layout: default
title: Tyrosine
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine 藥師評估報告

## 一句話總結

Tyrosine (酪氨酸) 是一種非必需胺基酸，TxGNN 預測其可能對多種甲狀腺疾病及神經系統疾病具有潛在療效，其中甲狀腺相關預測具有較強的生化機制支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Tyrosine (酪氨酸 / L-Tyrosine) |
| DrugBank ID | DB00135 |
| 原核准適應症 | 胺基酸營養補給劑 |
| 預測新適應症數量 | 10 項 |
| 最高預測分數適應症 | 馬尾症候群，分數 0.998 |
| 臨床試驗支持 | 有限，主要為間接相關 |
| 文獻證據 | 甲狀腺相關文獻較豐富 |
| 台灣上市狀態 | 多為已註銷之原料藥 |

---

## 為什麼預測合理

### 預測機制分析

1. **甲狀腺功能亢進 (Hyperthyroidism)** - TxGNN 分數: 0.995
   - **機制明確**：Tyrosine 是甲狀腺素 (T3/T4) 合成的必需前驅物
   - 有 4 項臨床試驗及 20+ 篇 PubMed 文獻支持
   - 文獻 PMID: 36848916 詳細描述甲狀腺功能亢進的病因學，提及 tyrosine kinase 抑制劑可誘發甲狀腺功能異常

2. **甲狀腺素過多血症 (Hyperthyroxinemia)** - TxGNN 分數: 0.995
   - 與甲狀腺素代謝直接相關
   - 文獻 PMID: 40171189 報導 Levodopa 誘導甲狀腺功能調節的案例，涉及多巴胺-甲狀腺軸

3. **姿位性心搏過速症候群 (POTS)** - TxGNN 分數: 0.995
   - 有 1 項臨床試驗 (NCT00580619) 涉及自主神經系統與慢性疲勞
   - 文獻 PMID: 39063020 報導使用 alpha-methyl-p-tyrosine (AMPT) 治療慢性疲勞合併 POTS 的案例

4. **隅角閉鎖型青光眼** - TxGNN 分數: 0.995
   - 有 6 篇相關文獻，涉及 tyrosine kinase 在眼壓調控中的角色
   - 文獻 PMID: 22568104 討論 SRC tyrosine kinase 在青光眼護理中的意義

5. **新生血管性青光眼 (Neovascular Glaucoma)** - TxGNN 分數: 0.993
   - 有 2 項臨床試驗 (NCT05131646, NCT04626128) 評估 tyrosine kinase 抑制劑
   - 文獻 PMID: 22898649 討論 anti-VEGF 療法與 tyrosine kinase 抑制劑在眼部新生血管的角色

### 知識圖譜連結

Tyrosine 作為兒茶酚胺 (多巴胺、腎上腺素) 和甲狀腺素的共同前驅物，與神經系統和內分泌系統疾病有廣泛的生化連結。

---

## 臨床試驗

### 相關臨床試驗

| 試驗編號 | 適應症 | 期別 | 狀態 | 國家 |
|----------|--------|------|------|------|
| NCT07200882 | TKI 對甲狀腺功能影響 | N/A | 尚未招募 | N/A |
| NCT04809454 | 甲狀腺功能亢進 | N/A | 未知 | 巴基斯坦 |
| NCT06264544 | 預防甲狀腺毒症 (鋅/硒/L-Tyrosine) | N/A | 尚未招募 | 俄羅斯 |
| NCT04740307 | 肝細胞癌 (TKI 組合療法) | Phase 2 | 已完成 | 多國 |
| NCT00580619 | POTS/慢性疲勞 | Phase 1 | 已完成 | 美國 |
| NCT05131646 | 新生血管性 AMD | N/A | 已完成 | 美國 |

**備註**：多數試驗涉及 tyrosine kinase 抑制劑而非 tyrosine 本身，但顯示相關生物路徑的臨床研究活躍度。

---

## 文獻證據

### 相關 PubMed 文獻

| 適應症 | 文獻數量 | 代表性文獻 |
|--------|----------|------------|
| 甲狀腺功能亢進 | 20+ | PMID: 36848916 - 甲狀腺功能亢進完整回顧 |
| POTS | 4 | PMID: 31412221 - POTS 機制與新療法 |
| 青光眼 | 6 | PMID: 32222418 - 過氧亞硝酸與青光眼 |
| 甲狀腺激素阻抗 | 8 | PMID: 10579356 - THR beta 受體突變 |

### 關鍵文獻摘要

1. **PMID: 36848916** - Lancet Diabetes & Endocrinology (2023)
   - 甲狀腺功能亢進全面回顧，提及 tyrosine kinase 抑制劑作為病因之一

2. **PMID: 39063020** - Int J Mol Sci (2024)
   - Alpha-methyl-p-tyrosine 治療壓力相關慢性疲勞合併 POTS 的案例報告

3. **PMID: 5327670** - Am J Med (1966)
   - 經典文獻：Tyrosine 與甲狀腺激素的關係

**證據等級評估：中等**
- 甲狀腺相關：有較強的生化基礎
- 神經系統相關：主要為間接證據

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tyrosine 的不重複許可證共 **174 張**：有效單方 0 張、有效複方 38 張、已註銷 136 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>有效・複方（適應症屬整個複方，不是本藥單獨的適應症）</strong>（38 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>劑型</th><th>核准適應症</th></tr></thead><tbody><tr><td>內衛藥製字第011832號</td><td>維他新多命膠囊</td><td>L- GLUTAMIC ACID、L-LEUCINE、METHIONINE DL-、RIBOFLAVIN (VIT B2…</td><td>膠囊劑</td><td>維他命缺乏症、營養補給、體力恢復、貧血、神經炎、病後促進復元、夜盲症</td></tr><tr><td>衛署藥製字第011723號</td><td>"信東" 胺美樂瑞注射液</td><td>XYLITOL、L-ISOLEUCINE、L-THREONINE、L-PROLINE、L-PHENYLALANINE、L…</td><td>注射劑</td><td>手術前後之營養補給、不能經口之補給營養及水分時</td></tr><tr><td>衛署藥製字第019962號</td><td>"台裕 "綜胺酸五碳糖注射液</td><td>L-TYROSINE、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-ALANINE、L-T…</td><td>注射劑</td><td>糖尿病患者或手術後糖利用障害需補充胺基酸及水份者經口服不能攝取營養及水份或手術前後營養補給</td></tr><tr><td>衛署藥製字第021883號</td><td>"信東" 胺美樂舒注射液</td><td>GLUTAMIC ACID L-、CYSTINE L-、L-SERINE、L-PROLINE、L-THREONINE、L…</td><td>注射劑</td><td>不能攝取適當食物之患者補助治療劑、蛋白質之消化吸收機能及合成利用障礙、嚴重創傷、火傷、骨折時蛋白質之補給、蛋白攝取減少之營養失調症</td></tr><tr><td>衛署藥製字第024029號</td><td>"中國化學" 蒙利安命賜源注射液</td><td>L-ARGININE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)…</td><td>注射劑</td><td>不能攝取適當食物之患者之補助治療劑、蛋白質消化吸收障礙及其合成利用障礙、嚴重創傷、火傷、骨折時蛋白質之補給、蛋白質攝取減少之營養失調症</td></tr><tr><td>衛署藥製字第025507號</td><td>胺美樂點滴注射液</td><td>L-PHENYLALANINE、L-HISTIDINE、L-ISOLEUCINE、L-TYROSINE、L-THREON…</td><td>注射劑</td><td>蛋白質、電解質及水分的補給</td></tr><tr><td>衛署藥製字第029276號</td><td>富安命注射液</td><td>L-ASPARTIC ACID、L-TYROSINE、L-ARGININE、L-TRYPTOPHAN、L-VALINE、…</td><td>注射劑</td><td>肝昏迷時氨基酸之補給</td></tr><tr><td>衛署藥製字第029417號</td><td>"濟生"達爾安命益注射液</td><td>L-TRYPTOPHAN、L-ALANINE、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L…</td><td>注射劑</td><td>蛋白質、電解質及水份之補給</td></tr><tr><td>衛署藥製字第029719號</td><td>礦安命注射液８．５％</td><td>L-PHENYLALANINE、LYSINE L- (HCL)、L-ALANINE、L-TRYPTOPHAN、MAGNE…</td><td>注射劑</td><td>不能攝取適當食物之患者之補助治療劑、蛋白質消化吸收障礙及合成利用障礙、手術前後嚴重創傷、火傷、骨折時蛋白質之補給、蛋白質攝取減少之營養失調症</td></tr><tr><td>衛署藥製字第031743號</td><td>安命生膠囊</td><td>RIBOFLAVIN (VIT B2)、CYSTEINE、THREONINE、METHIONINE DL-、PHENYL…</td><td>膠囊劑</td><td>營養補給</td></tr><tr><td>衛署藥製字第032498號</td><td>安命多－恩注射液</td><td>L-TRYPTOPHAN、L-CYSTEINE HCL MONOHYDRATE、L-ALANINE、L-PHENYLAL…</td><td>注射劑</td><td>蛋白質消化吸收障礙及其合成利用障礙、其他各種營養補給低蛋白血症</td></tr><tr><td>衛署藥製字第034067號</td><td>固力醣胺注射液</td><td>LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-TRYPTOPHAN、ASPARTATE M…</td><td>注射劑</td><td>手術前後的營養補給，不能經口攝取營養及水分的補給。</td></tr><tr><td>衛署藥製字第039687號</td><td>"南光" 立得命注射液５％</td><td>CYSTINE L-、GLUTAMIC ACID L-、L-SERINE、L-TYROSINE、L-ISOLEUCINE…</td><td>注射劑</td><td>手術前後之營養補給、低蛋白血症、消化道潰瘍、營養障礙之補給</td></tr><tr><td>衛署藥製字第042607號</td><td>保生安命注射液６％</td><td>L-PROLINE、L-THREONINE、L-ISOLEUCINE、L-HISTIDINE、N-ACETYL TYRO…</td><td>注射劑</td><td>用於嬰幼兒及早產兒之全靜脈營養注射、包括中央或周邊之給與、亦適用於不能攝取適當食物之患者之補助治療劑、蛋白質之消化吸收機能及合成利用障礙、嚴重創傷、火傷、骨折時蛋白質之補給、蛋白質…</td></tr><tr><td>衛署藥製字第045035號</td><td>"南光" 優安命注射液 3%</td><td>L-PHENYLALANINE、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-ASPART…</td><td>注射劑</td><td>手術前後之營養補給、低蛋白血症、消化道潰瘍、營養障礙之補給。</td></tr><tr><td>衛署藥製字第045310號</td><td>"台灣大塚" 安命保寧注射液 10% W/V</td><td>L-ALANINE、L-PHENYLALANINE、L- GLUTAMIC ACID、L-ASPARTIC ACID、L…</td><td>注射劑</td><td>低蛋白血症、低營養狀態、手術前後等的氨基酸補給。</td></tr><tr><td>衛署藥製字第049060號</td><td>愛普命膜衣錠</td><td>ALPHA-KETOVALINE CALCIUM SALT、L-THREONINE、ALPHA-HYDROXYMETHI…</td><td>膜衣錠</td><td>慢性腎不全時氨基酸之補給。</td></tr><tr><td>衛署藥輸字第018273號</td><td>吉多利錠</td><td>L-HISTIDINE、L-THREONINE、CALCIUM-3-METHYL-2-OXO-VALERATE、CALC…</td><td>膜衣錠</td><td>慢性腎不全時氨基酸之補給</td></tr><tr><td>衛署藥輸字第023218號</td><td>〝百特〞克里密絲輸注液　（N17G35E）</td><td>SODIUM CHLORIDE、MAGNESIUM CHLORIDE HEXAHYDRATE (EQ TO MAGNES…</td><td>注射劑</td><td>用於非經腸道營養，當腸無法吸收或吸收不良，經判斷為不可經腸道營養時使用。</td></tr><tr><td>衛署藥輸字第023224號</td><td>"百特" 克里密絲輸注液　（Ｎ９Ｇ１５Ｅ）</td><td>LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-PHENYLALANINE、L-HISTID…</td><td>注射劑</td><td>用於非經腸道營養，當腸無法吸收或吸收不良，經判斷為不可經腸道營養時使用。</td></tr><tr><td>衛署藥輸字第024180號</td><td>安敏芬5%輸注液</td><td>L-SERINE、L-ISOLEUCINE、L-HISTIDINE、L-PROLINE、L-THREONINE、TAUR…</td><td>注射劑</td><td>腸外營養補充劑。</td></tr><tr><td>衛署藥輸字第024270號</td><td>"百特" 歐諾美N7-1000E輸注乳液</td><td>L-ALANINE、L-TRYPTOPHAN、L-LEUCINE、L-HISTIDINE、L-ARGININE、L-TY…</td><td>注射劑</td><td>適用於成人及二歲以上孩童在無法或因有禁忌症而不適宜進食或使用口服腸道營養劑時之靜脈營養。</td></tr><tr><td>衛署藥輸字第024679號</td><td>“百特”歐諾美 N4-550E 輸注乳液</td><td>L-ISOLEUCINE、L-VALINE、L-GLYCINE、L-HISTIDINE、POTASSIUM CHLORI…</td><td>注射劑</td><td>適於成人及二歲以上孩童在無法或因有禁忌症而不適宜進食或使用口服腸道營養劑時之靜脈營養。</td></tr><tr><td>衛署藥輸字第025150號</td><td>斯莫克必恩周邊靜脈輸注液</td><td>SERINE、SERINE、ARGININE、SODIUM ACETATE (TRIHYDRATE)、ARGININE、…</td><td>注射劑</td><td>靜脈營養輸注，適用於無法由口腔進食或經腸道獲取足夠營養，或禁止由口腔及腸道進食之成年患者及2歲以上兒童。</td></tr><tr><td>衛署藥輸字第025179號</td><td>必富力得注射液</td><td>Thiamine chloride hydrochloride、L-TRYPTOPHAN、L-ALANINE、GLYCI…</td><td>注射劑</td><td>經口攝取不足、輕度的低蛋白血症、輕度的營養障礙、手術前後等狀態時的氨基酸、電解質、維生素B1及水分之營養補給。</td></tr><tr><td>衛署藥輸字第025203號</td><td>斯莫克必恩中心靜脈輸注液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、GLYCINE (E…</td><td>注射劑</td><td>靜脈營養輸注，適用於無法由口腔進食或經腸道獲取足夠營養，或禁止由口腔及腸道進食之成年患者及2歲以上兒童。</td></tr><tr><td>衛部藥製字第058130號</td><td>嘉安命-胺5%輸注液</td><td>L-PROLINE、L-THREONINE、L-VALINE、LYSINE L- HCL ( EQ TO L-LYSIN…</td><td>注射劑</td><td>腸外營養補充劑</td></tr><tr><td>衛部藥輸字第026388號</td><td>斯莫克必恩中心靜脈輸注液493毫升</td><td>MAGNESIUM SULPHATE HEPTAHYDRATE、L-LYSINE ACETATE、L-HISTIDINE…</td><td>注射劑</td><td>靜脈營養輸注，適用於無法由口腔進食或經腸道獲取足夠營養，或禁止由口腔及腸道進食之成年患者及2歲以上兒童。</td></tr><tr><td>衛部藥輸字第026393號</td><td>斯莫克必恩易福中心靜脈輸注液</td><td>GLUCOSE MONOHYDRATE、TRIGLYCERIDES MEDIUM CHAIN、L-LEUCINE、L-I…</td><td>注射劑</td><td>無法給予口服/腸道營養或口服/腸道營養不足或禁用時，適用於成人及2歲以上兒童病患的靜脈營養劑。</td></tr><tr><td>衛部藥輸字第027125號</td><td>安敏芬 15%輸注液</td><td>L-SERINE、L-ISOLEUCINE、L-VALINE、L-PHENYLALANINE、L-THREONINE、L…</td><td>注射劑</td><td>腸外營養補充劑。</td></tr><tr><td>衛部藥輸字第027257號</td><td>氨補膜衣錠</td><td>CALCIUM-DL-2-HYDROXY-4-(METHYL-THIO)-BUTYRATE、L-THREONINE、CA…</td><td>膜衣錠</td><td>慢性腎不全時氨基酸之補給。</td></tr><tr><td>衛部藥輸字第027610號</td><td>新每康G13%E輸注乳液</td><td>TAURINE (EQ TO AMINOETHYL SULFONIC ACID )、L-SERINE、L-CYSTEIN…</td><td>注射液劑</td><td>適用於早產新生兒在無法、不足或因有禁忌症而不適宜進食或使用腸道營養劑時之靜脈營養。</td></tr><tr><td>衛部藥輸字第027611號</td><td>新每康G16%E輸注乳液</td><td>CALCIUM CHLORIDE DIHYDRATE、L-CYSTEINE、L-SERINE、TAURINE (EQ T…</td><td>注射液劑</td><td>適用於足月新生兒和2歲以下的兒童在無法、不足或因有禁忌症而不適宜進食或使用腸道營養劑時之靜脈營養。</td></tr><tr><td>衛部藥輸字第027612號</td><td>新每康G19%E輸注乳液</td><td>REFINE SOYA + OLIVE OIL、L-PROLINE、L-THREONINE、CALCIUM CHLORI…</td><td>注射液劑</td><td>適用於2歲以上兒童和青少年在無法、不足或因有禁忌症而不適宜進食或使用腸道營養劑時之靜脈營養。</td></tr><tr><td>衛部藥輸字第028121號</td><td>"百特"歐立美N12E輸注乳液</td><td>L-TRYPTOPHAN、L-ALANINE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ T…</td><td>注射液劑</td><td>適用於成人及兩歲以上孩童在無法或因有禁忌症而不適宜進食或使用口服腸道營養劑時之靜脈營養。</td></tr><tr><td>衛部藥輸字第028122號</td><td>"百特"沛立美N4E輸注乳液</td><td>L-SERINE、CALCIUM CHLORIDE DIHYDRATE、SODIUM ACETATE (TRIHYDRA…</td><td>注射液劑</td><td>適用於成人及兩歲以上孩童在無法或因有禁忌症而不適宜進食或使用口服腸道營養劑時之靜脈營養。</td></tr><tr><td>衛部藥輸字第028197號</td><td>斯莫克必恩(升氮)中心靜脈輸注液</td><td>L-PROLINE、SODIUM GLYCEROPHOSPHATE ANHYDROUS、SODIUM ACETATE T…</td><td>注射劑</td><td>靜脈營養輸注，適用於無法由口腔進食或經腸道獲取足夠營養，或禁止由口腔及腸道進食之成年患者及2歲以上兒童。</td></tr><tr><td>衛部藥輸字第029001號</td><td>"百特"歐立美N9E輸注乳液</td><td>L-ISOLEUCINE、L-HISTIDINE、L-VALINE、SODIUM ACETATE (TRIHYDRATE…</td><td>注射液劑</td><td>適用於成人及兩歲以上孩童在無法或因有禁忌症而不適宜進食或使用口服腸道營養劑時之靜脈營養。</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（136 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第002049號</td><td>胺美樂糖衣片</td><td>L-HISTIDINE、L-VALINE、L-PHENYLALANINE、PYRIDOXINE HCL、RIBOFLAV…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007750號</td><td>胺美樂口服液</td><td>L-LEUCINE、PANTHENOL D- (EQ TO D-PANTHENOL)、L-TYROSINE、L-HIST…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第013121號</td><td>安命生膠囊</td><td>ARGININE、VALINE、ISOLEUCINE、THIAMINE HYDROCHLORIDE、GLUTAMIC A…</td><td>1990/09/10</td></tr><tr><td>內衛藥製字第013180號</td><td>安命生糖漿</td><td>SERINE、ISOLEUCINE、CYSTEINE、THIAMINE HYDROCHLORIDE、LEUCINE、LY…</td><td>1990/09/10</td></tr><tr><td>內衛藥輸字第000612號</td><td>扭立生ＳＡ注射液</td><td>LEUCINE、CYSTINE、SERINE、TYROSINE、SORBITOL、LYSINE、GLUTAMIC ACI…</td><td>1992/03/16</td></tr><tr><td>內衛藥輸字第000944號</td><td>樂力新注射劑</td><td>CHYMOTRYPSIN、TYROSINE</td><td>1988/09/05</td></tr><tr><td>衛署藥製字第006572號</td><td>永安命舒注射液</td><td>L-METHIONINE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOL…</td><td>2023/10/02</td></tr><tr><td>衛署藥製字第016400號</td><td>能安命注射液</td><td>L-SERINE、L-ISOLEUCINE、LYSINE HCL、XYLITOL、L-LEUCINE、L-THREONI…</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第024557號</td><td>"壽元"西力安命注射液</td><td>L-SERINE、XYLITOL、L-ISOLEUCINE、L-LEUCINE、HISTIDINE L- HCL (EQ…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第029297號</td><td>泛安命注射液</td><td>POTASSIUM PHOSPHATE ( eq to POTASSIUM PHOSPHATE DIBASIC)、L-V…</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第029426號</td><td>能安命注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、ARGININE H…</td><td>1990/07/11</td></tr><tr><td>衛署藥製字第031755號</td><td>安命生糖漿</td><td>RIBOFLAVIN (VIT B2)、THREONINE、METHIONINE DL-、CYSTEINE、PHENYL…</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第037714號</td><td>泰安命注射液１８％</td><td>L-VALINE、L-HISTIDINE、L-ISOLEUCINE、L-PROLINE、L-THREONINE、L-CY…</td><td>2013/10/03</td></tr><tr><td>衛署藥輸字第001612號</td><td>固力醣胺注射液</td><td>L-SERINE、L-VALINE、LYSINE HCL、XYLITOL、CYSTEINE L- HCL (EQ TO…</td><td>1988/03/02</td></tr><tr><td>衛署藥輸字第003698號</td><td>保體安民注射液</td><td>L-SERINE、NITROGEN、CYSTINE L-、SODIUM CITRATE (SODIUM CITRATE…</td><td>1988/04/02</td></tr><tr><td>衛署藥輸字第004172號</td><td>"協和" Ｌ-酪氨酸</td><td>L-TYROSINE</td><td>2023/04/19</td></tr><tr><td>衛署藥輸字第005301號</td><td>保體安民濃氨基酸注射液</td><td>L-PROLINE、L-THREONINE、L-TYROSINE、HISTIDINE L- HCL (EQ TO L-H…</td><td>1988/03/16</td></tr><tr><td>衛署藥輸字第006340號</td><td>"味之素" 乾酪氨酸</td><td>L-TYROSINE</td><td>2025/04/22</td></tr><tr><td>衛署藥輸字第007503號</td><td>（左）酪氨酸</td><td>L-TYROSINE</td><td>1988/03/16</td></tr><tr><td>衛署藥輸字第008053號</td><td>德泰安命注射液</td><td>CYSTINE L-、GLUTAMIC ACID L-、SODIUM CARBONATE MONOHYDRATE、SOR…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008101號</td><td>安命諾補樂注射液１０％</td><td>L-ORNITHINE  HCL、POTASSIUM ACETATE、GLYCINE (EQ TO AMINOACETI…</td><td>1989/12/29</td></tr><tr><td>衛署藥輸字第008102號</td><td>安命諾補樂注射液５％</td><td>L-TRYPTOPHAN、L-TYROSINE、L-ASPARTIC ACID、LYSINE L- HCL ( EQ T…</td><td>1989/12/29</td></tr><tr><td>衛署藥輸字第008103號</td><td>安命諾補樂注射液３％</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、L-ARGININE…</td><td>1991/09/05</td></tr><tr><td>衛署藥輸字第008362號</td><td>氨基酸電解質糖類點滴注射液</td><td>L-ARGININE、L-TYROSINE、L-ASPARTIC ACID、LYSINE L- HCL ( EQ TO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008419號</td><td>興得民１３注射液（添加電解質）</td><td>L-PROLINE、SODIUM METABISULFITE (SOD. PYROSULFITE)、L-THREONIN…</td><td>1988/07/29</td></tr><tr><td>衛署藥輸字第008420號</td><td>興得民１７注射液（未加電解質）</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、L-METHIONI…</td><td>1988/07/29</td></tr><tr><td>衛署藥輸字第008425號</td><td>興得民９注射液（添加電解質）</td><td>SODIUM CHLORIDE、L-PROLINE、L-ISOLEUCINE、L-THREONINE、SODIUM ME…</td><td>1988/07/29</td></tr><tr><td>衛署藥輸字第008431號</td><td>興得民９注射液（未加電解質）</td><td>LYSINE L- (HCL)、L-PHENYLALANINE、L-VALINE、L-ALANINE、L-TRYPTOP…</td><td>1988/07/29</td></tr><tr><td>衛署藥輸字第008432號</td><td>興得民１７注射液（添加電解質）</td><td>SODIUM CHLORIDE、SODIUM METABISULFITE (SOD. PYROSULFITE)、L-TH…</td><td>1988/07/29</td></tr><tr><td>衛署藥輸字第008477號</td><td>安美若胖得注射液２．５％</td><td>XYLITOL、L-HISTIDINE、L-ISOLEUCINE、L-LEUCINE、TYROSINE L-(N-ACE…</td><td>1997/11/22</td></tr><tr><td>衛署藥輸字第008479號</td><td>安美若胖得注射液</td><td>L-TRYPTOPHAN、L-ARGININE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ…</td><td>1997/11/22</td></tr><tr><td>衛署藥輸字第008480號</td><td>諾你健注射液</td><td>L-ASPARTIC ACID、METHIONINE DL-、L-HISTIDINE、L-VALINE、POTASSIU…</td><td>1997/11/22</td></tr><tr><td>衛署藥輸字第009068號</td><td>能使安寧注射液</td><td>L-VALINE、ASPARTATE SODIUM L-、L-PHENYLALANINE、L-LEUCINE、L-ALA…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009868號</td><td>扭立生Ｅ注射液</td><td>HISTIDINE、PHENYLALANINE、METHIONINE、GLYCINE (EQ TO AMINOACETI…</td><td>1992/03/16</td></tr><tr><td>衛署藥輸字第010147號</td><td>氨基樂酸注射液７％</td><td>LYSINE L- (ACETATE)、L-ARGININE、L-TYROSINE、L-PHENYLALANINE、L-…</td><td>1986/02/26</td></tr><tr><td>衛署藥輸字第010178號</td><td>合利胺基注射液</td><td>L-ASPARTIC ACID、L-ALANINE、L-TRYPTOPHAN、HISTIDINE L- HCL (EQ…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010402號</td><td>舒補胺基注射液</td><td>L-LEUCINE、HISTIDINE L- HCL (EQ TO L-HISTIDINE HYDROCHLORIDE)…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010729號</td><td>氨基樂酸注射液５％</td><td>L-PHENYLALANINE、L-ALANINE、L-TRYPTOPHAN、L-TYROSINE、L-ARGININE…</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第010755號</td><td>氨基樂注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、L-TRYPTOPH…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第010919號</td><td>汝得利賜－Ｓ注射液５％</td><td>L-LEUCINE、L-PHENYLALANINE、L-ISOLEUCINE、HISTIDINE L- HCL MONO…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第010920號</td><td>１２％喜加力安命－愛克注射液</td><td>L-SERINE、GLUTAMIC ACID L-、CYSTINE L-、L-THREONINE、L-PROLINE、L…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第010925號</td><td>３％喜加力安命－愛克注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、L-METHIONI…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第010936號</td><td>汝得利賜注射液１２％</td><td>L-PROLINE、L-THREONINE、HISTIDINE L- HCL MONOHYDRATE、L-ISOLEUC…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第011060號</td><td>氨基樂欣注射液５％</td><td>L-PHENYLALANINE、L-HISTIDINE、L-VALINE、L-TYROSINE、L-TRYPTOPHAN…</td><td>1988/06/08</td></tr><tr><td>衛署藥輸字第011061號</td><td>氨基樂欣注射液７％</td><td>L-PHENYLALANINE、L-ISOLEUCINE、L-TYROSINE、L-LEUCINE、L-THREONIN…</td><td>1989/05/15</td></tr><tr><td>衛署藥輸字第011062號</td><td>氨基樂欣注射液１０％</td><td>L-SERINE、L-ISOLEUCINE、L-TYROSINE、L-HISTIDINE、L-PROLINE、L-THR…</td><td>2013/01/03</td></tr><tr><td>衛署藥輸字第011152號</td><td>喜加力安命注射液１２％</td><td>L-VALINE、L-ASPARTIC ACID、L-ALANINE、HISTIDINE L- HCL (EQ TO L…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第011392號</td><td>多他命福注射液</td><td>LYSINE L-、SORBITOL、L-CYSTEINE、L-SERINE、GLUTAMIC ACID L-、POTA…</td><td>1990/01/16</td></tr><tr><td>衛署藥輸字第011399號</td><td>多他命足注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、NIACINAMID…</td><td>1990/01/09</td></tr><tr><td>衛署藥輸字第011503號</td><td>阿美諾愛克斯注射液</td><td>L-PROLINE、L-THREONINE、L-ISOLEUCINE、LYSINE HCL、L-LEUCINE、XYLI…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第011515號</td><td>阿美諾注射液</td><td>L-METHIONINE、ARGININE HCL L-、GLYCINE (EQ TO AMINOACETIC ACID…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第011738號</td><td>速利清注射液</td><td>ALANINE、PROLINE、VALINE、ARGININE、ISOLEUCINE、GLUTAMIC ACID、LYS…</td><td>1988/05/04</td></tr><tr><td>衛署藥輸字第011867號</td><td>多他命丙注射液</td><td>L-ISOLEUCINE、L-HISTIDINE、POTASSIUM PHOSPHATE MONOBASIC ANHYD…</td><td>1990/01/24</td></tr><tr><td>衛署藥輸字第011895號</td><td>愛樂定注射液</td><td>LYSINE L- (HCL)、L-LEUCINE、L-PHENYLALANINE、L-TYROSINE、CHLORID…</td><td>1988/01/18</td></tr><tr><td>衛署藥輸字第012002號</td><td>喜加力安命－愛克注射液１２％</td><td>GLUTAMIC ACID L-、CYSTINE L-、L-SERINE、XYLITOL、L-ISOLEUCINE、HI…</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012004號</td><td>喜加力安命注射液１２％</td><td>L-SERINE、CYSTINE L-、GLUTAMIC ACID L-、L-PROLINE、L-THREONINE、L…</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012005號</td><td>喜加力安命－愛克注射液３％</td><td>L-SERINE、GLUTAMIC ACID L-、CYSTINE L-、L-ISOLEUCINE、L-LEUCINE、…</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012705號</td><td>小兒專用安命諾補樂注射液</td><td>L-ARGININE、L-ASPARTIC ACID、POTASSIUM HYDROXIDE、L-TRYPTOPHAN、…</td><td>1991/05/23</td></tr><tr><td>衛署藥輸字第012920號</td><td>氨基樂欣注射液３．５％</td><td>SODIUM CHLORIDE、L-SERINE、MAGNESIUM ACETATE、L-VALINE、L-PHENYL…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014488號</td><td>舒樂命注射液</td><td>L-ISOLEUCINE、L-TYROSINE、L-HISTIDINE、L-PHENYLALANINE、L-THREON…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第014680號</td><td>保甘注射液</td><td>PHENYLALANINE、HISTIDINE、LIVER HYDROLYSATE、THREONINE、METHIONI…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第014783號</td><td>氨基樂酸注射液７％</td><td>POTASSIUM METABISULFITE、L-METHIONINE、GLYCINE (EQ TO AMINOACE…</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第015075號</td><td>安命納精注射液５％</td><td>L-METHIONINE、SODIUM HYDROXIDE、GLYCINE (EQ TO AMINOACETIC ACI…</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015144號</td><td>郝士曼安命納精注射液３％</td><td>ASPARAGINE L- MONOHYDRATE (EQ TO ASPARAGINE H2O L- )、GLUTAMI…</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015520號</td><td>氨基樂欣注射液３．５％</td><td>L-VALINE、L-PHENYLALANINE、ACETIC ACID GLACIAL( eq to  GLACIAL…</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第016133號</td><td>愛樂定注射液</td><td>L-VALINE、L-ISOLEUCINE、L-HISTIDINE、L-THREONINE、CYSTINE L-、SOD…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016300號</td><td>固力醣胺注射液</td><td>SODIUM GLUTAMATE L-、L-LEUCINE、LYSINE HCL、L-ISOLEUCINE、L-PROL…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第016334號</td><td>（左）酪氨酸</td><td>L-TYROSINE</td><td>2001/09/21</td></tr><tr><td>衛署藥輸字第016337號</td><td>保體安民注射液</td><td>L-ASPARTIC ACID、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-PHENYL…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016342號</td><td>保體安民濃氨基酸注射液</td><td>XYLITOL、L-ISOLEUCINE、L-PROLINE、L-THREONINE、ELECTROLYTE、L-SER…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016406號</td><td>郝士曼安命酸注射液１０％</td><td>SODIUM HYDROXIDE、L-METHIONINE、ORNITHINE L-、L-TRYPTOPHAN、GLYC…</td><td>1994/03/24</td></tr><tr><td>衛署藥輸字第016408號</td><td>郝士曼安命酸注射液１５％</td><td>L-ISOLEUCINE、L-TYROSINE、N-ACETYL TYROSINE L-、L-HISTIDINE、ASP…</td><td>1994/03/24</td></tr><tr><td>衛署藥輸字第016433號</td><td>喜加力安命－愛克注射液３％</td><td>CYSTINE L-、GLUTAMIC ACID L-、L-SERINE、HISTIDINE L- HCL (EQ TO…</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第016435號</td><td>喜加力安命注射液１２％</td><td>L-SERINE、GLUTAMIC ACID L-、CYSTINE L-、L-THREONINE、L-PROLINE、L…</td><td>1994/07/27</td></tr><tr><td>衛署藥輸字第016437號</td><td>喜加力安命－愛克注射液１２％</td><td>XYLITOL、L-ISOLEUCINE、LYSINE HCL、L-VALINE、L-THREONINE、L-PROLI…</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第016515號</td><td>速利清注射液</td><td>ALANINE、PROLINE、ISOLEUCINE、ARGININE、VALINE、GLUTAMIC ACID、LYS…</td><td>1991/11/22</td></tr><tr><td>衛署藥輸字第016594號</td><td>氨基樂欣注射液７％</td><td>LYSINE、LEUCINE、TYROSINE、SODIUM HYDROSULFITE (SODIUM DITHIONI…</td><td>2013/01/03</td></tr><tr><td>衛署藥輸字第016597號</td><td>興得民１３注射液（添加電解質）</td><td>L-HISTIDINE、L-LEUCINE、POTASSIUM PHOSPHATE ( eq to POTASSIUM…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016598號</td><td>興得民９注射液（添加電解質）</td><td>L-PHENYLALANINE、LYSINE L- (HCL)、L-VALINE、L-TRYPTOPHAN、L-ALAN…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016599號</td><td>興得民１７注射液（添加電解質）</td><td>SODIUM CHLORIDE、L-THREONINE、SODIUM METABISULFITE (SOD. PYROS…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016600號</td><td>興得民９注射液（未加電解質）</td><td>L-ISOLEUCINE、L-HISTIDINE、L-LEUCINE、L-THREONINE、L-PROLINE、SOD…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016601號</td><td>興得民１７注射液（未加電解質）</td><td>L-THREONINE、L-PROLINE、SODIUM METABISULFITE (SOD. PYROSULFITE…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016757號</td><td>氨基樂欣注射液５％</td><td>SERINE、VALINE、LEUCINE、LYSINE、TYROSINE、ARGININE、ISOLEUCINE、PR…</td><td>2013/01/03</td></tr><tr><td>衛署藥輸字第016877號</td><td>氨基樂欣嬰幼兒配方靜脈注射液７％Ｗ/Ｖ</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、PHENYLALAN…</td><td>2013/01/03</td></tr><tr><td>衛署藥輸字第017174號</td><td>氨基樂欣嬰幼兒配方１０％注射液</td><td>PROLINE、ISOLEUCINE、ALANINE、LYSINE ACETATE、SODIUM HYDROSULFIT…</td><td>2013/11/25</td></tr><tr><td>衛署藥輸字第017439號</td><td>多他命丙注射液</td><td>L-TYROSINE、L-TRYPTOPHAN、NIACINAMIDE (NICOTINAMIDE)、L-ASPARTI…</td><td>2000/09/20</td></tr><tr><td>衛署藥輸字第017440號</td><td>多他命福注射液</td><td>L-THREONINE、ASCORBIC ACID (VIT C)、L-PROLINE、L-HISTIDINE、POTA…</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第017442號</td><td>多他命足注射液</td><td>POTASSIUM PHOSPHATE MONOBASIC ANHYDROUS、L-LEUCINE、L-HISTIDIN…</td><td>2006/05/23</td></tr><tr><td>衛署藥輸字第017465號</td><td>安命諾補樂注射液１０％</td><td>SODIUM ACETATE TRIHYDRATE (EQ TO SODIUM ACETATE 3H2O )、SORBI…</td><td>1990/10/11</td></tr><tr><td>衛署藥輸字第017466號</td><td>安命諾補樂注射液５％</td><td>ASPARAGINE L- MONOHYDRATE (EQ TO ASPARAGINE H2O L- )、L-THREO…</td><td>1990/10/11</td></tr><tr><td>衛署藥輸字第017726號</td><td>德泰安命注射液</td><td>L-ARGININE、L-TYROSINE、L-TRYPTOPHAN、MAGNESIUM CHLORIDE、PYRIDO…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017986號</td><td>安命諾補樂－益注射液１０％</td><td>L-ALANINE、L-TYROSINE、L-PHENYLALANINE、LYSINE L- (HCL)、MAGNESI…</td><td>1991/03/20</td></tr><tr><td>衛署藥輸字第018172號</td><td>小兒專用安命諾補樂注射液</td><td>L-CYSTEINE HCL MONOHYDRATE、MAGNESIUM ACETATE TETRAHYDRATE、L-…</td><td>1999/01/29</td></tr><tr><td>衛署藥輸字第018199號</td><td>安命諾補樂注射液１０％</td><td>POTASSIUM ACETATE、L-METHIONINE、L-ORNITHINE  HCL、L-TRYPTOPHAN…</td><td>2014/04/28</td></tr><tr><td>衛署藥輸字第018200號</td><td>安命諾補樂注射液５％</td><td>L-CYSTEINE HCL MONOHYDRATE、L-ALANINE、L-ASPARTIC ACID、LYSINE…</td><td>2014/04/28</td></tr><tr><td>衛署藥輸字第018384號</td><td>安命諾補樂含電解質注射液-10％</td><td>L-THREONINE、MALIC ACID L-、L-PROLINE、L-CYSTEINE、SODIUM ACETAT…</td><td>2016/09/08</td></tr><tr><td>衛署藥輸字第018501號</td><td>安命保寧注射液１０％Ｗ/Ｖ</td><td>L-THREONINE、L-PROLINE、L-VALINE、L-HISTIDINE、L-ISOLEUCINE、L-CY…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第018515號</td><td>安命諾補樂注射液３％</td><td>L-ARGININE、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-ORNITHINE…</td><td>2014/04/28</td></tr><tr><td>衛署藥輸字第018609號</td><td>安米諾　胖得Ｎ６％</td><td>L-SERINE、ARGININE、MALIC ACID L-、L-PROLINE、L-ISOLEUCINE、L-THR…</td><td>2002/10/08</td></tr><tr><td>衛署藥輸字第020508號</td><td>喜加力安命注射液１２％</td><td>L-SERINE、CYSTINE L-、GLUTAMIC ACID L-、L-ISOLEUCINE、LYSINE HCL…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第020814號</td><td>喜加力安命－愛克注射液３％</td><td>L-SERINE、GLUTAMIC ACID L-、CYSTINE L-、XYLITOL、L-ISOLEUCINE、L-…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第020842號</td><td>利壽補樂命靜脈注射液</td><td>L-METHIONINE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOL…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第021614號</td><td>乾酪氨酸</td><td>TYROSINE</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第021967號</td><td>胺美卡立克注射液</td><td>L-METHIONINE、L-TRYPTOPHAN、ARGININE HCL L-、GLYCINE (EQ TO AMI…</td><td>2015/11/04</td></tr><tr><td>衛署藥輸字第022300號</td><td>安米諾靜脈輸注液％　Ｗ/Ｖ</td><td>ORNITHINE L- ASPARTATE L-、L-SERINE、ARGININE、L-PROLINE、L-THRE…</td><td>2002/10/08</td></tr><tr><td>衛署藥輸字第022301號</td><td>新安米諾靜脈輸注液１０％　Ｗ/Ｖ</td><td>L-ALANINE、TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、L-TRYP…</td><td>2002/10/08</td></tr><tr><td>衛署藥輸字第022915號</td><td>〝百特〞ＰＤ４　１．１％　胺基酸腹膜透析液</td><td>L-TRYPTOPHAN、L-ALANINE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ T…</td><td>2022/06/21</td></tr><tr><td>衛署藥輸字第022996號</td><td>安命諾補樂液　１０％</td><td>HISTIDINE、METHIONINE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO…</td><td>2017/04/14</td></tr><tr><td>衛署藥輸字第022998號</td><td>安命諾補樂液－１５％</td><td>ARGININE、TYROSINE、LEUCINE、GLUTAMIC ACID、PROLINE、ALANINE、SERI…</td><td>2014/04/28</td></tr><tr><td>衛署藥輸字第023116號</td><td>安命諾補樂含電解質注射液５％</td><td>GLUTAMIC ACID L-、ASPARAGINE L- MONOHYDRATE (EQ TO ASPARAGINE…</td><td>2017/04/14</td></tr><tr><td>衛署藥輸字第023170號</td><td>百源雙利－３號</td><td>L-METHIONINE、POTASSIUM ACETATE、GLYCINE (EQ TO AMINOACETIC AC…</td><td>2004/07/07</td></tr><tr><td>衛署藥輸字第023171號</td><td>百源雙利－１號</td><td>ZINC SULFATE、L-THREONINE、GLUCOSE、L-PROLINE、L-VALINE、L-HISTID…</td><td>2004/07/07</td></tr><tr><td>衛署藥輸字第023172號</td><td>百源雙利－２號</td><td>L-ASPARTIC ACID、L-TRYPTOPHAN、L-ALANINE、L-ARGININE、L-TYROSINE…</td><td>2004/07/07</td></tr><tr><td>衛署藥輸字第023210號</td><td>"百特" 克里密絲輸注液　（Ｎ１４Ｇ３０Ｅ）</td><td>SODIUM CHLORIDE、L-SERINE、LYSINE L-、MAGNESIUM CHLORIDE HEXAHY…</td><td>2022/06/21</td></tr><tr><td>衛署藥輸字第023217號</td><td>"百特" 克里密絲輸注液　（Ｎ９Ｇ２０Ｅ）</td><td>L-VALINE、POTASSIUM PHOSPHATE ( eq to POTASSIUM PHOSPHATE DIB…</td><td>2012/12/20</td></tr><tr><td>衛署藥輸字第023297號</td><td>安命優欣</td><td>L-ASPARTIC ACID、L-TYROSINE、L-ARGININE、L-TRYPTOPHAN、L-VALINE、…</td><td>2004/07/07</td></tr><tr><td>衛署藥輸字第023390號</td><td>"百特" 克里密絲輸注液 (N14G30)</td><td>L-HISTIDINE、L-VALINE、L-LEUCINE、L-TYROSINE、L-PROLINE、GLUCOSE、…</td><td>2019/04/02</td></tr><tr><td>衛署藥輸字第023878號</td><td>氨基富液</td><td>L- GLUTAMIC ACID、L-PHENYLALANINE、L-ALANINE、L-LEUCINE、LYSINE…</td><td>2021/03/26</td></tr><tr><td>衛署藥輸字第024153號</td><td>"百特" 森他命17不含電解質輸注液</td><td>L-PHENYLALANINE、L-HISTIDINE、AMINO ACETIC ACID、L-VALINE、L-TRY…</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第024159號</td><td>"百特" 瑞安命(胺基酸)注射劑</td><td>LYSINE、TYROSINE、LEUCINE、ALANINE、ISOLEUCINE、PROLINE、SERINE、VA…</td><td>2012/12/20</td></tr><tr><td>衛署藥輸字第024179號</td><td>安敏芬10%輸注液</td><td>L-TRYPTOPHAN、L-ALANINE、L-TYROSINE、L-VALINE、L-HISTIDINE、L-PHE…</td><td>2026/04/09</td></tr><tr><td>衛署藥輸字第024203號</td><td>"百特" 森他命14不含電解質輸注液</td><td>LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-ALANINE、L-TRYPTOPHAN、L…</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第024219號</td><td>"百特"  1.1% 胺基酸腹膜透析液</td><td>L-ISOLEUCINE、L-LEUCINE、L-HISTIDINE、L-PROLINE、L-THREONINE、SOD…</td><td>2026/05/22</td></tr><tr><td>衛署藥輸字第024271號</td><td>"百特" 歐諾美 N6-900 E 輸注乳液</td><td>L-SERINE、MAGNESIUM CHLORIDE HEXAHYDRATE (EQ TO MAGNESIUM CHL…</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第024313號</td><td>"百特"歐諾美 N5-800E輸注乳液</td><td>SODIUM GLYCEROPHOSPHATE 5H2O、L-SERINE、LYSINE L-、L-PROLINE、L-…</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第024319號</td><td>卡比敏安10%輸注液</td><td>L-ALANINE、L-TRYPTOPHAN、GLYCINE (EQ TO AMINOACETIC ACID)(EQ T…</td><td>2010/11/22</td></tr><tr><td>衛署藥輸字第024329號</td><td>速立恩中心靜脈輸注液</td><td>ZINC SULFATE 7H2O、CALCIUM CHLORIDE DIHYDRATE、LEUCINE、TYROSIN…</td><td>2022/07/07</td></tr><tr><td>衛署藥輸字第024336號</td><td>卡比敏安5%輸注液</td><td>L-ISOLEUCINE、L-THREONINE、L-PROLINE、L-LEUCINE、L-HISTIDINE、L-P…</td><td>2010/11/22</td></tr><tr><td>衛署藥輸字第024338號</td><td>速立恩周邊靜脈輸注液</td><td>L-PHENYLALANINE、L-ALANINE、L-TYROSINE、LYSINE ACETATE、L-ARGINI…</td><td>2022/07/07</td></tr><tr><td>衛署藥輸字第024542號</td><td>速立恩易孚中心靜脈輸注液</td><td>HISTIDINE、THREONINE、TRYPTOPHAN、GLYCINE (EQ TO AMINOACETIC AC…</td><td>2022/07/07</td></tr><tr><td>衛署藥輸字第025172號</td><td>安命諾得含電解質輸注液5%</td><td>PROLINE、LYSINE HCL、ALANINE、VALINE、SODIUM CHLORIDE、ISOLEUCINE…</td><td></td></tr><tr><td>衛署藥輸字第025173號</td><td>安命諾得輸注液10%</td><td>LEUCINE、SERINE、TYROSINE、GLUTAMIC ACID、PROLINE、ARGININE、VALIN…</td><td></td></tr><tr><td>衛署藥輸字第025174號</td><td>安命諾得含電解質輸注液10%</td><td>SODIUM HYDROXIDE、PHENYLALANINE、GLYCINE (EQ TO AMINOACETIC AC…</td><td></td></tr><tr><td>衛署藥輸字第025708號</td><td>新派瑞恩12%糖注射液</td><td>L-LYSINE ACETATE、Zinc sulfate hydrate、L-VALINE、L-HISTIDINE、L…</td><td>2021/03/30</td></tr><tr><td>衛署藥輸字第025902號</td><td>新派瑞恩17.5%糖注射液</td><td>L-LYSINE ACETATE、L-LEUCINE、RIBOFLAVIN PHOSPHATE SODIUM、GLUCO…</td><td>2021/03/24</td></tr><tr><td>衛部藥輸字第027780號</td><td>安敏若優周邊靜脈輸注液</td><td>L-THREONINE、L-PROLINE、GLUCOSE MONOHYDRATE、SODIUM ACETATE (TR…</td><td>2025/10/09</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**備註**：純 L-Tyrosine 原料藥許可證均已註銷，但含有 tyrosine kinase 抑制劑的藥品 (如英可欣、杰百康) 仍有有效許可證。

---

## 安全性資訊

### 藥物交互作用 (DDI)

**根據 DDinter 資料庫：無已知重大藥物交互作用**

Tyrosine 作為天然胺基酸，整體安全性良好。

### 使用注意事項

1. **甲狀腺疾病患者**：補充 tyrosine 可能影響甲狀腺激素合成
2. **使用 MAO 抑制劑者**：理論上可能增加酪胺反應風險
3. **苯酮尿症 (PKU) 患者**：phenylalanine 代謝異常，tyrosine 補充需謹慎評估
4. **高劑量使用**：可能出現腸胃不適、頭痛、疲勞

### 已知副作用

- 一般耐受性良好
- 偶見：噁心、頭痛、疲勞、心悸
- 高劑量可能影響血壓

---

## 結論

### 整體評估

Tyrosine 作為甲狀腺激素和兒茶酚胺的生物合成前驅物，其在甲狀腺相關疾病的預測具有明確的生化基礎。對於 POTS 和青光眼的預測則需要更多直接證據。

### 建議

1. **甲狀腺功能異常相關研究** - 值得進一步探索，但需注意可能加重甲亢症狀
2. **POTS 相關應用** - 可考慮小規模探索性研究，已有 AMPT 相關研究基礎
3. **營養補充層面** - 對於 tyrosine 缺乏或需求增加的情況，可作為輔助治療考量

### 證據等級

| 類別 | 評級 |
|------|------|
| 預測可信度 | 中至高 (甲狀腺相關)；中等 (其他) |
| 臨床證據 | 中等 (有間接試驗) |
| 安全性顧慮 | 低 (天然胺基酸) |
| 老藥新用潛力 | 中等 |

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 知識圖譜、PubMed、ClinicalTrials.gov、台灣 FDA*

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

