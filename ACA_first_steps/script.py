from demorene.fibonacci import get_fibonaci

# my_file = open('my_file.txt', 'w')
# my_file.close()

with open('my_file.txt', 'w') as my_file:
    for i in range(0, 21):
        line = f'{i}. {get_fibonaci(i)}\n'
        my_file.write(line)
