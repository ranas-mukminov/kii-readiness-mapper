import typer
import yaml
from pathlib import Path
from ...domain.models import OrganizationProfile
from ...domain.enums import Sector

def init_profile(output: Path = typer.Option(..., help="Output YAML file path")):
    """
    Initialize a new organization profile template.
    """
    profile = OrganizationProfile(
        name="My Organization",
        sector=Sector.OTHER,
        systems=[]
    )
    
    # Convert to dict and dump to YAML
    data = profile.model_dump(mode="json", exclude_none=True)
    
    with open(output, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
        
    typer.echo(f"Profile template created at {output}")
