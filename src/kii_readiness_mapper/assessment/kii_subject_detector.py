from ..domain.models import OrganizationProfile
from ..domain.enums import Sector

class KiiSubjectDetector:
    def detect(self, profile: OrganizationProfile) -> dict:
        """
        Determine if the organization is a potential CII subject.
        Returns a dict with 'is_potential_subject' (bool) and 'confidence' (str).
        """
        is_potential = False
        confidence = "low"
        reasons = []

        # Check sector
        if profile.sector in [
            Sector.HEALTH, Sector.TRANSPORT, Sector.ENERGY, Sector.FINANCE,
            Sector.SCIENCE, Sector.TELECOM, Sector.FUEL, Sector.ATOMIC,
            Sector.DEFENSE, Sector.ROCKET, Sector.MINING, Sector.METAL,
            Sector.CHEMICAL
        ]:
            is_potential = True
            confidence = "high"
            reasons.append(f"Отрасль '{profile.sector.value}' входит в перечень сфер КИИ (187-ФЗ).")

        # Check critical systems
        critical_systems_count = sum(1 for s in profile.systems if s.is_critical)
        if critical_systems_count > 0:
            is_potential = True
            if confidence == "low":
                confidence = "medium"
            reasons.append(f"Найдено {critical_systems_count} систем(ы), отмеченных как критичные.")

        return {
            "is_potential_subject": is_potential,
            "confidence": confidence,
            "reasons": reasons
        }
