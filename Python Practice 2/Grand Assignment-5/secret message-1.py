dict_a={"a":"z","b":"y","c":"d","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","i":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"}
n=input().lower()
# print(n)
output=""
for i in n:
    # print(i)
    if i in dict_a.keys():
        output+=dict_a[i]
print(output)

