
import typer, os

from typing import Optional
from frenchmaid import __app_name__, __version__, delcache

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="View the CLI version and stuff... maybe",
        callback=_version_callback,
        is_eager=True
    )
) -> None: return

@app.command()
def clean():
    dirdir = os.getcwd()
    delcache.pyCacheOnly(dirdir)
    raise typer.Exit()