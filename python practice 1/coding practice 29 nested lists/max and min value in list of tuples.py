n=int(input())
min=0
max=0
index_0=[]
index_1=[]
for i in range(n):
    input_a=input().split()
    index_0+=[int(input_a[0])]
    index_1+=[int(input_a[1])]
sorting_0=sorted(index_0)
sorting_1=sorted(index_1)
tuple_a=(sorting_0[len(sorting_0)-1],sorting_0[0])
tuple_b=(sorting_1[len(sorting_1)-1],sorting_1[0])
print(tuple_a)
print(tuple_b)