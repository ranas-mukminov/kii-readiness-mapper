from kii_readiness_mapper.assessment.kii_subject_detector import KiiSubjectDetector
from kii_readiness_mapper.domain.models import OrganizationProfile, SystemProfile
from kii_readiness_mapper.domain.enums import Sector, SystemType

def test_detect_subject_health():
    detector = KiiSubjectDetector()
    profile = OrganizationProfile(
        name="Clinic",
        sector=Sector.HEALTH,
        systems=[]
    )
    result = detector.detect(profile)
    assert result["is_potential_subject"] is True
    assert result["confidence"] == "high"

def test_detect_subject_other_critical():
    detector = KiiSubjectDetector()
    profile = OrganizationProfile(
        name="Factory",
        sector=Sector.OTHER,
        systems=[
            SystemProfile(id="s1", name="S1", type=SystemType.SCADA, is_critical=True)
        ]
    )
    result = detector.detect(profile)
    assert result["is_potential_subject"] is True
    # Confidence might be medium if sector is not explicit but has critical systems
    assert result["confidence"] in ["medium", "high"]

def test_detect_subject_none():
    detector = KiiSubjectDetector()
    profile = OrganizationProfile(
        name="Shop",
        sector=Sector.OTHER,
        systems=[]
    )
    result = detector.detect(profile)
    assert result["is_potential_subject"] is False
