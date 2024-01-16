def sum_of_digits(num)->int:
        listo = 0
        for i in range(0, len(num), 1):
            listo += int(x[i])
        return listo

x = input('type a number  digits: ')
print(sum_of_digits(x))