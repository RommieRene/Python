# num = int(input("Enter number"))
# yerkuakan = 0
# How to convert digit from Decimal to BIanry
# while num > 0:
#     r = num % 2
#     num = num // 2
#     yerkuakan = yerkuakan * 10 + r
# print(yerkuakan)
# How to make it Reversed
# rev = 0
# while yerkuakan > 0:
#     r = yerkuakan % 10
#     yerkuakan = yerkuakan // 10
#     rev = rev * 10 + r
# print(rev)
#----------------------------------------------
# this is the Correct code
deci = int(input('enter deci num: '))
binar = ''
while deci > 0:
    r = deci % 2
    deci = deci // 2
    binar = str(r) + binar
print('bin', binar, 'binar')