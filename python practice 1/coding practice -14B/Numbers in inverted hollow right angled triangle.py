s=int(input())
n=int(input())
end=s
for i in range(1,n+1):
    i=(n+1)-i
    space=n-i
    sum=""
    start=end 
    end=start+i
    for j in range(start,end):
        if i==1 or i==2 or i==n:
            sum=sum+str(j)+" "
        else:
            end=start+2
            spaces=i-2
            if j==start:
                sum=sum+str(j)+spaces*"  "
            elif j==end-1:
                sum=sum+str(j)+" "


       
    print(space*"  "+sum)
        
        
                
    

 
          
    