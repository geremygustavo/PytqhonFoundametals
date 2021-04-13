# Tuple
from sympy import principal_branch

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(5 in my_tuple)

user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
}
print(user[(1, 2)])

print(my_tuple[1:7])

tuple_test = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple_test.index(4))
