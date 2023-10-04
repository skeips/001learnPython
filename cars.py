import random
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


    def run(self):
        print(f"The {self.make} car is Running.") 


    def stop(self):
        print(f"the {self.make} car stopped.")


Traffic_lights = ["R", "Y", "G"]

my_car = Car("Toyota", "Crown")

while (True):
    my_car.run()
    random_lights = random.choice(Traffic_lights)
    if random_lights == 'R':
        ask_user = input("The Traffic light turned Red. Do you want to stop your car (y/n): ").lower()
        if ask_user == 'y':
            my_car.stop()
            break

    if random_lights == 'Y':
        continue

    if random_lights == 'G':
        my_car.run()

   