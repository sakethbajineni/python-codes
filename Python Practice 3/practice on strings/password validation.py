word=input()
length=len(word)
count=0
for i in range(length):
    if word[i].isdigit():
        count=count+1
if count!=0:
    print("valid password")
else:
    print("not a valid password")