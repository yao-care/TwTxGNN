---
layout: default
title: Peppermint Oil
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint oil：從外用止痛與蟲咬傷到心血管疾病

## 一句話總結

Peppermint oil（薄荷油）在台灣主要作為外用製劑，用於切傷、蟲咬傷、頭暈等症狀，也用於液劑矯味。
TxGNN 模型的最高分預測是**痲瘋病 (Leprosy)**，但該預測完全沒有實證支持。證據最完整的是第 9 名的**心血管疾病 (Cardiovascular Disease)**，目前有 **1 個臨床試驗**和 **2 篇直接相關的隨機對照試驗文獻**（一篇為試驗成果，一篇為試驗計畫書）。

<!-- review:begin peppermint_oil-original-indication-combo-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「Peppermint oil（薄荷油，如意油）」。「如意油」（內衛成製字第003166號）是丁香油、桂皮油、麻油與薄荷油的複方，已於 1998-01-12 註銷，不是薄荷油本身的品名。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end peppermint_oil-original-indication-combo-summary-2026-10-16 -->

> 說明：本報告依預測排名第 1 的疾病（痲瘋病）填寫快速總覽，並另外說明證據最強的心血管疾病方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 切傷、刀傷、創傷、火傷、蟲咬傷、頭暈（"洸洋"藥用薄荷油） |
| 預測新適應症 | 痲瘋病 (Leprosy) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 37 張（有效單方 3／有效複方 8／已註銷 26） |
| 建議決策 | Hold |

**其他預測方向的比較（前 10 名）：**

| 排名 | 預測疾病 | 分數 | 證據等級 | 建議 |
|-----|---------|------|---------|------|
| 1 | 痲瘋病 | 99.80% | L5 | Hold |
| 2 | 肺囊蟲病 (Pneumocystosis) | 99.58% | L5 | Hold |
| 3 | 冠狀動脈疾病 | 99.35% | L5 | Hold |
| 4 | 心肌缺血 | 99.26% | L5 | Hold |
| 5 | 細粒棘球絛蟲感染 | 99.25% | L5 | Hold |
| 6 | 聲帶息肉 | 99.14% | L5 | Hold |
| 7 | 子宮息肉 | 99.14% | L5 | Hold |
| 8 | 中耳息肉 | 99.14% | L5 | Hold |
| 9 | 心血管疾病 | 99.13% | L3 | 列為研究問題 |
| 10 | 額竇息肉 | 99.12% | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。薄荷油的主要成分為薄荷醇 (menthol)，外用時有清涼、止痛的作用，這也是它在台灣許可證中用於肌肉痛、神經痛、蟲咬傷、頭暈的基礎。

**痲瘋病（排名第 1）：** 薄荷油雖有一些體外抗菌活性，但沒有任何證據顯示對麻風桿菌 (*Mycobacterium leprae*) 有效。這個預測目前僅來自模型，機轉上找不到合理連結。

**其他 L5 預測（肺囊蟲病、棘球絛蟲、各類息肉等）：** 同樣缺乏機轉依據與研究證據。精油類成分的一般抗微生物或殺原蟲活性，尚未在這些疾病中被證實。

**心血管疾病（證據最強的方向）：** 薄荷醇可能透過鈣離子通道調節與 TRPM8 活化使血管平滑肌放鬆，並可能提高心臟副交感神經活性，理論上有機會降低血壓、改善心血管代謝指標。相關的冠狀動脈疾病與心肌缺血預測，則僅有理論上的血管張力推測，並無直接證據。

---

## 臨床試驗證據

以下為預測方向中唯一有臨床試驗登記者（心血管疾病）。痲瘋病（排名第 1）目前無相關臨床試驗登記。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | 不適用 (NA) | 完成 | 40 | 薄荷油用於輕中度高血壓與高血壓前期受試者的心血管代謝指標；先前試驗顯示口服薄荷可改善健康受試者的收縮壓與血脂 |

---

## 文獻證據

以下為心血管疾病方向的文獻（痲瘋病方向目前無相關文獻）。與薄荷油直接相關者列出如下；另有數篇主題無關的文獻（如降血壓藥的奈米乳化製劑開發）不納入。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [42024666](https://pubmed.ncbi.nlm.nih.gov/42024666/) | 2026 | RCT | PloS one | 安慰劑對照試驗，探討每日兩次補充薄荷油對高血壓前期及第 1 期高血壓患者心血管代謝指標的影響 |
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | RCT（試驗計畫書） | PloS one | 上述試驗的設計計畫書，說明薄荷富含薄荷醇與類黃酮，可能具降血壓潛力 |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Cohort | Experimental physiology | 健康成人實驗中，胃部冷刺激與薄荷醇可提高心臟副交感神經活性 |
| [27277875](https://pubmed.ncbi.nlm.nih.gov/27277875/) | 2016 | Cohort | Bioanalysis | 志願者口服薄荷油膠囊後，以質譜監測呼出的薄荷酮，於 60–120 分鐘達高峰（屬藥物代謝動態，非療效研究） |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Peppermint Oil 的不重複許可證共 **37 張**：有效單方 3 張、有效複方 8 張、已註銷 26 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署成製字第011018號 | 〝派頓〞廣益油 | 外用液劑 | 臺灣派頓化學製藥股份有限公司 | 2029/06/21 | 外用：蟲咬傷、頭暈、頭痛、肌肉痛、牙神經痛及口腔黏膜發炎。內服：緩解腸胃道所引起之不適。吸入：緩解感冒之鼻塞症狀。 |
| 衛署藥製字第000664號 | "應元"薄荷水 | 外用液劑 | 應元化學製藥股份有限公司 | 2029/05/25 | 液劑之矯味、矯臭劑、驅風劑 |
| 衛部成製字第016950號 | "洸洋"藥用薄荷油 | 外用液劑 | 洸洋化學製藥股份有限公司 | 2028/01/10 | 切傷、刀傷、創傷、火傷、蟲咬傷、頭暈。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（8 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第001049號 | "美"解癢藥膏 | PHENOL (CARBOLIC ACID)、METHYL SALICYLATE、DL-METHYLEPHEDRINE… | 軟膏劑 | 急、慢性濕疹、皮膚搔癢症、汗疹、癢疹、蕁麻疹、肛門陰部部搔癢症、蚊蟲咬刺傷、痱子疹 |
| 衛署成製字第005716號 | "德山"青皮藥膠布 | METHYL SALICYLATE、L-MENTHOL、PEPPERMINT OIL (OLEUM MENTH PIP)… | 藥膠布 | 神經痛、腰痛、打撲痛、筋肉痛、挫傷、腫脹、扭傷、肩膀酸痛、關節痛 |
| 衛署成製字第005910號 | "德山"象印膏藥膠布 | METHYL SALICYLATE、L-MENTHOL、ZINC OXIDE、PEPPERMINT OIL (OLEUM… | 藥膠布 | 肩痛、腰痛、打撲傷、肌肉痛、神經痛、齒痛、頭痛、關節痛之消炎鎮痛 |
| 衛署成製字第009417號 | “艾力特”金象油 | PEPPERMINT OIL (OLEUM MENTH PIP)、CLOVE OIL、L-MENTHOL、EUCALYP… | 軟膏劑 | 切傷、刀傷、創傷、蚊蟲咬傷、頭暈 |
| 衛署藥製字第021676號 | 諾得胃腸藥散 | CLOVE OIL、MAGNESIUM CARBONATE HEAVY、SWERTIA POWDER、SCOPOLIA… | 散劑 | 緩解胃部不適或灼熱感、或經診斷為胃及十二指腸潰瘍、胃炎、食道炎所伴隨之胃酸過多 |
| 衛署藥製字第023893號 | 晶涼軟膏 | PEPPERMINT OIL (OLEUM MENTH PIP)、D-CAMPHOR、CLOVE OIL、L-MENTH… | 軟膏劑 | 切傷、刀傷、創傷、火傷、蟲咬傷、頭暈 |
| 衛署藥製字第028231號 | "德山"祛風濕藥膠布 | MENTHOL、CAMPHOR、SCOPOLIA EXTRACT、PEPPERMINT OIL (OLEUM MENTH… | 藥膠布 | 神經痛、關節痛、風濕、打撲傷、腰痛、齒痛。 |
| 衛署藥製字第045173號 | "德山" 舒痠痛藥布 | EUCALYPTUS OIL (OLEUM EUCALYPTI)、CAMPHOR、L-MENTHOL、PEPPERMIN… | 藥膠布 | 打撲、捻挫、肌肉痛、肩膀痠痛、腰痛、關節痛、肌肉疲勞。 |

<details><summary><strong>已註銷</strong>（26 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛成製字第001012號</td><td>消腫膏</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、EUCALYPTUS OIL (OLEUM EUCAL…</td><td>2000/08/08</td></tr><tr><td>內衛成製字第003097號</td><td>虎標永安堂八卦丹</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、GLYCYRRHIZA POWDER</td><td>1992/10/28</td></tr><tr><td>內衛成製字第003166號</td><td>如意油</td><td>CLOVE OIL、CASSIA OIL、SESAME OIL、PEPPERMINT OIL (OLEUM MENTH…</td><td>1998/01/12</td></tr><tr><td>內衛藥輸字第000507號</td><td>薄荷油</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)</td><td>2005/06/16</td></tr><tr><td>內衛藥輸字第002925號</td><td>尼可散</td><td>PYRIDOXINE HCL、THIAMINE NITRATE、RIBOFLAVIN (VIT B2)、CINNAMON…</td><td>1986/06/14</td></tr><tr><td>衛署成製字第003328號</td><td>爭虎油</td><td>CLOVE OIL、PEPPERMINT OIL (OLEUM MENTH PIP)、ROSEMARY OIL (OLE…</td><td>1998/02/27</td></tr><tr><td>衛署成製字第003836號</td><td>百珍膏布</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、METHYL SALICYLATE、GARDENIA…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第004211號</td><td>金龍藥膏布</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、L-MENTHOL、THYMOL、GARDENIA F…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第004435號</td><td>黃金膏</td><td>DIPHENHYDRAMINE、METHYL SALICYLATE、PEPPERMINT OIL (OLEUM MENT…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第004906號</td><td>李施德美漱口藥水</td><td>ETHANOL ( EQ TO ETHYL ALCOHOL) (EQ TO ALCOHOL)、METHYL SALICY…</td><td>1998/07/06</td></tr><tr><td>衛署成製字第005021號</td><td>金象油</td><td>JASMINE OIL、PEPPERMINT OIL (OLEUM MENTH PIP)、CLOVE OIL、L-MEN…</td><td>1993/11/10</td></tr><tr><td>衛署成製字第005666號</td><td>大維貼痠痛藥布</td><td>METHYL SALICYLATE、OLIVE OIL、EUCALYPTUS OIL (OLEUM EUCALYPTI)…</td><td>2013/10/03</td></tr><tr><td>衛署成製字第005830號</td><td>耐斯藥膠布</td><td>PHELLODENDRON BARK POWDER (EQ TO POWDERED PHELLODENDRON BARK…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第006647號</td><td>疼痛膏</td><td>DL-CAMPHOR、THYMOL、MENTHOL、SALICYL ETHYLENE GLYCOL、PEPPERMINT…</td><td>2015/01/15</td></tr><tr><td>衛署成製字第009123號</td><td>金獅牌香口丹</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、GLYCYRRHIZA (LIQUORICE)</td><td>1998/09/09</td></tr><tr><td>衛署成製字第009759號</td><td>薄荷李施德霖漱口水</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、METHYL SALICYLATE、SPEARMINT…</td><td>2007/05/09</td></tr><tr><td>衛署成製字第010407號</td><td>清涼油</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、CLOVE OIL、ANISE OIL、CINNAMO…</td><td>2022/05/05</td></tr><tr><td>衛署成製字第015032號</td><td>“杏輝”晶涼軟膏</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、L-MENTHOL、EUCALYPTUS OIL (O…</td><td>2023/07/07</td></tr><tr><td>衛署藥製字第009248號</td><td>咳香糖錠</td><td>THYME OIL、PEPPERMINT OIL (OLEUM MENTH PIP)、EUCALYPTUS OIL (O…</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第011334號</td><td>"三陽" 痠痛萬金膏</td><td>METHYL SALICYLATE、PHELLODENDRON EXTRACT、MENTHOL、CAMPHOR、CHLO…</td><td>2015/01/15</td></tr><tr><td>衛署藥製字第018223號</td><td>鎮痢懸浮液</td><td>KAOLIN (WHITE)(BOLUS ALBA)、BENZOIC ACID、PECTIN、PEPPERMINT OI…</td><td>1992/12/10</td></tr><tr><td>衛署藥製字第019683號</td><td>健樂仙壹錠</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、ALUMINUM HYDROXIDE DRIED GE…</td><td>2017/02/03</td></tr><tr><td>衛署藥製字第023884號</td><td>寶安藥膠布</td><td>EUCALYPTUS OIL (OLEUM EUCALYPTI)、SCOPOLIA EXTRACT、CAMPHOR、L-…</td><td>2015/01/15</td></tr><tr><td>衛署藥製字第027213號</td><td>健胃仙錠</td><td>PEPPERMINT OIL (OLEUM MENTH PIP)、SIMETHICONE (ACTIVE DIMETHI…</td><td>2023/06/30</td></tr><tr><td>衛署藥輸字第009198號</td><td>莎膚納軟膏</td><td>CAMPHOR、L-MENTHOL、PEPPERMINT OIL (OLEUM MENTH PIP)、DIPHENHYD…</td><td>2022/07/20</td></tr><tr><td>衛署藥輸字第010094號</td><td>維時利軟膠囊</td><td>INOSITOL (MESO-INOSITOL)、VITAMIN B1 (MONONITRATE)、ASCORBATE…</td><td>2020/04/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的痲瘋病預測沒有任何臨床試驗、文獻或機轉支持，僅屬模型預測（L5）。前 10 名中除心血管疾病外，其餘預測也都是 L5。
- 心血管疾病方向有一項已完成的小型試驗（n=40）及一篇 2026 年的安慰劑對照 RCT，證據等級為 L3，適合作為後續研究問題，但族群為高血壓前期與輕度高血壓，並非已確診的心血管疾病，試驗規模也小。

**若要推進需要：**
- 取得 NCT05561543 與 PMID 42024666 的完整結果（血壓、血脂等主要終點與效果量），確認是否有臨床意義。
- 補充薄荷油的作用機轉資料（目前缺乏 MOA）。
- 針對高血壓／心血管族群設計較大型、較長期的 RCT，並釐清口服劑型與劑量；台灣現有許可證多為外用，需評估給藥途徑的相容性。
- 補充安全性資料（警語、禁忌、藥物交互作用），尤其是長期口服使用時。
- 痲瘋病等 L5 預測建議先做體外或前臨床驗證，確認有無生物學依據後再考慮投入資源。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」取自如意油 | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列為薄荷油單方許可證（洸洋藥用薄荷油）的適應症；一句話總結仍把「如意油」當成別名，另以 -summary 紀錄更正；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結把「如意油」當成本藥別名 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

