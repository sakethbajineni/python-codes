def convert_to_list(list):
    list_a=[]
    for i in list:
        list_a+=[int(i)]
    sorting=sorted(list_a,reverse=True)
    return sorting[0]



n=int(input())
list_b=[]
for i in range(n):
    input_a=input().split()
    num=convert_to_list(input_a)
    list_b+=[num]
print(list_b)

