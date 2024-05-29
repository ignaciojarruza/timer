import pandas as pd

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
