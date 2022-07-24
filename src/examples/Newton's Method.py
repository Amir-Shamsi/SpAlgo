from SpAlgo import Newton

# this is the knapsack algorithm.

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

# example of function and its derivative
function = lambda x: x**3 - x**2 - 1
der_function = lambda x: 3*x**2 - 2*x


""" 
    passing information to the "Newton" class:
      * function : Function for which we are searching for a solution f(x)=0.
      * derivative_function : Derivative of f(x).
"""
newton = Newton(function, der_function)

""" Let's test our function newton on the polynomial  to approximate the super golden ratio. """
approx, iter_count = newton.solve(x0=1, epsilon=1e-10, max_iter=10)

"""
    Return Value
    ------------
    the return value is a tuple of:
      * first value: Found solution
      * second value: Iteration count of found solution
"""

# we print to see the result
print('--------- Newton Algorithm ---------')


# printing the result
print('Found solution after' + BOLD_START + ORANGE_COLOR,
      iter_count, NORM + 'iterations is' + BOLD_START + ORANGE_COLOR, approx, NORM)