# import argv feature form sys module
from sys import argv

# unpack argv into script and filename
script, filename = argv

# open file and store this file variable in txt
txt = open(filename)

# print filename
print(f"Here's your file {filename}:")
# read the contents of file and print them
print(txt.read())

# print message
print("Type the filename again:")
# take filename as input value and assign to file_again
file_again = input("> ")

# open file and assing contents to txt_again
txt_again = open(file_again)

# print txt_again
print(txt_again.read())

# close files
txt.close()
txt_again.close()
print("Closed files.")
