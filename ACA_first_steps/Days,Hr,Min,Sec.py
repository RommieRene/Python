second = int(input('seconds: '))
print(
    second, 'seconds =', second//86400, 'days + ',
    second % 86400//3600, 'hours +',
    second % 86400 % 3600//60, 'minutes +',
    second % 60, 'seconds'
      )
