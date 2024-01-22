n=int(input())
factor=0
for i in range(1,n):
    if n%i==0:
        factor=i
print(factor)