n=int(input())
start=0
end=1
for i in range(1,n+1):
    start=end
    end=start+n
    sum=""
    for j in range(start,end):
        sum=sum+str(j)+" "
    print(sum)