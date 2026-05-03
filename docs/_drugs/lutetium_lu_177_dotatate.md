---
layout: default
title: Lutetium Lu 177 Dotatate
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Lutetium Lu 177 Dotatate
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

# Lutetium Lu 177 Dotatate：從 GEP-NETs 到垂體性侏儒症

## 一句話總結

Lutetium Lu 177 Dotatate（Lu-177 DOTATATE；品牌名 Lutathera®）是全球核准用於胃腸胰神經內分泌腫瘤（GEP-NETs）的靶向放射性藥物治療（PRRT），透過結合腫瘤細胞表面的體抑素受體（SSTR2）傳遞靶向放射線殺傷。
TxGNN 模型預測得分最高的新適應症為**垂體性侏儒症（Pituitary Dwarfism）**，預測分數達 99.99%，然而機轉分析顯示此預測與 SSTR2 靶向放射治療的作用原理不符。
目前第 1 名預測**無任何臨床試驗或文獻支持**，整體建議為 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | GEP-NETs（胃腸胰神經內分泌腫瘤） |
| 預測新適應症 | 垂體性侏儒症（Pituitary Dwarfism） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**Lu-177 DOTATATE 的作用機轉**

Lu-177 DOTATATE 是放射性同位素鑥-177（Lu-177）標記的體抑素類似物 DOTATATE 所組成的複合分子。DOTATATE 對腫瘤細胞表面的體抑素受體第 2 型（SSTR2）具有高度親和力，結合後將 Lu-177 的 β 射線直接傳遞至腫瘤細胞，造成 DNA 雙鏈斷裂以殺滅細胞。此藥物的療效前提是靶點腫瘤必須**高度表現 SSTR2**，如 GEP-NETs 即為典型的高 SSTR2 表現腫瘤。（本 Evidence Pack 未取得 DrugBank MOA 原文，以上根據已知藥理學補充。）

**第 1 名預測的機轉合理性：不支持**

垂體性侏儒症是生長激素（GH）分泌不足所導致的**非腫瘤性疾病**。Lu-177 DOTATATE 的治療機轉需要惡性腫瘤靶點（SSTR2 高表現細胞），在垂體性侏儒症中此前提根本不存在。更關鍵的是，體抑素類藥物本身即具有抑制 GH 分泌的效果，理論上會**加重**而非改善 GH 缺乏症狀。因此，此預測與藥物機轉方向相反，無任何臨床合理性。

**高分的可能原因，以及值得關注的備選預測**

TxGNN 對垂體性侏儒症的高分，可能源於知識圖譜中「垂體疾病」節點與「體抑素」路徑之間的非特異性關聯（體抑素類似物確實用於肢端肥大症等垂體過度分泌疾病），而非真正的治療機轉外推。在 10 個預測中，機轉較為合理的候選為：**第 6 名中耳神經內分泌腫瘤**（中耳類癌可高度表現 SSTR2，生物學特性與 GEP-NETs 高度類似）及**第 10 名橫紋肌樣腦膜瘤**（有個案報告直接記錄 Lu-177 DOTATATE PRRT 的治療經驗），這兩者均具有更紮實的機轉依據，建議優先評估。

---

## 臨床試驗證據

目前針對**垂體性侏儒症**無相關臨床試驗登記。

---

## 文獻證據

目前針對**垂體性侏儒症**無相關文獻。

---

## 台灣上市資訊

本藥物目前**未在台灣取得任何藥品許可證**，尚未上市。如需引進，須評估新藥上市申請（NDA）路徑，並配合輻射安全設施需求。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 靶向放射性藥物（Targeted Radionuclide Therapy / PRRT） |
| 骨髓抑制風險 | 中至高度（全身 β 射線效應；常見嗜中性白血球減少、血小板減少、貧血） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含白血球分類計數）、腎功能（血清肌酸酐 / eGFR）、肝功能、個人化劑量測定（dosimetry） |
| 處置防護 | 須依放射性藥物處置規範操作；需專屬輻射防護設施及合格人員；給藥後病患具有體外放射性，須遵守輻射安全隔離規定（限制探病、特殊廢棄物處理等） |

---

## 安全性考量

**藥物交互作用**（DDInter 資料庫查詢結果：共 73 筆；以下列出所有 Major 等級及代表性 Moderate 等級）

| 交互藥物 | 等級 | 類別說明 |
|---------|------|---------|
| Iothalamic acid | Major | 碘化造影劑（與放射性藥物合併使用增加腎毒性及清除競爭風險） |
| Diatrizoate | Major | 碘化造影劑 |
| Iopromide | Major | 碘化造影劑 |
| Iopamidol | Major | 碘化造影劑 |
| Iodipamide | Major | 碘化造影劑 |
| Iodixanol | Major | 碘化造影劑 |
| Iohexol | Major | 碘化造影劑 |
| Ioversol | Major | 碘化造影劑 |
| Ioxilan | Major | 碘化造影劑 |
| Deferasirox | Major | 鐵螯合劑（合併使用增加腎毒性風險） |
| Deferiprone | Major | 鐵螯合劑 |
| Samarium (153Sm) lexidronam | Major | 其他放射性藥物（合併使用加重骨髓抑制） |
| Strontium chloride Sr-89 | Moderate | 其他骨靶向放射性藥物 |
| Sulfasalazine | Moderate | 氨基水楊酸類（可能影響腎臟排泄） |
| Mesalazine | Moderate | 氨基水楊酸類 |
| Balsalazide | Moderate | 氨基水楊酸類 |
| Olsalazine | Moderate | 氨基水楊酸類 |
| Naltrexone | Moderate | 類鴉片拮抗劑 |
| Exenatide | Moderate | GLP-1 受體促效劑 |
| Roflumilast | Moderate | PDE4 抑制劑 |

> 剩餘 53 筆 Moderate 等級交互作用詳見完整 DDI 資料庫。警語與禁忌症資料尚待自 TFDA 仿單取得（Data Gap DG001），安全評估目前不完整。

---

## 結論與下一步

**決策：Hold**

**理由：**
第 1 名 TxGNN 預測（垂體性侏儒症）與 Lu-177 DOTATATE 的 SSTR2 靶向放射治療機轉存在根本性矛盾——此病非腫瘤性且體抑素效應方向相反——且完全缺乏臨床試驗與文獻支持（L5 等級）。此外，台灣目前無許可證、DDI 有多項 Major 等級交互作用、仿單警語與禁忌症資料尚未取得，安全評估無法完成，不具備進入下一階段評估的條件。

**若要推進需要：**
- **重新聚焦預測目標**：改以第 6 名（中耳神經內分泌腫瘤，L4）及第 10 名（橫紋肌樣腫瘤，L4，具 1 篇個案報告）作為首要評估對象
- **補充 TFDA 仿單（DG001）**：下載 TFDA 或 FDA 原廠仿單 PDF，解析警語與禁忌症，以完成 S1 安全性初評
- **補充 DrugBank MOA 資料（DG002）**：查詢 DrugBank API 以取得完整機轉描述
- **評估台灣引進路徑**：Lu-177 DOTATATE 若未來申請台灣上市，需確認 NDA 路徑、醫院輻射防護設施資格及健保給付策略
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

