#we use super() when we have to inherit methods from a parentclass().


# Why normal inheritance doesn't work in some scenerio:

class devices:
    def __init__(self, screensize, Is_portable):
        self.screemsize = screensize
        self.Is_portable = Is_portable

class mobile(devices):
    def __init__(self,  brand, screensize):
        self.screemsize = screensize
        self.brand = brand

mobile1 = mobile(screensize = 8, brand = "Apple", Is_portable = True)
print(mobile.screensize())
