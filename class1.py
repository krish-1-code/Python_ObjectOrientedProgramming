#Classes and objects

class drinks:
    
    no_drink = 0

    def __init__(self,drink,capacity):
        self.drink = drink
        self.capacity = capacity
        drinks.no_drink += 1

    def describe(self):
        print(f"I am drinking a {self.capacity} ml {self.drink}. {drinks.no_drink}")

    
drink1 = drinks("monster",500)
print(f"This is my {drinks.no_drink}")
drink1.describe()
print(drink1)