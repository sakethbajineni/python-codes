def list_of_squares(list):
    splitting=list.split()
    print(splitting)
    length=len(splitting)
    print(length)
    new_list=[]
    for i in range(length):
        s=splitting[i]
        print(s)
        sum=int(s)**2
        new_list=new_list+[sum]
    print(new_list)
list=input()
list_of_squares(list)