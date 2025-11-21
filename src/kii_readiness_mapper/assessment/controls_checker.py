from typing import List, Dict, Any
from ..domain.models import Gap, OrganizationProfile
from ..domain.enums import MeasureType, CriticalityLevel

class ControlsChecker:
    def check(self, profile: OrganizationProfile, answers: Dict[str, Any]) -> List[Gap]:
        """
        Check for gaps in controls based on profile and answers.
        """
        gaps = []

        # Check basic organizational measures
        # Assuming 'security_responsible' is a question ID
        if answers.get("security_responsible") is False:
            gaps.append(Gap(
                measure_id="org_security_responsible",
                type=MeasureType.ORG,
                criticality=CriticalityLevel.HIGH,
                description="Отсутствует ответственный за ИБ",
                recommendation="Назначить ответственного сотрудника или подразделение за обеспечение ИБ."
            ))

        # Check technical measures
        # Assuming 'antivirus' is a question ID (we haven't added it to the bank yet, but let's assume)
        if answers.get("antivirus") is False:
            gaps.append(Gap(
                measure_id="tech_antivirus",
                type=MeasureType.TECH,
                criticality=CriticalityLevel.MEDIUM,
                description="Отсутствует антивирусная защита",
                recommendation="Внедрить средства антивирусной защиты на всех узлах."
            ))
            
        # Check system specific gaps
        for system in profile.systems:
            if system.is_critical and not system.gaps:
                # If system is critical but has no specific gaps recorded yet (maybe from manual entry),
                # we might add a generic gap if we had per-system answers.
                # For now, the answers are global or mixed. 
                # In a real app, we'd map answers to systems.
                pass

        return gaps
