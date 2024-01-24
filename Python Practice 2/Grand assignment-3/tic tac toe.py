a=input().split()
b=input().split()
c=input().split()
abhinav=False
anjali=False
if a[0]==0 and a[1]==0 and a[2]==0:
    abhinav=True
elif a[0]=="X" and a[1]=="X" and a[2]=="X":
    anjali=True
elif b[0]==0 and b[1]==0 and b[2]==0:
    abhinav=True
elif b[0]=="X" and b[1]=="X" and b[2]=="X":
    anjali=True
elif c[0]==0 and c[1]==0 and c[2]==0:
    abhinav=True
elif c[0]=="X" and c[1]=="X" and c[2]=="X":
    anjali=True

for i in range(len(a)):
    if a[i]==0 and b[i]==0 and c[i]==0:
        abhinav=True
    elif a[i]=="X" and b[i]=="X" and c[i]=="X":
        anjali=True
if a[0]==0 and b[1]==0 and c[2]==0:
    abhinav=True
if c[0]=="X" and b[1]=="X" and a[2]=="X":
    anjali=True

if abhinav:
    print("Abhinav wins match")
elif anjali:
    print("anjali wins match ")
else:
    print("Tie")