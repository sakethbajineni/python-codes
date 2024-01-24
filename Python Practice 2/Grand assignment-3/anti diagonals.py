def anti(c,m,n):
    for i in range(m+n):
        for j in range(i+1):
            if j<m and (i-j)<n:
                d=c[j][i-j]
                print(d,end=' ')
        print()

m,n=input().split()
m=int(m)
n=int(n)
c=[]
for i in range(m):
    c+=[list(map(int,input().split()))]
anti(c,m,n)
 