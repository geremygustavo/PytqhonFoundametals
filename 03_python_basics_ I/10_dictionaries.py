# Dictionary
from sympy import primenu

dictionary = {
    'a': [1, 2, 3],
    'b': 2,
    'c': 'hello'
}
print(dictionary['a'])

# Methods

print(dictionary.get('b'))
# dictionary_2 = dict(name= 'abel')
# print(dictionary_2)

print('a' in dictionary)
print('hello' in dictionary.values())
print(('c', 'hello') in dictionary.items())

dictionary_copy = dictionary.copy()
print(dictionary_copy)

dictionary_copy.pop('a')
print(dictionary_copy)
print(dictionary_copy.popitem())
dictionary_copy.update({'b': 'updated'})
print(dictionary_copy)
