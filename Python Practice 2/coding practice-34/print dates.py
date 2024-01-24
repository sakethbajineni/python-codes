from datetime import datetime
date_string=input()
date_string_to_date_object=datetime.strptime(date_string,"%d %b %Y")
n=int(date_string_to_date_object.day)
for i in range(n-1,n+2):
    str_obj=datetime(year=date_string_to_date_object.year,month=date_string_to_date_object.month,day=i)
    print(str_obj)