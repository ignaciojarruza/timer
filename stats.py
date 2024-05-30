import pandas as pd
import datetime as dt

def printStats(times, text):
    """
    Print out stats for log of times.

    Parameters:
    times (pd series) :   A list of log entries containing start_time,
        end_time and tag.
    text (string)     :   Title text to precede stat printout.

    Raises:
    ValueError: If the pd series is empty
    """
    if not times:
        raise ValueError("Log entries cannot be empty.")
    
    print(text)
    for tag, total_seconds in times.items():
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        print(f"    {tag}: {int(hours)}h {int(minutes)}m")

# Load logs
file_path = 'log.csv'
logs = pd.read_csv(file_path)

# Pandas data calculations
logs['start_time'] = pd.to_datetime(logs['start_time'])
logs['end_time'] = pd.to_datetime(logs['end_time'])
logs['duration'] = (logs['end_time'] - logs['start_time']).dt.total_seconds()

# Total stats 
total_times = logs.groupby('tag')['duration'].sum()
printStats(total_times, "Stats")

# For current week stats
current_date = dt.datetime.now()
start_of_week = current_date - dt.timedelta(days = current_date.weekday())
current_week = logs[logs['start_time'] >= start_of_week]
total_times_current_week = current_week.groupby('tag')['duration'].sum()

# Print Weekly Stats
printStats(total_times_current_week, "Weekly Stats:")