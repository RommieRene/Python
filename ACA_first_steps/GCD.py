def  Great_CD(num1,num2):
    list_1 = set()
    list_2 = set()
    for i in range(1, num1, 1):
        if num1 % i == 0:
            list_1.add(i)
        else:
            pass
    for y in range(1, num2, 1):
            if num2 % y == 0:
                list_2.add(y)
    return max(list_1 & list_2)

user_1 = int(input('write number please: '))
user_2 = int(input("write number please: "))
print(Great_CD(user_1,user_2))




# -----------------------------




