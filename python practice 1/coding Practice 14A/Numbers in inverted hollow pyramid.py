n=int(input())
s=int(input())
for i in range(1,n+1):
    i=(n+1)-i
    spaces=n-i
    start=s
    end=start+i
    sum=""
    for j in range(start,end):
        if i==n or i==2 or i==1:
            sum=sum+str(j)+" "
        elif j==start or j==end-1:
            sum=sum+str(j)+" "
        elif j!=start or j!=end-1:
            sum=sum+" "+" "
    print(spaces*" "+sum)