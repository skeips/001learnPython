# import math

# def area():
#     print('Welcome To The Area Calculator!!')
#     user_shape = input('Please type your desired shape (eg. Rectangle, Square, Triangle etc): ').lower()
#     print(user_shape)
#     if user_shape == 'square':
#         side = int(input('Please input the side of your square: '))
#         result = side ** 2
#         print("The area of square is:",result)

#     elif user_shape == 'rectangle':
#         width = int(input('Please input the width of your rectangle: '))
#         height = int(input('Please input the height of your rectangle: ')) 
#         result = width * height
#         print("The area of rectangle is:",result)
        
#     elif user_shape == 'triangle':
#         base = int(input('Please input the base of your triangle: '))
#         height = int(input('Please input the height of your triangle: ')) 
#         result = 0.5 * base * height
#         print("The area of triangle is:",result)

#     elif user_shape == 'circle':
#         radius = int(input('Please input the radius of your circle: '))
#         result = math.pi * (radius ** 2)
#         print("The area of cicle is:",result)

#     else:
#         print("Did you choose the right shape?")

# def volume():
#     print('Welcome To The Volume Calculator!!')
#     user_shape = input('Please type your desired shape (eg. cube, cylinder, sphere etc): ').lower()
#     print(user_shape)
#     if user_shape == 'cube':
#         side = int(input('Please input the side of your cube: '))
#         result = side ** 3
#         print("The volume of cube is:",result)

#     elif user_shape == 'cylinder':
#         radius = int(input('Please input the radius of your cylinder: '))
#         height = int(input('Please input the height of your cylinder: '))
#         result = math.pi * (radius ** 2) * height
#         print("The volume of cyclinder is:",result)

#     elif user_shape == 'sphere':
#         radius = int(input('Please input the radius of your sphere: '))
#         result = 1.33 * math.pi * (radius ** 3)
#         print("The volume of sphere is:",result)

#     else:
#         print("Did you choose the right shape?")




# print("Welcome to the area, volume calculator")
# ask_user = input("What calculation do you want to perform, area or volume: ").lower()
# print('You chose to perform:', ask_user)

# if ask_user == 'area':
#     area()
# elif ask_user == 'volume':
#     volume()
# else:
#     print("Did you choose the right operation?")




# This program is a simple area and volume calculator.
# It allows the user to choose the shape they want to calculate the area or volume of,
# and then prompts them for the necessary dimensions.
# The program then calculates the area or volume and prints the result to the console.

import math

def area():
  """Calculates the area of a shape.

  Args:
    None.

  Returns:
    None.
  """

  print('Welcome To The Area Calculator!!')
  user_shape = input('Please type your desired shape (eg. Rectangle, Square, Triangle etc): ').lower()
  print(user_shape)

  if user_shape == 'square':
    side = int(input('Please input the side of your square: '))
    result = side ** 2
    print("The area of square is:",result)

  elif user_shape == 'rectangle':
    width = int(input('Please input the width of your rectangle: '))
    height = int(input('Please input the height of your rectangle: '))
    result = width * height
    print("The area of rectangle is:",result)

  elif user_shape == 'triangle':
    base = int(input('Please input the base of your triangle: '))
    height = int(input('Please input the height of your triangle: '))
    result = 0.5 * base * height
    print("The area of triangle is:",result)

  elif user_shape == 'circle':
    radius = int(input('Please input the radius of your circle: '))
    result = math.pi * (radius ** 2)
    print("The area of cicle is:",result)

  else:
    print("Did you choose the right shape?")


def volume():
  """Calculates the volume of a shape.

  Args:
    None.

  Returns:
    None.
  """

  print('Welcome To The Volume Calculator!!')
  user_shape = input('Please type your desired shape (eg. cube, cylinder, sphere etc): ').lower()
  print(user_shape)

  if user_shape == 'cube':
    side = int(input('Please input the side of your cube: '))
    result = side ** 3
    print("The volume of cube is:",result)

  elif user_shape == 'cylinder':
    radius = int(input('Please input the radius of your cylinder: '))
    height = int(input('Please input the height of your cylinder: '))
    result = math.pi * (radius ** 2) * height
    print("The volume of cyclinder is:",result)

  elif user_shape == 'sphere':
    radius = int(input('Please input the radius of your sphere: '))
    result = (4/3) * math.pi * (radius ** 3)
    print("The volume of sphere is:",result)

  else:
    print("Did you choose the right shape?")


print("Welcome to the area, volume calculator")
ask_user = input("What calculation do you want to perform, area or volume: ").lower()
print('You chose to perform:', ask_user)

if ask_user == 'area':
  area()
elif ask_user == 'volume':
  volume()
else:
  print("Did you choose the right operation?")
