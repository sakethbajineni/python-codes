# lambda is a anonymous function which accept number of arguments but only one expression

x=lambda a,b: a*b 
print(x(2,4))


y=lambda a,b,c: a*b*c
print(y(3,4,5))


# returning lamda function in another function

def fun(n):
    return lambda a:a*n
myDoubler=fun(2)
print(myDoubler(11))

# passing two values

def fun1(n):
    return lambda a:a*n
myDoubler1=fun1(2)
myTrippler=fun1(3)
print(myDoubler1(11))
print(myTrippler(11))