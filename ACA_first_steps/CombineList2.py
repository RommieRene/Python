coffe_shop = ['isecreem', 'capuchino', 'kaffa', 'royal armenia', 'tea', 'green tea', 'rdftgyvbhjn', 'fgyhbjk', 'gfchj']
price = ['100', '120', '150', '200', ' 300', '350']
menu = {}
for i in range(0, len(coffe_shop), 1):
    if i < len(price):
        menu.update({coffe_shop[i]: price[i]})
    else:
        menu[coffe_shop[i]] = None
print(menu)
