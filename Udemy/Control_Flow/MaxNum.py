sum_of_nums = int(input('Enter a Number of Numbers: '))
summ = 0
count = 0

while count < sum_of_nums:
    n = int(input("Enter your numbers: "))
    if n > summ:
        summ = n
    count += 1

print("max given number is ",summ)