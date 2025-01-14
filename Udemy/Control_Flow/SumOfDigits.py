n = int(input('Enter big digits: '))

summ = 0
while n > 0:
    summ += n % 10
    n = n // 10
    print('sum is ',summ)