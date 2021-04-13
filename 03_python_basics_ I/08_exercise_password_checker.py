# Excercice
username = input('what is your name ?')
password = input('what is your pwd?')

hidden_password = '*' * len(password)

print(f'{username}, your password,{hidden_password}, is {len(password)} letters long')
