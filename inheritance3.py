#This is multilevel inheritance where a child class inherits from parent class and the parent class inherits
# from the grandparent class.

class grandparent():
    def __init__(self, height, gender):
        self.height = height
        self.gender = gender

class parent(grandparent):
    def walking(self):
        print("Walking lol")

class child(parent):
    def describe(self):
        print(f"My height is {self.height}. I am a {self.gender}")

me1 = child(188,"Male")
me1.describe()
me1.walking()
    