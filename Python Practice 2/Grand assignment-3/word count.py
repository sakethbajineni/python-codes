m=input().split()
dict_a=list(dict(m))
print(dict_a)
# print(sorting)
# print(m.count("world"))

for i in range(len(dict_a)):
    # print(m[i])
    count=m.count(dict_a[i])
    string="{}:{}".format(dict_a[i],count)
    print(string)
