a=2
list_a=[1,"six",a,2.2]
list_b=[1,list_a]
print(list_a)
print(list_b)
print(list_a+list_b)

# ADDING ELEMENTS TO THE LIST 

list_a=[]
for i in range(1,5):
    list_a +=[i]
print(list_a[0])


 
# Repetition 
list_a=[1,2,3]
list_b=list_a*3
print(list_b)

# converting to list
list_a=list(range(4))
print(list_a)

# Lists are mutable
list_a=[1,2,3,4]
print(list_a)
print(list_a[3])
list_a[3]=7
print(list_a[3])
print(list_a)

# 
list_a=["dog","cat"]
list_b=["fox","rat"]
list_a+=list_b
print(list_a)

# finding id 
print(id("hellow"))
a="hello"
a=a+"world"
print(id(a))