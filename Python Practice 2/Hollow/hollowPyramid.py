n=int(input())
for i in range(1,2*n):
    spaces=i-2
    if i==1 or i==2:
        print(i*(str(i)+" "))
    elif i<=n:
        print(str(i)+spaces*"  "+str(i))
    else:
        nums=i-n
        i=n-nums
        space=i-2
        if i==1 or i==2:
             print(i*(str(i)+" "))
        else:
          print(str(i)+space*"  "+str(i))
        

        
    