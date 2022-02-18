from SpAlgo import Array

# find a peak inside a list of numbers.

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

# example of sequence of numerical data
data_sequence = [1, 4, 1.8, 6, 2, 12.1, 1, 4, 10.8, 5.5, 4, 10, 12, 1, 0]


""" 
    passing it into the "Array()" class inside "SpAlgo.Array"
    and call the function `findAllPeak()`
"""
arrayPeak = Array(data_sequence)

# getting found peak, and its index from findAllPeak() function
result = arrayPeak.findAllPeaks()
"""
result is a list of tuples which is in the following form:
    * (peak, index)
as you see the first element is the peak and the second one
is the index of that peak 
"""

# we print to see the result
print('--------- Find All Peaks Inside An Array ---------')

# printing the data sequence
print('data sequence', '->', BOLD_START, data_sequence, NORM)

# printing the result
print('The result of findAllPeak is:', BOLD_START + ORANGE_COLOR, result, NORM)