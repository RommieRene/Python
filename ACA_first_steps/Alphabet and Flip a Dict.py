def alphabet(lenght_integer = 0)-> dict:
    a = {}
    list_1 = list('abcdefghijklmnopqrstuvwxyz')
    list_2 = list(range(1, 26 + 1))
    if lenght_integer == 0:
        return   dict(zip(list_1,list_2))
    else:
        for i in range(lenght_integer):
            a[list_1[i]] = list_2[i]

        return a
print(alphabet(5))

#-------------------------------------------

def flip_dict(dict_1:dict):
    list_values = dict_1.keys()
    list_keys = dict_1.values()
    return  dict(zip(list_keys,list_values))
print(flip_dict(alphabet(5)))
#-------------------------------------------

amount_of_numbers = 0
dict_name = alphabet()
amount_of_letters = list('comprehension') #<--- here can be input()
for i in amount_of_letters:
    amount_of_numbers += int(dict_name[i])
print('amount of numbers in comprehension is ',amount_of_numbers,)
#---------------------------------------------

print(sum([dict_name[i] for i in amount_of_letters]),'WooDoo')



























