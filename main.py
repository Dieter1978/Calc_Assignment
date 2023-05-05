from calc_interface import addition, subtraction, multiplication, division, squared, cubed, power, simple, compound
from colored import fg,bg, attr
from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


choices = [ (1,'addition'),
            (2,'subtraction'),
            (3,'multiplication'),
            (4,"division"),
            (5,'squared'),
            (6,'cubed'),
            (7,'power'),
            (8,'simple'),
            (9,'compound')
           
        ]

try:
    while True:
        print(f"{fg('white')}{bg('yellow')}**** Welcome to Calcy the Calculator.****{attr('reset')}")
        print(f"{fg('red')}###########{dt_string}###########{attr('reset')}")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Squared")
        print("6. Cubed")
        print("7. To the power")    
        print("8. Simple interest")
        print("9. Compound interest")
        print(f"{fg('red')}#########################################{attr('reset')}")

        
        try:    
            choice =  input(f"{fg('white')}{bg('yellow')}Please choose a function to calculate,'q' to quit : {attr('reset')}")
        
            if choice.lower() == 'q': raise KeyboardInterrupt
        
            if not choice.isdigit(): raise ValueError("Please enter a number")

            c = int(choice)

            if c > 9: raise ValueError("Selected item not on menu")

              
            globals()[choices[c-1][1]]()
            input("Press a key to continue...")

        except ValueError as e:
            print("Invalid input " + str(e))


     

       
        # calc_interface.addition()

except KeyboardInterrupt:
    print("Thanks for using Calcy")    

    
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








