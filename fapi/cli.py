import typer
from fapi.commands.create import create_app
from fapi.commands.add import add
from fapi.commands.run import run_app

app = typer.Typer(help="FastAPI CLI Tool")
app.add_typer(create_app)
app.add_typer(add, name='add')
app.add_typer(run_app)

if __name__ == "__main__":
    app()
