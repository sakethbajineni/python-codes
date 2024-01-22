s=int(input())
n=int(input())
end=s 
for i in range(1,n+1):
    start=end
    end=start+i
    sum=""
    for j in range(start,end):
        if i==1 or i==2 or i==n:
            sum=sum+str(j)+" "
        else:
            spaces=i-2
            end=start+2
            if j==start:
                sum=sum+str(j)+spaces*"  "+" "
            elif j==end-1:
                sum=sum+str(j)+" "
    print(sum)