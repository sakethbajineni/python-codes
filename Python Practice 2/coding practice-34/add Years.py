from datetime import datetime,timedelta
date_string=input()
n=int(input())
date_string_to_date_object=datetime.strptime(date_string,"%b %d %Y")
ADDING=date_string_to_date_object+timedelta(days=n*365)
print(ADDING)
