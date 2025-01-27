# s1[start:end:step]
s1 = "Hello World"
print(s1[0:9:3])
print(s1[0:len(s1):1])
print(s1[:len(s1):1])
print(s1[::1])
print(s1[::])
print(s1[3::])
print(s1[6::])
print(s1[6:8])
print(s1[::2])
print(s1[::-1])
print(s1[-1:-len(s1)-1: -1])
print(s1[-1::-1])
print(s1[-1::-2])

# in not in
print('H' in s1)
print('h' in s1)
print('me' in s1)
print('me' not in s1)
