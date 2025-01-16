a = 0
b = 1
n = 1
count = 0
while count != 10:
    n = a + n
    a = n - a
    count += 1
    print(n,a)

a = int(input('Enter Fibo number: '))
n = 0
c = 1
for i in range(a):
    print(n)
    b = n + c
    n = c
    c = b