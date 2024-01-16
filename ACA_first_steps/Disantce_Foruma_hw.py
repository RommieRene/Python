import math

x_a = 14
x_b = 2
y_a = -3
y_b = 5

D = math.sqrt(
    (x_a - x_b) ** 2
    + (y_a - y_b) ** 2
)
print(
    f'The distance between A ( {x_a}, {x_b} ) & B ( {y_a}, {y_b} ) is', D, 'units.'
)
