num = int(input("Enter Prime number: "))

count = 0
for index in range(1,100+1):
    if num % index == 0:
        count += 1
if count == 2:
    print(num)