from SpAlgo import SubSeq

# find maximum value of longest subsequence in a list of numbers.

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

# example of sequence of numerical data
data_sequence = [-1, 3, -2.2, 5, 2, 12.1, -23, 4, 8, 6.5, 4, -10, 12, 15]


""" 
    passing it into the "longestMax()" function inside "SubSeq"
    and storing the result into the variable `result`
"""
longestMax = SubSeq.LongestMax(data_sequence)

# getting maximum sum from result
maximum_summation = longestMax.maximum_sum()

"""
    getting the start and end index from `longestMax` will looks like
    this:
    indexes -> (start index, end index)
"""
# extract the indexes into the separated variables
start_index = longestMax.start_index
end_index = longestMax.end_index

# get subsequence
subsequence = longestMax.subsequence()

