n=int(input())
for i in range(1,n+1):
    sum=""
    spaces=n-i
    for j in range(1,i+1):
        if i==1 or i==2 or i==n:
            sum=sum+"*"+" "
        elif j==1 or j==i:
            sum=sum+"*"+" "
        else:
            sum=sum+" "+" "
    print(spaces*" "+sum)