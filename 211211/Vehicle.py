class Vehicle:
    
    def __init__(self):
        self.name = "Vehicle"
    
    def say_my_name(self):
        print("I am a {}".format(self.name))

class Plane(Vehicle):
    
    def __init__(self, manufacturer, owner):
        self.name = "Plane"
        self.manufacturer = manufacturer
        self.owner = owner
        
    def manu(self):
        print("Made by {}".format(self.manufacturer))
    
    def ownedBy(self):
        print("Owned by {}".format(self.owner))
