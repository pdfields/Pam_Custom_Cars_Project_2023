# Welcome message enclosed in 'equal signs'
print("=================")
print("Welcome to the UMBC")
print("Car Customization Form!")
print("=================")
# 2 blank lines for formatting
print()
print()
# Ask customer for Make & Model choice
print("For multiple choice problems, please enter the letter of the selection you're looking for")
print("~ Make & Model ~")
print("1. What model of car are you ordering?")
print("a. Lightning Speedster")
print("b. Eco Leaf")
print("c. Harp Chord")
print("d. Chevron Jolt")
# retrieve and store answer in modelOption variable
modelOption = input("Please enter 'a' - 'd': ")
# blank line for formatting
print()
# Ask customer if they prefer 2-door or 4-door option
print("2. Would you like to upgrade from the 4-door option to the 2-door option?")
# retrieve and store answer in doorsUpgrade variable
doorsUpgrade = input("Please enter 'yes' or 'no': ")
# blank line for formatting
print()
# Ask customer for color preference
print("3. What color would you like your car to be? ")
# retrieve and store answer in desiredColor variable
desiredColor = input("You may enter the name of any color you'd like: ")
# blank line for formatting
print()
print("4. Would you like the deluxe weather package?")
# retrieve and store answer in deluxeWeather variable
deluxeWeather = input("Please enter 'yes' or 'no': ")
# blank line for formatting
print()
print("5. Which engine would you like your car to have?")
print("a. I-4 Entry Engine")
print("b. V-6 Performance Engine")
print("c. Eco Diesel Engine")
# retrieve and store answer in engineOption variable
engineOption = input("Please enter 'a' - 'c': ")
# blank line for formatting
print()
print("6. Would you like heated seats?")
# retrieve and store answer in heatedSeats variable
heatedSeats = input("Please enter 'yes' or 'no': ")
# blank line for formatting
print()
print("7. Would you like a sunroof?")
# retrieve and store answer in sunRoof variable
sunRoof = input("Please enter 'yes' or 'no': ")
# 2 blank lines for formatting
print()
print()
# Display summary of all the customer's selections
print("=============")
print("~ Summary ~")
print(f"Model Option: {modelOption}")
print(f"Upgrade to 2-door: {doorsUpgrade}")
print(f"Desired Color: {desiredColor}")
print(f"Upgrade to Deluxe Weather Package: {deluxeWeather}")
print(f"Engine Option: {engineOption}")
print(f"Upgrade to Heated Seats: {heatedSeats}")
print(f"Sunroof option: {sunRoof}")
