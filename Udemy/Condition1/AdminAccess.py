admin1 = 'Jhon'
admin2 = 'Smith'
username = str(input('Enter your username: '))
if username == admin1 or username == admin2:
    print('Authorised')
else:
    print('Unauthorised')