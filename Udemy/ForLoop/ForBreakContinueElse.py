for i in range(0,10):
    if i > 5:
        break
    else:
        print(i)
else:
    print('For Completed Properly')
for i in range(0,10):
    if i % 5 == 0:
        continue
    print(i)