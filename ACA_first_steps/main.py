# CSV Functions check them up
# vim?  terminal based
# pop install jupiter notebook
# pypi.org
# vga to hdmi



def func(my):
    if my == []:
        return []
    elif type(my[0]) == int:
        return [my[0]] + func(mylist[1:])
    else:
        return func(my[0]) + func(my[1:])



mylist = [1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]

print(func(mylist))