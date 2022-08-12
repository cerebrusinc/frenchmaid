
import typer

from typing import Optional
from frenchmaid import __app_name__, __version__

from .switches import cleanSwitch as clS, ignoreSwitch as igS

app = typer.Typer(help="A handy tool to delete all junk!", no_args_is_help=True)

ignoreSwitch = igS.IgnoreSwitch()
cleanSwitch = clS.CleanSwitch()

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
        help="View the CLI app version",
        callback=_version_callback,
        is_eager=True
    )
) -> None: return

@app.command(help="Delete all instances of junk folders")
def clean(folder: Optional[str] = typer.Argument(None, help="pycache, mypy")) -> None:
    if (folder):
        cleanSwitch.indirect(folder)
    else:
        cleanSwitch.indirect("all")
    raise typer.Exit()

@app.command(help="Add junk folders to ignore files", no_args_is_help=True)
def ignore(platform: Optional[str] = typer.Argument(..., help="git, docker")) -> None:
    ignoreSwitch.indirect(platform)
    raise typer.Exit()