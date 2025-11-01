import typer
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import shutil
import subprocess

app = typer.Typer(help="FastAPI project generator")

TEMPLATES_DIR = Path(__file__).parent / "templates"

def create_venv(project_dir: Path):
    typer.echo("🛠 Creating virtual environment...")
    subprocess.run(["python3", "-m", "venv", ".venv"], cwd=project_dir)


def req_installer(project_dir: Path):
    req_file = project_dir / "requirements.txt"
    pip_path = project_dir / ".venv" / "bin" / "pip"

    typer.echo("📦 Installing dependencies...")
    subprocess.run([str(pip_path), "install", "-r", str(req_file)])

def render_template(src, dest, context):
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template(src)
    rendered = template.render(**context)

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(rendered)


@app.command()
def create(project_name: str):
    """Create a new FastAPI project"""
    project_dir = Path(project_name)

    if project_dir.exists():
        typer.echo(f"Directory {project_name} already exists!")
        raise typer.Exit()

    typer.echo(f"Creating FastAPI project: {project_name}... ✅")

    context = {"project_name": project_name}

    # Create folders
    (project_dir / "app").mkdir(parents=True, exist_ok=True)

    # Render templates
    render_template("app/main.py.j2", project_dir / "app/main.py", context)
    render_template("requirements.txt.j2", project_dir / "requirements.txt", context)

    # Create .env example
    (project_dir / ".env").write_text("APP_NAME=" + project_name)
    create_venv(project_dir)
    req_installer(project_dir)

    typer.echo("✅ Project created successfully!")
    typer.echo(f"Next steps 👉 \n")
    typer.echo(f"cd {project_name}")
    typer.echo("""activate venv: 
               linux / mac: source .venv/bin/activate
                Windows (PowerShell):
                .venv\\Scripts\\Activate.ps1

                Windows (CMD):
                .venv\\Scripts\\activate.bat
               """)
    typer.echo(f"uvicorn app.main:app --reload")


if __name__ == "__main__":
    app()
