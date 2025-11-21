from kii_readiness_mapper.questionnaire.scoring import ScoringEngine
from kii_readiness_mapper.questionnaire.model import Questionnaire, Section, Question, QuestionType, AnswerOption

def test_scoring_basic():
    q = Question(
        id="q1", text="Q1", type=QuestionType.YES_NO, weight=10.0,
        options=[
            AnswerOption(id="yes", label="Yes", value=True),
            AnswerOption(id="no", label="No", value=False)
        ]
    )
    section = Section(id="s1", title="S1", questions=[q])
    questionnaire = Questionnaire(sections=[section])
    
    engine = ScoringEngine()
    
    # Test positive answer
    scores = engine.calculate_scores(questionnaire, {"q1": True})
    assert scores["overall_readiness"] == 100.0
    
    # Test negative answer
    scores = engine.calculate_scores(questionnaire, {"q1": False})
    assert scores["overall_readiness"] == 0.0
