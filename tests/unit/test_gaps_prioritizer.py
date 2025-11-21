from kii_readiness_mapper.assessment.gaps_prioritizer import GapsPrioritizer
from kii_readiness_mapper.domain.models import Gap
from kii_readiness_mapper.domain.enums import MeasureType, CriticalityLevel

def test_prioritize_gaps():
    prioritizer = GapsPrioritizer()
    g1 = Gap(measure_id="1", type=MeasureType.ORG, criticality=CriticalityLevel.LOW, description="d", recommendation="r")
    g2 = Gap(measure_id="2", type=MeasureType.ORG, criticality=CriticalityLevel.CRITICAL, description="d", recommendation="r")
    g3 = Gap(measure_id="3", type=MeasureType.ORG, criticality=CriticalityLevel.HIGH, description="d", recommendation="r")
    
    gaps = [g1, g2, g3]
    sorted_gaps = prioritizer.prioritize(gaps)
    
    assert sorted_gaps[0].criticality == CriticalityLevel.CRITICAL
    assert sorted_gaps[1].criticality == CriticalityLevel.HIGH
    assert sorted_gaps[2].criticality == CriticalityLevel.LOW
