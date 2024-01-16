dict_1 = {'b': 210,
          'a': 20,
          'C': 220,
          'g': 260,
          'E': 100,
          't': 250}
max_val = max(dict.values(dict_1))
min_val = min(dict.values(dict_1))
print(dict_1.items())
for key, value in dict_1.items():

    if value == min_val:
        print(f'min value key is {key}')
    if value == max_val:
        print(f'max value key is {key}')

