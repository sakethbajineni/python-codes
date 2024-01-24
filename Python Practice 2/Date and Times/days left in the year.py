from datetime import datetime,timedelta
date_string=input()
date_obj_conversion=datetime.strptime(date_string,"%d/%m/%Y")
year_end_date=datetime(year=date_obj_conversion.year,month=12,day=31)
duration=year_end_date-date_obj_conversion
print(duration)