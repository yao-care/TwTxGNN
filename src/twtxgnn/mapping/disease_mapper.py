"""疾病映射模組 - 中文適應症映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 中英文疾病/症狀對照表
DISEASE_DICT = {
    # 心血管系統
    "高血壓": "hypertension",
    "低血壓": "hypotension",
    "心臟病": "heart disease",
    "心肌梗塞": "myocardial infarction",
    "心絞痛": "angina",
    "心律不整": "arrhythmia",
    "心悸": "palpitation",
    "心衰竭": "heart failure",
    "動脈硬化": "atherosclerosis",
    "靜脈曲張": "varicose veins",
    "血栓": "thrombosis",
    "中風": "stroke",
    "腦中風": "stroke",

    # 呼吸系統
    "氣喘": "asthma",
    "哮喘": "asthma",
    "支氣管炎": "bronchitis",
    "肺炎": "pneumonia",
    "肺結核": "tuberculosis",
    "咳嗽": "cough",
    "感冒": "common cold",
    "流感": "influenza",
    "鼻炎": "rhinitis",
    "過敏性鼻炎": "allergic rhinitis",
    "鼻竇炎": "sinusitis",
    "呼吸困難": "dyspnea",
    "肺氣腫": "emphysema",

    # 消化系統
    "胃炎": "gastritis",
    "胃潰瘍": "gastric ulcer",
    "十二指腸潰瘍": "duodenal ulcer",
    "消化不良": "dyspepsia",
    "腹瀉": "diarrhea",
    "便秘": "constipation",
    "腸炎": "enteritis",
    "結腸炎": "colitis",
    "痢疾": "dysentery",
    "肝炎": "hepatitis",
    "肝硬化": "cirrhosis",
    "膽結石": "gallstone",
    "膽囊炎": "cholecystitis",
    "胰臟炎": "pancreatitis",
    "噁心": "nausea",
    "嘔吐": "vomiting",
    "胃酸過多": "hyperacidity",
    "胃食道逆流": "gastroesophageal reflux",

    # 神經系統
    "癲癇": "epilepsy",
    "頭痛": "headache",
    "偏頭痛": "migraine",
    "眩暈": "vertigo",
    "暈眩": "dizziness",
    "失眠": "insomnia",
    "神經痛": "neuralgia",
    "坐骨神經痛": "sciatica",
    "帕金森氏症": "parkinson disease",
    "阿茲海默症": "alzheimer disease",
    "失智症": "dementia",
    "多發性硬化症": "multiple sclerosis",
    "腦膜炎": "meningitis",

    # 精神疾病
    "憂鬱症": "depression",
    "焦慮症": "anxiety disorder",
    "躁鬱症": "bipolar disorder",
    "精神分裂症": "schizophrenia",
    "恐慌症": "panic disorder",
    "強迫症": "obsessive-compulsive disorder",

    # 內分泌系統
    "糖尿病": "diabetes",
    "甲狀腺機能亢進": "hyperthyroidism",
    "甲狀腺機能低下": "hypothyroidism",
    "肥胖": "obesity",
    "痛風": "gout",
    "高血脂": "hyperlipidemia",
    "高膽固醇": "hypercholesterolemia",

    # 肌肉骨骼系統
    "關節炎": "arthritis",
    "類風濕性關節炎": "rheumatoid arthritis",
    "骨質疏鬆": "osteoporosis",
    "骨折": "fracture",
    "肌肉痛": "myalgia",
    "腰痛": "back pain",
    "背痛": "back pain",
    "肩痛": "shoulder pain",
    "頸痛": "neck pain",
    "扭傷": "sprain",
    "挫傷": "contusion",
    "肌腱炎": "tendinitis",

    # 皮膚疾病
    "濕疹": "eczema",
    "蕁麻疹": "urticaria",
    "牛皮癬": "psoriasis",
    "皮膚炎": "dermatitis",
    "香港腳": "tinea pedis",
    "灰指甲": "onychomycosis",
    "青春痘": "acne",
    "痤瘡": "acne",
    "疥瘡": "scabies",
    "帶狀疱疹": "herpes zoster",
    "皮膚搔癢": "pruritus",
    "燒燙傷": "burn",

    # 泌尿系統
    "尿道炎": "urethritis",
    "膀胱炎": "cystitis",
    "腎炎": "nephritis",
    "腎結石": "kidney stone",
    "攝護腺肥大": "prostatic hyperplasia",
    "尿失禁": "urinary incontinence",
    "頻尿": "urinary frequency",

    # 眼科
    "結膜炎": "conjunctivitis",
    "青光眼": "glaucoma",
    "白內障": "cataract",
    "乾眼症": "dry eye",
    "近視": "myopia",
    "遠視": "hyperopia",

    # 耳鼻喉
    "中耳炎": "otitis media",
    "外耳炎": "otitis externa",
    "耳鳴": "tinnitus",
    "咽喉炎": "pharyngitis",
    "扁桃腺炎": "tonsillitis",

    # 感染症
    "細菌感染": "bacterial infection",
    "病毒感染": "viral infection",
    "黴菌感染": "fungal infection",
    "寄生蟲感染": "parasitic infection",
    "敗血症": "sepsis",
    "蜂窩性組織炎": "cellulitis",

    # 過敏
    "過敏": "allergy",
    "過敏反應": "allergic reaction",
    "花粉症": "hay fever",
    "食物過敏": "food allergy",
    "藥物過敏": "drug allergy",

    # 婦科
    "月經不順": "menstrual disorder",
    "經痛": "dysmenorrhea",
    "更年期症候群": "menopause syndrome",
    "子宮內膜異位": "endometriosis",
    "陰道炎": "vaginitis",
    "子宮肌瘤": "uterine fibroid",

    # 腫瘤/癌症
    "癌症": "cancer",
    "腫瘤": "tumor",
    "惡性腫瘤": "malignant tumor",
    "良性腫瘤": "benign tumor",
    "白血病": "leukemia",
    "淋巴癌": "lymphoma",

    # 一般症狀
    "發燒": "fever",
    "疼痛": "pain",
    "發炎": "inflammation",
    "水腫": "edema",
    "疲勞": "fatigue",
    "貧血": "anemia",
    "出血": "bleeding",
    "痙攣": "spasm",
    "抽筋": "cramp",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症文字提取個別適應症

    使用中文常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip()

    # 使用分隔符分割
    # 優先使用句號分割大段，再用頓號分割細項
    parts = re.split(r"[。；]", text)

    indications = []
    for part in parts:
        # 再用頓號和逗號細分
        sub_parts = re.split(r"[、，,]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見的非疾病描述前綴
            sub = re.sub(r"^(用於|適用於)", "", sub)
            sub = re.sub(r"^(治療|緩解|預防|改善)", "", sub)
            # 移除常見的後綴
            sub = re.sub(r"(等症狀?|之治療|所引起|引起之?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將中文適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for zh, en in DISEASE_DICT.items():
        if zh in indication:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """將台灣 FDA 藥品適應症映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        indication_str = row.get("適應症", "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "許可證字號": row["許可證字號"],
                        "中文品名": row["中文品名"],
                        "原始適應症": indication_str[:100],
                        "提取適應症": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "許可證字號": row["許可證字號"],
                    "中文品名": row["中文品名"],
                    "原始適應症": indication_str[:100],
                    "提取適應症": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["提取適應症"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
