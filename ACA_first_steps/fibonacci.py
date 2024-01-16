
def get_fibonaci(n:int):
    if n < 0:
        print('invalid syntax')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return get_fibonaci(n-1) + get_fibonaci(n-2)







