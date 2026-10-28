---
layout: default
title: Salicylamide
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-16
description: "Salicylamide：預測新適應症為咽炎 (Pharyngitis)（證據等級 L4）。原適應症：鎮痛藥"
monitor_inn: "Salicylamide"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "allergic urticaria", "lung disease", "massive neonatal aspiration syndrome", "respiratory syncytial virus bronchiolitis", "hantavirus infectious disease"]
---

# Salicylamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Salicylamide：從解熱鎮痛到咽炎
{: .text-alpha }

## 一句話總結

Salicylamide（水楊醯胺）是水楊酸類的解熱鎮痛藥，原本用於緩解疼痛與發熱。
TxGNN 模型預測它可能對**咽炎 (Pharyngitis)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇** 1953 年的病例系列文獻，證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鎮痛藥 |
| 預測新適應症 | 咽炎 (Pharyngitis) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 30 張／共 117 張） |
| 許可證數 | 117 張（有效單方 1／有效複方 29／已過期 2／已註銷 85） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Salicylamide 屬於水楊酸類解熱鎮痛藥，一般認為可能透過抑制前列腺素合成來緩解疼痛與發熱，但此說法並非來自本次彙整的機轉資料，僅為推論。

咽炎的主要症狀是喉嚨痛與發熱，與 Salicylamide 的既有適應症（解熱、鎮痛、緩解咽喉痛等）有重疊。因此模型預測的方向在症狀緩解層面上說得通。值得注意的是，台灣已核准的複方產品，其適應症已包含「咽喉痛」的緩解。

不過，這代表的是**症狀緩解**，而非針對咽炎病因的治療。支持證據僅有一篇 1953 年的義大利文報告（以 Salicylamide 搭配對胺基苯甲酸鈉治療嬰兒卡他性扁桃腺炎），無摘要，且年代久遠。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [13060598](https://pubmed.ncbi.nlm.nih.gov/13060598/) | 1953 | 病例系列 | Gazzetta medica italiana | 以 Salicylamide 合併對胺基苯甲酸鈉治療嬰兒卡他性扁桃腺炎（無摘要，細節不明） |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Salicylamide 的不重複許可證共 **117 張**：有效單方 1 張、有效複方 29 張、已過期 2 張（未註銷但有效日期早於資料集日期）、已註銷 85 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027398號 | 水楊醯胺 | （粉） | 丞泰企業有限公司 | 2028/02/27 | 鎮痛藥 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（29 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第000977號 | 小兒寶理熱顆粒 | BROMISOVALUM ( EQ TO BROMOVALERYLUREA) ( EQ TO BROMVALETONE)… | 內服顆粒劑 | 緩解感冒之各種症狀（咽喉痛、發燒、頭痛、關節痛、肌肉痛、流鼻水、鼻塞、打噴嚏）。 |
| 內衛藥製字第001097號 | "生達" 克風膠囊 | THIAMINE MONONITRATE、DEXTROMETHORPHAN HBR、SALICYLAMIDE、CHLOR… | 膠囊劑 | 緩解感冒之各種症狀（咽喉痛、發燒、頭痛、關節痛、肌肉痛、流鼻水、鼻塞、打噴嚏、咳嗽）。 |
| 衛署藥製字第001535號 | 舒舒感冒膠囊 | ACETAMINOPHEN (EQ TO PARACETAMOL)、CHLORPHENIRAMINE MALEATE、A… | 膠囊劑 | 感冒諸症狀（鼻塞、流鼻水、打噴嚏、咽喉痛、咳嗽、發熱、頭痛、關節痛、肌肉痛）之緩解 |
| 衛署藥製字第005741號 | 鎮風能膠囊"天良" | DL-METHYLEPHEDRINE HCL、ASCORBIC ACID (VIT C)、CHLORPHENIRAMIN… | 膠囊劑 | 感冒諸症狀（鼻塞、流鼻水、打噴嚏、咽喉痛、咳嗽、發熱、頭痛、關節痛、肌肉痛）之緩解 |
| 衛署藥製字第015564號 | 風達賜康膠囊 | PROMETHAZINE HCL、CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO PAR… | 膠囊劑 | 緩解感冒之各種症狀（頭痛、發燒、咽喉痛、關節痛、肌肉痛、流鼻水、鼻塞、打噴嚏） |
| 衛署藥製字第016042號 | 疼痛寧顆粒 | SALICYLAMIDE、CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO PARACET… | 內服顆粒劑 | 緩解感冒之各種症狀(流鼻水、鼻塞、打噴嚏、咽喉痛、咳嗽、畏寒、發燒、頭痛、關節痛、肌肉酸痛) |
| 衛署藥製字第016098號 | 屢克感膠囊 | SALICYLAMIDE、CHLORPHENIRAMINE MALEATE、CAFFEINE ANHYDROUS、ETH… | 膠囊劑 | 緩解感冒之各種症狀（咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉痠痛、流鼻水、鼻塞、打噴嚏、咳嗽、喀痰) |
| 衛署藥製字第016865號 | "健康"宜幼感冒顆粒 | ACETAMINOPHEN (EQ TO PARACETAMOL)、CAFFEINE ANHYDROUS、SALICYL… | 內服顆粒劑 | 緩解感冒之各種症狀（流鼻水、鼻塞、打噴嚏、咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛）。 |
| 衛署藥製字第017384號 | 快好感冒寧膠囊 | ASCORBIC ACID (VIT C)、DL-METHYLEPHEDRINE HCL、SALICYLAMIDE、CA… | 膠囊劑 | 感冒諸症狀（流鼻水、鼻塞、打噴嚏、發熱、頭痛、咽喉痛、咳嗽、喀痰）之緩解 |
| 衛署藥製字第017543號 | 感冒治膠囊 | SALICYLAMIDE、CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO P… | 膠囊劑 | 緩解感冒之各種症狀（咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛、流鼻水、鼻塞、打噴嚏）。 |
| 衛署藥製字第017936號 | 感冒一刻能膠囊 | CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO PARACETAMOL)、C… | 膠囊劑 | 緩解感冒之各種症狀（鼻塞、流鼻水、打噴嚏、咽喉痛、發燒、頭痛、關節痛、肌肉痛） |
| 衛署藥製字第017966號 | "約克" 感冒克膠囊 | PSEUDOEPHEDRINE HCL、CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (… | 膠囊劑 | 緩解感冒之各種症狀（咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛、流鼻水、鼻塞、打噴嚏） |
| 衛署藥製字第019225號 | 感安膠囊 | DL-METHYLEPHEDRINE HCL、ALUMINUM BIS(ACETYLSALICYLATE)(ALUMIN… | 膠囊劑 | 感冒諸症狀（鼻塞、流鼻水、打噴嚏、咽喉痛、發燒、頭痛、關節痛、肌肉痛）。 |
| 衛署藥製字第019669號 | 〝美西〞甜兒菜感冒熱飲顆粒 | CHLORPHENIRAMINE MALEATE、SALICYLAMIDE、ACETAMINOPHEN (EQ TO P… | 內服顆粒劑 | 緩解感冒之各種症狀（咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛、流鼻水、鼻塞、打噴嚏）。 |
| 衛署藥製字第020566號 | 濕而宜膠囊 | ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE | 膠囊劑 | 退燒、止痛（緩解頭痛、牙痛、咽喉痛、關節痛、神經痛、肌肉酸痛、月經痛）。 |
| 衛署藥製字第021023號 | "長安"痛妙舒錠 | ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE | 錠劑 | 退燒、止痛（頭痛、牙痛、咽喉痛、關節痛、神經痛、肌肉酸痛、月經痛）。 |
| 衛署藥製字第021206號 | 勿痛顆粒 | SALICYLAMIDE、CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO P… | 內服顆粒劑 | 緩解感冒之各種症狀（流鼻水、鼻塞、打噴嚏、咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛）。 |
| 衛署藥製字第022383號 | "生達"安治痛錠 | SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL) | 錠劑 | 退燒、止痛(緩解頭痛、牙痛、咽喉痛、關節痛、神經痛、肌肉酸痛、月經痛)。 |
| 衛署藥製字第025209號 | "十全"康福膠囊 | PSEUDOEPHEDRINE HCL、ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICY… | 膠囊劑 | 緩解感冒之各種症狀（鼻塞、流鼻水、打噴嚏、咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛）。 |
| 衛署藥製字第026595號 | 能風治糖衣錠 | CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYL… | 糖衣錠 | 緩解感冒之各種症狀(流鼻水、鼻塞、打噴嚏、咽喉痛、咳嗽、喀痰、畏寒、頭痛、發燒、關節痛、肌肉酸痛。） |
| 衛署藥製字第028124號 | 止痛寧散 | SALICYLAMIDE、CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO PARACET… | 粉劑 | 緩解感冒之各種症狀（頭痛、肌肉痛、關節痛、鼻塞，流鼻水，打噴嚏，咽喉痛，發燒） |
| 衛署藥製字第028125號 | 三應效散 | DL-METHYLEPHEDRINE HCL、ALUMINUM BIS(ACETYLSALICYLATE)(ALUMIN… | 粉劑 | 感冒諸症狀（鼻塞、流鼻水、打噴嚏、咽喉痛、咳嗽、喀痰、發熱、頭痛）之緩解 |
| 衛署藥製字第029959號 | 感冒克膠囊 | CAFFEINE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CHLORPHENIRAMINE… | 膠囊劑 | 緩解感冒之各種症狀（咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛、流鼻水、鼻塞、打噴嚏）。 |
| 衛署藥製字第031762號 | 三克定膠囊 | DL-METHYLEPHEDRINE HCL、ASCORBIC ACID (VIT C)、ACETAMINOPHEN (… | 膠囊劑 | 緩解感冒之各種症狀（咽喉痛、發燒、頭痛、關節痛、肌肉痛、流鼻水、鼻塞、打噴嚏） |
| 衛署藥製字第039056號 | 愛斯風克膜衣錠〝井田〞 | SALICYLAMIDE、CAFFEINE HYDRATE、NOSCAPINE HCL、ASCORBIC ACID (V… | 膜衣錠 | 緩解感冒之各種症狀（鼻塞、流鼻水、打噴嚏、咳嗽、咽喉痛、發燒、頭痛、關節痛、肌肉痛） |
| 衛署藥製字第041009號 | 〝派頓〞風友寧顆粒 | CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO PARACETAMOL)、S… | 內服顆粒劑 | 緩解感冒之各種症狀（流鼻水、鼻塞、打噴嚏、咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛）。 |
| 衛署藥製字第042913號 | 利痛膠囊 | ACETAMINOPHEN (EQ TO PARACETAMOL)、CAFFEINE ANHYDROUS、SALICYL… | 膠囊劑 | 退燒、止痛（緩解頭痛、牙痛、咽喉痛、關節痛、神經痛、肌肉酸痛、月經痛）。 |
| 衛署藥製字第049602號 | 鎮熱痛膠囊 | THIAMINE MONONITRATE、SALICYLAMIDE、CHLORPHENIRAMINE MALEATE、R… | 膠囊劑 | 緩解感冒之各種症狀(流鼻水、鼻塞、打噴嚏、咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛)。 |
| 衛署藥製字第051525號 | “新喜”感平膠囊 | PROMETHAZINE METHYLENDISALICYLATE、SALICYLAMIDE、ACETAMINOPHEN… | 膠囊劑 | 緩解感冒之各種症狀(鼻塞、流鼻水、打噴嚏、咽喉痛、發燒、頭痛、關節痛、肌肉痛)。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第010479號</td><td>澎湃膠囊</td><td>ASCORBIC ACID、ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE…</td><td>2024/05/25</td></tr><tr><td>衛署藥製字第024842號</td><td>"元宙"益風感膠囊</td><td>SALICYLAMIDE、CHLORPHENIRAMINE MALEATE、PSEUDOEPHEDRINE HCL、AC…</td><td>2024/05/25</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（85 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000054號</td><td>必定片</td><td>PROPYPHENAZONE (ISOPROPYPHENAZONE)、SALICYLAMIDE、CHLORPHENIRA…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第000961號</td><td>“新喜”感平膠囊</td><td>PROMETHAZINE HCL (METHYLENEDISALICYLATE)、SALICYLAMIDE、ACETAM…</td><td>2009/10/21</td></tr><tr><td>內衛藥製字第001888號</td><td>"美西"小兒必治安顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、PROMETHAZINE METHYLENDISAL…</td><td>2023/07/24</td></tr><tr><td>內衛藥製字第005041號</td><td>水楊胺錠５００公絲</td><td>SALICYLAMIDE</td><td>1989/11/27</td></tr><tr><td>內衛藥製字第007311號</td><td>柳酸醯胺</td><td>SALICYLAMIDE</td><td>2006/04/19</td></tr><tr><td>內衛藥製字第010253號</td><td>"正峰" 柳醯胺</td><td>SALICYLAMIDE</td><td>2023/08/23</td></tr><tr><td>內衛藥製字第010390號</td><td>感冒治糖衣片</td><td>CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO PARACETAMOL)、C…</td><td>2006/04/19</td></tr><tr><td>內衛藥製字第014286號</td><td>"瑞士"驅痛寧片</td><td>CAFFEINE、SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL)、PHEN…</td><td>2023/04/11</td></tr><tr><td>內衛藥製字第015346號</td><td>呼通片</td><td>SALICYLAMIDE、DIPHENYLPYRALINE HCL、NYLIDRIN HCL ( BUPHENIN HY…</td><td>2013/06/10</td></tr><tr><td>內衛藥輸字第001095號</td><td>佐利麥</td><td>SALICYLAMIDE</td><td>1986/01/06</td></tr><tr><td>內衛藥輸字第001661號</td><td>爽樂片</td><td>ASCORBIC ACID (VIT C)、SALICYLAMIDE、PARA-AMINOBENZOIC ACID (V…</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第002918號</td><td>水楊酸醯胺</td><td>SALICYLAMIDE</td><td>1987/03/27</td></tr><tr><td>內衛藥輸字第003840號</td><td>百朗顆粒</td><td>SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CAFFEINE ANHY…</td><td>1984/10/09</td></tr><tr><td>內衛藥輸字第005351號</td><td>柳酸胺</td><td>SALICYLAMIDE</td><td>1985/09/16</td></tr><tr><td>內衛藥輸字第005774號</td><td>效特齡</td><td>CHLORPHENIRAMINE MALEATE、PHENACETIN (ACETOPHENETIDIN)、APRONA…</td><td>2004/12/23</td></tr><tr><td>內衛藥輸字第005905號</td><td>水楊醯胺</td><td>SALICYLAMIDE</td><td>1985/10/23</td></tr><tr><td>內衛藥輸字第007268號</td><td>柳酸胺</td><td>SALICYLAMIDE</td><td>1986/04/22</td></tr><tr><td>衛署成製字第003207號</td><td>風熱散</td><td>SALICYLAMIDE</td><td>2022/05/05</td></tr><tr><td>衛署藥製字第000917號</td><td>定風膠囊</td><td>NOSCAPINE HCL、CHLORPHENIRAMINE MALEATE、SALICYLAMIDE、ACETAMIN…</td><td>2016/06/23</td></tr><tr><td>衛署藥製字第003706號</td><td>復新錠</td><td>SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL)</td><td>2013/06/10</td></tr><tr><td>衛署藥製字第005506號</td><td>水楊酸胺</td><td>SALICYLAMIDE</td><td>2023/07/18</td></tr><tr><td>衛署藥製字第007753號</td><td>停風膠囊</td><td>CHLORPHENIRAMINE MALEATE、DL-METHYLEPHEDRINE HCL、ASCORBIC ACI…</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第009270號</td><td>易而善感冒膠囊</td><td>ASCORBIC ACID (VIT C)、DL-METHYLEPHEDRINE HCL、CHLORPHENIRAMIN…</td><td>2015/07/02</td></tr><tr><td>衛署藥製字第010596號</td><td>穩克感錠</td><td>SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CAFFEINE ANHY…</td><td>2015/07/02</td></tr><tr><td>衛署藥製字第015020號</td><td>派感膠囊</td><td>ALUMINUM BIS(ACETYLSALICYLATE)(ALUMINUM ACETYLSALICYLA、DL-ME…</td><td>1998/11/16</td></tr><tr><td>衛署藥製字第016180號</td><td>加蒙膠囊</td><td>CHLORPHENIRAMINE MALEATE、ALUMINUM BIS(ACETYLSALICYLATE)(ALUM…</td><td>2017/08/24</td></tr><tr><td>衛署藥製字第017484號</td><td>痛快散</td><td>SALICYLAMIDE、CAFFEINE ANHYDROUS、DIHYDROXYALUMINUM AMINOACETA…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第017549號</td><td>祝爾安感冒散</td><td>CHLORPHENIRAMINE MALEATE、SALICYLAMIDE、ACETAMINOPHEN (EQ TO P…</td><td>2015/07/01</td></tr><tr><td>衛署藥製字第017565號</td><td>感冒膠囊</td><td>PSEUDOEPHEDRINE HCL、CHLORPHENIRAMINE MALEATE、SALICYLAMIDE、AC…</td><td>1993/06/22</td></tr><tr><td>衛署藥製字第017587號</td><td>小兒感冒藥顆粒</td><td>CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO PARACETAMOL)、C…</td><td>2009/06/12</td></tr><tr><td>衛署藥製字第017766號</td><td>滅傷風錠</td><td>CHLORPHENIRAMINE MALEATE、DL-METHYLEPHEDRINE HCL、ASCORBIC ACI…</td><td>2016/09/07</td></tr><tr><td>衛署藥製字第017895號</td><td>醫濕錠</td><td>SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL)</td><td>1995/12/29</td></tr><tr><td>衛署藥製字第017942號</td><td>感風膠囊</td><td>ALUMINUM BIS(ACETYLSALICYLATE)(ALUMINUM ACETYLSALICYLA、DL-ME…</td><td>1991/04/01</td></tr><tr><td>衛署藥製字第018148號</td><td>治痛顆粒</td><td>SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CHLORPHENIRAM…</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第018324號</td><td>風敵膠囊</td><td>CHLORPHENIRAMINE MALEATE、SALICYLAMIDE、ACETAMINOPHEN (EQ TO P…</td><td>1994/11/16</td></tr><tr><td>衛署藥製字第018325號</td><td>風敵錠</td><td>SALICYLAMIDE、CAFFEINE ANHYDROUS、CHLORPHENIRAMINE MALEATE、ACE…</td><td>1994/11/16</td></tr><tr><td>衛署藥製字第018456號</td><td>"美西"感冒膠囊</td><td>ALUMINUM BIS(ACETYLSALICYLATE)(ALUMINUM ACETYLSALICYLA、DL-ME…</td><td>2025/07/29</td></tr><tr><td>衛署藥製字第018484號</td><td>世感安膠囊</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、PSEUDOEPHEDRINE HCL、SALICY…</td><td>1998/06/08</td></tr><tr><td>衛署藥製字第019399號</td><td>立分能散</td><td>CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO PARACETAMOL)、S…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第019693號</td><td>風邪膠囊</td><td>ASCORBIC ACID (VIT C)、SALICYLAMIDE、CHLORPHENIRAMINE MALEATE、…</td><td>1995/12/29</td></tr><tr><td>衛署藥製字第019729號</td><td>雅治感膠囊</td><td>CHLORPHENOXAMINE MALEATE、SALICYLAMIDE、CAFFEINE ANHYDROUS、ETH…</td><td>2016/09/19</td></tr><tr><td>衛署藥製字第020224號</td><td>"人生"必治僂糖衣錠</td><td>SALICYLAMIDE、ASPIRIN</td><td>2026/08/17</td></tr><tr><td>衛署藥製字第020272號</td><td>克風感冒糖漿</td><td>CAFFEINE ANHYDROUS、SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACET…</td><td>1992/04/13</td></tr><tr><td>衛署藥製字第020307號</td><td>感冒克膠囊</td><td>CHLORPHENIRAMINE MALEATE、SALICYLAMIDE、PHENACETIN (ACETOPHENE…</td><td>1989/11/21</td></tr><tr><td>衛署藥製字第020644號</td><td>三克定膠囊”三合興”　　　　　　　　　　　　　　　　　　　　 S</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE、CAFFEINE ANHY…</td><td>1990/05/01</td></tr><tr><td>衛署藥製字第020823號</td><td>感冒膠囊</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE、ETHAVERINE HC…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第020905號</td><td>克痛錠（水楊酸胺）</td><td>SALICYLAMIDE</td><td>1990/02/09</td></tr><tr><td>衛署藥製字第021456號</td><td>風感必安顆粒</td><td>CHLORPHENIRAMINE MALEATE、SALICYLAMIDE、ACETAMINOPHEN (EQ TO P…</td><td>2026/08/03</td></tr><tr><td>衛署藥製字第022311號</td><td>克冒平糖衣錠</td><td>CAFFEINE ANHYDROUS、GLYCYRRHIZA (LIQUORICE)、ACETAMINOPHEN (EQ…</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第022498號</td><td>〝應元〞平烈風膠囊</td><td>CHLORPHENIRAMINE MALEATE、DL-METHYLEPHEDRINE HCL、ALUMINUM BIS…</td><td>2010/03/18</td></tr><tr><td>衛署藥製字第022601號</td><td>速克風錠</td><td>CHLORPHENIRAMINE MALEATE、HOMATROPINE METHYLBROMIDE、PHENYLPRO…</td><td>2006/01/23</td></tr><tr><td>衛署藥製字第022707號</td><td>"恆安"綜合感冒膠囊</td><td>PSEUDOEPHEDRINE HCL、ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICY…</td><td>2015/01/22</td></tr><tr><td>衛署藥製字第022939號</td><td>益斯得寧錠</td><td>ASPIRIN、SALICYLAMIDE、CAFFEINE、ACETAMINOPHEN (EQ TO PARACETAM…</td><td>1993/07/06</td></tr><tr><td>衛署藥製字第023826號</td><td>感風兒顆粒</td><td>CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (EQ TO PARACETAMOL)、S…</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第024934號</td><td>利濕安錠</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE</td><td>1998/11/10</td></tr><tr><td>衛署藥製字第025303號</td><td>安汝風錠</td><td>SALICYLAMIDE、PHENYLPROPANOLAMINE HCL (DL-NOREPHEDRINE HCL)、A…</td><td>1920/10/08</td></tr><tr><td>衛署藥製字第028975號</td><td>克風邪感冒膠囊</td><td>ASCORBIC ACID (VIT C)、DL-METHYLEPHEDRINE HCL、SALICYLAMIDE、CA…</td><td>1990/05/18</td></tr><tr><td>衛署藥製字第029284號</td><td>感冒錠</td><td>CAFFEINE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CHLORPHENIRAMINE…</td><td>1993/07/16</td></tr><tr><td>衛署藥製字第029429號</td><td>風風顆粒</td><td>CAFFEINE ANHYDROUS、CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (E…</td><td>2023/07/07</td></tr><tr><td>衛署藥製字第029703號</td><td>治傷風錠</td><td>CHLORPHENIRAMINE MALEATE、DL-METHYLEPHEDRINE HCL、ALUMINUM BIS…</td><td>2015/04/17</td></tr><tr><td>衛署藥製字第029869號</td><td>感冒液</td><td>CAFFEINE ANHYDROUS、SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACET…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第032150號</td><td>"救人" 克風邪感冒膠囊</td><td>SALICYLAMIDE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CAFFEINE、ASCO…</td><td>2023/07/12</td></tr><tr><td>衛署藥製字第033267號</td><td>感風膠囊</td><td>SALICYLAMIDE、CAFFEINE、CHLORPHENIRAMINE MALEATE、ETHENZAMIDE (…</td><td>2012/05/04</td></tr><tr><td>衛署藥製字第034976號</td><td>益斯得寧錠</td><td>CAFFEINE、ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE、ASPI…</td><td>1997/07/23</td></tr><tr><td>衛署藥製字第035877號</td><td>風友寧顆粒</td><td>CHLORPHENIRAMINE MALEATE、CAFFEINE ANHYDROUS、ACETAMINOPHEN (E…</td><td>1997/08/05</td></tr><tr><td>衛署藥製字第036225號</td><td>感冒錠</td><td>CAFFEINE、ACETAMINOPHEN (EQ TO PARACETAMOL)、SALICYLAMIDE、CHLO…</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第036306號</td><td>感冒膠囊</td><td>SALICYLAMIDE、PSEUDOEPHEDRINE HCL、CHLORPHENIRAMINE MALEATE、AC…</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第000803號</td><td>水楊酸胺</td><td>SALICYLAMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002047號</td><td>水楊醯胺</td><td>SALICYLAMIDE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第002087號</td><td>愛膚外用液</td><td>RESORCINOL ACETATE、CHLORAMPHENICOL、ISOPROPYL ALCOHOL (2-PROP…</td><td>1987/04/21</td></tr><tr><td>衛署藥輸字第002307號</td><td>水楊酸胺</td><td>SALICYLAMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004638號</td><td>水楊酸醯胺</td><td>SALICYLAMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第004887號</td><td>柳酸胺</td><td>SALICYLAMIDE</td><td>1994/06/10</td></tr><tr><td>衛署藥輸字第007716號</td><td>水楊酸胺</td><td>SALICYLAMIDE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第011013號</td><td>水楊酸胺粉劑</td><td>SALICYLAMIDE</td><td>2004/04/28</td></tr><tr><td>衛署藥輸字第012415號</td><td>依爾克風糖衣錠</td><td>CAFFEINE HYDRATE、BROMPHENIRAMINE MALEATE、SALICYLAMIDE、PROPYP…</td><td>1992/12/23</td></tr><tr><td>衛署藥輸字第014004號</td><td>柳酸胺粉劑</td><td>SALICYLAMIDE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014243號</td><td>水楊醯胺</td><td>SALICYLAMIDE</td><td>1993/04/03</td></tr><tr><td>衛署藥輸字第014384號</td><td>柳酸胺</td><td>SALICYLAMIDE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第014609號</td><td>水楊酸胺</td><td>SALICYLAMIDE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第014835號</td><td>柳酸胺</td><td>SALICYLAMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015757號</td><td>愛膚外用液</td><td>CHLORAMPHENICOL、RESORCINOL ACETATE、SALICYLAMIDE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第019725號</td><td>水楊醯胺</td><td>SALICYLAMIDE</td><td>2016/05/19</td></tr><tr><td>衛署藥輸字第020852號</td><td>水楊酸胺</td><td>SALICYLAMIDE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第021795號</td><td>水陽酸胺</td><td>SALICYLAMIDE</td><td>2005/06/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：本次彙整的資料中查無相關紀錄。

**知識圖譜標示的潛在禁忌疾病**（來自藥物－疾病關聯推論，並非仿單文字），包括：
- 肝臟：肝衰竭、肝病、膽囊疾病
- 腎臟：腎病
- 消化道：消化性潰瘍、胃炎、發炎性腸病、困難梭狀芽孢桿菌結腸炎
- 血液與凝血：血小板減少、凝血疾病、血友病、貧血（含巨球性貧血）
- 心血管與呼吸：高血壓、低血壓、慢性阻塞性肺病
- 內分泌代謝：糖尿病、糖尿病酮酸中毒、甲狀腺功能低下、黏液水腫、先天性甲狀腺功能低下、缺鉀、痛風
- 其他：癲癇、失眠、良性攝護腺增生、藥物濫用／依賴

此外，檢索到的文獻提示一些需留意的安全訊號：
- 1996 年有含 Salicylamide 的感冒複方（另含乙醯胺酚、咖啡因等）併用抗生素後，發生藥物誘發溶血性貧血合併顆粒球缺乏症的個案報告。
- 另有 Salicylamide 過量中毒的病例報告。

詳細警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數雖高，但實證僅有一篇 1953 年、無摘要的病例系列，沒有任何臨床試驗。
- 咽炎的合理性主要來自一般解熱鎮痛的症狀緩解，並非新的治療機會；且已有含 Salicylamide 的複方在台灣核准緩解咽喉痛。

**若要推進需要：**
- 取得作用機轉資料（MOA），釐清與咽炎的機轉關聯。
- 取得 1953 年原始報告全文，並檢索較新的臨床證據。
- 若要進一步研究，需設計對照試驗，評估咽喉痛與發熱的症狀緩解效果，並與現有解熱鎮痛藥比較。
- 針對肝腎功能不全、血液疾病、消化道潰瘍等族群，制定安全性評估與監測計畫。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「人生」必治僂糖衣錠狀態寫有效 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

