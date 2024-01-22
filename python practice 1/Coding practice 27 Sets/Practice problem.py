def convert_str_to_int(str_num_list):

    new_list=[]
    for i in str_num_list:
        int_num=int(i)
        new_list.append(int_num)
    return new_list
def get_unique_pairs(int_list,pair_sum):
    stop_index=len(int)
    unique_pair_set=set()
    for cur_index in range(stop_index):
        num_1=int_list[cur_index]
        num_2=pair_sum-num_1
        list_2=int_list[cur_index:]
        if num_2 in list_2:
           
           pair=(num_1,num_2)
           sorting=tuple(sorted(pair))
           unique_pair_set.add(sorting)
    return unique_pair_set
           
            




str_num_list=input().split(",")
pair_sum=int(input())
int_list=convert_str_to_int(str_num_list)
unique_pairs=get_unique_pairs(int_list,pair_sum)
for pair in unique_pairs:
    print(pair)