n=int(input())
for i in range(1,n+1):
    start=n
    end=2*n
    sum=""
    for j in range(start,end):
        j=2*n-j
        if i==1 or i==n:
            sum=sum+str(j)+" "
        elif j==start or j==(start-n)+1:
            sum=sum+str(j)+" "
        else:
            sum=sum+" "+" "
    print(sum)