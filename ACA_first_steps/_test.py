# num_1 = input("enter number here : ")
# num_2 = input("type number here: ")
#
#
# print('The product of ',num_2, 'and', num_1, 'is', int( num_2 ) * int ( num_1 ) )
# name = 'Zaphod'
# heads = 2
# arms = 3
# print(f"{name} has {heads} heads and {arms} arms! ")
# n = 3
# m = 4
# print(f"{n} times {m} is {n*m}")
# weight = 0.2
# animal = 'Newt'
# print('{} kg is the weight of the {}'.format(weight, animal))
#
#
#
#
#
# Hello = "a huge sentence "
# Helloo = Hello.find('fghjk')
# print(Helloo)
# user_input = input('enter your text: ').lower()
#
# user = user_input.replace('a', '4')
# user_1 = user.replace('e', '3')
# user_2 = user_1.replace('l', '1')
# user_3 = user_2.replace('o', '0')
# user_4 = user_3.replace("s", '5')
# user_5 = user_4.replace('t', '7')
# user_6 = user_5.replace('b', '8')
#
# print(user_6)
# num1 = 25000000
# num2 = 25_000_000
# print(num1 , num2)
#
# first = int(input("write a number: "))
# second = int(input(" write a number again: "))
# result = first * second
# print(f'{first} * {second} = {result}')
#
# num1 = int(input("write a number plz: "))
#
# num = abs(num1)
#
# # print(f'the absalute value of {num1} is {num}')
# num1 = float(input('number 1: '))
# num2 = float(input('number 2: '))
# num3 =  num1 - num2
# num3.is_integer()
# print(f'the differance between {num1} & {num2} is an {num3.is_integer()}')
#
# n = 1
# while n < 10:
#     print('n',n, '< 10')
#     n = n + 1
#
# print('n == 10')
# #
# num = float(input('type something interesting here: '))
#
# while num <= 0:
#     print('thats not a positive number')
#     num = float(input('type a possitive number: '))
#     break
#
# list_1 = [23,23,23,23,23,23,23,23,23]
#
#
# if len(set(list_1)) > 1:
#     print(False)
#
# else:
#     print(True)
# ---------------------------------------------------Start
# list_2 = [23,23,23,23,23,23,23,23,23,23]
# for e in list_1:
#
#     if e == list_1[0]:
#
#         print(True)
#         break
# #     else:
#         print(True)
# #     elif i == list_1[0]:
#
#         list_2.append(i)
#         print(f'{list_2} => True')
# print(list_2)
# --------------------------------------------------------------------
# lst = []
# for i in range(100,200,1):
#     numbers = i % 7
#     if numbers == 0:
#      lst.append(i)
# print('Mmmount of numbers which can be divided with 7 between 100 & 200 is', len(lst))
# print('Numbers which can be divided with 7 between 100 & 200 are',lst)
# --------------------------------------------------------
# new_set = set()
# for i in range(10,31,1):
#      sum = i-1
#      Sum = sum + i
#      new_set.add(Sum)
# print(new_set)
#
# for e in new_set:
#      arithmatic_average= e / 2
#      print(arithmatic_average)
# ---------------------------------------------------------
# numbers_1 = [19, 83, 76, 45, 23, 95, 136, 80]
# numbers_2 = [24, 55, 78, 92, 70, 30, 48, 74]
# number_3 = []
# for i in numbers_1:
#      if i % 5 == 0 :
#           number_3.append(i)
# for e in numbers_2:
#      if e % 6 == 0:
#           number_3.append(e)
# print(number_3)
# --------------------------------------------------------
# integer = 3765128
# string = str(integer)
# my_list = list(string)
# rev = reversed(my_list)
# sitr = ''.join(rev)
# integ = int(sitr)
# print(type(integ),integ)
# ---------------------------------------------------------
# integer = 3765128
# string = str(integer)
# my_list = list(string)
#
# for i in my_list:
#     b = int(i)
#
#
#     print(b)

# for i in integer:
# -------------------------------------------------------------
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# new = list(zip(keys,values))
# # new_1 = dict(new)
# # print(new_1)
# D={}
# for key,val in new:
#     D[key]=val
#     print(D)
# --------------------------------------------------------------
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)
# a = "I like tfurles"
# b = "I like tdureys"
# c = []
#
# if len(a) != len(b):
#     print('a string has more elements then in b')
# else:
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             c.append(i)
# print(len(c))
#
# n = [
#    [ 1, 2, 3, 4, 5],        # minimum value of row is 1
#    [ 5, 6, 7, 8, 9],        # minimum value of row is 5
#    [ 20, 21, 5, 34, 100]   # minimum value of row is 20
# ]
# ssum = 0
#
# for i in n:
#     ssum += min(i)



# print(ssum)

# print(min(n[2]))
#
# tuple1 = (99,11)
# tuple2 = (88,80)
#
# tuple1,tuple2 = tuple2 , tuple1
#
# print(tuple1,'<---------tuple1, tuple2-------->',tuple2)
#
# #
# num = [9,6,4,2,3,5,7,0,1]
# for i,j in enumerate(sorted(num)):
#     if i != j:
#      print(i)

# nums = [2,7,11,15]
# target = 9
# ssum = []
# for x in nums:
#     for y in nums:
#         a = x+y
#         if a == target:
#
# print(nums[0])
#
# user_1 = int(input('write 2 numbers: '))
# user_2 = int(input("blabla: "))
#
# list_1 = set()
# list_2 = set()
# for i in range(1, user_1, 1):
#     if user_1 % i == 0:
#         list_1.add(i)
#     else:
#         pass
#
# for y in range(1,user_2,1):
#     if user_2 % y ==0:
#         list_2.add(y)
#
# print(max(list_1 & list_2))
#
# #
# #
#
#
#
# z = f(x,y)
#
#
#
#
#
#
# def sum_of_digits(num) -> int:
#     listo = 0
#     for i in range(0, len(num), 1):
#         listo += int(num[i])
#     return listo
# x = input('type a number  digits: ')
# try:
#     digital_numbers = int(x)
#     print(sum_of_digits(x))
# except ValueError:
#     print('ValueError: invalid literal for int() with base 10:',x)
#
#


# def join_numbers(n: int) -> str:
    # return '-'.join(str(i) for i in range(1, n + 1))
# def factorial(n):
#     if n == 0:
#         return 1
#
#     print('n = ', n)
#     return factorial(n - 1) * n  # factorial(0) * 1
# print(factorial(5))
# fact(5) = fact(6 * 4) * 5
# X = 'Spam'
# def func():
#     X = 'NI!'
#
#
#
# print(func())
# print(X)



# def validate_braces(braces)-> bool:
#     if list('(){}[]') == braces:
#         return True
#     elif braces == list('([{}])'):
#         return True
#     else:
#         return False
# while True:
#     someone = list(input())
#     print(validate_braces(someone))

# while True:
#      unpacking = list(input('({[]})'))
#
#      mek = list('[]')
#      yerku = list('{}')
#      yereq = list('()')
#      first, *middle, last = unpacking
#      while first+last == mek or first+last == yerku or first+last == yereq:
#          if middle == []:
#              break
#
#          first, *middle, last = middle
#      if first+last == mek or first+last == yerku or first+last == yereq:
#         print(True)
#      else:
#         print(False)
# print(middle)
# print(last)
# while True:
#     user = list(input())
#     opening = ['(','{','[']
#     closing = [')','}',']']
#     new_list = []
#     nn = []
#     for i in range(0,len(user)):
#         for j in range(0,2+1):
#             if user[i] == opening[j]:
#                 new_list.append(j)
#             elif user[i] == closing[j]:
#                 nn.append(j)
#     nnn = list(reversed(nn))
#     if new_list == nnn:
#         print(True)
#     else:
#         print(False)
#
# #recursia
# number = [12, 67, [34, 98, 9, [1, 3, 4, 5, 6], [2, 6, 7, [34, 5, 89], 0], [23, 78, 0], 8], 56, 28]
#
#
# def flatten_list(nested_list: list) -> list:
#     numbers = []
#     for i in nested_list:
#         if isinstance(i, int):
#             numbers.append(i)
#         else:
#             numbers.extend(flatten_list(i))
#     return numbers
# #
# #
# #
# print(flatten_list((number)))


# def decorator(func):
#     def wrapper():
#         print('something will happen be4 function is called')
#         func()
#         print('something will happen after function is called')
#     return wrapper
# def say_whee():
#     print('Whee')
#
# say_whee = decorator(say_whee)
#
# print(say_whee())
#
#
# def logger(fun):
#     def inner_loger(argum):
#         print(fun(argum))
#     return inner_loger()
#
#
# print(logger(CamelCase(string)))


# a = 2468
# x = 3568
# y = 9762
# z = 1234
#
# avarage = (a + x + y + z) / 4
# # print(avarage)
#
# sec = 15917
# houre = sec % 3600
# minute = houre % 60
# print(minute)


# import sys
# print(sys.version)
#
# print(dir(sys))
# print(sys.path)
# print(sys.argv)
# print((sys.maxsize))
# sys.exit()
from datetime import datetime

def get_age(birthday):

    today = datetime.today()
    try:
        birthdate = datetime.strptime(birthday, "%d.%m.%Y")
        age = today.year - birthdate.year
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age -= 1
        return age

    except ValueError:
        return None



def get_age_in_seconds(birthday):
    try:
        birthdate = datetime.strptime(birthday,"%d.%m.%Y")
        age_in_seconds = ( datetime.now() - birthdate).total_seconds()
        return int(age_in_seconds)
    except ValueError:
        return None

def get_next_birthday(birthday):







