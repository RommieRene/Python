def  List_CM(num1,num2, num3):
    list_1 = set()
    list_2 = set()
    list_3 = set()
    for i in range(1, 100, 1):

        list_1.add(num1 * i)
    for n in range(1, 100,1):
        list_3.add(num3 * n)


    for y in range(1, 100, 1):

        list_2.add(num2 * y)
    return min(list_1 & list_2 & list_3)

user_1 = int(input('write number please: '))
user_2 = int(input("write number please: "))
user_3 = int(input("write number please: "))
print(List_CM (user_1, user_2, user_3 ))