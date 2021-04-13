# Define String variables

print('Hello this is a example !!')
print("Hello this is a example whit double quotes!!")

print('''
this 
is a
example
with 
spaces
''')

# Concat

print("my name is " + "---->" + " abel")
print("my phone number is " + "---->" + str(7888293))
print("my email is {}".format('abel@gmail.com'))

# type conversion

print(str(0))
print(str(0))
print(type(str(0.9999)))
print(type(str(0)))

# Escape Sequence
print("\t tab")
print("\n new line \n in \n console")
print("It \'s \"Kind of \"")  # It 's "Kind of "

# Formating
String1 = "{ab} {f} {g}".format(g='my name ', f='is ', ab='abel')
print(String1)

# indexing
self = "abcdefghijklmnopq"
print(self[0:4])
print(self[6:])
print(self[:8])
print(self[0:15:2])
print(self[-5])
print(self[::-3])

# Build in Functions
# ref https://www.w3schools.com/python/python_ref_string.asp
print(len('hello'))

name = "gustavo"

print(name.upper())
print(name.capitalize())
print(name.find('av'))
print(name.replace('v', 'b'))
