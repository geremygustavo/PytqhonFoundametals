# For Loops
for item in "123456789":
    for x in ['a', 'b', 'c']:
        print(item, x)
# Iterable => list ,dictionary, tuple, set, string

user = {
    'name': 'Abel',
    'age': '15',
    'email': 'ab@silo.com',
    'phone': '342342352',
}

for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)
