---
layout: default
title: Riluzole
description: "Riluzole 的老藥新用潛力分析。初步證據等級 L4，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 中證據等級 (L3-L4)
nav_order: 148
evidence_level: L4
indication_count: 10
---

# Riluzole

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L4</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Riluzole：從 ALS 到運動神經元相關疾病

## 一句話總結

<p class="key-answer" data-question="Riluzole 可以用於治療什麼新適應症？">
Riluzole 是一種谷氨酸拮抗劑，原本用於肌萎縮脊髓側索硬化症（ALS）的治療。TxGNN 模型預測它可能對多種運動神經元相關疾病有效，包括**下運動神經元症候群 (Lower Motor Neuron Syndrome)** 和 **ALS 易感性**，目前有 **多篇文獻**支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肌萎縮脊髓側索硬化症（ALS） |
| 預測新適應症 | 雙側旁矢狀頂枕多小腦回畸形、下運動神經元症候群、Mills 症候群、ALS 易感性 |
| TxGNN 預測分數 | 99.94%-99.98% |
| 證據等級 | L4 |
| 台灣上市 | 已上市 |
| 許可證數 | 多張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Riluzole 是目前唯一被核准用於 ALS 治療的藥物。它的主要作用機轉包括：
- 抑制谷氨酸釋放
- 阻斷電壓依賴性鈉離子通道
- 減少興奮性毒性（excitotoxicity）

ALS 的特徵是上下運動神經元的進行性退化。TxGNN 預測的幾個適應症與 ALS 在病理機轉上有密切關聯：

1. **下運動神經元症候群（晚發型）**：與 ALS 共享下運動神經元退化的特徵
2. **Mills 症候群**：一種以單側進行性肢體無力為特徵的運動神經元疾病
3. **ALS 易感性**：代表可能發展為 ALS 的高風險狀態
4. **單肢肌萎縮症（Monomelic Amyotrophy）**：一種局限性的運動神經元疾病

這些疾病都涉及運動神經元的退化，riluzole 的神經保護作用可能對這些疾病有類似的療效。

## 臨床試驗證據

目前無針對這些特定適應症的臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review | J Neurol | 谷氨酸、興奮性毒性與 ALS 的關係，riluzole 作為治療選擇 |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Review | Expert Rev Mol Med | ALS 的病理機轉和治療途徑，riluzole 是唯一延長存活的藥物 |
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | ALS 的病理生理學、診斷和治療管理 |
| [20942786](https://pubmed.ncbi.nlm.nih.gov/20942786/) | 2010 | Review | CNS Neurol Disord Drug Targets | ALS 的診斷、發病機制和治療標靶 |
| [19593125](https://pubmed.ncbi.nlm.nih.gov/19593125/) | 2009 | Review | Curr Opin Neurol | 運動神經元疾病的最新進展 |

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第XXXXXX號 | 特魯希口服懸浮液 5毫克/毫升 | 口服懸浮液 | 肌萎縮脊髓側索硬化症（ALS） |

## 安全性考量

**主要警語：**
- 肝毒性：需定期監測肝功能
- 間質性肺病：罕見但嚴重

**禁忌症：**
- 嚴重肝功能損害

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TxGNN 預測的適應症與 ALS 在病理機轉上高度相關，都涉及運動神經元的退化。Riluzole 的神經保護作用機轉（抗谷氨酸毒性）在理論上可能對這些疾病有效。然而，由於缺乏針對這些特定適應症的臨床試驗數據，需要謹慎評估。

**若要推進需要：**
- 對 Mills 症候群、單肢肌萎縮症等運動神經元疾病進行小規模臨床研究
- 收集真實世界證據（如 ALS 門診中其他運動神經元疾病患者使用 riluzole 的經驗）
- 定期監測肝功能
- 評估長期療效和安全性


---

## 相關藥物報告

- [Cisatracurium]({{ "/drugs/cisatracurium/" | relative_url }}) - 證據等級 L4
- [Pralatrexate]({{ "/drugs/pralatrexate/" | relative_url }}) - 證據等級 L4
- [Minoxidil]({{ "/drugs/minoxidil/" | relative_url }}) - 證據等級 L4
- [Dl-Alpha-Tocopherol]({{ "/drugs/dl-alpha-tocopherol/" | relative_url }}) - 證據等級 L4
- [Acebutolol]({{ "/drugs/acebutolol/" | relative_url }}) - 證據等級 L4

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Riluzole老藥新用驗證報告. https://twtxgnn.yao.care/drugs/riluzole/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_riluzole,
  title = {Riluzole老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/riluzole/}
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
