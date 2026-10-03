---
layout: default
title: Glycol Salicylate
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Glycol Salicylate
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

# Glycol Salicylate：從局部疼痛緩解到 Glanzmann 血小板無力症

## 一句話總結

Glycol salicylate 是一種水楊酸酯類外用製劑，廣泛用於貼布、乳膏等劑型，原本用於緩解腰痛、肩膀酸痛、關節痛等局部肌肉骨骼疼痛。
TxGNN 模型預測它可能對 **Glanzmann 血小板無力症 (Glanzmann Thrombasthenia)** 有效，
然而目前**無任何臨床試驗或文獻**支持這個方向，此預測目前僅停留在模型計算層次。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 暫時緩解局部疼痛（腰痛、肩膀酸痛、關節痛等） |
| 預測新適應症 | Glanzmann 血小板無力症 (Glanzmann Thrombasthenia) |
| TxGNN 預測分數 | 98.17% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 54 張（有效單方 0／有效複方 30／已註銷 24） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Glycol salicylate 詳細的作用機轉資料。根據已知資訊，本藥屬於**水楊酸酯類（salicylate ester）**化合物，與 aspirin 同族，主要以外用貼布、藥膠布、乳膏等劑型於皮膚局部給藥，全身性生物利用度極低。

理論上，水楊酸酯類可透過抑制 COX-1 酶減少血栓素 A2（TXA2）的生成，進而輕微干擾血小板活化路徑，故 TxGNN 模型可能依此將其連結至多種血液凝固相關疾病。然而，**Glanzmann 血小板無力症**的根本原因是 GPIIb/IIIa 受體（整合素 αIIbβ3）的基因缺陷，導致血小板無法正常凝集——這是一個與 TXA2 路徑完全不同的機制層次，水楊酸酯對 GPIIb/IIIa 缺陷並無已知的直接修復或補償作用。

此外，即使理論上的 TXA2 抑制路徑有某種間接影響，Glycol salicylate 以局部外用為主，**全身有效濃度幾乎無法達到臨床相關的抗血小板水準**。機轉連結極為薄弱，預測合理性低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Glycol Salicylate 的不重複許可證共 **54 張**：有效單方 0 張、有效複方 30 張、已註銷 24 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（30 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署成製字第007868號 | 人生舒冷巴佈膏 | L-MENTHOL、DL-CAMPHOR、GLYCOL SALICYLATE、TOCOPHEROL ACETATE AL… | 貼布劑 | 打撲傷、扭挫傷、腰痛、肌肉痛、關節痛、肌肉疲勞 |
| 衛署成製字第008368號 | 人生溫感巴佈膏 | DL-CAMPHOR、GLYCOL SALICYLATE、CAPSICUM EXTRACT、TOCOPHEROL ACE… | 貼布劑 | 打撲傷、扭挫傷、腰痛、肩痛、關節痛、肌肉痛、肌肉疲勞 |
| 衛署藥製字第027581號 | "德山"祛酸痛藥膠布 | L-MENTHOL、THYMOL、CAMPHOR、DIPHENHYDRAMINE、METHYL SALICYLATE、G… | 藥膠布 | 關節痛、神經痛、肩膀酸痛、筋肉痛、扭傷、腰痛、風濕痛、筋骨疲勞。 |
| 衛署藥製字第033156號 | 舒爾痛 | DIPHENHYDRAMINE HCL、DL-CAMPHOR、METHYL SALICYLATE、MENTHOL OIL… | 貼布劑 | 打撲傷，扭挫傷，腰痛肩痛，肌肉痛，關節痛，肌肉疲勞，骨折痛 |
| 衛署藥製字第034140號 | 生春痠痛寧藥膠布 | TOCOPHEROL ACETATE ALPHA (EQ TO VIT E ACETATE) (EQ TO VITAMI… | 藥膠布 | 消炎、鎮痛（筋肉痛、腰痛、神經痛、風濕痛、腰酸背痛、坐骨神經痛、關節痛） |
| 衛署藥製字第035322號 | "港香蘭"撲來貼藥布 | MENTHOL OIL、METHYL SALICYLATE、GLYCOL SALICYLATE | 藥膠布 | 扭挫傷、打撲傷、肌肉痛、關節痛、骨折痛。 |
| 衛署藥製字第036236號 | 摩撒肌噴劑 | METHYL SALICYLATE、GLYCOL SALICYLATE、DL-CAMPHOR、L-MENTHOL | 外用噴液劑 | 肩膀酸痛、腰痛、關節痛、筋肉痛、筋肉疲勞、撞傷、扭傷。 |
| 衛署藥製字第036419號 | "生春"治痛噴劑 | GLYCOL SALICYLATE、METHYL SALICYLATE、CAMPHOR、MENTHOL | 外用液劑 | 筋肉痛、腰痛、肩膀痠痛、打撲傷、挫傷、蚊蟲咬傷。 |
| 衛署藥製字第036460號 | “艾力特”春生油 | CINNAMON OIL (OLEUM CINNAMOMI)、METHYL SALICYLATE、GLYCOL SALI… | 外用液劑 | 捻挫、打撲痛、肌肉疲勞、神經痛、肩痛、昆蟲刺傷、皮膚搔癢 |
| 衛署藥製字第037295號 | 貼可藥布 | CAMPHOR、TOCOPHEROL ACETATE ALPHA (EQ TO VIT E ACETATE) (EQ T… | 藥膠布 | 消炎、鎮痛（筋肉痛、腰痛、神經痛、風濕痛、腰酸背痛、坐骨神經痛、關節痛） |
| 衛署藥製字第037297號 | 美帝喜布藥布 | MENTHOL、MENTHOL、CAMPHOR、CAMPHOR、DIPHENHYDRAMINE HCL、DIPHENHY… | 藥膠布 | 消炎、鎮痛（筋肉痛、腰痛、神經痛、風濕痛、腰酸背痛、坐骨神經痛、關節痛） |
| 衛署藥製字第038310號 | "生春"貼酸明痠痛布 | GLYCOL SALICYLATE、DIPHENHYDRAMINE HCL、DL-CAMPHOR、GLYCYRRHIZI… | 藥膠布 | 腰痛、碰傷、關節痛、筋肉痛、筋肉疲勞、骨折痛 |
| 衛署藥製字第039800號 | 貼利康溫感藥布 | GLYCOL SALICYLATE、TOCOPHEROL ACETATE ALPHA DL-、CAPSICUM EXTR… | 藥膠布 | 暫時緩解局部疼痛。 |
| 衛署藥製字第040204號 | 貼可喜布 | L-MENTHOL、DIPHENHYDRAMINE HCL、TOCOPHEROL ACETATE、DL-CAMPHOR、… | 藥膠布 | 打撲、捻挫、肩膀痠痛、關節痛、筋肉痛、筋肉疲勞、腰痛等症狀。 |
| 衛署藥製字第040515號 | 曼秀雷敦熱力鎮痛藥膠布 | GLYCOL SALICYLATE、NONYLIC-VANILLYLAMIDE、L-MENTHOL | 藥膠布 | 肩痛、腰痛、關節痛、肌肉痛、肌肉疲勞、打撲傷、扭挫傷。 |
| 衛署藥製字第040571號 | 透骨痠痛布 | THYMOL、DL-CAMPHOR、TOCOPHEROL ACETATE ALPHA (EQ TO VIT E ACET… | 藥膠布 | 消炎、鎮痛、（筋肉痛、腰痛、神經痛、風濕痛、腰痠背痛、坐骨神經痛、關節痛） |
| 衛署藥製字第040929號 | 救痛藥布 | GLYCOL SALICYLATE、DL-CAMPHOR、DL-ALPHA-TOCOPHEROL ACETATE、L-M… | 藥膠布 | 打撲、捻挫、腰痛、肩膀痠痛、筋肉痛、筋肉疲勞、關節痛、凍傷。 |
| 衛署藥製字第042767號 | 〝派頓〞舒暢噴劑 | CAMPHOR、L-MENTHOL、METHYL SALICYLATE、GLYCOL SALICYLATE | 外用噴液劑 | 筋肉痛、腰痛、肩膀酸痛、筋肉疲勞、撞傷。 |
| 衛署藥製字第042882號 | 德國薄荷標消炎膏 | TOCOPHEROL ACETATE ALPHA DL-、GLYCOL SALICYLATE、DL-CAMPHOR、L-… | 藥膠布 | 打撲傷、扭挫傷、肌肉痛、肌肉疲勞、腰痛、肩痛、關節痛、骨折痛。 |
| 衛署藥製字第043198號 | 曼秀雷敦熱力鎮痛水性藥膠布溫熱感 | GLYCOL SALICYLATE、CAPSICUM EXTRACT | 藥膠布 | 暫時緩解局部疼痛。 |
| 衛署藥製字第043430號 | "德山"筋來爽藥膠布 | TOCOPHEROL ACETATE ALPHA DL-、GLYCOL SALICYLATE、L-MENTHOL、CAM… | 藥膠布 | 打傷、撞傷、筋肉痛、筋肉疲勞、腰痛、肩痛、關節痛、骨折痛、凍傷。 |
| 衛署藥製字第048163號 | "漁人" 療痛貼藥膠布 | L-MENTHOL、CAMPHOR、TOCOPHEROL ACETATE ALPHA DL-、GLYCOL SALICY… | 藥膠布 | 打傷、撞傷、筋肉痛、筋肉疲勞、腰痛、肩痛、關節痛、骨折痛、凍傷。 |
| 衛署藥製字第049355號 | 〝護民〞緩痛貼藥膠布 | L-MENTHOL、CAMPHOR、TOCOPHEROL ACETATE ALPHA DL-、GLYCOL SALICY… | 藥膠布 | 打傷、撞傷、筋肉痛、筋肉疲勞、腰痛、肩痛、關節痛、骨折痛、凍傷。 |
| 衛署藥製字第049614號 | 〝國品〞療舒貼藥膠布 | TOCOPHEROL ACETATE ALPHA DL-、GLYCOL SALICYLATE、CAMPHOR、L-MEN… | 藥膠布 | 打傷、撞傷、筋肉傷、筋肉疲勞、腰痛、肩痛、關節痛、骨折痛、凍傷。 |
| 衛署藥製字第050257號 | “德山”邁疼溫感貼布 | TOCOPHEROL ACETATE ALPHA DL-、CAPSICUM EXTRACT、GLYCOL SALICYL… | 藥膠布 | 暫時緩解局部疼痛。 |
| 衛署藥輸字第013699號 | 擦勞滅軟膏 | NICOTINIC ACID BENZYL ESTER (BENZYL NICOTINATE)、METHYL SALIC… | 軟膏劑 | 筋肉疲勞、打撲傷、肌肉痛、蟲咬傷 |
| 衛署藥輸字第023545號 | 撒隆適布肌兒帕奇貼片 | GLYCOL SALICYLATE、DL-CAMPHOR、TOCOPHEROL ACETATE、L-MENTHOL | 貼片劑 | 筋肉痛、筋肉疲勞、腰痛、關節痛、肩膀酸痛、跌打損傷。 |
| 衛署藥輸字第025851號 | 清新安摩樂 | CHLORPHENIRAMINE MALEATE、NICOTINIC ACID BENZYL ESTER (BENZYL… | 外用液劑 | 肩頸痠痛、肌肉酸痛、肌肉疲勞、腰痛、瘀青、扭傷、關節痛 |
| 衛部藥製字第059851號 | 曼秀雷敦熱力酸痛藥布 | L-MENTHOL、TOCOPHEROL ACETATE ALPHA DL-、GLYCOL SALICYLATE | 藥膠布 | 腰痛、跌打損傷、扭傷、肩膀酸痛、關節痛、肌肉痛、肌肉疲勞。 |
| 衛部藥輸字第027340號 | 脫酸寧痠痛擦劑 | 4-HYDROXY-3-METHOXYBENZYL NONYLIC ACID AMIDE、L-MENTHOL、GLYCO… | 外用液劑 | 肩膀、頸部痠痛、腰痛、筋肉痛、肌肉疲勞、關節痛、瘀傷、骨折痛、扭傷。 |

<details><summary><strong>已註銷</strong>（24 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署成製字第003380號</td><td>歡喜巴斯</td><td>BORNEOL、METHYL SALICYLATE、D-CAMPHOR、GLYCOL SALICYLATE、ZINC O…</td><td>2000/01/03</td></tr><tr><td>衛署成製字第009438號</td><td>熱龍巴布</td><td>DL-CAMPHOR、GLYCOL SALICYLATE、CAPSICUM EXTRACT、TOCOPHEROL ACE…</td><td>2015/01/15</td></tr><tr><td>衛署藥製字第025651號</td><td>春生油</td><td>CLOVE OIL、CAMPHOR、L-MENTHOL、DIPHENHYDRAMINE HCL、CAPSICUM TIN…</td><td>1993/10/27</td></tr><tr><td>衛署藥製字第032109號</td><td>貼可藥膠布</td><td>CAMPHOR、MENTHOL、GLYCOL SALICYLATE、METHYL SALICYLATE</td><td>1994/06/14</td></tr><tr><td>衛署藥製字第032110號</td><td>美帝喜布藥膠布</td><td>CAMPHOR、MENTHOL、TOCOPHEROL ACETATE、GLYCOL SALICYLATE、DIPHENH…</td><td>1994/06/22</td></tr><tr><td>衛署藥製字第038086號</td><td>救筋酸痛布</td><td>GLYCOL SALICYLATE、METHYL SALICYLATE、MENTHOL OIL、MENTHOL、TOCO…</td><td>1997/03/06</td></tr><tr><td>衛署藥製字第038309號</td><td>福貼藥布</td><td>CAMPHOR、MENTHOL、MENTHA OIL、THYMOL、TOCOPHEROL ACETATE、GLYCOL…</td><td>2015/01/15</td></tr><tr><td>衛署藥製字第038322號</td><td>樂貼藥布</td><td>GLYCOL SALICYLATE、METHYL SALICYLATE、DIPHENHYDRAMINE、TOCOPHER…</td><td>2015/01/15</td></tr><tr><td>衛署藥製字第039768號</td><td>抗痛舒佈藥膠布</td><td>GLYCOL SALICYLATE、TOCOPHEROL ACETATE ALPHA DL-、L-MENTHOL、DL-…</td><td>1997/06/21</td></tr><tr><td>衛署藥製字第047842號</td><td>三箭水性鎮痛藥膏布</td><td>GLYCOL SALICYLATE、TOCOPHEROL (ACETATE ALPHA DL- )、L-MENTHOL、…</td><td>2017/02/09</td></tr><tr><td>衛署藥製字第049171號</td><td>〝美善滅酸疼〞溫感貼布</td><td>DL-CAMPHOR、GLYCOL SALICYLATE、TOCOPHEROL ACETATE ALPHA DL-、CA…</td><td>2016/09/10</td></tr><tr><td>衛署藥輸字第018206號</td><td>脫酸寧透明藥布</td><td>DL-CAMPHOR、MENTHA OIL、L-MENTHOL、GLYCOL SALICYLATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第018475號</td><td>三共藥布劑</td><td>DIPHENHYDRAMINE SALICYLATE、L-MENTHOL、GLYCOL SALICYLATE、ROSSK…</td><td>2006/02/24</td></tr><tr><td>衛署藥輸字第019083號</td><td>脫酸寧Ａ藥布</td><td>METHYL SALICYLATE、GLYCOL SALICYLATE、L-MENTHOL、DL-CAMPHOR、TOC…</td><td>2019/04/16</td></tr><tr><td>衛署藥輸字第019787號</td><td>日本三笠藥膠布Ｇ</td><td>GLYCOL SALICYLATE、DIPHENHYDRAMINE HCL、DL-CAMPHOR、MENTHA OIL、…</td><td>2010/09/17</td></tr><tr><td>衛署藥輸字第020500號</td><td>善必克貼布劑</td><td>L-MENTHOL、N-NONANOYL VANILLYLAMIDE、DL-CAMPHOR、DIPHENHYDRAMIN…</td><td>2004/05/11</td></tr><tr><td>衛署藥輸字第020601號</td><td>日本祐德巴斯貼布劑</td><td>L-MENTHOL、GLYCOL SALICYLATE</td><td>2014/04/24</td></tr><tr><td>衛署藥輸字第020734號</td><td>脫酸寧濕布Ａ貼片劑</td><td>GLYCOL SALICYLATE、L-MENTHOL、PHELLODENDRON BARK POWDER (EQ TO…</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第021138號</td><td>大正愛舒酸痛貼布</td><td>DL-MENTHOL、TOCOPHEROL ACETATE ALPHA DL-、GLYCOL SALICYLATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第022347號</td><td>撒隆適布</td><td>DL-CAMPHOR、L-MENTHOL、GLYCOL SALICYLATE、TOCOPHEROL ACETATE AL…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第022601號</td><td>大正愛舒酸痛貼布</td><td>DL-MENTHOL、GLYCOL SALICYLATE、TOCOPHEROL ACETATE ALPHA DL-</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第023307號</td><td>脫酸寧－Ａ擦劑</td><td>GLYCYRRHIZINIC ACID (EQ TO GLYCYRRHETINIC ACID GLYCOSIDE)(EQ…</td><td>2018/03/15</td></tr><tr><td>衛署藥輸字第023451號</td><td>脫酸寧濕布</td><td>L-MENTHOL、GLYCOL SALICYLATE</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第024820號</td><td>撒隆巴斯-益 噴劑</td><td>L-MENTHOL、EUCALYPTUS OIL (OLEUM EUCALYPTI)、DL-CAMPHOR、GLYCYR…</td><td>2024/04/29</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
所有 10 個 TxGNN 預測適應症均為 L5 等級（純模型預測，零臨床試驗、零文獻支持），且最高排名的預測 Glanzmann 血小板無力症與本藥的外用局部止痛機轉毫無合理對應關係——一個皮膚貼布無法有效治療 GPIIb/IIIa 基因缺陷造成的血液疾病。預測清單中另有多個血液凝固疾病（血栓傾向症、抗凝血酶缺乏等），機轉支持同樣極弱。

**若要推進需要：**

- 確認 Glycol salicylate 的完整藥理機轉（MOA）資料，尤其是全身性吸收數據
- 評估是否存在可改變給藥途徑的研究配方（口服/注射），以產生足夠的全身暴露量
- 針對任何候選適應症，需先完成前臨床（體外/動物）機轉驗證研究，才能考慮進入 L4 以上的評估階段
- 本藥現有適應症為局部肌肉骨骼疼痛，建議優先評估其他同為局部或炎症機轉相關的預測適應症，而非罕見血液疾病

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表皆為複方，3 張已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

