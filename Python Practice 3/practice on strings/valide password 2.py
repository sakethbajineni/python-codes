word=input()
length=len(word)
count=0
for i in range(length):
    if word[i].isupper():
        count=count+1
if count==0:
    print("Not a valid password")
else:
    print("Valid password ")
    