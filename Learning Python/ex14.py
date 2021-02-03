# Exercise 14 - Prompting and Passing


from sys import argv

script, user_name, mobile_num = argv

# This prints at the start of each prompt 
prompt = '• '

# Taking input from the command line and using it in the print statements.
print(f"Hi {user_name}, I'm the {script} script.")
print(f"I might call you later, are you sure {mobile_num} is the correct number to contact you on?")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# variable input 
likes = input(prompt)

print(f"Where do you live {user_name}?")
# variable input 
lives = input(prompt)

print("What kind of computer do you have?")
# variable input 
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")