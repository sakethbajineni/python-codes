list_a=[('apple','banana','orange','grapes'),('cricket','football','hockey'),('car','bicycle','bus')]
def accesing_elements(indexes):

    list_b=[]
    for i in indexes:
        list_b+=[int(i)]
    return list_b



list_c=[]
n=int(input())
for i in range(n):
    input_a=input().split()
    elements=accesing_elements(input_a)
    list_c+=[elements]
list_d=[]
for i in list_c:
    x=i[0]
    y=i[1]
    list_d+=[list_a[x][y]]
print(list_d)

