from calculator.calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    print("2 + 3 =", calc.add(2, 3))
    print("10 - 4 =", calc.subtract(10, 4))
    print("3 * 5 =", calc.multiply(3, 5))
    print("10 / 2 =", calc.divide(10, 2))
