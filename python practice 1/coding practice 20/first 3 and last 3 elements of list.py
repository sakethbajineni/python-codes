n=int(input())
list=[]
for i in range(n):
    inputs=input()
    if i<3:
        list=list+[inputs]
    elif i>=n-3 and i<n:
        
        list=list+[inputs]
print(list)