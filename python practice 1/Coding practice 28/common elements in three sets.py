def list_new(m):
    length=len(m)
    new_list=[]
    for i in range(length):
        new_list+=[int(m[i])]
    return new_list
 
m=input().split()
n=input().split()
o=input().split()
set_a=set(list_new(m))
set_b=set(list_new(n))
set_c=set(list_new(o))

common_value=(set_a&set_b&set_c)
print(common_value)

