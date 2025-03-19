# Attempting to create a calculator with basic functions

class Calculator:
    def _init_(self):
        pass
    def add(self, Num_1, Num_2):
        print(f"\nThe output of this operation is: {Num_1 + Num_2}\n")

    def subtract(self, Num_1, Num_2):
        print(Num_1 - Num_2)

    def multiply(self, Num_1, Num_2):
        print(Num_1 * Num_2)    

    def divide(self, Num_1, Num_2):
        print(Num_1 / Num_2)

calculator = Calculator()

print(f"\nWe can perform addition, subtraction, multiplication and division from here\n")

looptime = [1]

for loops in looptime:
    Num_1 = int(input(f"\nEnter first number: "))
    if Num_1 == 1999:
        break;
    Num_2 = int(input("Enter second number: "))
    if Num_2 == 1999:
        break;
    calculator.add(Num_1, Num_2)