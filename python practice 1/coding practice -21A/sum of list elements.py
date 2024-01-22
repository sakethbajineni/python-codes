numbers=input()
splitting=numbers.split()
length=len(splitting)
sum=0
for i in range(length):
    sum=sum+int(splitting[i])
print(sum)