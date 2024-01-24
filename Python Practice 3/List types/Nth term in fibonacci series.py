n=int(input())
a=0
b=1
c=a+b
list=[]
for i in range(n):
    a=b
    b=c
    
    if i==0:
        a=i
        list+=[a]
    elif i==1:
        b=i
        list+=[b]
    else:
        c=a+b
        list+=[c]

print(list[n-1])
        

