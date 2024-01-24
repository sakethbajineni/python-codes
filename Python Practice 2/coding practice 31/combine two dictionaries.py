student_names_1=input().split()
student_ids_1=input().split()
student_names_2=input().split()
student_ids_2=input().split()

dict_a={}
for i in range(len(student_names_1)):
    dict_a[student_names_1[i]]=int(student_ids_1[i])
for i in range(len(student_names_2)):
    dict_a[student_names_2[i]]=int(student_ids_2[i])
print(sorted(list(dict_a.items())))
