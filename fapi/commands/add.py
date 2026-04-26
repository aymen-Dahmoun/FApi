import typer
from pathlib import Path
from fapi.utils.utils import render_template, ensure_fastapi_project

add = typer.Typer(help="Adds entities like models, schemas, routes...")


def _read_env(project_path: Path) -> dict:
    env = {}
    env_path = project_path / ".env"
    if not env_path.exists():
        return env

    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")

    return env


def _project_context(project_path: Path, name: str) -> dict:
    env = _read_env(project_path)
    db_url = env.get("DATABASE_URL", "")

    use_db = bool(db_url)
    db_choice = None
    is_async = False

    if db_url.startswith("mongodb"):
        db_choice = "mongodb"
        is_async = True
    elif db_url.startswith("postgresql+asyncpg"):
        db_choice = "postgres"
        is_async = True
    elif db_url.startswith("postgresql"):
        db_choice = "postgres"
    elif db_url.startswith("sqlite+aiosqlite"):
        db_choice = "sqlite"
        is_async = True
    elif db_url.startswith("sqlite"):
        db_choice = "sqlite"

    return {
        "name": name.lower(),
        "class_name": name.capitalize(),
        "use_db": use_db,
        "db_choice": db_choice,
        "is_async": is_async,
    }




@add.command()
def route(name: str):
    """Create a new route file"""
    ensure_fastapi_project()
    if not name:
        typer.echo("You must provide a name for the route")
        raise typer.Exit()

    project_path = Path(".")
    context = _project_context(project_path, name)

    routes_dir = project_path / "app/api/routes"
    routes_dir.mkdir(parents=True, exist_ok=True)

    render_template("app/api/routes/route.py.j2", routes_dir / f"{name.lower()}.py", context)

    typer.echo(f"✅ Route `{name}` created successfully!")


@add.command()
def model(
    name: str,
    schema: bool = typer.Option(False, "--schema", help="Add a schema file"),
    crud: bool = typer.Option(False, "--crud", help="Add a CRUD file")
):
    ensure_fastapi_project()
    if not name:
        typer.echo("You must provide a name for the model")
        raise typer.Exit()

    project_path = Path(".")
    context = _project_context(project_path, name)

    models_dir = project_path / "app/models"
    models_dir.mkdir(parents=True, exist_ok=True)

    render_template("app/models/model.py.j2", models_dir / f"{name.lower()}.py", context)

    if schema:
        schemas_dir = project_path / "app/schemas"
        schemas_dir.mkdir(parents=True, exist_ok=True)

        render_template("app/schemas/schema.py.j2", schemas_dir / f"{name.lower()}.py", context)
        typer.echo(f"📦 Schema `{name}` created")

    if crud:
        crud_dir = project_path / "app/crud"
        crud_dir.mkdir(parents=True, exist_ok=True)

        render_template("app/crud/crud.py.j2", crud_dir / f"{name.lower()}.py", context)
        typer.echo(f"🛠️ CRUD `{name}` created")

    typer.echo(f"✅ Model `{name}` created successfully!")


@add.command()
def service(name: str):
    """Create a new service file"""
    ensure_fastapi_project()

    if not name:
        typer.echo("You must provide a name for the service")
        raise typer.Exit()

    project_path = Path(".")
    context = _project_context(project_path, name)

    routes_dir = project_path / "app/services"
    routes_dir.mkdir(parents=True, exist_ok=True)

    render_template("app/services/service.py.j2", routes_dir / f"{name.lower()}.py", context)

    typer.echo(f"✅ service `{name}` created successfully!")



@add.command()
def crud(name: str):
    """Create a new crud file"""

    ensure_fastapi_project()

    if not name:
        typer.echo("You must provide a name for the service")
        raise typer.Exit()

    project_path = Path(".")
    context = _project_context(project_path, name)

    routes_dir = project_path / "app/crud"
    routes_dir.mkdir(parents=True, exist_ok=True)

    render_template("app/crud/crud.py.j2", routes_dir / f"{name.lower()}.py", context)

    typer.echo(f"✅ crud `{name}` created successfully!")

@add.command()
def schema(name: str):
    """Create a new schema file"""
    
    ensure_fastapi_project()

    if not name:
        typer.echo("You must provide a name for the service")
        raise typer.Exit()

    project_path = Path(".")
    context = _project_context(project_path, name)

    routes_dir = project_path / "app/schemas"
    routes_dir.mkdir(parents=True, exist_ok=True)

    render_template("app/schemas/schema.py.j2", routes_dir / f"{name.lower()}.py", context)

    typer.echo(f"✅ schema `{name}` created successfully!")
