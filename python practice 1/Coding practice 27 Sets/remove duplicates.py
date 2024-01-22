n=input().split()
set_a={10,30,50,60,70,90,100}
# sets=set(list_a)
length=len(n)
for i in range(length):
    value=int(n[i])
    set_a.discard(value)
print(set_a)


