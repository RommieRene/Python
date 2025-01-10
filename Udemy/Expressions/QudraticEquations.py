import math

a = float(input('Enter : '))
b = float(input('Enter : '))
c = float(input('Enter : '))

root1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
root2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

print(f"Roots are {root1} {root2}")