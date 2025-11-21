from kii_readiness_mapper.assessment.controls_checker import ControlsChecker
from kii_readiness_mapper.domain.models import OrganizationProfile
from kii_readiness_mapper.domain.enums import Sector

def test_check_controls():
    checker = ControlsChecker()
    profile = OrganizationProfile(name="Org", sector=Sector.OTHER)
    answers = {"security_responsible": False, "antivirus": False}
    
    gaps = checker.check(profile, answers)
    assert len(gaps) >= 2
    ids = [g.measure_id for g in gaps]
    assert "org_security_responsible" in ids
    assert "tech_antivirus" in ids
