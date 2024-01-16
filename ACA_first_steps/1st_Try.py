# You can change set's element numbers
list_1 = [23,23,23,23,23,23,23,23,23,23]


for i in list_1:
    if i != list_1[0]:
        print(False)
        break
else:
    print(True)

print('---------')
#You can change set's element numbers
list_1 = [23,23,23,23,23,23,23,23,23,23]


if len(set(list_1)) > 1:
    print(False)

else:
    print(True)