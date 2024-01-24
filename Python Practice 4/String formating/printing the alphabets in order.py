def print_char_count(value):
    input_a=value
    set_a=set(input_a)
    set_a.discard(" ")
    for char in sorted(set_a):
        counting=input_a.count(char)
        msg="{char} : {counting}"
        print(msg.format(char=char,counting=counting))





value=input()
print_char_count(value)