n=int(input())
for i in range(1,n+1):
    sum=""
    for j in range(1,n+1):
        j=(n+1)-j
        sum=sum+str(j)+" "
    print(sum)