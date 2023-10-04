import random

class Pet:
    
    def __init__(self, height):
        self.height = height

    is_human = False
    owner = 'Michael Smith'

    @classmethod
    def create_random_height_pet(cls):
        height = random.randrange(0, 100)
        return cls(height)

for I in range(5):
    pet = Pet.create_random_height_pet()
    print(pet.height)