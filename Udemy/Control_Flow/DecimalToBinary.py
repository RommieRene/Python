num = int(input("Enter number"))
yerkuakan = 0

while num > 0:
    r = num % 2
    num = num // 2
    yerkuakan = yerkuakan * 10 + r
print(yerkuakan)
rev = 0
while yerkuakan > 0:
    r = yerkuakan % 10
    yerkuakan = yerkuakan // 10
    rev = rev * 10 + r
print(rev)