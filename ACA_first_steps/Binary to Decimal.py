
active = True
while active:
    _set = {'0','1'}
    s = list(reversed(input("Write a binary number to convert to decimal: ")))
    d = 0
    if _set & set(s):
        for i in range(0, len(s), 1):
            d += int(s[i]) * (2 ** i)
        print(d)
    elif s == list(reversed('quit')):
        active = False

    else:
        print('please enter a binary number')






