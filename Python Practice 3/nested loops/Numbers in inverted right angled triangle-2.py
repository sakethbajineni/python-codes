n=int(input())
sum=0
for i in range(1,n+1):
    i=(n+1)-i
    sum=sum+i
start=sum
end=start+1

    for j in range(start,end):
          j=(2*end-j)-(n+1)
          print(j)
        
        
    #     spaces=(n+1)-i
    #     j=(2*end-j)-(n+1)
    #     sums=sums+str(j)+" "
    # print(spaces*" "+sums)
