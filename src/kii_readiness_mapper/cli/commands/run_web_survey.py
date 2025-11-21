import typer
from ...survey.web_survey import run_server

def run_web_survey(
    host: str = typer.Option("127.0.0.1", help="Host to bind"),
    port: int = typer.Option(8000, help="Port to bind")
):
    """
    Start the Web Survey server.
    """
    typer.echo(f"Starting web survey at http://{host}:{port}")
    run_server(host, port)
