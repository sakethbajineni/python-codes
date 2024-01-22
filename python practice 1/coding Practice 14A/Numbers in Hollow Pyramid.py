n=int(input())
for i in range(1,n+1):
    start=n
    end=start+i
    sum=""
    spaces=n-i
    # print(spaces)
    for j in range(start,end):
        if i==1 or i==2 or  i==n:
            sum=sum+str(j)+" "
        elif j==start or j==end-1:
            sum=sum+str(j)+" "
        elif j>start or j<end-1:
            sum=sum+" "+" "
    print(spaces*" "+sum)