num = int(input('Enter a Prime Number: '))

count = 0
for index in range(1,num+1):
    if num % index == 0:
        count += 1
if count == 2:
    print("Its a Prime ")
else:
    print('Its Not Prime')