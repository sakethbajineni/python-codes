n=int(input())
k=int(input())
count=0
sum=""
for i in range(1,n+1):
    if n%i==0:
        count=count+1
        sum=sum+str(i)
    value=count-k
value=count-k
print(value)
print(sum[value])
