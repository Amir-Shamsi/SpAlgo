from SpAlgo import Matrix

# find a peak in a given m * n matrix

# example of a given matrix

input_matrix = [[2, 4, 1, 7, 8],
                [4, 7, 2, 1, 9],
                [6, 12, 21, 3, 5],
                [8, 10, 2, 20, 1]]

"""
    pass it into "Matrix" class inside "Matrix.py" and store
    result in `matrixPeak` variable
"""

matrixPeak = Matrix.Matrix(input_matrix)

# get peak from matrixPeak

peak = matrixPeak.findPeak()

# get all peaks from matrixPeak

allPeaks = matrixPeak.findAllPeak()

# print results

print("The first Peak in matrix base on divide and conquer is :", peak)

print("All peaks in matrix :", allPeaks)



