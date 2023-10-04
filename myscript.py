#Getting input from user and converting them into integer
x = int(input("Give your first number: "))
y = int(input("Give your second number: "))

#allow user to choose action, and convert action number into integer
choose = int(input("Please choose 1 for addition, 2 for subtraction, 3 for multplication, 4 for divide: "))


#Action condition based on the user input

if choose == 0:
    print("Invalid Number!! Please choose the number for action. Quitting Program, Run Again")
elif choose == 1:
    def add():
        return x + y
    print("The sum of given two numbers is:", add())

elif choose == 2:
    def subtract():
        return x - y
    print("The difference of given two numbers is:", subtract())

elif choose == 3:
    def multiply():
        return x * y
    print("The product of given two numbers is:", multiply())

elif choose == 4:
    def divide():
        return x / y
    print("The division of given two numbers is:", divide())
    




