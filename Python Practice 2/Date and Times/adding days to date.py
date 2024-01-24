# time delta
# Adding days to the time delta

from datetime import timedelta, datetime
delta=timedelta(days=365,hours=4)
print(delta)
date_obj=datetime.now()
next_year_datetime=delta+date_obj
print(next_year_datetime)