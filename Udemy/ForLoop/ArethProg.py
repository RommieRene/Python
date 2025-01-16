a = int(input('Enter a number: '))
d = int(input('Enter a difference: '))
n = int(input('Enter a number of terms: '))
for terms in range(a,a + n * d,d):
    print(terms)