name=input()
age=int(input())
msg="Hi {} you are {} years old"
print(msg.format(name,age))

# WE CAN ALSO GIVE NUMBERING TO THE PLACEHOLDER
msg="hi {1} you are {0} years old"
print(msg.format(name,age))

# WE CAN ALSO GIVE THE NAMING TO THR PLACEHOLDER
msg="Hi {name}. you are {age} years old"
print(msg.format(name=name,age=age))
