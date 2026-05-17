#Let's try to solve the problem of inheriting from super class (parent class) via using super()

class devices:
    def __init__(self, screensize, Is_portable):
        self.screensize = screensize
        self.Is_portable = Is_portable

class mobile(devices):
    def __init__(self,  brand, screensize,Is_portable):
        super().__init__(screensize, Is_portable)
        
        self.brand = brand

mobile1 = mobile(screensize = 8, brand = "Apple", Is_portable = True)
print(mobile1.screensize)
print(mobile1.Is_portable)