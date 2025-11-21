import typer
import json
from pathlib import Path
from ...domain.models import KiiReadinessResult
from ...report.markdown_report import MarkdownReportGenerator
from ...report.html_report import HtmlReportGenerator
from ...config.loader import ConfigLoader

def generate_report(
    result: Path = typer.Option(..., help="Path to result JSON"),
    profile: Path = typer.Option(..., help="Path to profile YAML (for context)"),
    format: str = typer.Option("markdown", help="Output format: markdown or html"),
    output: Path = typer.Option(..., help="Output report file")
):
    """
    Generate a human-readable report from assessment result.
    """
    # Load result
    with open(result, "r", encoding="utf-8") as f:
        result_data = json.load(f)
        readiness_result = KiiReadinessResult.model_validate(result_data)
        
    # Load profile
    org_profile = ConfigLoader.load_profile(profile)
    
    report_content = ""
    if format == "markdown":
        generator = MarkdownReportGenerator()
        report_content = generator.generate(readiness_result, org_profile)
    elif format == "html":
        generator = HtmlReportGenerator()
        report_content = generator.generate(readiness_result, org_profile)
    else:
        typer.echo(f"Unknown format: {format}")
        raise typer.Exit(code=1)
        
    with open(output, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    typer.echo(f"Report generated at {output}")
