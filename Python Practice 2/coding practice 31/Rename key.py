fruits={"apples":10,"bananas":20,"mangoes":15,"oranges":200,"watermelons":50}
m=input()
n=input()
list_a=list(fruits.items())
print(list_a[0][0])
for i in range (len(list_a)):
    if list_a[i][0]==m:
        update=(n,list_a[i][1])
        list_a[i]=update
print(list_a)