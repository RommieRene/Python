n = int(input('Enter big digits'))
r = n
while r > 0:
    r = n % 10
    n = n // 10
    print(r)