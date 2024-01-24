m=int(input())
n=int(input())
end=m+n
output=0
for i in range(1,end):
    if m%i==0 and n%i==0:
        output=i
print(output)