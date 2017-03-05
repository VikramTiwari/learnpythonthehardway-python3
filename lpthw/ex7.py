# prints a string
print("Mary had a little lamb.")
# assigns snow to the placeholder in previous string and prints the compelte string
print("Its fleece was white as {}.".format('snow'))
# pritns a string
print("And everywhere that Mary went.")
# prints . 10 times
print("." * 10) # what'd that do?

# variable assignments
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# joins variables end1 to end6, end=' ' tells print function to use a space rather than \n as end of print statement (defualt is \n which results in line break)
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# print this after the previous statement, but since the previous one ended with space, this prints in the same line
print(end7 + end8 + end9 + end10 + end11 + end12)
