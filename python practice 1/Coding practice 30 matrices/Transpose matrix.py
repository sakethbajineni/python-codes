def convert(input_a):
    new_list=[]
    for i in input_a:
        new_list+=[int(i)]
    return new_list


m,n=input().split()
m,n=int(m),int(n)
list_b=[]
for i in range(m):
    input_a=input().split()
    list_a=convert(input_a)
    list_b.append(list_a)
# print(list_b)

for i in range(m):
    list_d=[]
    for j in range(n):
        list_d=list_d+[list_b[j][i]]
    print(list_d)


    
    

