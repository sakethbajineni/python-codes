n=int(input())
for i in range(1,n+1):
    i=(n+1)-i
    spaces=n-i
    if i==1 or i==2 or i==n:
        print(spaces*"  "+i*"* ")
    else:
        hollow=n-(spaces+2)
        print(spaces*"  "+"* "+hollow*"  "+"* ")
        