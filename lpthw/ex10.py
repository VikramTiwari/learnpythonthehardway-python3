tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# mix some things up
formatter = '{} {} {}'

hi = '''
How you doing?
\v\a'''
hello = '\tHola! How\'s \"it\" going?'
bye = "\nGotta go! Bye."

print(formatter.format(hi, hello, bye))
