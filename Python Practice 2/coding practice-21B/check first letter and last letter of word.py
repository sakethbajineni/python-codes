word=input()
splitting=word.split()
sum=""
for i in splitting:
    length=len(i)
    for j in range(length):
        if i[0]==i[-1]:
           sum=True
        else:
            sum=False
    print(sum)
