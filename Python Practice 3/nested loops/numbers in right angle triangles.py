s=int(input())
n=int(input())
end=s
for i in range(1,n+1):
    s=end
    end=s+i
    sum=""
    for j in range(s,end):
        sum=sum+str(j)+" "
    print(sum)


# Inputs     
# 10
# 5

# Inputs
# 9
# 3
