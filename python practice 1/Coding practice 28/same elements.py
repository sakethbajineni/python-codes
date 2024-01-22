n=input().split()
new_list=[]
for i in n:
    new_list=new_list+[int(i)]
set_a=set(new_list)
length=len(set_a)
# print(length)
if length==1:
    print(True)
else:
    d=sorted(set_a)
    print(d)