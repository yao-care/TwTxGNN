---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
monitor_inn: "Cisatracurium"
predicted_indications: ["cauda equina syndrome", "preeclampsia", "obsolete neurogenic bladder (disease)", "migraine disorder", "thrombotic disease", "irritable bowel syndrome", "migraine with brainstem aura", "mild pre-eclampsia", "severe pre-eclampsia", "neurocirculatory asthenia"]
last_modified_at: 2026-10-16
description: "Cisatracurium：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：高選擇性及競爭性的非去極化神經肌肉阻斷劑，作為全身麻醉之輔助劑或加護病房使用，用以鬆弛骨骼肌，幫助氣管插管及與人工呼吸器的協調"
---

# Cisatracurium
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

## Cisatracurium：從全身麻醉輔助肌肉鬆弛到巨尾馬尾症候群（Cauda Equina Syndrome）
{: .text-alpha }

## 一句話總結

Cisatracurium 是一種高選擇性、競爭性的非去極化神經肌肉阻斷劑，原本用於全身麻醉輔助與加護病房的骨骼肌鬆弛。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，但目前**沒有任何臨床試驗與文獻**支持，僅為模型預測，且機轉上缺乏合理的治療連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高選擇性及競爭性的非去極化神經肌肉阻斷劑，作為全身麻醉之輔助劑或加護病房使用，用以鬆弛骨骼肌，幫助氣管插管及與人工呼吸器的協調 |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 5 張（有效單方 3／有效複方 0／已過期 1／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Cisatracurium 是非去極化神經肌肉阻斷劑，作用於骨骼肌神經肌肉接合處的菸鹼型乙醯膽鹼受體，用於麻醉時暫時性鬆弛肌肉。

馬尾症候群是脊髓末端神經根受壓所造成的急症，標準處置是儘早手術減壓。肌肉鬆弛劑並不能解除神經壓迫，也沒有修復神經的作用，因此機轉上找不到合理的治療連結。

所以，這個高分預測較可能反映知識圖譜中的統計關聯，而不是真實的療效訊號。在沒有任何臨床或文獻佐證下，不宜視為可行的再利用方向。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（備註：在其他排名較後的預測適應症中，如子癇前症與血栓性疾病，雖有少數文獻，但內容僅是 Cisatracurium 在剖腹產或肝臟移植麻醉中的附帶使用，並非療效證據。）

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cisatracurium 的不重複許可證共 **5 張**：有效單方 3 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第022770號 | 肌弛適　注射液２公絲/公撮 | 注射液劑 | 安沛國際有限公司 | 2030/01/19 | 本品為一高選擇性及競爭性的非去極化神經肌肉阻斷劑。可作為手術全身麻醉劑之輔助劑或加護病房使用，用以鬆弛骨骼肌，幫助氣管插管及與人工呼吸器的協調。 |
| 衛部藥製字第060359號 | 衛平適注射液2毫克/毫升 | 注射液劑 | 健亞生物科技股份有限公司 | 2029/09/25 | 本品為一高選擇性及競爭性的非去極化神經肌肉阻斷劑。可作為手術全身麻醉劑之輔助劑或加護病房使用，用以鬆弛骨骼肌，幫助氣管插管及與人工呼吸器的協調。 |
| 衛部藥輸字第029149號 | 肌適安鬆注射劑2毫克/毫升 | 注射液劑 | 美達特有限公司 | 2031/05/07 | 本品為一高選擇性及競爭性的非去極化神經肌肉阻斷劑。可作為手術全身麻醉之輔助劑或加護病房使用，用以鬆弛骨骼肌，幫助氣管插管及與人工呼吸器的協調。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛部藥輸字第026541號</td><td>"卡比"肌鬆弛注射液2毫克/毫升</td><td>CISATRACURIUM BESYLATE</td><td>2025/05/18</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第022759號</td><td>肌弛適　高單位注射液５公絲/公撮</td><td>CISATRACURIUM BESYLATE</td><td>2010/05/31</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：已查得 61 筆交互作用紀錄，以下為部分重點：
  - **嚴重 (Major)**：Kanamycin、Neomycin、Paromomycin、Polymyxin B、Streptomycin。這些胺基糖苷類或多黏菌素類抗生素可能增強神經肌肉阻斷作用。
  - **中度 (Moderate)**：Amphotericin B（含各劑型）、Doxycycline、Minocycline、Tetracycline、Vancomycin、Magnesium sulfate、Magnesium chloride、Mannitol、Metoclopramide。
  - **輕微 (Minor)**：Ranitidine。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有臨床試驗或文獻支持，證據等級僅為 L5。
- 神經肌肉阻斷劑無法解除馬尾神經壓迫，機轉上沒有合理的治療連結。

**若要推進需要：**
- 取得詳細的作用機轉資料，確認是否存在任何可檢驗的神經保護或其他相關機制。
- 進行系統性文獻回顧，確認是否有任何前臨床或臨床訊號。
- 在此之前，建議把資源放在證據更充分的候選藥物與適應症上。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

