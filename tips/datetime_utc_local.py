from datetime import datetime, timezone, timedelta
import time
# Current timestamp
start = time.time()

# UTC time
utc_time = datetime.fromtimestamp(start, tz=timezone.utc)

# Nepal time (UTC+5:45)
nepal_offset = timedelta(hours=5, minutes=45)
nepal_time = utc_time.astimezone(timezone(nepal_offset))

# Format both times
print("UTC Time   :", utc_time.strftime('%Y-%m-%d %H:%M:%S'))
print("Nepal Time :", nepal_time.strftime('%Y-%m-%d %H:%M:%S'))