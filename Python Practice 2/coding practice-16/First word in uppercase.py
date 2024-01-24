word=input()
count=0
for i in word:
    if i==" ":
        break
    else:
        count=count+1
first_word=word[0:count]
firstWord_capital=first_word.upper()
total=firstWord_capital+word[count:]
print(total)
