m=input()
n=input()
count=0
s=''
for i in range(1,len(m)+1):
    z=m[-i]
    s=z+s
    if s==n[:i]:
        count+=1
        print(s)
    if count==0:
        print("No overlapping")




