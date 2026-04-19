import typer
from fapi.utils.utils import render_template, req_installer, create_venv, scaffold_project, generate_env
from pathlib import Path
create_app = typer.Typer(help="FastAPI project generator")


@create_app.command()
def create(
    project_name: str = typer.Argument(...),
    db: str = typer.Option(
        None, "--db", help="Database: sqlite, postgres, or mongodb", case_sensitive=False
    ),
    routes: bool = typer.Option(
        None, "--routes", help="Generate routes?"
    ),
    is_async: bool = typer.Option(
        False, "--is-async", help="Use asynchronous database drivers (e.g. Async SQLAlchemy or Motor)"
    ),
    redis: bool = typer.Option(
        False, "--redis", help="Include Redis integration for caching"
    ),
    auth: str = typer.Option(
        None, "--auth", help="Auth system: jwt", case_sensitive=False
    ),
    websockets: bool = typer.Option(
        False, "--websockets", help="Include WebSocket boilerplates"
    ),
    tasks: str = typer.Option(
        None, "--tasks", help="Background tasks: celery or arq", case_sensitive=False
    ),
    mail: bool = typer.Option(
        False, "--mail", help="Include Mail Service integration"
    ),
):
    """Create a new FastAPI project"""
    project_dir = Path(project_name)

    if project_dir.exists():
        typer.echo(f"Directory {project_name} already exists!")
        raise typer.Exit()

    typer.echo(f"Creating FastAPI project: {project_name}... ✅")
    if db is None:
        use_db = typer.confirm("do you want to use a db?")
        db_choice = typer.prompt("Choose a Database (sqlite/postgres/mongodb)", default="sqlite") if use_db else None
    else:
        use_db = db.lower() in ["postgres", "sqlite", "mongodb"]
        db_choice = db.lower()
        if not use_db: 
            typer.echo(f"Invalid DB option! {db} neither 'sqlite', 'postgres', nor 'mongodb'")
            raise typer.Exit() 

    if routes is None:
        use_routes = typer.confirm("do you want to generate routes?")
    else:
        use_routes = routes

    context = {
        "project_name": project_name,
        "use_db": use_db,
        "db_choice": db_choice,
        "use_routes": use_routes,
        "is_async": is_async,
        "redis": redis,
        "auth": auth,
        "websockets": websockets,
        "tasks": tasks,
        "mail": mail,
    }

    scaffold_project(project_dir, context)
    generate_env(project_dir, context)
    
    create_venv(project_dir)
    req_installer(project_dir)
    (project_dir / ".fastapi").write_text("fastapi-project")


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
