n=int(input())
m=int(input())
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
end=0
for i in range(1,n+1):
    sum=""
    start=end
    end=start+m
    for j in range(start,end):
        if i==1 or i==n:
            sum=sum+alphabets[j]+" "
        elif j==start or j==end-1:
            sum=sum+alphabets[j]+" "
        else:
            sum=sum+" "+" "
    print(sum)