string_a=input().split(",")
string_b=input().split(",")
set_a=set(string_a)
set_b=set(string_b)
intersection=set_a&set_b
list_a=list(intersection)
list_a.sort()
print(list_a)