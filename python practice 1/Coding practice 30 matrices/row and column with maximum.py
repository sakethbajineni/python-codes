def convert(list_a):
    new_list=[]
    for i in list_a:
        new_list+=[int(i)]
    return new_list
m,n=input().split()
m,n=int(m),int(n)
list_row_column=[]
list_b=[]
for i in range(m):
    input_a=input().split()
    list_a=convert(input_a)
    list_row_column.append(list_a)
    list_b.extend(list_a)
maximun_num=max(list_b)
print(maximun_num)
row_list=[]
column_list=[]
row=0
column=0
for i in list_row_column:
    if maximun_num in i:
        column=(i.index(maximun_num))
        row=(list_row_column.index(i))
        row_list.extend(i)
    column_list=column_list+[int(i[column])]
print(row_list)
print(column_list)
    

    