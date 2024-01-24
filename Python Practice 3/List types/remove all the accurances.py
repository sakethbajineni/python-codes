list_a=[1,3,4,2,4,2,4,2,45,6,7]
n=int(input())
count=list_a.count(n)
for i in range(count):
    list_a.remove(n)
print(list_a)