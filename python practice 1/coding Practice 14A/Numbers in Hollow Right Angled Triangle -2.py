n=int(input())
end=1
for i in range(1,n+1):
    start=end
    end=start+i
    sum=""
    spaces=n-i
    for j in range(start,end):
        j=end-j

        if i==1 or i==2  or i==n:
            sum=sum+str(j)+" "
        elif j==i or j==1:
            sum=sum+str(j)+" "
        elif j!=i or j!=1:
            sum=sum+" "+" "
    print(spaces*"  "+sum)