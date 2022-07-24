from SpAlgo import Secant

# this is the knapsack algorithm.

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

# example of function and its derivative
polynomial = lambda x: x**3 - x**2 - 1

""" 
    passing information to the "Secant" class:
      * function : The function for which we are trying to approximate a solution f(x)=0.
"""
secant = Secant(polynomial)

""" Let's test our function with input values for which we know the correct output. Let's find an approximation of the
      super golden ratio: the only real root of the polynomial """
approx = secant.solve(a=1, b=2, N=20)

"""
    Return Value
    ------------
    the return value is Found solution
"""

# we print to see the result
print('--------- Secant Algorithm ---------')


# printing the result
print('Found solution is' + BOLD_START + ORANGE_COLOR, approx, NORM)