dict1 = {
    "acabus":"a calculator",
    "bachelor":"unmarried person",
    "cable":"strong rope"
}
print(dict1)
print(dict1['acabus'])
print(dict1["bachelor"])

dict2 = {
    101:"Jhon",
    102:"Smith",
    103:"Mark",
    104:"Davit"
}
''' Access key:value'''
print(dict2[102])
'''Insert Key & Value'''
print(dict2)
dict2[105] = "Alex"
'''Update value'''
print(dict2)
dict2[105] = "Eric"
print(dict2)
'''Delete Key & Value'''
print(dict2)
del dict2[104]
print(dict2)

dict3 = {
    "apple":"red",
    "grapes":"green",
    "mango":"yellow"
}
for i in dict3:
    print(i)
dict4 = {
    "Name":"rene",
    "Age":31,
    "Address":"Yerevan",
    "Phone":37444120444
}
for i in dict4:
    print(i)
    print(i,":")
    print(i,":",dict4[i])
