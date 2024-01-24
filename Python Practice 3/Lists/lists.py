list_a=[1,2,3]
list_b=[1,2,3]
print(id(list_a))
print(id(list_b))

list_a=[1,2,3]
list_b=list_a
print(id(list_a))
print(id(list_b))

list_a=[1,2]
list_b=list_a
list_a=[6,7]
print("list_a: " +str(list_a))
print("list_b: " +str(list_b))

list_a=[1,2]
list_b=list_a
list_a+=[6,7]
print("list_a: "+str(list_a))
print("list_b: "+str(list_b))

a=2
list_a=[1,a]
print(list_a)
a=3
print(list_a)
