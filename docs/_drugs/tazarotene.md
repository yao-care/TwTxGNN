---
layout: default
title: Tazarotene
description: "Tazarotene 的老藥新用潛力分析。模型預測等級 L5，包含 3 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 3
---

# Tazarotene

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>3</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tazarotene：從乾癬到脂漏性皮膚炎

## 一句話總結

<p class="key-answer" data-question="Tazarotene 可以用於治療什麼新適應症？">
Tazarotene 是一種維A酸類衍生物，原本用於治療乾癬和尋常性痤瘡。TxGNN 模型預測它可能對**脂漏性皮膚炎 (Seborrheic Dermatitis)** 有效，目前有 **1 個臨床試驗**支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乾癬及尋常性痤瘡 |
| 預測新適應症 | acne (disease)、seborrheic dermatitis、seborrheic keratosis |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Tazarotene 是一種合成的維A酸類藥物，透過與視黃酸受體（RAR）結合，調節表皮細胞的分化和增殖。根據藥理學資料，它對視黃酸受體-beta（RARB）具有最高親和力。

乾癬和脂漏性皮膚炎都屬於表皮角質化異常的皮膚疾病。乾癬的特徵是角質細胞過度增殖，而脂漏性皮膚炎則涉及皮脂腺功能異常和馬拉色菌感染。兩者在病理機轉上有部分重疊，特別是在表皮分化調節方面。

Tazarotene 調節角質形成細胞的分化作用，理論上可能對脂漏性皮膚炎的角質化異常有所幫助，但目前缺乏直接證據支持這一適應症。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | NA | 招募中 | 40 | 研究富含血小板血漿合併外用維A酸治療尋常性痤瘡（提及脂漏性皮膚炎作為痤瘡的臨床特徵） |

## 文獻證據

目前無直接針對 Tazarotene 治療脂漏性皮膚炎的文獻。

另有文獻支持 Tazarotene 用於脂漏性角化症：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/) | 2023 | 系統性回顧 | J Dermatolog Treat | Tazarotene 0.1% 乳膏每日兩次使用對脂漏性角化症有良好反應 |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | 臨床試驗 | Int J Dermatol | 比較冷凍治療與外用 Tazarotene 治療脂漏性角化症的效果 |

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥製字第049670號 | 癬痘克乳膏 | 乳膏劑 | 乾癬及尋常性痤瘡 |
| 衛署藥製字第049786號 | 派頓托樂蒂乳膏 | 乳膏劑 | 乾癬及尋常性痤瘡 |
| 衛署藥製字第047954號 | 療膚原外用凝膠 0.1% | 外用凝膠劑 | 乾癬及尋常性痤瘡 |
| 衛署藥製字第048511號 | 美妍凝膠 0.1% | 外用凝膠劑 | 乾癬及尋常性痤瘡 |
| 衛署藥製字第049239號 | 黃氏施膚雅乳膏 | 乳膏劑 | 乾癬及尋常性痤瘡 |

## 安全性考量

**藥物交互作用**：已知與多種藥物有交互作用（來源：DDInter），包括：
- Doxycycline、Minocycline（四環素類抗生素）
- Tretinoin、Adapalene（其他維A酸類藥物）
- Tacrolimus（免疫抑制劑）
- 多種外用類固醇如 Clobetasol、Fluticasone

使用時應避免與其他維A酸類藥物併用，以免增加皮膚刺激性。

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有模型預測支持 Tazarotene 用於脂漏性皮膚炎，缺乏直接的臨床試驗或文獻證據。雖然藥理機轉上有合理性，但證據等級過低（L5）。

**若要推進需要：**
- 進行針對脂漏性皮膚炎的 Pilot 臨床試驗
- 收集使用者的療效觀察性資料
- 與脂漏性角化症的文獻證據進行區分和比較


---

## 相關藥物報告

- [Clobetasone]({{ "/drugs/clobetasone/" | relative_url }}) - 證據等級 L5
- [Metoprolol]({{ "/drugs/metoprolol/" | relative_url }}) - 證據等級 L5
- [Salicylic Acid]({{ "/drugs/salicylic_acid/" | relative_url }}) - 證據等級 L5
- [Treprostinil]({{ "/drugs/treprostinil/" | relative_url }}) - 證據等級 L5
- [Caspofungin]({{ "/drugs/caspofungin/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Tazarotene老藥新用驗證報告. https://twtxgnn.yao.care/drugs/tazarotene/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_tazarotene,
  title = {Tazarotene老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/tazarotene/}
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
