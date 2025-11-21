import pytest
from pathlib import Path
from kii_readiness_mapper.config.loader import ConfigLoader
from kii_readiness_mapper.questionnaire.loader import QuestionnaireLoader
from kii_readiness_mapper.assessment.summary_builder import SummaryBuilder
from kii_readiness_mapper.report.markdown_report import MarkdownReportGenerator

def test_full_flow_clinic(tmp_path):
    # 1. Load profile (mocking text parser result by creating file directly)
    profile_content = """
    name: "Clinic"
    sector: "health"
    systems:
      - id: "mis"
        name: "MIS"
        type: "is"
        is_critical: true
        users_count: 5000
    """
    profile_path = tmp_path / "clinic.yaml"
    profile_path.write_text(profile_content, encoding="utf-8")
    profile = ConfigLoader.load_profile(profile_path)
    
    # 2. Load questionnaire
    # We need real banks or mocks. Let's use real banks if available or mock.
    # Since we are in integration test, we assume the package structure is intact.
    # But we need to point to the source banks.
    banks_dir = Path(__file__).parent.parent.parent / "src" / "kii_readiness_mapper" / "questionnaire" / "banks"
    if not banks_dir.exists():
        pytest.skip("Banks directory not found, skipping integration test")
        
    loader = QuestionnaireLoader(banks_dir)
    questionnaire = loader.load_questionnaire(profile.sector)
    
    # 3. Simulate answers
    answers = {
        "sector": "health",
        "service_impact": True,
        "security_responsible": True,
        "egisz_integration": True
    }
    
    # 4. Assess
    builder = SummaryBuilder()
    result = builder.build(profile, answers, questionnaire)
    
    assert result.potential_kii_subject is True
    assert result.subject_confidence == "high"
    
    # 5. Generate Report
    generator = MarkdownReportGenerator()
    report = generator.generate(result, profile)
    
    assert "Отчёт о готовности к КИИ: Clinic" in report
    assert "Потенциальный субъект КИИ**: Да" in report
