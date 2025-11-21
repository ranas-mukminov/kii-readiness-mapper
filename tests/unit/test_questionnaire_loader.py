from kii_readiness_mapper.questionnaire.loader import QuestionnaireLoader
from kii_readiness_mapper.domain.enums import Sector

def test_load_questionnaire(tmp_path):
    # Create dummy banks
    banks_dir = tmp_path / "banks"
    banks_dir.mkdir()
    
    (banks_dir / "common.yaml").write_text("""
    sections:
      - id: "common"
        title: "Common"
        questions: []
    """, encoding="utf-8")
    
    (banks_dir / "sector_health.yaml").write_text("""
    sections:
      - id: "health"
        title: "Health"
        questions: []
    """, encoding="utf-8")
    
    loader = QuestionnaireLoader(banks_dir)
    
    # Load common only
    q_common = loader.load_questionnaire(sector=None)
    assert len(q_common.sections) == 1
    assert q_common.sections[0].id == "common"
    
    # Load health
    q_health = loader.load_questionnaire(sector=Sector.HEALTH)
    assert len(q_health.sections) == 2
    ids = [s.id for s in q_health.sections]
    assert "common" in ids
    assert "health" in ids
