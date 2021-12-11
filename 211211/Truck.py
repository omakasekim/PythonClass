class Truck: #Class Definition

    def __init__(self):  # Constructor 
        self.name = "Truck"

    def say_my_name(self):  # Method
        print("I am  a {}".format(self.name))

truck1 = Truck()
truck1.say_my_name()
