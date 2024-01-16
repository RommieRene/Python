
DN = input('write here a numbers with comma: ').split(',')

if len(DN) == len(set(DN)):
    print('there are no duplicates')
else:
    print("there are duplicates ")
