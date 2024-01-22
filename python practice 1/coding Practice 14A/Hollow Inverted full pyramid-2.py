n=int(input())
for i in range(1,n+1):
    i=(n+1)-i
    spaces=n-i
    sum=""
    for j in range(1,i+1):
        if i==n or i==1 or i==2:
            sum=sum+str(j)+" "
        elif j==1 or j==i:
            sum=sum+str(j)+" "
        else:
            sum=sum+" "+" "
    print(spaces*" "+sum)