def convert_list(inputs):
    new_list=[]
    for i in inputs:
        new_list+=[int(i)]
    return new_list





m,n=input().split()
m=int(m)
n=int(n)
list_b=[]
for i in range(m):
    inputs=input().split()
    list_a=convert_list(inputs)
    list_b.extend(list_a)
sorting=sorted(list_b)
v=0
z=n
for i in range(m):
    d=''
    for j in range(v,z):
        d+=str(sorting[j])+' '
    print(d)
    v+=n 
    z+=n
