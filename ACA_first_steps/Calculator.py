cd ..num = input('Expression: ').strip().split()

if num[0].isdigit and num[2].isdigit():
    operation = num[1]
    num_1 = float(num[0])
    num_2 = float(num[2])

    match operation:
        case '*' | 'mul':
            print(num_1 * num_2)
        case '/' | 'div':
            print(num_1 / num_2)
        case '+' | 'add':
            print(num_1 + num_2)
        case '-' | 'sub':
            print(num_1 - num_2)
        case _:
            print('what are you doing ?')
else:
    print(' not digit ')