num_list=[(2,4,6,8),(5,15,25,35),(7,14,21)]
n=int(input())
for i in num_list:
    indexe1=num_list.index(i)
    for j in i:
        if n ==j:
            index2=i.index(j)
            print(str(indexe1)+" "+str(index2))
            break

    #         indexe1+=index2
    # print(indexe1)