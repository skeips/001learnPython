
# This program creates a list of coffee types that the user wants.
# It first prompts the user to add the defined menu to their menu.
# If the user says yes, the program adds the defined menu to the
# list of coffee types.

# The program then prompts the user to enter coffee types until they
# say no or leave their input blank. Each time the user enters a
# coffee type, the program adds it to the list of coffee types.

# Finally, the program prints the list of coffee types, with a serial
# number before each coffee type.

# The program also allows the user to delete an item from the list,
# choose a coffee type from the list, and clear the list.

# Overall, this program is a simple way to create a list of coffee types. It is easy to understand and use, and it can be customized to meet the user's specific needs.

#This program teaches you to ..
# (1) How to extend another list to your list
# (2) How to append items into your list
# (3) How to loop over your list with serial numbers before the list items
# (4) How to find out length of your list
# (5) How to remove items from your list
# (6) How to clear your list




# Define a list of coffee types.
coffee_types = []

# Define a list of defined menu items.
defined_menu = ["Americano", "Cafe Mocha", "Cappuccino", "Cafe Latte"]

# Print the defined menu.
print("Here is our menu:", defined_menu)

# Ask the user if they want to add the defined menu to their menu.
ask_to_add = input("Do you want to add this list to your menu? (y/n)").lower()

# If the user says yes, add the defined menu to their menu
if ask_to_add == "y":
    coffee_types.extend(defined_menu) #(1) extending another list

# Prompt the user to enter coffee types until they say no or leave their input blank
while True:
    user_another_input = input("Do you want to add another coffee type, y/n? ").lower()
    if user_another_input not in ["y", ""]:
        break

    coffee_type = input("Enter coffee type: ")
    coffee_types.append(coffee_type) # (2) appending items in your list



# Print the list of coffee types
print("Here is the list of your coffee types:")

#iterate coffee types and serial number before them using enumerate
# for i, coffee in enumerate(coffee_types):
#     print(f"{i + 1}. {coffee}")

# Create a list of serial numbers
serial_numbers = list(range(len(coffee_types))) # (3) counting the numbers of items in your list and creating another list for numbers

# Iterate over the coffee types and serial numbers together
for serial_number, coffee in zip(serial_numbers, coffee_types): #(3) looping over the numbers and items in your list
    print(f"{serial_number + 1}. {coffee}") #(3) printing the items with serial number before them


# Print the number of coffee types in the list.
coffee_count = len(coffee_types) # (4) length of items in your list

print(f"There are", coffee_count,  "items in your menu list")

# Ask the user if they want to delete an item from the list.
to_remove = int(input("Do you want to delete any items from your list? please specify the number or type 0 for not deleting the item : ")) - 1

# If the user enters a valid index, remove the item from the list.
if to_remove in range(len(coffee_types)):
    print(f"Removing {coffee_types[to_remove]} from the list")
    coffee_types.remove(coffee_types[to_remove]) #(5) deleting items from your list 
else:
    print("Invalid input or you type 0.")

# Print the updated list.
print("Here is the updated list:")
for serial_number, coffee in zip(serial_numbers, coffee_types):
    
    print(f"{serial_number + 1}. {coffee}")



# Ask the user which coffee type they want to taste.
print("Which coffee type do you want to taste?")
user_taste = int(input("Please choose the number? ")) - 1

# Ask the user if they want the coffee hot or cold.
coffee_temp = input("Do you want hot or cold, press enter for hot, type 'c' for cold (default is hot): ").lower()

# If the user wants the coffee cold, print a cold coffee.
if coffee_temp == "c":
    print(f"Here is your cold {coffee_types[user_taste]}")

# Otherwise, print a hot coffee.
else:
    print(f"Here is your hot {coffee_types[user_taste]}")

# Ask the user if they want to clear the list.
clear_list = input("Do you want to clear your menu list? (y/n):").lower()

# If the user says yes, clear the list.
if clear_list == 'y':
    coffee_types.clear() #6 clearing your list

# Print a farewell message.
print("ENJOY YOUR DRINK!!")

