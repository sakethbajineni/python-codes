n=input().split()
length=len(n)
new_list=[]
for i in n:
    new_list+=[int(i)]
last_num=new_list[length-1]
list_2=[]
for i in range(1,last_num):
    if i not in new_list:
        list_2+=[int(i)]
print(list_2)