from sympy import symbols, solve, Eq, parse_expr
import re

x,y,z = symbols('x y z')

class Equation:
    def __init__(self):
        pass

    def __call__(self,expr,a,b,c):
       expression = parse_expr(expr)
       return expression.subs(x,a).subs(y,b).subs(z,c)
    



# expr = '2*x + y'

# e(expr)

# print(e)
# x,y = symbols('x y')


# expr =  2*x+y
# expr.subs(x, 2)
