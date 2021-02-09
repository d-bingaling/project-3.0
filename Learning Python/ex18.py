# Names, Variables, Code & Functions 

# Functions do 3 things 
    # 1. They name pieces of code the way varibales name strings and numbers.
    # 2. They take arguements the way your scripts take argv
    # 3. Using 1 and 2, they let you make your own 'mini-scripts' or 'tiny commands'.


# def is what we use to 'define' a function. Using an asterics is similar to us calling argvs 
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# it doesn't matter what you name your function, as long as it explains what you're doing
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes one arguement 
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguements
def print_none():
    print("I got nothin'.")


print_two("Dan", "Bingaling")
print_two_again("Dan", "Bingaling")
print_one("First!")
print_none()