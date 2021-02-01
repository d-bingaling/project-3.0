


print("Mary had a little lamb.")

# setting {} = to snow and formatting as a string?
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# printing fullstops but * by 10, output = ..........
print("." * 10) # what'd that do?

# setting string variables
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

# watch end = ' ' at the end. try removing it to see what happens 
# combining all the varibales to spell a word, the end=' ', is setting end as a space.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# idk why that dude made me use 4 different variables for the letter e, here's me using the same one.
print(f"Reusing the same variable for 'e', {end1  + end2 + end3 + end3 + end5 + end3} ")
print(end7 + end8 + end9 + end10 + end3 + end12)