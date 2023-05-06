from sympy import symbols

x, y = symbols('x y')

expr = 2*x + y

print(expr.subs(x,2))


