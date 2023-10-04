class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
customer = Person('Mary', 'Lo')

# customers_fullname = customer.full_name

# print(customers_fullname)