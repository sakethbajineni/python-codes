n=int(input())
last=n+3
for i in range(1,last):
    if i==1 or i==last-1:
        print("+ "+n*"- "+"+ ")
    else:
        print("| "+n*"  "+"| ")
  