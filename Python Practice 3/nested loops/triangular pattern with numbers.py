# n=int(input())
# sum=""
# for i in range(1,n+1):
#     sum=sum+str(i)+" "
#     print(sum)

# ANOOTHER Method

num=int(input())
for i in range(1,num+1):
    row_output=" "
    for j in range(1,i+1):
        row_output=row_output+str(j)+" "
    print(row_output)
    