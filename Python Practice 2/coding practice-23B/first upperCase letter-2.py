def first_upper_case_letter(word):
    capital=""
    for i in word:
        if i.isupper():
            capital=i
            break
    print(capital)
word=input()
first_upper_case_letter(word)
