import typer
from typing import Dict, Any
from ..questionnaire.model import Questionnaire, QuestionType

class CliSurvey:
    def run(self, questionnaire: Questionnaire) -> Dict[str, Any]:
        """
        Run an interactive CLI survey based on the questionnaire.
        """
        answers = {}
        
        typer.echo("=== АНКЕТА KII-READINESS ===")
        
        for section in questionnaire.sections:
            typer.echo(f"\n--- {section.title} ---")
            if section.description:
                typer.echo(section.description)
                
            for question in section.questions:
                typer.echo(f"\n{question.text}")
                if question.help_text:
                    typer.echo(f"(Подсказка: {question.help_text})")
                
                answer = None
                
                if question.type == QuestionType.YES_NO:
                    answer = typer.confirm("Ваш ответ?")
                
                elif question.type == QuestionType.SINGLE_CHOICE:
                    if question.options:
                        for i, opt in enumerate(question.options):
                            typer.echo(f"{i+1}. {opt.label}")
                        
                        choice = typer.prompt("Выберите вариант (номер)", type=int)
                        # Validate choice
                        if 1 <= choice <= len(question.options):
                            answer = question.options[choice-1].value
                        else:
                            typer.echo("Неверный выбор, пропускаем.")
                
                elif question.type == QuestionType.FREE_TEXT:
                    answer = typer.prompt("Ваш ответ")
                
                # Store answer
                if answer is not None:
                    answers[question.id] = answer
                    
        return answers
