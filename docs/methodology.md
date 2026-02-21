---
layout: default
title: 方法論
nav_order: 6
description: "TwTxGNN 預測與驗證方法說明"
permalink: /methodology/
---

# 方法論
{: .fs-9 }

從 AI 預測到證據驗證的完整流程
{: .fs-6 .fw-300 }

---

## 整體流程

```
TxGNN 預測 → 資料收集 (Bundle) → 證據整理 (Evidence Pack) → 報告產出 (Notes)
```

---

## 第一步：TxGNN 預測

### 模型介紹

TxGNN 使用**知識圖譜**結合**圖神經網路**進行預測：

1. **知識圖譜建構**
   - 17,080 個節點（藥物、疾病、基因等）
   - 複雜的節點間關係

2. **圖神經網路訓練**
   - 學習節點間的隱含關聯
   - 預測新的藥物-疾病關係

3. **預測輸出**
   - 每個藥物-疾病配對的預測分數
   - 分數越高，預測越有信心

### 篩選標準

本專案採用的篩選條件：

| 參數 | 設定值 |
|------|--------|
| 最低預測分數 | 99% |
| 每藥物最多適應症 | 5 個 |
| 排除已知適應症 | 是 |

---

## 第二步：資料收集 (Bundle)

針對每個預測的藥物-疾病配對，自動收集以下資料：

### 臨床試驗

- **來源**：[ClinicalTrials.gov](https://clinicaltrials.gov/)
- **搜尋策略**：藥物名稱 + 疾病名稱
- **收集欄位**：試驗編號、階段、狀態、受試者人數

### 學術文獻

- **來源**：[PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- **搜尋策略**：藥物名稱 + 疾病名稱
- **收集欄位**：PMID、標題、年份、期刊、摘要

### 藥物資訊

- **來源**：[DrugBank](https://go.drugbank.com/)
- **收集欄位**：作用機轉、藥理作用、適應症

### 台灣上市資訊

- **來源**：衛福部食藥署 (TFDA)
- **收集欄位**：許可證號、品名、劑型、核准適應症

### 藥物交互作用 (DDI)

- **來源**：DDInter、Guide to PHARMACOLOGY
- **收集欄位**：交互作用藥物、嚴重程度、機轉

---

## 第三步：證據等級判定

根據收集到的證據，判定證據等級：

### 等級定義

| 等級 | 定義 | 判定標準 |
|:----:|------|----------|
| **L1** | 多個 Phase 3 RCT / 系統性回顧 | 有 ≥2 個 Phase 3 試驗或系統性回顧 |
| **L2** | 單一 RCT 或多個 Phase 2 試驗 | 有 1 個 RCT 或 ≥2 個 Phase 2 試驗 |
| **L3** | 觀察性研究 / 大型病例系列 | 有觀察性研究或病例系列報告 |
| **L4** | 前臨床 / 機轉研究 / 個案報告 | 僅有基礎研究或少量個案 |
| **L5** | 僅模型預測，無臨床證據 | 未找到相關臨床證據 |

### 判定流程

<style>
.flowchart {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-width: 500px;
  margin: 1.5rem 0;
}
.flow-step {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.flow-question {
  background: #f8f9fa;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border-left: 3px solid #1976D2;
  flex: 1;
}
.flow-arrow {
  color: #666;
  font-size: 1.2rem;
}
.flow-result {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-weight: 600;
  min-width: 50px;
  text-align: center;
}
.flow-l1 { background: #2E7D32; color: white; }
.flow-l2 { background: #66BB6A; color: white; }
.flow-l3 { background: #FDD835; color: #333; }
.flow-l4 { background: #FB8C00; color: white; }
.flow-l5 { background: #9E9E9E; color: white; }
.flow-no {
  margin-left: 2rem;
  padding-left: 1rem;
  border-left: 2px dashed #ddd;
}
</style>

<div class="flowchart">
  <div class="flow-step">
    <div class="flow-question">有 Phase 3 RCT 或系統性回顧？</div>
    <span class="flow-arrow">→</span>
    <div class="flow-result flow-l1">L1</div>
  </div>
  <div class="flow-no">
    <div class="flow-step">
      <div class="flow-question">有 Phase 2 RCT？</div>
      <span class="flow-arrow">→</span>
      <div class="flow-result flow-l2">L2</div>
    </div>
    <div class="flow-no">
      <div class="flow-step">
        <div class="flow-question">有觀察性研究？</div>
        <span class="flow-arrow">→</span>
        <div class="flow-result flow-l3">L3</div>
      </div>
      <div class="flow-no">
        <div class="flow-step">
          <div class="flow-question">有前臨床研究？</div>
          <span class="flow-arrow">→</span>
          <div class="flow-result flow-l4">L4</div>
        </div>
        <div class="flow-no">
          <div class="flow-step">
            <div class="flow-question">僅有模型預測</div>
            <span class="flow-arrow">→</span>
            <div class="flow-result flow-l5">L5</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

---

## 第四步：決策建議

根據證據等級和其他因素，給出決策建議：

| 決策 | 說明 | 建議行動 |
|------|------|----------|
| **Go** | 強力證據支持 | 可直接進入評估或試驗規劃 |
| **Proceed** | 充分證據支持 | 可進一步評估可行性 |
| **Consider** | 有一定證據 | 可考慮，但需注意風險 |
| **Explore** | 值得探索 | 需補充更多資料 |
| **Hold** | 證據不足 | 暫不建議推進 |

### 影響決策的因素

- 證據強度與一致性
- 台灣上市與許可證狀態
- 預測適應症與原適應症的相關性
- 安全性考量

---

## 品質控制

### 資料驗證

- 臨床試驗編號格式檢查
- PubMed ID 有效性驗證
- 許可證狀態確認

### 人工審核

- 高證據等級 (L1-L2) 報告經人工確認
- 決策建議的合理性檢查

---

## 限制與注意事項

1. **預測不等於因果**：TxGNN 預測基於關聯性，非因果關係
2. **證據收集有限**：僅搜尋公開資料庫，可能遺漏部分證據
3. **語言限制**：主要搜尋英文資料
4. **時效性**：資料會隨時間更新，報告反映產出時的狀態

{: .note }
> 本方法論會持續改進，歡迎提供回饋意見。
