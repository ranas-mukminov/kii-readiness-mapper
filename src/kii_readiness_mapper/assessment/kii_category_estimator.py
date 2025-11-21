from ..domain.models import SystemProfile
from ..domain.enums import KiiCategory

class KiiCategoryEstimator:
    def estimate(self, system: SystemProfile) -> KiiCategory:
        """
        Estimate the potential category of a system based on heuristics.
        This is a VERY ROUGH estimation.
        """
        if not system.is_critical:
            return KiiCategory.NONE

        # Simple heuristics based on user count and external access
        # In reality, this depends on specific impact criteria (social, political, economic, ecological, defense)
        
        if system.users_count > 100000:
            return KiiCategory.CAT_1
        elif system.users_count > 10000:
            return KiiCategory.CAT_2
        elif system.users_count > 0:
            return KiiCategory.CAT_3
            
        return KiiCategory.UNKNOWN
