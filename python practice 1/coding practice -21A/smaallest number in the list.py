list=input()
splitting=list.split()
smaller=int(splitting[0])
for i in splitting:
    if int(i)<smaller:
        smaller=i
print(smaller)
