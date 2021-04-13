# Exercise: Check for dupliates in list

some_lits = ['a', 'b', 'c', 'd', 'd', 'b']
duplicates = []
for value in some_lits:
    if some_lits.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
