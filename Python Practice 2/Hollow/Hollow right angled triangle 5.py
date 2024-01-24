n=int(input())
for i in range(1,n+1):
    spaces=(n+1)-i
    if i==1 or i==2 or i==n:
        print(spaces*"  "+i*"* ")
    else:
        hollow=i-2
        print(spaces*"  "+"* "+hollow*"  "+"* ")
