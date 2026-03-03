"""實體映射模組

包含：
- DrugBank 映射
- 疾病映射
- 多來源橋接（RxNorm、PubChem、ChEMBL）
- 中草藥映射（TCMSP）
"""

from .normalizer import normalize_ingredient, extract_ingredients, get_all_synonyms
from .drugbank_mapper import (
    load_drugbank_vocab,
    build_name_index,
    map_ingredient_to_drugbank,
    map_fda_drugs_to_drugbank,
    get_mapping_stats,
)
from .disease_mapper import (
    load_disease_vocab,
    build_disease_index,
    extract_indications,
    translate_indication,
    map_indication_to_disease,
    map_fda_indications_to_diseases,
    get_indication_mapping_stats,
    DISEASE_DICT,
)
from .herbal_mapper import (
    map_herbal_ingredient,
    is_herbal_ingredient,
    get_herbal_info,
    HERBAL_DRUGBANK_MAPPINGS,
)
from .multi_source_mapper import MultiSourceMapper

__all__ = [
    # Normalizer
    "normalize_ingredient",
    "extract_ingredients",
    "get_all_synonyms",
    # Drug mapping
    "load_drugbank_vocab",
    "build_name_index",
    "map_ingredient_to_drugbank",
    "map_fda_drugs_to_drugbank",
    "get_mapping_stats",
    # Disease mapping
    "load_disease_vocab",
    "build_disease_index",
    "extract_indications",
    "translate_indication",
    "map_indication_to_disease",
    "map_fda_indications_to_diseases",
    "get_indication_mapping_stats",
    "DISEASE_DICT",
    # Herbal mapping
    "map_herbal_ingredient",
    "is_herbal_ingredient",
    "get_herbal_info",
    "HERBAL_DRUGBANK_MAPPINGS",
    # Multi-source mapping
    "MultiSourceMapper",
]
