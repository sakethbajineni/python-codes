r=int(input())
c=int(input())
end=1
for i in range(1,r+1):
    start=end
    end=start+c
    sum=""
    for j in range(start,end):
        if i==1 or i==r:
            sum=sum+str(j)+" "
        elif j==start or j==end-1:
            sum=sum+str(j)+" "
        elif j!=start or j!=end-1:
            sum=sum+" "+" "
    print(sum)