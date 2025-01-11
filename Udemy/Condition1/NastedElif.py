jhone = int(input("Enter Jhone's Age: "))
smith = int(input("Enter Smith's Age: "))
ajay = int(input("Enter Ajay's Age: "))

if jhone > smith and jhone > ajay:
    print(f'Jhone is eldar')
elif smith > ajay:
    print(f'Smith is eldar')
else:
     print(f'Ajay is eldar')