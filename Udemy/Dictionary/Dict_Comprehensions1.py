dict1 = dict((("a",1),("b",2),("c",3)))
print(dict1)
dict2 = dict(([1,11],[2,22],[3,33]))
print(dict2)
dict2 = dict(("ab","cd","ef"))
print(dict2)
''' wrong --->dict2 = dict(([1,11,12],[2,22,23],[3,33,34]))
print(dict2)'''

L1 = [(1,2),(5,6),(8,9)]
dict2 = dict(L1)
print(L1)
print(dict2)

'''zip iterables'''
L1 = ['Price','Age','Weight']
L2 = [3000,31,120]
dict3 = dict(zip(L1,L2))
print(dict3)
'''Enumerate iterable'''
L3 = ['A','B','C']
for item in enumerate(L3):
    print(item)
dict4 = dict(enumerate(L3))
print(dict4)
dict5 = {(x,x**2) for x in range(1,5)}
print(dict5)
dict6 = dict((x,x**2) for x in range(1,5))
print(dict6)
L4 = [1,2,3]
L5 = ['a','b','c']
for i,x in zip(L4,L5):
    print(i,x)
dict7 = dict((x,i)for x,i in zip(L4,L5))
print(dict7)
dict7 = {i:x for x,i in zip(L4,L5)}
print(dict7)
L6 = ['a','b','c','d']
dict8 = dict((x,i) for i,x in enumerate(L6))
print(dict8)x