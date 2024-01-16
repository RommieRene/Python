# def find_single_element(numbers):
#     ones = 0
#     twos = 0
#     for num in numbers:
#         twos |= (ones & num)
#         ones ^= num
#         common_bits_mask = ~(ones & twos)
#         ones &= common_bits_mask
#         twos &= common_bits_mask
#     return ones
#
#
# numbers = [2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
# single_element = find_single_element(numbers)
# print(single_element)



number = 123456
while number>10:


    tver = list(str(number))


    for i in tver:
        total = 0
        total +=int(i)
        number = total

print(number)
