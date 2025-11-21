from kii_readiness_mapper.report.markdown_report import MarkdownReportGenerator
from kii_readiness_mapper.domain.models import KiiReadinessResult, OrganizationProfile, KiiCategory
from kii_readiness_mapper.domain.enums import Sector

def test_generate_markdown():
    generator = MarkdownReportGenerator()
    profile = OrganizationProfile(name="Test Org", sector=Sector.HEALTH)
    result = KiiReadinessResult(
        potential_kii_subject=True,
        subject_confidence="high",
        estimated_category=KiiCategory.CAT_3,
        summary_text="Summary",
        key_risks=["Risk 1"]
    )
    
    report = generator.generate(result, profile)
    assert "# Отчёт о готовности к КИИ: Test Org" in report
    assert "Потенциальный субъект КИИ**: Да" in report
    assert "Risk 1" in report
