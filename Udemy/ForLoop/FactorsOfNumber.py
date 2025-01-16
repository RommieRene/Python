num = int(input('Enter a number to find the factors :'))

for index in range(1,num + 1,1):
    if num % index == 0:
        print(index,'The number is Factor of ',num)