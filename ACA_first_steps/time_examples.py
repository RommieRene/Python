with open('generators (1).txt','r') as new:

    with open('new_file_text.txt','w') as new_text:
        for inx,line  in enumerate(new, start=1):
             new_text.write(f'{inx},{line}')

from collections import Counter, defaultdict

with open('generators (1).txt','r') as new:
    new_list = new.read().lower().split()
    print(defaultdict , Counter(new_list))

    count = {}
    new_dict = {}
    
    for letter in new_list:
        if letter not in count:
            count[letter] = 0
        count[letter] += 1
print(Counter(count))
print('------------------------')
value = count.values()

print(count)
for x, z in count.items():
    if z == max(value):
        new_dict.update({x: z})
print(new_dict)
