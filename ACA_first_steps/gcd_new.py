def  g_c_d(num1,num2):
    list_1 = set()

    for i in range(1, max(num1,num2), 1):
        if num1 % i == 0 and num2 % i ==0:
            list_1.add(i)
    return max(list_1)

user_1 = int(input('write number please: '))
user_2 = int(input("write number please: "))
print(g_c_d(user_1,user_2))