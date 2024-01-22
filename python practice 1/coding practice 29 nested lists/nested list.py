def nested_list(n):
    list_a=[]
    for i in range(n):
        input_a=input().split()
        value=[] 
        for j in input_a:
            value=value+[int(j)]
        list_a.append(value)
    print(list_a)



n=int(input())
nested_list(n)