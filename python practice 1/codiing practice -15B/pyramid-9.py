n=int(input())
for i in range(1,n+1):
    spaces=n-i
    value=2*i-1
    print(spaces*". "+value*"0 "+spaces*". ")