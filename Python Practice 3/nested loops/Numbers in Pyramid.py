n=int(input())
s=int(input())

for i in range(n,n+s):
    spaces=(n+s-1)-i
    sum=""
    for j in range(n,i+1):
        sum=sum+str(j)+"  "
    print(spaces*" "+sum)