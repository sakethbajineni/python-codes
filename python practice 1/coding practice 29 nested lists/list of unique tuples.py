def convert(new_list):
    list_a=[]
    for i in new_list:
        list_a+=[int(i)]
    return list_a

n=int(input())
list_main=[]
for i in range(n):
    input_a=input().split()
    list_b=convert(input_a)
    set_a=set(list_b)
    sorting=sorted(set_a)
    if sorting==list_b:
        list_main.append(list_b)
print(list_main)