from SpAlgo import F32bit, F64bit

# this is the knapsack algorithm.

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

# example of binary sequence of 32bits and 64bits
bin_seq_32bit = '00000100010001000100010010111010'
bin_seq_64bit = '0000010001000100010000001000100010001000100101110100010010111010'
""" 
    passing information to the class "F32bit" or "F64bit":
      * binary_sequence : The function for which we are trying to approximate a solution f(x)=0.
"""
f32bit = F32bit(bin_seq_32bit)
f64bit = F64bit(bin_seq_64bit)

""" get floating points as outputs"""
float_32 = f32bit.get_floating_point()
float_64 = f64bit.get_floating_point()

"""
you can also get the values below:
  * get_exponent(): returns calculated exponent
  * get_significand(): returns calculated significand
"""

# we print to see the result
print('--------- F32bit & F64bit Algorithm ---------')


# printing the result
print('Calculated floating point of 32-bits binary sequence is' + BOLD_START + ORANGE_COLOR, float_32, NORM)
print('Calculated floating point of 64-bits binary sequence is' + BOLD_START + ORANGE_COLOR, float_64, NORM)