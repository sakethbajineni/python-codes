m=int(input())
n=int(input())
start=(m*n)+1
for i in range(1,m+1):
    # print(start)
    end=start
    start=end-n
    sum=""
    for j in range(start,end):
        j=(2*end-j)-m
        sum=sum+str(j)+" "
    print(sum)

# Inputs 
# 6
# 5
