---
layout: default
title: Atezolizumab
description: "Atezolizumab 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Atezolizumab

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Atezolizumab：從肺癌免疫治療到泌尿道上皮癌

## 一句話總結
<p class="key-answer" data-question="Atezolizumab 可以用於治療什麼新適應症？">
Atezolizumab 是 PD-L1 免疫檢查點抑制劑，目前用於非小細胞肺癌、小細胞肺癌、三陰性乳癌、肝細胞癌等，TxGNN 預測其可能對攝護腺尿道泌尿上皮癌有效。
</p>


## 快速總覽
| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、三陰性乳癌、小細胞肺癌、肝細胞癌、肺泡狀軟組織肉瘤 |
| 預測新適應症 | 攝護腺尿道泌尿上皮癌 (prostatic urethra urothelial carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2 (Phase 1/2 臨床試驗進行中) |
| 台灣上市 | 已上市 |
| 許可證數 | 2 (注射劑、皮下注射劑) |
| 建議決策 | Proceed |

## 為什麼這個預測合理？
<p class="key-answer" data-question="這個藥物的作用機轉是什麼？">
Atezolizumab 透過阻斷 PD-L1 與 PD-1 的結合，解除腫瘤對 T 細胞的免疫抑制，增強抗腫瘤免疫反應。泌尿上皮癌是已知對免疫檢查點抑制劑有反應的腫瘤類型，FDA 已核准其他 PD-1/PD-L1 抑制劑用於膀胱癌等泌尿上皮癌。攝護腺尿道泌尿上皮癌與膀胱泌尿上皮癌同源，預期具有相似的免疫微環境，因此 atezolizumab 對此適應症的預測具有生物學合理性。
</p>

<div class="key-takeaway">
此預測基於藥物的作用機轉，與現有臨床證據方向一致。
</div>


## 臨床試驗證據
| 試驗編號 | 階段 | 狀態 | 收案人數 | 主要發現 |
|----------|------|------|----------|----------|
| NCT03170960 | Phase 1b | 進行中 | 914 | Cabozantinib 合併 atezolizumab 用於泌尿上皮癌等多種實體腫瘤 |
| NCT02844816 | Phase 2 | 已完成 | 172 | BCG 無效之非肌肉侵犯性膀胱癌使用 atezolizumab |

## 文獻證據
| PMID | 年份 | 標題 | 相關性 |
|------|------|------|--------|
| - | - | (無直接針對攝護腺尿道泌尿上皮癌的文獻) | - |

## 台灣上市資訊
| 許可證號 | 中文品名 | 劑型 | 許可證持有者 | 效期 |
|----------|----------|------|--------------|------|
| 衛部菌疫輸字第001050號 | 癌自禦 注射劑 | 注射液劑 | 羅氏大藥廠股份有限公司 | 2027/07/17 |
| 衛部菌疫輸字第001258號 | 癌自禦皮下注射劑 | 皮下注射劑 | 羅氏大藥廠股份有限公司 | 2029/05/29 |

## 安全性考量
- 主要交互作用：與免疫抑制劑 (adalimumab, etanercept, infliximab, baricitinib 等) 併用為 Major 級別交互作用
- 類固醇藥物 (hydrocortisone, dexamethasone, prednisone 等) 為 Moderate 級別交互作用，可能降低免疫治療效果
- 避免與活疫苗併用
- 需監測免疫相關不良反應：肺炎、肝炎、結腸炎、甲狀腺功能異常等

## 結論與下一步
**決策：Proceed**
**理由：** Atezolizumab 已在多種泌尿上皮癌中展現療效，攝護腺尿道泌尿上皮癌具有相似的腫瘤生物學特性。現有 Phase 1/2 臨床試驗正在評估其在泌尿上皮癌的療效，且藥物已在台灣上市，具備臨床使用基礎。
**若要推進需要：**
1. 關注 NCT03170960 試驗中泌尿上皮癌亞組的最終結果
2. 評估是否需要進行專門針對攝護腺尿道泌尿上皮癌的 Phase 2 試驗
3. 收集真實世界數據 (RWD) 以支持適應症擴展


---

## 相關藥物報告

- [Pentoxifylline]({{ "/drugs/pentoxifylline/" | relative_url }}) - 證據等級 L5
- [Ethynodiol Diacetate]({{ "/drugs/ethynodiol_diacetate/" | relative_url }}) - 證據等級 L5
- [Butenafine]({{ "/drugs/butenafine/" | relative_url }}) - 證據等級 L5
- [Tenofovir Alafenamide]({{ "/drugs/tenofovir_alafenamide/" | relative_url }}) - 證據等級 L5
- [Belimumab]({{ "/drugs/belimumab/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Atezolizumab老藥新用驗證報告. https://twtxgnn.yao.care/drugs/atezolizumab/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_atezolizumab,
  title = {Atezolizumab老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/atezolizumab/}
}
```

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-20 | 審核者：TwTxGNN Research Team</small>
</div>

{% include giscus.html %}
