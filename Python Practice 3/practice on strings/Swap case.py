word=input()
length=len(word)
sum=""
for i in range(length):
    if word[i].islower():
        sum=sum+word[i].upper()
    elif word[i].isupper():
        sum=sum+word[i].lower()
print(sum)
