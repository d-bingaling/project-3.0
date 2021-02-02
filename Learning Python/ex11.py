# EXERCISE 11 - taking an input and changing it into an output.

# Parameter = prompt - Description = A String, representing a default message before the input.
print("How old are you?", end=' ')
age = input()

# use the prompt parameter to write a message before the input.
print("How tall are you in centimeters?", end=' ')
height = int(input())

print("How much do you weigh?", end=' ')
weight= input()

convert_to_inches = (height / 30.48)

print(f"So you're {age} old, {height} tall and {weight} heavy.")

print(f"You are {height} in centimeters, which makes you {convert_to_inches} in feet")


print("How do you identify (gender)?", end=' ')
gender_identity = input()

print("What colour is your hair?", end=' ')
hair_colour = input()


print("What colour are your eyes?", end=' ')
eye_colour = input()

print("What's your favourite food?", end=' ')
fave_food = input()

print(f"You're a strong independant {gender_identity} human, with {hair_colour}, {eye_colour} eyes who enjoys eating a lot of {fave_food}.")



print("How are you feeling today?", end=' ')
emotion_input = input()

print("What music do you enjoy listening to?", end=' ')
music_input = input()

print("What is your beverage of choice?", end=' ')
beverage_input = input()

print(f"So I hear you're feeling {emotion_input} today, why don't you put a bit of {music_input} on and turn that shit up, then enjoy a cheeky {beverage_input}!")

#Jumped the gun abit here, we haven't done the if statement's yet.
#print("Did you hear about fight club?")
#fight_club = input()

#if fight_club == "yes":
 #   print("Oh really?, we're gonna have to do something about that")
#else: 
 #   print("Good, that's what I thought.")
