import time
from datetime import datetime, timedelta

def countdown_by_day(target_date_str):
    
    target_date = datetime.strptime(target_date_str, '%Y-%m-%d %H:%M:%S')

    while True:
        time_left = target_date - datetime.now()

        if time_left.total_seconds() <= 0:
            print("\nCountdown complete! Time completed!")
            break

        days = time_left.days
        hours, rem = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        timer = "{:02d} days, {:02d}:{:02d}:{:02d}".format(days, hrs, mins, secs)
        print(timer, end='\r')

        time.sleep(1)
