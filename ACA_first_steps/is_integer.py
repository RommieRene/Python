def is_integer(number)->bool:
    clean_whitespace =number.strip()
    is_number = set('0123456789')
    if set(clean_whitespace) & is_number == set():
        return False
    if set(clean_whitespace[0]) <= set('-'):
        return  set(clean_whitespace[1:]) <= is_number
    else:
        return set(clean_whitespace) <= is_number

while True :
        something = input("numbers: ")
        print(is_integer(something))










