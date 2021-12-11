class Animal:

    def __init__(self):
        pass


class Dog(Animal):

    def __init__(self):
        self.species = "Dog"
    
    def cry(self):
        print("Bark")

class Cat(Animal):

    def __init__(self):
        self.species = "Cat"
    
    def cry(self):
        print("Meow")
