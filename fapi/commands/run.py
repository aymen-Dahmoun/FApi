import typer
import subprocess
from pathlib import Path
from fapi.utils.utils import ensure_fastapi_project

run_app = typer.Typer(help="Run the FastAPI project")

@run_app.command("run")
def run():
    """Automatically detect the entry point and run the project using uvicorn with hot reload."""
    ensure_fastapi_project()
    typer.echo("Starting Uvicorn with hot reload...")
    
    venv_uvicorn = Path(".venv/bin/uvicorn")
    venv_python = Path(".venv/bin/python")
    
    if venv_uvicorn.exists():
        cmd = [str(venv_uvicorn), "app.main:app", "--reload"]
    elif venv_python.exists():
        cmd = [str(venv_python), "-m", "uvicorn", "app.main:app", "--reload"]
    else:
        cmd = ["uvicorn", "app.main:app", "--reload"]

    try:
        subprocess.run(cmd)
    except FileNotFoundError:
        typer.echo("❌ uvicorn not found. Please activate your virtual environment or install dependencies.")
        raise typer.Exit(1)
