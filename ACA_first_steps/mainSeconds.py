
word = input( "Enter your Word here with upper case: ").strip()
#(word length >= 4 ):
word = word.lower()
word = word[-2:] + word[2:-2] + word[:2]
print( word )