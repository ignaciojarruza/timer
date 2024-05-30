"""This module provides the Timer Database functionality."""
# timer/database.py

import configparser
import csv
from pathlib import Path
import pandas as pd
from typing import NamedTuple

from timer import DB_READ_ERROR, DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    Path.home().stem + "_log.csv"
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

class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
    
    def get_logs(self) -> int:
        try:
            logs = pd.read_csv(self._db_path)
            return SUCCESS
        except OSError:
            return DB_READ_ERROR
    
    def add_log(self, start_time, end_time, tag) -> int:
        try:
            with open(self._db_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([start_time, end_time, tag])
                return SUCCESS
        except OSError:
            return DB_WRITE_ERROR
        