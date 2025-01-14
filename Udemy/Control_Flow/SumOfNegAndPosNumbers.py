sum_of_nums = int(input('Enter a Number of Numbers: '))
sum_of_positive = 0
sum_of_negative = 0

count = 0
while count < sum_of_nums:
    n = int(input("Enter your numbers: "))
    if n > 0:
        sum_of_positive= sum_of_positive + n
    else:
        sum_of_negative = sum_of_negative - n
    count = count + 1
print("positive sum is ",sum_of_positive)
print("negative sum is ",sum_of_negative)
