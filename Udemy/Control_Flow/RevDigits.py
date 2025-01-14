num = int(input('Enter big digits: '))

rev = 0
while num > 0:
    r = num % 10
    num = num // 10
    rev = rev * 10 + r

print('Reverse of your number is ',rev)
print('value of your number now is ', num)