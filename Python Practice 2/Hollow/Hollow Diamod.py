n=int(input())
for i in range(1,2*n):
    spaces=n-i
    hollow=i-2
    if i==1 or i==2:
        print(spaces*" "+i*"* ")
    elif i<=n:
        print(spaces*" "+"* "+hollow*"  "+"* ")
    else:
        i=(2*n)-i
        spaces=n-i
        if i==1 or i==2:
            print(spaces*" "+i*"* ")
        else:
            hollow=i-2
            print(spaces*" "+"* "+hollow*"  "+"* ")
    