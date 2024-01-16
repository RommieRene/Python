numbers= input('type an integer here: ')
if not numbers.isdigit():
    print('please type here integer number')
else:
    number = int(numbers)
    if number % 3 == 0 and number % 2 == 0:
        print('the number divides 2 & 3')
    elif number % 2 == 0:
        print('The number is dividing 2')
    elif number % 3 == 0:
        print('the number dividing 3')

    else:
        print('the number is not dividing 2 nor 3')
        