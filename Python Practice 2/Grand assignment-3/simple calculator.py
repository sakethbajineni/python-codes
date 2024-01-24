m=input().split()
a=int(m[0])
b=int(m[2])
sign=m[1]
if sign=="+":
    print(a+b)
elif sign=="-":
    print(a-b)
elif sign=='*':
    print(a*b)
elif sign=="/":
    print(a/b)
