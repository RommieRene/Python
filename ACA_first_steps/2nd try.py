lst = []
for i in range(100,200,1):
    numbers = i % 7
    if numbers == 0:
     lst.append(i)
print('Mmmount of numbers which can be divided with 7 between 100 & 200 is', len(lst))
print('Numbers which can be divided with 7 between 100 & 200 are',lst)

