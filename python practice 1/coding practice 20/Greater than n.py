n=[1,3,2,4,90,3234,24,24,43,533]
length=len(n)
m=int(input())
list=[]
for i in n:
    if i>m:
        list=list+[i]
print(list)