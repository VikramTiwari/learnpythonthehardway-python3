# create a formatter with 4 placeholders
formatter = "{} {} {} {}"

# assign placeholders with numeric variables and print
print(formatter.format(1, 2, 3, 4))
# assign placeholders with string variables and print
print(formatter.format("one", "two", "three", "four"))
# assign placeholders with boolean variables and print
print(formatter.format(True, False, False, True))
# assign placeholders with formatter itself, this works cause now formatter itself is treated as plain string
print(formatter.format(formatter, formatter, formatter, formatter))
# assing string sentences to the formatter, new lines got nothing on formatter
print(formatter.format(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
