# s1 = 'qwertyuiopasdfghjklzxcvbnm'
# s2 = sorted(s1)
# ss = ''.join(s2)
# print(ss)
# ----------------------------------------------
# item = input("Enter the Item: ")
# price = input("Enter the Price: ")
#
# total_len = len(item) + len(price)
#
# dots = '.' * (25 - total_len)
# print(item+dots+price)
# -----------------------------------------------
# password = input('Enter password: ')
# repeat_password = input('Repeat Password: ')
#
# if password == repeat_password:
#     print("Correct Password")
# else:
#     if password.casefold() == repeat_password.casefold():
#         print("Please Check the Chars and repeat again ")
#     else:
#         print("Wrong password")
#----------------------------------------------------
# cardNo =  input("Enter Card Number: ")
# lastDidgits = cardNo[15::]
# four = '*' * 4
# dispno = four * 3 + lastDidgits
# print(dispno)
# ---------------------------------------------------
# emailid = input('Enter Email ID : ')
# atrate = emailid.find('@')
# print(atrate)
# print('email Id is: ',emailid[:atrate])
# print('domain name is: ', emailid[atrate+1:])
# ---------------------------------------------------
# s1 = input('Enter a string: ')
# rev = s1[::-1]
# print(s1 + rev)
# if s1 == rev:
#     print("Palindrome")
# else: print("Not a Palindrome")
#------------------------------------------------------
# mydate = input("Enter a Date in dd/mm/yyyy form: ")
# l = mydate.split('/')
# print(('Day: ', l[0]))
# print(('Month: ', l[1]))
# print(('Year: ', l[2]))
# -------------------------------------------------------
# s1 = input("Enter a string: ")
# s2 = input('Enter a second String: ')
#
# if len(s1) != len(s2):
#     print("Not Anagram")
# else:
#     for x in s1:
#         if x not in s2:
#             print("Not Anagram ")
#             break
#     else:
#         print("Anagram")
#----------------------------------------------------------
# str1 = "AbcDEfgHi"
# lower = ''
# upper = ''
# for x in str1:
#     if x.islower():
#         lower += x
#     else:
#         upper += x
# str2 = upper + lower
# print(str2)
# ------------------------------------------------------------
# punct = '''!()-[]{};:'",<>./?@#$%^*_~'''
# s1 = '[my_python@gmail.com]'
# s2 = ''
# for x in s1:
#     if x not in punct:
#         s2 = s2 + x
# print(s2)
# ------------------------------------------------------
