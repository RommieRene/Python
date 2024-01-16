def is_integer(number)->bool:
    clean_whitespace =number.strip()
    only_whitespace = set(' -')
    is_minus = set('-')
    is_number = set('0123456789')
    if set(clean_whitespace) <= only_whitespace:
        return False
    elif set(clean_whitespace[0]) <= is_minus:
        if set(clean_whitespace[1:]) <= is_number:
            return True
        else:
            return False

    elif set(clean_whitespace) <= is_number:
        return True
    else:
        return False



something = input("type any number here: ")
print(is_integer(something))
# ---------------------------------------------
# sum of numbers
sum_numbers = ("10 abc 20 de44 30 -55fg 40")
new_list = []
for i in sum_numbers:
    if set(i) <= set('abcdefghijklmnopqrstuvwxyz'):
        pass
    else:
        new_list.append(i)
        this_list = ''.join(new_list).split()
print(sum(map(int,this_list)))





