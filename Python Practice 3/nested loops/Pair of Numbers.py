n=int(input())
count=0
for i in range(1,n):
    start=i+1
    end=(n+1)
  
    for j in range(start,end):
        if  i==1:
            end=n
        if i+j==n:
            count=count+1
print("count: "+str(count))
        
    