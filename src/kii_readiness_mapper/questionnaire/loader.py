import yaml
from pathlib import Path
from typing import List, Optional
from .model import Questionnaire, Section
from ..domain.enums import Sector, SystemType

class QuestionnaireLoader:
    def __init__(self, banks_dir: Path):
        self.banks_dir = banks_dir

    def load_questionnaire(self, sector: Optional[Sector] = None, system_type: Optional[SystemType] = None) -> Questionnaire:
        """
        Load and merge questionnaire sections based on sector and system type.
        Always loads 'common.yaml'.
        """
        sections: List[Section] = []
        
        # Load common questions
        common_path = self.banks_dir / "common.yaml"
        if common_path.exists():
            sections.extend(self._load_file(common_path))

        # Load sector specific questions
        if sector:
            sector_path = self.banks_dir / f"sector_{sector.value}.yaml"
            if sector_path.exists():
                sections.extend(self._load_file(sector_path))

        # Load system type specific questions
        if system_type:
            # For now we just load system_types.yaml for all types, 
            # but we could have specific files like system_scada.yaml
            type_path = self.banks_dir / "system_types.yaml"
            if type_path.exists():
                sections.extend(self._load_file(type_path))
        
        return Questionnaire(sections=sections)

    def _load_file(self, path: Path) -> List[Section]:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            # Validate and parse sections
            return [Section.model_validate(s) for s in data.get("sections", [])]
