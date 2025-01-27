s1 = 'Hello World'
print(s1[0])
print(s1[2])
print(s1[3])
print(s1[-1])
print(s1[-4])
for index in s1:
    print(index)
for index in range(0,len(s1)):
    print(index)
    print(s1[index])
for index in range(len(s1)-1,-1,-1):
    print(index)
for index in range(len(s1)-1,-1,-1):
    print(s1[index])
for index in range(len(s1)-1,-1,-1):
    print(s1[index], end='')
for index in range(0,len(s1),2):
    print(index)
    print(s1[index])