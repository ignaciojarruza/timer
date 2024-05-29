import pandas as pd
import datetime as dt

# Load logs
file_path = 'log.csv'
logs = pd.read_csv(file_path)

# Pandas data calculations
logs['start_time'] = pd.to_datetime(logs['start_time'])
logs['end_time'] = pd.to_datetime(logs['end_time'])
logs['duration'] = (logs['end_time'] - logs['start_time']).dt.total_seconds()

# Total stats 
total_times = logs.groupby('tag')['duration'].sum()
print("Stats:")
for tag, total_seconds in total_times.items():
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    print(f"    {tag}: {int(hours)}h {int(minutes)}m")

# For current week stats
current_date = dt.datetime.now()
start_of_week = current_date - dt.timedelta(days = current_date.weekday())
current_week = logs[logs['start_time'] >= start_of_week]
total_times_current_week = current_week.groupby('tag')['duration'].sum()

# Print Weekly Stats
print("Weekly Stats:")
for tag, total_seconds in total_times_current_week.items():
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    print(f"    {tag}: {int(hours)}h {int(minutes)}m")