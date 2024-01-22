nums=input()
splitting=nums.split()
length=len(splitting)
list=[]
for i in splitting:
    if int(i)%3==0:
        list=list+[i]
print(list)