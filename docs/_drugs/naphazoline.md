---
layout: default
title: Naphazoline
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline 藥師筆記

## 一句話總結

Naphazoline 是一種 alpha 腎上腺素受體致效劑，主要用於鼻塞和眼部充血，TxGNN 預測其對毛髮相關疾病（如禿髮症）和青光眼有治療潛力，但缺乏臨床證據支持這些新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Naphazoline（萘唑啉） |
| DrugBank ID | DB06711 |
| 台灣商品名 | 噴速點鼻液、各類眼藥水 |
| 原核准適應症 | 過敏性鼻炎、鼻塞、結膜炎、眼充血 |
| 預測新適應症 | 頭皮毛髮稀疏症、先天性毛髮稀疏症、瀰漫性圓禿、禿髮症、原發性遺傳性青光眼、開角型青光眼 |
| 最高預測分數 | 0.9983（頭皮毛髮稀疏症） |
| 證據等級 | L5（僅預測） |

---

## 為什麼這個預測合理？

### 藥理機轉分析

Naphazoline 是一種 alpha-1 和 alpha-2 腎上腺素受體致效劑，主要作用是血管收縮。其機轉與預測適應症的關聯：

1. **毛髮相關疾病**（TxGNN Score: 0.9983-0.9976）
   - 包括頭皮毛髮稀疏症、禿髮症等
   - 血管收縮劑通常不利於毛髮生長（減少血流供應）
   - 與已知促進毛髮生長的血管擴張劑（如 minoxidil）機轉相反
   - **預測合理性低**

2. **青光眼**（TxGNN Score: 0.9962-0.9959）
   - Alpha 腎上腺素致效劑可減少房水生成
   - 但 Naphazoline 主要用於短期局部血管收縮
   - 眼科用 alpha 致效劑（如 brimonidine）才是青光眼治療選擇
   - Naphazoline 可能加重某些類型青光眼

---

## 臨床試驗證據

| 疾病 | 臨床試驗數量 | 最高期別 | 證據等級 |
|------|-------------|---------|---------|
| 頭皮毛髮稀疏症 | 0 | - | L5 |
| 禿髮症 | 0 | - | L5 |
| 開角型青光眼 | 0 | - | L5 |

**結論：目前無任何預測適應症進入臨床試驗階段。**

---

## 文獻證據

### 開角型青光眼相關文獻

| PMID | 標題 | 年份 | 相關性 |
|------|------|------|--------|
| 1295525 | Effect of topical corticosteroids on laser-induced peripheral anterior synechiae | 1992 | 間接相關（雷射治療後藥物使用） |

**文獻評估**：此文獻並非直接研究 Naphazoline 用於青光眼治療，僅為研究雷射小樑整形術後的藥物使用。Naphazoline 與青光眼治療的直接證據不足。

---

## 台灣上市資訊

### 鼻用製劑

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Naphazoline 的不重複許可證共 **184 張**：有效單方 6 張、有效複方 50 張、已註銷 128 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（6 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第003941號 | 拿必樂點眼液 | 點眼液劑 | 綠洲化學工業有限公司 | 2028/05/24 | 暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅。 |
| 衛署藥製字第043543號 | "派頓"舒明點眼液 | 點眼液劑 | 臺灣派頓化學製藥股份有限公司 | 2030/02/18 | 暫時緩解因輕微眼部刺激所引起之不適或眼睛紅。 |
| 衛部藥輸字第026125號 | 鹽酸萘甲嘧唑啉 | （粉） | 宣泓貿易有限公司 | 2028/08/22 | 交感神經藥(血管收縮藥)。 |
| 衛部藥輸字第026457號 | 硝酸萘甲嘧唑啉 | （粉） | 宣泓貿易有限公司 | 2029/11/24 | 血管收縮劑 |
| 衛部藥輸字第028360號 | 萘甲嘧唑啉鹽酸鹽 | （粉） | 台灣荃新股份有限公司 | 2027/08/15 | 類交感神經藥；血管收縮藥。 |
| 衛部藥輸字第029140號 | 萘甲嘧唑啉鹽酸鹽 | （粉） | 宣泓貿易有限公司 | 2031/04/24 | 類交感神經藥；血管收縮藥 |

<details><summary><strong>有效・複方（適應症屬整個複方，不是本藥單獨的適應症）</strong>（50 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>劑型</th><th>核准適應症</th></tr></thead><tbody><tr><td>內衛藥製字第012086號</td><td>"人生" 噴速點鼻液外用</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>外用液劑</td><td>急慢性鼻炎、過敏性鼻炎、鼻蓄膿症</td></tr><tr><td>衛署藥製字第001153號</td><td>噴通點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>因感冒而引起之鼻塞、鼻炎、肥厚性鼻炎等所引起之鼻充血</td></tr><tr><td>衛署藥製字第001601號</td><td>爽通鼻劑</td><td>TRIPELENNAMINE HCL、NAPHAZOLINE NITRATE</td><td>點鼻液劑</td><td>過敏性鼻炎、及由感冒過敏所引起之鼻塞、鼻充血</td></tr><tr><td>衛署藥製字第003994號</td><td>可恩點眼液</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>點眼液劑</td><td>眼科：角膜炎、眼睛疲勞、眼充血、結膜炎</td></tr><tr><td>衛署藥製字第013438號</td><td>"成大"華鼻露液</td><td>NAPHAZOLINE NITRATE、CHLORPHENIRAMINE MALEATE</td><td>外用液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀</td></tr><tr><td>衛署藥製字第014320號</td><td>"派頓"浠樂通點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>點鼻液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀。</td></tr><tr><td>衛署藥製字第015762號</td><td>嘉舒樂噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>鼻塞、鼻充血、鼻竇炎、過敏性鼻炎</td></tr><tr><td>衛署藥製字第016222號</td><td>"溫士頓"舒鼻喜噴鼻液</td><td>DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL、PROCAINE HCL</td><td>鼻用噴液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎及流鼻水、鼻塞、鼻出血</td></tr><tr><td>衛署藥製字第019585號</td><td>"長安"汎鼻寧噴劑</td><td>DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL、PROCAINE HCL</td><td>鼻用氣化噴霧劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎（鼻塞、流鼻水）鼻出血</td></tr><tr><td>衛署藥製字第019904號</td><td>"溫士頓"溫美眼眼藥水</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>點眼液劑</td><td>角膜炎、角膜潰瘍和浸潤、手術創傷和手術後之角膜混濁、角膜異物引起之角膜障害、角膜上皮剝離、腺病性角膜炎、眼充血、鼻淚管閉塞</td></tr><tr><td>衛署藥製字第020501號</td><td>"艾力特" 佑鼻噴霧液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>鼻用噴液劑</td><td>急、慢性副鼻腔炎、肥厚性鼻炎、急性鼻炎、過敏性鼻炎、感冒所引起之鼻塞、充血及上呼吸道之發炎症狀</td></tr><tr><td>衛署藥製字第021719號</td><td>"尼斯可"噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、CHLORPHENIRAMINE MALEATE、NAPHAZOLIN…</td><td>鼻用噴液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀</td></tr><tr><td>衛署藥製字第022488號</td><td>"派頓"保麗晶眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅、眼睛疲勞</td></tr><tr><td>衛署藥製字第022515號</td><td>"派頓" 晶潤 眼藥水</td><td>NAPHAZOLINE HCL、VITAMIN A、CHONDROITIN SULFATE SODIUM (EQ TO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛疲勞</td></tr><tr><td>衛署藥製字第023380號</td><td>"健康"宜鼻噴鼻液</td><td>NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL、PROCAINE HCL</td><td>鼻用噴液劑</td><td>急慢性鼻炎、過敏性鼻炎、副鼻腔炎、鼻塞、鼻充血</td></tr><tr><td>衛署藥製字第025931號</td><td>"成大" 愛鼻爽點鼻液</td><td>DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL、PROCAINE HCL</td><td>外用液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎所引起之鼻塞、流鼻水、鼻出血</td></tr><tr><td>衛署藥製字第027556號</td><td>噴愈好外用液</td><td>DIBUCAINE HCL、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>外用液劑</td><td>昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢。</td></tr><tr><td>衛署藥製字第032148號</td><td>寧疤寧黑圓圈噴鼻劑</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>點鼻液劑</td><td>過敏性鼻炎、鼻塞</td></tr><tr><td>衛署藥製字第032860號</td><td>鼻通噴液劑</td><td>NAPHAZOLINE HCL、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、CHL…</td><td>點鼻液劑</td><td>鼻塞、流鼻水，打噴嚏．</td></tr><tr><td>衛署藥製字第033252號</td><td>"明大" 鼻爽噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>外用液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀。</td></tr><tr><td>衛署藥製字第033483號</td><td>"大豐"鼻速通噴鼻液</td><td>BENZETHONIUM CHLORIDE、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEA…</td><td>鼻用噴液劑</td><td>緩解過敏性鼻炎、枯草熱所引起之相關症狀（流鼻水，鼻塞，打噴嚏）</td></tr><tr><td>衛署藥製字第038302號</td><td>"福元"鼻舒通噴鼻液</td><td>NAPHAZOLINE NITRATE、CHLORPHENIRAMINE MALEATE</td><td>外用液劑</td><td>鼻炎、副鼻腔炎、上呼吸道炎、過敏性鼻液、鼻塞</td></tr><tr><td>衛署藥製字第039047號</td><td>"近江兄弟"鼻立通噴液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀</td></tr><tr><td>衛署藥製字第040816號</td><td>"近江兄弟" 白藥水</td><td>DIBUCAINE HCL、NAPHAZOLINE HCL、BENZALKONIUM CHLORIDE、CHLORPHE…</td><td>外用液劑</td><td>蟲咬、搔癢、擦傷、刀傷、手指之殺菌、消毒。</td></tr><tr><td>衛署藥製字第041371號</td><td>甕鼻寧點鼻液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>點鼻液劑</td><td>鼻炎、副鼻腔炎、上呼吸氣道炎、鼻充血、鼻塞。</td></tr><tr><td>衛署藥製字第043457號</td><td>"派頓"保滴明點眼液</td><td>NAPHAZOLINE HCL、ZINC SULFATE</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅及因眼睛乾澀所引起灼熱感與刺激感。</td></tr><tr><td>衛署藥製字第043489號</td><td>"約克" 舒鼻爽噴鼻液</td><td>PROCAINE HCL、DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎所引起之流鼻水、鼻塞及鼻出血。</td></tr><tr><td>衛署藥製字第046987號</td><td>"中美" 膚諾痛外用液</td><td>NAPHAZOLINE HCL、DIBUCAINE HCL、BENZETHONIUM CHLORIDE、CHLORPHE…</td><td>外用液劑</td><td>傷口消毒、昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢，及暫時緩解皮膚搔癢。</td></tr><tr><td>衛署藥製字第049759號</td><td>“中美”鼻舒康噴鼻液</td><td>PROCAINE HCL、NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL</td><td>鼻用噴液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎所引起之流鼻水、鼻塞及鼻出血。</td></tr><tr><td>衛署藥製字第052298號</td><td>傷寧外用殺菌消毒液</td><td>NAPHAZOLINE HCL、DIBUCAINE HCL、CHLORPHENIRAMINE MALEATE、BENZA…</td><td>外用液劑</td><td>蟲咬、搔癢、擦傷、刀傷、手指之殺菌、消毒。</td></tr><tr><td>衛署藥製字第055989號</td><td>立明點眼液</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>點眼液劑</td><td>角膜炎、眼睛疲勞、眼充血、結膜炎。</td></tr><tr><td>衛署藥輸字第018605號</td><td>第一眼藥水</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、ALLANTOIN、CHONDROIT…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第020997號</td><td>獅之施美露眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM L- (eq to POTASSIUM L-ASPARTAT…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛疲勞</td></tr><tr><td>衛署藥輸字第023384號</td><td>e視界－５０點眼液</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第023466號</td><td>樂敦維他眼藥水</td><td>CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL、ASPARTATE POTASSIUM…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞</td></tr><tr><td>衛署藥輸字第024073號</td><td>"佐藤" 視朗點眼液</td><td>DIPOTASSIUM GLYCYRRHIZINATE、PYRIDOXINE HCL、CYANOCOBALAMIN (V…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激 所引起之不適、眼睛紅、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第024505號</td><td>視安達琪眼藥水</td><td>NEOSTIGMINE METHYLSULFATE、NAPHAZOLINE HCL、ALLANTOIN、DL-CHLOR…</td><td>點眼液劑</td><td>眼睛疲勞、暫時緩解因輕微眼部刺激所引起的不適或眼睛紅、眼睛癢。</td></tr><tr><td>衛署藥輸字第024871號</td><td>牛津艾露比眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、CYANOCOBALAMIN (VIT…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適，或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第024908號</td><td>雪之元噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、LIDOCAINE</td><td>鼻用噴液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀。</td></tr><tr><td>衛署藥輸字第025097號</td><td>視安眼藥水</td><td>CHLORPHENIRAMINE MALEATE、CHONDROITIN SULFATE SODIUM (EQ TO S…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起的不適或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025301號</td><td>“佐藤”視敏寧點眼液</td><td>ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM POTASSIUM…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025638號</td><td>日岩艾眼舒眼藥水</td><td>CHLORPHENIRAMINE MALEATE、CYANOCOBALAMIN (VIT B12)、NAPHAZOLIN…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適，或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025666號</td><td>詩披雅眼藥水</td><td>CHLORPHENIRAMINE MALEATE、TAURINE (EQ TO AMINOETHYL SULFONIC…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025668號</td><td>睛亮點眼液</td><td>PANTHENOL、NAPHAZOLINE HYDROCHLORIDE、AMINOCAPROIC ACID EPSILO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛疲勞、眼睛癢。</td></tr><tr><td>衛部藥製字第060516號</td><td>潔淨膚外用殺菌消毒液</td><td>CHLORPHENIRAMINE MALEATE、DIBUCAINE HCL、NAPHAZOLINE HCL、BENZA…</td><td>外用液劑</td><td>蟲咬、搔癢、擦傷、刀傷、手指之殺菌、消毒。</td></tr><tr><td>衛部藥製字第060999號</td><td>睛晶點眼液</td><td>DIPOTASSIUM GLYCYRRHIZINATE、CHLORPHENIRAMINE MALEATE、NAPHAZO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅。</td></tr><tr><td>衛部藥製字第061093號</td><td>"元宙"鼻通暢鼻用噴液劑</td><td>CHLORPHENIRAMINE MALEATE、BENZALKONIUM CHLORIDE、NAPHAZOLINE H…</td><td>點鼻液劑</td><td>鼻塞、流鼻水、打噴嚏。</td></tr><tr><td>衛部藥製字第061569號</td><td>碧露眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>眼用液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞。</td></tr><tr><td>衛部藥輸字第027184號</td><td>心安鼻舒鼻噴劑</td><td>NAPHAZOLINE HYDROCHLORIDE、BENZALKONIUM CHLORIDE、CHLORPHENIRA…</td><td>鼻用噴液劑</td><td>急性鼻炎、過敏性鼻炎、鼻塞、流鼻水、噴嚏、鼻充血、肥厚性鼻炎、副鼻腔炎。</td></tr><tr><td>衛部藥輸字第027497號</td><td>樂敦藍視光眼藥水</td><td>NAPHAZOLINE HCL、FLAVINEADENINE DINUCLEOTIDE SODIUM、NEOSTIGMI…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛疲勞。</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（128 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第002981號</td><td>鼻樂鈉液</td><td>TRIPELENNAMINE HCL、NAPHAZOLINE NITRATE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006285號</td><td>鼻必愈鼻用液</td><td>NAPHAZOLINE HCL</td><td>1990/05/18</td></tr><tr><td>內衛藥製字第007347號</td><td>凌波眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2017/02/09</td></tr><tr><td>內衛藥製字第007530號</td><td>可樂那眼藥水</td><td>NAPHAZOLINE HCL、MAFENIDE (HOMOSULFAMINE)</td><td></td></tr><tr><td>內衛藥製字第011034號</td><td>樂爽點鼻液</td><td>NAPHAZOLINE NITRATE、TRIPELENNAMINE HCL</td><td>2013/02/23</td></tr><tr><td>內衛藥製字第012824號</td><td>鼻克能液</td><td>NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL</td><td>1989/08/17</td></tr><tr><td>內衛藥製字第014160號</td><td>鼻適寧噴劑</td><td>PHENYLEPHRINE HCL、NAPHAZOLINE NITRATE、CHLOROBUTANOL (TRICHLO…</td><td>1993/07/22</td></tr><tr><td>內衛藥製字第016694號</td><td>麻肌朗藥水</td><td>DIBUCAINE HCL、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、BENZE…</td><td>2013/10/07</td></tr><tr><td>內衛藥輸字第001524號</td><td>可麗爾</td><td>NAPHAZOLINE NITRATE、GLYCEROPHOSPHATE COPPER</td><td>1986/01/16</td></tr><tr><td>內衛藥輸字第002224號</td><td>哥兒根點鼻藥</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1987/03/27</td></tr><tr><td>內衛藥輸字第004118號</td><td>鹽酸/夫唑/</td><td>NAPHAZOLINE HCL</td><td>1985/12/02</td></tr><tr><td>內衛藥輸字第004905號</td><td>惠痔康軟膏</td><td>NAPHAZOLINE HCL、DYCLONINE HCL、CAMPHOR、DL-MENTHOL、EPINEPHRINE…</td><td>1990/07/20</td></tr><tr><td>內衛藥輸字第005388號</td><td>樂樂點鼻藥</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1985/12/24</td></tr><tr><td>內衛藥輸字第006177號</td><td>鼻舒通－西</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1986/06/02</td></tr><tr><td>內衛藥輸字第008320號</td><td>福特眼藥水</td><td>ZINC LACTATE、TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、CHO…</td><td>1991/02/01</td></tr><tr><td>衛署藥製字第001951號</td><td>安鼻寧液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第003351號</td><td>欣欣眼藥水</td><td>NAPHAZOLINE HCL</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第007185號</td><td>可恩點鼻液</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>2023/07/14</td></tr><tr><td>衛署藥製字第007816號</td><td>噴爽液</td><td>BENZALKONIUM CHLORIDE、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEA…</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第012394號</td><td>鼻爽液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>2014/03/28</td></tr><tr><td>衛署藥製字第013222號</td><td>鼻爽噴鼻液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1991/04/26</td></tr><tr><td>衛署藥製字第014846號</td><td>“居禮”舒順鼻用噴液劑</td><td>SODIUM PHOSPHATE DIBASIC ANHYDROUS (EQ TO DISODIUM HYDROGEN…</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第015149號</td><td>鼻敏朗液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td></td></tr><tr><td>衛署藥製字第017789號</td><td>麻肌朗軟膏</td><td>DIBUCAINE HCL、CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第018078號</td><td>"美西"眼寧眼藥水</td><td>ALLANTOIN、CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、ZINC SULF…</td><td>2020/04/30</td></tr><tr><td>衛署藥製字第022409號</td><td>老威眼藥水</td><td>BORIC ACID、ZINC SULFATE、NAPHAZOLINE NITRATE</td><td>1989/08/17</td></tr><tr><td>衛署藥製字第023765號</td><td>可舒鼻噴鼻液</td><td>NAPHAZOLINE HCL、TETRACAINE HCL、CHLORPHENIRAMINE MALEATE、MAFE…</td><td>1994/05/03</td></tr><tr><td>衛署藥製字第027921號</td><td>鼻必通點鼻液</td><td>TRIPELENNAMINE HCL、BENZALKONIUM CHLORIDE、NAPHAZOLINE NITRATE</td><td>1989/06/14</td></tr><tr><td>衛署藥製字第030644號</td><td>大正配保能鼻用噴霧液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、BENZETHONIUM CHLORI…</td><td>2015/07/01</td></tr><tr><td>衛署藥製字第031668號</td><td>"大正"速傷明液</td><td>DIBUCAINE HCL、CHLORHEXIDINE GLUCONATE、NAPHAZOLINE HCL</td><td>2024/04/19</td></tr><tr><td>衛署藥製字第032771號</td><td>甕鼻寧點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1997/09/23</td></tr><tr><td>衛署藥製字第035419號</td><td>"大豐"滋潤眼藥水</td><td>NEOSTIGMINE METHYLSULFATE、ASPARTATE POTASSIUM MAGNESIUM L- (…</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第036152號</td><td>"大豐"舒舒眼藥水</td><td>NAPHAZOLINE HCL</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第036154號</td><td>"大豐"滋露眼藥水</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>2019/12/23</td></tr><tr><td>衛署藥製字第036308號</td><td>鼻適寧噴劑</td><td>NAPHAZOLINE NITRATE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHO…</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第037151號</td><td>鼻可舒噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、MAFENIDE (HOMOSULFA…</td><td>2013/10/01</td></tr><tr><td>衛署藥製字第037901號</td><td>妥瑞度外用液</td><td>CHLORPHENIRAMINE MALEATE、BENZETHONIUM CHLORIDE、NAPHAZOLINE H…</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第038048號</td><td>癒王外用液</td><td>CHLORPHENIRAMINE MALEATE、ALLANTOIN、DIBUCAINE HCL、BENZETHONIU…</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第039873號</td><td>鼻通液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>2017/02/09</td></tr><tr><td>衛署藥輸字第000423號</td><td>硝酸挪發寧</td><td>NAPHAZOLINE NITRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000424號</td><td>鹽酸挪發寧</td><td>NAPHAZOLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第001132號</td><td>鹽酸奈法佐林</td><td>NAPHAZOLINE HCL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第001990號</td><td>聖萊茵散</td><td>NAPHAZOLINE</td><td>1988/11/08</td></tr><tr><td>衛署藥輸字第002849號</td><td>鹽酸/法佐林</td><td>NAPHAZOLINE HCL</td><td>1993/02/09</td></tr><tr><td>衛署藥輸字第003071號</td><td>克利健鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1990/10/29</td></tr><tr><td>衛署藥輸字第003902號</td><td>硝酸/法佐林</td><td>NAPHAZOLINE NITRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003903號</td><td>鹽酸/法佐林</td><td>NAPHAZOLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005364號</td><td>視安眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2009/06/30</td></tr><tr><td>衛署藥輸字第006070號</td><td>拿走膿點鼻液</td><td>CHLORPHENIRAMINE MALEATE、CETYLPYRIDINIUM CHLORIDE、GLYCYRRHIZ…</td><td>1986/01/10</td></tr><tr><td>衛署藥輸字第006734號</td><td>可樂巴兒眼藥水</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第006811號</td><td>硝酸/法佐林</td><td>NAPHAZOLINE NITRATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第006826號</td><td>鹽酸/法佐林</td><td>NAPHAZOLINE HCL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第007076號</td><td>樂爽點鼻液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1995/02/15</td></tr><tr><td>衛署藥輸字第007434號</td><td>第一眼藥水</td><td>NAPHAZOLINE HCL、VITAMIN A、TAURINE (EQ TO 2-AMINOETHANE SULFO…</td><td>1991/06/08</td></tr><tr><td>衛署藥輸字第007453號</td><td>利鼻能液</td><td>FLUROPREDNISOLONE 9-ALPHA 21-PHOSPHATE (SODIUM)、EPHEDRINE HC…</td><td>1988/06/10</td></tr><tr><td>衛署藥輸字第007709號</td><td>兒童維－老篤眼藥水</td><td>ZINC LACTATE、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNES…</td><td>1990/03/22</td></tr><tr><td>衛署藥輸字第007873號</td><td>帝化眼藥水</td><td>NAPHAZOLINE HCL、BENZALKONIUM CHLORIDE、VITAMIN A WATER MISCIB…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第008113號</td><td>巴樂眼藥水</td><td>PANTOTHENATE CALCIUM、CHONDROITIN SULFATE SODIUM (EQ TO SODIU…</td><td>1991/03/20</td></tr><tr><td>衛署藥輸字第008337號</td><td>欣滴佳眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、L-MENTHOL、NEOSTIGMINE METHYLSUL…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第008343號</td><td>滴佳可眼藥水</td><td>NAPHAZOLINE HCL、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAG…</td><td>1989/10/02</td></tr><tr><td>衛署藥輸字第008394號</td><td>舒娜外傷液</td><td>BENZALKONIUM CHLORIDE、DIBUCAINE HCL、NAPHAZOLINE HCL、DIPHENHY…</td><td>1993/06/14</td></tr><tr><td>衛署藥輸字第008524號</td><td>愛目眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第008848號</td><td>寧朗點眼液</td><td>PYRIDOXINE HCL、NAPHAZOLINE HCL、GLYCYRRHIZINATE DIPOTASSIUM (…</td><td>1992/05/19</td></tr><tr><td>衛署藥輸字第008873號</td><td>維通眼藥水</td><td>ANTAZOLINE SULPHATE、NAPHAZOLINE NITRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008887號</td><td>美瞳點眼液</td><td>PANTOTHENATE CALCIUM、ALLANTOIN、NAPHAZOLINE HCL</td><td>1992/04/09</td></tr><tr><td>衛署藥輸字第008982號</td><td>那爽鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1992/03/26</td></tr><tr><td>衛署藥輸字第009321號</td><td>視美目藥水</td><td>CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL、CHLOROBUTANOL (TRICH…</td><td>1991/08/12</td></tr><tr><td>衛署藥輸字第009417號</td><td>碧露眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>1989/11/02</td></tr><tr><td>衛署藥輸字第009816號</td><td>酪菌素鼻用軟膏</td><td>CETRIMIDE、NAPHAZOLINE HCL、TYROTHRICIN</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第009947號</td><td>滴滴明眼藥水</td><td>NAPHAZOLINE HCL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第010476號</td><td>硝酸/法佐林粉劑</td><td>NAPHAZOLINE NITRATE</td><td>1998/03/05</td></tr><tr><td>衛署藥輸字第010511號</td><td>三敏眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2004/10/22</td></tr><tr><td>衛署藥輸字第010518號</td><td>安明眼藥水</td><td>CHONDROITIN SULFATE、D-BORNEOL、PROCAINE HCL、TAURINE (EQ TO 2-…</td><td>1986/12/17</td></tr><tr><td>衛署藥輸字第010522號</td><td>光娜眼薑水</td><td>NAPHAZOLINE HCL、ZINC SULFATE、CHLORPHENIRAMINE MALEATE</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第010673號</td><td>滴滴明眼藥水</td><td>NAPHAZOLINE HCL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第010685號</td><td>愛樂目藥水</td><td>NAPHAZOLINE HCL、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、Z…</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第011673號</td><td>斯巴百吉麗眼藥水</td><td>ASPARTATE POTASSIUM L- (eq to POTASSIUM L-ASPARTATE)、ASPARTA…</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第011694號</td><td>斯巴百睛麗眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、PANTOTHENATE CALCIUM、CHLORPHENI…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第011817號</td><td>愛目眼藥水</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、CHLORPHENIRAMI…</td><td>1989/03/03</td></tr><tr><td>衛署藥輸字第011828號</td><td>舒樂目藥</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>1989/01/05</td></tr><tr><td>衛署藥輸字第012077號</td><td>Ｖ－老篤眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM…</td><td>1988/11/02</td></tr><tr><td>衛署藥輸字第012328號</td><td>施美露眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、ALLANTOIN</td><td>1986/05/30</td></tr><tr><td>衛署藥輸字第012919號</td><td>光娜眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、ZINC SULFATE</td><td>2018/09/12</td></tr><tr><td>衛署藥輸字第013199號</td><td>酪菌素鼻用軟膏</td><td>CETRIMIDE、NAPHAZOLINE HCL、TYROTHRICIN</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第013386號</td><td>愛力舒點眼液</td><td>TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、CHLORPHENIRAMINE…</td><td>1992/06/13</td></tr><tr><td>衛署藥輸字第013389號</td><td>配保能鼻用噴霧劑</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第014416號</td><td>鹽酸/甲嘧唑/</td><td>NAPHAZOLINE HCL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014417號</td><td>樂樂點鼻藥</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1995/10/06</td></tr><tr><td>衛署藥輸字第014600號</td><td>拿走膿點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、GLYCYRRHIZINATE DIP…</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第014604號</td><td>可麗爾點眼液</td><td>GLYCEROPHOSPHATE COPPER、NAPHAZOLINE NITRATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第015018號</td><td>施美露眼藥水</td><td>NAPHAZOLINE HCL、ZINC SULFATE、ALLANTOIN</td><td>1986/11/18</td></tr><tr><td>衛署藥輸字第015163號</td><td>"滋賀" 安明眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、TAURINE (EQ TO 2-AMINOETHANE SU…</td><td>2018/09/12</td></tr><tr><td>衛署藥輸字第015337號</td><td>施美露眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、ALLANTOIN</td><td>1993/02/11</td></tr><tr><td>衛署藥輸字第015810號</td><td>硝酸/法佐林</td><td>NAPHAZOLINE NITRATE</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第016146號</td><td>鹽酸荼法佐林</td><td>NAPHAZOLINE HCL</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第016807號</td><td>Ｖ－老篤眼藥水</td><td>ALLANTOIN、NAPHAZOLINE HCL、ASPARTATE POTASSIUM MAGNESIUM L- (…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第017044號</td><td>廣貫堂眼藥水</td><td>CHLORPHENIRAMINE MALEATE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDR…</td><td>1991/01/24</td></tr><tr><td>衛署藥輸字第017251號</td><td>滴佳可眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第017380號</td><td>碧露眼藥水</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>2021/12/24</td></tr><tr><td>衛署藥輸字第018232號</td><td>巴樂眼藥水</td><td>NAPHAZOLINE HCL、GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSI…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第018647號</td><td>視美目藥水</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、NAPHAZOLINE、BENZA…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019024號</td><td>寧朗點眼液</td><td>CYANOCOBALAMIN (VIT B12)、GLYCYRRHIZINATE DIPOTASSIUM (EQ TO…</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第019061號</td><td>愛力舒點眼液</td><td>NAPHAZOLINE HCL、TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、…</td><td>2004/01/30</td></tr><tr><td>衛署藥輸字第019615號</td><td>施美露眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM L- (eq to POTASSIUM L-ASPARTAT…</td><td>1995/11/23</td></tr><tr><td>衛署藥輸字第020481號</td><td>安敏樂眼藥水</td><td>ANTAZOLINE SULPHATE、NAPHAZOLINE NITRATE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第020961號</td><td>樂樂點鼻藥</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、BENZETHONIUM CHLORI…</td><td>2004/05/11</td></tr><tr><td>衛署藥輸字第022031號</td><td>納福康點眼液０．０１２％（鹽酸　甲嘧坐　）</td><td>NAPHAZOLINE HCL</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第022766號</td><td>貝兒V眼藥水</td><td>CHLORPHENIRAMINE MALEATE、GLYCYRRHIZINATE DIPOTASSIUM (EQ TO…</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第022780號</td><td>妙目寧清新點眼液</td><td>NAPHAZOLINE HCL</td><td>2013/01/03</td></tr><tr><td>衛署藥輸字第023054號</td><td>安鼻舒點鼻藥</td><td>CHLORPHENIRAMINE MALEATE、BENZETHONIUM CHLORIDE、NAPHAZOLINE H…</td><td>2017/07/05</td></tr><tr><td>衛署藥輸字第023101號</td><td>金亮眼藥水</td><td>GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSIUM GLYCYRRHIZINA…</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第023102號</td><td>金清眼藥水</td><td>ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM POTASSIUM…</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第023145號</td><td>睛晶點眼液</td><td>DIPOTASSIUM GLYCYRRHIZINATE、CHLORPHENIRAMINE MALEATE、NAPHAZO…</td><td>2021/11/30</td></tr><tr><td>衛署藥輸字第023152號</td><td>金亮兒童眼藥水</td><td>PYRIDOXINE HCL、NAPHAZOLINE HCL、GLYCYRRHIZINATE DIPOTASSIUM (…</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第023332號</td><td>金壕點護明眼藥水</td><td>TOCOPHEROL ACETATE ALPHA D-、NAPHAZOLINE HCL、ALLANTOIN、DIPOTA…</td><td>2010/08/24</td></tr><tr><td>衛署藥輸字第023333號</td><td>采視眼藥水</td><td>ALLANTOIN、PYRIDOXINE HCL、CHLORPHENIRAMINE MALEATE、DIPOTASSIU…</td><td>2018/03/16</td></tr><tr><td>衛署藥輸字第023375號</td><td>維純視必佳眼藥水</td><td>NEOSTIGMINE METHYLSULFATE、TOCOPHEROL ACETATE ALPHA D-、ALLANT…</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第023508號</td><td>納康點眼液</td><td>PHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>2024/05/17</td></tr><tr><td>衛署藥輸字第023583號</td><td>補又晶眼藥水</td><td>PYRIDOXINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHON…</td><td>2020/04/10</td></tr><tr><td>衛署藥輸字第023600號</td><td>德佑視立明眼藥水</td><td>NEOSTIGMINE METHYLSULFATE、NAPHAZOLINE HCL、DIPOTASSIUM GLYCYR…</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第023760號</td><td>利可亮眼藥水</td><td>PYRIDOXINE HCL、CHLORPHENIRAMINE MALEATE、ALLANTOIN、ASPARTATE…</td><td>2019/03/15</td></tr><tr><td>衛署藥輸字第023915號</td><td>依點爾眼藥水</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL</td><td>2022/01/21</td></tr><tr><td>衛署藥輸字第023916號</td><td>天天亮眼藥水</td><td>PYRIDOXINE HCL、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>2020/04/17</td></tr><tr><td>衛署藥輸字第023940號</td><td>點至寶眼藥水</td><td>CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL、ALLANTOIN、ASPARTATE…</td><td>2020/04/17</td></tr><tr><td>衛署藥輸字第024728號</td><td>德佑外用殺菌消毒液</td><td>NAPHAZOLINE HCL、DIBUCAINE HCL、BENZALKONIUM CHLORIDE、CHLORPHE…</td><td>2019/04/02</td></tr><tr><td>衛署藥輸字第025015號</td><td>“鐵甲”愛維他眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、NEOSTIGMINE METHYLS…</td><td>2022/07/04</td></tr><tr><td>衛署藥輸字第025032號</td><td>愛巴龍眼用液劑</td><td>NAPHAZOLINE HCL</td><td>2020/04/16</td></tr><tr><td>衛署藥輸字第025579號</td><td>金明眼藥水</td><td>TAURINE (EQ TO AMINOETHYL SULFONIC ACID )、DIPHENHYDRAMINE HC…</td><td>2019/03/28</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

### 眼用製劑

**台灣有多張相關許可證，涵蓋鼻用和眼用劑型。**

---

## 安全性考量

### 主要警告

1. **反跳性充血**
   - 長期使用鼻用製劑可能導致藥物性鼻炎
   - 建議使用不超過 3-5 天

2. **眼科使用禁忌**
   - 閉角型青光眼患者禁用
   - 可能加重眼壓升高

3. **全身性吸收風險**
   - 過度使用可能導致心血管副作用
   - 兒童和老年人需謹慎使用

4. **特殊族群**
   - 高血壓、心臟病患者需謹慎
   - 甲狀腺功能亢進患者需謹慎
   - 糖尿病患者需謹慎

### 藥物交互作用

- 與 MAO 抑制劑併用可能增加高血壓危機風險
- 與其他血管收縮劑併用可能增加心血管風險

---

## 結論與下一步

### 評估結論

| 預測適應症 | 證據等級 | 臨床轉譯可行性 | 建議優先順序 |
|-----------|---------|---------------|-------------|
| 毛髮稀疏症/禿髮症 | L5 | 極低 | 不建議開發 |
| 青光眼 | L5 | 極低 | 不建議開發 |

### 建議

1. **毛髮相關疾病**
   - 藥理機轉不支持（血管收縮劑不利於毛髮生長）
   - TxGNN 預測可能為假陽性
   - **不建議**進一步研究

2. **青光眼**
   - 已有更適合的 alpha 致效劑（如 brimonidine）用於青光眼
   - Naphazoline 的短效性和安全性問題不適合長期使用
   - **不建議**作為青光眼治療開發

3. **整體評估**
   - 本藥物的預測適應症與其藥理機轉不符
   - 建議將資源投入其他更有潛力的候選藥物

### 後續行動

- [ ] 無需進一步追蹤
- [x] 標記為低優先順序候選藥物

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「噴速點鼻液」許可證列 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

