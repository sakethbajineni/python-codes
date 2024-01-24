n=int(input())
for i in range(1,n+1):
    i=(n+1)-i
    if i==1 or i==n:
        print(i*"* ")
    else:
        spaces=i-2
        print("* "+spaces*"  "+"* ")
        
    