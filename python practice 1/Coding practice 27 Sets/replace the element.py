num_list=[(10,20,30),(1,2),(5,10,15,45)]
n=int(input())
new_list=[]
for tuple_a in num_list:
    print(tuple_a)
    update=tuple_a[:-1]+(n,10,)
    new_list.append(update)
print(new_list)