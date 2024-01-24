from datetime import datetime,timedelta
date_string=int(input())
n=datetime(1970,1,1)
timed=timedelta(seconds=int(date_string))
m=n+timed
bla=m.strftime("%Y-%m-%d %H:%M:%S")
print(bla)



# input  give seconds as inputs 
# 44 
# output
# 1970-01-01 00:00:44