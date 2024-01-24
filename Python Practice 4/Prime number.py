number=int(input())
count=0
for i in range(2,number):
    print(number%2)
    if (number%i)==0:
        count=count+1
if count!=0:
    print("Not a prime Number")
else:
    print("Prime Number")
