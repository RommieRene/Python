n = int(input("Enter number: "))
count = 0

while n != 0:
    n = n // 10
    count += 1
print('Number of Digits are', count)