
# coffee_types = ["Americano", "Cafe Mocha", "Cappuccino", "Cafe Latte"]
# coffee_types.sort()
# print(coffee_types)

# starter = ['Cookies', 'Biscuits', 'Cup Cake', 'Chocolava']

# both_items = [coffee_types, starter] #combining lists, nested list
# print(both_items)


# print("Here is the menu for both cofee and starter: ")
# for i in range(len(both_items)):
#     for j in range(len(both_items[i])):
#         print((both_items[i] [j]))


coffee_types = ["Americano", "Cafe Mocha", "Cappuccino", "Cafe Latte"]
starter = ['Cookies', 'Biscuits', 'Cup Cake', 'Chocolava']

# Combine the lists into a single list using list comprehension
both_items = [item for sublist in [coffee_types, starter] for item in sublist]

# Print the menu
print("Here is the menu for both coffee and starter: ")
for item in both_items:
  print(item)


