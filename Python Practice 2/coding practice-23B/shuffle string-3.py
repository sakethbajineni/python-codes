def shuffle_string(string,indexes):
    splitting=indexes.split()
    length=len(string)
    sum=""
    for i in range(length):
        lists=splitting[i]
        sum=sum+string[int(lists)]
    print(sum)
word=input()
indexes=input()
shuffle_string(word,indexes)