word=input()
splitting=word.split()
length=len(splitting)
print(length)
list=[]
for i in range(length):
    j=length-i
    list=list+[splitting[j]]
print(list)