num_list=[(1,2,3,4,5,6),(2,4,6,8),(1,3,5,7)]
n=int(input())
def tuple_to_list(num_list):
    list_b=[]
    for i in num_list:
        list_a=list(i)
        if n in list_a:
            list_a.remove(n)
        tuple_a=tuple(list_a)
        list_b.append(tuple_a)
    print(list_b)
tuple_to_list(num_list)

