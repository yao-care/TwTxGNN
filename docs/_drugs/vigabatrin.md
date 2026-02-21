---
layout: default
title: Vigabatrin
description: "Vigabatrin 的老藥新用潛力分析。模型預測等級 L5。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 0
---

# Vigabatrin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>0</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Vigabatrin：抗癲癇輔助療法

## 一句話總結

<p class="key-answer" data-question="Vigabatrin 可以用於治療什麼新適應症？">
Vigabatrin 是一種用於抗癲癇輔助療法的藥物。
TxGNN 模型**未預測**出任何新的適應症。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗癲癇之輔助療法 |
| 預測新適應症 |  |
| TxGNN 預測分數 | N/A |
| 證據等級 | N/A |
| 台灣上市 | 已上市 |
| 許可證數 | 6 張（2 張有效） |
| 建議決策 | 無老藥新用候選 |

## 為什麼沒有預測新適應症？

Vigabatrin 是一種選擇性 GABA 轉胺酶（GABA-T）不可逆抑制劑，透過抑制 4-aminobutyrate aminotransferase 增加腦內 GABA 濃度。其作用機轉高度專一，主要針對癲癇相關的神經傳導異常，因此在 TxGNN 知識圖譜分析中未發現與其他疾病的顯著關聯。

## 臨床試驗證據

無相關新適應症的臨床試驗。

## 文獻證據

無相關新適應症的文獻證據。

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 | 狀態 |
|---------|------|------|-----------|------|
| 衛部藥輸字第028723號 | 必抗癲口服溶液用粉劑500毫克 | 口服溶液用粉劑 | 抗癲癇之輔助療法 | 有效 |
| 衛署藥輸字第021847號 | 赦癲易膜衣錠500公絲 | 膜衣錠 | 抗癲癇之輔助療法 | 有效 |
| 衛署藥輸字第021691號 | 膜衣錠500公絲 | 膜衣錠 | 抗癲癇之輔助療法 | 已註銷 |
| 衛署藥輸字第020477號 | 赦癲易錠500公絲 | 外用錠劑 | 抗癲癇之輔助療法 | 已註銷 |

## 安全性考量

### 重大藥物交互作用（Major）

| 交互作用藥物 | 嚴重度 |
|-------------|--------|
| Hydrocortisone | Major |
| Triamcinolone | Major |
| Dexamethasone | Major |
| Betamethasone | Major |
| Budesonide | Major |
| Prednisone | Major |
| Prednisolone | Major |
| Methylprednisolone | Major |
| Deflazacort | Major |
| Deferoxamine | Major |
| Chloroquine | Major |
| Hydroxychloroquine | Major |
| Quinine | Major |
| Tamoxifen | Major |

### 中度藥物交互作用（Moderate）

與多種鎮靜劑、抗組織胺藥物及類鴉片藥物有中度交互作用，可能增加中樞神經抑制作用。常見包括：Morphine、Codeine、Cetirizine、Diphenhydramine、Ethanol 等。

### 作用標靶

- Vesicular inhibitory amino acid transporter (SLC32A1)
- 4-aminobutyrate aminotransferase (ABAT)

## 結論與下一步

**決策：無老藥新用候選**

**理由：**
Vigabatrin 的作用機轉高度專一於 GABA 能神經傳導，TxGNN 模型未發現具有足夠證據支持的新適應症候選。

**注意事項：**
- Vigabatrin 可能導致不可逆的視野缺損，需定期監測視力
- 與皮質類固醇併用需特別注意交互作用


---

## 相關藥物報告

- [Alirocumab]({{ "/drugs/alirocumab/" | relative_url }}) - 證據等級 L5
- [Polyethylene Glycol]({{ "/drugs/polyethylene_glycol/" | relative_url }}) - 證據等級 L5
- [Nepafenac]({{ "/drugs/nepafenac/" | relative_url }}) - 證據等級 L5
- [Timepidium]({{ "/drugs/timepidium/" | relative_url }}) - 證據等級 L5
- [Urea]({{ "/drugs/urea/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Vigabatrin老藥新用驗證報告. https://twtxgnn.yao.care/drugs/vigabatrin/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_vigabatrin,
  title = {Vigabatrin老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/vigabatrin/}
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
