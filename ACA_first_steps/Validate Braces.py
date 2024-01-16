while True:
    user = list(input())
    opening = ['(','{','[']
    closing = [')','}',']']
    new_list = []
    nn = []
    for i in range(len(user)):
        for j in range(0, 2+1):
            if user[i] == opening[j]:
                new_list.append(j)
            elif user[i] == closing[j]:
                nn.append(j)
    nnn = list(reversed(nn))

    if new_list == nnn:
        print(True)
    elif nn == new_list:
            print(True)
    else:
        print(False)

