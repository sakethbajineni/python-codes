

def consecutive_list(num_list):
    length=len(num_list)
    list_a=[]
    for i in range(length-1):
        const_sum=num_list[i]+num_list[i+1]
        list_a.append(const_sum)
    return list_a

def getting_output(num_list):
    while len(num_list)>1:
        consecutive=consecutive_list(num_list)
        print(consecutive)
        num_list=consecutive
    return


def convert_str_to_int_list(str_num_list):
    num_list=[]
    for i in str_num_list:
        num_list+=[int(i)]
    return num_list



str_num_list=input().split(",")
num_list=convert_str_to_int_list(str_num_list)
print(num_list)
getting_output(num_list)