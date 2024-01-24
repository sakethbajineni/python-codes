from datetime import datetime
date_string=input()
date_string_to_date_obj=datetime.strptime(date_string,"%d %b %Y")
weekdayss=date_string_to_date_obj.strftime("%A")
print(weekdayss)
