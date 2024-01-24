n=int(input())
list=[]
for i in range(n):
    inputs=input().split()
    if inputs[0]=="append":
        value=inputs[1]
        list.append(value)
print(list)
