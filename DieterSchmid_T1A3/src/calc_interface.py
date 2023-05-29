
import calculator
from colored import fg,bg, attr
from fibonacci import Fibonacci
from game import Game
from equation import Equation
import re


#These functions interface with the user the print to the console and to file if the option is flagged.


#starts a game for the whole user session.
a_game = Game()

       

def addition(f):
        print("**add**")
        a = float(input("--> "))
        b = float(input("+   "))
        print(f"{fg('blue')}{calculator.add(a, b)}{attr('reset')}")
        print(f"{a} + {b} = {calculator.add(a, b)}",file=f)

def subtraction(f):
        print("**subtract**")
        a = float(input("--> "))
        b = float(input("-   "))
        print(f"{fg('blue')}{calculator.subtract(a, b)}{attr('reset')}")
        print(f"{a} - {b} = {calculator.subtract(a, b)}",file=f)

def multiplication(f):
        print("**multiply**")
        a = float(input("--> "))
        b = float(input("*   "))
        print(f"{fg('blue')}{calculator.multiply(a, b)}{attr('reset')}")
        print(f"{a} * {b} = {calculator.multiply(a, b)}",file=f)

def division(f):
        print("**divide**")
        a = float(input("--> "))
        b = float(input("/   "))
        print(f"{fg('blue')}{calculator.divide(a, b)}{attr('reset')}")
        print(f"{a} / {b} = {calculator.divide(a, b)}",file=f)

def squared(f):
        print("**square**")
        a = float(input("--> "))
        print(f"{fg('blue')}{calculator.square(a)}{attr('reset')}")
        print(f"{a} * {a} = {calculator.square(a)}",file=f)

def cubed(f):
        print("**cube**")
        a = float(input("--> "))
        print(f"{fg('blue')}{calculator.cube(a)}{attr('reset')}")
        print(f"{a} * {a} * {a} = {calculator.cube(a)}",file=f)

def power(f):
        print("**power**")
        a = float(input("--> "))
        b = float(input("^   "))
        print(f"{fg('blue')}{pow(a,b)}{attr('reset')}")
        print(f"{a} ^ {b}  = {pow(a,b)}",file=f)

def simple(f):
        print("**simple**")
        a = float(input("Principle = "))
        b = float(input("Rate  =     "))
        c = float(input("Time  =     "))
        print(calculator.simple_interest(a,b,c))
        print(f"{fg('blue')}{calculator.simple_interest(a,b,c)}{attr('reset')}")
        print(f"Principle = {a} Rate = {b} Time = {c} Interest Total = {calculator.simple_interest(a,b,c)}",file=f)


def compound(f):
        print("**compound**")
        a = float(input("Principle = "))
        b = float(input("Rate  =     "))
        c = float(input("Time  =     "))
        print(f"{fg('blue')}{calculator.compound_interest(a,b,c)}{attr('reset')}")
        print(f"Principle = {a} Rate = {b} Time = {c} Interest Total = {calculator.compound_interest(a,b,c)}",file=f)

def fibonacci(f):
        print("**fibonacci**")
        length = int(input("Enter range of sequence : "))
        fib = Fibonacci()

        print(f"{fg('blue')}{[fib(n) for n in range(length)]}{attr('reset')}")
        print(f"{[fib(n) for n in range(length)]}",file=f)

def guess_game(f):
        print("**guessing game**")
        guess = int(input("Guess the number [1-10] : "))

        print(a_game(guess))
        #no need for printing to file
        #print(a_game(guess),file=f)

def dec_to_binary(f):
       print("**Decimal to Binary**")
       a = int(input("--> "))
       print(f"{fg('blue')}{calculator.decimal_to_binary(a)}{attr('reset')}")
       print(f"{a} * {a} = {calculator.decimal_to_binary(a)}",file=f)

def dec_to_hex(f):
       print("**Decimal to Binary**")
       a = int(input("--> "))
       print(f"{fg('blue')}{calculator.decimal_to_hex(a)}{attr('reset')}")
       print(f"{a} * {a} = {calculator.decimal_to_hex(a)}",file=f)

def equation(f):

        print("***Linear Equation***")
        expr = input("Please enter your equation for x,y and z :")
        a,b,c = ['','','']
        
        try:
            if 'x' in expr: 
                a = float(input("Solve for x = "))
        except ValueError as e: 
                pass    
        
        try:
            if 'y' in expr:
                b = float(input("Solve for y = "))
        except ValueError as e: 
                pass  
        
        try:   
            if 'z' in expr:
                c = float(input("Solve for z = "))
        except ValueError as e: 
                pass  

        #Although it can use other values
        #Although it will confused the user so crash out to except
        if not a and not b and not c: raise ValueError("bad equation use 5*x + 9*y - 9*z")
        
        #use our OOP Equation class which does the validation.
        e = Equation()
        print(f"{fg('blue')}{e(expr,a,b,c)}{attr('reset')}")
        #print nice for file
        print(f"{expr} =\n x = {a}\n y = {b}\n z ={c} \n = {e(expr,a,b,c)}",file=f)

