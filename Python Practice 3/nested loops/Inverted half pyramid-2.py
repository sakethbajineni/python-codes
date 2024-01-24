n=int(input())
for i in range(1,n+1):
    i=(n+1)-i
    sum=""
    start=(n+1)-i
    for j in range(start,n+1):
        j=(n+1)-j
        sum=sum+str(j)+" "
    print(sum)