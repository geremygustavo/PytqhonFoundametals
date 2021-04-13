# Enumerate

for i, char in enumerate('hello word'):
    print(i, char)

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 5:
        print(f'index of 5 is {i}')
