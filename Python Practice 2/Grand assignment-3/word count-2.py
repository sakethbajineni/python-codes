m=input().split()
sorting=sorted(set(m))
for i in range(len(sorting)):
    count=m.count(sorting[i])
    string="{}: {}".format(sorting[i],count)
    print(string)