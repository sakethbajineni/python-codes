def convert(x):
    new_list=[]
    for i in x:
        new_list=new_list+[int(i)]
    z=set(new_list)
    return z
n=int(input())
main_list=[]
for i in range(n):
    list=input().split()
    con=convert(list)
    main_list.append(con)
res=main_list[0]
print(res)
for i in main_list:
    res=res&i
res=sorted(res)
print(res)


