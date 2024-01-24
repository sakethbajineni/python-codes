# reduce is not A  builtin function it is a python standard library so we have to import it
# the reduce is present in functools module so we have import from their
from functools import reduce

sequence=input().split()
convert_seq_to_int=list(map(int,sequence))
def adding(a,b):
    return a+b
adding_the_elements_in_the_liste_using_reduce=reduce(adding,convert_seq_to_int)
print(adding_the_elements_in_the_liste_using_reduce)