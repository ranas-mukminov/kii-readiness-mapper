import typer
import yaml
from pathlib import Path
from ...questionnaire.loader import QuestionnaireLoader
from ...survey.cli_survey import CliSurvey
from ...domain.enums import Sector, SystemType

def run_cli_survey(
    sector: Sector = typer.Option(..., help="Organization sector"),
    system_type: SystemType = typer.Option(SystemType.IS, help="System type"),
    output: Path = typer.Option(..., help="Output answers YAML file")
):
    """
    Run an interactive CLI survey.
    """
    # Locate banks dir relative to this file
    # src/kii_readiness_mapper/cli/commands/run_cli_survey.py -> .../questionnaire/banks
    banks_dir = Path(__file__).parent.parent.parent / "questionnaire" / "banks"
    
    loader = QuestionnaireLoader(banks_dir)
    questionnaire = loader.load_questionnaire(sector, system_type)
    
    survey = CliSurvey()
    answers = survey.run(questionnaire)
    
    with open(output, "w", encoding="utf-8") as f:
        yaml.dump(answers, f, allow_unicode=True, sort_keys=False)
        
    typer.echo(f"Answers saved to {output}")
