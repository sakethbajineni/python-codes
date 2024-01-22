n=input()
length=len(n)
count=0
for i in range(length):
    if int(n[i])==0:
        count=count+1
if count>3:
    print("Count of zeroes is greater than three")
else:
    print("count of zeroes is not greater than three")