---
layout: default
title: Pentosan Polysulfate
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 3
---

# Pentosan Polysulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Pentosan polysulfate：從間質性膀胱炎到血小板釋放障礙

## 一句話總結

Pentosan polysulfate（戊聚糖多硫酸酯）原本用於解除間質性膀胱炎引起的膀胱疼痛或不適，早期台灣許可證另有栓血症、栓塞症的適應症。
TxGNN 模型預測它可能對**血小板釋放障礙 (primary release disorder of platelets)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測，且藥理方向有疑慮。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 因間質性膀胱炎引起的膀胱疼痛或不適的解除 |
| 預測新適應症 | 血小板釋放障礙 (primary release disorder of platelets) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張（有效單方 3／有效複方 0／已註銷 3） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pentosan polysulfate 是一種類肝素的硫酸化多醣，具有微弱的抗凝血與抗血栓活性，在間質性膀胱炎的療效已有核准適應症，因此機轉上與止血系統有部分關聯。

不過，血小板釋放障礙的核心問題是血小板顆粒分泌功能受損，病人本身就有出血傾向。抗凝血藥物理論上會加重出血，而不是矯正問題。因此這項預測目前只建立在 TxGNN 模型的分數上，**作用方向（效果是否有益）存疑**。

同一模型也預測了另外兩個相近的疾病，同樣缺乏證據：
- **Glanzmann 血小板無力症**（第 2 名，分數 99.65%）：病因為血小板整合素 αIIb-β3 缺乏或功能異常，藥物沒有已知的機轉可恢復血小板凝集，抗凝血作用還可能增加出血風險。
- **假性血管性血友病 (pseudo-von Willebrand disease)**（第 3 名，分數 99.62%）：病因為血小板 GPIb-α 功能增強。硫酸化多醣或許會與醣蛋白或 von Willebrand 因子結合，但尚無支持的機轉，且同樣有出血風險。

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

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Pentosan Polysulfate 的不重複許可證共 **6 張**：有效單方 3 張、有效複方 0 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第057862號 | 優而順膠囊 | 膠囊劑 | 泰宗生物科技股份有限公司 | 2028/03/18 | 使用於因間質性膀胱炎引起的膀胱疼痛或不適的解除。 |
| 衛部藥製字第058601號 | 舒泌解膠囊100毫克 | 膠囊劑 | 國邑藥品科技股份有限公司 | 2030/07/02 | 因間質性膀胱炎引起的膀胱疼痛或不適的解除。 |
| 衛部藥輸字第027629號 | 硫酸戊聚糖鈉 | （粉） | 恒亞貿易股份有限公司 | 2029/04/11 | 因間質性膀胱炎引起的膀胱疼痛或不適的解除。 |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第002092號</td><td>愛斯庇５４針</td><td>SODIUM PENTOSAN POLYSULPHATE ( EQ TO PENTOSAN POLYSULFATE SO…</td><td>1986/08/19</td></tr><tr><td>內衛藥輸字第002202號</td><td>愛斯庇５４錠</td><td>SODIUM PENTOSAN POLYSULPHATE ( EQ TO PENTOSAN POLYSULFATE SO…</td><td>1986/08/19</td></tr><tr><td>衛署藥輸字第023657號</td><td>愛泌羅膠囊１００公絲</td><td>SODIUM PENTOSAN POLYSULPHATE ( EQ TO PENTOSAN POLYSULFATE SO…</td><td>2013/07/24</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單文字）：肝臟疾病、膽囊疾病、血小板低下、凝血疾病、血友病、肝素引起的血小板低下症。其中多項屬於出血或凝血異常，與預測的新適應症高度重疊，需特別留意。
- **藥物交互作用**：共查得 58 筆，以下為部分列出的中度交互作用，多數屬於抗凝血或抗血小板類藥物，合併使用可能增加出血風險：
  - 乙醯水楊酸 (Acetylsalicylic acid，阿斯匹靈)
  - 華法林 (Warfarin)
  - 氯吡格雷 (Clopidogrel)
  - 阿哌沙班 (Apixaban)
  - 艾多沙班 (Edoxaban)
  - 達肝素 (Dalteparin)
  - 西洛他唑 (Cilostazol)
  - 雙嘧達莫 (Dipyridamole)
  - 阿昔單抗 (Abciximab)
  - 阿替普酶 (Alteplase)
  - 比伐盧定 (Bivalirudin)
  - 其他如 Antithrombin III、Betrixaban、Cangrelor、Caplacizumab、Defibrotide、Anistreplase，以及 Ibritumomab tiuxetan、Tositumomab

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測適應症皆只有模型分數，沒有臨床試驗或文獻佐證（證據等級 L5）。
- 藥物的抗凝血特性與這些出血性血小板疾病的治療方向可能相反，安全疑慮明顯大於潛在效益。

**若要推進需要：**
- 補齊詳細的作用機轉資料（MOA），釐清藥物對血小板功能與 von Willebrand 因子的實際影響。
- 進行前臨床研究（如血小板功能試驗），確認作用方向是否有益。
- 在證實有益之前，先評估出血風險，並規劃安全性監測。
- 系統性檢索現有文獻與臨床試驗，確認是否真的完全沒有支持證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

