amount = int(input('Enter the Amount: '))

if amount <= 1000:
    amount -= amount * 0.10
    print(f'you get 10% discount {amount}')
elif amount <= 5000:
    amount -= amount * 0.20
    print(f'you get 20% discount {amount}')
elif amount <= 10000:
    amount -= amount * 0.30
    print(f'you get 30% discount {amount}')
elif amount > 10000:
    amount -= amount * 0.50
    print(f'you get 50% discount {amount}')
