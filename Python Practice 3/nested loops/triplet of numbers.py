n=int(input())
count=0
for i in range(1,n):
    start=i+1
    end=n
    for j in range(start,end):
        
        
        start=i+2
        end=n
        for k in range(start, end):
            if i+j+k==n and i<j<k:
                count=count+1
print(count)
    