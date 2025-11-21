
from typing import Dict, Any
from ..domain.models import KiiReadinessResult, OrganizationProfile
from ..domain.enums import KiiCategory
from .kii_subject_detector import KiiSubjectDetector
from .kii_category_estimator import KiiCategoryEstimator
from .controls_checker import ControlsChecker
from .gaps_prioritizer import GapsPrioritizer
from ..questionnaire.scoring import ScoringEngine
from ..questionnaire.model import Questionnaire

class SummaryBuilder:
    def __init__(self):
        self.subject_detector = KiiSubjectDetector()
        self.category_estimator = KiiCategoryEstimator()
        self.controls_checker = ControlsChecker()
        self.gaps_prioritizer = GapsPrioritizer()
        self.scoring_engine = ScoringEngine()

    def build(self, profile: OrganizationProfile, answers: Dict[str, Any], questionnaire: Questionnaire) -> KiiReadinessResult:
        # 1. Detect Subject
        subject_info = self.subject_detector.detect(profile)
        
        # 2. Estimate Category (max of all systems)
        max_category = KiiCategory.NONE
        # Logic to compare categories (1 > 2 > 3 > NONE)
        # Simplified: just take the "highest" found
        cat_priority = {
            KiiCategory.CAT_1: 3,
            KiiCategory.CAT_2: 2,
            KiiCategory.CAT_3: 1,
            KiiCategory.NONE: 0,
            KiiCategory.UNKNOWN: -1
        }
        
        for system in profile.systems:
            cat = self.category_estimator.estimate(system)
            system.estimated_category = cat
            if cat_priority.get(cat, -1) > cat_priority.get(max_category, -1):
                max_category = cat

        # 3. Check Controls & Gaps
        gaps = self.controls_checker.check(profile, answers)
        prioritized_gaps = self.gaps_prioritizer.prioritize(gaps)
        
        # 4. Calculate Scores
        scores = self.scoring_engine.calculate_scores(questionnaire, answers)
        
        # 5. Build Summary Text
        summary_text = f"Организация: {profile.name}\n"
        summary_text += f"Потенциальный субъект КИИ: {'Да' if subject_info['is_potential_subject'] else 'Нет'} ({subject_info['confidence']})\n"
        summary_text += f"Вероятная максимальная категория: {max_category.value}\n"
        summary_text += f"Найдено несоответствий: {len(gaps)}\n"

        return KiiReadinessResult(
            potential_kii_subject=subject_info['is_potential_subject'],
            subject_confidence=subject_info['confidence'],
            estimated_category=max_category,
            subject_score=scores.get("subject_probability", 0.0),
            criticality_score=scores.get("overall_readiness", 0.0), # Using readiness as proxy for now
            org_controls_score=scores.get("overall_readiness", 0.0), # TODO: Split scores
            tech_controls_score=scores.get("overall_readiness", 0.0), # TODO: Split scores
            summary_text=summary_text,
            key_risks=[g.description for g in prioritized_gaps[:5]] # Top 5 risks
        )
