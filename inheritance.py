#Inheritance:
#when a child class has access to the attributes and methods of parent class

class houses:
    def __init__(self, color, walls):
        self.color = color
        self.walls = walls

    def describe(self):
        print(f"The {self.color} house has {self.walls} walls")

class room(houses):

    def describe(self):
        print(f"The {self.color} room has {self.walls} walls")

house1 = houses("pink",4)
house1.describe()

room1 = room("blue",6)
room1.describe()