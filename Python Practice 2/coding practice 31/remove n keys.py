alphabets={'a':97,'b':98,'c':99,'d':100,'e':101,'f':102,'g':103,'h':104}
inputs=input().split()
for i in inputs:
    if i in alphabets:
       
       del alphabets[i]
print(alphabets)