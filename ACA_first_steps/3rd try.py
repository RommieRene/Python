new_set = set()
for i in range(10,31,1):
     sum = i-1
     Sum = sum + i
     new_set.add(Sum)
print(new_set)

for e in new_set:
     arithmetic_mean = e / 2
     print(arithmetic_mean, end=',')