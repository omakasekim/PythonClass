class CantFlyError(Exception):
    def __str__(self):
        return "날개가 없어요"

class Bird:
    def __init__(self):
        pass
class Eagle(Bird):
    def __init__(self):
        pass
    def fly(self):
        print("I believe I can fly")
class Penguin(Bird):
    def __init__(self):
        pass
    def fly(self):
        raise CantFlyError

pingu = Penguin()
pingu.fly()
