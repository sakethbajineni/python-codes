s=int(input())
n=int(input())
end=s
for i in range(1,n+1):
    start=end
    end=start+n
    sum=""
    for j in range(start, end):
        if i==1 or i==n:
            
          sum=sum+str(j)+" "
        elif j==start or j==end-1:
           sum=sum+str(j)+" "
        else:
           sum=sum+" "+" "
    print(sum)
              
            
        