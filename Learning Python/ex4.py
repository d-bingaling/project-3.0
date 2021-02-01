# car quantity
cars = 100 
# avaliable space in the car 
space_in_a_car = 4.0 
# amount of drivers 
drivers = 30 
# amount of passengers 
passengers = 90 
# cars that are not being driven
cars_not_driven = cars - drivers 
# cars being driven 
cars_driven = drivers 
# capool capacity 
carpool_capacity = cars_driven * space_in_a_car
# average passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars avaliable.")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
