n=int(input())
s1=set()
s2=set()
for i in range(1,n+1):
    s1.add(int(2*i))
    s2.add(int(3*i))
difference=s1-s2
symmetric_difference=s1^s2
list_a=list(difference)
list_b=list(symmetric_difference)
list_a.sort()
list_b.sort()
print(list_a)
print(list_b)
