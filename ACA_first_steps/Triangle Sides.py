import math

abc = input(" Enter here triangle's 3 sides with whitespace:  ").split()
A = abc[0]
B = abc[1]
C = abc[2]


if A.isdigit() and B.isdigit() and C.isdigit():
    a = int(A)
    b = int(B)
    c = int(C)
    if a > 0 and b > 0 and c > 0:
        print('positive')
    if a + b > c and a < c + b and c + a > b:
        p = (a + b + c) / 2
        AA = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("area of triangle is ", AA)
    else:
        print(f'there is no triangle with the sides -> {a},{b},{c}.')
else:
    print('you should enter an integer number')



