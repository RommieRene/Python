num = int(input('Enter big digits: '))
same_num = num

rev = 0
while num > 0:
    r = num % 10
    num = num // 10
    rev = rev * 10 + r

if same_num == rev:
    print('Your number is Palindrome', same_num)
else:
    print("The Number is not Palindrome")