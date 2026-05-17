#multiple inheritence:
#- inheritating ftom multiple classes.

class life:
    def __init__(self, alive, location):
        self.alive = alive
        self.location = location

class animal:
    def breath(self):
        print(f"The animal is breathing")

class dog(life,animal):
    
    def describe(self):
        print(f"Is the dog alive? {self.alive}. It lives on {self.location}")

golden = dog(True, "land")
golden.describe()
golden.breath()