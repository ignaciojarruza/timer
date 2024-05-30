"""This module provides the Timer Database functionality."""
# timer/database.py

import configparser
import csv
from pathlib import Path

from timer import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "log.csv"
)

def get_database_path(config_file: Path) -> Path:
    """Return the current path to the timer database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    """Create the timer database."""
    try:
        header = ["start_time", "end_time", "tag"]
        with db_path.open(mode='w', newline='') as database:
            writer = csv.writer(database)
            writer.writerow(header)
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR