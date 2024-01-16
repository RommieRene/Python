length = [40, 20, 30, 10, 89]
width = [6, 5, 4, 7, 8]
area = []
for i in length:
    for e in width:
        result = i * e
        area.append(result)
        print(f'area of rectangle with length {i} and  width {e} is {result}')
print(area)
print('the minimum area is ', min(area))
print('the Maximum area is', max(area))





