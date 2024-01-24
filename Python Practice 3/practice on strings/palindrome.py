word=input()
len_of_word=len(word)
sum=""
for i in range(len_of_word):
    i=(len_of_word-1)-i
    sum=sum+word[i]
if sum==word: 
   print("palindrome")
else:
  print("not a palindrome number")