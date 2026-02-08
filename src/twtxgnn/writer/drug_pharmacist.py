"""Drug-centric Pharmacist Notes Writer."""

from pathlib import Path

from ..reviewer.llm_client import get_prompt_path
from .base import BaseNotesWriter


class DrugPharmacistNotesWriter(BaseNotesWriter):
    """Generates Drug Pharmacist Notes from Drug Evidence Pack.

    Focus areas (drug-centric):
    - One drug with multiple predicted indications
    - Drug-level safety (ADR, contraindications, DDI)
    - Per-indication considerations
    - Monitoring and patient education
    - Taiwan availability
    """

    writer_type = "drug_pharmacist"
    prompt_name = "pharmacist_v4"

    @property
    def prompt_path(self) -> Path:
        """Get the path to the drug-centric pharmacist prompt file (v4)."""
        return get_prompt_path("pharmacist_v4")
