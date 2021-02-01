
# setting a variable that passes 4 arguements
formatter ="{} {} {} {}"

# format is a function that is compiling this data as a string
print(formatter.format(1, 2, 3 ,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("I'm not 100%", "on what this formatter is doing,", "but i'll keep going,", "keep pushing on"))

# Pass to format four arguments, which match up with the four {} in the formatter variable. This is like passing arguments to the command line command format.

# The result of calling format on formatter is a new string that has the {} replaced with the four variables. This is what print is now printing out.


