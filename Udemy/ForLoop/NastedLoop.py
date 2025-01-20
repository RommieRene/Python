for i in range(0,5):
    for j in range(0,5):
        print('*', end=', ')
    print('')

print('')

for i in range(0,5):
    for j in range(0,5):
        if i <= j:
            print('*', end=', ')
    print('')

print('')

for i in range(0,5):
    for j in range(0,5):
        if i >= j:
            print('*', end=', ')
    print('')
print('')
s1 ='abc'
s2 = 'xyz'
for i in s1:
    for j in s2:
        print(j, end=' ')
    print('')