import calculator
from colored import fg,bg, attr


def addition():
        print("**add**")
        a = int(input("--> "))
        b = int(input("+   "))
        print(f"{fg('blue')}{calculator.add(a, b)}{attr('reset')}")

def subtraction():
        print("**subtract**")
        a = int(input("--> "))
        b = int(input("-   "))
        print(f"{fg('blue')}{calculator.subtract(a, b)}{attr('reset')}")

def multiplication():
        print("**multiply**")
        a = int(input("--> "))
        b = int(input("*   "))
        print(f"{fg('blue')}{calculator.multiply(a, b)}{attr('reset')}")

def division():
        print("**divide**")
        a = int(input("--> "))
        b = int(input("/   "))
        print(f"{fg('blue')}{calculator.divide(a, b)}{attr('reset')}")

def squared():
        print("**square**")
        a = int(input("--> "))
        print(f"{fg('blue')}{calculator.square(a)}{attr('reset')}")

def cubed():
        print("**cube**")
        a = int(input("--> "))
        print(f"{fg('blue')}{calculator.cube(a)}{attr('reset')}")

def power():
        print("**power**")
        a = int(input("--> "))
        b = int(input("^   "))
        print(f"{fg('blue')}{pow(a,b)}{attr('reset')}")

def simple():
        print("**simple**")
        a = int(input("Principle = "))
        b = int(input("Rate  =     "))
        c = int(input("Time  =     "))
        print(calculator.simple_interest(a,b,c))
        print(f"{fg('blue')}{calculator.simple_interest(a,b,c)}{attr('reset')}")

def compound():
        print("**compound**")
        a = int(input("Principle = "))
        b = int(input("Rate  =     "))
        c = int(input("Time  =     "))
        print(f"{fg('blue')}{calculator.compound_interest(a,b,c)}{attr('reset')}")