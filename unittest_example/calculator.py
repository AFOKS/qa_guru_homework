class Calculator:

    def add(self, a, b):
        print(f"Складываем {a} + {b}")
        return a + b

    def subtract(self, a, b):
        print(f"Вычитаем {a} - {b}")
        return a - b

    def multiply(self, a, b):
        print(f"Умножаем {a} * {b}")
        return a * b

    def divide(self, a, b):
        print(f"Делим {a} / {b}")

        if b == 0:
            raise ZeroDivisionError("На ноль делить нельзя")

        return a / b