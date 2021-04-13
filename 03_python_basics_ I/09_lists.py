# list slicing
amazon_cart = [
    'notebooks',
    'surglasses',
    'toys',
    'grapes'
]

print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'

print(amazon_cart)

# Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],

]

print(matrix)
print(matrix[1])
print(matrix[1][1])

# List Methods

players = ['Santi', 'Ramos', 'Iniseta', 'Xavi', 'Iker', 'Xalonso']
print(players)
players.append('Pique')
print(players)
players.insert(0, 'Cazorla')
print(players)
players.extend(['Raul', 'Villa'])
print(players)
players.pop()
print(players)
players.pop(1)
print(players)
players.remove('Pique')
print(players)
# players.clear()
# print(players)
print(players.index('Raul'))
print('Cazorla' in players)
print(players.count('Ramos'))

print(sorted(players))
# print(players.reverse())

sentence = ''
new_sentence = '__'.join(['hy', 'my', 'name'], )
print(new_sentence)

# list unpacking

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(a)
print(b)
print(c)
print(other)
