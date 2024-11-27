password = input('Enter your password:')
if len(password) > 7:
    print('Password is valid')
elif len(password) == 7:
    print('Password is good but not too strong')
else:
    print('Password is too short')