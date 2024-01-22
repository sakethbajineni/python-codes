word=input()
splitting=word.split()
sum=""
for i in splitting:
    length=len(i)
    for j in range(length):
        if j==2:
            sum=sum+i[j]
joining=",".join(sum)
print(joining)