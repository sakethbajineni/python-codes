n=input()
set_a=set(n)
set_a.discard(" ")
sorting=sorted(set_a)

for i in sorting:
    counting=n.count(i)
    msg="{i}: {counting}"
    print(msg.format(i=i,counting=counting))

