# Set

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9}

print(my_set)

my_set.add(5)
my_set.add(100)
print(my_set)

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

# Methods
my_set_1 = {1, 2, 3, 4, 5, 6}

two_set = {5, 6, 8, 9}

# print(my_set_1.difference(two_set))
# my_set_1.discard(6)
# print(my_set_1)
print(my_set_1.difference_update(two_set))
# print(my_set_1.intersection(two_set))
