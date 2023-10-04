class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a Chinese Restaurant")
        print(f"You can enjoy {self.cuisine_type} in {self.restaurant_name} Restaurant.")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now!")


my_restarant = Restaurant('Miyang', 'Chopsey')

print(f"This is a {my_restarant.restaurant_name}")
my_restarant.describe_restaurant()


