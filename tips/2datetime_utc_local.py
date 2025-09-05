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


"""

or you can just add the offset time of utc + 5:45
5 hours 45 minutes to second like 5 * 60 * 60 + 45 * 60 seconds 

to the utc_time = time.time() as default is utc
utc_time + offset time

and convert into date
date_in_local = datetime.fromtimestamp(utctime+offset, tz=timezone.utc)

"""

nepal_offset = 5 * 60 * 60 + 45 * 60

time_now = time.time() # since it is in utc we can add our offset to get the current time and date in nepal 

add = time_now + nepal_offset
nepal_time2 = datetime.fromtimestamp(add, tz=timezone.utc)


print("Time 2:", nepal_time2.strftime('%Y-%m-%d %H:%M:%S'))
