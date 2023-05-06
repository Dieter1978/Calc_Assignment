from calc_interface import addition, guess_game, subtraction, multiplication, division, squared, cubed, power, simple, compound, fibonacci, equation
from colored import fg,bg, attr
from datetime import datetime
import sys
from pathvalidate import ValidationError, validate_filename

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

namefile = ""

# set up array for calculator choices
choices = [ (1,'addition'),
            (2,'subtraction'),
            (3,'multiplication'),
            (4,"division"),
            (5,'squared'),
            (6,'cubed'),
            (7,'power'),
            (8,'simple'),
            (9,'compound'),
            (10,'fibonacci'),
            (11,'guess_game'),
            (12,'equation'),
           
        ]

try:
    while True:
        #create menu system for user
        print(f"{fg('white')}{bg('yellow')}**** Welcome to Calcy the Calculator.****{attr('reset')}")
        print(f"{fg(135)}###########{dt_string}###########{attr('reset')}")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Squared")
        print("6. Cubed")
        print("7. To the power")    
        print("8. Simple interest")
        print("9. Compound interest")
        print("10.Fibonacci Sequence")
        print("11.Guessing Game")
        print("12.Equation")
        print(f"{fg(135)}#########################################{attr('reset')}")

        
        try:  
            #code for seting up a file to write to  
            if not namefile:
                filename = input(f"{fg(253)}Would you like to write to a file y/n ? {attr('reset')}")
                if filename == "y":
                        filename = input("Enter filename : ")
                        validate_filename(filename)
                        namefile = True
                elif filename == "n":
                        namefile = False 
                else:
                        namefile = False           

            #setup for validation for input   
            choice =  input(f"{fg(253)}Please choose a function to calculate,'q' to quit : {attr('reset')}")
        
            if choice.lower() == 'q': raise KeyboardInterrupt
        
            if not choice.isdigit(): raise ValueError("Please enter a number")

            value = int(choice)
            values = range(1,13)
            if value not in values : raise ValueError("Selected item not on menu")

            with open(f'{filename}', 'a') as f:  
                #call the function from the global function stack
                globals()[choices[value-1][1]](f)
                input("Press a key to continue...")

        except ValueError as e:
            print("Invalid input " + str(e))
            input("Press a key to continue...")
        
        except SyntaxError as e:
            print("Invalid format try 2*x + 6*y - 10*z " + str(e))
            input("Press a key to continue...")

        except FileNotFoundError as e:
            print("File format issue " + str(e))
            input("Press a key to continue...")
            

except KeyboardInterrupt:
    print(f"{fg('white')}{bg('yellow')}********* Thanks for using Calcy ********{attr('reset')}")    

    
# Calculator interface
# 1. Addition
# 2. Subraction
# 3. Multiplication
# 4. Division
# 5. Squared
# 6. Cubed
# 7. To the power
# 8. Simple interest
# 9. Complex interest
# Please choose a function to calculate








