a = "I like tfurles"
b = "I like tdureys"
c = []

if len(a) != len(b):
    print('a string has more elements then in b')
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            c.append(i)
print(len(c))
