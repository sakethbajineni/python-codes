n=input()
digits=""
letters=''
for i in n:
    if i.isdigit():
        digits+=i
    else:
        letters+=i
print(letters+digits)