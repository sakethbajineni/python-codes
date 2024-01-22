n=int(input())
for i in range(1,n+1):
    sum=""
    spaces=n-i
    for j in range(1,i+1):
        sum=sum+str(j)+" "
    print(spaces*" "+sum)
        