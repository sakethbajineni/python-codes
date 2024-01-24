word=input()
length=len(word)
sum=""
for i in range(length):
    if i==0 or word[i].islower():
        sum=sum+word[i]
    elif word[i].isupper():
        sum=sum+" "+word[i]
print(sum)
        