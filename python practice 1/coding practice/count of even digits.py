n=input()
length=len(n)
count=0
for i in range(length):
    if int(n[i])%2==0:
        count=count+1
if count>2:
    print("Count of even numnbers is greater than 2")
else:
    print("Count of even digit is not grater than two")