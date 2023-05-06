import calculator
from colored import fg,bg, attr


def addition(f):
        print("**add**")
        a = int(input("--> "))
        b = int(input("+   "))
        print(f"{fg('blue')}{calculator.add(a, b)}{attr('reset')}")
        print(f"{a} + {b} = {calculator.add(a, b)}",file=f)

def subtraction(f):
        print("**subtract**")
        a = int(input("--> "))
        b = int(input("-   "))
        print(f"{fg('blue')}{calculator.subtract(a, b)}{attr('reset')}")
        print(f"{a} - {b} = {calculator.subtract(a, b)}",file=f)

def multiplication(f):
        print("**multiply**")
        a = int(input("--> "))
        b = int(input("*   "))
        print(f"{fg('blue')}{calculator.multiply(a, b)}{attr('reset')}")
        print(f"{a} * {b} = {calculator.multiply(a, b)}",file=f)

def division(f):
        print("**divide**")
        a = int(input("--> "))
        b = int(input("/   "))
        print(f"{fg('blue')}{calculator.divide(a, b)}{attr('reset')}")
        print(f"{a} / {b} = {calculator.divide(a, b)}",file=f)

def squared(f):
        print("**square**")
        a = int(input("--> "))
        print(f"{fg('blue')}{calculator.square(a)}{attr('reset')}")
        print(f"{a} * {a} = {calculator.square(a)}",file=f)

def cubed(f):
        print("**cube**")
        a = int(input("--> "))
        print(f"{fg('blue')}{calculator.cube(a)}{attr('reset')}")
        print(f"{a} * {a} * {a} = {calculator.cubed(a)}",file=f)

def power(f):
        print("**power**")
        a = int(input("--> "))
        b = int(input("^   "))
        print(f"{fg('blue')}{pow(a,b)}{attr('reset')}")
        print(f"{a} ^ {b}  = {pow(a,b)}",file=f)

def simple(f):
        print("**simple**")
        a = int(input("Principle = "))
        b = int(input("Rate  =     "))
        c = int(input("Time  =     "))
        print(calculator.simple_interest(a,b,c))
        print(f"{fg('blue')}{calculator.simple_interest(a,b,c)}{attr('reset')}")
        print(f"Principle = {a} Rate = {b} Time = {c} Interest Total = {calculator.simple_interest(a,b,c)}",file=f)


def compound(f):
        print("**compound**")
        a = int(input("Principle = "))
        b = int(input("Rate  =     "))
        c = int(input("Time  =     "))
        print(f"{fg('blue')}{calculator.compound_interest(a,b,c)}{attr('reset')}")
        print(f"Principle = {a} Rate = {b} Time = {c} Interest Total = {calculator.compound_interest(a,b,c)}",file=f)

def fibonacci(f):
        print("**fibonacci**")
        length = int(input("Enter length of sequence : "))
        num = int(input("Enter number : "))

        print([calculator.fibonacci_of(num) for n in range(length)])