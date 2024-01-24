word=input()
upper=0
lower=0
digit=0

length=len(word)
for i in range(length):
    if word[i].isupper():
        upper=upper+1
    elif word[i].islower():
        lower=lower+1
    elif word[i].isdigit():
        digit=digit+1
if upper>=1 and lower>2 and digit>2:
    print("valid password")
else:
    print("not a valid password")
print(lower)
print(upper)
print(digit)