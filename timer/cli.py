"""This module provides the TimeLog CLI."""
# timer/cli.py

from pathlib import Path
from typing import Optional

import typer

from timer import (
    __app_name__, __version__, ERRORS, config, database, timer
)

app = typer.Typer()

@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="Provide a database file path if available. The default log.cvs database will be initialized if no database exists. Do NOT run if db exists, this will override existing db."
    ),
) -> None:
    """Initialize the timer database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f'The timer database is {db_path}', fg=typer.colors.GREEN)

def get_logger() -> timer.Logger:
    if config.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please run "timer init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    
    if db_path.exists():
        return timer.Logger(db_path)
    else:
        typer.secho(
            'Database not found. Please, run "timer init"',
            fg=typer.colors.RED
        )
        raise typer.Exit(1)
    
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
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return