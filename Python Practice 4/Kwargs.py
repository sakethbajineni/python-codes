def greet(**kwargs):
    for k,v in kwargs.items():
        print("{}:{}".format(k,v))
greet(a=1,b=2)

def greet_1(arg1="saketh",arg2="patel"):
    print(arg1+" "+arg2)
dict_a={"arg1":"raju","arg2":"ram"}
greet_1(**dict_a)

def greet_3(*args):
    print(args)
greet_3("saketh","patel",1,2,4)

def greet_4(arg1="name",arg2="patel"):
    print(arg1+" "+arg2)
list_c=["manish","pasha"]
greet_4(*list_c)


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
