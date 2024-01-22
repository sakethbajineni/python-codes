def rotating_list(lists):
    length=len(lists)
    new_list=[]
    for i in range(length):
        new_list=new_list+[int(lists[i])]
    return new_list







lists=input().split()
rotate_times=int(input())

int_list=rotating_list(lists)
length=len(int_list)
n_times=rotate_times%length
first_term=int_list[:n_times]
last_term=int_list[n_times:]
last_term.extend(first_term)
print(last_term)