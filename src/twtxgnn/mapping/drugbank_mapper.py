"""DrugBank 映射模組

提供台灣 FDA 藥品成分到 DrugBank 的映射功能。
支援多來源映射：DrugBank 直接映射、同義詞映射、中草藥映射。
"""

import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from .normalizer import extract_ingredients, get_all_synonyms

logger = logging.getLogger(__name__)


def load_drugbank_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 DrugBank 詞彙表

    Args:
        filepath: CSV 檔案路徑，預設為 data/external/drugbank_vocab.csv

    Returns:
        DrugBank 詞彙表 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drugbank_vocab.csv"

    return pd.read_csv(filepath)


def build_name_index(drugbank_df: pd.DataFrame) -> Dict[str, str]:
    """建立名稱索引（名稱 -> DrugBank ID）

    Args:
        drugbank_df: DrugBank 詞彙表

    Returns:
        名稱到 ID 的對照字典
    """
    index = {}

    for _, row in drugbank_df.iterrows():
        name_upper = row["drug_name_upper"]
        drugbank_id = row["drugbank_id"]

        # 完整名稱
        index[name_upper] = drugbank_id

        # 移除常見鹽類後綴，建立別名
        # 例如 "METFORMIN HCL" -> "METFORMIN"
        salt_suffixes = [
            " HCL", " HYDROCHLORIDE", " SODIUM", " POTASSIUM",
            " SULFATE", " SULPHATE", " MALEATE", " ACETATE",
            " CITRATE", " PHOSPHATE", " BROMIDE", " CHLORIDE",
            " TARTRATE", " FUMARATE", " SUCCINATE", " MESYLATE",
            " BESYLATE", " CALCIUM", " MAGNESIUM", " NITRATE",
            " LACTATE", " GLUCONATE", " DISODIUM", " MONOHYDRATE",
            " DIHYDRATE", " TRIHYDRATE", " ANHYDROUS",
            " DIPROPIONATE", " PROPIONATE", " ACETONIDE",
            " VALERATE", " BUTYRATE", " HEXAHYDRATE",
        ]

        for suffix in salt_suffixes:
            if name_upper.endswith(suffix):
                base_name = name_upper[:-len(suffix)].strip()
                if base_name and base_name not in index:
                    index[base_name] = drugbank_id

    # 添加常見同義詞對照
    # 格式：{FDA 成分名稱: DrugBank 名稱}
    synonym_map = {
        # ===== 維生素（通用名 -> DrugBank 化學名）=====
        "NIACINAMIDE": "NICOTINAMIDE",
        "NICOTINIC ACID": "NIACIN",
        # 維生素 B1 (DrugBank: THIAMINE)
        "VITAMIN B1": "THIAMINE",
        "THIAMINE HCL": "THIAMINE",
        "THIAMINE MONONITRATE": "THIAMINE",
        "THIAMINE DISULFIDE": "THIAMINE",
        # 維生素 B2 (DrugBank: RIBOFLAVIN)
        "VITAMIN B2": "RIBOFLAVIN",
        # 維生素 B6 (DrugBank: PYRIDOXINE)
        "VITAMIN B6": "PYRIDOXINE",
        "PYRIDOXINE HCL": "PYRIDOXINE",
        # 維生素 B12 (DrugBank: CYANOCOBALAMIN)
        "VITAMIN B12": "CYANOCOBALAMIN",
        # 維生素 C (DrugBank: ASCORBIC ACID)
        "VITAMIN C": "ASCORBIC ACID",
        # 維生素 E (DrugBank: TOCOPHEROL, ALPHA-TOCOPHEROL ACETATE)
        "VITAMIN E": "TOCOPHEROL",
        "TOCOPHEROL ACETATE": "ALPHA-TOCOPHEROL ACETATE",
        "TOCOPHEROL ACETATE ALPHA DL-": "ALPHA-TOCOPHEROL ACETATE",
        "DL-ALPHA-TOCOPHEROL ACETATE": "ALPHA-TOCOPHEROL ACETATE",
        "ALPHA-TOCOPHEROL": "TOCOPHEROL",
        # 維生素 A (DrugBank: RETINOL)
        "VITAMIN A": "RETINOL",
        "RETINOL PALMITATE": "RETINOL",
        "VITAMIN A PALMITATE": "RETINOL",
        "RETINOIC ACID": "TRETINOIN",
        # 維生素 D
        "VITAMIN D3": "CHOLECALCIFEROL",
        "VITAMIN D2": "ERGOCALCIFEROL",
        # 維生素 K
        "VITAMIN K1": "PHYTONADIONE",
        # 泛酸/維生素 B5 相關
        "PANTOTHENATE CALCIUM": "PANTOTHENIC ACID",
        "CALCIUM PANTOTHENATE": "PANTOTHENIC ACID",
        "CALCIUM PANTOTHENATE TYPE S": "PANTOTHENIC ACID",
        "SODIUM PANTOTHENATE": "PANTOTHENIC ACID",
        "PANTHENOL": "DEXPANTHENOL",
        "PANTHENOL D-": "DEXPANTHENOL",
        "D-PANTHENOL": "DEXPANTHENOL",
        # ===== 常見藥物別名 =====
        # 阿司匹林（DrugBank 用化學名 ACETYLSALICYLIC ACID）
        "ASPIRIN": "ACETYLSALICYLIC ACID",
        # 乙醯胺酚
        "PARACETAMOL": "ACETAMINOPHEN",
        # 腎上腺素
        "ADRENALINE": "EPINEPHRINE",
        "L-ADRENALINE": "EPINEPHRINE",
        "NORADRENALINE": "NOREPINEPHRINE",
        # 局部麻醉劑
        "LIGNOCAINE": "LIDOCAINE",
        # 利尿劑
        "FRUSEMIDE": "FUROSEMIDE",
        # 支氣管擴張劑
        "SALBUTAMOL": "ALBUTEROL",
        # 祛痰劑（Guaifenesin 同義詞）
        "GUAIACOL GLYCERYL ETHER": "GUAIFENESIN",
        "GUAIACOL GLYCOLATE": "GUAIFENESIN",
        "GLYCERYL GUAIACOLATE": "GUAIFENESIN",
        # 消脹劑
        "SIMETHICONE": "DIMETHICONE",
        "SIMETICONE": "DIMETHICONE",
        "SIMETHICONE EMULSION 30%": "DIMETHICONE",
        # 抗組織胺
        "DL-CHLORPHENIRAMINE MALEATE": "CHLORPHENIRAMINE",
        "CHLORPHENIRAMINE MALEATE": "CHLORPHENIRAMINE",
        # 乙醯膽鹼酯酶抑制劑
        "NEOSTIGMINE METHYLSULFATE": "NEOSTIGMINE",
        # 抗凝血劑
        "BROMISOVALUM": "BROMISOVAL",
        # 肝臟保護劑 (SILYMARIN/SILYBIN 不在 DrugBank 中，無法映射)
        # 制酸劑
        "ALUMINUM HYDROXIDE DRIED GEL": "ALUMINUM HYDROXIDE",
        "ALUMINIUM HYDROXIDE": "ALUMINUM HYDROXIDE",
        # 胃動力藥
        "OXETHAZAINE": "OXETACAINE",
        # ===== 葡萄糖/右旋糖 =====
        # DrugBank 中是 D-GLUCOSE
        "DEXTROSE": "D-GLUCOSE",
        "DEXTROSE MONOHYDRATE": "D-GLUCOSE",
        "DEXTROSE ANHYDROUS": "D-GLUCOSE",
        "DEXTROSE HYDROUS": "D-GLUCOSE",
        "GLUCOSE": "D-GLUCOSE",
        "GLUCOSE MONOHYDRATE": "D-GLUCOSE",
        "GLUCOSE ANHYDROUS": "D-GLUCOSE",
        # ===== L-/D-/DL- 前綴處理 =====
        "L-MENTHOL": "LEVOMENTHOL",
        "MENTHOL": "LEVOMENTHOL",
        "DL-MENTHOL": "RACEMENTHOL",
        # 胺基酸
        "METHIONINE DL-": "METHIONINE",
        "DL-METHIONINE": "METHIONINE",
        "L-METHIONINE": "METHIONINE",
        "LYSINE L- HCL": "LYSINE",
        "L-LYSINE HCL": "LYSINE",
        "L-LYSINE": "LYSINE",
        "ASPARTATE POTASSIUM L-": "ASPARTIC ACID",
        "L-ASPARTATE": "ASPARTIC ACID",
        # ===== 水合物/無水形式 =====
        "CAFFEINE ANHYDROUS": "CAFFEINE",
        "ATORVASTATIN CALCIUM TRIHYDRATE": "ATORVASTATIN",
        "MOSAPRIDE CITRATE DIHYDRATE": "MOSAPRIDE",
        "FORMOTEROL FUMARATE DIHYDRATE": "FORMOTEROL",
        "IRINOTECAN HYDROCHLORIDE TRIHYDRATE": "IRINOTECAN",
        "NILOTINIB HYDROCHLORIDE MONOHYDRATE": "NILOTINIB",
        "SITAGLIPTIN PHOSPHATE MONOHYDRATE": "SITAGLIPTIN",
        "ATROPINE SULFATE MONOHYDRATE": "ATROPINE",
        "ZIPRASIDONE HYDROCHLORIDE MONOHYDRATE": "ZIPRASIDONE",
        "LIDOCAINE HYDROCHLORIDE MONOHYDRATE": "LIDOCAINE",
        "LIDOCAINE HCL MONOHYDRATE": "LIDOCAINE",
        "NALOXONE HCL DIHYDRATE": "NALOXONE",
        "CIPROFLOXACIN HYDROCHLORIDE MONOHYDRATE": "CIPROFLOXACIN",
        "PANTOPRAZOLE SODIUM SESQUIHYDRATE": "PANTOPRAZOLE",
        # ===== 微粒化形式 =====
        "FLUTICASONE PROPIONATE MICRONIZED": "FLUTICASONE",
        "BUDESONIDE MICRONIZED": "BUDESONIDE",
        "FENOFIBRATE MICRONIZED": "FENOFIBRATE",
        "ACETAMINOPHEN MICRONIZED": "ACETAMINOPHEN",
        "PROGESTERONE MICRONIZED": "PROGESTERONE",
        "OLANZAPINE MICRONIZED": "OLANZAPINE",
        # ===== 其他常見變體 =====
        "ACETIC ACID GLACIAL": "ACETIC ACID",
        "ESTRADIOL ETHINYL": "ETHINYL ESTRADIOL",
        "ETHINYLESTRADIOL": "ETHINYL ESTRADIOL",
        "VALPROATE SODIUM": "VALPROIC ACID",
        "SODIUM VALPROATE": "VALPROIC ACID",
        "OLMESARTAN MEDOXOMIL": "OLMESARTAN",
        # CARBETAPENTANE 不在 DrugBank 中
        # 支氣管擴張劑（DrugBank: ORCIPRENALINE = METAPROTERENOL）
        "METAPROTERENOL SULFATE": "ORCIPRENALINE",
        "METAPROTERENOL": "ORCIPRENALINE",
        # ISOCONAZOLE 不在 DrugBank 中
        # LYSOZYME 不在 DrugBank 中
        "IODOCHLORHYDROXYQUIN": "CLIOQUINOL",
        # CHLOROPHYLLIN 不在 DrugBank 中
        "UNDECYLENATE ZINC": "UNDECYLENIC ACID",
        "DEXAMETHASONE SODIUM PHOSPHATE": "DEXAMETHASONE",
        "BETAMETHASONE SODIUM PHOSPHATE": "BETAMETHASONE",
        "GLYCYRRHIZINIC ACID": "GLYCYRRHIZIC ACID",
        "GLYCYRRHIZINATE DIPOTASSIUM": "GLYCYRRHIZIC ACID",
        # ===== RxNorm API 橋接發現的同義詞 =====
        # 制酸劑/胃藥
        "ALUMINUM HYDROXIDE GEL": "ALUMINUM HYDROXIDE",
        "ALUMINUM MAGNESIUM SILICATE": "ALMASILATE",
        "BASIC ALUMINUM SUCROSE SULFATE": "SUCRALFATE",
        # 抗生素
        "AMOXYCILLIN": "AMOXICILLIN",
        "CEPHRADINE": "CEFRADINE",
        "RIFAMPIN": "RIFAMPICIN",
        "CLAVULANATE POTASSIUM": "CLAVULANIC ACID",
        # 心血管藥物
        "AMLODIPINE BESILATE": "AMLODIPINE",
        "CLOPIDOGREL HYDROGEN SULFATE": "CLOPIDOGREL",
        "BETAHISTINE DIHYDROCHLORIDE": "BETAHISTINE",
        # 抗癌藥物
        "CABOZANTINIB-MALATE": "CABOZANTINIB",
        "SUNITINIB MALATE": "SUNITINIB",
        "NIRAPARIB TOSYLATE MONOHYDRATE": "NIRAPARIB",
        # 免疫抑制劑
        "CYCLOSPORIN": "CYCLOSPORINE",
        # 抗病毒藥物
        "DARUNAVIR ETHANOLATE": "DARUNAVIR",
        # 抗組織胺
        "CETIRIZINE DIHYDROCHLORIDE": "CETIRIZINE",
        "LEVOCETIRIZINE DIHYDROCHLORIDE": "LEVOCETIRIZINE",
        # 止痛/抗發炎
        "KETOROLAC TROMETHAMINE": "KETOROLAC",
        "DICLOFENAC DIETHYLAMINE": "DICLOFENAC",
        # 局部麻醉劑
        "DIBUCAINE": "CINCHOCAINE",
        "DIBUCAINE HCL": "CINCHOCAINE",
        # 呼吸系統
        "CARBOCYSTEINE": "CARBOCISTEINE",
        "DIPROPHYLLINE": "DYPHYLLINE",
        # 抗真菌
        "CICLOPIROX OLAMINE": "CICLOPIROX",
        # 荷爾蒙相關
        "LEUPRORELIN ACETATE": "LEUPROLIDE",
        "TRIPTORELIN PAMOATE": "TRIPTORELIN",
        "PASIREOTIDE PAMOATE": "PASIREOTIDE",
        "CLOMIPHENE CITRATE": "CLOMIFENE",
        "NORETHINDRONE ACETATE": "NORETHINDRONE ENANTHATE",
        # 精神科藥物
        "ESCITALOPRAM OXALATE": "ESCITALOPRAM",
        "RIVASTIGMINE HYDROGEN TARTRATE": "RIVASTIGMINE",
        # 消化系統
        "SODIUM RABEPRAZOLE": "RABEPRAZOLE",
        # 抗癲癇/情緒穩定劑
        "DIVALPROEX SODIUM": "VALPROIC ACID",
        # 類固醇
        "CLOBETASOL-17-PROPIONATE": "CLOBETASOL PROPIONATE",
        # 止血劑
        "AMINOCAPROIC ACID EPSILON-": "AMINOCAPROIC ACID",
        # 子宮收縮劑
        "ERGONOVINE MALEATE": "ERGOMETRINE",
        # 抗感染
        "NITROFURAZONE": "NITROFURAL",
        "SULFADIAZINE SILVER": "SILVER SULFADIAZINE",
        # 胺基酸/營養補充
        "ARGININE HCL L-": "ARGININE",
        "L- GLUTAMIC ACID": "GLUTAMIC ACID",
        "LYSINE L-": "L-LYSINE",
        "CHOLINE BITARTRATE": "CHOLINE",
        # 維生素 E 變體
        "TOCOPHEROL ACETATE ALPHA": "ALPHA-TOCOPHEROL ACETATE",
        "TOCOPHEROL ACETATE ALPHA D-": "ALPHA-TOCOPHEROL SUCCINATE",
        "TOCOPHEROL ALPHA D-": "ALPHA-TOCOPHEROL SUCCINATE",
        "TOCOPHEROL ALPHA DL-": "ALPHA-TOCOPHEROL SUCCINATE",
        "TOCOPHEROL ALPHA-": "ALPHA-TOCOPHEROL ACETATE",
        # 咖啡因
        "CAFFEINE HYDRATE": "CAFFEINE",
        # 水楊酸
        "SODIUM SALICYLATE": "SALICYLIC ACID",
        # 植物鹼
        "BERBERINE TANNATE": "BERBERINE",
        "GLYCYRRHIZIN": "GLYCYRRHIZIC ACID",
        # 黏膜保護劑
        "HYDROXYPROPYLMETHYLCELLULOSE": "HYPROMELLOSE",
        # 凝血因子
        "ANTIHEMOPHILIC FACTOR": "TUROCTOCOG ALFA",
        "FACTOR VIII": "TUROCTOCOG ALFA",
        "RFIXFC": "EFTRENONACOG ALFA",
        # 呼吸道用藥
        "VILANTEROL TRIFENATATE": "VILANTEROL",
        # 其他
        "CHLORIDE": "CHLORIDE ION",
        # ===== PubChem 橋接發現的同義詞 =====
        "ALCOHOL 95%": "ETHANOL",
        "DIHYDROERGOTOXINE METHANESULFONATE": "ERGOLOID MESYLATE",
        "DIHYDROXYPROPYL THEOPHYLLINE": "DYPHYLLINE",
        "POTASSIUM PHOSPHATE MONOBASIC": "MONOPOTASSIUM PHOSPHATE",
        # ===== ChEMBL 橋接發現的同義詞 =====
        "GRAMICIDIN": "GRAMICIDIN D",
        # ===== 2026-03-03 API 查詢新增 (RxNorm 16 + PubChem 49 + ChEMBL 4) =====
        "ALENDRONATE": "ALENDRONIC ACID",
        "ALUMINUM": "ALUMINUM HYDROXIDE",
        "ANAGRELIDE": "ANAGRELIDE",
        "ANHYDROUS": "TEZACITABINE",
        "ASPARTATE": "ASPARTIC ACID",
        "ATOSIBAN": "ATOSIBAN",
        "BETAMETHASONE": "BETAMETHASONE",
        "BUCLIZINE": "BUCLIZINE",
        "CAFFEINE": "CAFFEINE",
        "CALCIUM": "CALCIUM",
        "CARRIER": "LEVOCARNITINE",
        "CEPHALORIDINE": "CEFALORIDINE",
        "CHLORHEXIDINE": "CHLORHEXIDINE",
        "CICLOSPORIN": "CYCLOSPORINE",
        "CLAVULANATE": "CLAVULANIC ACID",
        "CLOPIDOGREL": "CLOPIDOGREL",
        "COCARBOXYLASE": "THIAMINE",
        "CROMOLYN": "CROMOGLICIC ACID",
        "D-GLUCOSAMINE": "GLUCOSAMINE",
        "D-Α-TOCOPHEROL": "ALPHA-TOCOPHEROL ACETATE",
        "DAPAGLIFLOZIN": "DAPAGLIFLOZIN",
        "DIFLUCORTOLONE": "DIFLUOCORTOLONE",
        "ESOMEPRAZOLE": "ESOMEPRAZOLE",
        "FLUPENTIXOL": "FLUPENTIXOL",
        "FOLINATE": "LEUCOVORIN",
        "FOLLITROPIN": "FOLLITROPIN",
        "FUSIDATE": "FUSIDIC ACID",
        "GENTAMYCIN": "GENTAMICIN",
        "GINKGO": "GINKGO BILOBA",
        "GLYCYRRHIZINATE": "GLYCYRRHIZIC ACID",
        "HISTIDINE": "HISTIDINE",
        "ISOSORBIDE": "ISOSORBIDE",
        "KAEMPFEROL": "KAEMPHEROL",
        "L-CARNITINE": "LEVOCARNITINE",
        "L-CYSTEINE": "CYSTEINE",
        "L-HISTIDINE": "HISTIDINE",
        "LYSINE": "L-LYSINE",
        "MAGNESIUM": "MAGNESIUM",
        "METHISOPRINOL": "INOSINE PRANOBEX",
        "METHYLEPHEDRINE": "DL-METHYLEPHEDRINE",
        "N": "NITROGEN",
        "N-ACETYL-L-CYSTEINE": "ACETYLCYSTEINE ZINC",
        "NINTEDANIB": "NINTEDANIB",
        "NOREPINEPHRINE": "NOREPINEPHRINE",
        "PAROXETINE": "PAROXETINE",
        "PASIREOTIDE": "PASIREOTIDE",
        "PEMETREXED": "PEMETREXED",
        "PERTUSSIS": "PERTUSSIS VACCINE",
        "PHYTOMENADIONE": "PHYLLOQUINONE",
        "PIRENZEPINE": "PIRENZEPINE",
        "PITAVASTATIN": "PITAVASTATIN",
        "POTASSIUM": "POTASSIUM IODIDE",
        "POVIDONE": "POVIDONE K30",
        "PROCATEROL": "PROCATEROL",
        "PROPOXYPHENE": "DEXTROPROPOXYPHENE",
        "PYRIDOXAL": "PYRIDOXAL",
        "PYRILAMINE": "MEPYRAMINE",
        "RECOMBINANT": "ANTIHEMOPHILIC FACTOR, HUMAN RECOMBINANT",
        "RETINOL": "VITAMIN A",
        "SACUBITRIL/VALSARTAN": "VALSARTAN",
        "SALMETEROL": "SALMETEROL",
        "SCOPOLAMINE": "SCOPOLAMINE",
        "SIBUTRAMINE": "SIBUTRAMINE",
        "TETRAHYDROZOLINE": "TETRYZOLINE",
        "THEOPHYLLINE": "THEOPHYLLINE",
        "TOCOPHEROL": "VITAMIN E",
        "TOLTERODINE": "TOLTERODINE",
        "ZINC": "ZINC",
        "ZOLPIDEM": "ZOLPIDEM",
        # ===== 2026-03-03 完整 API 查詢新增 (RxNorm 19 + PubChem 99 + ChEMBL 109 + 重疊 113 = 340 個新映射) =====
        "1-PROPANOL": "PROPYL ALCOHOL",
        "10%": "DOLASTATIN 10",
        "177LU-DOTA0-TYR3-OCTREOTATE": "LUTETIUM LU 177 DOTATATE",
        "2%": "SULFATE ION",
        "ACETAMINOPHEN": "ACETAMINOPHEN",
        "ACETATE": "SODIUM ACETATE",
        "ADAGRASIB": "MRTX849",
        "AFATINIB": "AFATINIB",
        "AGALSIDASE": "AGALSIDASE BETA",
        "ALCOHOL": "ETHANOL",
        "ALOGLIPTIN": "ALOGLIPTIN",
        "ALPHA-KETOISOLEUCINE": "ALPHA-NAPHTHOFLAVONE",
        "ALPHA-KETOLEUCINE": "ALPHA-NAPHTHOFLAVONE",
        "ALPHA-KETOPHENYLALANINE": "PHENYLPYRUVIC ACID",
        "ALPHA-KETOVALINE": "ALPHA-KETOISOVALERATE",
        "ALPROSTADIL": "ALPROSTADIL",
        "AMIDOTRIZOIC": "DIATRIZOATE",
        "AMINOETHYLSULFONIC": "TAURINE",
        "AMINOSALICYLATE": "AMINOSALICYLIC ACID",
        "AMINOSALICYLIC": "AMINOSALICYLIC ACID",
        "AMMONIA": "AMMONIA N-13",
        "ANTIBIOTICS-RESISTANT": "DELAMANID",
        "ANTITHROMBIN": "ANTITHROMBIN ALFA",
        "APROTININ": "APROTININ",
        "ARGININE": "ARGININE",
        "ASCORBATE": "SODIUM ASCORBATE",
        "ASCORBIC": "ASCORBIC ACID",
        "ASPIRIN": "ACETYLSALICYLIC ACID",
        "ATORVASTATIN": "ATORVASTATIN",
        "ATROPINE": "ATROPINE",
        "AVERAGE": "TRASTUZUMAB",
        "BACITRACIN": "BACITRACIN",
        "BALSALAZIDE": "BALSALAZIDE",
        "BENACTYZINE": "BENACTYZINE",
        "BENCYCLANE": "BENCYCLANE",
        "BENDAMUSTINE": "BENDAMUSTINE",
        "BENOXINATE": "OXYBUPROCAINE",
        "BENZHEXOL": "TRIHEXYPHENIDYL",
        "BERBERINE": "BERBERINE",
        "BETA-CAROTENE": "BETA CAROTENE",
        "BICARBONATE": "POTASSIUM BICARBONATE",
        "BICISATE": "BICISATE",
        "BIOTIN": "BIOTIN",
        "BISMUTH": "BISMUTH SUBGALLATE",
        "BISOPROLOL": "BISOPROLOL",
        "BOVINE": "PEGADEMASE",
        "BROMOCRIPTINE": "BROMOCRIPTINE",
        "BUPIVACAINE": "BUPIVACAINE",
        "CALCIFEROL": "VITAMIN D",
        "CALCIPOTRIOL": "CALCIPOTRIOL",
        "CAMPHOR": "CAMPHOR",
        "CAMPHORATE": "CAMPHOR",
        "CAMPHORATED": "CAMPHOR",
        "CAMYLOFINE": "CAMYLOFIN",
        "CANAGLIFLOZIN": "CANAGLIFLOZIN",
        "CAPMATINIB": "CAPMATINIB",
        "CAPSULAR": "HAEMOPHILIUS INFLUENZAE TYPE B STRAIN 20752 CAPSULAR POLYSACCHARIDE TETANUS TOXOID CONJUGATE ANTIGEN",
        "CAPSULE": "CHLORAMPHENICOL SUCCINATE",
        "CARBACHOL": "CARBAMOYLCHOLINE",
        "CARBON": "CARBON MONOXIDE",
        "CAROTENE": "BETA CAROTENE",
        "CASCARA": "FRANGULA PURSHIANA BARK",
        "CEFEPIME": "CEFEPIME",
        "CEFIDEROCOL": "CEFIDEROCOL",
        "CEFMENOXIME": "CEFMENOXIME",
        "CEFTAZIDIME": "CEFTAZIDIME",
        "CEFUROXIME": "CEFUROXIME",
        "CENTELLA": "CENTELLA ASIATICA",
        "CEPHALOTHIN": "CEFALOTIN",
        "CEPHAPIRIN": "CEFAPIRIN",
        "CEPHRADINE": "CEFRADINE",
        "CETRAXATE": "CIPROFLOXACIN",
        "CETYLPYRIDINIUM": "CETYLPYRIDINIUM",
        "CHARCOAL": "ACTIVATED CHARCOAL",
        "CHLOPHEDIANOL": "CLOFEDANOL",
        "CHLORAMPENICOL": "CHLORAMPHENICOL",
        "CHLORMETHINE": "MECHLORETHAMINE",
        "CHLORPHENESIN": "CHLORPHENESIN",
        "CHOLINE": "CHOLINE SALICYLATE",
        "CHONDROITIN": "CHONDROITIN SULFATE",
        "CITRULLINE": "CITRULLINE",
        "CLOFIBRATE": "CLOFIBRATE",
        "CLOSTRIDIUM": "COLLAGENASE CLOSTRIDIUM HISTOLYTICUM",
        "CLOTIAPINE": "CLOTHIAPINE",
        "CLOVE": "CLOVE OIL",
        "COAGULATION": "ANTIHEMOPHILIC FACTOR HUMAN",
        "COATED": "PLANTAGO SEED",
        "COBIMETINIB": "COBIMETINIB",
        "COLISTIN": "COLISTIMETHATE",
        "CONC.": "ALFENTANIL",
        "CONJUGATED": "CONJUGATED ESTROGENS",
        "COPPER": "COPPER",
        "CORYDALIS": "TETRAHYDROPALMATINE",
        "CRYSTALLINE": "CEFTIOFUR",
        "CYANOCOBALAMIN": "CYANOCOBALAMIN",
        "CYANOCOBALAMINE": "CYANOCOBALAMIN",
        "CYPROHEPTADINE": "CYPROHEPTADINE",
        "CYSTEINE": "CYSTEINE",
        "DABIGATRAN": "DABIGATRAN",
        "DEHYDROEPIANDROSTERONE": "PRASTERONE",
        "DESMOPRESSIN": "DESMOPRESSIN",
        "DEXKETOPROFEN": "DEXKETOPROFEN",
        "DEXTRAN": "DEXTRAN",
        "DEXTROMETHORPHAN": "DEXTROMETHORPHAN",
        "DIBASIC": "CALCIUM PHOSPHATE",
        "DIFLORASONE": "DIFLORASONE",
        "DIHYDROERGOTAMINE": "DIHYDROERGOTAMINE",
        "DILUTED": "ISOSORBIDE DINITRATE",
        "DIMERCAPTOSUCCINIC": "SUCCIMER",
        "DIMETHOTHIAZINE": "DIMETOTIAZINE",
        "DINUTUXIMAB": "DINUTUXIMAB",
        "DIPHENHYDRAMINE": "DIPHENHYDRAMINE",
        "DL-ALPHA-TOCOPHERYL": "VITAMIN E",
        "DL-ARGININE": "ARGININE",
        "DOCOSAHEXAENOIC": "DOCONEXENT",
        "DORIPENEM": "DORIPENEM",
        "DOTHIEPIN": "DOSULEPIN",
        "DOXYCYCLINE": "DOXYCYCLINE",
        "DOXYLAMINE": "DOXYLAMINE",
        "EDOXABAN": "EDOXABAN",
        "EICOSAPENTAENOIC": "ICOSAPENT",
        "EPINEPHRINE": "EPINEPHRINE",
        "EPTACOG": "COAGULATION FACTOR VIIA RECOMBINANT HUMAN",
        "ERGOT": "ERGOTAMINE",
        "ERYTHROMYCIN": "ERYTHROMYCIN",
        "ESTRADIOL": "ESTRADIOL CYPIONATE",
        "ESTROGENS": "SYNTHETIC CONJUGATED ESTROGENS, A",
        "ETHANOL": "ETHANOL",
        "ETILEFRIN": "ETILEFRINE",
        "F18-FLORBETABEN": "FLORBETABEN (18F)",
        "FEDRATINIB": "FEDRATINIB",
        "FERRIC": "FERRIC HYDROXIDE",
        "FERRIC-HYDROXIDE-SUCROSE": "FERRIC HYDROXIDE",
        "FERROUS": "FERROUS FUMARATE",
        "FISH": "FISH OIL",
        "FLAVINEADENINE": "FLAVIN ADENINE DINUCLEOTIDE",
        "FLUCICLOVINE": "FLUCICLOVINE (18F)",
        "FLUDEOXYGLUCOSE": "FLUDEOXYGLUCOSE (18F)",
        "FLUFENAMATE": "FLUFENAMIC ACID",
        "FLUOROURACIL": "FLUOROURACIL",
        "FLUPHENAZINE": "FLUPHENAZINE",
        "FLUTEMETAMOL": "FLUTEMETAMOL (18F)",
        "FOLIC": "FOLIC ACID",
        "FOLINIC": "LEUCOVORIN",
        "FONAZINE": "DIMETOTIAZINE",
        "FOSAPREPITANT": "FOSAPREPITANT",
        "FOSFOMYCIN": "FOSFOMYCIN",
        "FRADIOMYCIN": "NEOMYCIN",
        "GABEXATE": "GABEXATE",
        "GADOBENATE": "GADOBENIC ACID",
        "GADOLINIUM": "MOTEXAFIN GADOLINIUM",
        "GADOPENTETATE": "GADOPENTETIC ACID",
        "GALLIUM": "GALLIUM NITRATE",
        "GAMMA": "GAMMA-TOCOPHEROL",
        "GINSENG": "GINSENG",
        "GLUCONATE": "GLUCONIC ACID",
        "GLUTAMATE": "GLUTAMIC ACID",
        "GLUTATHIONE": "GLUTATHIONE",
        "GLYCOL": "POLYETHYLENE GLYCOL",
        "GLYCOPYRROLATE": "GLYCOPYRRONIUM",
        "GLYCYRRHIZIN": "GLYCYRRHIZIC ACID",
        "GMP": "GUANOSINE-5'-MONOPHOSPHATE",
        "GUAIACOL": "GUAIACOL",
        "GUAIPHENESIN": "GUAIFENESIN",
        "HALCINONIDE": "HALCINONIDE",
        "HEPARINOID": "DANAPAROID",
        "HETASTARCH": "HYDROXYETHYL STARCH",
        "HIGHLY": "INSULIN BEEF",
        "HOP": "(1S,2S,5S)2-(4-GLUTARIDYLBENZYL)-5-PHENYL-1-CYCLOHEXANOL",
        "HYALURONATE": "HYALURONIC ACID",
        "HYDROCORTISONE": "HYDROCORTISONE VALERATE",
        "HYDROGEN": "HYDROGEN PEROXIDE",
        "HYDROXYZINE": "HYDROXYZINE",
        "HYOSCINE": "SCOPOLAMINE",
        "I-123": "IOFLUPANE I-123",
        "IBUPROFEN": "IBUPROFEN",
        "ICHTHAMMOL": "HYDROXYUREA",
        "IMMUNOGLOBULIN": "HUMAN IMMUNOGLOBULIN G",
        "INOSITOL": "INOSITOL",
        "INSULIN": "INSULIN HUMAN",
        "INTERFERON": "INTERFERON ALFA",
        "IODINE": "IODINE",
        "IODINE-131": "IODINE",
        "IPECAC": "IPECAC",
        "IRON": "IRON",
        "ISOPROPYLANTIPYRINE": "PROPYPHENAZONE",
        "ISOPROTERENOL": "ISOPRENALINE",
        "ISOSORBIDE-5-MONONITRATE": "ISOSORBIDE MONONITRATE",
        "ISPAGHULA": "PLANTAGO SEED",
        "KAOLIN": "KAOLIN",
        "KETOTIFEN": "KETOTIFEN",
        "L-LYSINE": "L-LYSINE",
        "LACTIC": "LACTIC ACID",
        "LACTULOSE": "LACTULOSE",
        "LANTHANUM": "LANTHANUM CARBONATE",
        "LAPATINIB": "LAPATINIB",
        "LENVATINIB": "LENVATINIB",
        "LEUCOMYCIN": "KITASAMYCIN",
        "LIGNOCAINE": "LIDOCAINE",
        "LORCASERIN": "LORCASERIN",
        "MACROGOL": "POLYETHYLENE GLYCOL",
        "MALTOSE": "MALTOSE",
        "MANGANESE": "MANGANESE",
        "MEBHYDROLINE": "MEBHYDROLIN",
        "MECLIZINE": "MECLIZINE",
        "MECLOFENAMATE": "MECLOFENAMIC ACID",
        "MENADIOL": "KAPPADIONE",
        "MENADIONE": "MENADIONE",
        "MENOTROPHIN": "MENOTROPINS",
        "MENTHOL": "RACEMENTHOL",
        "MEPIRIZOLE": "EPIRIZOLE",
        "MEPREDNISONE": "MEPREDNISONE",
        "MEROPENEM": "MEROPENEM",
        "METFORMIN": "METFORMIN",
        "METHYLDOPA": "METHYLDOPA",
        "METHYLERGOMETRINE": "METHYLERGOMETRINE",
        "METHYLERGONOVINE": "METHYLERGOMETRINE",
        "METHYLPREDNISOLONE": "METHYLPREDNISOLONE ACEPONATE",
        "METHYLPREDNISONE": "METHYLPREDNISONE",
        "METOCLOPRAMIDE": "METOCLOPRAMIDE",
        "MINERAL": "MINERAL OIL",
        "MITIGLINIDE": "MITIGLINIDE",
        "MITOMYCIN": "MITOMYCIN",
        "MONOSODIUM": "SODIUM PHOSPHATE, MONOBASIC",
        "N-DIETHYL-META-TOLUAMIDE": "DIETHYLTOLUAMIDE",
        "NADROPARINE": "NADROPARIN",
        "NALDEMEDINE": "NALDEMEDINE",
        "NANDROLONE": "NANDROLONE PHENPROPIONATE",
        "NATIVE": "SODIUM FLUORIDE",
        "NEMONOXACIN": "NEMONOXACIN",
        "NEUSILIN": "MAGNESIUM ALUMINUM SILICATE",
        "NICOTINE": "NICOTINE",
        "NICOTINIC": "NIACIN",
        "NORETHINDRONE": "NORETHINDRONE ENANTHATE",
        "OCTOCOG": "ANTIHEMOPHILIC FACTOR, HUMAN RECOMBINANT",
        "OESTROGEN": "CONJUGATED ESTROGENS",
        "OKA": "9,10-DEEPITHIO-9,10-DIDEHYDROACANTHIFOLICIN",
        "OMEGA-3-": "OMEGA-3 FATTY ACIDS",
        "ONDANSETRON": "ONDANSETRON",
        "OPIUM": "OPIUM",
        "ORNITHINE": "ORNITHINE",
        "OX;;CALCIUM": "CALCIUM CHLORIDE",
        "OYSTER": "VARENICLINE",
        "PANTOPRAZOLE": "PANTOPRAZOLE",
        "PANTOTHENOL": "DEXPANTHENOL",
        "PANTOTHENYL": "DEXPANTHENOL",
        "PARACETAMOL": "ACETAMINOPHEN",
        "PASINIAZIDE": "ISONIAZID",
        "PEFLOXACINE": "PEFLOXACIN",
        "PENICILLIN": "BENZYLPENICILLIN",
        "PEPPERMINT": "PEPPERMINT OIL",
        "PERAMIVIR": "PERAMIVIR",
        "PERFLUOROBUTANE": "PERFLUBUTANE",
        "PERILLA": "PERILLYL ALCOHOL",
        "PERINDOPRIL": "PERINDOPRIL",
        "PHENOTHRIN": "PHENOTHRIN",
        "PHOSPHATE": "PHOSPHATE ION",
        "PHYTONADIONE": "PHYLLOQUINONE",
        "PICOSULFATE": "PICOSULFURIC ACID",
        "PIPERAZINE": "PIPERAZINE",
        "PLANTAGO": "PLANTAGO SEED",
        "PODOPHYLLOTOXIN": "PODOFILOX",
        "POLYETHYLENE": "POLYETHYLENE GLYCOL",
        "PONATINIB": "PONATINIB",
        "PRAMOXINE": "PRAMOCAINE",
        "PRESERVATIVES": "DICYCLOMINE",
        "PRIDINOL": "PRIDINOL",
        "PRIMACLONE": "PRIMIDONE",
        "PROCHLORPERAZINE": "PROCHLORPERAZINE",
        "PROMETHAZINE": "PROMETHAZINE",
        "PROTHIONAMIDE": "PROTIONAMIDE",
        "PSEUDOEPHEDRINE": "PSEUDOEPHEDRINE",
        "PYRANTEL": "PYRANTEL",
        "PYRIDOXINE": "PYRIDOXINE",
        "QUININE": "QUININE",
        "QUIZARTINIB": "QUIZARTINIB",
        "RADIOACTIVE": "CYANOCOBALAMIN",
        "RADIUM-223": "RADIUM RA 223 DICHLORIDE",
        "RHASB": "GALSULFASE",
        "RHGALNS": "ELOSULFASE ALFA",
        "RIBOFLAVIN": "RIBOFLAVIN",
        "RIBOFLAVIN-5-PHOSPHATE": "FLAVIN MONONUCLEOTIDE",
        "RISEDRONATE": "RISEDRONIC ACID",
        "RIZATRIPTAN": "RIZATRIPTAN",
        "ROPIVACAINE": "ROPIVACAINE",
        "ROSE": "ROSE BENGAL",
        "SAFINAMIDE": "SAFINAMIDE",
        "SALICYLIC": "SALICYLIC ACID",
        "SALINE": "SODIUM CHLORIDE",
        "SAPROPTERIN": "SAPROPTERIN",
        "SELUMETINIB": "SELUMETINIB",
        "SENNOSIDES": "SENNOSIDES",
        "SIPONIMOD": "SIPONIMOD",
        "SIROLIMUS": "SIROLIMUS",
        "SITAGLIPTIN": "SITAGLIPTIN",
        "SOMATROPIN": "SOMATOTROPIN",
        "SORAFENIB": "SORAFENIB",
        "SOTORASIB": "AMG-510",
        "SOYBEAN": "SOYBEAN OIL",
        "STANNOUS": "STANNOUS FLUORIDE",
        "SULFAMINE": "SULFANILAMIDE",
        "SULFISOMIDINE": "SULFAISODIMIDINE",
        "SULPHUR": "SULFUR HEXAFLUORIDE",
        "SULTAMICILLIN": "SULBACTAM",
        "SYNTHETIC": "SYNTHETIC CONJUGATED ESTROGENS, B",
        "TAK-491": "AZILSARTAN MEDOXOMIL",
        "TALAZOPARIB": "TALAZOPARIB",
        "TC-99M": "TECHNETIUM TC-99M PYROPHOSPHATE",
        "TESTOSTERONE": "TESTOSTERONE UNDECANOATE",
        "THEOBROMINUM": "THEOBROMINE",
        "THIAMINE": "THIAMINE",
        "THIOCARLIDE": "TIOCARLIDE",
        "THYME": "THYMOL",
        "THYMOXAMINE": "MOXISYLYTE",
        "THYROID": "THYROID, PORCINE",
        "TIAGABINE": "TIAGABINE",
        "TIRBANIBULIN": "KX-01",
        "TIROFIBAN": "TIROFIBAN",
        "TOCOPHEROL-ALPHA-D": "VITAMIN E",
        "TOCOPHERYL": "VITAMIN E",
        "TOLMETIN": "TOLMETIN",
        "TORSEMIDE": "TORASEMIDE",
        "TRAMETINIB": "TRAMETINIB",
        "TRICALCIUM": "CALCIUM CITRATE",
        "TRIENTINE": "TRIETHYLENETETRAMINE",
        "TRIMEPRAZINE": "ALIMEMAZINE",
        "TRIPOTASSIUM": "POTASSIUM CITRATE",
        "TRIPROLIDINE": "TRIPROLIDINE",
        "TRISILICATE": "MAGNESIUM TRISILICATE",
        "TURPENTINE": "TURPENTINE",
        "URSODESOXYCHOLIC": "URSODEOXYCHOLIC ACID",
        "URSODIOL": "URSODEOXYCHOLIC ACID",
        "VALACICLOVIR": "VALACICLOVIR",
        "VALACYCLOVIR": "VALACICLOVIR",
        "VALBENAZINE": "VALBENAZINE",
        "VARDENAFIL": "VARDENAFIL",
        "VITAMINE": "ALPHA-TOCOPHEROL SUCCINATE",
        "WARFARIN": "WARFARIN",
        "WITHOUT": "TRICHLOROETHYLENE",
        "XANTHINOL": "XANTHINOL",
    }

    for alias, canonical in synonym_map.items():
        if canonical in index and alias not in index:
            index[alias] = index[canonical]

    return index


def map_ingredient_to_drugbank(
    ingredient: str,
    name_index: Dict[str, str],
) -> Optional[str]:
    """將單一成分映射到 DrugBank ID

    映射策略（優先順序）：
    1. 完全匹配
    2. 移除鹽類後綴後匹配
    3. 使用基本名稱匹配

    Args:
        ingredient: 標準化後的成分名稱
        name_index: 名稱索引

    Returns:
        DrugBank ID，若無法映射則回傳 None
    """
    if not ingredient:
        return None

    ingredient = ingredient.upper().strip()

    # 1. 完全匹配
    if ingredient in name_index:
        return name_index[ingredient]

    # 2. 移除台灣 FDA 常見的鹽類/水合物/製藥標準後綴
    salt_patterns = [
        # 鹽類
        r"\s+HCL$", r"\s+HYDROCHLORIDE$", r"\s+SODIUM$",
        r"\s+POTASSIUM$", r"\s+SULFATE$", r"\s+SULPHATE$",
        r"\s+MALEATE$", r"\s+ACETATE$", r"\s+CITRATE$",
        r"\s+PHOSPHATE$", r"\s+BROMIDE$", r"\s+CHLORIDE$",
        r"\s+TARTRATE$", r"\s+HBR$", r"\s+HYDROBROMIDE$",
        r"\s+FUMARATE$", r"\s+SUCCINATE$", r"\s+MESYLATE$",
        r"\s+BESYLATE$", r"\s+CALCIUM$", r"\s+MAGNESIUM$",
        r"\s+NITRATE$", r"\s+LACTATE$", r"\s+GLUCONATE$",
        r"\s+DISODIUM$", r"\s+MONONITRATE$", r"\s+METHYLSULFATE$",
        r"\s+MEDOXOMIL$",
        # 水合物
        r"\s+ANHYDROUS$", r"\s+MONOHYDRATE$", r"\s+DIHYDRATE$",
        r"\s+TRIHYDRATE$", r"\s+TETRAHYDRATE$", r"\s+HEXAHYDRATE$",
        r"\s+SESQUIHYDRATE$", r"\s+HEMIHYDRATE$", r"\s+HYDROUS$",
        # 酯類
        r"\s+DIPROPIONATE$", r"\s+PROPIONATE$", r"\s+ACETONIDE$",
        r"\s+VALERATE$", r"\s+BUTYRATE$", r"\s+PALMITATE$",
        r"\s+FUROATE$", r"\s+PIVALATE$",
        # 製藥標準/製劑
        r"\s+USP$", r"\s+BP$", r"\s+JP$", r"\s+EP$",
        r"\s+MICRONIZED$", r"\s+GRANULE$", r"\s+POWDER$",
        r"\s+DRIED\s+GEL$", r"\s+EMULSION\s+\d+%$",
    ]

    base_ingredient = ingredient
    for pattern in salt_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient, flags=re.IGNORECASE)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 2b. 移除 L-/D-/DL-/ALPHA-/BETA- 前綴
    prefix_patterns = [r"^L-", r"^D-", r"^DL-", r"^ALPHA-", r"^BETA-", r"^DL-ALPHA-"]
    base_ingredient = ingredient
    for pattern in prefix_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient, flags=re.IGNORECASE)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 2c. 嘗試移除尾部的 L-/D-/DL-（台灣特有格式如 "METHIONINE DL-"）
    suffix_stereo_patterns = [r"\s+L-$", r"\s+D-$", r"\s+DL-$"]
    base_ingredient = ingredient
    for pattern in suffix_stereo_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 3. 嘗試移除括號內容
    base_ingredient = re.sub(r"\s*\([^)]*\)", "", ingredient).strip()
    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 4. 組合策略：同時移除前綴和後綴
    base_ingredient = ingredient
    # 先移除前綴
    for pattern in prefix_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient, flags=re.IGNORECASE)
    # 再移除後綴
    for pattern in salt_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient, flags=re.IGNORECASE)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    return None


def map_fda_drugs_to_drugbank(
    fda_df: pd.DataFrame,
    drugbank_df: Optional[pd.DataFrame] = None,
    use_herbal_mapping: bool = True,
) -> pd.DataFrame:
    """將台灣 FDA 藥品映射到 DrugBank

    映射策略（依優先順序）：
    1. DrugBank 直接映射（完全匹配或同義詞）
    2. 中草藥映射（若啟用）
    3. 鹽類後綴移除後再匹配

    Args:
        fda_df: 台灣 FDA 藥品 DataFrame
        drugbank_df: DrugBank 詞彙表（可選）
        use_herbal_mapping: 是否啟用中草藥映射（預設 True）

    Returns:
        包含映射結果的 DataFrame，包含 mapping_source 欄位
    """
    if drugbank_df is None:
        drugbank_df = load_drugbank_vocab()

    # 建立索引
    name_index = build_name_index(drugbank_df)

    # 載入中草藥映射器（若啟用）
    herbal_mapper = None
    if use_herbal_mapping:
        try:
            from .herbal_mapper import is_herbal_ingredient, map_herbal_ingredient
            herbal_mapper = (is_herbal_ingredient, map_herbal_ingredient)
            logger.debug("中草藥映射已啟用")
        except ImportError:
            logger.warning("無法載入中草藥映射模組")

    results = []

    for _, row in fda_df.iterrows():
        ingredient_str = row.get("主成分略述", "")
        if not ingredient_str:
            continue

        # 提取所有成分及同義詞
        synonyms_data = get_all_synonyms(ingredient_str)

        for main_name, synonyms in synonyms_data:
            drugbank_id = None
            mapping_source = "failed"

            # 1. 先嘗試主名稱（DrugBank 直接/同義詞映射）
            drugbank_id = map_ingredient_to_drugbank(main_name, name_index)
            if drugbank_id:
                mapping_source = "drugbank"

            # 2. 若失敗，嘗試同義詞
            if drugbank_id is None:
                for syn in synonyms:
                    drugbank_id = map_ingredient_to_drugbank(syn, name_index)
                    if drugbank_id:
                        mapping_source = "drugbank_synonym"
                        break

            # 3. 若仍失敗，嘗試中草藥映射
            if drugbank_id is None and herbal_mapper:
                is_herbal, map_herbal = herbal_mapper
                if is_herbal(main_name):
                    herbal_target = map_herbal(main_name)
                    if herbal_target:
                        drugbank_id = map_ingredient_to_drugbank(herbal_target, name_index)
                        if drugbank_id:
                            mapping_source = "herbal"
                            logger.debug(f"中草藥映射: {main_name} -> {herbal_target}")

            results.append({
                "許可證字號": row["許可證字號"],
                "中文品名": row["中文品名"],
                "原始主成分": ingredient_str,
                "標準化成分": main_name,
                "同義詞": "; ".join(synonyms) if synonyms else "",
                "drugbank_id": drugbank_id,
                "映射成功": drugbank_id is not None,
                "映射來源": mapping_source,
            })

    return pd.DataFrame(results)


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算映射統計

    Args:
        mapping_df: 映射結果 DataFrame

    Returns:
        統計字典，包含整體和各來源的統計
    """
    total = len(mapping_df)
    success = mapping_df["映射成功"].sum()
    unique_ingredients = mapping_df["標準化成分"].nunique()
    unique_drugbank = mapping_df[mapping_df["映射成功"]]["drugbank_id"].nunique()

    stats = {
        "total_ingredients": total,
        "mapped_ingredients": int(success),
        "mapping_rate": success / total if total > 0 else 0,
        "unique_ingredients": unique_ingredients,
        "unique_drugbank_ids": unique_drugbank,
    }

    # 如果有映射來源欄位，加入來源統計
    if "映射來源" in mapping_df.columns:
        source_counts = mapping_df["映射來源"].value_counts().to_dict()
        stats["by_source"] = source_counts

    return stats
