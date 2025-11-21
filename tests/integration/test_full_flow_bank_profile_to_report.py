import pytest
from pathlib import Path
from kii_readiness_mapper.config.loader import ConfigLoader
from kii_readiness_mapper.questionnaire.loader import QuestionnaireLoader
from kii_readiness_mapper.assessment.summary_builder import SummaryBuilder

def test_full_flow_bank(tmp_path):
    # 1. Load profile
    profile_content = """
    name: "Bank"
    sector: "finance"
    systems:
      - id: "cbs"
        name: "Core Banking"
        type: "is"
        is_critical: true
        users_count: 1000000
    """
    profile_path = tmp_path / "bank.yaml"
    profile_path.write_text(profile_content, encoding="utf-8")
    profile = ConfigLoader.load_profile(profile_path)
    
    # 2. Load questionnaire
    banks_dir = Path(__file__).parent.parent.parent / "src" / "kii_readiness_mapper" / "questionnaire" / "banks"
    if not banks_dir.exists():
        pytest.skip("Banks directory not found, skipping integration test")
        
    loader = QuestionnaireLoader(banks_dir)
    questionnaire = loader.load_questionnaire(profile.sector)
    
    # 3. Simulate answers (partial)
    answers = {
        "sector": "finance",
        "service_impact": True
    }
    
    # 4. Assess
    builder = SummaryBuilder()
    result = builder.build(profile, answers, questionnaire)
    
    assert result.potential_kii_subject is True
    # Should detect CAT_1 due to user count > 100k
    assert result.estimated_category.value == "1"
