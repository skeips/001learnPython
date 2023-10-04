
#The program you provided is a simple calculator that allows the user to perform one of four mathematical operations on two integer inputs.

#Defining operation Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Get input from user and convert them into integer, if user enter invalid number then exit the program

try:
    x = int(input("Give your first number: "))
    y = int(input("Give your second number: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Allow user to choose action, and convert action number into integer
try:
    choose = int(input("Please choose 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
except ValueError:
    # User entered nothing
    choose = None

# Validate user input
if choose is None:
    print("Please enter a valid number for the action.")
elif choose < 1 or choose > 4:
    print("Please enter a number between 1 and 4 for the action.")
else:
    # Perform the selected action
    if choose == 1:
        print("The sum of the given two numbers is:", add(x, y))
    elif choose == 2:
        print("The difference of the given two numbers is:", subtract(x, y))
    elif choose == 3:
        print("The product of the given two numbers is:", multiply(x, y))
    elif choose == 4:
        print("The division of the given two numbers is:", divide(x, y))
