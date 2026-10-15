---
layout: default
title: Oxytetracycline
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Oxytetracycline
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

# Oxytetracycline：從細菌感染症到慢性鼻竇炎

## 一句話總結

Oxytetracycline（羥四環素）是四環素類抗生素，原本用於治療革蘭氏陽性與陰性菌等所引起的感染症。
TxGNN 模型預測它可能對**慢性鼻竇炎 (Chronic Rhinosinusitis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅屬模型推論。
在其他預測適應症中，證據相對較多的是**外耳炎 (Otitis externa)**，有 17 篇相關文獻，但多為含 oxytetracycline 的複方外用製劑研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 支氣管炎、Q 熱、細菌性痢疾、扁桃腺炎、軟性下疳、耳炎、胃腸炎 |
| 預測新適應症 | 慢性鼻竇炎 (Chronic Rhinosinusitis) |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 132 張（有效單方 3／有效複方 0／已註銷 129） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。根據已知資訊，Oxytetracycline 是四環素類抗生素，屬抑菌性藥物，一般認為是透過抑制細菌 30S 核糖體次單位而阻斷蛋白質合成。四環素類另有次要的抗發炎作用，理論上可能與鼻竇疾病相關。

慢性鼻竇炎與原適應症中的上呼吸道感染（如支氣管炎、扁桃腺炎、耳炎）同屬呼吸道與耳鼻喉相關疾病，涉及的病原菌有部分重疊，這可能是模型給出高分的原因。

需要注意的是，目前沒有臨床試驗或文獻佐證此適應症，這個預測僅是模型推論。排名第 2 的慢性篩竇炎也屬同類，同樣沒有證據。

另一個值得留意的是第 10 名的**外耳炎**：已有文獻，其中包含數項 RCT，評估含 oxytetracycline 的外用複方（搭配 polymyxin B 與 hydrocortisone）。系統將其評為 L2、「Proceed with Guardrails」。但這些研究測試的是複方，無法單獨歸因於 oxytetracycline，且多數研究年代久遠。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為預測新適應症「慢性鼻竇炎」以外，證據相對最多的**外耳炎**之文獻（慢性鼻竇炎本身目前無相關文獻）。依 RCT 優先排序，列出主要項目：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8222746](https://pubmed.ncbi.nlm.nih.gov/8222746/) | 1993 | RCT | Curr Med Res Opin | 30 位外耳炎患者，比較 ciprofloxacin 耳滴劑與 oxytetracycline／polymyxin B／hydrocortisone 複方，療程 7 天 |
| [2415098](https://pubmed.ncbi.nlm.nih.gov/2415098/) | 1985 | RCT | Arch Oto-Rhino-Laryngol | 55 位急性外耳炎患者，framycitin/gramicidin 與 oxytetracycline/hydrocortisone/polymyxin B 兩組療效無顯著差異，治癒率 78% |
| [2156538](https://pubmed.ncbi.nlm.nih.gov/2156538/) | 1990 | 隨機單盲研究 | Eur Arch Otorhinolaryngol | 46 位患者，hydrocortisone butyrate 與 oxytetracycline 複方比較，整體治癒率 80% |
| [15949095](https://pubmed.ncbi.nlm.nih.gov/15949095/) | 2005 | 開放性隨機研究（系統分類為病例系列） | J Laryngol Otol | 51 位患者，betamethasone 單方耳滴劑與含 oxytetracycline 的複方比較，顯示不含抗生素的類固醇也有效 |
| [12019482](https://pubmed.ncbi.nlm.nih.gov/12019482/) | 2002 | Case series | Am J Otolaryngol | 探討耳用粉劑治療急性外耳炎 |
| [11583468](https://pubmed.ncbi.nlm.nih.gov/11583468/) | 2001 | 動物研究 | Eur Arch Otorhinolaryngol | 大鼠外耳炎模型，單用類固醇的效果可媲美含 oxytetracycline 的複方 |
| [6412426](https://pubmed.ncbi.nlm.nih.gov/6412426/) | 1983 | 體外研究 | Vet Microbiol | EDTA-Tris 與抗菌藥物組合對病原菌的作用（獸醫領域） |

另有數篇 1950–1960 年代的早期臨床報告，因年代久遠且缺乏摘要，此處不列出。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Oxytetracycline 的不重複許可證共 **132 張**：有效單方 3 張、有效複方 0 張、已註銷 129 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第006780號 | "利達" 鹽酸羥四環素膠囊２５０公絲 | 膠囊劑 | 利達製藥股份有限公司 | 2029/05/25 | 支氣管炎、Ｑ熱、細菌性痢疾、扁桃腺炎、軟性下疳、耳炎、胃腸炎 |
| 衛署藥製字第001165號 | 鹽酸羥四環素膠囊 | 膠囊劑 | 中美兄弟製藥股份有限公司 | 2029/05/25 | 革蘭氏陽性、陰性菌、立克次氏體、及巨型濾過性病毒所引起之感染症 |
| 衛署藥製字第055116號 | “羅得”塩酸羥四環素外用軟膏 | 軟膏劑 | 羅得化學製藥股份有限公司 | 2030/07/16 | 急救、預防及減緩皮膚刀傷、刮傷、燙傷之感染。 |

<details><summary><strong>已註銷</strong>（129 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000352號</td><td>羥四環素注射液１２５ＭＧ/ＭＬ（肌肉注射用）</td><td>OXYTETRACYCLINE</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第000630號</td><td>鹽酸羥四環素膠囊</td><td>OXYTETRACYCLINE HCL</td><td>1990/08/04</td></tr><tr><td>內衛藥製字第001512號</td><td>羥四環素膠衣錠２５０公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>1991/01/29</td></tr><tr><td>內衛藥製字第001536號</td><td>鹽酸羥四環素膠囊</td><td>OXYTETRACYCLINE (HCL)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第001859號</td><td>羥四環素針</td><td>OXYTETRACYCLINE、LIDOCAINE HCL</td><td>2016/09/19</td></tr><tr><td>內衛藥製字第002568號</td><td>羥四環素注射液</td><td>OXYTETRACYCLINE (HCL)、LIDOCAINE</td><td>2023/07/21</td></tr><tr><td>內衛藥製字第002683號</td><td>地靈黴素眼藥膏</td><td>OXYTETRACYCLINE (HCL)、POLYMYXIN B</td><td>2013/10/08</td></tr><tr><td>內衛藥製字第002755號</td><td>羥四環素注射液肌肉用</td><td>LIDOCAINE、OXYTETRACYCLINE (HCL)</td><td>1999/09/30</td></tr><tr><td>內衛藥製字第003344號</td><td>地靈黴素膠囊２５０公絲</td><td>OXYTETRACYCLINE</td><td>2013/10/08</td></tr><tr><td>內衛藥製字第006182號</td><td>羥四環素肌肉注射液</td><td>OXYTETRACYCLINE (HCL)、LIDOCAINE HCL</td><td>1998/06/08</td></tr><tr><td>內衛藥製字第006750號</td><td>鹽酸羥四環素針</td><td>OXYTETRACYCLINE (HCL)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007196號</td><td>鹽酸羥四環素注射液１００ＭＧ/２ＭＬ</td><td>LIDOCAINE、OXYTETRACYCLINE (HCL)</td><td>1988/12/31</td></tr><tr><td>內衛藥製字第007314號</td><td>良黴素膠囊２５０公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>1998/06/01</td></tr><tr><td>內衛藥製字第007696號</td><td>良黴素薄衣錠</td><td>OXYTETRACYCLINE</td><td>1998/06/01</td></tr><tr><td>內衛藥製字第008045號</td><td>羥四環素片２５０公絲</td><td>OXYTETRACYCLINE HCL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第008290號</td><td>羥四環素膠囊</td><td>OXYTETRACYCLINE (HCL)</td><td>1998/03/02</td></tr><tr><td>內衛藥製字第009119號</td><td>羥四環素肌肉注射液</td><td>OXYTETRACYCLINE</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第010243號</td><td>鹽酸羥四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>2010/02/08</td></tr><tr><td>內衛藥製字第010463號</td><td>滅菌鹽酸羥四環素注射劑１００ＭＧ/ＶＩＡＬ</td><td>OXYTETRACYCLINE HCL</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第010900號</td><td>鹽酸羥四環素肌肉注射液</td><td>OXYTETRACYCLINE HCL</td><td>2004/05/20</td></tr><tr><td>內衛藥製字第011130號</td><td>鹽酸羥四環素注射劑</td><td>OXYTETRACYCLINE HCL</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011135號</td><td>鹽酸氧四環素眼藥膏</td><td>POLYMYXIN B SULFATE、OXYTETRACYCLINE HCL</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011381號</td><td>羥四環素錠</td><td>OXYTETRACYCLINE DIHYDRATE</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011772號</td><td>鹽酸羥四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE HCL</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第012061號</td><td>"應元"羥四環素靜脈注射液</td><td>OXYTETRACYCLINE</td><td>2024/04/19</td></tr><tr><td>內衛藥製字第012062號</td><td>"應元"羥四環素２５０注射液</td><td>OXYTETRACYCLINE、LIDOCAINE</td><td>2024/04/19</td></tr><tr><td>內衛藥製字第012279號</td><td>鹽酸羥四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE HCL</td><td>1996/09/02</td></tr><tr><td>內衛藥製字第012315號</td><td>鹽酸羥四環素膠囊２５０ＭＧ</td><td>OXYTETRACYCLINE HCL</td><td>1991/04/26</td></tr><tr><td>內衛藥製字第012640號</td><td>鹽酸羥四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE HCL</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第013615號</td><td>"應元"羥四環素肌肉注射液</td><td>OXYTETRACYCLINE</td><td>2016/09/19</td></tr><tr><td>內衛藥製字第014233號</td><td>羥四環素肌肉注射液５０公絲</td><td>OXYTETRACYCLINE (HCL)、LIDOCAINE HCL</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第014592號</td><td>良黴素糖衣片２５０公絲</td><td>OXYTETRACYCLINE DIHYDRATE</td><td>1998/06/01</td></tr><tr><td>內衛藥輸字第000004號</td><td>羥四環素基體</td><td>OXYTETRACYCLINE</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第000038號</td><td>地靈黴素鈣鹽原料</td><td>OXYTETRACYCLINE CALCIUM</td><td>2005/06/15</td></tr><tr><td>內衛藥輸字第000900號</td><td>氧黴素眼用油膏</td><td>OXYTETRACYCLINE</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第002004號</td><td>廣力黴素肌肉注射液１００公絲</td><td>OXYTETRACYCLINE</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第002005號</td><td>廣力黴素肌肉注射２５０公絲</td><td>OXYTETRACYCLINE</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第002046號</td><td>氧得士黴素</td><td>OXYTETRACYCLINE</td><td>1985/09/23</td></tr><tr><td>內衛藥輸字第002047號</td><td>鈣氧得士黴素</td><td>OXYTETRACYCLINE CALCIUM</td><td>1985/09/13</td></tr><tr><td>內衛藥輸字第002120號</td><td>廣力黴素肌肉注射５００公絲</td><td>OXYTETRACYCLINE</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第002121號</td><td>廣力黴素靜脈注射２５０公絲</td><td>OXYTETRACYCLINE</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第002554號</td><td>極黴素靜脈注射劑</td><td>OXYTETRACYCLINE HCL</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第002574號</td><td>極黴素肌肉注射劑</td><td>OXYTETRACYCLINE HCL</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第002652號</td><td>極黴素靜脈注射劑</td><td>OXYTETRACYCLINE HCL</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第003204號</td><td>英卜黴素片</td><td>OXYTETRACYCLINE DIHYDRATE</td><td>1990/08/01</td></tr><tr><td>內衛藥輸字第004215號</td><td>鹽酸氧四環黴素</td><td>OXYTETRACYCLINE HCL</td><td>1985/08/02</td></tr><tr><td>內衛藥輸字第004676號</td><td>佑利黴素片</td><td>OXYTETRACYCLINE DIHYDRATE</td><td>1986/04/30</td></tr><tr><td>內衛藥輸字第004677號</td><td>佑利黴素膠囊</td><td>OXYTETRACYCLINE HCL</td><td>1986/04/30</td></tr><tr><td>內衛藥輸字第004886號</td><td>鹽酸氧四環黴素</td><td>OXYTETRACYCLINE HCL</td><td>1985/08/02</td></tr><tr><td>內衛藥輸字第004891號</td><td>氧四環黴素</td><td>OXYTETRACYCLINE</td><td>1985/08/02</td></tr><tr><td>內衛藥輸字第005162號</td><td>鹽酸氧四環素</td><td>OXYTETRACYCLINE HCL</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第006595號</td><td>靜脈注射用大德土黴素針</td><td>OXYTETRACYCLINE HCL</td><td>1987/04/02</td></tr><tr><td>衛署藥製字第000518號</td><td>〝大安〞鹽酸羥四環素膠囊</td><td>OXYTETRACYCLINE HCL</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第003398號</td><td>鹽酸羥四環素注射液</td><td>OXYTETRACYCLINE (HCL)、LIDOCAINE HCL</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第004186號</td><td>鹽酸羥四環素膠囊</td><td>OXYTETRACYCLINE (HCL)</td><td>2009/10/21</td></tr><tr><td>衛署藥製字第005589號</td><td>"聯邦"鹽酸羥四環素軟膏</td><td>OXYTETRACYCLINE (HCL)</td><td>2023/08/15</td></tr><tr><td>衛署藥製字第005627號</td><td>"聯邦"鹽酸羥四環素肌肉注射液50毫克/毫升</td><td>LIDOCAINE HCL、OXYTETRACYCLINE (HCL)</td><td>2023/08/15</td></tr><tr><td>衛署藥製字第009129號</td><td>地靈黴素膠囊５００公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第012065號</td><td>羥四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>2000/06/12</td></tr><tr><td>衛署藥製字第023577號</td><td>鹽酸羥四環素膠囊</td><td>OXYTETRACYCLINE (HCL)</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第024161號</td><td>鹽酸羥四環素注射液肌注用</td><td>OXYTETRACYCLINE (HCL)</td><td>1987/06/18</td></tr><tr><td>衛署藥製字第027180號</td><td>"南光"羥四環素靜脈注射液２５０毫升／３毫升</td><td>OXYTETRACYCLINE</td><td>2016/09/07</td></tr><tr><td>衛署藥製字第027353號</td><td>鹽酸羥四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第027427號</td><td>地黴素外用藥膏</td><td>POLYMYXIN B、POLYMYXIN B SULFATE、OXYTETRACYCLINE (HCL)、OXYTET…</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第027924號</td><td>鹽酸羥四環素注射液</td><td>OXYTETRACYCLINE (HCL)、LIDOCAINE</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第028170號</td><td>中性羥四環素結晶粉劑９７％</td><td>OXYTETRACYCLINE (HCL)</td><td>1995/07/11</td></tr><tr><td>衛署藥製字第028173號</td><td>鹽酸鹽羥四環素結晶粉劑９２％</td><td>OXYTETRACYCLINE (HCL)</td><td>1995/07/11</td></tr><tr><td>衛署藥製字第028930號</td><td>歐欣黴素眼藥膏</td><td>OXYTETRACYCLINE (HCL)</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第031270號</td><td>"羅得"塩酸羥四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>2023/07/17</td></tr><tr><td>衛署藥輸字第000265號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000268號</td><td>羥四環素基</td><td>OXYTETRACYCLINE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000404號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000746號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1994/06/08</td></tr><tr><td>衛署藥輸字第000770號</td><td>羥四環素</td><td>OXYTETRACYCLINE</td><td>1994/06/08</td></tr><tr><td>衛署藥輸字第000887號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第000979號</td><td>羥四環素鈣鹽</td><td>OXYTETRACYCLINE CALCIUM</td><td>1994/06/08</td></tr><tr><td>衛署藥輸字第001261號</td><td>鹽酸地靈黴素西藥級原料</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001269號</td><td>二性地靈黴素原料</td><td>OXYTETRACYCLINE AMPHOTERIC</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001270號</td><td>二性地靈黴素肌肉注射用原料</td><td>OXYTETRACYCLINE AMPHOTERIC</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001272號</td><td>鹽酸地靈黴素滅菌原料</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001273號</td><td>雙地靈黴素鈣鹽</td><td>OXYTETRACYCLINE CALCIUM</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001288號</td><td>鹽酸地靈黴素西藥級原料</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001310號</td><td>鹽酸地靈黴素</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001324號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001399號</td><td>鹽酸地靈黴素滅菌原料</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第001746號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002081號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第002146號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002433號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第002537號</td><td>羥四環素鹽酸鹽</td><td>OXYTETRACYCLINE HCL</td><td>2005/01/31</td></tr><tr><td>衛署藥輸字第002671號</td><td>普黴素針ＩＶ　５００公絲</td><td>OXYTETRACYCLINE HCL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第003003號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1993/02/09</td></tr><tr><td>衛署藥輸字第003491號</td><td>奧舒黴素膠囊</td><td>OXYTETRACYCLINE HCL</td><td>2000/09/26</td></tr><tr><td>衛署藥輸字第003980號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第004551號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第004728號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第004831號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第006616號</td><td>羥四黴素基</td><td>OXYTETRACYCLINE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第006618號</td><td>鹽酸羥四環黴素</td><td>OXYTETRACYCLINE HCL</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第006978號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006981號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第007753號</td><td>鹽酸地黴素</td><td>OXYTETRACYCLINE HCL</td><td>1990/09/25</td></tr><tr><td>衛署藥輸字第007828號</td><td>地黴素</td><td>OXYTETRACYCLINE</td><td>1990/09/25</td></tr><tr><td>衛署藥輸字第009813號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第010098號</td><td>二水羥四環素基</td><td>OXYTETRACYCLINE DIHYDRATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第010106號</td><td>能克黴素膠囊</td><td>OXYTETRACYCLINE HCL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第010145號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第010380號</td><td>益力克四環素膠囊２５０公絲</td><td>OXYTETRACYCLINE (HCL)</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第010996號</td><td>速維黴素膠囊</td><td>OXYTETRACYCLINE HCL</td><td>1985/11/04</td></tr><tr><td>衛署藥輸字第012512號</td><td>兩性地靈黴素原料</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第013755號</td><td>氧四環黴素粉劑</td><td>OXYTETRACYCLINE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第013773號</td><td>鹽酸氧四環黴素粉劑</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第013774號</td><td>鹽酸氧四環黴素粉劑</td><td>OXYTETRACYCLINE HCL</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第014032號</td><td>羥四環素粉劑</td><td>OXYTETRACYCLINE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第014059號</td><td>羥四環素鈣粉劑</td><td>OXYTETRACYCLINE CALCIUM</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第014295號</td><td>舒維歐可膠囊２５０公絲</td><td>OXYTETRACYCLINE HCL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第015113號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第015552號</td><td>鹽酸氧四環素</td><td>OXYTETRACYCLINE HCL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第016464號</td><td>鹽酸　四環素</td><td>OXYTETRACYCLINE (HCL)</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017659號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE (HCL)</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第019948號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第021706號</td><td>羥四杯素</td><td>OXYTETRACYCLINE</td><td>2010/05/31</td></tr><tr><td>衛署藥陸輸字第000019號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2020/04/07</td></tr><tr><td>衛署藥陸輸字第000120號</td><td>羥四環素</td><td>OXYTETRACYCLINE</td><td>2013/12/31</td></tr><tr><td>衛署藥陸輸字第000125號</td><td>羥四環素</td><td>OXYTETRACYCLINE</td><td>2022/07/13</td></tr><tr><td>衛署藥陸輸字第000183號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HCL</td><td>2019/03/15</td></tr><tr><td>衛署藥陸輸字第000195號</td><td>土霉素</td><td>OXYTETRACYCLINE</td><td>2019/03/15</td></tr><tr><td>衛署藥陸輸字第000415號</td><td>鹽酸羥四環素</td><td>oxytetracycline hydrochloride</td><td>2022/07/13</td></tr><tr><td>衛部藥陸輸字第000809號</td><td>鹽酸羥四環素</td><td>OXYTETRACYCLINE HYDROCHLORIDE</td><td>2024/05/06</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單內容）：腎臟疾病、肝臟疾病、膽囊疾病、腎衰竭、尿毒症、腎絲球腎炎、G6PD 缺乏症、困難梭狀芽孢桿菌結腸炎、心房顫動、房室傳導阻滯、呼吸衰竭等。
- **藥物交互作用**：共查得 144 筆。重點如下：
  - **Major（嚴重）**：Vitamin A
  - **Moderate（中度）**：含鈣、鎂、鋅、鉀的製劑（如 Calcium acetate、Magnesium oxide、Zinc sulfate、Potassium citrate 等）、多種胰島素製劑、Amoxicillin、Balsalazide
  - **Minor（輕微）**：Mannitol

詳細警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 慢性鼻竇炎的預測分數雖高（99.61%），但沒有任何臨床試驗或文獻佐證，屬 L5 等級，僅為模型預測。
- 外耳炎雖有 RCT 文獻，但皆為含 oxytetracycline 的複方外用製劑，且研究年代較舊、樣本數小。此外，目前台灣有效許可證僅 1 張口服膠囊，與外用劑型不符。

**若要推進需要：**
- 補充詳細的作用機轉（MOA）資料
- 針對慢性鼻竇炎進行文獻與臨床試驗的系統性檢索，確認是否存在直接證據
- 評估給藥途徑的可行性（目前台灣有效許可證為口服膠囊）
- 若考慮外耳炎方向，需釐清 oxytetracycline 單方相對於複方的貢獻，並確認外用製劑在台灣的可取得性
- 針對腎、肝功能不全等族群，以及與含多價陽離子製劑、Vitamin A 併用的風險，擬定安全性監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄；頁首證據等級依本頁「快速總覽」的證據等級列重算，模型預測、總覽表與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L2） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

