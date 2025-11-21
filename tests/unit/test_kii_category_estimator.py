from kii_readiness_mapper.assessment.kii_category_estimator import KiiCategoryEstimator
from kii_readiness_mapper.domain.models import SystemProfile
from kii_readiness_mapper.domain.enums import SystemType, KiiCategory

def test_estimate_category():
    estimator = KiiCategoryEstimator()
    
    # Not critical
    s1 = SystemProfile(id="s1", name="S1", type=SystemType.IS, is_critical=False)
    assert estimator.estimate(s1) == KiiCategory.NONE
    
    # Critical, small users
    s2 = SystemProfile(id="s2", name="S2", type=SystemType.IS, is_critical=True, users_count=100)
    assert estimator.estimate(s2) == KiiCategory.CAT_3
    
    # Critical, huge users
    s3 = SystemProfile(id="s3", name="S3", type=SystemType.IS, is_critical=True, users_count=200000)
    assert estimator.estimate(s3) == KiiCategory.CAT_1
