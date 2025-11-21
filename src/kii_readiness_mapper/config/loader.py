import yaml
from pathlib import Path
from typing import Union
from ..domain.models import OrganizationProfile

class ConfigLoader:
    @staticmethod
    def load_profile(path: Union[str, Path]) -> OrganizationProfile:
        """
        Load an organization profile from a YAML or JSON file.
        """
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Profile file not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return OrganizationProfile.model_validate(data)

    @staticmethod
    def save_profile(profile: OrganizationProfile, path: Union[str, Path]) -> None:
        """
        Save an organization profile to a YAML file.
        """
        path = Path(path)
        # Ensure parent directory exists
        path.parent.mkdir(parents=True, exist_ok=True)
        
        data = profile.model_dump(mode="json", exclude_none=True)
        
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
