word=input()
vowels=["a","e","i","o","u"]
vowel=0
consonants=0
for i in word:
    if i not in  vowels:
        consonants=consonants+1
        
    else:
        vowel=vowel+1
print("vowels in given input :"+str(vowel))
print("constants in given input :"+str(consonants))

        