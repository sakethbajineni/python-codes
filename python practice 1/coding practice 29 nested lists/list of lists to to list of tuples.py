def convert_to_tuple(inputs):
    list_b=[]
    for i in inputs:
        list_b+=[int(i)]
    tuple_a=tuple(list_b)
    return tuple_a





n=int(input())
list_a=[]
for i in range(n):
    input_a=input().split()
    tuples=convert_to_tuple(input_a)
    list_a+=[tuples]
print(list_a)
