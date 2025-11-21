from typing import List
from ..domain.models import Gap
from ..domain.enums import CriticalityLevel

class GapsPrioritizer:
    def prioritize(self, gaps: List[Gap]) -> List[Gap]:
        """
        Sort gaps by criticality.
        """
        order = {
            CriticalityLevel.CRITICAL: 0,
            CriticalityLevel.HIGH: 1,
            CriticalityLevel.MEDIUM: 2,
            CriticalityLevel.LOW: 3
        }
        
        return sorted(gaps, key=lambda g: order.get(g.criticality, 99))
