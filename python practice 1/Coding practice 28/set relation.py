num_set={1,2,3,4,5,6,7,8,9}
list=input().split()
list_new=[]
for i in list:
    list_new+=[int(i)]
sorted(list_new)
set_a=set(list_new)
if set_a.issubset(num_set):
    print("subset")
if set_a.issuperset(num_set):
    print("superset")
if set_a.isdisjoint(num_set):
    print("disjoint")