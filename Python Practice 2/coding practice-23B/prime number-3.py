def prime_number(num):
    count=0
    for i in range(1,num):
        if int(num)%i==0:
            count=count+1
    if count==1:
        print("Prime number")
    else:
        print("Not a prime number")
num=int(input())
num1=int(input())
prime_number(num)
prime_number(num1)