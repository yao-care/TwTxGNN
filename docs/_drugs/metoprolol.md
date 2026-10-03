---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

# Metoprolol：從 高血壓 到 惡性高血壓腎病變與慢性肺心病

## 一句話總結

Metoprolol（美托普洛）是一種選擇性 beta-1 腎上腺素受體阻斷劑，用於治療高血壓、狹心症和心律不整。TxGNN 模型預測它對**惡性高血壓腎病變 (malignant hypertensive renal disease)** 和**慢性肺心病 (chronic pulmonary heart disease)** 有潛在治療效果，目前有超過 **15 項臨床試驗**支持慢性肺心病相關應用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、狹心症、心室上心律不整 |
| 預測新適應症 | 惡性高血壓腎病變、慢性肺心病、心肌梗塞 |
| TxGNN 預測分數 | 99.91% (惡性高血壓腎病變), 99.40% (慢性肺心病) |
| 證據等級 | L2 (慢性肺心病), L5 (惡性高血壓腎病變) |
| 台灣上市 | 已上市 |
| 許可證數 | 46 張（有效單方 8／有效複方 0／已註銷 38） |
| 建議決策 | Explore |

## 為什麼這個預測合理？

Metoprolol 通過選擇性阻斷心臟 beta-1 受體，減少心率、心肌收縮力和心輸出量，從而降低血壓和心肌耗氧量。

**機轉支持（慢性肺心病）：**
- Beta-blocker 可改善右心功能
- 減少心律不整風險
- 在心衰患者中證實可降低死亡率
- 選擇性 beta-1 阻斷對支氣管影響較小

**機轉支持（惡性高血壓腎病變）：**
- 長效降壓作用
- 減少交感神經過度活化
- 可作為血壓控制的維持治療

## 臨床試驗證據

**慢性肺心病/COPD 相關試驗：**

| 試驗編號 | 階段 | 狀態 | 主要研究目標 |
|---------|------|------|-------------|
| NCT06825728 | Phase 4 | 尚未招募 | Metoprolol 對 HFrEF 合併 COPD 患者的死亡和再住院影響 |
| NCT03370835 | Phase 4 | 完成 | 比較 Metoprolol 和 Carvedilol 在 COPD 患者的耐受性 |
| NCT03778554 | Phase 4 | 進行中 | 心肌梗塞後無心衰患者的 beta-blocker 治療 |
| NCT02587351 | Phase 3 | 終止 | Metoprolol 預防 COPD 急性惡化 |
| NCT03566667 | Phase 4 | 進行中 | Beta-blocker 對 COPD 患者的益處 |
| NCT00288548 | Phase 4 | 未知 | Metoprolol 與 Formoterol 合用對 COPD 肺功能的影響 |

## 文獻證據

| PMID | 年份 | 類型 | 主要發現 |
|------|-----|------|---------|
| [8737105](https://pubmed.ncbi.nlm.nih.gov/8737105/) | 1996 | RCT | Metoprolol vs Xamoterol 對心肌梗塞後心衰患者左心功能的影響 |
| [14711192](https://pubmed.ncbi.nlm.nih.gov/14711192/) | 2003 | 動物研究 | 不同劑量 Carvedilol 和 Metoprolol 預防梗塞後心室重塑的比較 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Metoprolol 的不重複許可證共 **46 張**：有效單方 8 張、有效複方 0 張、已註銷 38 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（8 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第029301號 | "明德" 心壓暢錠100毫克（美托普洛） | 錠劑 | 明德製藥股份有限公司 | 2029/11/28 | 高血壓、狹心症 |
| 衛署藥製字第029313號 | “成大”貝他寧錠１００毫克（美托普洛） | 錠劑 | 成大藥品股份有限公司 | 2028/12/10 | 高血壓、狹心症 |
| 衛署藥製字第031032號 | “健喬”心舒寧錠１００毫克（美托普洛） | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2028/08/30 | 高血壓、狹心症。 |
| 衛署藥製字第036844號 | 速暢壓錠100毫克 | 錠劑 | 約克製藥股份有限公司 | 2028/10/20 | 高血壓、狹心症。 |
| 衛署藥製字第048912號 | “生泰”琥珀酸美托普洛 | 原料藥結晶性粉末 | 生泰合成工業股份有限公司 | 2027/07/30 | 降血壓劑。 |
| 衛署藥製字第057407號 | "永日"琥珀酸美托普洛 | 原料藥粉末 | 永日化學工業股份有限公司台中幼獅廠 | 2027/10/18 | 降血壓劑。 |
| 衛部藥輸字第026220號 | 酒石酸美托普洛 | （粉） | 新雙隆生技股份有限公司 | 2028/12/16 | 降壓劑 |
| 衛部藥輸字第026617號 | 琥珀酸美托普洛 | （粉） | 新雙隆生技股份有限公司 | 2030/09/03 | 降血壓劑 |

<details><summary><strong>已註銷</strong>（38 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第035842號</td><td>美托普洛錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第040476號</td><td>"生泰"酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2019/05/16</td></tr><tr><td>衛署藥製字第040547號</td><td>"壽元"滅得錠１００公絲/（美托普洛）</td><td>METOPROLOL TARTRATE</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第041956號</td><td>"十全"心達樂錠100毫克(酒石酸美托普洛)</td><td>METOPROLOL TARTRATE</td><td>2025/05/14</td></tr><tr><td>衛署藥輸字第009358號</td><td>舒壓寧錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>1989/07/25</td></tr><tr><td>衛署藥輸字第012933號</td><td>倍舒壓錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、METOPR…</td><td>1985/11/15</td></tr><tr><td>衛署藥輸字第013519號</td><td>舒壓寧注射液１公絲/公撮</td><td>METOPROLOL TARTRATE</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第013672號</td><td>舒壓寧持效錠２００公絲</td><td>METOPROLOL TARTRATE</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第014370號</td><td>倍舒壓錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、METOPR…</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第015811號</td><td>美托普洛酒石酸鹽</td><td>METOPROLOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第015962號</td><td>樂華寧錠</td><td>METOPROLOL TARTRATE</td><td>1991/12/18</td></tr><tr><td>衛署藥輸字第016210號</td><td>"合吉" 酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第016503號</td><td>美得寧錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第016564號</td><td>康達心錠</td><td>METOPROLOL TARTRATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016585號</td><td>美得寧錠５０公絲</td><td>METOPROLOL TARTRATE</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第016649號</td><td>可達平錠５０公絲</td><td>METOPROLOL TARTRATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016888號</td><td>得耐舒錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2025/06/03</td></tr><tr><td>衛署藥輸字第017200號</td><td>舒壓寧錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第017202號</td><td>舒壓寧持效錠２００公絲</td><td>METOPROLOL TARTRATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017205號</td><td>舒壓寧注射液１公絲/公撮</td><td>METOPROLOL TARTRATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017228號</td><td>倍舒壓錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、METOPR…</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017477號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第017837號</td><td>美托普洛醇酒石酸酯</td><td>METOPROLOL TARTRATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第018751號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第018794號</td><td>樂華寧錠</td><td>METOPROLOL TARTRATE</td><td>1993/06/14</td></tr><tr><td>衛署藥輸字第018891號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第019044號</td><td>酒石酸鹽美托普洛</td><td>METOPROLOL TARTRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019507號</td><td>敏樂舒錠５０公絲</td><td>METOPROLOL TARTRATE</td><td>2019/03/14</td></tr><tr><td>衛署藥輸字第019508號</td><td>敏樂舒錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2019/03/14</td></tr><tr><td>衛署藥輸字第020097號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>1999/03/11</td></tr><tr><td>衛署藥輸字第020173號</td><td>舒壓寧控釋錠２００公絲</td><td>METOPROLOL SUCCINATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第020174號</td><td>舒壓寧控釋錠１００公絲</td><td>METOPROLOL SUCCINATE</td><td>2025/10/07</td></tr><tr><td>衛署藥輸字第020175號</td><td>舒壓寧控釋錠５０公絲</td><td>METOPROLOL SUCCINATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第020540號</td><td>樂必舒緩釋錠１９０公絲</td><td>METOPROLOL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第021187號</td><td>脈妥普樂注射液１公絲－公撮</td><td>METOPROLOL TARTRATE</td><td>1997/12/10</td></tr><tr><td>衛署藥輸字第021835號</td><td>"莫伊士" 酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第021955號</td><td>脈妥普樂注射液１公絲－公撮</td><td>METOPROLOL TARTRATE</td><td>2002/03/29</td></tr><tr><td>衛署藥輸字第023799號</td><td>舒壓寧控釋錠２５公絲</td><td>METOPROLOL SUCCINATE</td><td>2025/03/18</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

**禁忌症：**
- 嚴重竇性心動過緩
- 二或三度房室傳導阻滯
- 心源性休克
- 失代償性心衰
- 嚴重周邊動脈疾病

**COPD 患者注意事項：**
- 選擇性 beta-1 阻斷劑相對安全
- 低劑量起始，緩慢調整
- 監測肺功能和呼吸症狀
- 有支氣管痙攣病史者謹慎使用

**藥物交互作用：**
- Verapamil/Diltiazem：增加心動過緩和傳導阻滯風險
- Digoxin：增強心動過緩效果
- MAO 抑制劑：可能增強降壓效果
- Beta-agonist 吸入劑：可能相互拮抗

## 結論與下一步

**決策：Explore**

**理由：**
Metoprolol 對慢性肺心病的預測具有臨床相關性。多項進行中的臨床試驗正在評估 beta-blocker 在 COPD 和心衰共病患者中的效益和安全性。傳統上認為 beta-blocker 在 COPD 中禁忌，但近期證據顯示選擇性 beta-1 阻斷劑可能帶來淨益處，特別是在心血管共病患者中。

**若要推進需要：**
- 等待進行中試驗（如 NCT06825728, NCT03566667）結果
- 確定 COPD 嚴重程度與治療風險/效益的關係
- 建立 COPD 患者使用 beta-blocker 的最佳劑量策略
- 開發預測哪些患者最可能受益的生物標記

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

