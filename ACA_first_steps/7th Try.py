keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new = list(zip(keys,values))
# new_1 = dict(new)
# print(new_1)
D={}
for key,val in new:
    D[key]=val
print(D)