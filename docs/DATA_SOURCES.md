# 藥物交互作用資料來源

本文件記錄 TwTxGNN 專案使用的藥物交互作用資料來源，便於定期更新。

## 資料總覽

| 類型 | 資料來源 | 記錄數 | 最後更新 | 授權 |
|------|----------|--------|----------|------|
| DDI (藥物-藥物) | DDInter 2.0 | 302,516 | 2026-02-08 | CC BY-NC-SA 4.0 |
| DFI (藥物-食物) | DDInter 2.0 | 857 | 2026-02-21 | CC BY-NC-SA 4.0 |
| DHI (藥物-草藥) | 精選資料集 | 35 | 2026-02-21 | - |

---

## DDI - 藥物-藥物交互作用

### 資料來源：DDInter 2.0

- **網站**：https://ddinter2.scbdd.com/
- **論文**：[DDInter 2.0 (Nucleic Acids Research, 2024)](https://academic.oup.com/nar/article/53/D1/D1356/7740584)
- **授權**：CC BY-NC-SA 4.0

### 下載方式

**方法一：網頁下載（分類檔案）**
```
https://ddinter2.scbdd.com/download/
```

按 ATC 藥物分類下載 CSV：
- Code A: 消化道及代謝藥物
- Code B: 血液及造血器官藥物
- Code D: 皮膚病藥物
- Code H: 全身性荷爾蒙製劑
- Code L: 抗腫瘤及免疫調節劑
- Code P: 抗寄生蟲藥物
- Code R: 呼吸系統藥物
- Code V: 其他藥物

**方法二：API 端點**
```bash
# 取得 DDI 資料（需 POST 請求）
curl -X POST "https://ddinter2.scbdd.com/server/interaction-source/" \
  -d "draw=1&start=0&length=1000"
```

### 資料格式

```csv
DDInterID_A,Drug_A,DDInterID_B,Drug_B,Level
DDInter1263,Naltrexone,DDInter1,Abacavir,Moderate
```

- `Level`: Major / Moderate / Minor

### 本地檔案位置

```
data/external/ddi/ddinter/
├── ddinter_code_A.csv
├── ddinter_code_B.csv
├── ddinter_code_D.csv
├── ddinter_code_H.csv
├── ddinter_code_L.csv
├── ddinter_code_P.csv
├── ddinter_code_R.csv
└── ddinter_code_V.csv
```

---

## DFI - 藥物-食物交互作用

### 資料來源：DDInter 2.0

- **網站**：https://ddinter2.scbdd.com/
- **統計**：857 筆 DFI，涵蓋 29 種食物
- **授權**：CC BY-NC-SA 4.0

### API 端點

```bash
# 取得完整 DFI 資料
curl -X POST "https://ddinter2.scbdd.com/server/food-interaction-source/" \
  -d "draw=1&start=0&length=1000"
```

### 回應格式

```json
{
  "draw": 1,
  "recordsTotal": 857,
  "recordsFiltered": 857,
  "data": [
    {
      "id": 1,
      "drugName": "Calcium lactate",
      "foodName": "spinach",
      "internalID_a_id": "DDInter278",
      "level": "2",
      "references": "...",
      "newInteraction": "Administration with food may increase...",
      "newManagement": "Calcium may be administered with food...",
      "magnesium": "Absorption"
    }
  ]
}
```

- `level`: 1=Major, 2=Moderate, 3=Minor
- `magnesium`: 實際是機制欄位（Absorption/Metabolism/Synergy/Antagonism）

### 本地檔案位置

```
data/external/dfi/
├── ddinter2_dfi_raw.json      # API 原始回應
└── ddinter2_dfi_processed.json # 處理後的資料
```

### 更新腳本

```bash
uv run python scripts/process_ddinter_dfi.py
```

---

## DHI - 藥物-草藥交互作用

### 資料來源：精選資料集

DDInter 2.0 不提供 DHI 資料，目前使用手動精選的資料集。

### 資料來源參考

| 來源 | 狀態 | 說明 |
|------|------|------|
| [Natural Medicines Database](https://naturalmedicines.therapeuticresearch.com/) | 需訂閱 | 最完整的 DHI 資料庫 |
| [PHYDGI](https://www.synapse-medicine.com/blog/blogpost/herb-drug-interactions-database-phydgi) | 非公開 | Synapse Medicine 商業資料庫 |
| [DrugBank](https://docs.drugbank.com/) | 需申請 | 學術授權可免費 |
| [TCMBank](https://tcmbank.cn/) | 待確認 | 中藥資料庫，可能含 DHI |
| [DDInter 2.0](https://ddinter2.scbdd.com/) | 規劃中 | 論文提到未來會支援 DHI |
| 臨床文獻 | 手動整理 | 目前使用此方式 |

> **注意**：目前公開可下載的 DHI 資料庫非常有限，因此使用手動精選。待 DDInter 2.0 支援 DHI 後可改為自動更新。

### 涵蓋草藥

| 草藥 | 英文名 | 主要機制 |
|------|--------|----------|
| 聖約翰草 | St. John's Wort | CYP3A4/P-gp 誘導 |
| 銀杏 | Ginkgo | 抗血小板作用 |
| 人參 | Ginseng | 多重途徑 |
| 大蒜 | Garlic | 抗血小板/CYP3A4 |
| 紫錐花 | Echinacea | 免疫調節 |
| 卡瓦 | Kava | CNS 抑制/肝毒性 |
| 纈草 | Valerian | CNS 抑制 |
| 甘草 | Licorice | 礦物皮質素作用 |
| 當歸 | Dong Quai | 增強抗凝血 |
| 綠茶 | Green Tea | 維生素 K/CYP |

### 本地檔案位置

```
data/external/dhi/
└── dhi_curated.json   # 精選資料集（35 筆）
```

---

## DDSI - 藥物-疾病交互作用（未整合）

DDInter 2.0 也提供 DDSI 資料，目前尚未整合。

### API 端點

```bash
curl -X POST "https://ddinter2.scbdd.com/server/disease-interaction-source/" \
  -d "draw=1&start=0&length=1000"
```

- **記錄數**：8,359 筆

---

## 更新流程

### 手動更新

1. **DDI 更新**
   ```bash
   # 從 DDInter 2.0 下載頁面下載最新 CSV
   # https://ddinter2.scbdd.com/download/
   # 放置到 data/external/ddi/ddinter/
   ```

2. **DFI 更新**
   ```bash
   uv run python scripts/process_ddinter_dfi.py
   ```

3. **DHI 更新**
   - 手動編輯 `data/external/dhi/dhi_curated.json`
   - 執行 `uv run python scripts/integrate_dfi_dhi.py`

### 自動更新（GitHub Actions）

參見 `.github/workflows/interaction-update-check.yml`

---

## 版本歷史

| 日期 | 更新內容 |
|------|----------|
| 2026-02-21 | 整合 DDInter 2.0 DFI 資料（857 筆） |
| 2026-02-21 | 建立 DHI 精選資料集（35 筆） |
| 2026-02-08 | 下載 DDInter DDI 資料（分類檔案） |

---

## 聯絡資訊

- **DDInter 2.0 團隊**：http://www.scbdd.com/
- **論文引用**：
  ```bibtex
  @article{ddinter2,
    title={DDInter 2.0: an enhanced drug interaction resource},
    journal={Nucleic Acids Research},
    year={2024},
    doi={10.1093/nar/gkae716}
  }
  ```
