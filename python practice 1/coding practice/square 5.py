s=int(input())
n=int(input())
last_value=s+n
sum=""
for i in range(1,last_value):
    if i>=s:
        sum=sum+str(i)+" "
for i in range(n+1):
    print(sum)
