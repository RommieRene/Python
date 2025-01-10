num1 = int(input('user 1 Enter a number: '))
num2 = int(input('user 2 Enter a number'))

if num1 - num2 > 0:
    print(f'user 1 is higher from user 2 {num1 - num2}')
elif num1 - num2 == 0:
    print(f'user 1 and user 2 are Equal')
else:
    print(f'user 2 is higher then user 1 {num1 - num2}')