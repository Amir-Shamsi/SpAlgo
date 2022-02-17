from SpAlgo import Matrix

# find a peak in a given m * n matrix

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

# example of a given matrix

input_matrix = [[2, 4, 1, 7, 8],
                [4, 7, 2, 1, 9],
                [6, 12, 21, 3, 5],
                [8, 10, 2, 20, 1]]

'''
    pass it into 'Matrix' class inside 'Matrix.py' and store
    result in `matrix` variable
'''

matrixPeak = Matrix.Matrix(input_matrix)

# get peak from matrixPeak

peak = matrixPeak.findPeak()

# get all peaks from matrixPeak

allPeaks = matrixPeak.findAllPeak()

# we print to see the result
print('--------- Find A Peak Inside A Matrix ---------')

# print results
print('a found Peak in matrix is:', BOLD_START + ORANGE_COLOR, peak, NORM)




