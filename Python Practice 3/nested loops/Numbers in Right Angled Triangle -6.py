n=int(input())
for i in range(1,n+1):
    sum=""
    for j in range(1,i+1):
        sum=sum+str(j)+" "
    for j in range(1,i):

        sum=sum+str(j)+" "
        
    print(sum)
        