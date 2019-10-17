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


calc = Calculator()
print("1 + 3 = " + calc.add(1, 3).__str__())
print("3 - 1 = " + calc.difference(3, 1).__str__())
print("15 / 3 = " + calc.divide(15, 3).__str__())
print("3 * 5 = " + calc.multiply(3, 5).__str__())