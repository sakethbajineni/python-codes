n=input().split()
mapping=list(map(int,n))
a=mapping[0]
b=mapping[1]
try:
    d=a/b
    print(d)
except ZeroDivisionError:
    print("Denominator cant be zero")
except ValueError:
    print("Input should be an integer") 