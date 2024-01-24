m=int(input())
n=int(input())
if m>n:
    greater=m
else:
    greater=n
output=0
for i in range(greater):
    if m%i==0 and n%i==0:
         output=i
print(output)