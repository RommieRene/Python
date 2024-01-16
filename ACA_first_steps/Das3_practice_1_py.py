# PROBLEM 1
# Convert celsius to farenheit and kelvin

celsius = int(input('Tempearature in celsius: '))
farenheit = 9 / 5 * celsius + 32
kelvin = celsius + 273

print(f'{celsius} C is equal to {farenheit} F, {kelvin} K')


# PROBLEM 2
# Read a user input, count all 'o's in the string
# replace 'o's with 'oooo'
# and count 'o's again

word = input('Input some exepression: ')
print(word.count('o'))
new_word = word.replace('o', 'ooo')
print(new_word)
print(new_word.count('o'))


# PROBLEM 3
# Make the replacement string user defined
# from the last problem
word = input('Input some exepression: ')
letter = input('Letter to be changed: ')
print(word.count(letter))
new_word = word.replace(letter, 3 * letter)
print(new_word)
print(new_word.count(letter))


# PROBLEM 4
# Ask from user for a word
# Capitalize first 3 characters of the word
# leaving the others the same
word = input('Insert a word: ')
print(f'{word[:3].upper()}{word[3:]}')
