from SpAlgo import ClosestPair, Point
# this is the ClosestPair algorithm.

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

"""
example of the set of the points. the set items can define as a:
    * list  -> e.g. [[-1, 2], [5, 0]]
    * tuple -> e.g. [(-1, 2), (5, 0)]
    * Point -> e.g. [Point(-1, 2), Point(5, 0)]
     
"""
points_set = [(7, -2), (11, 0),
              (-50, 20), (-20, 1),
              (0, 10), (3, -8)]
""" 
enter set inside the "ClosestPair" class
"""
closest_pair = ClosestPair(points_set)

# getting minimum distance
min_distance = closest_pair.get_min_distance()

"""
getting pairs those have the minimum distance
    OPTIONAL =>
        :argument _type: its default is Point and it will return list of Points otherwise
                         enter types list or tuple
                         
            _type = list  -> e.g. [[7, 0], [11, 0]]
            _type = tuple -> e.g. [(7, 0), (11, 0)]
            _type = Point -> e.g. [Point(7, 0), Point(11, 0)]
"""
pairs = closest_pair.get_closest_pair(_type=Point)

# we print to see the result
print('--------- ClosestPair Algorithm ---------')
# printing the result
print('The minimum distance of the points set is', BOLD_START + ORANGE_COLOR, min_distance, NORM,
      '\nand found the pairs are:\n' + BOLD_START + 'First Point: ' + ORANGE_COLOR +
      '{}, {}'.format(pairs[0].x, pairs[0].y) + NORM +
      BOLD_START + '\nSecond Point: ' + ORANGE_COLOR +'{}, {}'.format(pairs[1].x, pairs[1].y) + NORM)
