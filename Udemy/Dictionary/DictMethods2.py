dict1 = {101:'Production', 102:'Accounts', 103:'Sales & Marketing', 104:'Inventory'}
dict2 = dict1.pop(101,'Production')
print('dict2',dict2)
print('dict1',dict1)
dict2 = dict1.pop(111,'None')
print(dict2)
dict3 = dict1.popitem()
print(dict3)
print(dict1)
dict1 = {101:'Production', 102:'Accounts', 103:'Sales & Marketing', 104:'Inventory'}
dict3 = dict1.popitem()
print(dict3)
print(dict1)
dict4 = dict1.copy()
print(dict4,'dict4')
dict4.clear()
print(dict4)
print(dict1,'dict1')
del dict1
# print(dict1) Error 