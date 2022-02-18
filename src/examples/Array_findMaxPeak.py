from SpAlgo import Array

# find max peak inside a list of numbers.

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
    and call the function `findMaxPeak()`
"""
arrayPeak = Array(data_sequence)

# getting found peak, and its index from findPeak() function
result = arrayPeak.findMaxPeak()

peak = result[0]
peak_index = result[1]

# we print to see the result
print('--------- Find Max Peak Inside An Array ---------')

# printing the data sequence
print('data sequence', '->', BOLD_START, data_sequence, NORM)

# printing the result
print('The result of findMaxPeak is', BOLD_START + ORANGE_COLOR, peak, NORM, 'and its index is',
      BOLD_START + ORANGE_COLOR, peak_index, NORM)