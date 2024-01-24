# polymorphism means same method is used by different classes

class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("car moving")
class Boat():
    def __init__(self):
        pass
    def move(self):
        print("Boat is moving")
class Plane():
    def __init__(self):
        pass
    def moving(self):
        print("Plane is moving")
# here move method is used by both classes i,es Car,Boat,Plane
#that is called polymorphism

