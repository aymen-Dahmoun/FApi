import typer
from commands.create import create_app
from commands.add import add

app = typer.Typer(help="FastAPI CLI Tool")
app.add_typer(create_app)
app.add_typer(add, name='add')

if __name__ == "__main__":
    app()
