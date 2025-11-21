import pytest
from kii_readiness_mapper.config.loader import ConfigLoader
from kii_readiness_mapper.domain.models import OrganizationProfile
from kii_readiness_mapper.domain.enums import Sector

def test_load_valid_profile(tmp_path):
    profile_content = """
    name: "Test Org"
    sector: "health"
    systems:
      - id: "sys1"
        name: "System 1"
        type: "is"
    """
    profile_file = tmp_path / "profile.yaml"
    profile_file.write_text(profile_content, encoding="utf-8")
    
    profile = ConfigLoader.load_profile(profile_file)
    assert isinstance(profile, OrganizationProfile)
    assert profile.name == "Test Org"
    assert profile.sector == Sector.HEALTH
    assert len(profile.systems) == 1
    assert profile.systems[0].id == "sys1"

def test_load_nonexistent_profile():
    with pytest.raises(FileNotFoundError):
        ConfigLoader.load_profile("nonexistent.yaml")
