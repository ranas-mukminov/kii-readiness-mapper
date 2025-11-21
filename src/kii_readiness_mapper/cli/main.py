import typer
from .commands import init_profile, run_cli_survey, assess_profile, generate_report, run_web_survey

app = typer.Typer(help="KII Readiness Mapper CLI")

app.command(name="init-profile")(init_profile.init_profile)
app.command(name="run-cli-survey")(run_cli_survey.run_cli_survey)
app.command(name="assess-profile")(assess_profile.assess_profile)
app.command(name="generate-report")(generate_report.generate_report)
app.command(name="run-web-survey")(run_web_survey.run_web_survey)

if __name__ == "__main__":
    app()
