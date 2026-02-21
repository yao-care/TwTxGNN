---
layout: default
title: Xylometazoline
description: "Xylometazoline 的老藥新用潛力分析。模型預測等級 L5，包含 2 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 2
---

# Xylometazoline

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>2</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Xylometazoline：從過敏性鼻炎到鼻腔疾病的廣泛應用

## 一句話總結

<p class="key-answer" data-question="Xylometazoline 可以用於治療什麼新適應症？">
Xylometazoline 原本用於緩解鼻塞、過敏性鼻炎等症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (nasal cavity disease)** 和**急性咽喉炎 (acute laryngopharyngitis)** 有效，
有 **2 個臨床試驗**和 **7 篇文獻**支持鼻腔疾病方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 感冒、鼻塞、過敏性鼻炎 |
| 預測新適應症 | 鼻腔疾病、急性咽喉炎 |
| TxGNN 預測分數 | 99.91% (鼻腔疾病)、99.89% (急性咽喉炎) |
| 證據等級 | L3 (有文獻支持) |
| 台灣上市 | 已上市 |
| 許可證數 | 24 張 (多張有效) |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Xylometazoline 是一種 alpha 腎上腺素受體激動劑，作用於鼻黏膜血管，
使血管收縮而達到減少鼻腔充血的效果。其作用標靶包括：

- **alpha-1D 腎上腺素受體** (ADRA1D)
- **alpha-2A 腎上腺素受體** (ADRA2A)
- **alpha-2B 腎上腺素受體** (ADRA2B)
- **alpha-2C 腎上腺素受體** (ADRA2C)

由於其本身就是作用於鼻腔的血管收縮劑，預測其對鼻腔疾病有效在機轉上完全合理。
這個預測更像是確認現有適應症的延伸，而非真正的「老藥新用」。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05072392](https://clinicaltrials.gov/study/NCT05072392) | N/A | UNKNOWN | 80 | 研究 Foley 導管輔助鼻腔插管對成人患者鼻出血的影響 |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | COMPLETED | 16 | 比較 cocaine、lidocaine/xylometazoline 和生理食鹽水在鼻腔鎮痛的效果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | 臨床研究 | Korean J Anesthesiol | Xylometazoline 噴霧可有效擴張鼻腔 |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | RCT | Arzneimittel-Forschung | 比較 tuaminoheptane/NAC 與 xylometazoline 在減少鼻阻力的效果 |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | 回顧 | Vestn Otorinolaringol | 0.1% xylometazoline 結合 5% dexpanthenol 可改善老年人鼻腔黏膜再生 |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | RCT | Eur Arch Otorhinolaryngol | 比較棉塞填塞與局部噴霧在鼻內視鏡前準備的效果 |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | 臨床研究 | Rhinology | Xylometazoline 可顯著降低鼻氣道阻力並消除不對稱性 |

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 許可證持有者 | 狀態 |
|---------|------|------|-------------|------|
| 衛部藥製字第061432號 | 大豐克敏通噴鼻液 0.1% | 鼻用噴液劑 | 大豐製藥 | 有效 |
| 衛部藥製字第059249號 | 強生欣鼻通噴鼻液 0.1% | 鼻用噴液劑 | 強生化學製藥 | 有效 |
| 衛署藥製字第043631號 | 斯斯鼻通噴鼻液 0.1% | 鼻用噴液劑 | 五洲製藥 | 有效 |
| 衛署藥輸字第024654號 | 歐治鼻噴鼻液 0.1% | 鼻用噴液劑 | 英商赫力昂 | 有效 |
| 衛署藥製字第047345號 | 大正百保能噴鼻液 0.1% | 鼻用噴液劑 | 台灣大正製藥 | 有效 |

## 安全性考量

- **藥物交互作用**：作用於 alpha-腎上腺素受體，與其他交感神經藥物併用需謹慎。
- **使用限制**：連續使用不宜超過 7 天，以避免藥物性鼻炎 (rhinitis medicamentosa)。
- **禁忌**：閉角型青光眼、嚴重高血壓患者應謹慎使用。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Xylometazoline 在鼻腔疾病中的應用與其原適應症高度相關，機轉明確且有充足的臨床證據支持。
預測的「鼻腔疾病」實際上是原適應症的泛化表述，臨床上已廣泛應用。

**若要推進需要：**
- 對於急性咽喉炎適應症，需要額外的臨床證據
- 針對特定鼻腔疾病亞型的療效評估
- 長期使用安全性監測


---

## 相關藥物報告

- [Pemetrexed]({{ "/drugs/pemetrexed/" | relative_url }}) - 證據等級 L5
- [Emedastine]({{ "/drugs/emedastine/" | relative_url }}) - 證據等級 L5
- [Magnesium Sulfate]({{ "/drugs/magnesium_sulfate/" | relative_url }}) - 證據等級 L5
- [Potassium Iodide]({{ "/drugs/potassium_iodide/" | relative_url }}) - 證據等級 L5
- [Methocarbamol]({{ "/drugs/methocarbamol/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Xylometazoline老藥新用驗證報告. https://twtxgnn.yao.care/drugs/xylometazoline/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_xylometazoline,
  title = {Xylometazoline老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/xylometazoline/}
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
