
       
def add(x,y):
        return x+y
    
def subtract(x,y):
        return x - y
       
    
def multiply(x,y):
        return x*y
    
def divide(x,y):
        return x/y
    
def square(x):
        return x*x
    
def cube(x):
        return x*x*x
    
def square_root(x):
        return x**0.5
    
def simple_interest(x,y,z):
        return (x*y*z) / 100
    
def compound_interest(x,y,z):
        return x * pow((1 + y/100),z)

def decimal_to_binary(decimal):
        bin_a = bin(decimal)
        bin_string = f"{bin_a}"
        return bin_string[2:]

def decimal_to_hex(decimal):
        hex_a = hex(decimal)
        hex_string = f"{hex_a}"
        return hex_string

# def fibonacci_of(num):
#         if num in cache:
#                 return cache[num]
        
#         cache[num] = fibonacci_of(num-1) + fibonacci_of(num - 2)
#         return cache[num]
    

    
