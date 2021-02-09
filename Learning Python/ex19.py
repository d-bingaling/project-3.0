# Exercise 16 - Functions and Varibales 

# defining the function 
# setting 2 arguements 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

# setting the variable values that are passed in the function above.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# seeing different variable to run in the function
print("Or, we can use varibales from our script:")
amount_of_cheese = 10 
amount_of_crackers = 50 

# changing the function values to use new variables 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# changing the values again, this time to preform maths.
print("We can even do maths inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# combining the variables set previously with maths. 
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



# own function 


def party_drinks(wine_amount, no_of_glasses):
    print(f"In total we have {wine_amount} bottles of wine, and {no_of_glasses} glasses!")
    print("Do you think that will be enough for the party?")
    print(f"I reckon {wine_amount} bottles should be plently!")


party_drinks(30, 60)


bottles_of_wine = 50 
wine_glass_amount = 75 

party_drinks(bottles_of_wine, wine_glass_amount)