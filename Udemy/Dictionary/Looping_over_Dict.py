dict1 = {101:'Production', 102:'Accounts', 103:'Sales & Marketing', 104:'Inventory'}
# get()
for x in dict1:
    print(x,dict1[x])
print('')
for i in dict1:
    print(i,dict1.get(i))
print('')
print(dict1[102])
print(dict1.get(104))
# print(dict1[106]) Error
print(dict1.get(106))
print('')
print(dict1.get(106,'invalid key'))
print('')
# key()
print(dict1.keys())#returns a list of keys of the dictionary
print('')
# values()
print(dict1.values())# returns a list of values of the dictionary
print('')
# items()
print(dict1.items())#Returns a list of tuple of key:value from the dictionary
print('')
for i in dict1.keys():#returns keys & values of the dictionary
    print(i,dict1[i])
print('')
for x in dict1.values():#returns values of the dictionary keys
    print(x)
print('')
for i,x in dict1.items():#returns keys & values of the dictionary
    print(i,x)
