n=int(input())
for i in range(1,n+1):
    string=str(i)
    sum=0
    length=len(string)
    for j in range(length):
        output=int(string[j])
        sum=sum+output**length
    if sum==i:
        print(i)


    # output=i**int(length)
    # if output==i:
    #     print(i)