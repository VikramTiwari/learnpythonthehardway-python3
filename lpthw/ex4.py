# assign 100 to cars
cars = 100
# assign 4.0 to space in a car
space_in_a_car = 4.0
# assign 30 drivers
drivers = 30
# assign 90 to passengers variable
passengers = 90
# get cars not driven by subtracting cars with drivers but using variables
cars_not_driven = cars - drivers
# assing value of a variable with another variable
cars_driven = drivers
# do operations on the variables and assign result to a new variable
carpool_capacity = cars_driven * space_in_a_car
# do operations on the variables and assign result to a new available
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study drill

# Error by Zed

# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# Error is on line 8 of file ex4.py
# Zed forgot to define car_pool_capacity
# But it is a typo since the variable previously declated is carpool_capacity
# But even if he corrected it, the mathematical result will be still wrong until he fixes the equation
# correct equation is average_passengers_per_car = passengers / cars_driven

# if space_in_a_car is 4 and not 4.0 then all the equations involving space_in_a_car do not result in a floating point value
# this means that carpool_capacity would be 120 rather than 120.0

