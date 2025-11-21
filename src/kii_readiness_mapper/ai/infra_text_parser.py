from .base import AIProvider
from ..domain.models import OrganizationProfile
from ..domain.enums import Sector

class InfraTextParser:
    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider

    def parse(self, text: str) -> OrganizationProfile:
        """
        Parse infrastructure description text into a profile.
        Currently a stub that returns a generic profile.
        """
        # In a real implementation, we would use self.ai_provider.chat() to extract JSON
        
        return OrganizationProfile(
            name="Parsed Organization",
            sector=Sector.OTHER,
            systems=[]
        )
