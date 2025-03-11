password = input('Enter a password: ')

while password != 'pass123':
    print('OOPS.... Password is incorrect. Please enter again...')
    password = input('Enter a password: ')

print('Password was correct!!!')
