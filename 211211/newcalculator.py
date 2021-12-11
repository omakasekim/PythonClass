class Calculator:

    def __init__(self, first, second):
        self.first = float(first)
        self.second = float(second)
        self.result = 0

    def printRes(self):
        print(self.result)
        self.result = 0

    def add(self):
        self.result = self.first + self.second
        self.printRes()
    def sub(self):
        self.result = self.first - self.second
        self.printRes()
    def mul(self):
        self.result = self.first * self.second
        self.printRes()
    def div(self):
        self.result = self.first / self.second
        self.printRes()
    def mod(self):
        self.result = self.first % self.second
        self.printRes()


calc = Calculator(5,0)
calc.div()


