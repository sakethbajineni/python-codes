students_dict={"ram":"cricket","naresh":"football","vani":"Tennis","Rahim":"cricket"}
n=int(input())
for i in range(n):
    inputs=input().split()
    key,value=inputs[0],inputs[1]
    students_dict[key]=value
print(students_dict)
