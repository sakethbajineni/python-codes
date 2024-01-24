set_a={1,2,3,4,5,6}
set_b={1,2,3,4}
superset=set_a.issuperset(set_b)
print(superset)

# The All values in the set_b are present in the set_a
# so thats why set_a is the superset of the set_b
set_1={1,2,3,4,5,6,7,8}
set_2={1,2,3,4,100}
superset_1=set_1.issuperset(set_2)
print(superset_1)