# This code is a program to collect and manage personal information. 
# It allows the user to input their name, contact number, email address, and location.
# The information is stored in a dictionary called my_info and can be updated if needed.
my_info = {
    "name": None,
    "contact_no": None,
    "email": None,
    "location": None
}

# Prompting the user to input their information
name = input("What is your name: ")
contact_no = input("What is your contact no.: ")
email = input("What is your email address: ")
location = input("What is your location: ")

# Assigning the input values to the corresponding keys in the dictionary
my_info["name"] = name
my_info["contact_no"] = contact_no
my_info["email"] = email
my_info["location"] = location

# Printing out the collected information
print("Here is your information: ")
for key, value in my_info.items():
    print(f"{key}: {value}")

# Function to update information
def askUpdate():
    while True:
        ask_update = int(input("Please choose the number from this list 1.name, 2.contact_no, 3.email, 4.location, 0. for quit: "))
        if ask_update == 1:
            name = input("What is your name: ")
            my_info["name"] = name
        elif ask_update == 2:
            contact_no = input("What is your contact no.: ")
            my_info["contact_no"] = contact_no
        elif ask_update == 3:
            email = input("What is your email address: ")
            my_info["email"] = email
        elif ask_update == 4:
            location = input("What is your location: ")
            my_info["location"] = location
        elif ask_update == 0:
            break
        else:
            print("Please choose correct number")

    print("Here is the updated information: ")
    for key, value in my_info.items():        
        print(f"{key}: {value}")
        

# Asking the user if they want to update their information
ask_user = input("Do you want to update your information (y/n): ").lower()
if ask_user == 'y':
    askUpdate()
else:
    exit()




