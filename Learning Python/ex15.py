from sys import argv

# expected arguements to be entered in the command line, in this case it's the script name and file name
script, filename = argv

# setting txt to open 'filename'
txt = open(filename)

# printing the filename 
print(f"Here's your file {filename}:")

# printing the text in the file in a read format
print(txt.read())

print("Type the filename again:")
# expecting an input from the command line of the filename
file_again = input("> ")
# setting txt_again to open file_again
txt_again = open(file_again)

# printing the open file by calling txt_again
print(txt_again.read())


