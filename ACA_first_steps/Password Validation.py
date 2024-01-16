password = list(input('write your password: '))
password1 = set(password)
upper_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lower_letters = set('abcdefghijklmnopqrstuvwxyz')
number = set('0123456789')
Symbols = set(r"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

if len(password) < 8:
    print(' your chars should be 8 or more ')
elif not password1 & upper_letters:
    print('u have no upper letters')
elif not password1 & lower_letters:
    print('u have no lower letters')
elif not password1 & number:
    print('you password has no Numbers')
elif not password1 & Symboles:
    print(' Your password has no symbols')
else:
    print("password is correct")
