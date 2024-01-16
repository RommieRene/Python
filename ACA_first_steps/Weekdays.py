
weekDays = input('write here the day of the week: ')
match weekDays:
    case "1":
        print('Monday')
    case "2":
        print('Tuesday')
    case '3':
        print('Wendsday')
    case '4':
        print('Thursday')
    case '5':
        print('Friday')
    case '6':
        print('Saturday')
    case '7':
        print('Sunday')
    case _:
        print("is that a number of weekdays ?")
