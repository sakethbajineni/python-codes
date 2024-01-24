s=int(input())
n=int(input())
end=2
for i in range(1,n+1):
    start=end
    end=start+2*i
    sum=""

    for j in range(start,end):
        sum=sum+str(j)+" "
    print(sum)
        
    # Inputs
    # 2
    # 4

    # Inputs 
    # 6
    # 5