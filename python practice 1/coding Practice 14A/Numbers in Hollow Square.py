n=int(input())
for i in range(1,n+1):
   sum=""
   for j in range(1,n+1):
      if i==1 or i==n:
         sum=sum+str(j)+" "
      elif i>1 or i<n:
         if j==1 or j==n:
            sum=sum+str(j)+" "
         else:
            spaces=n-2
            sum=sum+spaces*" "
            

  #  if i==1 or i==n:
  #     for j in range(1,n+1):
  #        sum=sum+str(j)+" "
  #  elif i>1 or i<n:
  #     spaces=n-2
  #     sum=sum+str(1)+" "+spaces*"  "+str(n)
    
           
   print(sum)