from typing import Dict, Any
from .model import Questionnaire

class ScoringEngine:
    def calculate_scores(self, questionnaire: Questionnaire, answers: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate scores based on answers.
        Returns a dictionary with score names and values (0-100).
        """
        total_weight = 0.0
        earned_score = 0.0
        
        # Simple scoring logic for now
        for section in questionnaire.sections:
            for question in section.questions:
                answer_value = answers.get(question.id)
                if answer_value is None:
                    continue
                
                # Find the selected option to get its weight/value
                if question.options:
                    for option in question.options:
                        # Handle boolean/string comparison carefully
                        if str(option.value) == str(answer_value):
                            # For yes/no or choice, we might use option.weight or just count it
                            # Let's assume option.value is the score contribution for now if it's numeric,
                            # or we use the question weight if the answer is "positive".
                            
                            # Simplified: if option.id == 'yes' or 'health' etc, we add question weight
                            # This is a stub logic. Real logic would be more complex.
                            if option.id in ["yes", "health", "transport", "energy", "finance"]:
                                earned_score += question.weight
                            break
                
                total_weight += question.weight

        # Normalize to 0-100
        final_score = 0.0
        if total_weight > 0:
            final_score = (earned_score / total_weight) * 100.0
            
        return {
            "overall_readiness": final_score,
            "subject_probability": final_score # Stub
        }
