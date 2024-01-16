number = input('number:')
# divisores = []
if not number.isdigit():
      print('number is not digit')
else:
      for n in range(2, int(number) // 2):
        if int(number) % n == 0:
            break

        else:
            print(number, 'is prime number')


#               divisores.append(n)
#         else:
#             pass
# if len(divisores) ==0 :
#     print("prime")
# else:
#     print("not prime")
#
