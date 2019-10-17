class Calculator:
    def __init__(self):
        print("spawned calculator")

    def add(self, a, b):
        return a+b

    def difference(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b

class ScienceCalculator(Calculator):
    def power(self, a, b):
        out = a
        for i in range(b - 1):
            out *= a
        return out

calc = ScienceCalculator()
print ("2 * 3 = " + calc.multiply(2, 3).__str__())
print ("2 ^ 3 = " + calc.power(2, 3).__str__())