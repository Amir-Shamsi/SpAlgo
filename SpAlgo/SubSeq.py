from typing import Union

class LongestMax:
    _sequence = None
    _maximum_summation = None
    start_index = -1
    end_index = -1
    """
        :var sequence: sequence of numbers which will be given at first
    """

    def __init__(self, sequence: list[Union[int, float]]):
        """
            The given sequence is a list of type int or float by the
             other word must be a numerical list.

            All list's elements can have different types:
                * float
                * integer
            :param sequence: sequence of numbers which will be given at first
        """
        self.sequence = sequence
