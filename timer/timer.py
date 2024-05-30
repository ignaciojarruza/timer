from pathlib import Path
import select
import time
import sys
from time import strftime, localtime
import csv
from datetime import datetime
from timer.database import DatabaseHandler

class Logger:
    def _init_(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)

    def log_event(self, start_time, end_time, tag) -> int:
        return self._db_handler.add_log(start_time, end_time, tag)

def main():
    tag = input("Enter tag for activity.")
    print("Press any button to stop the timer.")
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
        sys.stdout.write("\rElapsed Time: {}".format(time_str))
        sys.stdout.flush()
        time.sleep(1)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = input()
            break
    start = strftime('%Y-%m-%d %H:%M:%S', localtime(start_time))
    end = strftime('%Y-%m-%d %H:%M:%S', localtime(time.time()))

    #log_event(start, end, tag)

    print("start_time: {} | end_time: {}".format(start, end))
    print("\nElapsed Time: {} hours {} minutes {} seconds".format(int(hours), int(minutes), int(seconds)))