name = 'Patrick'
password = 'test'


if input('What is your name:') == name:
    print('Hello Patrick') # start of first block of code
    if input('Input your password:') == password:
        print('Access granted.')#second block of code
    else:
        print('Wrong passwword:')#third block of code
