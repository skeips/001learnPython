
#This program spins a fan until the user tells it to stop.

# It does this by first setting the fan state to "on". Then, it enters a loop that spins the fan for 5 times and then asks the user if they want to stop the fan. If the user says yes, the function slows down the fan and then turns it off completely. If the user says no, the function continues spinning the fan again for 5 times.

# The loop continues until the user tells the function to stop spinning the fan, or until the fan state is changed to something other than "on".

fan_state = "on"

while fan_state == "on":
    # Spin the fan
    for i in range(5):
        print("The fan is spinning...", i + 1)

    # Ask the user if they want to stop the fan
    user_input = input("Do you want to stop the fan? (y/n): ")

    # If the user wants to stop the fan, slow it down and then stop it completely
    if user_input == "y":
        print("You chose to turn off the fan.")
        for i in range(3):
            print("The fan is slowing down...", i + 1)

        print("The fan stopped completely.")

        # Ask the user if they want to turn the fan back on
        user_input = input("Do you want to turn the fan on again? (y/n): ")

        # If the user wants to turn the fan back on, set the fan state to "on"
        if user_input == "y":
            fan_state = "on"

        # Otherwise, break out of the loop and turn the fan off
        else:
            break

    # If the user doesn't want to stop the fan, continue spinning it
    else:
        continue

# If the loop is exited, the fan is off
print("The fan is off.")


       
    


    
        
        

