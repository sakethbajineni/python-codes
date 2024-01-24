from datetime import datetime
date_string=input().split()
mapping=list(map(int,date_string))
count=0
for i in range(mapping[0],mapping[1]+1):
    for j in range(1,13):
        str_obj=datetime(year=i,month=j, day=1)
        weekdays=str_obj.strftime("%A")
        if weekdays=="Monday":
            count=count+1
print(count)
