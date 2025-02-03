s = "hello, how are you"
s.find('o')
s.rfind('o',0,15)
s.index('o',5)
s.rindex('o',0,15)
s = 'python'
s.ljust(10)#adds extra spaces at the end of the string
# (You can add your prefered character instead of space, s.ljust(10,'*'))
s.rjust(10)#adds extra spaces at the start of the string
# (You can add your prefered character instead of space, s.rjust(10,'*'))
s.center(10)#adds extra spaces at the start and end ( Centeralizing the word )
# ( You can add your prefered character instead of space, s.center(10,*)
s.strip()#Removes space characters from the start and end of your string
# (Can remove your prefered char s.strip('*') you can mention multiple chars
s.lstrip()#Removes space characters from the start of your string
# (Can remove your prefered char s.strip('*') you can mention multiple chars
s.rstrip()#Removes space characters from the end of your string
# (Can remove your prefered char s.strip('*') you can mention multiple chars
s.capitalize()# It will generate new string and first letter will be capitalized
s.lower()# It will generate new string and all the letters will be lowwer case
s.upper()# It will generate new string and all the letters will be upper case
s.title()#It will generate new string and the word's first letter will be upper case
s.swapcase()# It will generate new string and the Upper letters will be lowered and lower letters upper
s.casefold()# is same with lower() but has differance
s.removeprefix('he')# Removes first chars
s.removesuffix('ou')# Removes last chars
s.partition('how')#Separates the given chars as a string in a tuple
s.rpartition('o')# Separates the given chars from the end as a string in a tuple

#Join Methods
s = 'a_b_c_d_e'
s1 = 'YXS'
s.replace('_',',', 3)#changes char step1: old char, step2: new char, step3: how many chars
s.join(s1)#Joins the given string puts first char of s1 to start of s then puts second char of s1 to the end of s and
#copies the s to the end of s and puts the last char of s1 ( so here will print "Ya_b_c_d_eXa_b_c_d_eS")
s.split()# Returns list of separated elements from start to the end, if you put char in split will return list separated with that char.
s.rsplit()# Returns list of separated elements from the end to the start
s.splitlines()
s.sorted()#returns Sorted list of chars in order of ascii