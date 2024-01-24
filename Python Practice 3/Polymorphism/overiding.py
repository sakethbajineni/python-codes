# when we use the same method name in the super class and subclasss the overiding occures to avoid it we use super keyword
class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("car moving")
class Boat(Car):
    def __init__(self):
        pass
    def move(self):
        print("Boat is moving")
class Plane(Car):
    def __init__(self):
        pass
    def move(self):
        print("Plane is moving")

# here method overriding will occure to avoid this we use superkeyword


class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("car moving")
class Boat(Car):
    def __init__(self):
        pass
    def move(self):
        print("Boat is moving")
class Plane(Car):
    def __init__(self):
        pass
    def move(self):
        print("Plane is moving")

