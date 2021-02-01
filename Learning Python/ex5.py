name = 'Dan Bingaling'
age = 25 
height = 176.784 # cm
weight = 69.85 # kg 
eyes = 'Brown' # eye colour 
teeth = 'Stained' # 50 shades of yellow
hair = 'Purple'
weight_in_stone = weight / 6.35
height_in_ft = height / 30.48

# use round() to round up a decimal/equation  

print(f"Let's talk about {name}.")
print(f"She's {height} centimeters tall, which in feet is {height_in_ft}.")
print(f"She's {weight} kilos heavy, which amounts to {weight_in_stone} stone.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} due to all the tea.")

# this line is tricky, try to get it exactly right
total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get {total}.")

