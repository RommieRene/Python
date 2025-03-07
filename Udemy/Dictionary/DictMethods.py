dict1 = {101:'Production', 102:'Accounts', 103:'Sales & Marketing', 104:'Inventory'}
dict2 = dict1.copy()
print(dict2)
dict2[102] = "Designing"
print(' dict1',dict1,'\n','dict2',dict2)
print(id(dict1[101]))
print(id(dict2[101]))
dict2 = {105:'Designing', 106:'Packaging'}
print(dict1)
dict1.update(dict2)
print(dict2)
dict2.setdefault(107)
print(dict2)
dict2.setdefault(108,'invalid value')
print(dict2)
print('')
L1 = [11,22,33,44]
dict3 = {}
dict3.fromkeys(L1)
print(dict3)
print(dict3.fromkeys(L1))
print(dict3)
print(dict3.fromkeys(L1,'value'))
# copy()
# update(iterable)
# setdefault(key,default)
# fromkeys(sequance,value)
