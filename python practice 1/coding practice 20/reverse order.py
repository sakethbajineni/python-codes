n=int(input())
list=[]
for i in range(n):
    inputs=input()
    list=list+[inputs]
length=len(list)
print(list[:length:1])
# d=len(list)-1
# while d>-1:
#     print(list[d])
#     d=d-1
