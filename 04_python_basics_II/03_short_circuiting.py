# Short Circuiting


is_friend = True
is_user = True
# And
if is_user or is_friend:
    print('best friend forever')
# OR
if is_user and is_friend:
    print('best friend forever')
# logical Operator

print('4 > 5', 4 > 5)
print("4 < 5", 4 < 5)
print("4 != 5", 4 != 5)
print("4 == 5", 4 == 5)
print("4 >= 5", 4 >= 5)
print("4 <= 5", 4 <= 5)

print("not (True)", not (True))

print('a' == 'A')
# IS vs ==
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
