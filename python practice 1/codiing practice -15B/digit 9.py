n=int(input())
for i in range(1,2*n):
    if i==1 or i==n or i==2*n-1:
        print(n*"* ")
    elif i>1 and i<n:
        spaces=n-2
        print("* "+spaces*"  "+"* ")
    elif i>n and i<2*n-1:
        spaces=n-1
        print(spaces*"  "+"* ")
    
        