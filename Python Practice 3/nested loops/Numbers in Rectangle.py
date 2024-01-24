n=int(input())
s=int(input())
for i in range(1,n+1):
    sum=""
    for j in range(7,7+s):
        sum=sum+str(j)+" "
    print(sum)
        