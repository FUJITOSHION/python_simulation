from sympy import *

var("x")
equation = Eq(x**3 + 2 * x**2 - 5 * x - 6, 0)
answer = solve(equation)
print(answer)
