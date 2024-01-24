m=input().split()
n=int(input())
strings=''
for i in m:
    if len(i)!=n:
        strings+=i+" "
print(strings)