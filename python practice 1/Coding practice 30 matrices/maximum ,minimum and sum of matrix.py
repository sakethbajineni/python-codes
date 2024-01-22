def convert(list_a):
    new_list=[]
    for i in list_a:
        new_list+=[int(i)]
    return new_list

m,n=input().split()
m,n=int(m),int(n)
new_list=[]
for i in range(m):
    input_a=input().split()
    list_a=convert(input_a)
    new_list.extend(list_a)

print(max(new_list))
print(min(new_list))
print(sum(new_list))
