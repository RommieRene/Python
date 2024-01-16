import math

radius = int(input('Enter the radius of the sphere: '))

surface_area = 4 * math.pi * radius ** 2
volume = 4 / 3 * math.pi * radius ** 3

print(f"Radius of sphere is {radius}"
      f", Surface area is {surface_area}"
      f", Volume is {volume}")