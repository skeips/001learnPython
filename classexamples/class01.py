class Country:
    def __init__(self, name='Unspecified', population = None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def size_miles_sq(self, conversion_rate = 0.621371):
        return self.size_kmsq * conversion_rate ** 2
    
    def __str__(self):
        label = self.name
        if self.population:
            label = f'{label}, population: {self.population}'
        if self.size_kmsq:
            label = f'{label}, size_kmsq: {self.size_kmsq}'
        return label
    
chad = Country(name='Chad', population=100)

print(chad)