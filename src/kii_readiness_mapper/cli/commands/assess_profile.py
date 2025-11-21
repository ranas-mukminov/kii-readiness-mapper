import typer
import yaml
from pathlib import Path
from ...config.loader import ConfigLoader
from ...assessment.summary_builder import SummaryBuilder
from ...questionnaire.loader import QuestionnaireLoader

def assess_profile(
    profile: Path = typer.Option(..., help="Path to profile YAML"),
    answers: Path = typer.Option(..., help="Path to answers YAML"),
    out: Path = typer.Option(..., help="Output result JSON file")
):
    """
    Assess readiness based on profile and answers.
    """
    # Load profile
    org_profile = ConfigLoader.load_profile(profile)
    
    # Load answers
    with open(answers, "r", encoding="utf-8") as f:
        answers_data = yaml.safe_load(f)
        
    # Load questionnaire (we need it for scoring weights)
    # For simplicity, we reload it based on profile sector. 
    # Ideally we should know which questionnaire was used.
    banks_dir = Path(__file__).parent.parent.parent / "questionnaire" / "banks"
    loader = QuestionnaireLoader(banks_dir)
    questionnaire = loader.load_questionnaire(org_profile.sector)
    
    # Build summary
    builder = SummaryBuilder()
    result = builder.build(org_profile, answers_data, questionnaire)
    
    # Save result
    with open(out, "w", encoding="utf-8") as f:
        f.write(result.model_dump_json(indent=2))
        
    typer.echo(f"Assessment result saved to {out}")
