n=int(input())
sums=0
for i in range(1,n+1):
    sums=sums+i
end=sums
for j in range(1,n+1):
    j=(n+1)-j
    start=end
    end=start+j
    sum=""
    # print("statr"+str(start))
    for k in range(start,end):
        
        k=2*start-k
        if j==1 or j==2 or j==n:
            sum=sum+str(k)+" "
        elif k==start or k==(start-j)+1:
            sum=sum+str(k)
        else:
            sum=sum+" "+" "
          

    end=k-1
    print(sum)

