year = int(input('Enter Year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print("The Year is Leap Year")
    else:
        print('The Year is Not Leap Year')
elif year % 4 == 0:
    print('Leap Year')
else:
    print('not a leap year')