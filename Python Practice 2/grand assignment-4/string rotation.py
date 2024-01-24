s1=input()
s2=input()
count=0
if s1==s2:
      print(count)
else:
    adding=''
    for i in range(1,len(s1)+1):

        r1=s1[-i:]
        remaining=s1[:-i]
        count=count+1
        adding=r1+remaining
        if s2==adding:
           
           print(count)
           break
    if s2!=adding:
        print("No match")















