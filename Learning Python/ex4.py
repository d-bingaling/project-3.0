# number of cars 
cars = 100

# how much space is in the car 
space_in_a_car = 4.0 

# how many drivers 
drivers = 30 

# number of passenger 
passengers = 90

# how many cars not being driven
cars_not_driven = cars - drivers

# how many cars are driven
cars_driven = drivers 

# carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# how many passengers per car 
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avaiable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")