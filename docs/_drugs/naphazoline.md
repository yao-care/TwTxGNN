---
layout: default
title: Naphazoline
parent: 僅模型預測 (L5)
nav_order: 188
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

# Naphazoline：從鼻炎與鼻塞到頭皮毛髮稀少症（hypotrichosis simplex of the scalp）

## 一句話總結

Naphazoline 是一種交感神經類血管收縮劑，原本用於過敏性鼻炎、鼻塞及眼充血等症狀。
TxGNN 模型預測它可能對**頭皮單純性毛髮稀少症 (hypotrichosis simplex of the scalp)** 有效，
但目前**沒有任何臨床試驗與文獻**支持，證據僅來自模型預測，屬於 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 交感神經藥（血管收縮藥） |
| 預測新適應症 | 頭皮單純性毛髮稀少症 (hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 183 張（有效單方 5／有效複方 50／已註銷 128） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Naphazoline 是 α-腎上腺素受體促效劑（資料顯示作用於 α1A、α2A、α2C 受體），透過收縮血管來減輕鼻腔與眼睛黏膜的充血與腫脹。

頭皮毛髮稀少症屬於遺傳性毛囊發育異常，與血管收縮所緩解的黏膜充血在病理上沒有明確關聯。此外，常用的促進毛髮生長藥物（如 minoxidil）作用偏向血管擴張，與 Naphazoline 的血管收縮作用方向相反。

因此，這個預測目前只能視為模型的統計關聯訊號，缺乏機轉上的支持，也可能是模型將多個毛髮相關疾病一併關聯的假象。排名前 4 的預測（毛髮稀少、圓禿、一般禿髮）都集中在毛髮疾病，同樣沒有證據支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Naphazoline 的不重複許可證共 **183 張**：有效單方 5 張、有效複方 50 張、已註銷 128 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第003941號 | 拿必樂點眼液 | 點眼液劑 | 綠洲化學工業有限公司 | 2028/05/24 | 暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅。 |
| 衛署藥製字第043543號 | "派頓"舒明點眼液 | 點眼液劑 | 臺灣派頓化學製藥股份有限公司 | 2030/02/18 | 暫時緩解因輕微眼部刺激所引起之不適或眼睛紅。 |
| 衛部藥輸字第026125號 | 鹽酸萘甲嘧唑啉 | （粉） | 宣泓貿易有限公司 | 2028/08/22 | 交感神經藥(血管收縮藥)。 |
| 衛部藥輸字第026457號 | 硝酸萘甲嘧唑啉 | （粉） | 宣泓貿易有限公司 | 2029/11/24 | 血管收縮劑 |
| 衛部藥輸字第028360號 | 萘甲嘧唑啉鹽酸鹽 | （粉） | 台灣荃新股份有限公司 | 2027/08/15 | 類交感神經藥；血管收縮藥。 |

<details><summary><strong>有效・複方（適應症屬整個複方，不是本藥單獨的適應症）</strong>（50 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>劑型</th><th>核准適應症</th></tr></thead><tbody><tr><td>內衛藥製字第012086號</td><td>"人生" 噴速點鼻液外用</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>外用液劑</td><td>急慢性鼻炎、過敏性鼻炎、鼻蓄膿症</td></tr><tr><td>衛署藥製字第001153號</td><td>噴通點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>因感冒而引起之鼻塞、鼻炎、肥厚性鼻炎等所引起之鼻充血</td></tr><tr><td>衛署藥製字第001601號</td><td>爽通鼻劑</td><td>TRIPELENNAMINE HCL、NAPHAZOLINE NITRATE</td><td>點鼻液劑</td><td>過敏性鼻炎、及由感冒過敏所引起之鼻塞、鼻充血</td></tr><tr><td>衛署藥製字第003994號</td><td>可恩點眼液</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>點眼液劑</td><td>眼科：角膜炎、眼睛疲勞、眼充血、結膜炎</td></tr><tr><td>衛署藥製字第013438號</td><td>"成大"華鼻露液</td><td>NAPHAZOLINE NITRATE、CHLORPHENIRAMINE MALEATE</td><td>外用液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀</td></tr><tr><td>衛署藥製字第014320號</td><td>"派頓"浠樂通點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>點鼻液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀。</td></tr><tr><td>衛署藥製字第015762號</td><td>嘉舒樂噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>鼻塞、鼻充血、鼻竇炎、過敏性鼻炎</td></tr><tr><td>衛署藥製字第016222號</td><td>"溫士頓"舒鼻喜噴鼻液</td><td>PROCAINE HCL、DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎及流鼻水、鼻塞、鼻出血</td></tr><tr><td>衛署藥製字第019585號</td><td>"長安"汎鼻寧噴劑</td><td>NAPHAZOLINE HCL、PROCAINE HCL、DIPHENHYDRAMINE HCL</td><td>鼻用氣化噴霧劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎（鼻塞、流鼻水）鼻出血</td></tr><tr><td>衛署藥製字第019904號</td><td>"溫士頓"溫美眼眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>點眼液劑</td><td>角膜炎、角膜潰瘍和浸潤、手術創傷和手術後之角膜混濁、角膜異物引起之角膜障害、角膜上皮剝離、腺病性角膜炎、眼充血、鼻淚管閉塞</td></tr><tr><td>衛署藥製字第020501號</td><td>"艾力特" 佑鼻噴霧液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>急、慢性副鼻腔炎、肥厚性鼻炎、急性鼻炎、過敏性鼻炎、感冒所引起之鼻塞、充血及上呼吸道之發炎症狀</td></tr><tr><td>衛署藥製字第021719號</td><td>"尼斯可"噴鼻液</td><td>NAPHAZOLINE NITRATE、NAPHAZOLINE NITRATE、CHLORPHENIRAMINE MAL…</td><td>鼻用噴液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀</td></tr><tr><td>衛署藥製字第022488號</td><td>"派頓"保麗晶眼藥水</td><td>ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM POTASSIUM…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅、眼睛疲勞</td></tr><tr><td>衛署藥製字第022515號</td><td>"派頓" 晶潤 眼藥水</td><td>TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、NAPHAZOLINE HCL、…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛疲勞</td></tr><tr><td>衛署藥製字第023380號</td><td>"健康"宜鼻噴鼻液</td><td>NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL、PROCAINE HCL</td><td>鼻用噴液劑</td><td>急慢性鼻炎、過敏性鼻炎、副鼻腔炎、鼻塞、鼻充血</td></tr><tr><td>衛署藥製字第025931號</td><td>"成大" 愛鼻爽點鼻液</td><td>NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL、PROCAINE HCL</td><td>外用液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎所引起之鼻塞、流鼻水、鼻出血</td></tr><tr><td>衛署藥製字第027556號</td><td>噴愈好外用液</td><td>DIBUCAINE HCL、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>外用液劑</td><td>昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢。</td></tr><tr><td>衛署藥製字第032148號</td><td>寧疤寧黑圓圈噴鼻劑</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>點鼻液劑</td><td>過敏性鼻炎、鼻塞</td></tr><tr><td>衛署藥製字第032860號</td><td>鼻通噴液劑</td><td>CHLORPHENIRAMINE MALEATE、CHLORPHENIRAMINE MALEATE、NAPHAZOLIN…</td><td>點鼻液劑</td><td>鼻塞、流鼻水，打噴嚏．</td></tr><tr><td>衛署藥製字第033252號</td><td>"明大" 鼻爽噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>外用液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀。</td></tr><tr><td>衛署藥製字第033483號</td><td>"大豐"鼻速通噴鼻液</td><td>BENZETHONIUM CHLORIDE、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEA…</td><td>鼻用噴液劑</td><td>緩解過敏性鼻炎、枯草熱所引起之相關症狀（流鼻水，鼻塞，打噴嚏）</td></tr><tr><td>衛署藥製字第038302號</td><td>"福元"鼻舒通噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE NITRATE</td><td>外用液劑</td><td>鼻炎、副鼻腔炎、上呼吸道炎、過敏性鼻液、鼻塞</td></tr><tr><td>衛署藥製字第039047號</td><td>"近江兄弟"鼻立通噴液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀</td></tr><tr><td>衛署藥製字第040816號</td><td>"近江兄弟" 白藥水</td><td>BENZALKONIUM CHLORIDE、CHLORPHENIRAMINE MALEATE、NAPHAZOLINE H…</td><td>外用液劑</td><td>蟲咬、搔癢、擦傷、刀傷、手指之殺菌、消毒。</td></tr><tr><td>衛署藥製字第041371號</td><td>甕鼻寧點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>點鼻液劑</td><td>鼻炎、副鼻腔炎、上呼吸氣道炎、鼻充血、鼻塞。</td></tr><tr><td>衛署藥製字第043457號</td><td>"派頓"保滴明點眼液</td><td>NAPHAZOLINE HCL、ZINC SULFATE</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅及因眼睛乾澀所引起灼熱感與刺激感。</td></tr><tr><td>衛署藥製字第043489號</td><td>"約克" 舒鼻爽噴鼻液</td><td>PROCAINE HCL、DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎所引起之流鼻水、鼻塞及鼻出血。</td></tr><tr><td>衛署藥製字第046987號</td><td>"中美" 膚諾痛外用液</td><td>NAPHAZOLINE HCL、DIBUCAINE HCL、CHLORPHENIRAMINE MALEATE、BENZE…</td><td>外用液劑</td><td>傷口消毒、昆蟲咬傷或皮膚刺激所引起之疼痛及搔癢，及暫時緩解皮膚搔癢。</td></tr><tr><td>衛署藥製字第049759號</td><td>“中美”鼻舒康噴鼻液</td><td>PROCAINE HCL、DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL</td><td>鼻用噴液劑</td><td>鼻炎、副鼻腔炎、過敏性鼻炎所引起之流鼻水、鼻塞及鼻出血。</td></tr><tr><td>衛署藥製字第052298號</td><td>傷寧外用殺菌消毒液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、DIBUCAINE HCL、BENZA…</td><td>外用液劑</td><td>蟲咬、搔癢、擦傷、刀傷、手指之殺菌、消毒。</td></tr><tr><td>衛署藥製字第055989號</td><td>立明點眼液</td><td>NAPHAZOLINE HYDROCHLORIDE、CHONDROITIN SULFATE SODIUM (EQ TO…</td><td>點眼液劑</td><td>角膜炎、眼睛疲勞、眼充血、結膜炎。</td></tr><tr><td>衛署藥輸字第018605號</td><td>第一眼藥水</td><td>ALLANTOIN、NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第020997號</td><td>獅之施美露眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM L- (eq to POTASSIUM L-ASPARTAT…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛疲勞</td></tr><tr><td>衛署藥輸字第023384號</td><td>e視界－５０點眼液</td><td>TOCOPHEROL ACETATE ALPHA D-、CHLORPHENIRAMINE MALEATE、NAPHAZO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第023466號</td><td>樂敦維他眼藥水</td><td>PYRIDOXINE HCL、ASPARTATE POTASSIUM L- (eq to POTASSIUM L-ASP…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞</td></tr><tr><td>衛署藥輸字第024073號</td><td>"佐藤" 視朗點眼液</td><td>PYRIDOXINE HCL、NAPHAZOLINE HCL、CYANOCOBALAMIN (VIT B12)、DIPO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激 所引起之不適、眼睛紅、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第024505號</td><td>視安達琪眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM…</td><td>點眼液劑</td><td>眼睛疲勞、暫時緩解因輕微眼部刺激所引起的不適或眼睛紅、眼睛癢。</td></tr><tr><td>衛署藥輸字第024871號</td><td>牛津艾露比眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、CYANOCOBALAMIN (VIT…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適，或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第024908號</td><td>雪之元噴鼻液</td><td>NAPHAZOLINE HCL、LIDOCAINE、CHLORPHENIRAMINE MALEATE</td><td>鼻用噴液劑</td><td>暫時緩解因鼻炎、過敏性鼻炎、過敏或感冒引起之鼻塞、流鼻水、打噴嚏症狀。</td></tr><tr><td>衛署藥輸字第025097號</td><td>視安眼藥水</td><td>NAPHAZOLINE HYDROCHLORIDE、CHONDROITIN SULFATE SODIUM (EQ TO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起的不適或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025301號</td><td>“佐藤”視敏寧點眼液</td><td>DIPHENHYDRAMINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025638號</td><td>日岩艾眼舒眼藥水</td><td>NAPHAZOLINE HYDROCHLORIDE、CYANOCOBALAMIN (VIT B12)、CHLORPHEN…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適，或眼睛紅、眼睛癢、眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025666號</td><td>詩披雅眼藥水</td><td>PANTHENOL、NAPHAZOLINE HYDROCHLORIDE、AMINOCAPROIC ACID EPSILO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞。</td></tr><tr><td>衛署藥輸字第025668號</td><td>睛亮點眼液</td><td>PANTHENOL、NAPHAZOLINE HYDROCHLORIDE、AMINOCAPROIC ACID EPSILO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅、眼睛疲勞、眼睛癢。</td></tr><tr><td>衛部藥製字第060516號</td><td>潔淨膚外用殺菌消毒液</td><td>DIBUCAINE HCL、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、BENZA…</td><td>外用液劑</td><td>蟲咬、搔癢、擦傷、刀傷、手指之殺菌、消毒。</td></tr><tr><td>衛部藥製字第060999號</td><td>睛晶點眼液</td><td>DIPOTASSIUM GLYCYRRHIZINATE、CHLORPHENIRAMINE MALEATE、NAPHAZO…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適或眼睛紅。</td></tr><tr><td>衛部藥製字第061093號</td><td>"元宙"鼻通暢鼻用噴液劑</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、BENZALKONIUM CHLORI…</td><td>點鼻液劑</td><td>鼻塞、流鼻水、打噴嚏。</td></tr><tr><td>衛部藥製字第061569號</td><td>碧露眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>眼用液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛癢，眼睛疲勞。</td></tr><tr><td>衛部藥輸字第027184號</td><td>心安鼻舒鼻噴劑</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HYDROCHLORIDE、BENZALKON…</td><td>鼻用噴液劑</td><td>急性鼻炎、過敏性鼻炎、鼻塞、流鼻水、噴嚏、鼻充血、肥厚性鼻炎、副鼻腔炎。</td></tr><tr><td>衛部藥輸字第027497號</td><td>樂敦藍視光眼藥水</td><td>PYRIDOXINE HCL、FLAVINEADENINE DINUCLEOTIDE SODIUM、NEOSTIGMIN…</td><td>點眼液劑</td><td>暫時緩解因輕微眼部刺激所引起之不適、或眼睛紅，眼睛疲勞。</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（128 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第002981號</td><td>鼻樂鈉液</td><td>TRIPELENNAMINE HCL、NAPHAZOLINE NITRATE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006285號</td><td>鼻必愈鼻用液</td><td>NAPHAZOLINE HCL</td><td>1990/05/18</td></tr><tr><td>內衛藥製字第007347號</td><td>凌波眼藥水</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>2017/02/09</td></tr><tr><td>內衛藥製字第007530號</td><td>可樂那眼藥水</td><td>MAFENIDE (HOMOSULFAMINE)、NAPHAZOLINE HCL</td><td></td></tr><tr><td>內衛藥製字第011034號</td><td>樂爽點鼻液</td><td>NAPHAZOLINE NITRATE、TRIPELENNAMINE HCL</td><td>2013/02/23</td></tr><tr><td>內衛藥製字第012824號</td><td>鼻克能液</td><td>NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL</td><td>1989/08/17</td></tr><tr><td>內衛藥製字第014160號</td><td>鼻適寧噴劑</td><td>NAPHAZOLINE NITRATE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHO…</td><td>1993/07/22</td></tr><tr><td>內衛藥製字第016694號</td><td>麻肌朗藥水</td><td>NAPHAZOLINE HCL、DIBUCAINE HCL、BENZETHONIUM CHLORIDE、CHLORPHE…</td><td>2013/10/07</td></tr><tr><td>內衛藥輸字第001524號</td><td>可麗爾</td><td>NAPHAZOLINE NITRATE、GLYCEROPHOSPHATE COPPER</td><td>1986/01/16</td></tr><tr><td>內衛藥輸字第002224號</td><td>哥兒根點鼻藥</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1987/03/27</td></tr><tr><td>內衛藥輸字第004118號</td><td>鹽酸/夫唑/</td><td>NAPHAZOLINE HCL</td><td>1985/12/02</td></tr><tr><td>內衛藥輸字第004905號</td><td>惠痔康軟膏</td><td>CHLORAL HYDRATE、EPINEPHRINE HCL、NAPHAZOLINE HCL、DYCLONINE HC…</td><td>1990/07/20</td></tr><tr><td>內衛藥輸字第005388號</td><td>樂樂點鼻藥</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1985/12/24</td></tr><tr><td>內衛藥輸字第006177號</td><td>鼻舒通－西</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1986/06/02</td></tr><tr><td>內衛藥輸字第008320號</td><td>福特眼藥水</td><td>TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、NAPHAZOLINE HCL、…</td><td>1991/02/01</td></tr><tr><td>衛署藥製字第001951號</td><td>安鼻寧液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第003351號</td><td>欣欣眼藥水</td><td>NAPHAZOLINE HCL</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第007185號</td><td>可恩點鼻液</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>2023/07/14</td></tr><tr><td>衛署藥製字第007816號</td><td>噴爽液</td><td>BENZALKONIUM CHLORIDE、CHLORPHENIRAMINE MALEATE、NAPHAZOLINE H…</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第012394號</td><td>鼻爽液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>2014/03/28</td></tr><tr><td>衛署藥製字第013222號</td><td>鼻爽噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1991/04/26</td></tr><tr><td>衛署藥製字第014846號</td><td>“居禮”舒順鼻用噴液劑</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、SODIUM PHOSPHATE DI…</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第015149號</td><td>鼻敏朗液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td></td></tr><tr><td>衛署藥製字第017789號</td><td>麻肌朗軟膏</td><td>NAPHAZOLINE HCL、DIBUCAINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第018078號</td><td>"美西"眼寧眼藥水</td><td>ALLANTOIN、ZINC SULFATE、CHLORPHENIRAMINE MALEATE、NAPHAZOLINE…</td><td>2020/04/30</td></tr><tr><td>衛署藥製字第022409號</td><td>老威眼藥水</td><td>NAPHAZOLINE NITRATE、ZINC SULFATE、BORIC ACID</td><td>1989/08/17</td></tr><tr><td>衛署藥製字第023765號</td><td>可舒鼻噴鼻液</td><td>CHLORPHENIRAMINE MALEATE、TETRACAINE HCL、MAFENIDE (HOMOSULFAM…</td><td>1994/05/03</td></tr><tr><td>衛署藥製字第027921號</td><td>鼻必通點鼻液</td><td>NAPHAZOLINE NITRATE、BENZALKONIUM CHLORIDE、TRIPELENNAMINE HCL</td><td>1989/06/14</td></tr><tr><td>衛署藥製字第030644號</td><td>大正配保能鼻用噴霧液</td><td>NAPHAZOLINE HCL、BENZETHONIUM CHLORIDE、CHLORPHENIRAMINE MALEA…</td><td>2015/07/01</td></tr><tr><td>衛署藥製字第031668號</td><td>"大正"速傷明液</td><td>CHLORHEXIDINE GLUCONATE、NAPHAZOLINE HCL、DIBUCAINE HCL</td><td>2024/04/19</td></tr><tr><td>衛署藥製字第032771號</td><td>甕鼻寧點鼻液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>1997/09/23</td></tr><tr><td>衛署藥製字第035419號</td><td>"大豐"滋潤眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM…</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第036152號</td><td>"大豐"舒舒眼藥水</td><td>NAPHAZOLINE HCL</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第036154號</td><td>"大豐"滋露眼藥水</td><td>CHLORPHENIRAMINE MALEATE、CHONDROITIN SULFATE SODIUM (EQ TO S…</td><td>2019/12/23</td></tr><tr><td>衛署藥製字第036308號</td><td>鼻適寧噴劑</td><td>PHENYLEPHRINE HCL、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)…</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第037151號</td><td>鼻可舒噴鼻液</td><td>TETRACAINE HCL、MAFENIDE (HOMOSULFAMINE)、NAPHAZOLINE HCL、CHLO…</td><td>2013/10/01</td></tr><tr><td>衛署藥製字第037901號</td><td>妥瑞度外用液</td><td>NAPHAZOLINE HCL、DIBUCAINE HCL、BENZETHONIUM CHLORIDE、CHLORPHE…</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第038048號</td><td>癒王外用液</td><td>ALLANTOIN、CHLORPHENIRAMINE MALEATE、BENZETHONIUM CHLORIDE、NAP…</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第039873號</td><td>鼻通液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>2017/02/09</td></tr><tr><td>衛署藥輸字第000423號</td><td>硝酸挪發寧</td><td>NAPHAZOLINE NITRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000424號</td><td>鹽酸挪發寧</td><td>NAPHAZOLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第001132號</td><td>鹽酸奈法佐林</td><td>NAPHAZOLINE HCL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第001990號</td><td>聖萊茵散</td><td>NAPHAZOLINE</td><td>1988/11/08</td></tr><tr><td>衛署藥輸字第002849號</td><td>鹽酸/法佐林</td><td>NAPHAZOLINE HCL</td><td>1993/02/09</td></tr><tr><td>衛署藥輸字第003071號</td><td>克利健鼻液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1990/10/29</td></tr><tr><td>衛署藥輸字第003902號</td><td>硝酸/法佐林</td><td>NAPHAZOLINE NITRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003903號</td><td>鹽酸/法佐林</td><td>NAPHAZOLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005364號</td><td>視安眼藥水</td><td>NAPHAZOLINE HCL、TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、…</td><td>2009/06/30</td></tr><tr><td>衛署藥輸字第006070號</td><td>拿走膿點鼻液</td><td>CETYLPYRIDINIUM CHLORIDE、GLYCYRRHIZINATE DIPOTASSIUM (EQ TO…</td><td>1986/01/10</td></tr><tr><td>衛署藥輸字第006734號</td><td>可樂巴兒眼藥水</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第006811號</td><td>硝酸/法佐林</td><td>NAPHAZOLINE NITRATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第006826號</td><td>鹽酸/法佐林</td><td>NAPHAZOLINE HCL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第007076號</td><td>樂爽點鼻液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1995/02/15</td></tr><tr><td>衛署藥輸字第007434號</td><td>第一眼藥水</td><td>NAPHAZOLINE HCL、TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、…</td><td>1991/06/08</td></tr><tr><td>衛署藥輸字第007453號</td><td>利鼻能液</td><td>NAPHAZOLINE NITRATE、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLO…</td><td>1988/06/10</td></tr><tr><td>衛署藥輸字第007709號</td><td>兒童維－老篤眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM…</td><td>1990/03/22</td></tr><tr><td>衛署藥輸字第007873號</td><td>帝化眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第008113號</td><td>巴樂眼藥水</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、GLYCYRRHIZINATE DIP…</td><td>1991/03/20</td></tr><tr><td>衛署藥輸字第008337號</td><td>欣滴佳眼藥水</td><td>TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、NEOSTIGMINE METH…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第008343號</td><td>滴佳可眼藥水</td><td>NAPHAZOLINE HCL、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHO…</td><td>1989/10/02</td></tr><tr><td>衛署藥輸字第008394號</td><td>舒娜外傷液</td><td>NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL、DIBUCAINE HCL、BENZALKONI…</td><td>1993/06/14</td></tr><tr><td>衛署藥輸字第008524號</td><td>愛目眼藥水</td><td>VITAMIN A、CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROIT…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第008848號</td><td>寧朗點眼液</td><td>PYRIDOXINE HCL、GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSIU…</td><td>1992/05/19</td></tr><tr><td>衛署藥輸字第008873號</td><td>維通眼藥水</td><td>ANTAZOLINE SULPHATE、NAPHAZOLINE NITRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008887號</td><td>美瞳點眼液</td><td>NAPHAZOLINE HCL、PANTOTHENATE CALCIUM、ALLANTOIN</td><td>1992/04/09</td></tr><tr><td>衛署藥輸字第008982號</td><td>那爽鼻液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1992/03/26</td></tr><tr><td>衛署藥輸字第009321號</td><td>視美目藥水</td><td>PYRIDOXINE HCL、BENZALKONIUM CHLORIDE、VITAMIN A、PANTOTHENATE…</td><td>1991/08/12</td></tr><tr><td>衛署藥輸字第009417號</td><td>碧露眼藥水</td><td>CHLORPHENIRAMINE MALEATE、CHONDROITIN SULFATE SODIUM (EQ TO S…</td><td>1989/11/02</td></tr><tr><td>衛署藥輸字第009816號</td><td>酪菌素鼻用軟膏</td><td>TYROTHRICIN、CETRIMIDE、NAPHAZOLINE HCL</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第009947號</td><td>滴滴明眼藥水</td><td>NAPHAZOLINE HCL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第010476號</td><td>硝酸/法佐林粉劑</td><td>NAPHAZOLINE NITRATE</td><td>1998/03/05</td></tr><tr><td>衛署藥輸字第010511號</td><td>三敏眼藥水</td><td>PANTHENOL、CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、CYANOCOBA…</td><td>2004/10/22</td></tr><tr><td>衛署藥輸字第010518號</td><td>安明眼藥水</td><td>D-BORNEOL、ZINC SULFATE、PROCAINE HCL、TAURINE (EQ TO 2-AMINOET…</td><td>1986/12/17</td></tr><tr><td>衛署藥輸字第010522號</td><td>光娜眼薑水</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、ZINC SULFATE</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第010673號</td><td>滴滴明眼藥水</td><td>NAPHAZOLINE HCL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第010685號</td><td>愛樂目藥水</td><td>TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、NAPHAZOLINE HCL、…</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第011673號</td><td>斯巴百吉麗眼藥水</td><td>ASPARTATE POTASSIUM L- (eq to POTASSIUM L-ASPARTATE)、PYRIDOX…</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第011694號</td><td>斯巴百睛麗眼藥水</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、ZINC SULFATE、PYRIDO…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第011817號</td><td>愛目眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、CHONDROITIN SULFATE…</td><td>1989/03/03</td></tr><tr><td>衛署藥輸字第011828號</td><td>舒樂目藥</td><td>CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、NAPHAZOLINE HCL、T…</td><td>1989/01/05</td></tr><tr><td>衛署藥輸字第012077號</td><td>Ｖ－老篤眼藥水</td><td>NEOSTIGMINE METHYLSULFATE、NAPHAZOLINE HCL、ASPARTATE POTASSIU…</td><td>1988/11/02</td></tr><tr><td>衛署藥輸字第012328號</td><td>施美露眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、ALLANTOIN</td><td>1986/05/30</td></tr><tr><td>衛署藥輸字第012919號</td><td>光娜眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>2018/09/12</td></tr><tr><td>衛署藥輸字第013199號</td><td>酪菌素鼻用軟膏</td><td>CETRIMIDE、NAPHAZOLINE HCL、TYROTHRICIN</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第013386號</td><td>愛力舒點眼液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、TAURINE (EQ TO 2-AM…</td><td>1992/06/13</td></tr><tr><td>衛署藥輸字第013389號</td><td>配保能鼻用噴霧劑</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第014416號</td><td>鹽酸/甲嘧唑/</td><td>NAPHAZOLINE HCL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014417號</td><td>樂樂點鼻藥</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE</td><td>1995/10/06</td></tr><tr><td>衛署藥輸字第014600號</td><td>拿走膿點鼻液</td><td>GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSIUM GLYCYRRHIZINA…</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第014604號</td><td>可麗爾點眼液</td><td>NAPHAZOLINE NITRATE、GLYCEROPHOSPHATE COPPER</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第015018號</td><td>施美露眼藥水</td><td>ZINC SULFATE、NAPHAZOLINE HCL、ALLANTOIN</td><td>1986/11/18</td></tr><tr><td>衛署藥輸字第015163號</td><td>"滋賀" 安明眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2018/09/12</td></tr><tr><td>衛署藥輸字第015337號</td><td>施美露眼藥水</td><td>ALLANTOIN、NAPHAZOLINE HCL、ZINC SULFATE</td><td>1993/02/11</td></tr><tr><td>衛署藥輸字第015810號</td><td>硝酸/法佐林</td><td>NAPHAZOLINE NITRATE</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第016146號</td><td>鹽酸荼法佐林</td><td>NAPHAZOLINE HCL</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第016807號</td><td>Ｖ－老篤眼藥水</td><td>ALLANTOIN、ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第017044號</td><td>廣貫堂眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、CHONDROITIN SULFATE…</td><td>1991/01/24</td></tr><tr><td>衛署藥輸字第017251號</td><td>滴佳可眼藥水</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、CHONDROITIN SULFATE…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第017380號</td><td>碧露眼藥水</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、CHONDROITIN SULFATE…</td><td>2021/12/24</td></tr><tr><td>衛署藥輸字第018232號</td><td>巴樂眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第018647號</td><td>視美目藥水</td><td>NAPHAZOLINE、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、CHLOR…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019024號</td><td>寧朗點眼液</td><td>PYRIDOXINE HCL、NAPHAZOLINE HCL、CYANOCOBALAMIN (VIT B12)、GLYC…</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第019061號</td><td>愛力舒點眼液</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、TAURINE (EQ TO 2-AM…</td><td>2004/01/30</td></tr><tr><td>衛署藥輸字第019615號</td><td>施美露眼藥水</td><td>NAPHAZOLINE HCL、ALLANTOIN、ASPARTATE POTASSIUM L- (eq to POTA…</td><td>1995/11/23</td></tr><tr><td>衛署藥輸字第020481號</td><td>安敏樂眼藥水</td><td>NAPHAZOLINE NITRATE、ANTAZOLINE SULPHATE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第020961號</td><td>樂樂點鼻藥</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、BENZETHONIUM CHLORI…</td><td>2004/05/11</td></tr><tr><td>衛署藥輸字第022031號</td><td>納福康點眼液０．０１２％（鹽酸　甲嘧坐　）</td><td>NAPHAZOLINE HCL</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第022766號</td><td>貝兒V眼藥水</td><td>NAPHAZOLINE HCL、GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSI…</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第022780號</td><td>妙目寧清新點眼液</td><td>NAPHAZOLINE HCL</td><td>2013/01/03</td></tr><tr><td>衛署藥輸字第023054號</td><td>安鼻舒點鼻藥</td><td>BENZETHONIUM CHLORIDE、NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEA…</td><td>2017/07/05</td></tr><tr><td>衛署藥輸字第023101號</td><td>金亮眼藥水</td><td>AMINOETHYLSULFONIC ACID、GLYCYRRHIZINATE DIPOTASSIUM (EQ TO D…</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第023102號</td><td>金清眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NEOSTIGMINE METHYLSULFATE、NAPHAZOLI…</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第023145號</td><td>睛晶點眼液</td><td>CHLORPHENIRAMINE MALEATE、DIPOTASSIUM GLYCYRRHIZINATE、NAPHAZO…</td><td>2021/11/30</td></tr><tr><td>衛署藥輸字第023152號</td><td>金亮兒童眼藥水</td><td>GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSIUM GLYCYRRHIZINA…</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第023332號</td><td>金壕點護明眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NEOSTIGMINE METHYLSULFATE、DIPOTASSI…</td><td>2010/08/24</td></tr><tr><td>衛署藥輸字第023333號</td><td>采視眼藥水</td><td>DIPOTASSIUM GLYCYRRHIZINATE、NAPHAZOLINE HCL、CHLORPHENIRAMINE…</td><td>2018/03/16</td></tr><tr><td>衛署藥輸字第023375號</td><td>維純視必佳眼藥水</td><td>ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM POTASSIUM…</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第023508號</td><td>納康點眼液</td><td>NAPHAZOLINE HCL、PHENIRAMINE MALEATE</td><td>2024/05/17</td></tr><tr><td>衛署藥輸字第023583號</td><td>補又晶眼藥水</td><td>PYRIDOXINE HCL、AMINOETHYLSULFONIC ACID、NAPHAZOLINE HCL、ZINC…</td><td>2020/04/10</td></tr><tr><td>衛署藥輸字第023600號</td><td>德佑視立明眼藥水</td><td>NEOSTIGMINE METHYLSULFATE、NAPHAZOLINE HCL、CHLORPHENIRAMINE M…</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第023760號</td><td>利可亮眼藥水</td><td>ASPARTATE POTASSIUM MAGNESIUM L- ( EQ TO MAGNESIUM POTASSIUM…</td><td>2019/03/15</td></tr><tr><td>衛署藥輸字第023915號</td><td>依點爾眼藥水</td><td>CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL、PYRIDOXINE HCL</td><td>2022/01/21</td></tr><tr><td>衛署藥輸字第023916號</td><td>天天亮眼藥水</td><td>PYRIDOXINE HCL、CHLORPHENIRAMINE MALEATE、NAPHAZOLINE HCL</td><td>2020/04/17</td></tr><tr><td>衛署藥輸字第023940號</td><td>點至寶眼藥水</td><td>GLYCYRRHIZINATE DIPOTASSIUM (EQ TO DIPOTASSIUM GLYCYRRHIZINA…</td><td>2020/04/17</td></tr><tr><td>衛署藥輸字第024728號</td><td>德佑外用殺菌消毒液</td><td>NAPHAZOLINE HCL、CHLORPHENIRAMINE MALEATE、DIBUCAINE HCL、BENZA…</td><td>2019/04/02</td></tr><tr><td>衛署藥輸字第025015號</td><td>“鐵甲”愛維他眼藥水</td><td>PANTHENOL、AMINOCAPROIC ACID EPSILON-、CHLORPHENIRAMINE MALEAT…</td><td>2022/07/04</td></tr><tr><td>衛署藥輸字第025032號</td><td>愛巴龍眼用液劑</td><td>NAPHAZOLINE HCL</td><td>2020/04/16</td></tr><tr><td>衛署藥輸字第025579號</td><td>金明眼藥水</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>2019/03/28</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **模型資料庫標示的疾病禁忌（來自知識圖譜，非仿單內容）**：高血壓、心血管疾病、心臟病、高血糖、糖尿病（含糖尿病酮酸中毒）、隅角閉鎖型青光眼、甲狀腺機能亢進（含葛瑞夫茲氏病、甲狀腺毒症）、眼部感染性疾病、結膜炎。
- **藥物交互作用／藥理標的**：已知作用於 α1A、α2A、α2C 腎上腺素受體（另有小鼠 Taar4 相關標的）。未提供具體藥物間交互作用等級。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
預測分數雖高，但沒有任何臨床試驗或文獻佐證，機轉上也缺乏合理連結（血管收縮作用與促進毛髮生長方向相反），僅屬模型預測，證據等級為 L5。

**若要推進需要：**
- 取得 Naphazoline 完整的作用機轉資料，並釐清是否與毛囊生物學有任何關聯
- 進行文獻回顧與前臨床研究（如毛囊細胞或動物模型），驗證是否有生長促進效果
- 評估經皮或頭皮外用的劑型與給藥途徑可行性（目前上市劑型為鼻用、眼用與外用液劑）
- 評估全身吸收所帶來的心血管與血壓風險，因為知識圖譜顯示高血壓與心血管疾病為禁忌
- 在上述基礎出現前，不建議投入臨床開發資源

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

